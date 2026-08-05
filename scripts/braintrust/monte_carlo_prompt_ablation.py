"""Paired-bootstrap prompt ablation over the joint corpus.

For every pair of prompt versions run on the SAME model, compares exact-match
outcomes on the SHARED image set using a paired bootstrap: per-image deltas
``correct(A) - correct(B)`` are resampled with replacement, giving a mean delta,
a 95% confidence interval, and ``P(A beats B)`` (the fraction of resamples with a
positive mean delta). Per-class and per-confusion-pair deltas are reported the
same way so a prompt change is understood *where* it wins/loses, not just that
it moved overall.

This is the statistical gate for prompt iteration: a candidate version should
beat the incumbent on shared images with a comfortably-high ``P(win)`` and a CI
that excludes zero before it is promoted.

Usage:
    python scripts/braintrust/monte_carlo_prompt_ablation.py
    python scripts/braintrust/monte_carlo_prompt_ablation.py --min-shared 20
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # noqa: E402

import numpy as np
from matplotlib import pyplot as plt

from src.constants import DOCUMENT_CLASSES  # noqa: E402
from src.monte_carlo import paired_delta_bootstrap, save_figure, style_axis

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CORPUS = ROOT / "reports" / "monte_carlo" / "corpus.jsonl"
OUTPUT_DIR = ROOT / "reports" / "monte_carlo"

VALID_CLASSES = list(DOCUMENT_CLASSES)


def load_outcomes(corpus_path: Path) -> dict[str, dict[str, dict[str, dict]]]:
    """Return ``{model: {prompt_version: {filename: outcome_dict}}}``.

    ``outcome_dict`` carries ``{expected, correct, predicted, confusion_pair}``.
    Only completed rows with a valid prediction are kept.
    """
    by_model: dict[str, dict[str, dict[str, dict]]] = defaultdict(
        lambda: defaultdict(dict)
    )
    for line in corpus_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        if record.get("status") != "completed":
            continue
        predicted = (record.get("predicted") or "").strip().lower()
        if predicted not in VALID_CLASSES:
            continue
        expected = record["expected"]
        by_model[record["model"]][record["prompt_version"]][record["filename"]] = {
            "expected": expected,
            "correct": int(predicted == expected),
            "predicted": predicted,
            "confusion_pair": record.get("confusion_pair") or "",
        }
    return dict(by_model)


def paired_ablation(by_model: dict) -> list[dict]:
    """Bootstrap every prompt pair per model and return the comparison rows."""
    comparisons: list[dict] = []
    for model, prompts in by_model.items():
        versions = sorted(prompts.keys())
        for i, a in enumerate(versions):
            for b in versions[i + 1:]:
                shared = set(prompts[a]) & set(prompts[b])
                if not shared:
                    continue
                deltas = [prompts[a][fn]["correct"] - prompts[b][fn]["correct"]
                          for fn in shared]
                boot = paired_delta_bootstrap(deltas, n_boot=10000, seed=42)
                per_class: dict[str, dict] = {}
                for cls in VALID_CLASSES:
                    cls_shared = [fn for fn in shared if prompts[a][fn]["expected"] == cls]
                    if len(cls_shared) < 5:
                        continue
                    cls_deltas = [prompts[a][fn]["correct"] - prompts[b][fn]["correct"]
                                  for fn in cls_shared]
                    per_class[cls] = paired_delta_bootstrap(cls_deltas, n_boot=10000, seed=42)
                comparisons.append({
                    "model": model,
                    "prompt_a": a,
                    "prompt_b": b,
                    "shared": len(shared),
                    "acc_a": sum(prompts[a][fn]["correct"] for fn in shared) / len(shared),
                    "acc_b": sum(prompts[b][fn]["correct"] for fn in shared) / len(shared),
                    "delta": boot["mean"],
                    "ci_lo": boot["ci_lo"],
                    "ci_hi": boot["ci_hi"],
                    "p_win": boot["p_win"],
                    "per_class": per_class,
                })
    comparisons.sort(key=lambda c: -abs(c["delta"]))
    return comparisons


def significance(p_win: float) -> str:
    if p_win >= 0.975:
        return "A wins**"
    if p_win <= 0.025:
        return "B wins**"
    if p_win >= 0.90:
        return "A likely"
    if p_win <= 0.10:
        return "B likely"
    return "inconclusive"


def run() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS,
                        help=f"Joint corpus JSONL (default: {DEFAULT_CORPUS})")
    parser.add_argument("--min-shared", type=int, default=20,
                        help="Minimum shared images for a pair to be compared")
    parser.add_argument("--n-boot", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    by_model = load_outcomes(args.corpus)
    comparisons = [c for c in paired_ablation(by_model) if c["shared"] >= args.min_shared]
    if not comparisons:
        print("No prompt pairs meet --min-shared; nothing to report.")
        return
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Chart: mean delta with 95% CI whiskers, colored by significance.
    labels = [f"{c['prompt_a']} vs {c['prompt_b']}\n({c['model'].split('/')[-1]}, n={c['shared']})"
              for c in comparisons]
    deltas = [c["delta"] for c in comparisons]
    lo = [c["ci_lo"] for c in comparisons]
    hi = [c["ci_hi"] for c in comparisons]
    fig, ax = plt.subplots(figsize=(11, max(6, 0.5 * len(comparisons) + 2)))
    y = np.arange(len(comparisons))
    colors = ["#2ecc71" if c["p_win"] >= 0.975 else "#e74c3c" if c["p_win"] <= 0.025
              else "#f39c12" if c["p_win"] >= 0.90 or c["p_win"] <= 0.10 else "#95a5a6"
              for c in comparisons]
    ax.barh(y, deltas, color=colors, edgecolor="gray", linewidth=0.5)
    ax.errorbar(deltas, y, xerr=[np.array(deltas) - np.array(lo), np.array(hi) - np.array(deltas)],
                fmt="none", ecolor="black", capsize=3)
    ax.axvline(0, color="black", linewidth=1)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=9, fontfamily="monospace")
    style_axis(ax, "Prompt Ablation: Accuracy Delta (A vs B) with 95% CI",
               "Delta (acc A - acc B)", "")
    save_figure(fig, OUTPUT_DIR / "prompt_ablation_pairwise.png")

    md = [f"# Prompt Ablation (Paired Bootstrap)",
          "",
          f"- **Minimum shared images**: {args.min_shared}",
          f"- **Bootstrap reps**: {args.n_boot}",
          "",
          "Positive delta favors the first prompt; ``A wins**``/``B wins**`` means",
          "the 95% CI excludes zero.",
          "",
          "| model | A | B | shared | acc A | acc B | delta | 95% CI | P(A wins) | verdict |",
          "|---|---|---:|---:|---:|---:|---:|---|---:|---|",
          ]
    for c in comparisons:
        md.append(f"| `{c['model'].split('/')[-1]}` | `{c['prompt_a']}` | `{c['prompt_b']}` | "
                  f"{c['shared']} | {c['acc_a']:.3f} | {c['acc_b']:.3f} | "
                  f"{c['delta']:+.3f} | {c['ci_lo']:+.3f}..{c['ci_hi']:+.3f} | "
                  f"{c['p_win']:.3f} | {significance(c['p_win'])} |")
    md.append("")
    md.append("## Per-class deltas (A - B) on shared images")
    md.append("")
    md.append("Only classes with >=5 shared images are shown.")
    md.append("")
    for c in comparisons:
        if not c["per_class"]:
            continue
        md.append(f"### {c['prompt_a']} vs {c['prompt_b']} ({c['model'].split('/')[-1]})")
        md.append("")
        md.append("| class | delta | 95% CI | P(A wins) |")
        md.append("|---|---:|---:|---:|")
        for cls in sorted(c["per_class"]):
            pc = c["per_class"][cls]
            md.append(f"| {cls} | {pc['mean']:+.3f} | {pc['ci_lo']:+.3f}..{pc['ci_hi']:+.3f} | {pc['p_win']:.3f} |")
        md.append("")
    path = OUTPUT_DIR / "prompt_ablation.md"
    path.write_text("\n".join(md), encoding="utf-8")
    print(f"Report saved: {path}")
    print(f"\nCompared {len(comparisons)} prompt pairs across {len(by_model)} models:")
    for c in comparisons:
        print(f"  {c['model'].split('/')[-1]:<28} {c['prompt_a']:<6} vs {c['prompt_b']:<6} "
              f"n={c['shared']:<4} delta={c['delta']:+.3f} "
              f"({c['ci_lo']:+.3f}..{c['ci_hi']:+.3f}) P={c['p_win']:.2f} {significance(c['p_win'])}")


if __name__ == "__main__":
    run()
