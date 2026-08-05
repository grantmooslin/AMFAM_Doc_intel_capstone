"""Score a completed evaluation from its local manifest and save the final numbers.

Computes exact_match, per-class accuracy, failure rate, per-row cost, and
near-miss (runner-up) accuracy directly from the manifest JSONL checkpoint
(``reports/manifests/*.jsonl``) — no Braintrust scorer credits. The manifest
records every row the moment the model returns, so the final result numbers are
always available and savable locally, even if Braintrust score/credit limits cap
out. Errors count as misses (matching ``braintrust_report.py``).

The Braintrust eval tracks ``exact_match``, ``failure``, and ``cost`` scorers;
these same numbers (plus near-miss, which has no Braintrust scorer) are derived
here from the manifest so they are always available locally. Rows are expected
to carry ``status``, ``predicted``, and (on the resilient runner) ``runner_up``
+ ``cost`` fields.

Near-miss/cost tracking: rows recorded with a ``runner_up`` / ``cost`` field
(eval runs on the resilient runner) contribute directly. Rows that predate the
tracking are backfilled from Braintrust span metadata (read-only data fetch, no
scorer credits); pass ``--no-backfill`` to skip.

Writes ``<manifest-stem>_final.json`` and ``<manifest-stem>_final.md`` into
``--output-dir`` (default ``reports/experiment_reports/``).

Usage:
    python scripts/braintrust/score_manifest.py --manifest reports/manifests/<name>.jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # noqa: E402

from src.constants import DOCUMENT_CLASSES  # noqa: E402
from src.braintrust_config import load_braintrust_config  # noqa: E402
from src.braintrust_utils import fetch_experiment_rows, list_experiments  # noqa: E402
from src.openrouter_classifier import extract_runner_up  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]

REASONING_PLACEHOLDER = "(reasoning not exposed by model)"


def _canonical_braintrust_config():
    """Braintrust config honoring ``braintrust.env`` as the single source of truth.

    ``load_braintrust_config`` loads env files with ``override=False``, so a
    stale value already in ``os.environ`` (e.g. the old API key loaded from
    ``.env`` by ``require_env`` upstream) would shadow ``braintrust.env``.
    Temporarily push ``braintrust.env`` values onto the environment so the
    canonical config wins regardless of what the caller's env carries.
    """
    import os
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
    """Return (header_metadata, {filename: last_record}) from an append-only manifest.

    Every record is guaranteed a ``tag``: ``OK`` (correct), ``MISS!``
    (misclassified), or ``ERROR!`` (failed/empty). Records written before tagging
    shipped are derived in-memory from ``status`` + prediction vs expected.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    header = json.loads(lines[0])
    final: dict[str, dict] = {}
    for line in lines[1:]:
        if line.strip():
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


def fetch_row_metadata_by_filename(
    experiment_name: str,
    project_id: str,
    api_key: str,
    api_base: str = "https://api.braintrust.dev",
) -> dict[str, dict]:
    """Fetch reasoning + cost metadata for every experiment version matching a name.

    The resume loop relaunches the eval under the SAME experiment name, so the
    reasoning/cost for a row lives only in the cycle where it was first completed
    (cached rows in later cycles log nothing). Braintrust appends a version
    suffix (``-34646987``) to repeated names, so both the exact name and any
    ``<name>-*`` versions are merged, preferring the first non-empty reasoning /
    first present cost per filename. Returns ``{filename: {"reasoning": str,
    "cost": float}}``. Read-only data fetch — uses no scorer credits.
    """
    meta_by_filename: dict[str, dict] = {}
    try:
        experiments = list_experiments(api_key, project_id, api_base)
    except Exception as exc:  # noqa: BLE001 - backfill must never abort scoring
        print(f"WARNING: could not list experiments for backfill: {exc}", file=sys.stderr)
        return meta_by_filename
    prefix = experiment_name + "-"
    matching = [e for e in experiments if e.get("name") == experiment_name
                or str(e.get("name", "")).startswith(prefix)]
    if not matching:
        print(f"WARNING: no experiments named '{experiment_name}' found for backfill",
              file=sys.stderr)
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
            filename = meta.get("filename") or (event.get("input") or {}).get("filename")
            if not filename:
                continue
            entry = meta_by_filename.setdefault(filename, {})
            reasoning = meta.get("reasoning")
            if reasoning and reasoning != REASONING_PLACEHOLDER and "reasoning" not in entry:
                entry["reasoning"] = reasoning
            cost = meta.get("cost")
            if isinstance(cost, (int, float)) and "cost" not in entry:
                entry["cost"] = float(cost)
    return meta_by_filename


def backfill_rows(final: dict[str, dict], metadata: dict) -> tuple[int, int, int, int]:
    """Fill missing ``runner_up`` and ``cost`` fields from Braintrust span metadata.

    Rows completed before runner-up/cost tracking shipped have neither field in
    the manifest, but their reasoning traces (which contain the ``Runner-up:``
    line) and billed cost were already logged to Braintrust span metadata.
    Mutates ``final`` in place with a single fetch; returns ``(runner_up
    backfilled, runner_up still missing, cost backfilled, cost still missing)``.
    """
    runner_missing = [r for r in final.values()
                      if r.get("status") == "completed" and not (r.get("runner_up") or "").strip()]
    cost_missing = [r for r in final.values()
                    if r.get("status") == "completed" and not isinstance(r.get("cost"), (int, float))]
    if not runner_missing and not cost_missing:
        return 0, 0, 0, 0
    experiment_name = metadata.get("experiment_name")
    if not experiment_name:
        return 0, len(runner_missing), 0, len(cost_missing)
    config = _canonical_braintrust_config()
    meta_map = fetch_row_metadata_by_filename(
        experiment_name, config.project_id, config.api_key or "", config.api_base
    )
    runner_backfilled = 0
    for r in runner_missing:
        reasoning = meta_map.get(r["filename"], {}).get("reasoning")
        if reasoning:
            r["runner_up"] = extract_runner_up(reasoning)
            runner_backfilled += 1
    cost_backfilled = 0
    for r in cost_missing:
        cost = meta_map.get(r["filename"], {}).get("cost")
        if cost is not None:
            r["cost"] = cost
            cost_backfilled += 1
    return (
        runner_backfilled,
        len(runner_missing) - runner_backfilled,
        cost_backfilled,
        len(cost_missing) - cost_backfilled,
    )


def score(metadata: dict, final: dict[str, dict]) -> dict:
    rows = sorted(final.values(), key=lambda r: (r.get("expected", ""), r.get("filename", "")))
    total = len(rows)
    completed = [r for r in rows if r.get("status") == "completed"]
    errored = [r for r in rows if r.get("status") == "error"]
    empty = [r for r in rows if r.get("status") == "empty"]
    exact = [r for r in completed if (r.get("predicted") or "").strip().lower() == (r.get("expected") or "").strip().lower()]
    misses = [r for r in completed if (r.get("predicted") or "").strip().lower() != (r.get("expected") or "").strip().lower()]
    near_miss = [
        r for r in misses
        if (r.get("runner_up") or "").strip().lower() == (r.get("expected") or "").strip().lower()
    ]

    per_class: dict[str, dict] = {}
    for cls in DOCUMENT_CLASSES:
        cls_rows = [r for r in rows if r.get("expected") == cls]
        cls_completed = [r for r in completed if r.get("expected") == cls]
        cls_exact = [r for r in exact if r.get("expected") == cls]
        cls_errors = [r for r in rows if r.get("expected") == cls and r.get("status") != "completed"]
        if cls_rows:
            per_class[cls] = {
                "total": len(cls_rows),
                "correct": len(cls_exact),
                "errors": len(cls_errors),
                "accuracy": len(cls_exact) / len(cls_rows) if cls_rows else 0.0,
            }

    costs = [
        float(r["cost"]) for r in completed if isinstance(r.get("cost"), (int, float))
    ]
    total_cost = sum(costs)
    cost_coverage = len(costs)

    return {
        "experiment": metadata.get("experiment_name"),
        "dataset": metadata.get("dataset"),
        "model": metadata.get("model"),
        "prompt_version": metadata.get("prompt_version"),
        "max_tokens": metadata.get("max_tokens"),
        "reasoning_effort": metadata.get("reasoning_effort"),
        "total_rows": total,
        "completed": len(completed),
        "error": len(errored),
        "empty": len(empty),
        "failed_rows": len(errored) + len(empty),
        "failure_rate": (len(errored) + len(empty)) / total if total else 0.0,
        "exact_match": len(exact),
        "exact_match_accuracy": len(exact) / total if total else 0.0,
        "near_miss": len(near_miss),
        "near_miss_accuracy": len(near_miss) / total if total else 0.0,
        "near_miss_share_of_misses": len(near_miss) / len(misses) if misses else 0.0,
        "near_miss_filenames": [r.get("filename") for r in near_miss],
        "runner_up_coverage": sum(1 for r in completed if (r.get("runner_up") or "").strip()),
        "total_cost_usd": round(total_cost, 6),
        "cost_coverage": cost_coverage,
        "avg_cost_per_image_usd": round(total_cost / cost_coverage, 8) if cost_coverage else 0.0,
        "per_class": per_class,
        "error_filenames": [r.get("filename") for r in errored],
        "miss_filenames": [r.get("filename") for r in misses],
    }


def to_markdown(result: dict) -> str:
    lines = [
        f"# Final Results: {result['experiment']}",
        "",
        f"- **Dataset**: {result['dataset']}",
        f"- **Model**: {result['model']}",
        f"- **Prompt**: {result['prompt_version']}",
        f"- **Max tokens**: {result['max_tokens']}",
        "",
        f"## Overall",
        "",
        f"- **Rows**: {result['total_rows']}",
        f"- **Completed**: {result['completed']}",
        f"- **Errors**: {result['error']}",
        f"- **Empty**: {result['empty']}",
        f"- **exact_match**: {result['exact_match']}/{result['total_rows']} ({result['exact_match_accuracy']:.1%})",
        f"- **failure rate**: {result['failed_rows']}/{result['total_rows']} ({result['failure_rate']:.1%})",
        f"- **near_miss** (correct answer was the model's runner-up): {result['near_miss']}/{result['total_rows']} ({result['near_miss_accuracy']:.1%} of rows; {result['near_miss_share_of_misses']:.1%} of all misses)",
        f"- **runner_up coverage**: {result['runner_up_coverage']}/{result['completed']} completed rows had a parsable runner-up",
        f"- **Total cost**: ${result['total_cost_usd']:.4f} across {result['cost_coverage']} rows with billed cost"
        + (f" (avg ${result['avg_cost_per_image_usd']:.6f}/image)" if result['cost_coverage'] else ""),
        "",
        "## Per-class accuracy",
        "",
        "| Class | Correct | Total | Errors | Accuracy |",
        "|---|---:|---:|---:|---:|",
    ]
    for cls in DOCUMENT_CLASSES:
        pc = result["per_class"].get(cls)
        if pc is None:
            continue
        lines.append(
            f"| {cls} | {pc['correct']} | {pc['total']} | {pc['errors']} | {pc['accuracy']:.1%} |"
        )
    if result["error_filenames"]:
        lines += ["", "## Failed (error) rows", ""]
        lines += [f"- `{name}`" for name in result["error_filenames"]]
    if result["near_miss_filenames"]:
        lines += [
            "",
            "## Near-miss rows (correct answer was the model's runner-up)",
            "",
            "These rows were misclassified but the model named the correct class as its",
            "second choice in the reasoning trace — the closest possible misses.",
            "",
        ]
        lines += [f"- `{name}`" for name in result["near_miss_filenames"]]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True,
                        help="Path to the manifest JSONL (reports/manifests/*.jsonl)")
    parser.add_argument("--output-dir", type=Path,
                        default=ROOT / "reports" / "experiment_reports",
                        help="Directory for the saved result files (default: reports/experiment_reports)")
    parser.add_argument("--no-backfill", action="store_true",
                        help="Skip fetching reasoning/cost from Braintrust for rows that "
                             "predate runner-up/cost tracking (near-miss and cost then only "
                             "count rows recorded in the manifest)")
    args = parser.parse_args()

    metadata, final = load_manifest(args.manifest)
    ru_backfilled = ru_missing = cost_backfilled = cost_missing = 0
    if not args.no_backfill:
        ru_backfilled, ru_missing, cost_backfilled, cost_missing = backfill_rows(final, metadata)
        if ru_backfilled:
            print(f"Backfilled runner_up for {ru_backfilled} pre-tracking rows from Braintrust reasoning")
        if cost_backfilled:
            print(f"Backfilled cost for {cost_backfilled} pre-tracking rows from Braintrust span metadata")
    result = score(metadata, final)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = args.manifest.stem
    json_path = args.output_dir / f"{stem}_final.json"
    md_path = args.output_dir / f"{stem}_final.md"
    json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(to_markdown(result), encoding="utf-8")

    print(
        f"Saved: {json_path}\nSaved: {md_path}"
    )
    print()
    print(f"exact_match {result['exact_match']}/{result['total_rows']} ({result['exact_match_accuracy']:.1%})")
    print(f"failure rate {result['failed_rows']}/{result['total_rows']} ({result['failure_rate']:.1%})")
    print(f"total cost ${result['total_cost_usd']:.4f} across {result['cost_coverage']} rows"
          + (f" (avg ${result['avg_cost_per_image_usd']:.6f}/image)" if result['cost_coverage'] else ""))
    print(f"near_miss {result['near_miss']}/{result['total_rows']} "
          f"({result['near_miss_accuracy']:.1%} of rows; {result['near_miss_share_of_misses']:.1%} of misses)")
    print(f"runner_up coverage {result['runner_up_coverage']}/{result['completed']} completed rows")
    if ru_missing:
        print(f"WARNING: {ru_missing} completed rows still lack a runner_up "
              f"(pre-tracking rows with no Braintrust reasoning available)", file=sys.stderr)
    if cost_missing:
        print(f"WARNING: {cost_missing} completed rows have no per-row cost "
              f"(pre-tracking rows with no Braintrust cost metadata)", file=sys.stderr)
    print(f"completed={result['completed']} error={result['error']} empty={result['empty']}")


if __name__ == "__main__":
    main()
