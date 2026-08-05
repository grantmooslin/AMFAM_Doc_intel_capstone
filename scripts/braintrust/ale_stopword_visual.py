"""ALE (Accumulated Local Effects) and stop-word visualization for reasoning traces.

Reads the joint Monte Carlo corpus (``reports/monte_carlo/corpus.jsonl``),
parses each reasoning trace into its check-by-check structure, and answers two
interpretability questions with zero API spend:

1. **ALE charts** — how do continuous reasoning features (reasoning length,
   number of checks walked, stop position, token budget, cost, retry attempts)
   affect the probability of a *correct* classification? ALE isolates the local
   effect of a single feature while averaging over the others, so these curves
   show, e.g., whether walking more checks really buys accuracy or whether a
   longer scratchpad mostly signals uncertainty.

2. **Stop-word visualization** — which words/phrases in the *stopping evidence*
   (the concrete header words, field labels, and mastheads the model quotes at
   the check where it commits) trigger the model to **over-hastily stop** before
   completing the 1-14 check cascade — i.e. words whose presence is associated
   with an earlier stop than baseline *and* a higher-than-baseline error rate.

Outputs (into ``--out-dir``, default ``reports/monte_carlo/``):

- ``ale_correctness_<scope>.png`` — multi-panel ALE curves with 95% bootstrap CI
- ``stop_word_hasty.png`` — top trigger words ranked by a hasty-stop score
- ``stop_word_scatter.png`` — stop-position vs error-rate bubble chart
- ``ale_stopword_report.md`` — methodology + full word table

Usage:
    python scripts/braintrust/ale_stopword_visual.py
    python scripts/braintrust/ale_stopword_visual.py --corpus reports/monte_carlo/corpus.jsonl
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # noqa: E402

import numpy as np
from matplotlib import pyplot as plt

from src.constants import DOCUMENT_CLASSES  # noqa: E402
from src.monte_carlo import load_corpus, save_figure, style_axis  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CORPUS = ROOT / "reports" / "monte_carlo" / "corpus.jsonl"
DEFAULT_OUT = ROOT / "reports" / "monte_carlo"

CLASS_BY_INDEX = {name: i + 1 for i, name in enumerate(DOCUMENT_CLASSES)}

# ---------------------------------------------------------------------------
# Reasoning trace parsing
# ---------------------------------------------------------------------------

# v11.8-style bold header: **Check 1: file_folder** (may also appear un-bolded
# as "- Check 10: ADMINISTRATIVE FORM -> form" in some traces).
CHECK_HEADER_RE = re.compile(
    r"(?:^|\n)\s*[-*# ]*\**\s*Check\s+(\d+):\s*([^*\n]+?)\s*\**\s*(?:\n|$)",
    re.I,
)
# v0-style numbered evaluation: **Check 7: invoice?** Yes./No.
CHECK_EVAL_RE = re.compile(
    r"-\s*\*\*Check\s+(\d+):\s*([a-z_]+)\?\*\*\s*(Yes|No)\.?",
    re.I,
)
# v0-style label evaluation (no number): - **advertisement**: No.
LABEL_EVAL_RE = re.compile(
    r"-\s*\*\*(advertisement|budget|email|file_folder|form|handwritten|invoice|"
    r"letter|memo|news_article|presentation|questionnaire|resume|"
    r"scientific_publication|scientific_report|specification)\*\*:",
    re.I,
)

STOP_POSITIVE_RE = re.compile(
    r"\bStop here\.?\b|Result:\s*YES|Result:\s*yes\b|yes\s*—|yes\.$|^\s*Yes\.|"
    r"Final label|final label|final decision",  # noqa: E501
    re.I,
)
EVIDENCE_LINE_RE = re.compile(r"[Ee]vidence:\s*(.+)")
STOP_MARKER_RE = re.compile(r"Result:\s*not this check|not this check|^\s*No\.", re.I)


def _verdict_from_section(section: str, verdict_hint: str = "") -> str:
    """Classify a check section as 'yes'/'no' from its text."""
    if verdict_hint:
        return verdict_hint.lower()
    if STOP_MARKER_RE.search(section):
        return "no"
    if STOP_POSITIVE_RE.search(section):
        return "yes"
    return "no"


def parse_reasoning(reasoning: str) -> dict | None:
    """Parse a reasoning trace into ordered checks + stop point.

    Returns ``{format, checks: [(num, label, verdict)], stop_position,
    checks_walked, stop_evidence}`` or ``None`` when no check structure is
    found. ``stop_position`` is the first positively-verdict'ed check number, or
    ``None`` when the model walked every check without committing early.
    """
    if not reasoning:
        return None

    # --- v11.8 / v0-style numbered headers: **Check N: name** ---
    headers = list(CHECK_HEADER_RE.finditer(reasoning))
    if headers:
        sections: list[tuple[int, str, str]] = []
        for i, m in enumerate(headers):
            end = headers[i + 1].start() if i + 1 < len(headers) else len(reasoning)
            section = reasoning[m.end():end]
            num = int(m.group(1))
            label = m.group(2).strip().strip("?").strip().lower()
            verdict = _verdict_from_section(section)
            sections.append((num, label, verdict, section))
        return _finish_parse("header", sections)

    # --- v0 numbered evaluations: **Check N: label?** Yes./No. ---
    evals = list(CHECK_EVAL_RE.finditer(reasoning))
    if evals:
        sections = []
        for i, m in enumerate(evals):
            end = evals[i + 1].start() if i + 1 < len(evals) else len(reasoning)
            section = reasoning[m.end():end]
            num = int(m.group(1))
            label = m.group(2).strip().lower()
            verdict = m.group(3).lower()
            sections.append((num, label, verdict, section))
        return _finish_parse("check-eval", sections)

    # --- v0 label evaluations: - **label**: (16 labels in class order) ---
    labels = list(LABEL_EVAL_RE.finditer(reasoning))
    if labels:
        sections = []
        for i, m in enumerate(labels):
            end = labels[i + 1].start() if i + 1 < len(labels) else len(reasoning)
            section = reasoning[m.end():end]
            label = m.group(1).strip().lower()
            num = CLASS_BY_INDEX.get(label, 0)
            verdict = _verdict_from_section(section)
            sections.append((num, label, verdict, section))
        return _finish_parse("label-eval", sections)

    return None


def _finish_parse(fmt: str, sections: list[tuple[int, str, str, str]]) -> dict | None:
    if not sections:
        return None
    checks = [(num, label, verdict) for num, label, verdict, _ in sections]
    stop_position = None
    stop_evidence = ""
    for num, label, verdict, section in sections:
        if verdict == "yes":
            stop_position = num
            stop_evidence = _extract_evidence(section)
            break
    distinct = {num for num, _, _ in checks if num}
    checks_walked = len(distinct) if distinct else len(checks)
    return {
        "format": fmt,
        "checks": checks,
        "stop_position": stop_position,
        "checks_walked": checks_walked,
        "stop_evidence": stop_evidence,
    }


def _extract_evidence(section: str) -> str:
    """Pull the concrete evidence the model quoted at the stopping check.

    Prefers ``Evidence:`` lines (v11.8 style); falls back to the raw section
    minus its verdict markers (v0 style).
    """
    lines = [m.group(1).strip() for m in EVIDENCE_LINE_RE.finditer(section)]
    if lines:
        return " ".join(lines)
    cleaned = STOP_POSITIVE_RE.sub(" ", section)
    cleaned = STOP_MARKER_RE.sub(" ", cleaned)
    return cleaned.strip()


# ---------------------------------------------------------------------------
# Stop-word tokenization
# ---------------------------------------------------------------------------

STOPWORDS = frozenset(
    """a an and are as at be but by for from has have in is it its of on or that the
    this to was were with will would no not none yes page document text contains look
    looks looking see seen there here what which whose when where why how i me my we
    you your it's don't doesn't isn't can't cannot could should would have been being
    does did doing had having than then them they these those each other some such only
    just also very more most less least likely clearly obviously probably however
    therefore because if then else nor but or yet so rather quite""".split()
)
TOKEN_RE = re.compile(r"[a-z][a-z0-9'_\-]{2,}")
QUOTED_RE = re.compile(
    r"[\"'\u2018\u2019\u201c\u201d]([^\"'\u2018\u2019\u201c\u201d]{3,80})"
    r"[\"'\u2018\u2019\u201c\u201d]"
)


def tokenize_evidence(text: str) -> list[str]:
    """Lowercase word tokens from stop evidence, minus generic stopwords.

    Prefers the *quoted* spans — the concrete page text (header words, field
    labels, mastheads) the model cites as the basis for its commit — and falls
    back to the whole evidence section for traces with no quoted text. These
    quoted tokens are the high-signal triggers the hasty-stop analysis ranks.
    """
    if not text:
        return []
    spans = [m.group(1) for m in QUOTED_RE.finditer(text)]
    if not spans:
        spans = [text]
    tokens = []
    for span in spans:
        for tok in TOKEN_RE.findall(span.lower()):
            if tok in STOPWORDS:
                continue
            tokens.append(tok)
    return tokens


# ---------------------------------------------------------------------------
# ALE (Accumulated Local Effects)
# ---------------------------------------------------------------------------

def accumulated_local_effects(
    x: list[float],
    y: list[float],
    n_bins: int = 20,
    n_boot: int = 200,
    seed: int = 42,
) -> dict | None:
    """ALE of feature ``x`` on binary outcome ``y`` with bootstrap CI.

    Implementation notes: with only observational outcomes (no queryable model)
    the boundary predictions ``f(z_k, x_i^{(-j)})`` are approximated by the mean
    outcome of the data points inside each quantile interval, so the local
    effect of interval ``k`` is ``mean(y | x in bin k) - mean(y | x in bin k-1)``
    and the ALE is their centered cumulative sum. Confidence bands come from
    resampling the whole binning+accumulation procedure (``n_boot`` draws).
    """
    x_arr = np.asarray(x, dtype=float)
    y_arr = np.asarray(y, dtype=float)
    valid = np.isfinite(x_arr) & np.isfinite(y_arr)
    x_arr, y_arr = x_arr[valid], y_arr[valid]
    n = len(x_arr)
    if n < 4 or len(np.unique(x_arr)) < 3:
        return None

    # Fixed quantile edges from the full data so every bootstrap draw shares the
    # same bin centers.
    edges = np.unique(np.quantile(x_arr, np.linspace(0.0, 1.0, n_bins + 1)))
    if len(edges) < 3:
        edges = np.unique(x_arr)
    k_bins = len(edges) - 1
    centers = (edges[:-1] + edges[1:]) / 2.0

    def _ale(xs, ys):
        bins = np.clip(np.searchsorted(edges, xs, side="right") - 1, 0, k_bins - 1)
        bin_mean = np.full(k_bins, np.nan)
        for k in range(k_bins):
            mask = bins == k
            if mask.any():
                bin_mean[k] = ys[mask].mean()
        for k in range(1, k_bins):  # forward-fill empty interior bins
            if np.isnan(bin_mean[k]):
                bin_mean[k] = bin_mean[k - 1]
        le = np.zeros(k_bins)
        for k in range(1, k_bins):
            le[k] = bin_mean[k] - bin_mean[k - 1]
        ale = np.cumsum(le)
        counts = np.bincount(bins, minlength=k_bins)
        wmean = np.average(ale, weights=counts) if counts.sum() else 0.0
        return ale - wmean

    ale = _ale(x_arr, y_arr)
    rng = np.random.default_rng(seed)
    boot = np.empty((n_boot, k_bins))
    for b in range(n_boot):
        idx = rng.integers(0, n, size=n)
        boot[b] = _ale(x_arr[idx], y_arr[idx])
    ci_lo = np.nanpercentile(boot, 2.5, axis=0)
    ci_hi = np.nanpercentile(boot, 97.5, axis=0)
    return {
        "centers": centers,
        "ale": ale,
        "ci_lo": ci_lo,
        "ci_hi": ci_hi,
        "n": int(n),
    }


# ---------------------------------------------------------------------------
# Stop-word analysis
# ---------------------------------------------------------------------------

def stop_word_analysis(rows: list[dict], min_count: int = 8) -> list[dict]:
    """Rank stop-evidence words by how hasty + error-prone their triggers are.

    For every word appearing in a trace's stopping evidence, collects the stop
    position and correctness of that trace. Returns words ranked by
    ``hasty_score``:

    ``score = early_lift * max(err_lift, 0) * sqrt(freq)``

    where ``early_lift`` is how many checks earlier than baseline the model
    stops when the word triggers it (normalized to ``[0, 1]`` against the
    baseline stop position) and ``err_lift`` is the word's error rate minus the
    baseline error rate. Words that stop the model *and* push it toward
    misclassification rank highest; words that trigger only accurate early stops
    (a correctly-read clear signal) rank low.
    """
    rows_with_stop = [r for r in rows if r.get("stop_position")]
    if not rows_with_stop:
        return []

    baseline_stop = float(np.mean([r["stop_position"] for r in rows_with_stop]))
    baseline_err = float(np.mean([0.0 if r["correct"] else 1.0 for r in rows_with_stop]))

    word_items: dict[str, list[tuple[int, bool]]] = defaultdict(list)
    for r in rows_with_stop:
        for tok in tokenize_evidence(r.get("stop_evidence") or ""):
            word_items[tok].append((r["stop_position"], r["correct"]))

    results = []
    for word, items in word_items.items():
        if len(items) < min_count:
            continue
        positions = [p for p, _ in items]
        corrects = [c for _, c in items]
        avg_stop = float(np.mean(positions))
        err_rate = 1.0 - float(np.mean(corrects))
        early_lift = max(0.0, (baseline_stop - avg_stop) / max(baseline_stop - 1.0, 1e-9))
        err_lift = err_rate - baseline_err
        score = early_lift * max(err_lift, 0.0) * float(np.sqrt(len(items)))
        results.append({
            "word": word,
            "freq": len(items),
            "avg_stop_position": round(avg_stop, 2),
            "error_rate": round(err_rate, 4),
            "early_lift": round(early_lift, 4),
            "err_lift": round(err_lift, 4),
            "hasty_score": round(score, 4),
        })
    results.sort(key=lambda d: d["hasty_score"], reverse=True)
    return results


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

def plot_ale(rows: list[dict], scope: str, out_dir: Path, n_bins: int = 20) -> None:
    """Multi-panel ALE of reasoning features on P(correct)."""
    features = [
        ("reasoning_len", "Reasoning length (chars)"),
        ("checks_walked", "Checks walked before stop"),
        ("stop_position", "Stop position (check #)"),
        ("max_tokens", "Token budget"),
        ("cost", "Cost (USD)"),
        ("attempts", "Attempts"),
    ]
    panels = []
    for key, label in features:
        pts = [(r[key], 1.0 if r["correct"] else 0.0) for r in rows
               if r.get(key) is not None and np.isfinite(r[key])]
        if len(pts) < 20:
            continue
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        res = accumulated_local_effects(xs, ys, n_bins=n_bins)
        if res is None:
            print(f"  skipping ALE panel for '{key}' (no variation / too few points)")
            continue
        panels.append((key, label, res))

    if not panels:
        print("  no ALE panels computable")
        return

    ncols = 2
    nrows = int(np.ceil(len(panels) / ncols))
    fig, axes = plt.subplots(nrows, ncols, figsize=(13, 3.4 * nrows))
    axes = np.atleast_1d(axes).ravel()
    for ax, (key, label, res) in zip(axes, panels):
        if res is None:
            ax.set_visible(False)
            continue
        ax.fill_between(res["centers"], res["ci_lo"], res["ci_hi"],
                        color="#3366cc", alpha=0.15)
        ax.plot(res["centers"], res["ale"], color="#1f3d7a", lw=2)
        ax.axhline(0.0, color="gray", lw=0.8, ls="--")
        style_axis(ax, f"ALE of {label}", label, "Effect on P(correct)")
        ax.grid(alpha=0.3)
    for ax in axes[len(panels):]:
        ax.set_visible(False)
    fig.suptitle(
        f"Accumulated Local Effects on Classification Accuracy — {scope}\n"
        f"{rows[0]['model']} / prompt {rows[0]['prompt_version']} "
        f"({len(rows)} rows)",
        fontsize=13, fontweight="bold",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    save_figure(fig, out_dir / f"ale_correctness_{scope}.png")


def plot_stop_words(words: list[dict], out_dir: Path, top_n: int = 20) -> None:
    """Horizontal bar chart of the top hasty-stop trigger words."""
    top = words[:top_n][::-1]
    if not top:
        print("  no stop words to plot")
        return
    labels = [w["word"] for w in top]
    scores = [w["hasty_score"] for w in top]
    errs = [w["error_rate"] for w in top]

    fig, ax = plt.subplots(figsize=(11, 0.42 * len(top) + 2))
    colors = ["#e74c3c" if e >= 0.5 else "#f39c12" if e >= 0.3 else "#2ecc71"
              for e in errs]
    bars = ax.barh(labels, scores, color=colors, edgecolor="gray", linewidth=0.5)
    for bar, w in zip(bars, top):
        ax.text(
            bar.get_width() + 0.01, bar.get_y() + bar.get_height() / 2,
            f"stop@#{w['avg_stop_position']:.0f} · err {w['error_rate']:.0%} · n={w['freq']}",
            va="center", fontsize=8,
        )
    ax.set_xlim(0, max(scores) * 1.45)
    style_axis(
        ax,
        "Hasty-Stop Trigger Words (stop early + err above baseline)",
        "Hasty-stop score (early_lift × err_lift × √freq)",
        "",
    )
    ax.grid(alpha=0.3, axis="x")
    fig.tight_layout()
    save_figure(fig, out_dir / "stop_word_hasty.png")


def plot_stop_scatter(words: list[dict], out_dir: Path) -> None:
    """Bubble chart: stop position vs error rate per trigger word."""
    if not words:
        print("  no stop words to plot")
        return
    top = words[:40]
    fig, ax = plt.subplots(figsize=(11, 7))
    xs = [w["avg_stop_position"] for w in top]
    ys = [w["error_rate"] * 100 for w in top]
    sizes = [20 + 55 * np.log1p(w["freq"]) for w in top]
    sc = ax.scatter(xs, ys, s=sizes, alpha=0.65, c=[w["hasty_score"] for w in top],
                    cmap="RdYlBu_r", edgecolor="gray", linewidth=0.5)
    for w in top[:18]:
        ax.annotate(w["word"], (w["avg_stop_position"], w["error_rate"] * 100),
                    fontsize=7.5, xytext=(4, 3), textcoords="offset points")
    ax.axvspan(1, 6, color="#e74c3c", alpha=0.06, label="early-stop zone")
    ax.axhline(50, color="gray", ls="--", lw=0.8, alpha=0.6)
    ax.set_xlabel("Mean stop position (check #) when word triggers", fontsize=12)
    ax.set_ylabel("Error rate when word triggers (%)", fontsize=12)
    ax.set_title("Stop-Word Trigger Geography: early + wrong = hasty",
                 fontsize=13, fontweight="bold")
    ax.legend(loc="lower right", fontsize=9)
    cbar = fig.colorbar(sc, ax=ax, shrink=0.7)
    cbar.set_label("hasty score", fontsize=10)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    save_figure(fig, out_dir / "stop_word_scatter.png")


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def write_report(rows: list[dict], words: list[dict], out_dir: Path,
                 n_bins: int) -> None:
    baseline_stop_rows = [r for r in rows if r.get("stop_position")]
    parsed = sum(1 for r in rows if r.get("checks_walked"))
    stopped = len(baseline_stop_rows)
    baseline_stop = np.mean([r["stop_position"] for r in baseline_stop_rows]) if stopped else 0
    overall_err = np.mean([0.0 if r["correct"] else 1.0 for r in rows])

    md = [
        "# ALE + Stop-Word Analysis of Reasoning Traces",
        "",
        f"- **Corpus rows**: {len(rows)} (reasoning-covered)",
        f"- **Traces parsed into checks**: {parsed}",
        f"- **Traces with an explicit stop**: {stopped}",
        f"- **Baseline stop position**: {baseline_stop:.1f} of 14 checks",
        f"- **Overall error rate**: {overall_err:.1%}",
        "",
        "## ALE (Accumulated Local Effects)",
        "",
        "ALE of each reasoning feature on the probability of a correct label, "
        "computed with 20 quantile bins and a 200-draw bootstrap. A rising curve "
        "means more of the feature is associated with higher accuracy; a falling "
        "curve means it is associated with error. Because ALE averages out "
        "correlated features locally, the curves isolate each feature's own "
        "effect rather than the raw marginal trend.",
        "",
        f"![ALE curves](ale_correctness_{rows[0].get('scope', 'all')}.png)",
        "",
        "## Hasty-stop trigger words",
        "",
        "Words below are quoted in the stopping evidence of traces where the "
        "model committed to a label. `hasty_score` combines how much earlier "
        "than baseline the stop happens (`early_lift`) with how much the error "
        "rate rises (`err_lift`), weighted by frequency — a high score means the "
        "word pushes the model to over-hastily commit before finishing the "
        "check cascade, and that commit is wrong above the baseline rate.",
        "",
        "| word | n | avg stop # | error rate | early_lift | err_lift | hasty_score |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for w in words[:25]:
        md.append(
            f"| {w['word']} | {w['freq']} | {w['avg_stop_position']:.1f} | "
            f"{w['error_rate']:.0%} | {w['early_lift']:.2f} | {w['err_lift']:+.2f} | "
            f"{w['hasty_score']:.3f} |"
        )
    md += [
        "",
        "![Hasty stop words](stop_word_hasty.png)",
        "",
        "![Stop-word trigger geography](stop_word_scatter.png)",
        "",
    ]
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "ale_stopword_report.md"
    path.write_text("\n".join(md), encoding="utf-8")
    print(f"Report saved: {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def build_rows(records: list[dict]) -> list[dict]:
    """Project corpus records into analysis rows (correct, parsed features)."""
    rows = []
    for r in records:
        reasoning = r.get("reasoning") or ""
        if not reasoning.strip() or r.get("status") not in ("completed", ""):
            continue
        parsed = parse_reasoning(reasoning)
        correct = (r.get("predicted") or "").strip().lower() == \
            (r.get("expected") or "").strip().lower()
        rows.append({
            "filename": r.get("filename"),
            "model": r.get("model"),
            "prompt_version": r.get("prompt_version"),
            "expected": r.get("expected"),
            "predicted": r.get("predicted"),
            "correct": correct,
            "reasoning_len": r.get("reasoning_len"),
            "cost": r.get("cost"),
            "max_tokens": r.get("max_tokens"),
            "attempts": r.get("attempts"),
            "checks_walked": parsed["checks_walked"] if parsed else None,
            "stop_position": parsed["stop_position"] if parsed else None,
            "stop_evidence": parsed["stop_evidence"] if parsed else "",
        })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS,
                        help=f"Corpus JSONL (default: {DEFAULT_CORPUS})")
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT,
                        help=f"Output dir (default: {DEFAULT_OUT})")
    parser.add_argument("--min-count", type=int, default=8,
                        help="Min stop-evidence occurrences for a trigger word")
    parser.add_argument("--n-bins", type=int, default=20,
                        help="ALE quantile bins")
    parser.add_argument("--scope", default="all",
                        help="Label for output filenames (default: all)")
    parser.add_argument("--prompt-version", default=None,
                        help="Restrict to one prompt version, e.g. v11.8 "
                             "(default: all versions, which mix the v0 flat "
                             "16-label evaluation with the v11.8 1-14 cascade)")
    args = parser.parse_args()

    records = load_corpus(args.corpus)
    rows = build_rows(records)
    rows = [r for r in rows if r.get("reasoning_len", 0) > 0]
    if args.prompt_version:
        rows = [r for r in rows if r.get("prompt_version") == args.prompt_version]
    for r in rows:
        r["scope"] = args.scope
    print(f"Loaded {len(records)} corpus records; "
          f"{len(rows)} rows with reasoning"
          + (f" (prompt {args.prompt_version})" if args.prompt_version else ""))

    args.out_dir.mkdir(parents=True, exist_ok=True)
    plot_ale(rows, args.scope, args.out_dir, n_bins=args.n_bins)

    words = stop_word_analysis(rows, min_count=args.min_count)
    if words:
        print(f"Top hasty-stop words ({len(words)} total ≥{args.min_count} occurrences):")
        for w in words[:10]:
            print(f"  {w['word']:<22} stop@#{w['avg_stop_position']:.0f} "
                  f"err {w['error_rate']:.0%} score {w['hasty_score']:.3f}")
        plot_stop_words(words, args.out_dir)
        plot_stop_scatter(words, args.out_dir)
    else:
        print("No stop words found (raise --min-count or check parsing).")

    write_report(rows, words, args.out_dir, args.n_bins)
    print("Done.")


if __name__ == "__main__":
    main()
