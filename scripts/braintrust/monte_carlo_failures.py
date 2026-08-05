"""Monte Carlo simulation of the eval retry/failover/fallback pipeline.

Fits per-attempt failure probabilities from the corpus manifests (completed /
error / empty statuses, attempts histogram, fallback + finish_reason from the
span backfill) and optionally from the ``reports/eval_*.log`` retry markers, then
simulates the resilient runner's event loop — bounded retries per key, key
failover on quota errors, token doubling on ``finish_reason=length``, adaptive
throttling on 429s, and a fallback-model salvage pass — over a large number of
synthetic rows.

Answers, with zero API spend:
- expected failure rate for the CURRENT pipeline config, with a confidence band;
- expected failures (and tail risk) extrapolated to production scale (800 /
  25,000 / 320,000 images);
- how failure rate responds to ``--max-tries``, enabling/disabling the fallback
  model, and provider reliability (429 / transient error rates).

Usage:
    python scripts/braintrust/monte_carlo_failures.py
    python scripts/braintrust/monte_carlo_failures.py --max-tries 5 --fallback on
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # noqa: E402

import numpy as np
from matplotlib import pyplot as plt

from src.monte_carlo import save_figure, style_axis

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CORPUS = ROOT / "reports" / "monte_carlo" / "corpus.jsonl"
DEFAULT_LOGS_DIR = ROOT / "reports"
OUTPUT_DIR = ROOT / "reports" / "monte_carlo"

SCALE_TARGETS = (800, 25_000, 320_000)


def fit_corpus(records: list[dict]) -> dict:
    """Empirical per-attempt probabilities and row failure rates from manifests."""
    per_model: dict[str, dict] = defaultdict(lambda: {
        "total": 0, "completed": 0, "error": 0, "empty": 0,
        "attempts_one": 0, "fallback": 0, "length": 0,
    })
    for r in records:
        model = r.get("model") or "unknown"
        stats = per_model[model]
        stats["total"] += 1
        status = r.get("status")
        if status == "completed":
            stats["completed"] += 1
            if r.get("attempts") == 1:
                stats["attempts_one"] += 1
            if r.get("fallback"):
                stats["fallback"] += 1
            if r.get("finish_reason") == "length":
                stats["length"] += 1
        elif status == "error":
            stats["error"] += 1
        elif status == "empty":
            stats["empty"] += 1
    fitted: dict[str, dict] = {}
    for model, s in per_model.items():
        n = s["total"]
        if not n:
            continue
        p_row_fail = (s["error"] + s["empty"]) / n
        p_success_first = s["attempts_one"] / max(s["completed"], 1)
        p_length = s["length"] / max(s["completed"], 1)
        p_fallback_used = s["fallback"] / max(s["completed"], 1)
        fitted[model] = {
            **s,
            "p_row_fail": p_row_fail,
            "p_success_first": p_success_first,
            "p_length": p_length,
            "p_fallback_used": p_fallback_used,
        }
    return fitted


LOG_PATTERNS = {
    "length": re.compile(r"finish_reason=length"),
    "rate_limited": re.compile(r"Rate limited, waiting"),
    "quota": re.compile(r"WARN: OpenRouter key quota|all OpenRouter keys exhausted"),
    "error": re.compile(r"^ERROR:"),
}


def scan_logs(logs_dir: Path) -> dict[str, int]:
    """Count retry/failure markers across the eval logs."""
    counts: Counter = Counter()
    for path in sorted(logs_dir.glob("eval_*.log")):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for name, pattern in LOG_PATTERNS.items():
            counts[name] += len(pattern.findall(text))
    return dict(counts)


def simulate_pipeline(
    config: dict,
    n_rows: int,
    seed: int,
) -> dict:
    """Run the retry/failover/fallback event loop over ``n_rows`` synthetic rows.

    Per-attempt events: success, ``finish_reason=length`` (retry with doubled
    tokens), transient network error (retry), 429 (retry), quota (key failover),
    any remaining ``retryable`` mass (retry), and a ``terminal`` provider error
    (content filter / hard failure) that ends the row. Retries are bounded by
    ``max_tries`` per key across ``n_keys`` keys; exhausted rows get one
    fallback-model attempt when enabled.
    """
    rng = random.Random(seed)
    max_tries = config["max_tries"]
    n_keys = config["n_keys"]
    fallback = config["fallback"]
    p_success = config["p_success"]
    p_length = config["p_length"]
    p_transient = config["p_transient"]
    p_429 = config["p_429"]
    p_quota = config["p_quota"]
    p_terminal = config["p_terminal"]
    p_retryable = max(0.0, 1.0 - p_success - p_length - p_transient - p_429 - p_quota - p_terminal)
    p_fallback_success = config["p_fallback_success"]

    outcomes = {"completed": 0, "failed": 0}
    attempts_total = 0
    for _ in range(n_rows):
        key = 0
        attempts = 0
        completed = False
        max_attempts = max_tries * max(1, n_keys)
        for _ in range(max_attempts):
            attempts += 1
            roll = rng.random()
            if roll < p_success:
                completed = True
                break
            roll -= p_success
            if roll < p_length:
                continue
            roll -= p_length
            if roll < p_transient:
                continue
            roll -= p_transient
            if roll < p_429:
                continue
            roll -= p_429
            if roll < p_quota:
                if key + 1 < n_keys:
                    key += 1
                    continue
                break
            roll -= p_quota
            if roll < p_terminal:
                break
            # Remaining mass is retryable unknown errors; retry.
        if not completed and fallback:
            attempts += 1
            if rng.random() < p_fallback_success:
                completed = True
        outcomes["completed" if completed else "failed"] += 1
        attempts_total += attempts
    return {
        **outcomes,
        "failure_rate": outcomes["failed"] / n_rows,
        "avg_attempts": attempts_total / n_rows,
    }


def tail_risk(p_fail: float, n: int, n_sim: int, seed: int) -> dict:
    """MC distribution of failure counts at scale via binomial draws."""
    rng = np.random.default_rng(seed)
    draws = rng.binomial(n, p_fail, size=n_sim)
    return {
        "expected": float(np.mean(draws)),
        "ci_lo": float(np.percentile(draws, 2.5)),
        "ci_hi": float(np.percentile(draws, 97.5)),
        "p_gt_1pct": float(np.mean(draws > 0.01 * n)),
        "p_gt_5pct": float(np.mean(draws > 0.05 * n)),
    }


def run() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS,
                        help=f"Joint corpus JSONL (default: {DEFAULT_CORPUS})")
    parser.add_argument("--logs-dir", type=Path, default=DEFAULT_LOGS_DIR,
                        help="Directory scanned for eval_*.log retry markers")
    parser.add_argument("--max-tries", type=int, default=3)
    parser.add_argument("--n-keys", type=int, default=2,
                        help="Number of OpenRouter keys (primary + research funding)")
    parser.add_argument("--fallback", choices=["on", "off"], default="on",
                        help="Include the fallback-model salvage pass")
    parser.add_argument("--p-transient", type=float, default=None,
                        help="Per-attempt transient/network error probability (default: from logs)")
    parser.add_argument("--p-429", type=float, default=None,
                        help="Per-attempt upstream 429 probability (default: from logs)")
    parser.add_argument("--p-fallback-success", type=float, default=0.95,
                        help="Probability the fallback model produces a valid label")
    parser.add_argument("--n-sim", type=int, default=50_000,
                        help="Synthetic rows per pipeline simulation")
    parser.add_argument("--n-boot", type=int, default=10_000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    records = []
    for line in args.corpus.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    fitted = fit_corpus(records)
    log_counts = scan_logs(args.logs_dir)
    total_rows = sum(s["total"] for s in fitted.values()) or 1

    # Aggregate the primary model (largest row share) for the headline sim.
    primary = max(fitted.items(), key=lambda item: item[1]["total"])[0]
    stats = fitted[primary]
    p_success = stats["p_success_first"]
    p_length = stats["p_length"]
    p_transient = (log_counts.get("error", 0) / total_rows) if args.p_transient is None \
        else args.p_transient
    p_429 = (log_counts.get("rate_limited", 0) / total_rows) if args.p_429 is None \
        else args.p_429
    p_quota = log_counts.get("quota", 0) / total_rows
    p_fallback_success = args.p_fallback_success

    print(f"Primary model: {primary} ({stats['total']} rows)")
    print(f"  observed row failure rate: {stats['p_row_fail']:.3%} "
          f"(error={stats['error']}, empty={stats['empty']})")
    print(f"  P(first attempt success): {p_success:.3f}")
    print(f"  finish_reason=length:     {p_length:.3f}")
    print(f"  log markers -> transient {p_transient:.4f}, 429 {p_429:.4f}, quota {p_quota:.4f}")

    config = {
        "max_tries": args.max_tries,
        "n_keys": args.n_keys,
        "fallback": args.fallback == "on",
        "p_success": p_success,
        "p_length": p_length,
        "p_transient": p_transient,
        "p_429": p_429,
        "p_quota": p_quota,
        "p_terminal": stats["p_row_fail"],
        "p_fallback_success": p_fallback_success,
    }
    result = simulate_pipeline(config, args.n_sim, args.seed)
    print(f"\nSimulated pipeline ({args.n_sim} rows):")
    print(f"  failure rate:  {result['failure_rate']:.3%} "
          f"(vs observed {stats['p_row_fail']:.3%})")
    print(f"  avg attempts/row: {result['avg_attempts']:.2f}")

    md = [f"# Failure-Pipeline Monte Carlo",
          "",
          f"- **Primary model**: `{primary}`",
          f"- **Fitted**: P(first success)={p_success:.3f}, length={p_length:.3f}, "
          f"transient={p_transient:.4f}, 429={p_429:.4f}, quota={p_quota:.4f}",
          f"- **Config**: max_tries={args.max_tries}, keys={args.n_keys}, "
          f"fallback={args.fallback}",
          "",
          "## Current-pipeline simulation",
          "",
          f"- **Failure rate**: {result['failure_rate']:.3%} "
          f"(observed {stats['p_row_fail']:.3%})",
          f"- **Average attempts per row**: {result['avg_attempts']:.2f}",
          "",
          "## Extrapolated failures at scale",
          "",
          "| scale | expected | 95% CI | P(>1% failures) | P(>5% failures) |",
          "|---:|---:|---:|---:|---:|",
          ]
    for n in SCALE_TARGETS:
        tail = tail_risk(result["failure_rate"], n, 10_000, args.seed)
        md.append(f"| {n:,} | {tail['expected']:.0f} | "
                  f"{tail['ci_lo']:.0f}-{tail['ci_hi']:.0f} | "
                  f"{tail['p_gt_1pct']:.3f} | {tail['p_gt_5pct']:.3f} |")
    md.append("")

    # Sensitivity sweep over max_tries and fallback.
    sweep_rows = []
    for tries in (1, 2, 3, 5):
        for fallback in ("off", "on"):
            cfg = dict(config, max_tries=tries, fallback=fallback == "on")
            sim = simulate_pipeline(cfg, args.n_sim, args.seed)
            sweep_rows.append((tries, fallback, sim["failure_rate"], sim["avg_attempts"]))
    md += ["## Sensitivity sweep", "",
           "| max_tries | fallback | simulated failure rate | avg attempts/row |",
           "|---:|---|---:|---:|"]
    for tries, fallback, rate, attempts in sweep_rows:
        md.append(f"| {tries} | {fallback} | {rate:.3%} | {attempts:.2f} |")
    md.append("")

    path = OUTPUT_DIR / "failure_pipeline.md"
    path.write_text("\n".join(md), encoding="utf-8")
    print(f"Report saved: {path}")

    # Chart: failure rate vs tries, both fallback settings.
    tries_list = sorted({r[0] for r in sweep_rows})
    fig, ax = plt.subplots(figsize=(10, 6))
    for fallback in ("off", "on"):
        rates = [next(r[2] for r in sweep_rows if r[0] == t and r[1] == fallback)
                 for t in tries_list]
        ax.plot(tries_list, [r * 100 for r in rates], marker="o",
                label=f"fallback {fallback}")
    style_axis(ax, "Simulated Failure Rate vs Retry Budget",
               "MAX_TRIES", "Failure rate (%)")
    ax.legend(loc="upper right", fontsize=10)
    save_figure(fig, OUTPUT_DIR / "failure_rate_vs_tries.png")


if __name__ == "__main__":
    run()
