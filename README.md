# Document Intelligence Pipeline with OpenRouter Vision Models

A Python toolkit for downloading the RVL-CDIP document image dataset, preprocessing pages, running exploratory data analysis, and classifying documents with vision models through OpenRouter.

## What's Included

**Core library (`src/`)**
- `document_processor.py` — Convert TIFF/PDF pages to 300 DPI grayscale PNGs and run OCR with bounding boxes.
- `openrouter_classifier.py` — Send a document image to an OpenRouter vision model for one of 16 class predictions.
- `prompts.py` — Versioned classification prompts (v1 → v15) with disambiguation rules.
- `constants.py`, `image_utils.py`, `openrouter_utils.py`, `env_utils.py`, `cli_utils.py` — Shared helpers.

**Scripts (`scripts/`)**
- `datasets/` — `download_dataset.py`, `create_balanced_dataset.py`, `create_fixed_size_dataset.py`, `run_tiff_processing.py` — data acquisition and preprocessing.
- `eda/` — `eda_analysis.py`, `eda_dimensions_summary.py` — exploratory data analysis.
- `braintrust/` — `create_braintrust_800_dataset.py`, `braintrust_openrouter_input.py`, `braintrust_report.py`, `braintrust_metrics_visual.py`, `summarize_braintrust_experiment.py`, `copy_braintrust_dataset.py` — Braintrust evaluation and reporting.
- `openrouter/` — `estimate_openrouter_cost.py` — extrapolate token usage/cost for 800, 25,000, and 320,000 images.

**Documentation (`docs/`)**
- `experiments/` — Experiment log and all experiment results (confusion matrices, misclassification reasoning, cost projections).
- `prompt_rules_provenance.md` — Sources and validation status of prompt rules across versions.
- `document_processor.md` — `document_processor.py` module reference.
- `README.md` — Index of the documentation tree.

**Generated output (`reports/`)**
- `dimensions_summary.json` — EDA dimension summary. Confusion-matrix PNGs/heatmaps and `report_*.md` also land here.

**Other**
- `requirements.txt` — Python dependencies.
- `.env.example` — Template for API key environment variable.

## Setup

1. Install system dependencies:
   - [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
   - [Poppler](https://github.com/oschwartz10612/poppler-windows) (for `pdf2image`)

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add your OpenRouter API key:

   ```bash
   cp .env.example .env
   ```

   Edit `.env`:

   ```text
   OPENROUTER_API_KEY=sk-or-v1-...
   ```

## Usage Workflow

1. **Download the dataset**

   ```bash
   python scripts/datasets/download_dataset.py
   ```

2. **Create a balanced subset**

   ```bash
   python scripts/datasets/create_balanced_dataset.py
   ```

3. **Run EDA**

   ```bash
   python scripts/eda/eda_analysis.py
   ```

4. **Process TIFF pages to PNGs**

   ```bash
   python scripts/datasets/run_tiff_processing.py
   ```

5. **Estimate OpenRouter cost for a model**

   Edit `MODEL` in `scripts/openrouter/estimate_openrouter_cost.py`, then run:

   ```bash
   python scripts/openrouter/estimate_openrouter_cost.py
   ```

   This updates `docs/experiments/1pic_cost_estimation.md` automatically.

6. **Classify a single image**

   ```bash
   python src/openrouter_classifier.py
   ```

## Security Notes

- **Never commit `.env` or any file containing your API key.** `.env` is excluded by `.gitignore`.
- `.env.example` is safe to commit because it contains a placeholder value only.
- Generated datasets, images, and report files are excluded from version control by `.gitignore`.

## Notes

- The scripts contain example `__main__` blocks with hardcoded paths for local testing. Update the `*_PATH` variables in each script to match your environment before running.
- Cost projections are linear extrapolations from a single representative image per model. Actual costs may vary with image size, content, and OpenRouter pricing changes.
