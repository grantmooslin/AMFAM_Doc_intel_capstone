# Core Library (`src/`)

The `src/` package contains the shared Python library used by all scripts. It has no runnable
CLI of its own — scripts import from it (they insert the repository root on `sys.path`, so
`from src.<module> import ...` works from any location).

## Modules

| Module | Contents |
|---|---|
| `constants.py` | Single source of truth for the 16 RVL-CDIP `DOCUMENT_CLASSES` and `IMAGE_EXTENSIONS`. |
| `image_utils.py` | `encode_image_base64()`, `find_images()` (recursive discovery), `resize_with_padding()` (aspect-ratio-preserving, padded). |
| `openrouter_utils.py` | OpenRouter API endpoints and `build_vision_messages()` (OpenAI-style messages with a base64 image). |
| `openrouter_classifier.py` | `classify_image()` (send an image to an OpenRouter vision model), `clean_prediction()`, `VALID_CLASSES`. |
| `prompts.py` | Versioned classification prompts through `PROMPT_V15`, the `PROMPTS` map, `get_prompt()`, `list_prompt_versions()`, and strict `DEFAULT_PROMPT_VERSION` (`v15`). |
| `document_processor.py` | PDF → 300 DPI grayscale PNG conversion with spatial OCR (word bounding boxes). `DocumentProcessor`, `BatchProcessor`, `ClassOrganizedBatchProcessor`, `process_pdf_file()`, `process_pdf_bytes()`. |
| `env_utils.py` | `load_dotenv_if_available()`, `require_env()` (loads `.env`, validates required variables). |
| `cli_utils.py` | `print_header()` — console output helpers. |
| `braintrust_config.py` | `load_braintrust_config()` and the `BraintrustConfig` dataclass — reads `braintrust.env` (single source of truth), falls back to `.env`. |
| `braintrust_utils.py` | Shared Braintrust wire-protocol helpers: `list_experiments()`, `list_datasets()`, `delete_dataset_by_name()`, `fetch_experiment_rows()`, `resolve_prompt_version()`, `find_misses()`, `fetch_attachment_bytes()`, `load_braintrust_dataset()`. |

## Usage

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # if you are in a subdirectory

from src.prompts import get_prompt, list_prompt_versions
from src.openrouter_classifier import classify_image, VALID_CLASSES
from src.braintrust_config import load_braintrust_config
```

## Prompt versions

`prompts.py` carries the full evolution of the classification prompt (v1 baseline through v14, plus
v11.5 and v11.6). Versions differ in disambiguation rules, decision-cascade structure, and the optional scratchpad
deliberation step. See `docs/prompt_rules_provenance.md` for the provenance of each rule and
`docs/experiments/experiment_log.md` for how each version performed.
