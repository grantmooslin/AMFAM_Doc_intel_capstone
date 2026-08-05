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

- `.env` — API keys: `OPENROUTER_API_KEY`, `BRAINTRUST_API_KEY`; optional `RESEARCH_FUNDING_API_KEY`, `DATA_BRAINTRUST_KEY`, `BRAINTRUST_SOURCE_API_KEY`, `BRAINTRUST_DEST_API_KEY`
- `braintrust.env` — single source of truth for Braintrust org/project/dataset/model config, loaded by `src/braintrust_config.py`

Copy `*.env.example` templates to create them. Missing env vars cause `sys.exit(1)` via `src/env_utils.require_env()`.

System binaries required: **Tesseract OCR** and **Poppler** (for `pdf2image`).

### Research Funding API Key (`RESEARCH_FUNDING_API_KEY`)

`RESEARCH_FUNDING_API_KEY` (optional, in `.env`) is a separate OpenRouter key reserved for **large or significant runs only**:

- **Default access**: every run uses `OPENROUTER_API_KEY` as its OpenRouter access point. All routine testing and prompt iteration runs on the default key.
- **Explicit invocation only**: the research funding key is used only when a script explicitly requests it — e.g. `run_v11_8_800_after_480.py` calls `require_env("RESEARCH_FUNDING_API_KEY")` and injects it into the child eval's environment. It is never selected by default.
- **Vetting gate**: it is only saved for runs that have passed all vetting steps — a settled, most-confident prompt that has cleared preflight and prior slice evaluations — such as a final 800-image slice on the current best prompt.
- **Automatic failover**: `braintrust_openrouter_input.py:_candidate_keys()` falls back to `RESEARCH_FUNDING_API_KEY` when the primary key hits an OpenRouter quota/credit 403, so a funded run survives the default key running out of credits.

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

Manifest-backed runs (no `--experiment` needed; also matches Braintrust's resume-loop version suffixes like `-06b91b68`):

```bash
# Full report suite directly from a manifest + Braintrust trace merge
python scripts/braintrust/braintrust_report_manifest.py \
  --manifest reports/manifests/qwen3.7-flash_v11.8_1600_balanced_1120.jsonl \
  --input-price 0.03 --output-price 0.13
```

Artifacts produced in `reports/`: `report_<experiment>.md`, `confusion_matrix_<experiment>.{png,md}`, `per_class_accuracy_<experiment>.png`, `misclassification_reasoning_<experiment>.md`.

`braintrust_metrics_visual.py` and `braintrust_report_manifest.py` also append to `docs/experiments/experiment_log.md` (skips experiments already recorded).

## Quarto Site & Notebooks

The shareable documentation site lives in `website/` and is published from there (e.g. `quarto publish posit-connect-cloud` from `website/`). It renders offline with **no API/network spend**.

```bash
# 1. Regenerate charts (SVGs) from committed markdown reports
python scripts/site/build_site_charts.py

# 2. Regenerate the documentation pages (methods, results, prompt evolution,
#    cost, monte carlo, appendix) from docs/reports/ into website/**/*.qmd
python scripts/site/build_site.py

# 3. Regenerate the three walkthrough notebooks (repo + website copies)
python scripts/site/build_notebooks.py

# 4. Render the site (execution is disabled via `execute: {enabled: false}`)
quarto render website/
```

- `scripts/site/build_site_charts.py` — 34 SVG charts from `reports/` + `docs/experiments/` (accuracy arcs, per-class, confusion heatmaps, cost, Monte Carlo ALE/stop-word).
- `scripts/site/build_site.py` — wraps docs/reports into `website/**/*.qmd`; fixes `$` costs corrupted by `/bin/zsh.`; rewrites asset paths; builds the misclassification appendix (markdown traces inside `<details>`, one open per class) and the classes page from `src/constants.py`.
- `scripts/site/build_notebooks.py` — emits the three nbformat v4 walkthrough notebooks to `notebooks/` and mirrors them into `website/notebooks/`. Regenerate after any prompt/runner change that the notebooks reference.
- `website/_quarto.yml` — `cosmo` theme + `assets/css/custom.scss`; navbar groups (Methods & Reference, Results, Prompt Evolution, Cost Analysis, Monte Carlo, Notebooks, Appendix); `execute: {enabled: false}` so notebook pages render statically.
- `website/_site/` is gitignored (render output).

The three notebooks are the end-to-end onboarding path: **01** env setup + single-image classification, **02** deterministic balanced sampling + idempotent Braintrust upload + queuing a run, **03** preflight, the three registered evaluators, manifest watchers, crash-proof resume, and the post-run scoring/reporting chain.

## Dataset Slices

Datasets are balanced (N images per class x 16 classes) and uploaded to Braintrust as row attachments (base64 PNGs with ground-truth labels). All scripts de-duplicate against existing datasets.

```bash
# 160-image slice (10/class) — from HF parquet mirror, no full RVL-CDIP download needed
python scripts/braintrust/create_braintrust_800_dataset.py --dataset fixed_size_sampled --images-per-class 10

# Disjoint 160-image slice (seed 1738) — fresh test images, pixel-deduped vs fixed_size_sampled + _480
python scripts/braintrust/create_braintrust_160_v2_dataset.py

# Two mutually-disjoint 160-image validation slices (v3/v4, seeds 2303/9413) from HF test shards
python scripts/braintrust/create_braintrust_160_v3_v4_datasets.py

# 480-image superset (30/class) — CONTAINS the original 160, topped up with fresh images
python scripts/braintrust/create_braintrust_480_dataset.py

# 800-image slice (50/class) — train split of the 100/class HF mirror
python scripts/braintrust/create_braintrust_800_dataset.py --dataset rvl_cdip_800 --images-per-class 50

# 1600-image slice (100/class) — train + test + validation splits combined
python scripts/braintrust/create_braintrust_1600_dataset.py --exclude-dataset rvl_cdip_800

# Smoke / eval-union datasets from every misclassification across prompt versions (preview first)
python scripts/braintrust/create_misclassification_smoke_dataset.py --dry-run
python scripts/braintrust/create_v11_v17_eval_dataset.py --dry-run            # v11-v17 union
```

Local preprocessing (before upload): `create_balanced_dataset.py` samples from RVL-CDIP dirs; `create_fixed_size_dataset.py` resizes to a target square with aspect-ratio-preserving padding via `src/image_utils.resize_with_padding()`.

Images are always converted to grayscale PNG at 1024x1024 (with white padding preserving aspect ratio) before upload. Every builder also logs a `create-<dataset>` experiment carrying provenance (source_url, split, seed, target_size, images), so each slice has a traceable build record in Braintrust.

### Slice generation insights

- **Source capacity** — the mirror `jordyvl/rvl_cdip_100_examples_per_class` holds exactly **100 images/class**: train 50 (800), test 25 (400), validation 25 (400). The 800 script draws from train only (`--images-per-class 50` max); the 1600 script combines all three splits (`--images-per-class 100` max). The v3/v4 script reads `chainyo/rvl-cdip` test shards in RAM and falls back to Kaggle `pdavpoojan/the-rvlcdip-dataset-test` when HF cannot satisfy a class quota. Beyond 100/class, point at a different parquet mirror or the full Kaggle RVL-CDIP download.
- **Determinism** — every sampler seeds `random.Random(seed)` (default 42; v2 uses 1738; v3/v4 use 2303/9413). The same seed + source always reproduces the same slice.
- **Disjointness is enforced in rendered-pixel space** — a candidate is converted to the normalized PNG *first*, hashed (`md5`/`sha256` of `image.convert("L").tobytes()`), and accepted only if that hash is not already in the exclusion set. Build exclusion hashes the same way (render → hash), never from raw source bytes; otherwise identical images evade dedup. Accepted images are added to `used_hashes` as sampling proceeds, so a slice is also internally duplicate-free (the 480/1600 scripts print "skipped N pixel duplicates").
- **Building the exclusion set** — load existing slices via `load_braintrust_dataset()` (it honors `DATA_BRAINTRUST_KEY` for cross-account reads), hash every stored attachment, and pass the set into the sampler (e.g. `--exclude-dataset`, `--exclude-dataset-project`). The v3/v4 script aggregates several datasets (v1, v2, _320, _480) plus its own slices before sampling.
- **Rebuild idempotently** — most builders call `delete_dataset_by_name()` before `init_dataset()` so re-runs are safe; eval-union/smoke builders also pass a deterministic `id=<md5(filename)>` to `dataset.insert()`. No builder needs a manual wipe.
- **Upload reliability** — the SDK's background attachment uploader silently drops objects on bulk copies. `copy_datasets_to_new_env.py` uploads synchronously with 8 retries, inserts a row only after its object upload is confirmed, then re-downloads every row to verify. `create_v11_v17_eval_dataset.py` wraps uploads in `upload_rows_with_retry()` (3 tries, 60s wait, dataset rebuilt per attempt so a failure leaves nothing half-written).
- **Eval-union datasets** — `find_misses()` across target experiments, deduped by filename (prefer non-empty/longest reasoning), then the actual PNG is pulled from the slice datasets and re-attached with metadata: `versions`, `predictions`, `misclassification` (`expected -> predicted`), and reasoning capped at 4000 chars. `--cache <path>` persists the deduped records as JSON so re-runs skip experiment fetching; `--skip-experiment` prunes noisy runs.
- **Filename convention** — `rvl_cdip__{class}__{NNNN}.png` embeds the ground-truth class so `extract_class_from_filename()` recovers it; keep this pattern for any new slice so the whole eval/report toolchain keeps working.
- **After porting accounts** — slice builders resolve the project through `load_braintrust_config()`, so once `braintrust.env` points at the new account they create/read datasets there automatically. For slices that must still read source datasets from the previous account, set `DATA_BRAINTRUST_KEY` to a read-only key for that account.

## Cost & Accuracy Metrics

**Accuracy** is `exact_match`: `output.strip().lower() == expected_class`. Scored as 1.0 or 0.0 per row. Failed/errored rows (output starts with `ERROR: `) count as misses and are tracked by a separate `failure` scorer. A third scorer, `cost`, records each row's actual billed USD from OpenRouter's `usage.cost`. These are the only three scorers registered on the Braintrust eval (`exact_match`, `failure`, `cost`); near-miss (runner-up) is computed locally by `score_manifest.py` from the runner-up line the manifest records.

**Cost calculation** (`braintrust_report.py:compute_cost`):
- **Expected cost** = `(sum(prompt_tokens) * input_price + sum(completion_tokens) * output_price) / 1e6` — list-price projection from measured token counts
- **Actual cost** = `sum(row.metrics.cost)` — the billed cost OpenRouter reports back via Braintrust
- **Scale-up** = per-image actual/expected extrapolated linearly to 800 / 25,000 / 320,000 images
- `--input-price` and `--output-price` are per-million-token USD rates (check OpenRouter model listing for current values)

**Single-image cost estimation** (`estimate_openrouter_cost.py`): runs one image through the model, records actual token counts and `usage.cost` from the API response, then extrapolates linearly. Updates `docs/experiments/1pic_cost_estimation.md` automatically with per-model sections.

## Braintrust Ecosystem

**Config hierarchy**: `braintrust.env` (gitignored, single source of truth) → loaded by `src/braintrust_config.py` → falls back to `.env` for unset variables. `BraintrustConfig` dataclass exposes: `org_id`, `project_id`, `project_name`, `dataset`, `dataset_project`, `smoke_dataset`, `model`, `qwen_experiments`, `api_key`, `data_api_key`. CLI flags override config per run.

### Using `braintrust.env`

`braintrust.env` is the **single source of truth** for Braintrust configuration. `src/braintrust_config.py:load_braintrust_config()` loads it first (highest precedence) and only falls back to `.env` for variables it does not set. Today `braintrust.env` carries the **new** account's credentials (`AMFAMv2` org/project plus the new `BRAINTRUST_API_KEY`) while `.env` may still hold the **previous** account's key. Because `braintrust.env` loads first, `config.api_key` from `load_braintrust_config()` resolves to the **new** key — but scripts that read `os.environ["BRAINTRUST_API_KEY"]` directly will silently pick up the stale `.env` value. **Always resolve Braintrust keys/ids via `config.api_key` / `config.project_id` from `load_braintrust_config()`.** OpenRouter keys (`OPENROUTER_API_KEY`, `RESEARCH_FUNDING_API_KEY`) normally live in `.env`.

### Adding / configuring new Braintrust credentials

1. Create the env file from the template: `cp braintrust.env.example braintrust.env` (never commit it — it holds API keys).
2. In the new Braintrust account, generate an API key with write access to the target org/project.
3. Fill in `braintrust.env`: `BRAINTRUST_ORG_ID`, `BRAINTRUST_PROJECT_ID`, `BRAINTRUST_PROJECT_NAME`, `BRAINTRUST_DATASET_PROJECT`, `BRAINTRUST_DATASET`, `BRAINTRUST_SMOKE_DATASET`, `QWEN_EXPERIMENTS`, `BRAINTRUST_MODEL`, `BRAINTRUST_API_BASE`, and the new `BRAINTRUST_API_KEY`.
4. Optional: set `DATA_BRAINTRUST_KEY` to a read-only key for a source account when datasets live in a different org (cross-account reads); leave blank to reuse `BRAINTRUST_API_KEY`.
5. Verify resolution: `python -c "from src.braintrust_config import load_braintrust_config; print(load_braintrust_config())"` should show the new org/project id and a non-empty `api_key`. Then run `python scripts/braintrust/preflight_eval.py --dataset <ds> --prompt-version v17` to confirm the dataset is reachable with the new credentials before spending any model credits.
6. Port any datasets you need from the previous account (below), then re-run experiments against the new project.

### Porting datasets from the previous account

- **Preferred — `copy_datasets_to_new_env.py`**: reads source credentials from `braintrust.env`/`.env` and writes to an explicitly-passed destination (the new account). Attachments are uploaded synchronously with retries (8 attempts) so a row is inserted only after its object upload succeeds, and every row is then verified by re-downloading it.

  ```bash
  python scripts/braintrust/copy_datasets_to_new_env.py \
    --datasets fixed_size_sampled fixed_size_sampled_320 \
    --dest-project-id <new-project-id> \
    --dest-project-name AMFAMv2 \
    --dest-org <new-org-id> \
    --dest-api-key <new-key>          # or export BRAINTRUST_DEST_API_KEY
  ```

  Flags: `--source-project` (defaults to the `braintrust.env` project), `--source-api-key` (or `BRAINTRUST_SOURCE_API_KEY`; defaults to the `braintrust.env` key), `--no-verify` to skip the full re-download check, and `--delete-existing` to drop a same-named destination dataset first (idempotent re-copy).

- **One-off — `copy_braintrust_dataset.py`**: a simple hardcoded variant. Edit the `SOURCE_API_KEY` / `SOURCE_PROJECT` / `SOURCE_DATASET` and `DEST_API_KEY` / `DEST_PROJECT` / `DEST_DATASET` constants at the top before running; no CLI flags. Prefer `copy_datasets_to_new_env.py` for repeatable, verified porting.

**Key Braintrust concepts used**:
- **Datasets** — rows with `input` (image base64 + filename), `expected` (ground-truth class). Stored in a Braintrust project. Multiple named datasets coexist (`fixed_size_sampled`, `fixed_size_sampled_v2`, `_v3`, `_v4`, `_480`, smoke sets).
- **Experiments** — a named run of a prompt+model against a dataset. Each row produces `output` (predicted class), `scores` (exact_match, failure, cost), and `metadata` (reasoning trace, model, prompt_version, runner_up, cost). Experiment names follow: `{model}_{prompt_version}_reasoning`. Near-miss (runner_up == expected while predicted != expected) is computed locally by `score_manifest.py` from the runner-up line, not by a Braintrust scorer.
- **Projects** — the container for experiments and datasets. Current: `AMFAM v2`.
- **Manifests** — JSONL checkpoint files in `reports/manifests/` enable resumable eval runs after interruption. `ManifestStore` (`src/evaluation.py`) tracks per-row status; `--manifest` flag on `braintrust_openrouter_input.py`. Each completed record carries a `tag` (`OK`/`MISS!`/`ERROR!`) plus `runner_up` and `cost`; `score_manifest.load_manifest()` derives the tag in-memory when absent.

**Eval runner** (`braintrust_openrouter_input.py`): wraps an OpenAI client pointed at OpenRouter with `braintrust.wrap_openai()`. Uses `braintrust.Eval()` to run the classification task with `max_concurrency=8`. Retries transient provider failures (502s, token caps, empty responses) up to `MAX_TRIES=3`; grows `max_tokens` on `finish_reason=length` up to `MAX_TOKENS_CAP=32768`.

**Preflight** (`preflight_eval.py`): validates prompt + dataset without sending any model requests. Run before evals to catch issues early.

**Production eval queue** (`run_eval_queue.py`): runs multiple eval jobs sequentially with preflight checks and manifest verification after each job.

**REST API**: `src/braintrust_utils.py` handles all Braintrust HTTP calls (experiment fetch with pagination/rate-limit retry, dataset CRUD, attachment downloads). API base is always normalized to `.../v1`.

## Debugging Braintrust Errors

### Error surfaces and where to look

| Symptom | Where it appears | Likely cause |
|---|---|---|
| `ERROR: <filename>: ...` on stderr | Eval runner stdout | All 3 retries exhausted — check stderr for the exception text |
| `FAIL` rows in per-image listing | Eval runner stdout | Row produced an `ERROR: ` sentinel output (scored as miss + `failure` metric) |
| `SKIP <class> <filename>: ...` on stderr | Dataset loading | Attachment download failed for one row — eval continues with remaining rows |
| `WARNING: skipped N rows with unreadable attachments` | Dataset loading | Multiple attachment fetches failed — check network/API key |
| `Rate limited, waiting Ns` | Report/visual scripts | Braintrust 429 — exponential backoff up to 30s, 6 retries max |
| `Timeout, retry N/6` | Report/visual scripts | Braintrust fetch timeout (120s) — linear backoff |
| `Error: experiment 'X' not found` | Report/visual scripts | Experiment name misspelled or wrong project_id |
| `No scored task rows found` | `braintrust_report.py` | Experiment still running or all rows failed — check Braintrust UI |
| `manifest metadata does not match` | Manifest load | Reusing a manifest from a different eval config — delete and re-run |
| Quota/credit `403` on a funded run | Eval runner stdout | Primary OpenRouter key out of credits; `_candidate_keys()` fails over to `RESEARCH_FUNDING_API_KEY` if set |
| Experiments/datasets point at the old account | Report/visual scripts | `.env` still holds the previous account's `BRAINTRUST_API_KEY`; ensure `braintrust.env` holds the new key and the script uses `config.api_key` from `load_braintrust_config()` |
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
- **All rows fail**: verify the OpenRouter key is valid and has credits — `OPENROUTER_API_KEY` for routine runs, `RESEARCH_FUNDING_API_KEY` for a vetted large/funded run
- **Attachment failures on dataset load**: check `BRAINTRUST_API_KEY` has read access to the dataset project; `DATA_BRAINTRUST_KEY` may be needed for cross-account datasets
- **Stale `.env` Braintrust key**: `.env` may carry the previous account's key while `braintrust.env` holds the new one — always use `config.api_key` from `load_braintrust_config()` so the new key wins over any stale `.env` value
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
- **Pixel-hash dedup** — hash the *normalized rendered* PNG (`hashlib.md5`/`sha256` of `image.convert("L").tobytes()`), never raw source bytes. Hash output must match what a later slice would render, so dedup stays effective across slices; the 480/1600 builders render first, then hash.
- **Exclusion sets** — new slices load existing Braintrust datasets via `load_braintrust_dataset()`, hash their stored attachments, and skip any matching pixels (see "Slice generation insights" in Dataset Slices for the full rules)
- **`--output-dir` is optional** — omit it to skip disk writes entirely; only the Braintrust upload runs
- **Temp parquet** — the 800/480/1600 scripts stream the HF parquet to `/tmp/` (atomically via a `.part` file) and delete it in a `finally` block; the v3/v4 script holds all shards in RAM (no temp file)
- **Provenance experiment** — every builder logs a `create-<dataset>` experiment with source_url/split/seed/target_size so each slice is reproducible and attributable
- **`dataset.flush()` + `dataset.close()`** — must be called after all inserts to ensure writes complete

### Scaling up

To create a larger slice (e.g., 800 images at 50/class), use the existing `create_braintrust_800_dataset.py` with `--images-per-class 50`. To go beyond 50/class, point at a different HF parquet URL or the full Kaggle RVL-CDIP download. The in-memory pipeline handles thousands of images without disk pressure. Remember the source ceiling: the 100/class mirror tops out at 800 (train) / 1600 (all three splits combined).

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
