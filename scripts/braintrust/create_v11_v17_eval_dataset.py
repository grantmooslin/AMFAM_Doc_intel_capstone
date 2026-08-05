"""
Build a Braintrust evaluation dataset from the union of failed classifications
across prompt versions v11-v17 (v11, v11.5-v11.9, v12, v13, v14, v15, v16, v17).

Guarantees:
- NO duplicate entries: exactly one row per unique filename across all source
  experiments (a sample that failed under multiple versions appears once).
- Each row embeds the ACTUAL PNG image as a Braintrust attachment (not just
  metadata), so a new prompt iteration can be evaluated against every failure.
- Rows carry the reasoning trace, the source experiment, every version that
  failed on the image, and that version's predicted label.

Every experiment whose prompt version resolves to a value in TARGET_PV is
included (all models that ran those versions, e.g. qwen3.7-flash, gemini, kimi,
qwen3.5), so persistent failures across slices (160 v1/v2/v3, 320, 480) and
dedicated *_eval sets are all captured. The dataset is rebuilt idempotently
(deleted and recreated). Run with --dry-run to preview without writing.

Usage:
    python scripts/braintrust/create_v11_v17_eval_dataset.py
    python scripts/braintrust/create_v11_v17_eval_dataset.py --dry-run
    python scripts/braintrust/create_v11_v17_eval_dataset.py --dataset custom_name
    python scripts/braintrust/create_v11_v17_eval_dataset.py --versions "v13 v14 v15"
    python scripts/braintrust/create_v11_v17_eval_dataset.py --skip-experiment kimi-k2.6_v11_8_reasoning_160
"""

import argparse
import base64
import hashlib
import json
import os
import sys
import time
from collections import Counter
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import braintrust

from src.braintrust_config import load_braintrust_config
from src.braintrust_utils import (
    delete_dataset_by_name,
    fetch_experiment_rows,
    find_misses,
    index_span_metadata,
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

# Prompt versions (as resolved from experiment metadata) that feed the eval set.
TARGET_PV = {
    "v11", "v11.5", "v11.6", "v11.7", "v11.8", "v11.9",
    "v12", "v13", "v14", "v15", "v16", "v17",
}

# Experiments to always skip (aborted / partial / noise).
SKIP_EXPERIMENTS_DEFAULT = {
    "kimi-k2.6_v11_8_reasoning_160",
    "kimi-k2.6_v11_8_reasoning_160-1b34955a",
}

REASONING_LIMIT = 4000


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

    Preference: non-empty reasoning > longer reasoning > alphabetically first
    experiment. Also record every version/experiment that missed this image.
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
        versions = sorted({r["prompt_version"] for r in recs})
        predictions = {r["prompt_version"]: r["predicted"] for r in recs}

        primary["also_missed_by"] = also
        primary["versions"] = versions
        primary["predictions"] = predictions
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
    """Turn deduped records into (row_id, row) pairs ready for insertion.

    Each row embeds the real PNG as a Braintrust attachment plus metadata that
    records which versions failed on the image and what each predicted.
    """
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
        versions = rec.get("versions", [])
        predictions = rec.get("predictions", {})

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
                    "versions": versions,
                },
            },
            "expected": rec["expected"],
            "metadata": {
                "prompt_version": rec["prompt_version"],
                "source_experiment": rec["experiment"],
                "versions": versions,
                "predictions": predictions,
                "also_missed_by": also if also else None,
                "predicted": rec["predicted"],
                "misclassification": f"{rec['expected']} -> {rec['predicted']}",
                "reasoning": reasoning or None,
            },
        }))

    if missing:
        print(f"WARNING: skipped {missing} records (image not in any slice dataset)", file=sys.stderr)
    return rows


def upload_rows(config, api_key: str, dataset_name: str, rows: list[tuple[str, dict]]) -> None:
    """Delete any existing dataset and insert rows into a fresh one."""
    deleted = delete_dataset_by_name(api_key, config.project_id, dataset_name, config.api_base)
    if deleted:
        print(f"Deleted existing dataset {dataset_name} ({deleted})")

    braintrust.login(api_key=api_key, force_login=True)
    dataset = braintrust.init_dataset(project_id=config.project_id, name=dataset_name)

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
    print(f"\nDataset ready: {dataset_name} ({len(rows)} rows)")


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
    for exp, cnt in by_exp.most_common(25):
        print(f"  {exp:<55} {cnt}")
    print("By expected class:")
    for cls in sorted(by_class):
        print(f"  {cls:<24} {by_class[cls]}")


def save_records_cache(path: str, records: list[dict]) -> None:
    """Persist deduped records as JSON so re-runs can skip experiment fetching."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    serializable = []
    for r in records:
        item = dict(r)
        item["also_missed_by"] = sorted(r.get("also_missed_by", []))
        item["versions"] = sorted(r.get("versions", []))
        item["predictions"] = dict(r.get("predictions", {}))
        serializable.append(item)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=2)
    print(f"Saved {len(serializable)} records to {path}")


def load_records_cache(path: str) -> list[dict]:
    """Load records previously persisted by save_records_cache."""
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)
    print(f"Loaded {len(records)} records from cache {path}")
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env-file", default="braintrust.env")
    parser.add_argument("--dataset", default="qwen_misclassification_eval_v11_v17",
                        help="Name of the dataset to create (default: qwen_misclassification_eval_v11_v17)")
    parser.add_argument("--versions", default=None,
                        help="Space-separated prompt versions to include (overrides v11-v17 default)")
    parser.add_argument("--skip-experiment", action="append", default=[],
                        help="Experiment name to exclude (may repeat)")
    parser.add_argument("--cache", default=None,
                        help="Path to a records JSON cache; loads it instead of fetching experiments if it exists, "
                             "and always writes it after collection")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    config = load_braintrust_config(args.env_file)
    api_key = config.api_key or os.environ.get("BRAINTRUST_API_KEY")
    if not api_key:
        sys.exit("Error: BRAINTRUST_API_KEY not set")

    skip = SKIP_EXPERIMENTS_DEFAULT | set(args.skip_experiment)
    target_pvs = set(args.versions.split()) if args.versions else set(TARGET_PV)

    print(f"Environment: org {config.org_id} / project {config.project_name} ({config.project_id})")
    print(f"Target prompt versions: {sorted(target_pvs)}")
    print(f"Skip experiments: {sorted(skip)}")
    print(f"Slice datasets: {SLICE_DATASETS}")
    print(f"Eval dataset: {args.dataset}")

    if args.cache and os.path.exists(args.cache):
        deduped = load_records_cache(args.cache)
        print_summary(deduped)
    else:
        experiments = discover_pv_experiments(api_key, config.project_id, config.api_base, target_pvs, skip)
        print(f"\nDiscovered {len(experiments)} experiments:")
        for e in experiments:
            print(f"  {e['name']}  (pv={resolve_prompt_version(e)}, id={e['id'][:12]})")

        records = collect_misses(api_key, experiments, config.api_base)
        deduped = dedupe_by_filename(records)
        print_summary(deduped)

        if args.cache:
            save_records_cache(args.cache, deduped)

    if args.dry_run:
        print("\nDry run — no dataset created.")
        return

    if not deduped:
        sys.exit("No misclassifications to include.")

    images = load_images_by_filename(config, api_key, SLICE_DATASETS)
    rows = build_rows(deduped, images)
    if not rows:
        sys.exit("No rows could be built (all source images missing).")

    print(f"\nUploading {len(rows)} rows to {args.dataset}...")
    upload_rows_with_retry(config, api_key, args.dataset, rows)

    per_version = Counter(r["prompt_version"] for r in deduped)
    print(f"Uploaded {len(rows)} rows across {len(per_version)} prompt versions to {args.dataset}.")


def upload_rows_with_retry(config, api_key: str, dataset_name: str, rows: list[tuple[str, dict]],
                           retries: int = 3, wait: int = 60) -> None:
    """Upload rows, retrying on transient network failures (e.g. S3 timeouts).

    The dataset is rebuilt idempotently (deleted and recreated) each attempt, so
    a partial failure leaves no half-written dataset behind.
    """
    for attempt in range(1, retries + 1):
        try:
            upload_rows(config, api_key, dataset_name, rows)
            return
        except Exception as exc:  # noqa: BLE001 - retry transient failures
            if attempt == retries:
                raise
            print(f"Upload attempt {attempt} failed ({exc}); retrying in {wait}s...", file=sys.stderr)
            time.sleep(wait)


if __name__ == "__main__":
    main()
