"""
Braintrust Metrics Visualization

Fetches the latest experiment results from the Braintrust SDK and generates
per-class accuracy bar charts showing which classes the model gets wrong.

Prerequisites:
    pip install braintrust matplotlib numpy
    Set BRAINTRUST_API_KEY in your .env file or environment.

Usage:
    python scripts/braintrust/braintrust_metrics_visual.py
"""

import json
import sys
import time
from pathlib import Path
from typing import Union

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import matplotlib.pyplot as plt
import numpy as np
import requests

from src.braintrust_config import load_braintrust_config
from src.env_utils import require_env
from src.openrouter_classifier import VALID_CLASSES

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OUTPUT_DIR = Path(__file__).resolve().parents[2] / "reports"


# ---------------------------------------------------------------------------
# Fetch experiment data from Braintrust
# ---------------------------------------------------------------------------

API_BASE = "https://api.braintrust.dev/v1"


def fetch_experiment_results(target_experiment: Union[str, None] = None) -> tuple[list[dict], str, dict]:
    """Fetch results from a Braintrust experiment via REST API.
    If target_experiment is provided, fetch that specific experiment by name.
    Otherwise fetch the most recent. Returns (results, experiment_name, experiment_meta)."""
    config = load_braintrust_config()
    api_key = config.api_key or require_env("BRAINTRUST_API_KEY")[0]

    headers = {"Authorization": f"Bearer {api_key}"}

    project_id = config.project_id or config.project_name
    if not project_id:
        resp = requests.get(f"{API_BASE}/project", headers=headers)
        resp.raise_for_status()
        projects = resp.json().get("objects", [])
        project = next((p for p in projects if p["name"] == config.project_name), None)
        if not project:
            print(f"Error: Project '{config.project_name}' not found.")
            sys.exit(1)
        project_id = project["id"]

    # Get experiments for this project (most recent first)
    resp = requests.get(
        f"{API_BASE}/experiment",
        headers=headers,
        params={"project_id": project_id},
    )
    resp.raise_for_status()
    experiments = resp.json().get("objects", [])
    if not experiments:
        print("No experiments found.")
        sys.exit(1)

    # Pick the target or most recent experiment
    if target_experiment:
        latest = next((e for e in experiments if e["name"] == target_experiment), None)
        if not latest:
            print(f"Error: Experiment '{target_experiment}' not found.")
            print(f"Available: {[e['name'] for e in experiments]}")
            sys.exit(1)
    else:
        latest = sorted(experiments, key=lambda e: e.get("created", ""))[-1]
    experiment_id = latest["id"]
    experiment_name = latest["name"]
    print(f"Fetching results from experiment: {experiment_name}")

    # Fetch experiment rows (paginated POST to handle large experiments)
    rows = []
    cursor = None
    max_retries = 6
    while True:
        body = {"limit": 100}
        if cursor:
            body["cursor"] = cursor
        for attempt in range(max_retries):
            try:
                resp = requests.post(
                    f"{API_BASE}/experiment/{experiment_id}/fetch",
                    headers=headers,
                    json=body,
                    timeout=120,
                )
                resp.raise_for_status()
                break
            except requests.exceptions.HTTPError as e:
                if resp.status_code == 429 and attempt < max_retries - 1:
                    wait = 10 * (2 ** attempt)  # 10, 20, 40, 80, 160s
                    print(f"  Rate limited, waiting {wait}s (retry {attempt + 1}/{max_retries})")
                    time.sleep(wait)
                elif attempt < max_retries - 1:
                    wait = 5 * (attempt + 1)
                    print(f"  Retry {attempt + 1}/{max_retries} after {wait}s ({e})")
                    time.sleep(wait)
                else:
                    raise
            except requests.exceptions.Timeout as e:
                if attempt < max_retries - 1:
                    wait = 10 * (attempt + 1)
                    print(f"  Timeout, retry {attempt + 1}/{max_retries} after {wait}s")
                    time.sleep(wait)
                else:
                    raise
        data = resp.json()
        batch = data.get("events", [])
        rows.extend(batch)
        cursor = data.get("cursor")
        print(f"  Fetched {len(batch)} rows (total: {len(rows)})")
        if not cursor or not batch:
            break

    results = []
    # Collect token/timing metrics from all rows (including spans)
    prompt_tokens_list = []
    completion_tokens_list = []
    reasoning_tokens_list = []
    cached_tokens_list = []
    duration_list = []

    # Build a lookup of metadata from span rows (keyed by root_span_id)
    # Metadata (reasoning, filename) is logged on child spans via current_span().log()
    span_metadata_by_root = {}
    detected_model = None
    for row in rows:
        metadata = row.get("metadata") or {}
        root_span_id = row.get("root_span_id", "")
        span_id = row.get("span_id", "")
        # Capture model name from metadata (check every row)
        if not detected_model and metadata.get("model"):
            detected_model = metadata["model"]
        # If this row has metadata with reasoning or filename, index it
        if metadata.get("reasoning") or metadata.get("filename"):
            span_metadata_by_root[root_span_id] = metadata

    for row in rows:
        # Collect metrics from any row that has them
        metrics = row.get("metrics") or {}
        if metrics.get("prompt_tokens"):
            prompt_tokens_list.append(metrics["prompt_tokens"])
        if metrics.get("completion_tokens"):
            completion_tokens_list.append(metrics["completion_tokens"])
        if metrics.get("tokens"):
            # Some rows report total as 'tokens'
            pass
        if metrics.get("cached_tokens"):
            cached_tokens_list.append(metrics["cached_tokens"])
        if metrics.get("duration"):
            duration_list.append(metrics["duration"])

        expected = row.get("expected", "")
        output = row.get("output", "")

        # Skip span/trace rows that don't have valid eval data
        if not expected or expected not in VALID_CLASSES:
            continue
        if not output:
            continue

        # Get metadata from this row or from its child span
        metadata = row.get("metadata") or {}
        root_span_id = row.get("root_span_id", "")
        span_id = row.get("span_id", "")
        # Try to find child span metadata using root_span_id or span_id
        child_meta = span_metadata_by_root.get(root_span_id, {})
        if not child_meta:
            child_meta = span_metadata_by_root.get(span_id, {})

        reasoning = metadata.get("reasoning", "") or child_meta.get("reasoning", "")
        filename = metadata.get("filename", "") or child_meta.get("filename", "")

        results.append({
            "expected": expected,
            "output": output,
            "correct": output.strip().lower() == expected.strip().lower(),
            "reasoning": reasoning,
            "filename": filename,
        })

    # Compute averages
    def avg(lst):
        return sum(lst) / len(lst) if lst else 0

    experiment_meta = {
        "id": experiment_name,
        "model": detected_model or "unknown",
        "prompt_tokens_avg": avg(prompt_tokens_list),
        "completion_tokens_avg": avg(completion_tokens_list),
        "reasoning_tokens_avg": avg(reasoning_tokens_list),
        "cached_tokens_avg": avg(cached_tokens_list),
        "duration_avg": avg(duration_list),
        "total_rows": len(rows),
    }

    print(f"Filtered to {len(results)} eval rows (from {len(rows)} total rows)")
    return results, experiment_name, experiment_meta


# ---------------------------------------------------------------------------
# Visualization
# ---------------------------------------------------------------------------

def plot_per_class_accuracy(results: list[dict], experiment_name: str):
    """Generate a horizontal bar chart of per-class accuracy, sorted worst to best."""
    class_correct = {cls: 0 for cls in VALID_CLASSES}
    class_total = {cls: 0 for cls in VALID_CLASSES}
    misclassified_as = {cls: {} for cls in VALID_CLASSES}

    for r in results:
        expected = r["expected"]
        output = r["output"]
        if expected in VALID_CLASSES:
            class_total[expected] += 1
            if r["correct"]:
                class_correct[expected] += 1
            else:
                misclassified_as[expected][output] = misclassified_as[expected].get(output, 0) + 1

    # Compute accuracy
    classes = []
    accuracies = []
    for cls in VALID_CLASSES:
        total = class_total[cls]
        acc = (class_correct[cls] / total * 100) if total > 0 else 0
        classes.append(cls)
        accuracies.append(acc)

    # Sort by accuracy (worst first at top)
    sorted_pairs = sorted(zip(accuracies, classes))
    accuracies_sorted = [p[0] for p in sorted_pairs]
    classes_sorted = [p[1] for p in sorted_pairs]

    # Color bars by performance
    colors = []
    for acc in accuracies_sorted:
        if acc >= 90:
            colors.append("#2ecc71")
        elif acc >= 70:
            colors.append("#f39c12")
        elif acc >= 50:
            colors.append("#e67e22")
        else:
            colors.append("#e74c3c")

    # Overall accuracy
    total_correct = sum(1 for r in results if r["correct"])
    overall_acc = total_correct / len(results) * 100 if results else 0

    # Plot
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(range(len(classes_sorted)), accuracies_sorted, color=colors, edgecolor="gray", linewidth=0.5)

    ax.set_yticks(range(len(classes_sorted)))
    ax.set_yticklabels(classes_sorted, fontsize=11, fontfamily="monospace")
    ax.set_xlabel("Accuracy (%)", fontsize=12)
    ax.set_title(
        f"Per-Class Classification Accuracy — {experiment_name}\n"
        f"Overall: {overall_acc:.1f}% ({total_correct}/{len(results)})",
        fontsize=13, fontweight="bold"
    )
    ax.set_xlim(0, 110)
    ax.axvline(x=overall_acc, color="blue", linestyle="--", linewidth=1.2, alpha=0.7, label=f"Overall avg ({overall_acc:.1f}%)")
    ax.legend(loc="lower right", fontsize=10)

    # Add percentage + error count labels on bars
    for i, (bar, acc, cls) in enumerate(zip(bars, accuracies_sorted, classes_sorted)):
        total = class_total[cls]
        errors = total - class_correct[cls]
        label = f"{acc:.0f}%"
        if errors > 0:
            label += f"  ({errors} wrong)"
        ax.text(acc + 1.5, i, label, va="center", fontsize=9, fontweight="bold")

    plt.tight_layout()

    output_path = OUTPUT_DIR / f"per_class_accuracy_{experiment_name}.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    print(f"\nChart saved: {output_path}")
    plt.close()

    # Print terminal summary with misclassification breakdown
    print("\n" + "=" * 60)
    print("PER-CLASS MISCLASSIFICATION DETAILS")
    print("=" * 60)
    for cls in classes_sorted:
        total = class_total[cls]
        correct_count = class_correct[cls]
        acc = (correct_count / total * 100) if total > 0 else 0
        print(f"\n  {cls} — {correct_count}/{total} correct ({acc:.0f}%)")
        if misclassified_as[cls]:
            for wrong_cls, count in sorted(misclassified_as[cls].items(), key=lambda x: -x[1]):
                print(f"      -> predicted '{wrong_cls}' instead: {count}x")
        else:
            print(f"      (no errors)")


# ---------------------------------------------------------------------------
# Confusion Matrix
# ---------------------------------------------------------------------------

def build_confusion_matrix(results: list[dict], experiment_name: str, model_name: str = "unknown"):
    """Build and save a confusion matrix heatmap + markdown doc."""
    # Use only classes that appear in the results
    all_classes = sorted(VALID_CLASSES)

    # Build the matrix
    matrix = {expected: {predicted: 0 for predicted in all_classes} for expected in all_classes}
    for r in results:
        expected = r["expected"].strip().lower()
        predicted = r["output"].strip().lower()
        if expected in matrix:
            matrix[expected][predicted] = matrix[expected].get(predicted, 0) + 1

    # --- Heatmap PNG ---
    labels = all_classes
    n = len(labels)
    data = np.zeros((n, n))
    for i, exp in enumerate(labels):
        for j, pred in enumerate(labels):
            data[i][j] = matrix[exp].get(pred, 0)

    fig, ax = plt.subplots(figsize=(14, 12))
    im = ax.imshow(data, cmap="YlOrRd", aspect="auto")

    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=9, fontfamily="monospace")
    ax.set_yticklabels(labels, fontsize=9, fontfamily="monospace")
    ax.set_xlabel("Predicted", fontsize=12)
    ax.set_ylabel("Expected (True)", fontsize=12)
    ax.set_title(
        f"Confusion Matrix — {experiment_name}\n"
        f"{len(results)} images | {sum(1 for r in results if r['correct'])} correct",
        fontsize=13, fontweight="bold"
    )

    # Annotate cells
    for i in range(n):
        for j in range(n):
            val = int(data[i][j])
            if val == 0:
                continue
            color = "white" if val > data.max() * 0.6 else "black"
            ax.text(j, i, str(val), ha="center", va="center",
                    fontsize=8, fontweight="bold", color=color)

    plt.colorbar(im, ax=ax, shrink=0.8, label="Count")
    plt.tight_layout()

    heatmap_path = OUTPUT_DIR / f"confusion_matrix_{experiment_name}.png"
    plt.savefig(heatmap_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Confusion matrix heatmap saved: {heatmap_path}")

    # --- Markdown doc ---
    total_correct = sum(1 for r in results if r["correct"])
    total = len(results)
    accuracy = (total_correct / total * 100) if total else 0

    md = []
    md.append(f"# Confusion Matrix — {experiment_name}")
    md.append(f"")
    samples_per_class = total // len(labels) if labels else total
    md.append(f"**Overall Accuracy:** {accuracy:.1f}% ({total_correct}/{total})  ")
    md.append(f"**Dataset:** {samples_per_class} per class  ")
    md.append(f"**Model:** `{model_name}`")
    md.append(f"")
    md.append(f"![Confusion Matrix](confusion_matrix_{experiment_name}.png)")
    md.append(f"")

    # Markdown table
    md.append("## Raw Counts")
    md.append("")
    header = "| Expected \\ Predicted | " + " | ".join(f"`{c[:6]}`" for c in labels) + " | **Total** | **Acc** |"
    md.append(header)
    md.append("|" + "---:|" * (n + 3))

    for i, exp in enumerate(labels):
        row_total = sum(int(data[i][j]) for j in range(n))
        row_correct = int(data[i][i])
        row_acc = (row_correct / row_total * 100) if row_total > 0 else 0
        cells = []
        for j in range(n):
            val = int(data[i][j])
            if i == j and val > 0:
                cells.append(f"**{val}**")
            elif val > 0:
                cells.append(f"{val}")
            else:
                cells.append(".")
        md.append(f"| `{exp}` | " + " | ".join(cells) + f" | {row_total} | {row_acc:.0f}% |")

    md.append("")

    # Top confused pairs
    md.append("## Top Confused Pairs")
    md.append("")
    md.append("| Expected | Predicted As | Count |")
    md.append("|----------|-------------|------:|")

    confused = []
    for exp in labels:
        for pred in labels:
            if exp != pred:
                count = matrix[exp].get(pred, 0)
                if count > 0:
                    confused.append((exp, pred, count))

    confused.sort(key=lambda x: -x[2])
    for exp, pred, count in confused[:20]:
        md.append(f"| `{exp}` | `{pred}` | {count} |")

    md.append("")

    # Write markdown file
    md_path = OUTPUT_DIR / f"confusion_matrix_{experiment_name}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"Confusion matrix markdown saved: {md_path}")


# ---------------------------------------------------------------------------
# Misclassification Reasoning Extraction
# ---------------------------------------------------------------------------

def extract_misclassification_reasoning(results: list[dict], experiment_name: str):
    """Generate a markdown doc with reasoning text for every misclassification,
    grouped by confused pair."""
    # Collect misclassifications
    errors = [r for r in results if not r["correct"]]
    if not errors:
        print("No misclassifications found.")
        return

    # Group by (expected, predicted) pair
    pairs: dict[tuple[str, str], list[dict]] = {}
    for r in errors:
        key = (r["expected"], r["output"].strip().lower())
        pairs.setdefault(key, []).append(r)

    # Sort pairs by count descending
    sorted_pairs = sorted(pairs.items(), key=lambda x: -len(x[1]))

    total = len(results)
    total_correct = sum(1 for r in results if r["correct"])

    md = []
    md.append(f"# Misclassification Reasoning — {experiment_name}")
    md.append("")
    md.append(f"**Overall Accuracy:** {(total_correct / total * 100):.1f}% ({total_correct}/{total})  ")
    md.append(f"**Total Errors:** {len(errors)}  ")
    md.append(f"**Unique Confused Pairs:** {len(sorted_pairs)}")
    md.append("")
    md.append("---")

    for (expected, predicted), items in sorted_pairs:
        md.append("")
        md.append(f"## {expected} → {predicted} ({len(items)} errors)")
        md.append("")

        for item in items:
            filename = item.get("filename", "unknown")
            reasoning = item.get("reasoning", "").strip()

            md.append(f"### `{filename}`")
            md.append(f"**Expected:** `{expected}` | **Predicted:** `{predicted}`")
            md.append("")
            if reasoning:
                md.append("**Reasoning:**")
                md.append(f"> {reasoning}")
            else:
                md.append("*No reasoning text captured.*")
            md.append("")
            md.append("---")

    md_path = OUTPUT_DIR / f"misclassification_reasoning_{experiment_name}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"Misclassification reasoning saved: {md_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

# Pricing lookup by model (input $/M, output $/M)
MODEL_PRICING = {
    "google/gemini-2.5-flash": (0.15, 0.60),
    "moonshotai/kimi-k3": (0.30, 15.00),
    "anthropic/claude-opus-4.7": (15.00, 75.00),
    "anthropic/claude-sonnet-4": (3.00, 15.00),
    "openai/gpt-5.6-terra": (2.50, 10.00),
    "x-ai/grok-4.5": (2.00, 6.00),
    "anthropic/claude-sonnet-5": (3.00, 15.00),
    "google/gemini-3.6-flash": (0.15, 0.60),
    "anthropic/claude-opus-5": (15.00, 75.00),
}


def print_doc_section(results: list[dict], experiment_name: str, meta: dict):
    """Print a markdown section for the experiment log."""
    total_correct = sum(1 for r in results if r["correct"])
    total = len(results)
    accuracy = (total_correct / total * 100) if total else 0

    prompt_avg = meta["prompt_tokens_avg"]
    completion_avg = meta["completion_tokens_avg"]
    total_tokens_avg = prompt_avg + completion_avg
    duration_avg = meta["duration_avg"]
    cached_avg = meta["cached_tokens_avg"]
    model_name = meta.get("model", "unknown")

    # Look up pricing for this model
    input_price_per_m, output_price_per_m = MODEL_PRICING.get(
        model_name, (0.15, 0.60)  # default to Gemini Flash pricing
    )

    images_per_class = total // 16 if total else 0

    section = f"""
---

## Experiment: `{model_name}` — {total} Images ({images_per_class} per class × 16 classes)

**Experiment ID:** {experiment_name}
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py`
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`

### Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **{accuracy:.2f}%** ({total_correct}/{total} correct) |
| Prompt tokens (avg) | {prompt_avg:,.2f} |
| Prompt cached tokens (avg) | {cached_avg:,.2f} |
| Completion tokens (avg) | {completion_avg:,.2f} |
| Total tokens (avg) | {total_tokens_avg:,.2f} |
| Duration (avg) | {duration_avg:.2f}s |
| Errors | 0 |

### Cost Projections (`{model_name}`, `max_tokens=1024`)

**Pricing:** ${input_price_per_m}/M input tokens, ${output_price_per_m}/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
|--------|---:|---:|---:|---:|
| 800 | {int(prompt_avg * 800):,} | {int(completion_avg * 800):,} | {int(total_tokens_avg * 800):,} | **${(prompt_avg * 800 * input_price_per_m / 1_000_000) + (completion_avg * 800 * output_price_per_m / 1_000_000):.2f}** |
| 25,000 | {int(prompt_avg * 25000):,} | {int(completion_avg * 25000):,} | {int(total_tokens_avg * 25000):,} | **${(prompt_avg * 25000 * input_price_per_m / 1_000_000) + (completion_avg * 25000 * output_price_per_m / 1_000_000):.2f}** |
| 320,000 | {int(prompt_avg * 320000):,} | {int(completion_avg * 320000):,} | {int(total_tokens_avg * 320000):,} | **${(prompt_avg * 320000 * input_price_per_m / 1_000_000) + (completion_avg * 320000 * output_price_per_m / 1_000_000):.2f}** |
"""
    print(section)
    return section


def main():
    # Optional CLI arg: experiment name
    target = sys.argv[1] if len(sys.argv) > 1 else None
    results, experiment_name, meta = fetch_experiment_results(target)
    print(f"Fetched {len(results)} results\n")
    plot_per_class_accuracy(results, experiment_name)

    # Build confusion matrix
    model_name = meta.get("model", "unknown")
    build_confusion_matrix(results, experiment_name, model_name=model_name)

    # Extract misclassification reasoning
    extract_misclassification_reasoning(results, experiment_name)

    # Print doc section
    section = print_doc_section(results, experiment_name, meta)

    # Append to experiment log (skip if experiment already recorded)
    docs_dir = Path(__file__).resolve().parents[2] / "docs" / "experiments"
    docs_dir.mkdir(parents=True, exist_ok=True)
    doc_path = docs_dir / "experiment_log.md"
    existing_content = ""
    if doc_path.exists():
        existing_content = doc_path.read_text(encoding="utf-8")

    if experiment_name in existing_content:
        print(f"\nSkipping append — {experiment_name} already in {doc_path}")
    else:
        with open(doc_path, "a", encoding="utf-8") as f:
            f.write(section)
        print(f"\nAppended results to: {doc_path}")
    print("Done.")


if __name__ == "__main__":
    main()