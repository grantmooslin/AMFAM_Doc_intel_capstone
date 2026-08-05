# Scripts

Every runnable script in this project lives under `scripts/`, grouped by purpose. All scripts
resolve the repository root themselves (via `Path(__file__).resolve().parents[2]`), so they can be
run from anywhere and import `src/` directly. Run them from the repository root:

```bash
python scripts/<group>/<script>.py [options]
```

## Layout

| Directory | Purpose |
|---|---|
| [`datasets/`](datasets/README.md) | Dataset acquisition and preprocessing (download, balanced sampling, fixed-size resizing, TIFF→PNG processing). |
| [`eda/`](eda/README.md) | Exploratory data analysis (class distribution, dimensions, file sizes, visualizations). |
| [`braintrust/`](braintrust/README.md) | Braintrust evaluation and reporting (dataset upload, prompt evaluation runs, reports, visualization, smoke datasets, account copies). |
| [`openrouter/`](openrouter/README.md) | OpenRouter cost estimation. |

## Environment

Two env files are used (both gitignored; templates committed):

- `.env` — `OPENROUTER_API_KEY` (and optional `BRAINTRUST_API_KEY`, `DATA_BRAINTRUST_KEY`).
- `braintrust.env` — the single source of truth for Braintrust org/project/dataset/model config,
  loaded by `src/braintrust_config.py`. See `braintrust.env.example`.

## Prerequisites

- Python 3.10+ with `requirements.txt` installed (`pip install -r requirements.txt`).
- System binaries for the document pipeline: Tesseract OCR and Poppler (`pdf2image`).
- The `.env` / `braintrust.env` files populated with your keys.

## Fresh v15 validation slices

Create two disjoint 160-image Hugging Face mirror slices and upload them to the
`AMFAM v2` Braintrust project as `fixed_size_sampled_v3` and
`fixed_size_sampled_v4`:

```bash
python scripts/braintrust/create_braintrust_160_v3_v4_datasets.py
```

Use `--dry-run` to build and validate the samples without writing Braintrust.

## Notes

- Several scripts keep example configuration in a `main()` block with hardcoded dev-machine paths
  (`c:\Users\grant\...`). Update those constants to your environment before running.
- Generated artifacts (charts, heatmaps, reports, JSON) are written to the top-level
  `reports/` directory rather than into `scripts/`.
