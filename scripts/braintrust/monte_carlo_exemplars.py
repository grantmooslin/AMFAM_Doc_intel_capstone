"""Mine high-leverage reasoning traces as few-shot exemplars for prompt iteration.

Every scratchpad trace that CORRECTLY classified an image while explicitly
navigating a confused pair (the runner-up line or the body names the decoy label)
is a candidate exemplar: it demonstrates the disambiguation the model most
often misses. This script:

1. tallies confusion pairs across the corpus;
2. finds, per pair, correct traces whose reasoning names the other label (the
   near-miss decoy) — these are the closest-call wins;
3. runs a Monte Carlo random search over exemplar subsets (bounded by an
   exemplar count and a token budget) with a simple surrogate: selecting an
   exemplar for pair ``(E -> P)`` is expected to flip ``efficacy x count`` of
   that pair's current errors;
4. writes the winning subset, the full traces, and a ready-to-paste exemplar
   appendix for the next prompt version.

No model spend: everything is derived from the existing corpus. Run this after
each new experiment so the exemplar bank tracks the latest confusion pairs.

Usage:
    python scripts/braintrust/monte_carlo_exemplars.py
    python scripts/braintrust/monte_carlo_exemplars.py --max-exemplars 8
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

from src.constants import DOCUMENT_CLASSES  # noqa: E402
from src.openrouter_classifier import extract_runner_up  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CORPUS = ROOT / "reports" / "monte_carlo" / "corpus.jsonl"
OUTPUT_DIR = ROOT / "reports" / "monte_carlo"

VALID_CLASSES = list(DOCUMENT_CLASSES)
EVIDENCE_TOKENS = (
    "header", "masthead", "salutation", "fields", "approval", "signature",
    "stamp", "journal", "volume", "doi", "shall", "masthead", "invoice",
    "budget", "check", "stub", "voucher", "memo", "letter", "bates",
    "facsimile", "fax", "form", "questionnaire", "label", "field",
)


def evidence_score(reasoning: str) -> float:
    """Heuristic clarity score: quoted evidence + concrete layout vocabulary."""
    if not reasoning:
        return 0.0
    lowered = reasoning.lower()
    quoted = len(re.findall(r"[\"']", reasoning))
    tokens = sum(1 for t in EVIDENCE_TOKENS if t in lowered)
    return 0.5 * min(1.0, quoted / 6.0) + 0.5 * min(1.0, tokens / 4.0)


def load_corpus(path: Path) -> list[dict]:
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def build_candidates(records: list[dict], min_pair_errors: int,
                     top_pairs: int, candidates_per_pair: int) -> tuple[dict, dict]:
    """Return (pair_stats, exemplar_candidates).

    ``pair_stats[(e, p)]`` = error count across observations. Candidates per pair
    are correct traces (expected == predicted) whose reasoning names the decoy.
    """
    pair_stats: Counter = Counter()
    by_pair: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in records:
        if r.get("status") != "completed":
            continue
        expected = r.get("expected")
        predicted = (r.get("predicted") or "").strip().lower()
        if predicted not in VALID_CLASSES:
            continue
        if predicted != expected:
            pair_stats[(expected, predicted)] += 1
        reasoning = r.get("reasoning") or ""
        if not reasoning or predicted != expected:
            continue
        runner_up = (r.get("runner_up") or "").strip().lower()
        if not runner_up:
            runner_up = extract_runner_up(reasoning).strip().lower()
        # A correct trace whose runner-up names a different class demonstrates
        # exactly the disambiguation for that (expected, decoy) pair — the model
        # walked to the right answer while explicitly rejecting the decoy.
        if runner_up in VALID_CLASSES and runner_up != expected:
            by_pair[(expected, runner_up)].append({
                "filename": r["filename"],
                "model": r.get("model") or "",
                "prompt_version": r.get("prompt_version") or "",
                "expected": expected,
                "decoy": runner_up,
                "runner_up": runner_up,
                "reasoning": reasoning,
                "reasoning_len": len(reasoning),
                "clarity": evidence_score(reasoning),
            })

    candidates: dict[tuple[str, str], list[dict]] = {}
    for pair, count in pair_stats.items():
        if count < min_pair_errors:
            continue
        pool = sorted(by_pair.get(pair, []), key=lambda c: -c["clarity"])
        if pool:
            candidates[pair] = pool[:candidates_per_pair]
    return dict(pair_stats), candidates


def subset_gain(selected: list[dict], efficacy: float,
                per_pair_extra: float, pair_stats: Counter) -> float:
    """Expected errors flipped by ``selected`` exemplars, by confusion pair."""
    by_pair: Counter = Counter()
    for exemplar in selected:
        by_pair[(exemplar["expected"], exemplar["decoy"])] += 1
    gain = 0.0
    for pair, n_sel in by_pair.items():
        multiplier = efficacy * (1.0 + per_pair_extra * (n_sel - 1))
        gain += multiplier * pair_stats.get(pair, 0)
    return gain


def random_search(pairs: list[tuple[tuple[str, str], int]], candidates: dict,
                  pair_stats: Counter, n_iter: int, max_exemplars: int,
                  token_budget: int, efficacy: float, per_pair_extra: float,
                  p_select: float, seed: int) -> dict:
    """Monte Carlo search for the exemplar subset with the largest expected gain."""
    rng = random.Random(seed)
    best = None
    best_gain = -1.0
    for _ in range(n_iter):
        chosen: list[dict] = []
        for pair, _count in pairs:
            pool = candidates.get(pair, [])
            if not pool or rng.random() >= p_select:
                continue
            chosen.append(rng.choice(pool))
            if len(chosen) >= max_exemplars:
                break
        if not chosen:
            continue
        if sum(c["reasoning_len"] for c in chosen) > token_budget:
            continue
        gain = subset_gain(chosen, efficacy, per_pair_extra, pair_stats)
        if gain > best_gain:
            best_gain = gain
            best = chosen
    return {"subset": best or [], "gain": best_gain}


def run() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS,
                        help=f"Joint corpus JSONL (default: {DEFAULT_CORPUS})")
    parser.add_argument("--min-pair-errors", type=int, default=3,
                        help="Only consider confusion pairs with at least this many errors")
    parser.add_argument("--top-pairs", type=int, default=12,
                        help="Number of most-confused pairs to target")
    parser.add_argument("--candidates-per-pair", type=int, default=8)
    parser.add_argument("--n-iter", type=int, default=10_000,
                        help="Monte Carlo subset-search iterations")
    parser.add_argument("--max-exemplars", type=int, default=8)
    parser.add_argument("--token-budget", type=int, default=12_000,
                        help="Max total exemplar characters (proxy for prompt tokens)")
    parser.add_argument("--efficacy", type=float, default=0.25,
                        help="Expected fraction of a pair's errors flipped by one exemplar")
    parser.add_argument("--per-pair-extra", type=float, default=0.5,
                        help="Diminishing-return multiplier for a second exemplar on the same pair")
    parser.add_argument("--p-select", type=float, default=0.5,
                        help="Probability a pair is selected per random-search iteration")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    records = load_corpus(args.corpus)
    pair_stats, candidates = build_candidates(records, args.min_pair_errors,
                                              args.top_pairs, args.candidates_per_pair)
    targeted = sorted(pair_stats.items(), key=lambda item: -item[1])[:args.top_pairs]
    targeted = [(pair, count) for pair, count in targeted if pair in candidates]
    if not targeted:
        print("No targetable confusion pairs found; lower --min-pair-errors.")
        return

    best = random_search(targeted, candidates, pair_stats, args.n_iter,
                         args.max_exemplars, args.token_budget, args.efficacy,
                         args.per_pair_extra, args.p_select, args.seed)
    subset = best["subset"]
    total_errors = sum(pair_stats.values()) or 1
    gain_pp = best["gain"] / total_errors

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    md = [f"# Few-Shot Exemplar Mining",
          "",
          f"- **Corpus**: {args.corpus}",
          f"- **Targeted pairs**: {len(targeted)} (from {len(pair_stats)} total)",
          f"- **Surrogate**: efficacy={args.efficacy}, second-exemplar multiplier="
          f"{1 + args.per_pair_extra}",
          "",
          f"## Simulated gain",
          "",
          f"- **Expected errors flipped**: {best['gain']:.1f} of {int(total_errors)} "
          f"corpus errors ({gain_pp:.2%} of the error pool)",
          f"- **Exemplars selected**: {len(subset)} (token cost "
          f"{sum(c['reasoning_len'] for c in subset)}/{args.token_budget} chars)",
          "",
          "## Confusion pairs targeted",
          "",
          "| expected | predicted-as | errors | exemplars available |",
          "|---|---:|---:|---:|",
          ]
    for pair, _count in targeted:
        pool = candidates[pair]
        md.append(f"| {pair[0]} | {pair[1]} | {pair_stats[pair]} | {len(pool)} |")
    md.append("")

    md += ["## Selected exemplars", ""]
    for i, exemplar in enumerate(subset, start=1):
        md.append(f"### {i}. `{exemplar['filename']}` ({exemplar['model'].split('/')[-1]}, "
                  f"{exemplar['prompt_version']})")
        md.append(f"**expected**: `{exemplar['expected']}` | **decoy**: `{exemplar['decoy']}` | "
                  f"**runner_up**: `{exemplar['runner_up']}` | **clarity**: {exemplar['clarity']:.2f}")
        md.append("")
        md.append(f"```")
        md.append(exemplar["reasoning"].strip())
        md.append("```")
        md.append("")

    appendix = []
    for i, exemplar in enumerate(subset, start=1):
        appendix.append(f"### Worked example {i} — {exemplar['expected']} vs {exemplar['decoy']}")
        appendix.append("")
        appendix.append(exemplar["reasoning"].strip())
        appendix.append("")
    appendix_text = "\n".join(appendix)
    md += ["## Proposed exemplar appendix (copy into the next prompt version)", ""]
    md.append("```")
    md.append(appendix_text)
    md.append("```")
    md.append("")

    path = OUTPUT_DIR / "exemplar_candidates.md"
    path.write_text("\n".join(md), encoding="utf-8")
    print(f"Report saved: {path}")
    print(f"\nSimulated gain: {best['gain']:.1f} errors flipped ({gain_pp:.2%} of error pool)")
    print(f"Selected {len(subset)} exemplars across {len(targeted)} targeted pairs:")
    for exemplar in subset:
        print(f"  {exemplar['expected']:<22} {exemplar['decoy']:<14} "
              f"{exemplar['filename']} ({exemplar['model'].split('/')[-1]}, "
              f"{exemplar['prompt_version']})")


if __name__ == "__main__":
    run()
