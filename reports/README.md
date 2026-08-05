# Reports (`reports/`)

Generated artifacts live here, separate from the curated experiment documentation in `docs/`.
This directory is produced by the scripts — contents are regenerated on each run.

## Layout

```
reports/
├── failed_reasoning_traces/   misclassification_reasoning_<experiment>.md
├── confusion_matrices/        confusion_matrix_<experiment>.md/.png
├── experiment_reports/        report_<experiment>.md, summary_*.md, *_analysis.md
├── manifests/                 eval checkpoint JSONL files (resumable runs)
├── eval_*.log                 eval runner stdout logs
├── per_class_accuracy_*.png   per-class accuracy charts
└── dimensions_summary.json    EDA dimension summary
```

Note: the reporting scripts (`braintrust_report.py`, `braintrust_metrics_visual.py`) still write
new artifacts to the `reports/` root; move them into the appropriate subfolder after generation.

## What lands here

| Artifact | Produced by |
|---|---|
| `dimensions_summary.json` | `scripts/eda/eda_dimensions_summary.py` |
| `eda_report.json` | `scripts/eda/eda_analysis.py` |
| `class_distribution.png`, `image_dimensions.png`, `dimensions_by_class.png`, `file_sizes.png`, `image_modes.png`, `sample_images.png` | `scripts/eda/eda_analysis.py` |
| `confusion_matrices/confusion_matrix_<experiment>.png/.md` | `scripts/braintrust/braintrust_report.py`, `braintrust_metrics_visual.py` |
| `per_class_accuracy_<experiment>.png` | `scripts/braintrust/braintrust_report.py`, `braintrust_metrics_visual.py` |
| `failed_reasoning_traces/misclassification_reasoning_<experiment>.md` | `scripts/braintrust/braintrust_report.py`, `braintrust_metrics_visual.py` |
| `experiment_reports/report_<experiment>.md` | `scripts/braintrust/braintrust_report.py` |

## Notes

- The curated, human-readable summaries of these artifacts live in `docs/experiments/` (see
  `docs/README.md`). Documents there link back to charts here via `../../reports/...`.
- Markdown image links from `docs/experiments/` resolve to this directory (e.g.
  `![Confusion Matrix](../../reports/confusion_matrix_main-123.png)`).
