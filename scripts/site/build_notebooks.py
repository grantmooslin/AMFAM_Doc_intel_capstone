"""Generate the three capstone walkthrough notebooks as nbformat v4 JSON.

The notebooks are assembled here as Python cell strings so they stay
reviewable and regenerable. Each notebook is written to ``notebooks/`` at the
repo root and mirrored into ``website/notebooks/`` so the Quarto site can
render it as a static appendix page (the site config disables execution, so
rendering never spends model credits).

Usage:
    python scripts/site/build_notebooks.py
"""

from __future__ import annotations

import json
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NOTEBOOKS_DIR = ROOT / "notebooks"
SITE_NOTEBOOKS_DIR = ROOT / "website" / "notebooks"

BOOTSTRAP = """\
import sys
from pathlib import Path

ROOT = next(
    p for p in (Path.cwd(), *Path.cwd().parents)
    if (p / "src" / "constants.py").exists()
)
sys.path.insert(0, str(ROOT))
print("Repo root:", ROOT)
"""

CONFIG = """\
from src.braintrust_config import load_braintrust_config
from src.env_utils import require_env

config = load_braintrust_config()      # braintrust.env first, then .env
api_key = require_env("OPENROUTER_API_KEY")[0]

print("project:", config.project_name)
print("project_id:", config.project_id)
print("dataset:", config.dataset_project, "/", config.dataset)
print("model:", config.model)
print("braintrust api_key set:", bool(config.api_key))
print("openrouter api_key set:", bool(api_key))
"""


def code(src: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": uuid.uuid4().hex,
        "metadata": {},
        "outputs": [],
        "source": src,
    }


def md(src: str) -> dict:
    return {"cell_type": "markdown", "id": uuid.uuid4().hex, "metadata": {}, "source": src}


def raw(src: str) -> dict:
    return {"cell_type": "raw", "id": uuid.uuid4().hex, "metadata": {}, "source": src}


def notebook(title: str, cells: list[dict]) -> dict:
    frontmatter = raw(f"---\ntitle: {title!r}\n---\n")
    return {
        "cells": [frontmatter, *cells],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.9"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def notebook_01() -> dict:
    return notebook(
        "01 · Environment setup & single-image classification",
        [
            md(
                "# 01 · Environment setup & single-image classification\n"
                "\n"
                "This notebook walks the full **first step** of the capstone pipeline:\n"
                "\n"
                "1. Configure OpenRouter + Braintrust credentials.\n"
                "2. Load a document image from a local RVL-CDIP tree.\n"
                "3. Normalize it exactly like the dataset slices (grayscale, 1024x1024, white padding).\n"
                "4. Ask an OpenRouter vision model to classify it, then parse the prediction.\n"
                "\n"
                "Everything reuses the repo's `src/` library rather than reimplementing logic.\n"
                "See `scripts/braintrust/braintrust_openrouter_input.py` for the full eval runner.\n"
            ),
            md(
                "## Prerequisites\n"
                "\n"
                "```bash\n"
                "pip install -r requirements-dev.txt\n"
                "```\n"
                "\n"
                "Two env files (both gitignored) must exist:\n"
                "\n"
                "- `.env` — `OPENROUTER_API_KEY` (and optionally `RESEARCH_FUNDING_API_KEY`).\n"
                "- `braintrust.env` — single source of truth for the Braintrust org/project/dataset/model.\n"
                "\n"
                "Create them from the templates:\n"
                "\n"
                "```bash\n"
                "cp .env.example .env\n"
                "cp braintrust.env.example braintrust.env\n"
                "```\n"
                "\n"
                "`src/braintrust_config.py` loads `braintrust.env` **first** and only falls back to\n"
                "`.env`, so the Braintrust key always resolves to the current account. Always read\n"
                "keys/ids through `config` from `load_braintrust_config()` — never straight from\n"
                "`os.environ` — or a stale `.env` value can silently win.\n"
            ),
            md("## 0. Bootstrap: repo path + credentials"),
            code(BOOTSTRAP),
            code(CONFIG),
            md(
                "## 1. Load a document image\n"
                "\n"
                "Images follow the filename convention `rvl_cdip__{class}__{NNNN}.png`, which embeds the\n"
                "ground-truth class so `extract_class_from_filename()` can recover the label. Point\n"
                "`image_dir` at any local RVL-CDIP tree (`processed_balanced_dataset/images`,\n"
                "`fixed_size_sampled`, a Kaggle download, ...)."
            ),
            code(
                """\
from src.image_utils import find_images

# EDIT ME: a directory of RVL-CDIP document images (.png/.jpg/.tif/...).
image_dir = ROOT / "processed_balanced_dataset" / "images"
if not image_dir.exists():
    print(f"{image_dir} not found - point 'image_dir' at your local RVL-CDIP tree.")

paths = find_images(image_dir, recursive=True)
print(f"{len(paths)} images found under {image_dir}")

image_path = paths[0] if paths else None
print("Using:", image_path)
"""
            ),
            code(
                """\
from IPython.display import Image as IPImage, display


def extract_class_from_filename(filename: str) -> str:
    # Recover the ground-truth class from 'rvl_cdip__{class}__{NNNN}.png'.
    parts = filename.split("__")
    return parts[1] if len(parts) >= 3 else "?"


display(IPImage(filename=str(image_path), width=360))
print("Filename:", image_path.name)
expected = extract_class_from_filename(image_path.name)
print("Ground-truth class:", expected)
"""
            ),
            md(
                "## 2. Normalize to the standard representation\n"
                "\n"
                "Every dataset slice stores **grayscale 1024x1024 PNGs with white padding** that\n"
                "preserves the aspect ratio (`src/image_utils.resize_with_padding`). Normalizing a\n"
                "single image the same way means a standalone classification matches what the eval\n"
                "runner would see."
            ),
            code(
                """\
from PIL import Image

from src.image_utils import resize_with_padding

img = Image.open(image_path).convert("L")
normalized = resize_with_padding(img, (1024, 1024), fill=255)
print("Normalized size:", normalized.size, "| mode:", normalized.mode)
display(normalized)
"""
            ),
            md(
                "## 3. Build the request payload\n"
                "\n"
                "`src/openrouter_utils.build_vision_messages` packs the prompt text + base64 image into\n"
                "an OpenAI-style `messages` payload. Use the repo's current default prompt\n"
                "(`get_prompt(DEFAULT_PROMPT_VERSION)` = v17.2) rather than a hardcoded string."
            ),
            code(
                """\
from src.image_utils import encode_image_base64
from src.openrouter_utils import build_vision_messages
from src.prompts import DEFAULT_PROMPT_VERSION, get_prompt

prompt = get_prompt(DEFAULT_PROMPT_VERSION)
image_b64 = encode_image_base64(image_path)
messages = build_vision_messages(prompt, image_b64, image_format="png")

print("Prompt version:", DEFAULT_PROMPT_VERSION, "| chars:", len(prompt))
print("Message role:", messages[0]["role"], "| content parts:", len(messages[0]["content"]))
"""
            ),
            md(
                "## 4. Classify (spends OpenRouter credits)\n"
                "\n"
                "The one-liner `classify_image()` uses the module's pinned prompt (v14). To classify\n"
                "with the **current default prompt** (v17.2), send the payload built above directly and\n"
                "parse the answer with `clean_prediction()` / `extract_runner_up()`."
            ),
            code(
                """\
from src.openrouter_classifier import classify_image

result = classify_image(api_key, image_path, model=config.model)
print("model:", result["model"])
print("classification:", result["classification"])
print("status:", result["status"])
print("usage:", result.get("usage"))
print("exact_match:", result["classification"] == expected)
"""
            ),
            code(
                """\
import requests

from src.openrouter_classifier import clean_prediction, extract_runner_up
from src.openrouter_utils import OPENROUTER_API_URL

payload = {
    "model": config.model,
    "messages": build_vision_messages(prompt, image_b64),
    "max_tokens": 4096,
    "temperature": 0.1,
}
resp = requests.post(
    OPENROUTER_API_URL,
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json=payload,
    timeout=120,
)
resp.raise_for_status()
data = resp.json()
raw = data["choices"][0]["message"].get("content") or ""
print("raw tail:", raw[-300:])
print("clean_prediction:", clean_prediction(raw))
print("runner_up:", extract_runner_up(raw))
print("usage:", data.get("usage"))
"""
            ),
            md(
                "## Next\n"
                "\n"
                "Notebook **02 · Balanced sampling & Braintrust upload** turns this single-image flow\n"
                "into a deterministic, class-balanced dataset slice that gets uploaded to Braintrust\n"
                "and queued as a full eval run."
            ),
        ],
    )


def notebook_02() -> dict:
    return notebook(
        "02 · Balanced sampling, Braintrust upload & queuing a run",
        [
            md(
                "# 02 · Balanced sampling, Braintrust upload & queuing a run\n"
                "\n"
                "This notebook builds a **deterministic, class-balanced dataset slice** exactly the way\n"
                "the slice builders do (`scripts/braintrust/create_braintrust_800_dataset.py`):\n"
                "\n"
                "1. Sample `N` images per class with a seeded `random.Random`.\n"
                "2. De-duplicate in **rendered-pixel space** (hash the normalized PNG, never raw bytes).\n"
                "3. Normalize each image to a grayscale 1024x1024 PNG and upload it to Braintrust as a\n"
                "   row attachment.\n"
                "4. Queue an eval run against the new slice.\n"
            ),
            md("## 0. Bootstrap: repo path + credentials"),
            code(BOOTSTRAP),
            code(CONFIG),
            md(
                "## 1. Sampling parameters\n"
                "\n"
                "`N_PER_CLASS` and `SEED` are your spec: the same seed + source always reproduces the\n"
                "same slice. The slice has `16 * N_PER_CLASS` rows (each of the 16 classes in\n"
                "`src.constants.DOCUMENT_CLASSES`)."
            ),
            code(
                """\
from src.constants import DOCUMENT_CLASSES

N_PER_CLASS = 2   # EDIT: images per class -> 16 * N_PER_CLASS total rows
SEED = 42         # EDIT: deterministic sampling seed
print(f"{N_PER_CLASS} per class x {len(DOCUMENT_CLASSES)} classes = {N_PER_CLASS * len(DOCUMENT_CLASSES)} rows")
"""
            ),
            md(
                "## 2. Randomized balanced sample from a local tree\n"
                "\n"
                "This mirrors `scripts/datasets/create_balanced_dataset.py`: walk one directory per\n"
                "class and draw `N_PER_CLASS` files with a seeded RNG. (For larger slices from a Hugging\n"
                "Face parquet mirror, the 800/1600 builders stream the parquet and apply the same\n"
                "sampling + dedup logic.)"
            ),
            code(
                """\
import random
from pathlib import Path

from src.image_utils import find_images

source_root = ROOT / "rvlcdip_dataset"   # EDIT: local RVL-CDIP per-class directory tree

rng = random.Random(SEED)


def sample_balanced(source_root: Path, n_per_class: int, rng: random.Random):
    selected: list[tuple[str, Path]] = []
    for cls in DOCUMENT_CLASSES:
        files = find_images(source_root / cls, recursive=True)
        if len(files) < n_per_class:
            print(f"WARNING: {cls}: only {len(files)} files found")
        for path in rng.sample(files, min(n_per_class, len(files))):
            selected.append((cls, path))
    return selected


selected = sample_balanced(source_root, N_PER_CLASS, rng)
print(f"{len(selected)} images sampled ({N_PER_CLASS}/class x {len(DOCUMENT_CLASSES)} classes)")
for cls, path in selected[:6]:
    print(" ", cls, path.name)
"""
            ),
            md(
                "## 3. Normalize + pixel-hash de-duplication\n"
                "\n"
                "De-duplication is enforced on the **normalized rendered PNG**, so identical images from\n"
                "different files cannot slip past. Each image is rendered to a grayscale 1024x1024 PNG\n"
                "first, hashed, and skipped if the hash was already accepted."
            ),
            code(
                """\
import hashlib
from io import BytesIO

from PIL import Image

from src.image_utils import resize_with_padding


def to_png_bytes(img: Image.Image, target_size=(1024, 1024)) -> bytes:
    img = img.convert("L")
    img = resize_with_padding(img, target_size, fill=255)
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def pixel_hash(png_bytes: bytes) -> str:
    return hashlib.sha256(png_bytes).hexdigest()


cls, path = selected[0]
png = to_png_bytes(Image.open(path))
print(cls, path.name, "->", len(png), "bytes, hash", pixel_hash(png)[:16])
"""
            ),
            md(
                "## 4. Upload to Braintrust (idempotent)\n"
                "\n"
                "The upload matches the documented pattern used by every slice builder:\n"
                "`braintrust.login` -> `init_dataset` -> `insert` with an `Attachment` payload -> "
                "`flush`/`close`. An existing dataset with the same name is deleted first so re-runs\n"
                "are safe. Each row records its `expected` label and provenance metadata."
            ),
            code(
                """\
import braintrust
from braintrust import Attachment

from src.braintrust_utils import delete_dataset_by_name

dataset_name = f"notebook_balanced_{N_PER_CLASS}"

braintrust.login(api_key=config.api_key)
deleted = delete_dataset_by_name(config.api_key, config.project_id, dataset_name, config.api_base)
print("deleted existing dataset" if deleted else "no existing dataset to delete")

dataset = braintrust.init_dataset(project_id=config.project_id, name=dataset_name)
used: set[str] = set()
i = 0
for cls, path in selected:
    png = to_png_bytes(Image.open(path))
    h = pixel_hash(png)
    if h in used:
        print("  skip pixel duplicate:", path.name)
        continue
    used.add(h)
    i += 1
    fn = f"rvl_cdip__{cls}__{i:04d}.png"
    dataset.insert(
        input={
            "image": Attachment(data=png, filename=fn, content_type="image/png"),
            "metadata": {"class": cls, "placeholder": False},
        },
        expected=cls,
        metadata={"source": "notebook-balanced-sample", "seed": SEED, "n_per_class": N_PER_CLASS},
    )
dataset.flush()
dataset.close()
print(f"Uploaded {len(used)} unique images -> dataset '{dataset_name}'")
"""
            ),
            md(
                "## 5. Queue an eval run against the slice\n"
                "\n"
                "Preflight first (validates prompt + dataset, **spends no credits**), then the eval\n"
                "runner (`braintrust_openrouter_input.py`) executes the slice and streams results into\n"
                "both Braintrust and a local JSONL manifest. This step spends OpenRouter credits."
            ),
            code(
                """\
import subprocess
import sys


def run_script(rel_script: str, *args: str) -> None:
    cmd = [sys.executable, str(ROOT / "scripts" / rel_script), *args]
    print("$", " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


experiment_name = f"notebook_{config.model.replace('/', '_')}_v17.2_{dataset_name}"

# 0) Preflight: validates prompt + dataset, spends no credits.
run_script("braintrust/preflight_eval.py", "--dataset", dataset_name, "--prompt-version", "v17.2")

# 1) Queue the eval run (this spends OpenRouter credits).
run_script(
    "braintrust/braintrust_openrouter_input.py",
    "--dataset", dataset_name,
    "--prompt-version", "v17.2",
    "--model", config.model,
    "--experiment-name", experiment_name,
    "--manifest", str(ROOT / "reports" / "manifests" / f"{experiment_name}.jsonl"),
)
"""
            ),
            md(
                "## Next\n"
                "\n"
                "Notebook **03 · Watchers, evaluators & full experiment launch** covers preflight,\n"
                "monitoring a run from the manifest, crash-proof resume, and the post-run scoring/\n"
                "reporting chain."
            ),
        ],
    )


def notebook_03() -> dict:
    return notebook(
        "03 · Watchers, evaluators & launching a full experiment",
        [
            md(
                "# 03 · Watchers, evaluators & launching a full experiment\n"
                "\n"
                "Once `.env` / `braintrust.env` are configured, this notebook shows the complete\n"
                "experiment lifecycle used by the production scripts:\n"
                "\n"
                "1. **Preflight** — validate prompt + dataset with zero model credits.\n"
                "2. **Evaluators** — the three Braintrust scorers registered by the runner.\n"
                "3. **Launch** — start a full experiment run.\n"
                "4. **Watchers** — monitor progress from the JSONL manifest; resume after a crash.\n"
                "5. **Report** — score locally, then generate summary/report/charts.\n"
            ),
            md("## 0. Bootstrap: repo path + credentials"),
            code(BOOTSTRAP),
            code(CONFIG),
            md(
                "## 1. Preflight (zero credits)\n"
                "\n"
                "`preflight_eval.py` checks that the prompt version resolves and the dataset is\n"
                "reachable under the current credentials **without sending any model request**.\n"
                "Run it before any eval to catch setup problems early."
            ),
            code(
                """\
import subprocess
import sys


def run_script(rel_script: str, *args: str) -> None:
    cmd = [sys.executable, str(ROOT / "scripts" / rel_script), *args]
    print("$", " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


run_script("braintrust/preflight_eval.py", "--dataset", config.dataset, "--prompt-version", "v17.2")
"""
            ),
            md(
                "## 2. Evaluators registered by the runner\n"
                "\n"
                "The eval runner wraps the OpenAI client with `braintrust.wrap_openai()` and runs\n"
                "`braintrust.Eval(..., scores=[...])`. Exactly three scorers are registered:\n"
                "\n"
                "- **`exact_match`** — `output.strip().lower() == expected_class`, scored 1.0/0.0.\n"
                "- **`failure`** — rows whose output starts with `ERROR: ` (count as misses too).\n"
                "- **`cost`** — each row's actual billed USD from OpenRouter's `usage.cost`.\n"
                "\n"
                "Near-miss (runner-up == expected while predicted != expected) is **not** a Braintrust\n"
                "scorer — it is computed locally from the runner-up line the manifest records, by\n"
                "`score_manifest.py`.\n"
                "\n"
                "Abridged registration from `braintrust_openrouter_input.py`:\n"
                "\n"
                "```python\n"
                "from braintrust import Eval, wrap_openai\n"
                "from openai import OpenAI\n"
                "\n"
                "client = wrap_openai(OpenAI(base_url=OPENROUTER_BASE_URL, api_key=key))\n"
                "\n"
                "Eval(\n"
                "    dataset=dataset_rows,\n"
                "    task=classify_row,          # returns (output, metadata) per row\n"
                "    scores=[exact_match, failure, cost],\n"
                "    metadata={\"model\": model, \"prompt_version\": prompt_version},\n"
                "    max_concurrency=8,\n"
                ")\n"
                "```\n"
            ),
            md(
                "## 3. Launch a full experiment\n"
                "\n"
                "Launch the runner in the background against the configured dataset. Each completed row\n"
                "is written to a **local JSONL manifest** (the durable checkpoint) as well as Braintrust,\n"
                "so the run survives crashes, Braintrust limits, and quota errors."
            ),
            code(
                """\
experiment_name = f"notebook_full_{config.model.replace('/', '_')}_v17.2"
manifest = ROOT / "reports" / "manifests" / f"{experiment_name}.jsonl"

cmd = [
    sys.executable,
    str(ROOT / "scripts" / "braintrust" / "braintrust_openrouter_input.py"),
    "--dataset", config.dataset,
    "--prompt-version", "v17.2",
    "--model", config.model,
    "--experiment-name", experiment_name,
    "--manifest", str(manifest),
]
print("$", " ".join(cmd))
proc = subprocess.Popen(cmd, cwd=ROOT)
print("Launched PID:", proc.pid)
"""
            ),
            md(
                "## 4. Watch the run from the manifest\n"
                "\n"
                "Re-run this cell as the eval runs: it counts the final status per unique filename.\n"
                "Each manifest record carries a `status` (`completed` / `error` / `empty`) plus\n"
                "`runner_up` and `cost`; the eval runner retries transient provider failures up to\n"
                "`MAX_TRIES=3`, growing `max_tokens` toward `MAX_TOKENS_CAP=32768` on length caps."
            ),
            code(
                """\
import json
from pathlib import Path


def manifest_status_counts(path: Path) -> dict:
    counts: dict[str, int] = {}
    if not path.exists():
        return {"(manifest not created yet)": 0}
    for line in path.read_text().splitlines()[1:]:
        if not line.strip():
            continue
        rec = json.loads(line)
        status = rec.get("status", "empty")
        counts[status] = counts.get(status, 0) + 1
    return counts


manifest_status_counts(manifest)
"""
            ),
            md(
                "## 5. Crash-proof resume\n"
                "\n"
                "If a run dies (crash, Braintrust cap, quota 403), re-invoke the runner through\n"
                "`resume_until_complete.py` until `--expected-rows` unique filenames have a final\n"
                "status. Completed rows are skipped; failed/error rows are re-attempted. On completion\n"
                "it auto-scores the manifest locally with `score_manifest.py` (no Braintrust scorer\n"
                "credits). For production, `run_eval_queue.py` chains multiple jobs sequentially with\n"
                "preflight checks and manifest verification between jobs."
            ),
            code(
                """\
# Illustrative: re-invokes the runner until every row is finished.
# Expected rows must equal the dataset slice size (fixed_size_sampled = 160).
cmd = [
    sys.executable,
    str(ROOT / "scripts" / "braintrust" / "resume_until_complete.py"),
    "--dataset", config.dataset,
    "--prompt-version", "v17.2",
    "--model", config.model,
    "--max-tokens", "8192",
    "--experiment-name", experiment_name,
    "--manifest", str(manifest),
    "--expected-rows", "160",
]
print("$", " ".join(cmd))
# subprocess.run(cmd, cwd=ROOT, check=True)   # uncomment to run
"""
            ),
            md(
                "## 6. Post-run scoring & reporting\n"
                "\n"
                "The full reporting chain (also wired in `scripts/braintrust/`):\n"
                "\n"
                "1. `score_manifest.py` — local scoring from the manifest, no Braintrust credits.\n"
                "2. `summarize_braintrust_experiment.py` — per-image OK/MISS summary + exact_match.\n"
                "3. `braintrust_report.py` — accuracy, confusion matrix (PNG+MD), misclassification\n"
                "   reasoning, cost breakdown (adjust `--input-price`/`--output-price` to the current\n"
                "   OpenRouter model rates).\n"
                "4. `braintrust_metrics_visual.py` — per-class chart + heatmap, and appends the\n"
                "   experiment to `docs/experiments/experiment_log.md`."
            ),
            code(
                """\
run_script("braintrust/score_manifest.py", "--manifest", str(manifest))

run_script("braintrust/summarize_braintrust_experiment.py", "--experiment", experiment_name)

run_script(
    "braintrust/braintrust_report.py",
    "--experiment", experiment_name,
    "--model", config.model,
    "--prompt-version", "v17.2",
    "--dataset", config.dataset,
    "--images-per-class", "10",
    "--input-price", "0.03",
    "--output-price", "0.13",
)

run_script("braintrust/braintrust_metrics_visual.py", experiment_name)
"""
            ),
            md(
                "## Recap\n"
                "\n"
                "1. Preflight validates prompt + dataset with zero credits.\n"
                "2. The runner registers `exact_match`, `failure`, and `cost` scorers.\n"
                "3. A full run writes every row to the local manifest as well as Braintrust.\n"
                "4. Watch progress from the manifest; resume with `resume_until_complete.py`.\n"
                "5. Score locally, then generate the summary / report / charts / experiment log.\n"
                "\n"
                "Inspect individual row traces in the Braintrust UI (each span carries `raw_response`,\n"
                "`reasoning`, `model`, `prompt_version`, `filename`, and error rows add `error`/`attempts`)."
            ),
        ],
    )


def write_notebook(path: Path, nb: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(nb, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {path} ({len(nb['cells'])} cells)")


def main() -> None:
    for name, builder in [
        ("01_env_setup_and_single_image.ipynb", notebook_01),
        ("02_balanced_sampling_and_braintrust_upload.ipynb", notebook_02),
        ("03_watchers_evaluators_full_experiment.ipynb", notebook_03),
    ]:
        nb = builder()
        write_notebook(NOTEBOOKS_DIR / name, nb)
        write_notebook(SITE_NOTEBOOKS_DIR / name, nb)


if __name__ == "__main__":
    main()
