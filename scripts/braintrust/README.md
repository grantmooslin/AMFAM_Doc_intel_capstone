# Braintrust Scripts (`scripts/braintrust/`)

Everything that talks to Braintrust: dataset construction/upload, prompt-evaluation runs,
experiment summarization, full reports, visualization, misclassification smoke datasets, and
one-off account copies.

These scripts get their Braintrust org/project/dataset/model configuration from `braintrust.env`
via `src/braintrust_config.py` (falling back to `.env`). Per-run CLI flags override the config.

## The evaluation workflow

The typical flow is: **build dataset → run eval → summarize → report/visualize → smoke dataset**.

1. **Build & upload a dataset** — `create_braintrust_800_dataset.py`
2. **Run a prompt evaluation** — `braintrust_openrouter_input.py`
3. **Quick summary** — `summarize_braintrust_experiment.py`
4. **Full report** — `braintrust_report.py`
5. **Charts + experiment log** — `braintrust_metrics_visual.py`
6. **Regression smoke set** — `create_misclassification_smoke_dataset.py`

## Scripts

### `create_braintrust_800_dataset.py`

Builds an 800-image RVL-CDIP slice (50 images × 16 classes) from a public Hugging Face parquet
mirror (no full 5 GB download), converts each TIFF to a 1024×1024 grayscale PNG (aspect-ratio
preserving, white padding), and inserts every image into a Braintrust dataset as a row attachment.

```bash
python scripts/braintrust/create_braintrust_800_dataset.py
python scripts/braintrust/create_braintrust_800_dataset.py --dataset rvl_cdip_800 --images-per-class 50 --seed 42
```

Key options: `--project`, `--project-id`, `--org`, `--dataset`, `--images-per-class`, `--seed`,
`--target-size W H`, `--source-url`, `--output-dir`.

### `braintrust_openrouter_input.py`

Runs the classification prompt (any of v1–v11) against a Braintrust dataset — or a local directory
of PNGs — with an OpenRouter vision model, and logs the results to a Braintrust experiment for
prompt iteration in the UI.

```bash
python scripts/braintrust/braintrust_openrouter_input.py
python scripts/braintrust/braintrust_openrouter_input.py --prompt-version v11 --model qwen/qwen3.7-flash
python scripts/braintrust/braintrust_openrouter_input.py --images-dir path/to/images --limit 20
python scripts/braintrust/braintrust_openrouter_input.py --experiment-name qwen3.7-flash_v11_reasoning
```

Key options: `--project`, `--project-id`, `--dataset-project`, `--dataset`, `--images-dir`,
`--limit`, `--model`, `--prompt-version`, `--max-tokens`, `--experiment-name`.

### `summarize_braintrust_experiment.py`

Recomputes per-image OK/MISS lines, per-class accuracy, and overall `exact_match` directly from a
Braintrust experiment's records. Useful when a run's local summary was lost (e.g. the process hung
after tasks completed).

```bash
python scripts/braintrust/summarize_braintrust_experiment.py --experiment qwen3.7-flash_v11_reasoning
```

Options: `--experiment` (required), `--project-id`.

### `braintrust_report.py`

Generates a full experiment report from Braintrust: accuracy + per-class, confusion matrix
(PNG + markdown), misclassification analysis with reasoning traces, and an expected-vs-actual cost
breakdown. Writes everything to `reports/` (override with `--output-dir`).

```bash
python scripts/braintrust/braintrust_report.py \
  --experiment qwen3.7-flash_v11_reasoning \
  --model qwen/qwen3.7-flash \
  --prompt-version v11 \
  --dataset fixed_size_sampled \
  --images-per-class 10 \
  --image-size 1024x1024 \
  --input-price 0.03 --output-price 0.13
```

Artifacts: `report_<experiment>.md`, `confusion_matrix_<experiment>.{png,md}`,
`per_class_accuracy_<experiment>.png`, `misclassification_reasoning_<experiment>.md`.

### `braintrust_metrics_visual.py`

Fetches experiment results and regenerates per-class accuracy charts, the confusion matrix
heatmap + markdown, and misclassification reasoning traces. It also appends a results section to
`docs/experiments/experiment_log.md` (skipping experiments already recorded). Pass an experiment
name as a positional argument to target it; otherwise it uses the most recent experiment.

```bash
python scripts/braintrust/braintrust_metrics_visual.py
python scripts/braintrust/braintrust_metrics_visual.py qwen3.7-flash_v11_reasoning
```

Artifacts are written to `reports/`.

### `create_misclassification_smoke_dataset.py`

Builds a Braintrust smoke-test dataset from every misclassification across the Qwen prompt-version
experiments (v1–v11). For each experiment in `QWEN_EXPERIMENTS` it pulls the offending rows, loads
their images from the source dataset, and inserts an annotated row (prompt version, source
experiment, predicted label, reasoning trace) into `BRAINTRUST_SMOKE_DATASET`
(default `qwen_misclassification_smoke_v1_v11`). Rebuilt idempotently on every run.

```bash
python scripts/braintrust/create_misclassification_smoke_dataset.py
python scripts/braintrust/create_misclassification_smoke_dataset.py --dry-run
python scripts/braintrust/create_misclassification_smoke_dataset.py --experiments "qwen3.7-flash_v9_reasoning qwen3.7-flash_v10_reasoning"
```

Options: `--env-file` (default `braintrust.env`), `--dataset`, `--experiments`, `--dry-run`.

### `copy_datasets_to_new_env.py`

Preferred way to port image datasets from the previous account to a newly configured Braintrust
account. Source credentials come from `braintrust.env`/`.env`; the destination (new account) is
passed explicitly. Attachments are uploaded synchronously with retries (8 attempts) so a row is
only inserted after its object upload succeeds, then every row is verified by re-downloading it.

```bash
python scripts/braintrust/copy_datasets_to_new_env.py \
  --datasets fixed_size_sampled fixed_size_sampled_320 \
  --dest-project-id <new-project-id> \
  --dest-project-name AMFAMv2 \
  --dest-org <new-org-id> \
  --dest-api-key <new-key>          # or export BRAINTRUST_DEST_API_KEY
```

Flags: `--source-project`, `--source-api-key` (or `BRAINTRUST_SOURCE_API_KEY`), `--no-verify`,
`--delete-existing`.

### `copy_braintrust_dataset.py`

One-off utility: copies a Braintrust dataset from one account to another. Edit the
`SOURCE_*` / `DEST_*` constants at the top of the file (API keys, project names, dataset names)
before running. Prefer `copy_datasets_to_new_env.py` for repeatable, verified porting.

```bash
python scripts/braintrust/copy_braintrust_dataset.py
```

## Configuration

All Braintrust scripts read from `braintrust.env` (see `braintrust.env.example`):

| Variable | Meaning |
|---|---|
| `BRAINTRUST_ORG_ID` | Braintrust organization id |
| `BRAINTRUST_PROJECT_NAME` / `BRAINTRUST_PROJECT_ID` | Project where experiments are logged |
| `BRAINTRUST_DATASET_PROJECT` | Project that owns the dataset (e.g. `AMFAM v2`) |
| `BRAINTRUST_DATASET` | Dataset name to evaluate (default `fixed_size_sampled`) |
| `BRAINTRUST_SMOKE_DATASET` | Smoke-test dataset name (default `qwen_misclassification_smoke_v1_v11`) |
| `QWEN_EXPERIMENTS` | Space-separated experiment names consumed by the smoke dataset builder |
| `BRAINTRUST_MODEL` | Default evaluation model (default `qwen/qwen3.7-flash`) |
| `BRAINTRUST_API_KEY` | Braintrust API key |
| `DATA_BRAINTRUST_KEY` | Optional separate key for the source-account dataset |
| `OPENROUTER_API_KEY` | OpenRouter key used by `braintrust_openrouter_input.py` |
| `RESEARCH_FUNDING_API_KEY` | Optional separate OpenRouter key for large/vetted runs only; used only when a script explicitly invokes it or as 403-quota failover |

CLI flags on individual scripts override these values per run. Never commit `braintrust.env` —
it is gitignored.
