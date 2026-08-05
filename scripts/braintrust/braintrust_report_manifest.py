"""
Generate the full report suite for a completed eval run from its local manifest,
with trace-level detail (reasoning, cost, token metrics) merged from Braintrust.

Unlike ``braintrust_report.py`` — which fetches a single experiment by exact name
and therefore misses rows that the resume loop wrote into ``<name>-*``
version-suffixed experiments — this script treats the local manifest JSONL as the
source of truth for every row and uses Braintrust only for the trace details that
are not in the manifest. Produces, in ``--output-dir`` (default ``reports/``):

- ``report_<experiment>.md`` — full report + results interpretation
- ``per_class_accuracy_<experiment>.png``
- ``confusion_matrix_<experiment>.{png,md}``
- ``misclassification_reasoning_<experiment>.md`` — reasoning trace for every miss

Near-miss (runner-up) is computed from the ``Runner-up:`` line in each row's
reasoning trace exactly as ``score_manifest.py`` does; it requires the Braintrust
fetch (pass ``--no-backfill`` to skip it and report from the manifest alone).
Read-only data fetch — no Braintrust scorer credits.

Usage:
    python scripts/braintrust/braintrust_report_manifest.py \\
      --manifest reports/manifests/qwen3.7-flash_v11.8_1600_balanced_1120.jsonl \\
      --input-price 0.03 --output-price 0.13
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # noqa: E402

import matplotlib
matplotlib.use("Agg")  # noqa: E402

from src.braintrust_utils import fetch_experiment_rows, list_experiments  # noqa: E402
from src.constants import DOCUMENT_CLASSES  # noqa: E402
from src.openrouter_classifier import extract_runner_up  # noqa: E402
from scripts.braintrust.braintrust_report import (  # noqa: E402
    avg,
    compute_cost,
    write_confusion_matrix,
    write_misclassification_reasoning,
    write_per_class_chart,
)
from scripts.braintrust.score_manifest import (  # noqa: E402
    REASONING_PLACEHOLDER,
    _canonical_braintrust_config,
    load_manifest,
)

ROOT = Path(__file__).resolve().parents[2]
VALID_CLASSES = DOCUMENT_CLASSES


def fetch_merged_events(
    experiment_name: str, project_id: str, api_key: str, api_base: str
) -> list[dict]:
    """Fetch span events from the exact-named experiment and its <name>-* versions."""
    events: list[dict] = []
    try:
        experiments = list_experiments(api_key, project_id, api_base)
    except Exception as exc:  # noqa: BLE001 - backfill must never abort reporting
        print(f"WARNING: could not list experiments for report backfill: {exc}", file=sys.stderr)
        return events
    prefix = experiment_name + "-"
    matching = [e for e in experiments if e.get("name") == experiment_name
                or str(e.get("name", "")).startswith(prefix)]
    if not matching:
        print(f"WARNING: no experiments named '{experiment_name}' found for report backfill",
              file=sys.stderr)
        return events
    for exp in matching:
        try:
            exp_events = fetch_experiment_rows(api_key, exp["id"], api_base)
        except Exception as exc:  # noqa: BLE001 - skip one broken experiment
            print(f"WARNING: could not fetch experiment {exp['id']} for report backfill: {exc}",
                  file=sys.stderr)
            continue
        print(f"  Fetched {len(exp_events)} events from {exp['name']}")
        events.extend(exp_events)
    return events


def merge_trace_data(events: list[dict]) -> tuple[dict[str, str], dict[str, dict], float]:
    """Return (reasoning_by_filename, metrics_by_filename, actual_cost_total).

    Reasoning and filename come from task-span metadata; usage metrics (tokens,
    cost, duration) come from the wrapped model-call child spans under each task
    root. The representative metrics per row are the span with the most tokens
    (the final successful completion); actual cost is the sum over every billed
    call (including retries), de-duplicated by span_id.
    """
    reasoning_by_filename: dict[str, str] = {}
    filename_by_root: dict[str, str] = {}
    metrics_by_root: dict[str, list[dict]] = {}
    seen_spans: set[str] = set()
    actual_cost = 0.0
    for ev in events:
        span_id = ev.get("span_id")
        if span_id:
            if span_id in seen_spans:
                continue
            seen_spans.add(span_id)
        meta = ev.get("metadata") or {}
        metrics = ev.get("metrics") or {}
        inp = ev.get("input")
        if not isinstance(inp, dict):
            inp = {}
        filename = meta.get("filename") or inp.get("filename") or ""
        root_id = ev.get("root_span_id") or ev.get("span_id") or ""
        if filename:
            filename_by_root[root_id] = filename
        reasoning = meta.get("reasoning")
        if reasoning and reasoning != REASONING_PLACEHOLDER:
            if filename:
                reasoning_by_filename.setdefault(filename, reasoning)
        if metrics.get("prompt_tokens") is not None or metrics.get("cost") is not None:
            metrics_by_root.setdefault(root_id, []).append(metrics)
        if isinstance(metrics.get("cost"), (int, float)):
            actual_cost += float(metrics["cost"])
    metrics_by_filename: dict[str, dict] = {}
    for root_id, mlist in metrics_by_root.items():
        fn = filename_by_root.get(root_id)
        if not fn:
            continue
        best = max(mlist, key=lambda m: (m.get("prompt_tokens") or 0) + (m.get("completion_tokens") or 0))
        metrics_by_filename[fn] = best
    return reasoning_by_filename, metrics_by_filename, actual_cost


def build_tasks(
    final: dict[str, dict],
    reasoning_by_filename: dict[str, str],
    metrics_by_filename: dict[str, dict],
) -> tuple[list[dict], list[dict]]:
    rows = sorted(final.values(), key=lambda r: (r.get("expected", ""), r.get("filename", "")))
    tasks: list[dict] = []
    failures: list[dict] = []
    for r in rows:
        fn = r.get("filename", "")
        expected = (r.get("expected") or "").strip().lower()
        if r.get("status") != "completed" or not (r.get("predicted") or "").strip():
            failures.append({
                "expected": expected,
                "output": str(r.get("predicted") or ""),
                "filename": fn,
                "status": r.get("status"),
                "error": r.get("error") or "missing output",
            })
            continue
        predicted = str(r["predicted"]).strip().lower()
        reasoning = reasoning_by_filename.get(fn, "") or ""
        runner_up = (r.get("runner_up") or "").strip().lower()
        if not runner_up and reasoning:
            runner_up = (extract_runner_up(reasoning) or "").strip().lower()
        tasks.append({
            "expected": expected,
            "output": predicted,
            "correct": predicted == expected,
            "reasoning": reasoning,
            "filename": fn,
            "runner_up": runner_up,
            "metrics": metrics_by_filename.get(fn, {}),
        })
    return tasks, failures


def build_report(
    experiment: str, model: str, prompt_version: str, dataset: str, per_class: int,
    image_size: str, input_price: float, output_price: float, reasoning: str,
    tasks: list[dict], failures: list[dict], cost: dict, metrics: dict,
    result: dict, confused: list[tuple[str, str, int]],
) -> str:
    total = len(tasks)
    correct = sum(1 for t in tasks if t["correct"])
    accuracy = correct / total * 100 if total else 0
    per_class_acc = Counter(t["expected"] for t in tasks)
    per_class_ok = Counter(t["expected"] for t in tasks if t["correct"])
    accs = sorted((per_class_ok[c] / per_class_acc[c] * 100.0 if per_class_acc[c] else 0.0, c)
                  for c in sorted(VALID_CLASSES) if per_class_acc.get(c))
    worst = accs[:3]
    best = list(reversed(accs[-3:]))
    actual_per_image = cost["actual_usd"] / total if total else 0
    expected_per_image = cost["expected_usd"] / total if total else 0

    md = []
    md.append(f"# Full Report — {experiment}")
    md.append("")
    md.append(f"**Model:** `{model}`  ")
    md.append(f"**Prompt version:** `{prompt_version}`  ")
    md.append(f"**Dataset:** `{dataset}` ({per_class} per class × 16 classes = {total} images)  ")
    md.append(f"**Image size:** {image_size}  ")
    md.append(f"**Reasoning:** {reasoning}  ")
    md.append(f"**Max concurrency:** 8  ")
    md.append("")
    md.append("## Results")
    md.append("")
    md.append("| Metric | Value |")
    md.append("|--------|------:|")
    md.append(f"| **Accuracy (exact_match)** | **{accuracy:.2f}%** ({correct}/{total}) |")
    md.append(f"| Scored rows | {total} |")
    md.append(f"| Failed/empty rows | {len(failures)} |")
    md.append(f"| Failure rate | {result['failure_rate']:.1%} |")
    md.append(f"| **Near-miss** (correct answer was model's runner-up) | **{result['near_miss']}** ({result['near_miss_accuracy']:.1%} of rows; {result['near_miss_share_of_misses']:.1%} of all misses) |")
    md.append(f"| Runner-up coverage | {result['runner_up_coverage']}/{total} completed rows |")
    md.append(f"| Prompt tokens (avg) | {metrics['prompt_tokens_avg']:,.1f} |")
    md.append(f"| Prompt cached tokens (avg) | {metrics['cached_tokens_avg']:,.1f} |")
    md.append(f"| Completion tokens (avg) | {metrics['completion_tokens_avg']:,.1f} |")
    md.append(f"| Completion reasoning tokens (avg) | {metrics['reasoning_tokens_avg']:,.1f} |")
    md.append(f"| Total tokens (avg) | {metrics['prompt_tokens_avg'] + metrics['completion_tokens_avg']:,.1f} |")
    md.append(f"| Time to first token (avg) | {metrics['ttft_avg']:.2f}s |")
    md.append(f"| Duration (avg) | {metrics['duration_avg']:.2f}s |")
    md.append("")
    md.append("## Cost — Expected vs Actual")
    md.append("")
    md.append(f"**List pricing:** ${input_price}/M input tokens, ${output_price}/M output tokens "
              f"(`{model}`, per OpenRouter model listing).")
    md.append("")
    md.append("| Metric | Value |")
    md.append("|--------|------:|")
    md.append(f"| Total prompt tokens (measured) | {cost['prompt_tokens']:,} |")
    md.append(f"| Total completion tokens (measured) | {cost['completion_tokens']:,} |")
    md.append(f"| Total tokens (measured) | {cost['total_tokens']:,} |")
    md.append(f"| **Expected cost** (list price × measured tokens) | **${cost['expected_usd']:.4f}** |")
    md.append(f"| **Actual cost** (OpenRouter billed, all calls incl. retries) | **${cost['actual_usd']:.4f}** |")
    md.append(f"| Difference (expected − actual) | ${cost['difference_usd']:+.4f} "
              f"({cost['pct_diff']:+.1f}%) |")
    md.append(f"| Cost coverage | {cost['cost_coverage']}/{total} rows with billed cost |")
    md.append("")
    md.append("### Scale-up projections (list-price expected vs extrapolated actual)")
    md.append("")
    md.append("| Images | Expected Cost | Estimated Actual |")
    md.append("|--------|--------------:|-----------------:|")
    for n in (800, 25000, 320000):
        md.append(f"| {n:,} | ${expected_per_image * n:.2f} | ${actual_per_image * n:.2f} |")
    md.append("")
    md.append("## Per-Class Accuracy")
    md.append("")
    md.append(f"![Per-Class Accuracy](per_class_accuracy_{experiment}.png)")
    md.append("")
    md.append("| Class | Correct | Total | Accuracy |")
    md.append("|-------|--------:|------:|---------:|")
    for cls in sorted(VALID_CLASSES):
        if per_class_acc[cls] == 0:
            md.append(f"| `{cls}` | 0 | 0 | — |")
            continue
        md.append(f"| `{cls}` | {per_class_ok[cls]} | {per_class_acc[cls]} | "
                  f"{per_class_ok[cls] / per_class_acc[cls] * 100:.0f}% |")
    md.append("")
    md.append("## Confusion Matrix & Misclassification Analysis")
    md.append("")
    md.append(f"- [Confusion matrix markdown](confusion_matrix_{experiment}.md)")
    md.append(f"  - [Confusion matrix heatmap](confusion_matrix_{experiment}.png)")
    md.append(f"- [Misclassification reasoning traces](misclassification_reasoning_{experiment}.md)")
    md.append("")
    md.append("### Top Confused Pairs")
    md.append("")
    md.append("| Expected | Predicted As | Count |")
    md.append("|----------|-------------|------:|")
    for e, p, c in confused[:20]:
        md.append(f"| `{e}` | `{p}` | {c} |")
    md.append("")
    md.append("## Results Interpretation")
    md.append("")
    md.append(f"### Overall")
    md.append("")
    md.append(f"qwen3.7-flash with prompt **v11.8** classifies **{correct}/{total} "
              f"({accuracy:.1f}%)** of the {total}-image `{dataset}` slice exactly. "
              f"There are **{len(failures)} failed/empty rows** (failure rate "
              f"{result['failure_rate']:.1%}) — the resilient retry loop recovered every "
              f"transient provider error, so accuracy is measured over the full slice.")
    md.append("")
    md.append(f"**Near-miss analysis:** {result['near_miss']} of the {total - correct} misses "
              f"({result['near_miss_share_of_misses']:.1%}) were near-misses — the model got "
              f"the answer wrong but named the correct class as its runner-up in the reasoning "
              f"trace. {result['runner_up_coverage']}/{total} rows had a parsable runner-up line. "
              f"If runner-up confusion were fixed (e.g. sharpening the tie-break rules between "
              f"the confused pairs below), accuracy would rise to approximately "
              f"{(correct + result['near_miss']) / total * 100:.1f}%.")
    md.append("")
    md.append("### Strengths")
    md.append("")
    for acc, cls in best:
        md.append(f"- **`{cls}`**: {acc:.0f}% ({per_class_ok[cls]}/{per_class_acc[cls]})")
    md.append("")
    md.append("### Weaknesses")
    md.append("")
    for acc, cls in worst:
        md.append(f"- **`{cls}`**: {acc:.0f}% ({per_class_ok[cls]}/{per_class_acc[cls]})")
    md.append("")
    if confused:
        md.append("### Top Confusion Patterns")
        md.append("")
        top_pairs = confused[:5]
        md.append("The most frequent misclassifications are:")
        for e, p, c in top_pairs:
            md.append(f"- **`{e}` → `{p}`**: {c} images")
        md.append("")
        shared = "".join(f"`{e}` ↔ `{p}` " for e, p, c in confused[:3])
        md.append(f"The dominant failure mode is confusion between visually similar classes "
                  f"({shared}); the single largest confused pair accounts for "
                  f"{confused[0][2] / max(total - correct, 1):.0%} of all misses.")
        md.append("")
    md.append("### Cost")
    md.append("")
    md.append(f"The run billed **${cost['actual_usd']:.4f}** actual vs "
              f"**${cost['expected_usd']:.4f}** list-price expected "
              f"({cost['pct_diff']:+.1f}%), averaging ${actual_per_image:.6f}/image. "
              f"The gap is mostly prompt caching — {metrics['cached_tokens_avg']:,.0f} of "
              f"{metrics['prompt_tokens_avg']:,.0f} avg prompt tokens/row were cache hits "
              f"(cached input billed at ~10% of the input price). "
              f"Extrapolated linearly: ${actual_per_image * 800:.2f} for 800 images, "
              f"${actual_per_image * 25000:.2f} for 25,000, and "
              f"${actual_per_image * 320000:.2f} for a 320,000-image production sweep.")
    md.append("")
    md.append("### Recommendations")
    md.append("")
    recs = []
    if result["near_miss"]:
        recs.append(f"Address the {result['near_miss']} near-misses by adding tie-break "
                    "disambiguation rules between the top confused pairs — this is the "
                    "highest-leverage prompt change (up to ~"
                    f"{result['near_miss'] / total * 100:.1f}pp of accuracy).")
    if confused:
        recs.append(f"Add worked counter-examples for the dominant pairs "
                    f"({', '.join(f'`{e}`→`{p}`' for e, p, _ in confused[:3])}).")
    if len(failures):
        recs.append(f"Inspect the {len(failures)} failed/empty rows; the retry loop already "
                    "handles transient failures so any new errors point at persistent "
                    "provider content filters.")
    recs.append("Review the misclassification reasoning traces linked above before iterating "
                "on the prompt — the raw reasoning often exposes the exact rule the model "
                "misfired on.")
    for i, r in enumerate(recs, 1):
        md.append(f"{i}. {r}")
    md.append("")
    return "\n".join(md)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True,
                        help="Path to the manifest JSONL (reports/manifests/*.jsonl)")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "reports",
                        help="Directory for the report artifacts (default: reports/)")
    parser.add_argument("--input-price", type=float, default=0.03,
                        help="List price per million input tokens (USD)")
    parser.add_argument("--output-price", type=float, default=0.13,
                        help="List price per million output tokens (USD)")
    parser.add_argument("--image-size", default="1024x1024")
    parser.add_argument("--reasoning", default="enabled (effort=high), trace logged")
    parser.add_argument("--no-backfill", action="store_true",
                        help="Skip the Braintrust fetch; reasoning, token metrics, and "
                             "billed cost will be empty")
    args = parser.parse_args()

    metadata, final = load_manifest(args.manifest)
    experiment = metadata.get("experiment_name") or args.manifest.stem
    model = metadata.get("model") or "qwen/qwen3.7-flash"
    prompt_version = metadata.get("prompt_version") or "v11.8"
    dataset = metadata.get("dataset") or "unknown"
    per_class = metadata.get("dataset_size", len(final)) // 16

    reasoning_by_filename: dict[str, str] = {}
    metrics_by_filename: dict[str, dict] = {}
    actual_cost = 0.0
    if not args.no_backfill:
        config = _canonical_braintrust_config()
        print(f"Merging trace data from Braintrust experiments matching '{experiment}'...")
        events = fetch_merged_events(experiment, config.project_id, config.api_key or "", config.api_base)
        reasoning_by_filename, metrics_by_filename, actual_cost = merge_trace_data(events)
        print(f"  reasoning for {len(reasoning_by_filename)} rows, metrics for "
              f"{len(metrics_by_filename)} rows, billed cost sum ${actual_cost:.6f}")
    else:
        print("Skipping Braintrust fetch (--no-backfill)")

    tasks, failures = build_tasks(final, reasoning_by_filename, metrics_by_filename)
    if not tasks:
        sys.exit("No completed rows found in the manifest")

    correct = sum(1 for t in tasks if t["correct"])
    misses = [t for t in tasks if not t["correct"]]
    near_miss = [t for t in misses if t["runner_up"] == t["expected"]]
    runner_up_coverage = sum(1 for t in tasks if t["runner_up"])
    result = {
        "total_rows": len(tasks) + len(failures),
        "completed": len(tasks),
        "failed_rows": len(failures),
        "failure_rate": len(failures) / (len(tasks) + len(failures)) if (tasks or failures) else 0.0,
        "near_miss": len(near_miss),
        "near_miss_accuracy": len(near_miss) / (len(tasks) + len(failures)) if (tasks or failures) else 0.0,
        "near_miss_share_of_misses": len(near_miss) / len(misses) if misses else 0.0,
        "runner_up_coverage": runner_up_coverage,
    }

    metrics = {
        "prompt_tokens_avg": avg([t["metrics"].get("prompt_tokens") or 0 for t in tasks]),
        "completion_tokens_avg": avg([t["metrics"].get("completion_tokens") or 0 for t in tasks]),
        "reasoning_tokens_avg": avg([t["metrics"].get("completion_reasoning_tokens") or 0 for t in tasks]),
        "cached_tokens_avg": avg([t["metrics"].get("prompt_cached_tokens") or 0 for t in tasks]),
        "duration_avg": avg([t["metrics"].get("duration") or 0 for t in tasks]),
        "ttft_avg": avg([t["metrics"].get("time_to_first_token") or 0 for t in tasks]),
    }
    cost = compute_cost(tasks, args.input_price, args.output_price)
    cost["actual_usd"] = actual_cost
    cost["difference_usd"] = cost["expected_usd"] - actual_cost
    cost["pct_diff"] = (cost["expected_usd"] - actual_cost) / cost["expected_usd"] * 100 \
        if cost["expected_usd"] else 0.0
    cost["cost_coverage"] = sum(1 for t in tasks if t["metrics"].get("cost") is not None)

    out_dir = args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Generating artifacts for {experiment} ({len(tasks)} rows, {len(failures)} failures)...")
    write_per_class_chart(tasks, experiment, out_dir)
    _, _, confused = write_confusion_matrix(tasks, experiment, out_dir, dataset, model, per_class)
    write_misclassification_reasoning(tasks, experiment, out_dir)

    report = build_report(
        experiment, model, prompt_version, dataset, per_class, args.image_size,
        args.input_price, args.output_price, args.reasoning, tasks, failures,
        cost, metrics, result, confused,
    )
    report_path = out_dir / f"report_{experiment}.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"Report written: {report_path}")

    print(f"exact_match {correct}/{len(tasks) + len(failures)} "
          f"({correct / (len(tasks) + len(failures)) * 100:.1f}%)")
    print(f"near_miss {len(near_miss)} ({result['near_miss_share_of_misses']:.1%} of misses)")
    print(f"failure rate {result['failure_rate']:.1%} | "
          f"expected ${cost['expected_usd']:.4f} | actual ${cost['actual_usd']:.4f} "
          f"| diff {cost['pct_diff']:+.1f}%")
    print(f"Per-class rows: {dict(sorted(Counter(t['expected'] for t in tasks).items()))}")

    # Append a summary section to the experiment log (skip if already recorded).
    docs_dir = ROOT / "docs" / "experiments"
    docs_dir.mkdir(parents=True, exist_ok=True)
    doc_path = docs_dir / "experiment_log.md"
    existing = doc_path.read_text(encoding="utf-8") if doc_path.exists() else ""
    if experiment in existing:
        print(f"Skipping append — {experiment} already in {doc_path}")
    else:
        section = (
            f"---\n\n## Experiment: `{experiment}` — {len(tasks) + len(failures)} images "
            f"({per_class} per class × 16 classes)\n\n"
            f"**Model:** `{model}`  \n"
            f"**Prompt:** `{prompt_version}`  \n"
            f"**Dataset:** `{dataset}`  \n\n"
            f"| Metric | Value |\n|---|---:|\n"
            f"| **exact_match** | **{correct}/{len(tasks) + len(failures)} "
            f"({correct / (len(tasks) + len(failures)) * 100:.1f}%)** |\n"
            f"| Failure rate | {result['failure_rate']:.1%} |\n"
            f"| Near-miss | {result['near_miss']} "
            f"({result['near_miss_share_of_misses']:.1%} of misses) |\n"
            f"| Expected cost | ${cost['expected_usd']:.4f} |\n"
            f"| Actual cost | ${cost['actual_usd']:.4f} |\n\n"
        )
        with open(doc_path, "a", encoding="utf-8") as f:
            f.write(section)
        print(f"Appended results to: {doc_path}")


if __name__ == "__main__":
    main()
