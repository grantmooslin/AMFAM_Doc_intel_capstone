"""Generate the Quarto website source (.qmd files) from committed docs/reports.

Deterministic and rerunnable: run ``python scripts/site/build_site.py`` after
pulling in new experiments/docs to regenerate the ``website/`` pages, then
``quarto render website/`` and publish.

Hand-authored pages (``website/index.qmd``, ``website/methods/overview.qmd``,
``website/results/headline-results.qmd``) are left untouched.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WEBSITE = ROOT / "website"
CHARTS = WEBSITE / "charts"

GITHUB_BLOB = "https://github.com/Exios66/AMFAM_capstone/blob/main/"

# ---------------------------------------------------------------------------
# Corruption fixes for experiment_log.md (a `$0.` sequence was expanded by zsh
# into `/bin/zsh.` when the log was written). Values restored from the report
# files in reports/experiment_reports/.
# ---------------------------------------------------------------------------

EXP_LOG_FIXES = [
    (
        "**Pricing:** /bin/zsh.03/M input, /bin/zsh.13/M output. Expected /bin/zsh.1792 (list price × measured tokens); actual billed /bin/zsh.1773 (+1.1%).\n\n| Images | Expected Cost | Estimated Actual |\n|--------|--------------:|-----------------:|\n| 800 | /bin/zsh.18 | /bin/zsh.18 |\n| 25,000 | .60 | .54 |\n| 320,000 | .68 | .92 |",
        "**Pricing:** $0.03/M input, $0.13/M output. Expected $0.1792 (list price × measured tokens); actual billed $0.1773 (+1.1%).\n\n| Images | Expected Cost | Estimated Actual |\n|--------|--------------:|-----------------:|\n| 800 | $0.18 | $0.18 |\n| 25,000 | $5.60 | $5.54 |\n| 320,000 | $71.68 | $70.92 |",
    ),
    (
        "**Pricing:** /bin/zsh.03/M input (/bin/zsh.003/M cached), /bin/zsh.13/M output. Heavy prompt caching (~61% of prompt tokens cached). Expected /bin/zsh.3276 (cache-adjusted); actual billed /bin/zsh.3427 (+4.6%).\n\n| Images | Expected Cost | Estimated Actual |\n|--------|--------------:|-----------------:|\n| 800 | /bin/zsh.33 | /bin/zsh.34 |\n| 25,000 | .24 | .71 |\n| 320,000 | .04 | .08 |",
        "**Pricing:** $0.03/M input ($0.003/M cached), $0.13/M output. Heavy prompt caching (~61% of prompt tokens cached). Expected $0.3276 (cache-adjusted); actual billed $0.3427 (+4.6%).\n\n| Images | Expected Cost | Estimated Actual |\n|--------|--------------:|-----------------:|\n| 800 | $0.33 | $0.34 |\n| 25,000 | $10.24 | $10.71 |\n| 320,000 | $131.04 | $137.08 |",
    ),
]

IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)]*\.(?:png|jpg|jpeg))\)")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]*\.md)\)")
PNG_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]*\.png)\)")


def _img_replacement(match: re.Match) -> str:
    alt, path = match.group(1), match.group(2)
    base = path.rsplit("/", 1)[-1]
    stem = base.rsplit(".", 1)[0]
    if "confusion_matrix" in stem:
        return f"![{alt}](../charts/{stem}.svg)"
    if "per_class_accuracy" in stem:
        return f"![{alt}](../charts/{stem}.svg)"
    if "stop_word_hasty" in stem:
        return "![Hasty-stop trigger words](../charts/hasty_stop_words.svg)"
    if any(k in stem for k in ("ale_correctness", "stop_word_scatter")):
        return f"*{alt} — chart not reproduced on the site; see `reports/monte_carlo/` in the repository.*"
    return f"*{alt} — chart not reproduced on the site; see the repository's `reports/`.*"


def _png_link_replacement(match: re.Match) -> str:
    text, path = match.group(1), match.group(2)
    base = path.rsplit("/", 1)[-1]
    stem = base.rsplit(".", 1)[0]
    if "confusion_matrix" in stem:
        return f"[{text}](../charts/{stem}.svg)"
    if "per_class_accuracy" in stem:
        return f"[{text}](../charts/{stem}.svg)"
    if "stop_word_hasty" in stem:
        return f"[{text}](../charts/hasty_stop_words.svg)"
    if any(k in stem for k in ("ale_correctness", "stop_word_scatter")):
        return f"{text} (chart not reproduced on the site; see the repository's `reports/monte_carlo/`)"
    return f"[{text}]({GITHUB_BLOB}{path.replace('../../', '')})"


def _link_replacement(match: re.Match) -> str:
    text, path = match.group(1), match.group(2)
    base = path.rsplit("/", 1)[-1]
    if base.startswith("confusion_matrix"):
        return f"[{text}](../results/confusion-matrices.html)"
    if base.startswith("misclassification_reasoning"):
        return f"[{text}](../appendix/misclassifications.html)"
    if path.startswith("../../reports/") or path.startswith("reports/") or path.startswith("docs/"):
        return f"[{text}]({GITHUB_BLOB}{path.replace('../../', '')})"
    return f"[{text}]({path})"


def fix_experiment_log(text: str) -> str:
    for old, new in EXP_LOG_FIXES:
        text = text.replace(old, new)
    return text


def strip_h1(text: str) -> str:
    lines = text.splitlines()
    if lines and re.match(r"^#\s+\S", lines[0]):
        lines = lines[1:]
        if lines and lines[0].strip() == "---":
            lines = lines[1:]
    return "\n".join(lines).lstrip("\n")


def demote_heads(text: str, levels: int = 1) -> str:
    def _demote(m: re.Match) -> str:
        return "#" * (len(m.group(1)) + levels) + m.group(2)

    return re.sub(r"^(#{1,6})(\s+\S.*)$", _demote, text, flags=re.M)


def rewrite_assets(text: str, *, exp_log: bool = False) -> str:
    if exp_log:
        text = fix_experiment_log(text)
    text = IMG_RE.sub(_img_replacement, text)
    text = LINK_RE.sub(_link_replacement, text)
    text = PNG_LINK_RE.sub(_png_link_replacement, text)
    return text


def write_page(target: Path, title: str, body: str, *, subtitle: str = "",
               description: str = "", toc: bool = True, toc_depth: int = 3) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    parts = ["---", f"title: {title!r}"]
    if subtitle:
        parts.append(f"subtitle: {subtitle!r}")
    if description:
        parts.append(f"description: {description!r}")
    parts += ["toc: true" if toc else "toc: false", f"toc-depth: {toc_depth}", "---", ""]
    target.write_text("\n".join(parts) + body, encoding="utf-8")
    print(f"  wrote {target.relative_to(WEBSITE)}")


# ---------------------------------------------------------------------------
# Page map: (source, target, title, subtitle/description)
# ---------------------------------------------------------------------------

DOC_PAGES = [
    (
        ROOT / "docs/CLI_COMMANDS.md",
        WEBSITE / "methods/cli-commands.qmd",
        "CLI Commands Reference",
        "Every useful terminal command: setup, data pipeline, EDA, cost estimation, Braintrust evaluation.",
    ),
    (
        ROOT / "docs/document_processor.md",
        WEBSITE / "methods/document-processor.qmd",
        "Document Processor Module",
        "PDF/TIFF → 300 DPI grayscale PNG + spatial OCR (Tesseract + Poppler) for LLM processing.",
    ),
    (
        ROOT / "docs/prompt_rules_provenance.md",
        WEBSITE / "methods/prompt-rules-provenance.qmd",
        "Prompt Rules Provenance",
        "Sources and validation status of classification rules across prompt versions v1–v4.",
    ),
    (
        ROOT / "docs/experiments/experiment_log.md",
        WEBSITE / "results/experiment-log.qmd",
        "Braintrust Experiment Log",
        "Every Braintrust eval: accuracy, tokens, errors, cost projections, and prompt-version notes.",
    ),
    (
        ROOT / "docs/experiments/800pic_tst_notes.md",
        WEBSITE / "results/gemini-800-notes.qmd",
        "Gemini 2.5 Flash — 800 Images",
        "50/class slice: 72.9% accuracy, per-class table, top confusion pairs, cost projections.",
    ),
    (
        ROOT / "docs/experiments/braintrust_dataset_run_gemini25flash.md",
        WEBSITE / "results/gemini-160-notes.qmd",
        "Gemini 2.5 Flash — 160 Images",
        "Braintrust run on the fixed_size_sampled slice: 80.0% accuracy, top confusion pairs.",
    ),
    (
        ROOT / "docs/CHANGELOG.md",
        WEBSITE / "prompts/prompt-changelog.qmd",
        "Prompt Version Changelog",
        "v0 → v18: every prompt change, its rationale, and measured accuracy on each dataset slice.",
    ),
    (
        ROOT / "docs/experiments/prompt_enhancement_list.md",
        WEBSITE / "prompts/enhancements.qmd",
        "Data-Backed Enhancement List",
        "Prioritized, data-backed next levers: near-miss ceiling, form over-attractor, escalation.",
    ),
    (
        ROOT / "docs/experiments/1pic_cost_estimation.md",
        WEBSITE / "cost/cost-estimation.qmd",
        "OpenRouter Cost Estimation",
        "Single-image token usage and linear extrapolation for 800 / 25,000 / 320,000 images.",
    ),
    (
        ROOT / "docs/experiments/monte_carlo_simulation.md",
        WEBSITE / "montecarlo/overview.qmd",
        "Monte Carlo Simulation",
        "Zero-spend what-if analysis over the 4,641-row / 1,512-image Braintrust reasoning corpus.",
    ),
    (
        ROOT / "reports/monte_carlo/prompt_ablation.md",
        WEBSITE / "montecarlo/prompt-ablation.qmd",
        "Prompt Ablation — Paired Bootstrap",
        "Statistical gate for prompt promotion: mean delta, 95% CI, P(A wins) on shared images.",
    ),
    (
        ROOT / "reports/monte_carlo/ensemble_accuracy_vs_k.md",
        WEBSITE / "montecarlo/ensemble-voting.qmd",
        "Ensemble Voting — Accuracy vs K",
        "Committee majority-vote simulation over 1,512 images: 82.1% → 86.3% at 1×–25× cost.",
    ),
    (
        ROOT / "reports/monte_carlo/routing_abstention.md",
        WEBSITE / "montecarlo/routing-abstention.qmd",
        "Confidence-Gated Escalation",
        "Routing the low-confidence tail to a stronger model: accuracy-vs-cost Pareto curve.",
    ),
    (
        ROOT / "reports/monte_carlo/failure_pipeline.md",
        WEBSITE / "montecarlo/failure-pipeline.qmd",
        "Failure Pipeline Simulation",
        "Retry/failover/fallback event simulation: 2.7% → 0.11% failure with fallback; 320K scale risk.",
    ),
    (
        ROOT / "reports/monte_carlo/exemplar_candidates.md",
        WEBSITE / "montecarlo/exemplar-mining.qmd",
        "Few-Shot Exemplar Mining",
        "Correct near-miss reasoning traces mined as exemplars for the top confusion pairs.",
    ),
    (
        ROOT / "reports/monte_carlo/ale_stopword_report.md",
        WEBSITE / "montecarlo/ale-stopword.qmd",
        "ALE + Stop-Word Analysis",
        "What reasoning features drive accuracy — and which trigger words make the model stop too early.",
    ),
    (
        ROOT / "reports/monte_carlo/verification_results.md",
        WEBSITE / "montecarlo/verification.qmd",
        "Verification Evals — Measured vs Simulated",
        "Spend-minimal verification: escalation slice and exemplar slice, measured vs predicted.",
    ),
    (
        ROOT / "reports/monte_carlo/corpus.summary.md",
        WEBSITE / "montecarlo/corpus-summary.qmd",
        "Monte Carlo Corpus Summary",
        "4,641 records / 1,512 images / 14 experiments across 4 models and prompt versions v0–v17.2.",
    ),
]

CLASSES_MD = ROOT / "src/constants.py"
MISCLASSIFICATION = (
    ROOT / "reports/misclassification_reasoning_qwen3.7-flash_v11.8_reasoning_1600_balanced_1120.md"
)
CONFUSION_SOURCES = sorted((ROOT / "reports/confusion_matrices").glob("confusion_matrix_*.md"))
CONFUSION_SOURCES += sorted((ROOT / "docs/experiments").glob("confusion_matrix_main-*.md"))
REPORT_SOURCES = sorted((ROOT / "reports/experiment_reports").glob("report_*.md"))

# ---------------------------------------------------------------------------
# Classes page
# ---------------------------------------------------------------------------

CLASS_INTRO = """
The classifier distinguishes between these 16 RVL-CDIP document classes. They are the
target vocabulary for the exact-match accuracy metric and the rows/columns of every
confusion matrix on this site.

| # | Class | Notes |
|---|-------|-------|
"""


def build_classes() -> None:
    classes = []
    for line in CLASSES_MD.read_text(encoding="utf-8").splitlines():
        m = re.match(r'\s*"([a-z_]+)"', line)
        if m:
            classes.append(m.group(1))
    rows = "\n".join(
        f"| {i} | `{c}` | |" for i, c in enumerate(classes, start=1)
    )
    body = CLASS_INTRO + rows + "\n"
    write_page(
        WEBSITE / "methods/classes.qmd",
        "Document Classes",
        body,
        subtitle="The 16-class RVL-CDIP target vocabulary",
    )


# ---------------------------------------------------------------------------
# Misclassification reasoning → collapsible details page
# ---------------------------------------------------------------------------

PAIR_RE = re.compile(r"^## (.+?)\s*→\s*(.+?)\s*\((\d+) errors?\)\s*$")
TRACE_FILE_RE = re.compile(r"^### `(.+)`\s*$")


def inline_md(seg: str) -> str:
    seg = html.escape(seg)
    seg = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", seg)
    seg = re.sub(r"`([^`]+)`", r"<code>\1</code>", seg)
    return seg


def trace_lines_to_md(lines: list[str]) -> str:
    """Convert one trace's reasoning lines to plain markdown.

    Emits markdown paragraphs/bullets (NOT <p>-wrapped HTML) separated by blank
    lines — pandoc's HTML reader recurses pathologically when <p> blocks share
    a line with no blank separator.
    """
    out: list[str] = []
    bullets: list[str] = []
    for line in lines:
        stripped = line[2:] if line.startswith("> ") else line[1:] if line.startswith(">") else line
        stripped = stripped.replace("<", "&lt;").replace(">", "&gt;")
        if stripped.strip() == "":
            if bullets:
                out.append("\n".join(f"- {b}" for b in bullets))
                bullets = []
            continue
        if stripped.startswith("- ") or stripped.startswith("* "):
            bullets.append(stripped[2:])
            continue
        if bullets:
            out.append("\n".join(f"- {b}" for b in bullets))
            bullets = []
        out.append(stripped)
    if bullets:
        out.append("\n".join(f"- {b}" for b in bullets))
    return "\n\n".join(out)


def build_misclassifications() -> None:
    text = MISCLASSIFICATION.read_text(encoding="utf-8")
    lines = text.splitlines()

    header = []
    pairs: list[tuple[str, str, int]] = []
    pair_sections: list[tuple[str, str, int, list[str]]] = []

    current_pair: tuple[str, str, int, list[str]] | None = None
    i = 0
    while i < len(lines):
        line = lines[i]
        pm = PAIR_RE.match(line)
        if pm:
            if current_pair:
                pair_sections.append(current_pair)
            exp, pred = pm.group(1).strip(), pm.group(2).strip()
            current_pair = (exp, pred, int(pm.group(3)), [])
            i += 1
            continue
        if current_pair is not None:
            current_pair[3].append(line)
        else:
            header.append(line)
        i += 1
    if current_pair:
        pair_sections.append(current_pair)

    parts = []
    parts.append(
        "Full reasoning traces for all 195 misclassifications (70 confusion pairs) from the "
        "1,120-image v11.8 run — every trace's 14-check scratchpad, runner-up line, and final label. "
        "Collapse each pair to browse, or expand to read the model's reasoning."
    )

    # summary table
    parts.append("## All confusion pairs")
    rows = "\n".join(
        f"| {exp} | {pred} | {n} |" for exp, pred, n, _ in sorted(pair_sections, key=lambda t: -t[2])
    )
    parts.append("| Expected | Predicted | Errors |\n|----------|-----------|-------:|\n" + rows)
    parts.append(
        "For each pair below, the trace shows the model walking the check-1→14 cascade, naming its "
        "runner-up, and committing to a (wrong) final label."
    )

    for exp, pred, n, body in sorted(pair_sections, key=lambda t: -t[2]):
        parts.append(f"## {exp} → {pred}")
        largest = n == max(p[2] for p in pair_sections)
        parts.append(f'<details class="trace-group"{" open" if largest else ""}>')
        parts.append(f"<summary>{n} reasoning traces</summary>")
        current_file = None
        trace_lines: list[str] = []
        meta_seen = False
        for bl in body:
            fm = TRACE_FILE_RE.match(bl)
            if fm:
                if current_file:
                    parts.append(trace_lines_to_md(trace_lines))
                current_file = fm.group(1)
                parts.append(f'<h3 class="trace-file"><code>{current_file}</code></h3>')
                trace_lines = []
                meta_seen = False
                continue
            if current_file and "Expected:" in bl and "Predicted:" in bl:
                parts.append(f'<p class="trace-meta">{inline_md(bl.strip())}</p>')
                meta_seen = True
                continue
            if current_file and bl.strip() == "**Reasoning:**":
                parts.append('<p class="trace-label">Reasoning</p>')
                continue
            if current_file:
                trace_lines.append(bl)
        if current_file:
            parts.append(trace_lines_to_md(trace_lines))
        parts.append("</details>")

    body = "\n".join(header[:6]) + "\n\n" + "\n\n".join(parts)
    body = body.replace("**Overall Accuracy:**", "<strong>Overall accuracy:</strong>")
    write_page(
        WEBSITE / "appendix/misclassifications.qmd",
        "Misclassification Reasoning — 1,120-Image v11.8 Run",
        body,
        subtitle="195 errors · 70 confusion pairs · full model scratchpads",
    )


# ---------------------------------------------------------------------------
# Aggregate pages
# ---------------------------------------------------------------------------

def build_confusion_page() -> None:
    parts = []
    for md in CONFUSION_SOURCES:
        text = md.read_text(encoding="utf-8")
        title_line = text.splitlines()[0] if text.splitlines() else md.stem
        title_line = title_line.lstrip("# ").strip()
        text = rewrite_assets(text)
        text = demote_heads(text, 1)
        parts.append(f"\n## {title_line}\n")
        parts.append(text)
    body = (
        "<p>Every confusion matrix computed from committed experiment data. The heatmap counts "
        "predicted (columns) against expected (rows) classes; the diagonal is the correct-class "
        "count. The recurring story across runs: `letter → memo`, `budget ↔ invoice`, and "
        "`* → form`.</p>\n" + "\n".join(parts)
    )
    write_page(
        WEBSITE / "results/confusion-matrices.qmd",
        "Confusion Matrices",
        body,
        subtitle="All experiments · heatmaps generated from committed tables",
    )


def build_report_page() -> None:
    parts = []
    for md in REPORT_SOURCES:
        text = md.read_text(encoding="utf-8")
        title_line = text.splitlines()[0] if text.splitlines() else md.stem
        title_line = title_line.lstrip("# ").strip()
        text = rewrite_assets(text)
        text = demote_heads(text, 1)
        parts.append(f"\n## {title_line}\n")
        parts.append(text)
    body = (
        "<p>Full per-experiment reports: exact-match accuracy, token usage, expected-vs-actual "
        "cost with scale-up projections, per-class accuracy, and confusion-matrix links.</p>\n"
        + "\n".join(parts)
    )
    write_page(
        WEBSITE / "results/experiment-reports.qmd",
        "Experiment Reports",
        body,
        subtitle="Per-run: accuracy · tokens · cost · per-class breakdowns",
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("Generating documentation pages:")
    for source, target, title, desc in DOC_PAGES:
        text = source.read_text(encoding="utf-8")
        text = rewrite_assets(text, exp_log=source.name == "experiment_log.md")
        body = strip_h1(text)
        write_page(target, title, body, description=desc)

    print("Aggregates:")
    build_confusion_page()
    build_report_page()

    print("Classes page:")
    build_classes()

    print("Misclassification appendix:")
    build_misclassifications()

    print("Done. Charts come from build_site_charts.py.")


if __name__ == "__main__":
    main()
