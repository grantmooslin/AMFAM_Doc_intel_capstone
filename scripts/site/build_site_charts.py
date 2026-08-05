"""Generate the website's charts (SVG) from committed markdown tables.

Fully offline and deterministic: every chart is rendered from tables that are
already committed to the repository (confusion-matrix grids, per-class accuracy
tables, cost projections, and curated accuracy-progress data). No API keys, no
network access, no model spend.

Outputs SVG files into ``website/charts/`` so they are tracked by git (the repo
gitignores ``*.png`` but not ``*.svg``).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
CHARTS_DIR = ROOT / "website" / "charts"

sys.path.insert(0, str(ROOT))
from src.constants import DOCUMENT_CLASSES  # noqa: E402

N_CLASSES = len(DOCUMENT_CLASSES)

# ---------------------------------------------------------------------------
# Styling
# ---------------------------------------------------------------------------

BG = "#ffffff"
NAVY = "#1b2a4a"
ACCENT = "#2d6cdf"
ACCENT_LIGHT = "#dbe6fb"
GOOD = "#1e9e5a"
BAD = "#d64545"
GRID = "#e8ecf3"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.facecolor": "white",
        "figure.facecolor": "white",
        "svg.fonttype": "none",
        "axes.edgecolor": GRID,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
    }
)


def _save(fig, name: str) -> Path:
    fig.tight_layout()
    out = CHARTS_DIR / name
    fig.savefig(out, format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"  chart: {out.name}")
    return out


def _norm(label: str) -> str:
    label = label.strip().strip("`").strip("*").strip()
    return label


# ---------------------------------------------------------------------------
# Confusion matrices
# ---------------------------------------------------------------------------

ROW_RE = re.compile(r"^\|\s*`?([a-zA-Z_]+)`?\s*\|(.*)\|")


def parse_confusion_matrix(md_text: str) -> dict:
    """Parse a ``## Raw Counts`` grid into an 16x16 matrix + per-class accuracy."""
    in_counts = False
    rows = []
    row_labels = []
    acc = {}
    for line in md_text.splitlines():
        if line.strip().startswith("## Raw Counts"):
            in_counts = True
            continue
        if in_counts:
            if line.strip().startswith("| Expected"):
                continue
            if line.strip().startswith("|---"):
                continue
            if line.strip().startswith("## "):
                break
            m = ROW_RE.match(line)
            if not m:
                continue
            label = _norm(m.group(1))
            if not label or "invalid" in label.lower():
                continue
            cells = [c.strip() for c in m.group(2).split("|")]
            cells = [c for c in cells if c != ""]
            values = []
            for cell in cells:
                if cell in (".", "—", "-"):
                    values.append(0)
                else:
                    values.append(int(re.sub(r"[^\d]", "", cell)))
            if len(values) >= N_CLASSES:
                rows.append(values[:N_CLASSES])
                row_labels.append(label)
                acc[label] = values[-1] if values else 0
    matrix = np.array(rows, dtype=float) if rows else np.zeros((0, 0))
    return {"matrix": matrix, "labels": row_labels, "acc": acc}


def chart_confusion_matrix(md_path: Path, out_name: str) -> None:
    data = parse_confusion_matrix(md_path.read_text(encoding="utf-8"))
    matrix = data["matrix"]
    labels = data["labels"]
    if matrix.size == 0 or matrix.shape[0] != matrix.shape[1]:
        print(f"  skip (no parseable grid): {md_path.name}")
        return
    n = matrix.shape[0]
    diag = np.diag(matrix).copy()
    max_v = matrix.max() if matrix.max() > 0 else 1
    cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list(
        "amfam", ["#ffffff", "#c7d8fb", ACCENT]
    )
    fig, ax = plt.subplots(figsize=(10, 8.4))
    im = ax.imshow(matrix, cmap=cmap, vmin=0, vmax=max_v, aspect="equal")
    for i in range(n):
        for j in range(n):
            v = matrix[i, j]
            if v == 0:
                continue
            on_diag = i == j
            color = "white" if v > max_v * 0.62 else ("#10316b" if on_diag else "#33415c")
            ax.text(
                j, i, f"{int(v)}", ha="center", va="center",
                fontsize=8, color=color, fontweight="bold" if on_diag else "normal",
            )
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    short = [
        "advert", "budget", "email", "file_f", "form", "handwr", "invoic",
        "letter", "memo", "news_a", "presen", "questi", "resume", "sci_pub",
        "sci_rep", "specif",
    ]
    ax.set_xticklabels(short[:n], rotation=45, ha="right", fontsize=8)
    ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Expected")
    ax.set_title("Confusion matrix (correct class counts on the diagonal)", fontsize=12, pad=12)
    fig.colorbar(im, ax=ax, fraction=0.035, pad=0.02)
    _save(fig, out_name)


# ---------------------------------------------------------------------------
# Per-class accuracy
# ---------------------------------------------------------------------------

PCA_HEADER_RE = re.compile(r"^\|?\s*Class\s*\|")


def parse_per_class_accuracy(md_text: str) -> dict[str, tuple[int, int]]:
    out = {}
    for line in md_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        if "Per-Class Accuracy" in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        cells = [_norm(c) for c in cells]
        if len(cells) >= 2 and cells[0] and PCA_HEADER_RE.match(cells[0]):
            continue
        if len(cells) >= 4 and cells[0] in DOCUMENT_CLASSES:
            try:
                correct = int(cells[1])
                total = int(cells[2])
            except ValueError:
                continue
            out[cells[0]] = (correct, total)
        elif len(cells) >= 2 and cells[0] in DOCUMENT_CLASSES:
            m = re.search(r"(\d+)%", cells[1])
            if m:
                out[cells[0]] = (int(m.group(1)), 100)
    return out


def chart_per_class(md_path: Path, out_name: str, title: str) -> None:
    pca = parse_per_class_accuracy(md_path.read_text(encoding="utf-8"))
    if not pca:
        print(f"  skip (no per-class table): {md_path.name}")
        return
    classes = DOCUMENT_CLASSES
    accs = []
    for c in classes:
        if c in pca:
            correct, total = pca[c]
            accs.append((c, correct, total, correct / total if total else 0))
    if not accs:
        return
    accs.sort(key=lambda t: t[3])
    names = [t[0] for t in accs]
    vals = [t[3] * 100 for t in accs]
    details = [f"{t[1]}/{t[2]}" for t in accs]
    colors = [GOOD if v >= 80 else ("#e8a13c" if v >= 60 else BAD) for v in vals]
    fig, ax = plt.subplots(figsize=(9.5, 6.6))
    y = np.arange(len(names))
    ax.barh(y, vals, color=colors, height=0.72, edgecolor="none")
    for yi, v, d in zip(y, vals, details):
        ax.text(v + 1, yi, f"{v:.0f}% ({d})", va="center", fontsize=8.5, color="#33415c")
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=9)
    ax.set_xlim(0, 108)
    ax.set_xlabel("Exact-match accuracy (%)")
    ax.axvline(80, color=GRID, lw=1, ls="--", zorder=0)
    ax.set_title(title, fontsize=12, pad=10)
    ax.grid(axis="y", visible=False)
    _save(fig, out_name)


# ---------------------------------------------------------------------------
# Cost projections
# ---------------------------------------------------------------------------

def parse_cost_projections(md_text: str) -> list[dict]:
    """Parse model sections with a 3-row cost table (800 / 25K / 320K)."""
    models = []
    cur = None
    for line in md_text.splitlines():
        m = re.match(r"^## Model\s+\d+:\s*`([^`]+)`", line.strip())
        if m:
            cur = {"model": m.group(1), "costs": {}}
            models.append(cur)
            continue
        if cur is None or not line.strip().startswith("|"):
            continue
        cells = [_norm(c) for c in line.strip().strip("|").split("|")]
        scale = {"800": 800, "25,000": 25000, "320,000": 320000}
        key = cells[0] if cells else ""
        cost_m = re.search(r"\$([\d,]+\.?\d*)", cells[-1]) if cells else None
        if key in scale and cost_m:
            cur["costs"][scale[key]] = float(cost_m.group(1).replace(",", ""))
    return [m for m in models if len(m["costs"]) == 3]


def chart_cost_projection(paths: list[Path], out_name: str) -> None:
    models = []
    for p in paths:
        models.extend(parse_cost_projections(p.read_text(encoding="utf-8")))
    if not models:
        print("  skip (no cost tables)")
        return
    scales = [800, 25000, 320000]
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(models))
    width = 0.26
    for si, scale in enumerate(scales):
        vals = [m["costs"][scale] for m in models]
        bars = ax.bar(
            x + (si - 1) * width, vals, width,
            color=[ACCENT, "#5b8def", "#a6c2f7"][si],
            label=f"{scale:,} images",
        )
        for b, v in zip(bars, vals):
            ax.text(
                b.get_x() + b.get_width() / 2, b.get_height(),
                f"${v:,.0f}", ha="center", va="bottom", fontsize=7.5,
            )
    ax.set_xticks(x)
    ax.set_xticklabels([m["model"] for m in models], rotation=20, ha="right", fontsize=8.5)
    ax.set_yscale("log")
    ax.set_ylabel("Projected cost (USD, log scale)")
    ax.set_title("Extrapolated OpenRouter cost per model (800 / 25K / 320K images)")
    ax.legend(frameon=False)
    _save(fig, out_name)


# ---------------------------------------------------------------------------
# Hasty-stop trigger words
# ---------------------------------------------------------------------------

def chart_hasty_stop_words(md_path: Path, out_name: str) -> None:
    rows = []
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [_norm(c) for c in line.strip().strip("|").split("|")]
        if len(cells) >= 7 and cells[0] and cells[0] != "word":
            try:
                rows.append((cells[0], float(cells[-1]), int(cells[1])))
            except ValueError:
                continue
    if not rows:
        print("  skip (no hasty-stop table)")
        return
    rows.sort(key=lambda t: t[1])
    words = [r[0] for r in rows]
    scores = [r[1] for r in rows]
    ns = [r[2] for r in rows]
    fig, ax = plt.subplots(figsize=(9, 6.5))
    y = np.arange(len(words))
    ax.barh(y, scores, color=BAD if max(scores) > 1 else ACCENT, height=0.7)
    for yi, s, n in zip(y, scores, ns):
        ax.text(s + 0.01, yi, f"{s:.2f}  (n={n})", va="center", fontsize=8)
    ax.set_yticks(y)
    ax.set_yticklabels(words, fontsize=9)
    ax.set_xlabel("hasty score (early stop × error lift × frequency)")
    ax.set_title("Hasty-stop trigger words — words that push early, wrong commits")
    ax.grid(axis="y", visible=False)
    _save(fig, out_name)


# ---------------------------------------------------------------------------
# Accuracy progress (curated)
# ---------------------------------------------------------------------------

PROGRESS = [
    # (label, slice, accuracy_pct) -- curated from docs/CHANGELOG.md + experiment_log.md
    ("gemini-2.5-flash v0 (baseline)", "800", 72.9),
    ("qwen v0 (baseline control)", "480", 69.2),
    ("gemini disambiguation", "160", 83.75),
    ("qwen v10", "160", 97.5),
    ("qwen v11", "160", 98.7),
    ("qwen v11.7", "160", 98.1),
    ("qwen v11.8", "160", 99.4),
    ("qwen v11.8", "320", 87.2),
    ("qwen v11.8", "480", 89.1),
    ("qwen v11.8", "800", 83.1),
    ("qwen v11.8", "1,120", 82.6),
    ("qwen v13", "160 (v2)", 86.2),
    ("qwen v14", "160 (v2)", 85.0),
    ("qwen v16", "160 (v1)", 96.2),
    ("qwen v16", "160 (v3)", 79.4),
    ("qwen v17", "160 (v1)", 95.0),
    ("qwen v17.2", "exemplar 48", 68.8),
    ("qwen v18 (exp.)", "exemplar 48", 64.6),
]

SLICE_COLORS = {
    "160": "#1b2a4a",
    "320": ACCENT,
    "480": "#5b8def",
    "800": "#a6c2f7",
    "1,120": "#8e44ad",
    "160 (v1)": "#d4a017",
    "160 (v2)": "#d4a017",
    "160 (v3)": "#d4a017",
    "exemplar 48": "#e8a13c",
}


def chart_progress(out_name: str) -> None:
    fig, ax = plt.subplots(figsize=(11, 6))
    x = np.arange(len(PROGRESS))
    colors = [SLICE_COLORS.get(s, GRID) for _, s, _ in PROGRESS]
    vals = [v for _, _, v in PROGRESS]
    ax.bar(x, vals, color=colors, width=0.68)
    for xi, (label, sl, v) in zip(x, PROGRESS):
        ax.text(xi, v + 1.2, f"{v:.1f}", ha="center", fontsize=7.5, color="#33415c")
        ax.text(xi, -3.0, label.split(" ")[0].split("-")[0], ha="center", fontsize=6.5, color="#6b7280")
    ax.set_xticks(x)
    ax.set_xticklabels([f"{l}\n({s})" for l, s, _ in PROGRESS], rotation=45, ha="right", fontsize=7.5)
    ax.set_ylim(0, 108)
    ax.set_ylabel("Exact-match accuracy (%)")
    ax.set_title("Accuracy progress: baseline → prompt iterations → production slices")
    ax.grid(axis="x", visible=False)
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in dict.fromkeys(SLICE_COLORS.values())]
    labels = ["160 dev-set", "320", "480", "800", "1,120", "HF-mirror v2/v3", "exemplar slice"]
    ax.legend(handles, labels, ncol=4, frameon=False, loc="upper left", fontsize=8, bbox_to_anchor=(0, 1.14))
    _save(fig, out_name)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    print("Confusion matrices (reports/confusion_matrices + docs/experiments):")
    sources = sorted((ROOT / "reports" / "confusion_matrices").glob("confusion_matrix_*.md"))
    sources += sorted((ROOT / "docs" / "experiments").glob("confusion_matrix_main-*.md"))
    for md in sources:
        exp = md.name.removeprefix("confusion_matrix_").removesuffix(".md")
        chart_confusion_matrix(md, f"confusion_matrix_{exp}.svg")

    print("Per-class accuracy (report files + 800pic notes):")
    report_sources = sorted((ROOT / "reports" / "experiment_reports").glob("report_*.md"))
    for md in report_sources:
        exp = md.name.removeprefix("report_").removesuffix(".md")
        chart_per_class(md, f"per_class_accuracy_{exp}.svg", f"Per-class accuracy — {exp}")
    final_1120 = ROOT / "reports" / "experiment_reports" / "qwen3.7-flash_v11.8_1600_balanced_1120_final.md"
    if final_1120.exists():
        chart_per_class(
            final_1120,
            "per_class_accuracy_qwen3.7-flash_v11.8_reasoning_1600_balanced_1120.svg",
            "Per-class accuracy — qwen3.7-flash v11.8 · 1,120-image slice",
        )
    chart_per_class(
        ROOT / "docs" / "experiments" / "800pic_tst_notes.md",
        "per_class_accuracy_gemini-2.5-flash_800_notes.svg",
        "Per-class accuracy — gemini-2.5-flash 800 (from notes)",
    )

    print("Cost projections:")
    chart_cost_projection(
        [ROOT / "docs" / "experiments" / "1pic_cost_estimation.md"],
        "cost_projection_models.svg",
    )

    print("Hasty-stop words:")
    chart_hasty_stop_words(ROOT / "reports" / "monte_carlo" / "ale_stopword_report.md", "hasty_stop_words.svg")

    print("Accuracy progress:")
    chart_progress("accuracy_progress.svg")

    print("Done.")


if __name__ == "__main__":
    main()
