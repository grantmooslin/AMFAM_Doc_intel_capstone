"""Monte Carlo ensemble voting + confidence-gated escalation simulation.

Reads the joint corpus and treats every completed row as a sample from a
per-image label distribution. Three Monte Carlo questions are answered with
zero API spend:

1. **Ensemble voting** — if each image were re-run ``K`` times and the labels
   majority-voted, what accuracy would we get? Reports ``accuracy(K)`` overall
   and per class, with bootstrap confidence bands, so the committee ceiling and
   its cost multiplier (``K`` x average single-pass cost) are known up front.

2. **Confidence heuristic** — per-image confidence in ``[0, 1]`` from vote
   dominance, label entropy, a near-miss signal (some observation named the
   expected class as its runner-up), and uncertainty phrasing in the reasoning.

3. **Abstention/escalation** — route the lowest-confidence ``alpha`` fraction to
   a stronger model (parameterized ``--escalated-acc``, with a +/- sensitivity
   band) and sweep the accuracy-vs-cost Pareto frontier, so the escalation
   threshold and its expected accuracy/cost tradeoff are visible before any
   credits are spent. The concrete filenames to escalate are written to
   ``escalation_candidates.txt`` for a spend-minimal verification eval.

Usage:
    python scripts/braintrust/monte_carlo_ensemble.py
    python scripts/braintrust/monte_carlo_ensemble.py --k-list 1,3,5,7,10
    python scripts/braintrust/monte_carlo_ensemble.py --escalated-acc 0.90
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # noqa: E402

import numpy as np
from matplotlib import pyplot as plt

from src.constants import DOCUMENT_CLASSES  # noqa: E402
from src.openrouter_classifier import extract_runner_up  # noqa: E402
from src.monte_carlo import (
    bootstrap,
    confidence_score,
    normalize_dist,
    majority_margin,
    save_figure,
    shannon_entropy,
    style_axis,
    uncertainty_phrases,
)

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CORPUS = ROOT / "reports" / "monte_carlo" / "corpus.jsonl"
OUTPUT_DIR = ROOT / "reports" / "monte_carlo"

VALID_CLASSES = list(DOCUMENT_CLASSES)


def load_observations(corpus_path: Path) -> dict[str, dict]:
    """Group completed corpus rows into per-image observations.

    Returns ``{filename: {expected, observations: [predicted...], runner_ups,
    reasoning: [...], models, prompts}}``.
    """
    images: dict[str, dict] = defaultdict(lambda: {
        "expected": "",
        "observations": [],
        "runner_ups": [],
        "reasoning": [],
        "models": set(),
        "prompts": set(),
    })
    for line in corpus_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        if record.get("status") != "completed":
            continue
        predicted = (record.get("predicted") or "").strip().lower()
        if predicted not in VALID_CLASSES:
            continue
        image = images[record["filename"]]
        image["expected"] = record["expected"]
        image["observations"].append(predicted)
        reasoning = record.get("reasoning") or ""
        runner_up = (record.get("runner_up") or "").strip().lower()
        if runner_up not in VALID_CLASSES and reasoning:
            runner_up = extract_runner_up(reasoning).strip().lower()
        if runner_up in VALID_CLASSES:
            image["runner_ups"].append(runner_up)
        if reasoning:
            image["reasoning"].append(reasoning)
        image["models"].add(record.get("model") or "")
        image["prompts"].add(record.get("prompt_version") or "")
    return dict(images)


def hard_distribution(observations: list[str]) -> dict[str, float]:
    return normalize_dist(Counter(observations))


def committee_correctness(
    dist: dict[str, float],
    expected: str,
    k: int,
    n_sim: int,
    rng: np.random.Generator,
) -> float:
    """Estimated probability a ``k``-vote majority over ``dist`` equals ``expected``."""
    labels = list(dist.keys())
    probs = [dist[label] for label in labels]
    if expected not in labels or k < 1:
        return 0.0
    expected_pos = labels.index(expected)
    votes = rng.choice(len(labels), size=(n_sim, k), p=probs)
    counts = np.stack([(votes == i).sum(axis=1) for i in range(len(labels))], axis=1)
    jitter = rng.random(counts.shape) * 1e-9
    winners = (counts + jitter).argmax(axis=1)
    return float(np.mean(winners == expected_pos))


def simulate_committees(images: dict[str, dict], k_list: list[int],
                        n_sim: int, seed: int) -> tuple[dict, dict, int]:
    """Return (accuracy_by_k, per_class_by_k, multi_obs_count)."""
    rng = np.random.default_rng(seed)
    accuracy_by_k: dict[int, list[float]] = {k: [] for k in k_list}
    per_class_by_k: dict[int, dict[str, list[float]]] = {
        k: defaultdict(list) for k in k_list
    }
    multi = 0
    for image in images.values():
        dist = hard_distribution(image["observations"])
        expected = image["expected"]
        for k in k_list:
            if k == 1:
                p = dist.get(expected, 0.0)
            else:
                p = committee_correctness(dist, expected, k, n_sim, rng)
            accuracy_by_k[k].append(p)
            per_class_by_k[k][expected].append(p)
        if len(image["observations"]) > 1:
            multi += 1
    return accuracy_by_k, per_class_by_k, multi


def build_confidence(images: dict[str, dict]) -> dict[str, dict]:
    """Per-image confidence metadata: dist stats + heuristic score."""
    result: dict[str, dict] = {}
    for filename, image in images.items():
        dist = hard_distribution(image["observations"])
        near_miss = any(ru == image["expected"] for ru in image["runner_ups"])
        uncertainty = any(uncertainty_phrases(text) for text in image["reasoning"])
        result[filename] = {
            "filename": filename,
            "expected": image["expected"],
            "n_obs": len(image["observations"]),
            "mode": max(dist.items(), key=lambda item: item[1])[0] if dist else "",
            "margin": majority_margin(dist),
            "entropy": shannon_entropy(dist, normalized=True),
            "near_miss": near_miss,
            "uncertainty": uncertainty,
            "confidence": confidence_score(dist, near_miss_signal=near_miss, uncertainty=uncertainty),
            "p_correct": dist.get(image["expected"], 0.0),
        }
    return result


def run() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS,
                        help=f"Joint corpus JSONL (default: {DEFAULT_CORPUS})")
    parser.add_argument("--k-list", default="1,3,5,7,10,15,25",
                        help="Comma-separated committee sizes to simulate")
    parser.add_argument("--n-sim", type=int, default=2000,
                        help="Monte Carlo repetitions per image per committee size")
    parser.add_argument("--alpha-grid", default="0.01,0.02,0.05,0.1,0.15,0.2,0.3,0.4,0.5",
                        help="Escalation fractions to sweep")
    parser.add_argument("--escalated-acc", type=float, default=0.90,
                        help="Assumed accuracy of the escalated (stronger) model")
    parser.add_argument("--escalated-cost-mult", type=float, default=3.0,
                        help="Cost multiplier of the escalated model vs the base")
    parser.add_argument("--n-boot", type=int, default=10000,
                        help="Bootstrap repetitions for confidence intervals")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    k_list = [int(x) for x in args.k_list.split(",") if x.strip()]
    alpha_grid = [float(x) for x in args.alpha_grid.split(",") if x.strip()]
    if 1 not in k_list:
        k_list = [1] + k_list

    images = load_observations(args.corpus)
    print(f"Loaded {len(images)} images from {args.corpus}")
    accuracy_by_k, per_class_by_k, multi = simulate_committees(images, k_list, args.n_sim, args.seed)
    conf = build_confidence(images)
    print(f"Multi-observation images: {multi}/{len(images)}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # --- Ensemble chart + markdown ---
    ks = k_list
    means = [float(np.mean(accuracy_by_k[k])) for k in ks]
    boots = {k: bootstrap(accuracy_by_k[k], lambda vals: float(np.mean(vals)),
                          n_boot=args.n_boot, seed=args.seed) for k in ks}
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(ks, means, marker="o", color="#2ecc71", label="Simulated committee accuracy")
    ax.fill_between(ks, [boots[k]["ci_lo"] for k in ks],
                    [boots[k]["ci_hi"] for k in ks], color="#2ecc71", alpha=0.2,
                    label="95% bootstrap CI")
    style_axis(ax, "Ensemble Majority-Vote Accuracy vs Committee Size", "Committee size K", "Accuracy")
    ax.legend(loc="lower right", fontsize=10)
    save_figure(fig, OUTPUT_DIR / "ensemble_accuracy_vs_k.png")

    md = [f"# Ensemble Majority-Vote Simulation",
          "",
          f"- **Images**: {len(images)} (multi-observation: {multi})",
          f"- **Simulations**: {args.n_sim} committee votes per image per K",
          "",
          "## Accuracy vs committee size K",
          "",
          "| K | accuracy | 95% CI | cost multiplier |",
          "|---:|---:|---|---:|",
          ]
    for k in ks:
        b = boots[k]
        md.append(f"| {k} | {b['estimate']:.3f} | {b['ci_lo']:.3f}-{b['ci_hi']:.3f} | {k}x |")
    md.append("")
    md.append("## Per-class accuracy by K (simulated)")
    md.append("")
    md.append("| class | " + " | ".join(f"K={k}" for k in ks) + " |")
    md.append("|" + "---:|" * (len(ks) + 1))
    for cls in sorted(per_class_by_k[ks[0]]):
        row = "| " + cls + " | " + " | ".join(
            f"{np.mean(per_class_by_k[k][cls]):.3f}" for k in ks) + " |"
        md.append(row)
    md.append("")
    path = OUTPUT_DIR / "ensemble_accuracy_vs_k.md"
    path.write_text("\n".join(md), encoding="utf-8")
    print(f"Report saved: {path}")

    # --- Escalation / routing ---
    rows = [conf[f] for f in conf]
    rows.sort(key=lambda r: r["confidence"])
    n = len(rows)
    n_esc_choices = [int(round(alpha * n)) for alpha in alpha_grid]
    curve = []
    for alpha, n_esc in zip(alpha_grid, n_esc_choices):
        kept = rows[n_esc:]
        escalated = rows[:n_esc]
        p_kept = [r["p_correct"] for r in kept]
        acc = (sum(p_kept) + len(escalated) * args.escalated_acc) / n
        boot = bootstrap(p_kept + [args.escalated_acc] * len(escalated),
                         lambda vals: float(np.mean(vals)), n_boot=args.n_boot, seed=args.seed)
        cost_factor = (1.0 - alpha) + alpha * args.escalated_cost_mult
        curve.append({
            "alpha": alpha, "n_escalated": n_esc, "kept": len(kept),
            "accuracy": acc, "ci_lo": boot["ci_lo"], "ci_hi": boot["ci_hi"],
            "cost_factor": cost_factor,
        })

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot([c["cost_factor"] for c in curve], [c["accuracy"] for c in curve],
            marker="o", color="#f39c12")
    for c in curve:
        ax.annotate(f"{c['alpha']:.0%}", (c["cost_factor"], c["accuracy"]),
                    textcoords="offset points", xytext=(0, 6), ha="center", fontsize=8)
    style_axis(ax, "Confidence-Gated Escalation: Accuracy vs Cost",
               "Cost factor (base = 1.0)", "Expected accuracy")
    save_figure(fig, OUTPUT_DIR / "routing_pareto.png")

    md = ["# Confidence-Gated Escalation Simulation",
          "",
          f"- **Escalated model accuracy**: {args.escalated_acc:.0%} (assumed)",
          f"- **Escalated cost multiplier**: {args.escalated_cost_mult}x",
          "",
          "| alpha | escalated | kept | accuracy | 95% CI | cost factor |",
          "|---:|---:|---:|---:|---:|---:|",
          ]
    for c in curve:
        md.append(f"| {c['alpha']:.0%} | {c['n_escalated']} | {c['kept']} | "
                  f"{c['accuracy']:.3f} | {c['ci_lo']:.3f}-{c['ci_hi']:.3f} | {c['cost_factor']:.2f}x |")
    md += ["",
           "## Sensitivity to the escalated-model accuracy assumption",
           "",
           "| alpha | accuracy @ acc-5pp | accuracy @ acc | accuracy @ acc+5pp |",
           "|---:|---:|---:|---:|",
           ]
    for alpha, n_esc in zip(alpha_grid, n_esc_choices):
        kept = rows[n_esc:]
        p_kept = [r["p_correct"] for r in kept]
        cells = []
        for shift in (-0.05, 0.0, 0.05):
            acc = (sum(p_kept) + n_esc * (args.escalated_acc + shift)) / n
            cells.append(f"{acc:.3f}")
        md.append(f"| {alpha:.0%} | {cells[0]} | {cells[1]} | {cells[2]} |")
    md += ["",
           "## Baseline (no escalation)",
           "",
           f"Observed single-pass accuracy: **{np.mean([r['p_correct'] for r in rows]):.3f}** "
           f"at cost 1.0x.",
           "",
           "## How to use",
           "",
           "Pick the smallest alpha whose accuracy meets the target; escalate the "
           "filenames in ``escalation_candidates.txt`` (top alpha fraction) through "
           "the stronger model and compare the measured vs simulated accuracy.",
           "",
           ]
    path = OUTPUT_DIR / "routing_abstention.md"
    path.write_text("\n".join(md), encoding="utf-8")
    print(f"Report saved: {path}")

    # Candidate list for the verification eval (top alpha fraction).
    top_alpha = alpha_grid[0]
    n_top = int(round(top_alpha * n))
    candidates = rows[:n_top]
    cand_path = OUTPUT_DIR / "escalation_candidates.txt"
    with cand_path.open("w", encoding="utf-8") as fh:
        fh.write(f"# Top {n_top} lowest-confidence images for escalation (alpha={top_alpha:.0%})\n")
        fh.write(f"# columns: filename | expected | mode | n_obs | confidence | margin | entropy | near_miss | uncertainty\n")
        for r in candidates:
            fh.write(f"{r['filename']} | {r['expected']} | {r['mode']} | {r['n_obs']} | "
                     f"{r['confidence']:.3f} | {r['margin']:.3f} | {r['entropy']:.3f} | "
                     f"{int(r['near_miss'])} | {int(r['uncertainty'])}\n")
    print(f"Candidates saved: {cand_path}")

    # Confidence histogram
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist([r["confidence"] for r in rows], bins=50, color="#3498db", edgecolor="white")
    style_axis(ax, "Image Confidence Distribution", "Confidence", "Images")
    save_figure(fig, OUTPUT_DIR / "confidence_histogram.png")


if __name__ == "__main__":
    run()
