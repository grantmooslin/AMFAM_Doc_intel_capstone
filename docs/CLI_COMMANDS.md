# CLI Commands Reference

The most common commands for working with this project from the terminal. Run everything from the
repository root. Each script also supports `--help` for its full option list
(e.g. `python scripts/braintrust/braintrust_report.py --help`).

## Setup

```bash
pip install -r requirements.txt          # Python dependencies
brew install tesseract poppler           # macOS: OCR + PDF system binaries

cp .env.example .env                     # OpenRouter API key (OPENROUTER_API_KEY)
cp braintrust.env.example braintrust.env # Braintrust org/project/dataset/model config
```

Both env files are gitignored. `braintrust.env` is the single source of truth for Braintrust
settings; `.env` fills the gaps (notably `OPENROUTER_API_KEY`).

## Quick reference

| Task | Command |
|---|---|
| Download RVL-CDIP (Kaggle) | `python scripts/datasets/download_dataset.py` |
| Sample 50 images/class | `python scripts/datasets/create_balanced_dataset.py` |
| Build fixed-size image sets | `python scripts/datasets/create_fixed_size_dataset.py` |
| TIFF → 300 DPI PNG + OCR | `python scripts/datasets/run_tiff_processing.py` |
| Full EDA | `python scripts/eda/eda_analysis.py` |
| Dimensions summary | `python scripts/eda/eda_dimensions_summary.py` |
| Cost projection | `python scripts/openrouter/estimate_openrouter_cost.py` |
| Build + upload Braintrust dataset | `python scripts/braintrust/create_braintrust_800_dataset.py` |
| Run an eval (prompt × model) | `python scripts/braintrust/braintrust_openrouter_input.py` |
| Summarize an experiment | `python scripts/braintrust/summarize_braintrust_experiment.py --experiment <name>` |
| Full experiment report | `python scripts/braintrust/braintrust_report.py --experiment <name> --prompt-version <v> --dataset <ds> --images-per-class <n>` |
| Charts + append experiment log | `python scripts/braintrust/braintrust_metrics_visual.py [<experiment>]` |
| Build misclassification smoke set | `python scripts/braintrust/create_misclassification_smoke_dataset.py [--dry-run]` |
| Validate a queued eval | `python scripts/braintrust/preflight_eval.py --dataset <ds> --prompt-version v14` |
| Run production eval queue | `python scripts/braintrust/run_eval_queue.py --dry-run` |
| Port datasets to a new account | `python scripts/braintrust/copy_datasets_to_new_env.py --datasets <ds...> --dest-project-id <id> --dest-project-name AMFAMv2 --dest-org <org> --dest-api-key <key>` |

The production queue includes `qwen3.7-flash_v14_fixed_size_sample`, which runs
prompt `v14` with `qwen/qwen3.7-flash` on the canonical `fixed_size_sampled`
dataset. `fixed_siz_sample` is not a repository dataset name.

## Data pipeline

```bash
# 1. Download the RVL-CDIP dataset from Kaggle
python scripts/datasets/download_dataset.py

# 2. Sample a balanced subset (50 per class) — edit SOURCE_PATH/OUTPUT_PATH in the script
python scripts/datasets/create_balanced_dataset.py

# 3. Resize/sample to fixed square sets (2550x3300, 1024x1024, ...) — edit configs in the script
python scripts/datasets/create_fixed_size_dataset.py

# 4. Convert TIFF pages to 300 DPI grayscale PNGs with spatial OCR — edit INPUT/OUTPUT_DIR
python scripts/datasets/run_tiff_processing.py
```

## EDA

```bash
# Full analysis: class distribution, dimensions, file sizes, image modes, sample grid
python scripts/eda/eda_analysis.py

# Average image dimensions across all configured datasets -> reports/dimensions_summary.json
python scripts/eda/eda_dimensions_summary.py
```

Outputs go to `reports/` (charts + `eda_report.json` / `dimensions_summary.json`).

## Cost estimation

```bash
# Edit MODEL / IMAGE_PATH / pricing constants in the script first
python scripts/openrouter/estimate_openrouter_cost.py
```

Updates `docs/experiments/1pic_cost_estimation.md` with token/cost projections for 800, 25,000,
and 320,000 images.

## Braintrust evaluation workflow

```bash
# 1. Build the 800-image dataset and upload it to Braintrust
python scripts/braintrust/create_braintrust_800_dataset.py

# 2. Run the production prompt against a dataset/model and log to an experiment
python scripts/braintrust/braintrust_openrouter_input.py \
  --prompt-version v14 \
  --model qwen/qwen3.7-flash \
  --experiment-name qwen3.7-flash_v14_reasoning \
  --manifest reports/manifests/eval_v14.jsonl

# 3. Quick per-class accuracy + exact_match (good if the run's local summary was lost)
python scripts/braintrust/summarize_braintrust_experiment.py --experiment qwen3.7-flash_v11_reasoning

# 4. Full report: confusion matrix, misclassification reasoning, cost breakdown
python scripts/braintrust/braintrust_report.py \
  --experiment qwen3.7-flash_v11_reasoning \
  --model qwen/qwen3.7-flash \
  --prompt-version v14 \
  --dataset fixed_size_sampled \
  --images-per-class 10 \
  --image-size 1024x1024 \
  --input-price 0.03 --output-price 0.13

# 5. Regenerate charts and append the results section to docs/experiments/experiment_log.md
python scripts/braintrust/braintrust_metrics_visual.py qwen3.7-flash_v11_reasoning

# 6. Assemble a regression smoke dataset from every misclassification across v1-v11
python scripts/braintrust/create_misclassification_smoke_dataset.py --dry-run   # preview first
python scripts/braintrust/create_misclassification_smoke_dataset.py              # build + upload
```

Braintrust config (org/project/dataset/model) is read from `braintrust.env`; every command above
can override it with `--project-id`, `--project`, `--dataset`, or `--model`.

## Porting datasets to a new Braintrust account

`braintrust.env` is the single source of truth for Braintrust credentials and should carry the
**new** account's key (`.env` may still hold the previous account's stale key). After configuring
new credentials (see `AGENTS.md` → "Adding / configuring new Braintrust credentials"), port
datasets from the previous account:

```bash
# Source credentials come from braintrust.env/.env; destination is passed explicitly.
python scripts/braintrust/copy_datasets_to_new_env.py \
  --datasets fixed_size_sampled fixed_size_sampled_320 \
  --dest-project-id <new-project-id> \
  --dest-project-name AMFAMv2 \
  --dest-org <new-org-id> \
  --dest-api-key <new-key>          # or export BRAINTRUST_DEST_API_KEY
```

Attachments upload synchronously with retries and every row is verified by re-download;
`--delete-existing` makes re-copies idempotent. The one-off `copy_braintrust_dataset.py` variant
copies a single dataset by editing its `SOURCE_*`/`DEST_*` constants.

## Research funding key

`RESEARCH_FUNDING_API_KEY` (optional, in `.env`) is a separate OpenRouter key reserved for large
or significant runs whose prompt has passed all vetting steps. It is **never** the default —
routine testing/iteration runs on `OPENROUTER_API_KEY`. It is used only when a script explicitly
requests it (e.g. `run_v11_8_800_after_480.py`) or as automatic 403-quota failover in
`braintrust_openrouter_input.py`.

## Helpful flags

- `--images-dir path/to/pngs` — evaluate a local image folder instead of a Braintrust dataset
  (`braintrust_openrouter_input.py`).
- `--limit N` — classify only the first `N` images (fast smoke runs).
- `--dry-run` — preview without writing (`create_misclassification_smoke_dataset.py`).
- `--output-dir <dir>` — where report artifacts are written (default `reports`).
- `--experiment <name>` — target a specific experiment; most tools default to the most recent one.

## Where results land

- Script-generated charts/reports: `reports/`
- Running experiment log + curated results: `docs/experiments/` (see `docs/README.md`)
- Cost projections: `docs/experiments/1pic_cost_estimation.md`

## Secrets safety

- `braintrust.env` and `.env` contain live API keys and are gitignored — never commit them.
- Commit only the templates: `.env.example`, `braintrust.env.example`.
