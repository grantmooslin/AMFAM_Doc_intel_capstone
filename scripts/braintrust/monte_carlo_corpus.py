"""Build the joint Monte Carlo corpus from every eval manifest.

Aggregates every ``reports/manifests/*.jsonl`` checkpoint into one flat JSONL
corpus, one record per scored row, with the run-level context (model, prompt
version, dataset, temperature, reasoning effort) lifted from each manifest
header. Optionally backfills the full reasoning trace + finish_reason/fallback
from Braintrust span metadata (read-only data fetch, no scorer credits) for rows
where it is not already present.

The corpus is the single input to the ``monte_carlo_*`` scripts; keep it cached
(``--cache``) and rebuild idempotently (``--rebuild``).

Usage:
    python scripts/braintrust/monte_carlo_corpus.py
    python scripts/braintrust/monte_carlo_corpus.py --no-backfill
    python scripts/braintrust/monte_carlo_corpus.py --rebuild
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # noqa: E402

from src.constants import DOCUMENT_CLASSES  # noqa: E402
from src.braintrust_config import load_braintrust_config  # noqa: E402
from src.braintrust_utils import fetch_experiment_rows, list_experiments  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFESTS_DIR = ROOT / "reports" / "manifests"
DEFAULT_CORPUS = ROOT / "reports" / "monte_carlo" / "corpus.jsonl"

VALID_CLASSES = set(DOCUMENT_CLASSES)
REASONING_PLACEHOLDER = "(reasoning not exposed by model)"


def _canonical_braintrust_config():
    """Braintrust config honoring ``braintrust.env`` as the single source of truth."""
    from dotenv import dotenv_values

    bt_env = dotenv_values("braintrust.env")
    saved: dict[str, str | None] = {}
    for key, value in bt_env.items():
        if value is None:
            continue
        saved[key] = os.environ.get(key)
        os.environ[key] = value
    try:
        return load_braintrust_config()
    finally:
        for key, old in saved.items():
            if old is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = old


def load_manifest(path: Path) -> tuple[dict, dict[str, dict]]:
    """Return (header_metadata, {filename: last_record}) from a manifest JSONL.

    Mirrors ``score_manifest.load_manifest``: the first line is a run header and
    later lines are append-only row states with the last state per filename being
    authoritative. Tags are derived in-memory when absent.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    header = json.loads(lines[0])
    final: dict[str, dict] = {}
    for line in lines[1:]:
        if not line.strip():
            continue
        record = json.loads(line)
        if "tag" not in record:
            if record.get("status") != "completed":
                record["tag"] = "ERROR!"
            elif (record.get("predicted") or "").strip().lower() == \
                    (record.get("expected") or "").strip().lower():
                record["tag"] = "OK"
            else:
                record["tag"] = "MISS!"
        final[record["filename"]] = record
    return header.get("metadata", {}), final


def fetch_span_metadata_by_filename(
    experiment_name: str,
    project_id: str,
    api_key: str,
    api_base: str,
) -> dict[str, dict]:
    """Fetch reasoning/finish_reason/fallback/cost for every matching experiment.

    The resume loop relaunches evals under the same experiment name with a
    version suffix (``-34646987``), so both the exact name and any ``<name>-*``
    versions are merged, preferring the first non-empty reasoning / first present
    value per filename. Returns ``{filename: {reasoning, finish_reason, fallback,
    cost, runner_up}}``.
    """
    meta_by_filename: dict[str, dict] = {}
    try:
        experiments = list_experiments(api_key, project_id, api_base)
    except Exception as exc:  # noqa: BLE001 - backfill must never abort the build
        print(f"WARNING: could not list experiments for backfill: {exc}", file=sys.stderr)
        return meta_by_filename
    prefix = experiment_name + "-"
    matching = [e for e in experiments if e.get("name") == experiment_name
                or str(e.get("name", "")).startswith(prefix)]
    if not matching:
        return meta_by_filename
    for exp in matching:
        try:
            events = fetch_experiment_rows(api_key, exp["id"], api_base)
        except Exception as exc:  # noqa: BLE001 - skip one broken experiment
            print(f"WARNING: could not fetch experiment {exp['id']} for backfill: {exc}",
                  file=sys.stderr)
            continue
        for event in events:
            meta = event.get("metadata") or {}
            input_data = event.get("input")
            input_filename = ""
            if isinstance(input_data, dict):
                input_filename = input_data.get("filename") or ""
            filename = meta.get("filename") or input_filename
            if not filename:
                continue
            entry = meta_by_filename.setdefault(filename, {})
            reasoning = meta.get("reasoning")
            if reasoning and reasoning != REASONING_PLACEHOLDER and "reasoning" not in entry:
                entry["reasoning"] = reasoning
            for field in ("finish_reason", "fallback"):
                value = meta.get(field)
                if value is not None and field not in entry:
                    entry[field] = value
            for field in ("cost", "runner_up"):
                value = meta.get(field)
                if value and field not in entry:
                    entry[field] = value
    return meta_by_filename


def build_corpus(manifests_dir: Path, backfill: bool) -> list[dict]:
    """Read every manifest and (optionally) backfill reasoning from Braintrust."""
    manifests = sorted(manifests_dir.glob("*.jsonl"))
    if not manifests:
        print(f"No manifests found in {manifests_dir}", file=sys.stderr)
        return []

    config = None
    if backfill:
        config = _canonical_braintrust_config()

    records: list[dict] = []
    for manifest_path in manifests:
        metadata, final = load_manifest(manifest_path)
        experiment_name = metadata.get("experiment_name") or manifest_path.stem
        span_meta: dict[str, dict] = {}
        if backfill and experiment_name and config:
            span_meta = fetch_span_metadata_by_filename(
                experiment_name,
                config.project_id,
                config.api_key or "",
                config.api_base,
            )
            if span_meta:
                print(f"Backfilled span metadata for {len(span_meta)} rows from {experiment_name}")

        for record in final.values():
            filename = record.get("filename") or ""
            expected = record.get("expected") or ""
            predicted = record.get("predicted") or ""
            status = record.get("status") or "empty"
            span = span_meta.get(filename, {})
            reasoning = record.get("reasoning") or span.get("reasoning") or ""
            if reasoning == REASONING_PLACEHOLDER:
                reasoning = ""
            if predicted.strip().lower() in VALID_CLASSES and status == "completed":
                confusion_pair = f"{expected}->{predicted.strip().lower()}" if expected else ""
            else:
                confusion_pair = ""
            records.append({
                "filename": filename,
                "expected": expected,
                "model": metadata.get("model") or "",
                "prompt_version": metadata.get("prompt_version") or "",
                "dataset": metadata.get("dataset") or "",
                "experiment_name": experiment_name,
                "predicted": predicted.strip().lower() if predicted else "",
                "runner_up": (record.get("runner_up") or span.get("runner_up") or "").strip().lower(),
                "status": status,
                "tag": record.get("tag") or ("OK" if predicted and predicted.strip().lower() == expected.strip().lower() else "MISS!"),
                "cost": record.get("cost") if isinstance(record.get("cost"), (int, float)) else (span.get("cost") if isinstance(span.get("cost"), (int, float)) else None),
                "attempts": record.get("attempts"),
                "error": record.get("error") or "",
                "fallback": span.get("fallback", record.get("fallback")),
                "finish_reason": span.get("finish_reason"),
                "reasoning": reasoning,
                "reasoning_len": len(reasoning),
                "max_tokens": metadata.get("max_tokens"),
                "temperature": metadata.get("temperature"),
                "reasoning_effort": metadata.get("reasoning_effort"),
                "confusion_pair": confusion_pair,
            })
    return records


def summarize(records: list[dict]) -> dict:
    """Aggregate corpus-level stats for the console and the summary file."""
    statuses = Counter(r["status"] for r in records)
    tags = Counter(r["tag"] for r in records)
    models = Counter(r["model"] for r in records)
    prompts = Counter(r["prompt_version"] for r in records)
    datasets = Counter(r["dataset"] for r in records)
    experiments = Counter(r["experiment_name"] for r in records)
    images = Counter(r["filename"] for r in records)
    reasoning_coverage = sum(1 for r in records if r["reasoning_len"] > 0)
    pairs = Counter(r["confusion_pair"] for r in records if r["confusion_pair"])
    return {
        "records": len(records),
        "images": len(images),
        "experiments": len(experiments),
        "statuses": dict(statuses),
        "tags": dict(tags),
        "models": dict(models),
        "prompts": dict(prompts),
        "datasets": dict(datasets),
        "reasoning_coverage": reasoning_coverage,
        "top_confusion_pairs": pairs.most_common(20),
    }


def print_summary(stats: dict) -> None:
    print("\nCorpus summary")
    print(f"  records:       {stats['records']} across {stats['images']} images")
    print(f"  experiments:   {stats['experiments']}")
    print(f"  statuses:      {stats['statuses']}")
    print(f"  tags:          {stats['tags']}")
    print(f"  models:        {dict(stats['models'])}")
    print(f"  prompts:       {dict(stats['prompts'])}")
    print(f"  datasets:      {dict(stats['datasets'])}")
    print(f"  reasoning:     {stats['reasoning_coverage']}/{stats['records']} rows have a trace")
    if stats["top_confusion_pairs"]:
        print("  top confusions:")
        for pair, count in stats["top_confusion_pairs"]:
            print(f"    {pair:<40} {count}")


def write_markdown_summary(stats: dict, path: Path) -> None:
    lines = [
        "# Monte Carlo Corpus Summary",
        "",
        f"- **Records**: {stats['records']}",
        f"- **Images**: {stats['images']}",
        f"- **Experiments**: {stats['experiments']}",
        f"- **Reasoning coverage**: {stats['reasoning_coverage']}/{stats['records']} rows",
        "",
        "## Status",
        "",
        "| status | count |",
        "|---|---:|",
    ]
    for status, count in sorted(stats["statuses"].items()):
        lines.append(f"| {status} | {count} |")
    lines += ["", "## Models", "", "| model | rows |", "|---|---:|"]
    for model, count in sorted(stats["models"].items()):
        lines.append(f"| {model} | {count} |")
    lines += ["", "## Prompt versions", "", "| prompt | rows |", "|---|---:|"]
    for prompt, count in sorted(stats["prompts"].items()):
        lines.append(f"| {prompt} | {count} |")
    lines += ["", "## Top confusion pairs", "", "| expected->predicted | count |", "|---|---:|"]
    for pair, count in stats["top_confusion_pairs"]:
        lines.append(f"| `{pair}` | {count} |")
    lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Summary saved: {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifests-dir", type=Path, default=DEFAULT_MANIFESTS_DIR,
                        help=f"Directory of eval manifests (default: {DEFAULT_MANIFESTS_DIR})")
    parser.add_argument("--cache", type=Path, default=DEFAULT_CORPUS,
                        help=f"Corpus JSONL output (default: {DEFAULT_CORPUS})")
    parser.add_argument("--rebuild", action="store_true",
                        help="Rebuild even if the cache already exists")
    parser.add_argument("--no-backfill", action="store_true",
                        help="Skip fetching reasoning/finish_reason from Braintrust spans")
    args = parser.parse_args()

    if args.cache.exists() and not args.rebuild:
        records = []
        for line in args.cache.read_text(encoding="utf-8").splitlines():
            if line.strip():
                records.append(json.loads(line))
        print(f"Loaded {len(records)} records from existing corpus {args.cache} "
              f"(pass --rebuild to rebuild)")
        stats = summarize(records)
        print_summary(stats)
        return

    records = build_corpus(args.manifests_dir, backfill=not args.no_backfill)
    if not records:
        sys.exit("No records built; nothing to write.")

    args.cache.parent.mkdir(parents=True, exist_ok=True)
    args.cache.write_text(
        "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
        encoding="utf-8",
    )
    print(f"Corpus saved: {args.cache} ({len(records)} records)")

    stats = summarize(records)
    print_summary(stats)
    write_markdown_summary(stats, args.cache.with_suffix(".summary.md"))


if __name__ == "__main__":
    main()
