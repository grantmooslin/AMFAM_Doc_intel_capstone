# AGENTS.md

## Project Overview

Python document classification pipeline: RVL-CDIP images → OpenRouter vision models → Braintrust evaluation. 16 document classes.

## Commands

```bash
# Install
pip install -r requirements-dev.txt

# Test
pytest                              # all tests
pytest tests/test_prompts.py -v     # single file
pytest -k "test_clean_prediction"   # by name match

# Coverage
pytest --cov=src --cov=scripts --cov-report=term-missing

# Run scripts (work from any directory)
python scripts/datasets/download_dataset.py
python scripts/braintrust/braintrust_report.py
python src/openrouter_classifier.py
```

No linter, formatter, or typecheck is configured.

## Environment

Two env files (both gitignored):

- `.env` — API keys: `OPENROUTER_API_KEY`, `BRAINTRUST_API_KEY`
- `braintrust.env` — single source of truth for Braintrust org/project/dataset/model config, loaded by `src/braintrust_config.py`

Copy `*.env.example` templates to create them. Missing env vars cause `sys.exit(1)` via `src/env_utils.require_env()`.

System binaries required: **Tesseract OCR** and **Poppler** (for `pdf2image`).

## Architecture

- `src/` — shared library (no CLI); scripts import via `from src.<module> import ...`
- `scripts/` — runnable scripts grouped by purpose (`datasets/`, `eda/`, `braintrust/`, `openrouter/`)
- `reports/` — generated artifacts (charts, confusion matrices, JSON)
- `docs/experiments/` — curated experiment documentation (links back to `reports/`)
- `conftest.py` adds project root to `sys.path` and sets matplotlib backend to `Agg`

Scripts resolve the repo root via `Path(__file__).resolve().parents[2]`, so they can be run from anywhere.

## Key Files

- `src/constants.py` — 16 `DOCUMENT_CLASSES` and `IMAGE_EXTENSIONS`
- `src/prompts.py` — versioned prompts (v1–v17); `DEFAULT_PROMPT_VERSION` is current
- `src/braintrust_config.py` — `load_braintrust_config()` dataclass; reads `braintrust.env`, falls back to `.env`
- `src/evaluation.py` — `validate_dataset()`, `ManifestStore` for resumable eval runs

## Conventions

- Scripts keep example `__main__` blocks with hardcoded dev-machine paths — update path constants before running locally
- Generated output goes to `reports/`, not `docs/`
- Prompt versions are append-only in `src/prompts.py`; register new versions in the `PROMPTS` dict and update `DEFAULT_PROMPT_VERSION`

## Report Generation

The typical flow: **run eval → summarize → full report → charts/experiment log**.

```bash
# 1. Run a prompt evaluation against a Braintrust dataset
python scripts/braintrust/braintrust_openrouter_input.py \
  --prompt-version v17 --model qwen/qwen3.7-flash \
  --dataset fixed_size_sampled --experiment-name qwen3.7-flash_v17_reasoning

# 2. Quick per-image OK/MISS summary + exact_match
python scripts/braintrust/summarize_braintrust_experiment.py \
  --experiment qwen3.7-flash_v17_reasoning

# 3. Full report: accuracy, confusion matrix (PNG+MD), misclassification reasoning, cost breakdown
python scripts/braintrust/braintrust_report.py \
  --experiment qwen3.7-flash_v17_reasoning \
  --model qwen/qwen3.7-flash --prompt-version v17 \
  --dataset fixed_size_sampled --images-per-class 10 \
  --input-price 0.03 --output-price 0.13

# 4. Per-class accuracy chart + confusion matrix heatmap + experiment log append
python scripts/braintrust/braintrust_metrics_visual.py \
  qwen3.7-flash_v17_reasoning
```

Artifacts produced in `reports/`: `report_<experiment>.md`, `confusion_matrix_<experiment>.{png,md}`, `per_class_accuracy_<experiment>.png`, `misclassification_reasoning_<experiment>.md`.

`braintrust_metrics_visual.py` also appends to `docs/experiments/experiment_log.md` (skips experiments already recorded).

## Dataset Slices

Datasets are balanced (N images per class x 16 classes) and uploaded to Braintrust as row attachments (base64 PNGs with ground-truth labels). All scripts de-duplicate against existing datasets.

```bash
# 160-image slice (10/class) — from HF parquet mirror, no full RVL-CDIP download needed
python scripts/braintrust/create_braintrust_800_dataset.py --dataset fixed_size_sampled --images-per-class 10

# 480-image superset (30/class) — CONTAINS the original 160, topped up with fresh images
python scripts/braintrust/create_braintrust_480_dataset.py

# Two disjoint 160-image validation slices (v3 and v4) from HF test shards
python scripts/braintrust/create_braintrust_160_v3_v4_datasets.py

# Smoke-test dataset from all misclassifications across prompt versions v1-v11
python scripts/braintrust/create_misclassification_smoke_dataset.py --dry-run  # preview first
```

Local preprocessing (before upload): `create_balanced_dataset.py` samples from RVL-CDIP dirs; `create_fixed_size_dataset.py` resizes to a target square with aspect-ratio-preserving padding via `src/image_utils.resize_with_padding()`.

Images are always converted to grayscale PNG at 1024x1024 (with white padding preserving aspect ratio) before upload.

## Cost & Accuracy Metrics

**Accuracy** is `exact_match`: `output.strip().lower() == expected_class`. Scored as 1.0 or 0.0 per row. Failed/errored rows (output starts with `ERROR: `) count as misses and are tracked by a separate `failed` scorer.

**Cost calculation** (`braintrust_report.py:compute_cost`):
- **Expected cost** = `(sum(prompt_tokens) * input_price + sum(completion_tokens) * output_price) / 1e6` — list-price projection from measured token counts
- **Actual cost** = `sum(row.metrics.cost)` — the billed cost OpenRouter reports back via Braintrust
- **Scale-up** = per-image actual/expected extrapolated linearly to 800 / 25,000 / 320,000 images
- `--input-price` and `--output-price` are per-million-token USD rates (check OpenRouter model listing for current values)

**Single-image cost estimation** (`estimate_openrouter_cost.py`): runs one image through the model, records actual token counts and `usage.cost` from the API response, then extrapolates linearly. Updates `docs/experiments/1pic_cost_estimation.md` automatically with per-model sections.

## Braintrust Ecosystem

**Config hierarchy**: `braintrust.env` (gitignored, single source of truth) → loaded by `src/braintrust_config.py` → falls back to `.env` for unset variables. `BraintrustConfig` dataclass exposes: `org_id`, `project_id`, `project_name`, `dataset`, `dataset_project`, `smoke_dataset`, `model`, `qwen_experiments`, `api_key`, `data_api_key`. CLI flags override config per run.

**Key Braintrust concepts used**:
- **Datasets** — rows with `input` (image base64 + filename), `expected` (ground-truth class). Stored in a Braintrust project. Multiple named datasets coexist (`fixed_size_sampled`, `fixed_size_sampled_v2`, `_v3`, `_v4`, `_480`, smoke sets).
- **Experiments** — a named run of a prompt+model against a dataset. Each row produces `output` (predicted class), `scores` (exact_match, failed), and `metadata` (reasoning trace, model, prompt_version). Experiment names follow: `{model}_{prompt_version}_reasoning`.
- **Projects** — the container for experiments and datasets. Current: `AMFAM v2`.
- **Manifests** — JSONL checkpoint files in `reports/manifests/` enable resumable eval runs after interruption. `ManifestStore` (`src/evaluation.py`) tracks per-row status; `--manifest` flag on `braintrust_openrouter_input.py`.

**Eval runner** (`braintrust_openrouter_input.py`): wraps an OpenAI client pointed at OpenRouter with `braintrust.wrap_openai()`. Uses `braintrust.Eval()` to run the classification task with `max_concurrency=8`. Retries transient provider failures (502s, token caps, empty responses) up to `MAX_TRIES=3`; grows `max_tokens` on `finish_reason=length` up to `MAX_TOKENS_CAP=32768`.

**Preflight** (`preflight_eval.py`): validates prompt + dataset without sending any model requests. Run before evals to catch issues early.

**Production eval queue** (`run_eval_queue.py`): runs multiple eval jobs sequentially with preflight checks and manifest verification after each job.

**REST API**: `src/braintrust_utils.py` handles all Braintrust HTTP calls (experiment fetch with pagination/rate-limit retry, dataset CRUD, attachment downloads). API base is always normalized to `.../v1`.

## Debugging Braintrust Errors

### Error surfaces and where to look

| Symptom | Where it appears | Likely cause |
|---|---|---|
| `ERROR: <filename>: ...` on stderr | Eval runner stdout | All 3 retries exhausted — check stderr for the exception text |
| `FAIL` rows in per-image listing | Eval runner stdout | Row produced an `ERROR: ` sentinel output (scored as miss + `failed` metric) |
| `SKIP <class> <filename>: ...` on stderr | Dataset loading | Attachment download failed for one row — eval continues with remaining rows |
| `WARNING: skipped N rows with unreadable attachments` | Dataset loading | Multiple attachment fetches failed — check network/API key |
| `Rate limited, waiting Ns` | Report/visual scripts | Braintrust 429 — exponential backoff up to 30s, 6 retries max |
| `Timeout, retry N/6` | Report/visual scripts | Braintrust fetch timeout (120s) — linear backoff |
| `Error: experiment 'X' not found` | Report/visual scripts | Experiment name misspelled or wrong project_id |
| `No scored task rows found` | `braintrust_report.py` | Experiment still running or all rows failed — check Braintrust UI |
| `manifest metadata does not match` | Manifest load | Reusing a manifest from a different eval config — delete and re-run |
| `Missing environment variables: ...` | Any script | `.env` or `braintrust.env` not populated — check with `require_env()` |

### Eval runner failure modes (`braintrust_openrouter_input.py`)

The retry loop (`MAX_TRIES=3`, linear backoff 2s/4s) handles:
1. **Empty response / `finish_reason=error`** — provider returned no usable content (Alibaba 502s, content filtering)
2. **`finish_reason=length`** — model hit token cap; `max_tokens` doubles on retry, capped at `MAX_TOKENS_CAP=32768`
3. **Network exceptions** — 502, timeout (300s on OpenAI client), connection errors
4. **No valid class in response** — model returned text but `extract_prediction()` found no matching class name

On all-retries-exhausted: writes `status: "error"` to manifest, returns `ERROR: ` sentinel, logs error metadata to Braintrust span. Manifest resume re-attempts `"error"` and `"empty"` rows but skips `"completed"`.

### Braintrust UI debugging

Every eval row logs metadata to its Braintrust span: `raw_response`, `reasoning`, `model`, `prompt_version`, `max_tokens`, `filename`. Error rows also log `error` and `attempts`. Use the Braintrust UI to inspect individual row traces when stdout logs are insufficient.

### Common fixes

- **High failure rate**: check OpenRouter provider status; increase `MAX_TRIES` or `MAX_TOKENS_CAP`
- **All rows fail**: verify `OPENROUTER_API_KEY` is valid and has credits
- **Attachment failures on dataset load**: check `BRAINTRUST_API_KEY` has read access to the dataset project; `DATA_BRAINTRUST_KEY` may be needed for cross-account datasets
- **Manifest errors**: delete `reports/manifests/<name>.jsonl` to start fresh; manifests are keyed by dataset fingerprint so changing the dataset invalidates them

## High-Volume Sampling (No Local Disk)

All `create_braintrust_*.py` scripts stream images from source → in-memory processing → Braintrust upload without saving to the project filesystem. Use these patterns to generate larger dataset slices.

### Data flow (no-disk path)

```
HF Parquet URL → requests.get(stream) → io.BytesIO / temp file
    → pq.read_table() → list[dict] in RAM (label + raw image bytes)
    → deterministic sample (seed + pixel-hash dedup against existing datasets)
    → to_png_bytes(): Image.open(BytesIO) → .convert("L") → resize_with_padding() → .save(BytesIO, "PNG")
    → braintrust.Attachment(data=png_bytes, filename=..., content_type="image/png")
    → dataset.insert(input={...}, expected=class_name, metadata={...})
    → dataset.flush() + dataset.close()
```

### Key patterns

- **`to_png_bytes(tiff_bytes, target_size)`** — converts raw TIFF bytes to 1024x1024 grayscale PNG with white padding, entirely in RAM via `io.BytesIO`
- **Pixel-hash dedup** — `hashlib.sha256(image.convert("L").tobytes()).hexdigest()` ensures no duplicate images across slices
- **Exclusion sets** — new slices load existing Braintrust datasets, hash their images, and skip any matching pixels
- **`--output-dir` is optional** — omit it to skip disk writes entirely; only the Braintrust upload runs
- **Temp parquet** — the 800/480 scripts stream the HF parquet to `/tmp/` and delete it in a `finally` block; the v3/v4 script holds all shards in RAM (no temp file)
- **`dataset.flush()` + `dataset.close()`** — must be called after all inserts to ensure writes complete

### Scaling up

To create a larger slice (e.g., 800 images at 50/class), use the existing `create_braintrust_800_dataset.py` with `--images-per-class 50`. To go beyond 50/class, point at a different HF parquet URL or the full Kaggle RVL-CDIP download. The in-memory pipeline handles thousands of images without disk pressure.

### Upload API pattern

```python
braintrust.login(api_key=api_key)
dataset = braintrust.init_dataset(project_id=config.project_id, name="new_slice_name")
for record in records:
    dataset.insert(
        input={
            "image": braintrust.Attachment(data=png_bytes, filename=fn, content_type="image/png"),
            "metadata": {"class": label, "placeholder": False},
        },
        expected=label,
        metadata={"source": "rvl_cdip_hf_parquet", "slice": "new_slice_name"},
    )
dataset.flush()
dataset.close()
```

For idempotent re-runs (smoke datasets), pass `id=<deterministic_hash>` to `dataset.insert()` and `delete_dataset_by_name()` before `init_dataset()`.

## Changelog Updates

### What is automatically updated

| File | Updated by | Mechanism |
|---|---|---|
| `docs/experiments/experiment_log.md` | `braintrust_metrics_visual.py` | Appends a per-experiment section after generating charts; de-duplicates by checking if experiment name already exists in file |
| `docs/experiments/1pic_cost_estimation.md` | `estimate_openrouter_cost.py` | Idempotent insert-or-replace per `## Model:` section via regex |

### What requires manual updates

| File | When to update |
|---|---|
| `CHANGELOG.md` (root) | After meaningful code changes (new features, bug fixes, config changes). Follow existing `## Unreleased` / `### Changed` / `### Added` format |
| `docs/CHANGELOG.md` (prompt changelog) | After adding a new prompt version to `src/prompts.py`. Document: what changed from previous version, rationale, accuracy results on each dataset slice |
| `src/prompts.py` PROMPTS dict | When adding a prompt version: append `PROMPT_V*` constant, register in `PROMPTS` dict, update `DEFAULT_PROMPT_VERSION` if it should be the new default |

### Agent workflow after running a new experiment

1. Run eval → summarize → report → metrics_visual (auto-appends to `experiment_log.md`)
2. If the experiment used a **new prompt version**: update `docs/CHANGELOG.md` with the version's changes, rationale, and results table row
3. If the experiment produced **meaningful accuracy improvements or regressions**: update `CHANGELOG.md` under `## Unreleased`
4. If the experiment introduced **new failure modes or fixes**: document them in `CHANGELOG.md`
