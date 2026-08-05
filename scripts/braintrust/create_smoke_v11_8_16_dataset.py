"""
Build a Braintrust smoke-test dataset from every misclassification across ALL
v11.8 and v16 prompt-version experiments.

Key guarantees:
- NO repeated images: exactly one row per unique filename across all experiments.
- Failed reasoning samples cover every 160-image slice (v1/v2/v3/320/480).
- Each row carries the reasoning trace, the source experiment, and a list of
  every other experiment that also misclassified the same image.

Usage:
    python scripts/braintrust/create_smoke_v11_8_16_dataset.py
    python scripts/braintrust/create_smoke_v11_8_16_dataset.py --dry-run
    python scripts/braintrust/create_smoke_v11_8_16_dataset.py --dataset custom_name
    python scripts/braintrust/create_smoke_v11_8_16_dataset.py --skip-experiment kimi-k2.6_v11_8_reasoning_160
"""

import argparse
import base64
import hashlib
import json
import os
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import braintrust
import requests

from src.braintrust_config import load_braintrust_config
from src.braintrust_utils import (
    delete_dataset_by_name,
    fetch_experiment_rows,
    find_misses,
    index_span_metadata,
    list_datasets,
    list_experiments,
    load_braintrust_dataset,
    resolve_prompt_version,
)

# Slice datasets whose images to preload (all v1/v2/v3/320/480 slices).
SLICE_DATASETS = [
    "fixed_size_sampled",
    "fixed_size_sampled_v2",
    "fixed_size_sampled_v3",
    "fixed_size_sampled_320",
    "fixed_size_sampled_480",
]

# Experiments to always skip (aborted / partial / noise).
SKIP_EXPERIMENTS_DEFAULT = {
    "kimi-k2.6_v11_8_reasoning_160",
    "kimi-k2.6_v11_8_reasoning_160-1b34955a",
}

REASONING_LIMIT = 4000


def _v1_api_base(api_base: str) -> str:
    api_base = api_base.rstrip("/")
    return f"{api_base}/v1" if not api_base.endswith("/v1") else api_base


def discover_pv_experiments(api_key: str, project_id: str, api_base: str,
                            prompt_versions: set[str], skip: set[str]) -> list[dict]:
    """Return experiments whose prompt_version matches one of *prompt_versions*."""
    all_exps = list_experiments(api_key, project_id, api_base)
    result = []
    for e in all_exps:
        name = e.get("name", "")
        if name in skip:
            continue
        pv = resolve_prompt_version(e)
        if pv in prompt_versions:
            result.append(e)
    result.sort(key=lambda e: e.get("name", ""))
    return result


def collect_misses(api_key: str, experiments: list[dict], api_base: str) -> list[dict]:
    """Fetch every experiment and return one miss record per unique miss row.

    Each record: {experiment, prompt_version, expected, predicted, filename, reasoning}.
    """
    records: list[dict] = []
    for exp in experiments:
        name = exp["name"]
        eid = exp["id"]
        print(f"Fetching {name}...")
        try:
            rows = fetch_experiment_rows(api_key, eid, api_base)
        except Exception as exc:
            print(f"  SKIP {name}: {exc}", file=sys.stderr)
            continue

        span_meta = index_span_metadata(rows)
        misses = find_misses(rows, span_meta)
        version = resolve_prompt_version(exp)

        # Dedup misses within this experiment by filename (keep longest reasoning).
        seen_in_exp: dict[str, dict] = {}
        for miss in misses:
            fn = miss["filename"]
            prev = seen_in_exp.get(fn)
            if prev is None or len(miss["reasoning"]) > len(prev["reasoning"]):
                seen_in_exp[fn] = miss

        for fn, miss in seen_in_exp.items():
            records.append({
                "experiment": name,
                "prompt_version": version,
                "expected": miss["expected"],
                "predicted": miss["predicted"],
                "filename": fn,
                "reasoning": miss["reasoning"],
            })

        n = len(seen_in_exp)
        print(f"  {name}: {n} unique misclassifications (prompt {version})")
        if n:
            first = list(seen_in_exp.values())[0]
            print(f"    e.g. {first['expected']} -> {first['predicted']} ({first['filename']})")

    return records


def dedupe_by_filename(records: list[dict]) -> list[dict]:
    """Keep exactly ONE record per filename across ALL experiments.

    Preference: non-empty reasoning > longer reasoning > alphabetically first experiment.
    Also record every experiment that missed this image in 'also_missed_by'.
    """
    buckets: dict[str, list[dict]] = {}
    for r in records:
        buckets.setdefault(r["filename"], []).append(r)

    kept: list[dict] = []
    skipped_dup = 0
    for filename, recs in sorted(buckets.items()):
        # Sort: non-empty reasoning first, then longest reasoning, then exp name.
        recs.sort(key=lambda r: (bool(r["reasoning"]), len(r["reasoning"]), r["experiment"]))
        primary = recs[-1]  # last = best after sort
        also = sorted({r["experiment"] for r in recs} - {primary["experiment"]})

        primary["also_missed_by"] = also
        kept.append(primary)
        skipped_dup += len(recs) - 1

    print(f"\nDeduped: {len(records)} raw → {len(kept)} unique filenames ({skipped_dup} duplicates removed)")
    return kept


def load_images_by_filename(config, api_key: str, slice_datasets: list[str]) -> dict[str, bytes]:
    """Download source images from every slice dataset, keyed by filename."""
    source_key = config.data_api_key or None
    by_filename: dict[str, bytes] = {}
    for ds_name in slice_datasets:
        print(f"Loading images from {ds_name}...")
        try:
            recs = load_braintrust_dataset(
                config.dataset_project, ds_name,
                dataset_api_key=source_key, org_id=config.org_id, api_base=config.api_base,
            )
            for rec in recs:
                by_filename.setdefault(rec["filename"], base64.b64decode(rec["image_b64"]))
            print(f"  {ds_name}: {len(recs)} records ({sum(1 for r in recs if r['filename'] in by_filename)} new)")
        except Exception as exc:
            print(f"  SKIP {ds_name}: {exc}", file=sys.stderr)

    print(f"Total unique images across {len(slice_datasets)} slices: {len(by_filename)}")
    return by_filename


def build_rows(records: list[dict], images: dict[str, bytes]) -> list[tuple[str, dict]]:
    """Turn deduped records into (row_id, row) pairs ready for insertion."""
    rows: list[tuple[str, dict]] = []
    missing = 0
    for rec in records:
        filename = rec["filename"]
        image_bytes = images.get(filename)
        if image_bytes is None:
            missing += 1
            print(f"  SKIP {rec['expected']:<24} {filename}: not in any slice dataset", file=sys.stderr)
            continue

        row_id = hashlib.md5(f"{filename}".encode("utf-8")).hexdigest()
        reasoning = (rec.get("reasoning") or "")[:REASONING_LIMIT]
        also = rec.get("also_missed_by", [])

        rows.append((row_id, {
            "input": {
                "image": braintrust.Attachment(
                    data=image_bytes,
                    filename=filename,
                    content_type="image/png",
                ),
                "filename": filename,
                "metadata": {
                    "prompt_version": rec["prompt_version"],
                    "source_experiment": rec["experiment"],
                },
            },
            "expected": rec["expected"],
            "metadata": {
                "prompt_version": rec["prompt_version"],
                "source_experiment": rec["experiment"],
                "also_missed_by": also if also else None,
                "predicted": rec["predicted"],
                "misclassification": f"{rec['expected']} -> {rec['predicted']}",
                "reasoning": reasoning or None,
            },
        }))

    if missing:
        print(f"WARNING: skipped {missing} records (image not in any slice dataset)", file=sys.stderr)
    return rows


def upload_rows(config, api_key: str, rows: list[tuple[str, dict]]) -> None:
    """Delete any existing dataset and insert rows into a fresh one."""
    deleted = delete_dataset_by_name(api_key, config.project_id, config.smoke_dataset, config.api_base)
    if deleted:
        print(f"Deleted existing dataset {config.smoke_dataset} ({deleted})")

    braintrust.login(api_key=api_key, force_login=True)
    dataset = braintrust.init_dataset(project_id=config.project_id, name=config.smoke_dataset)

    for i, (row_id, row) in enumerate(rows):
        dataset.insert(
            input=row["input"],
            expected=row["expected"],
            metadata=row["metadata"],
            id=row_id,
        )
        if (i + 1) % 25 == 0 or (i + 1) == len(rows):
            print(f"  Inserted {i + 1}/{len(rows)} rows...")

    dataset.flush()
    print(f"\nDataset ready: {config.smoke_dataset} ({len(rows)} rows)")


def print_summary(records: list[dict]) -> None:
    by_version = Counter(r["prompt_version"] for r in records)
    by_exp = Counter(r["experiment"] for r in records)
    by_class = Counter(r["expected"] for r in records)

    print("\n--- Summary ---")
    print(f"Total unique misclassifications: {len(records)}")
    print("By prompt version:")
    for version in sorted(by_version):
        print(f"  {version:<8} {by_version[version]}")
    print("By experiment (raw before dedup):")
    for exp, cnt in by_exp.most_common(20):
        print(f"  {exp:<55} {cnt}")
    print("By expected class:")
    for cls in sorted(by_class):
        print(f"  {cls:<24} {by_class[cls]}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env-file", default="braintrust.env")
    parser.add_argument("--dataset", default=None,
                        help="Override smoke dataset name (default: qwen_misclassification_smoke_v11_8+16)")
    parser.add_argument("--skip-experiment", action="append", default=[],
                        help="Experiment name to exclude (may repeat)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    config = load_braintrust_config(args.env_file)
    api_key = config.api_key or os.environ.get("BRAINTRUST_API_KEY")
    if not api_key:
        sys.exit("Error: BRAINTRUST_API_KEY not set")

    smoke_name = args.dataset or "qwen_misclassification_smoke_v11_8+16"
    config = replace(config, smoke_dataset=smoke_name)

    skip = SKIP_EXPERIMENTS_DEFAULT | set(args.skip_experiment)
    target_pvs = {"v11.8", "v16"}

    print(f"Environment: org {config.org_id} / project {config.project_name} ({config.project_id})")
    print(f"Target prompt versions: {sorted(target_pvs)}")
    print(f"Skip experiments: {sorted(skip)}")
    print(f"Slice datasets: {SLICE_DATASETS}")
    print(f"Smoke dataset: {smoke_name}")

    experiments = discover_pv_experiments(api_key, config.project_id, config.api_base, target_pvs, skip)
    print(f"\nDiscovered {len(experiments)} experiments:")
    for e in experiments:
        print(f"  {e['name']}  (pv={resolve_prompt_version(e)}, id={e['id'][:12]})")

    records = collect_misses(api_key, experiments, config.api_base)
    deduped = dedupe_by_filename(records)
    print_summary(deduped)

    if args.dry_run:
        print("\nDry run — no dataset created.")
        return

    if not deduped:
        sys.exit("No misclassifications to include.")

    images = load_images_by_filename(config, api_key, SLICE_DATASETS)
    rows = build_rows(deduped, images)
    if not rows:
        sys.exit("No rows could be built (all source images missing).")

    print(f"\nUploading {len(rows)} rows to {smoke_name}...")
    upload_rows(config, api_key, rows)

    per_version = Counter(r["prompt_version"] for r in deduped)
    print(f"Uploaded {len(rows)} rows across {len(per_version)} prompt versions to {smoke_name}.")


if __name__ == "__main__":
    main()
