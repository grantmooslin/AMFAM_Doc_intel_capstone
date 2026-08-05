"""Create two fresh, disjoint 160-image Braintrust evaluation slices.

The Hugging Face RVL-CDIP mirror is the source of truth. Each output contains
10 images per class, is disjoint from existing fixed-size Braintrust datasets,
and is also disjoint from the other newly created slice.

Usage:
    python scripts/braintrust/create_braintrust_160_v3_v4_datasets.py
    python scripts/braintrust/create_braintrust_160_v3_v4_datasets.py --dry-run
"""

import argparse
import base64
import hashlib
import io
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import braintrust
import pyarrow.parquet as pq
import requests
from PIL import Image

from src.braintrust_config import load_braintrust_config
from src.braintrust_utils import delete_dataset_by_name, load_braintrust_dataset
from src.constants import DOCUMENT_CLASSES
from src.env_utils import require_env
from src.image_utils import resize_with_padding

CONFIG = load_braintrust_config()
TARGET_SIZE = (1024, 1024)
PER_CLASS = 10
SLICES = (
    ("fixed_size_sampled_v3", 2303),
    ("fixed_size_sampled_v4", 9413),
)
DEFAULT_EXCLUSIONS = (
    "fixed_size_sampled",
    "fixed_size_sampled_v2",
    "fixed_size_sampled_320",
    "fixed_size_sampled_480",
)
HF_DATASET = "chainyo/rvl-cdip"
HF_REVISION = "66f430a1252ea1732413a80a56a1b6e8bc74264e"
HF_PARQUET_URL = "https://huggingface.co/datasets/chainyo/rvl-cdip/resolve/" + HF_REVISION + "/data/test-{index:05d}-of-00015.parquet"
HF_SHARDS = 15
KAGGLE_DATASET = "pdavpoojan/the-rvlcdip-dataset-test"

# RVL-CDIP numeric label order in the Hugging Face mirror.
LABELS = [
    "letter", "form", "email", "handwritten", "advertisement",
    "scientific_report", "scientific_publication", "specification",
    "file_folder", "news_article", "budget", "invoice", "presentation",
    "questionnaire", "resume", "memo",
]


def download_source() -> list[bytes]:
    shards = []
    for index in range(HF_SHARDS):
        url = HF_PARQUET_URL.format(index=index)
        print(f"Downloading HF shard {index + 1}/{HF_SHARDS}...")
        with requests.get(url, timeout=600) as response:
            response.raise_for_status()
            shards.append(response.content)
    return shards


def load_parquet_rows(data: bytes) -> list[dict]:
    table = pq.read_table(io.BytesIO(data))
    labels = table.column("label").to_pylist()
    images = table.column("image").to_pylist()
    rows = []
    for row_index, (label, image) in enumerate(zip(labels, images)):
        image_bytes = (image or {}).get("bytes")
        if image_bytes is None or not isinstance(label, int) or not 0 <= label < len(LABELS):
            continue
        rows.append({
            "label": LABELS[label],
            "source_index": row_index,
            "image_bytes": image_bytes,
        })
    return rows


def load_rows(shards: list[bytes]) -> list[dict]:
    rows = []
    offset = 0
    for data in shards:
        shard_rows = load_parquet_rows(data)
        for row in shard_rows:
            row["source_index"] += offset
        rows.extend(shard_rows)
        offset += len(shard_rows)
    return rows


def load_kaggle_rows() -> list[dict]:
    """Load a fallback Kaggle checkout when HF has insufficient fresh rows."""
    import kagglehub

    root = Path(kagglehub.dataset_download(KAGGLE_DATASET))
    rows = []
    image_extensions = {".png", ".jpg", ".jpeg", ".tif", ".tiff"}
    for source_index, path in enumerate(sorted(p for p in root.rglob("*") if p.suffix.lower() in image_extensions)):
        label = next((name for name in DOCUMENT_CLASSES if name in {part.lower() for part in path.parts}), None)
        if label is None:
            for name in DOCUMENT_CLASSES:
                if path.name.lower().startswith(name + "_"):
                    label = name
                    break
        if label is None:
            continue
        rows.append({"label": label, "source_index": source_index, "path": path})
    return rows


def render_row(row: dict) -> bytes:
    if "image_bytes" in row:
        return png_bytes(row["image_bytes"])
    with Image.open(row["path"]) as image:
        buffer = io.BytesIO()
        image.save(buffer, format="TIFF")
        return png_bytes(buffer.getvalue())


def png_bytes(source_bytes: bytes) -> bytes:
    with Image.open(io.BytesIO(source_bytes)) as image:
        grayscale = image.convert("L")
        resized = resize_with_padding(grayscale, TARGET_SIZE, fill=255)
        buffer = io.BytesIO()
        resized.save(buffer, format="PNG", dpi=(300, 300))
        return buffer.getvalue()


def pixel_hash(data: bytes) -> str:
    with Image.open(io.BytesIO(data)) as image:
        return hashlib.sha256(image.convert("L").tobytes()).hexdigest()


def load_exclusion_hashes(project: str, datasets: tuple[str, ...], api_key: str, org: str) -> set[str]:
    hashes: set[str] = set()
    for dataset_name in datasets:
        try:
            records = load_braintrust_dataset(
                project,
                dataset_name,
                dataset_api_key=api_key,
                org_id=org,
                api_base=CONFIG.api_base,
            )
        except Exception as exc:
            print(f"WARNING: could not load {project}/{dataset_name}: {exc}", file=sys.stderr)
            continue
        for record in records:
            try:
                hashes.add(pixel_hash(base64.b64decode(record["image_b64"])))
            except Exception as exc:
                print(f"WARNING: could not hash a row from {dataset_name}: {exc}", file=sys.stderr)
        print(f"Loaded {len(records)} rows from {project}/{dataset_name}")
    return hashes


def sample_slices(rows: list[dict], exclusions: set[str]) -> dict[str, list[dict]]:
    by_class: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_class[row["label"]].append(row)

    used = set(exclusions)
    output: dict[str, list[dict]] = {}
    for dataset_name, seed in SLICES:
        rng = random.Random(seed)
        selected: list[dict] = []
        for class_name in DOCUMENT_CLASSES:
            candidates = list(by_class[class_name])
            rng.shuffle(candidates)
            for row in candidates:
                rendered = render_row(row)
                digest = pixel_hash(rendered)
                if digest in used:
                    continue
                used.add(digest)
                selected.append({
                    "label": class_name,
                    "source_index": row["source_index"],
                    "png_bytes": rendered,
                    "hash": digest,
                    "filename": f"rvl_cdip__{class_name}__{len([x for x in selected if x['label'] == class_name]) + 1:04d}.png",
                })
                if sum(item["label"] == class_name for item in selected) == PER_CLASS:
                    break
            count = sum(item["label"] == class_name for item in selected)
            if count != PER_CLASS:
                raise RuntimeError(f"{dataset_name}/{class_name}: selected {count}, need {PER_CLASS}")
        output[dataset_name] = selected
        print(f"{dataset_name}: {len(selected)} rows, seeds {seed}, per-class {dict(Counter(x['label'] for x in selected))}")
    return output


def upload_slice(dataset_name: str, records: list[dict], api_key: str, dry_run: bool) -> None:
    if dry_run:
        return
    deleted = delete_dataset_by_name(api_key, CONFIG.project_id, dataset_name, CONFIG.api_base)
    if deleted:
        print(f"Deleted existing dataset {dataset_name} ({deleted})")

    braintrust.login(api_key=api_key, force_login=True)
    dataset = braintrust.init_dataset(project_id=CONFIG.project_id, name=dataset_name)
    seed = dict(SLICES)[dataset_name]
    for record in records:
        dataset.insert(
            input={
                "image": braintrust.Attachment(
                    data=record["png_bytes"],
                    filename=record["filename"],
                    content_type="image/png",
                ),
                "document_id": f"rvl_cdip_{record['source_index']}",
                "metadata": {
                    "class": record["label"],
                    "source_index": record["source_index"],
                    "pixel_hash": record["hash"],
                    "placeholder": False,
                },
            },
            expected=record["label"],
            metadata={
                "source": "rvl_cdip_hf_parquet",
                "source_url": HF_PARQUET_URL,
                "source_dataset": HF_DATASET,
                "split": "test",
                "slice": "160_images",
                "seed": seed,
                "prompt_validation_target": "v15",
            },
        )
    dataset.flush()
    dataset.close()
    print(f"Uploaded {dataset_name}: {len(records)} rows")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=CONFIG.dataset_project)
    parser.add_argument("--org", default=CONFIG.org_id)
    parser.add_argument("--api-key", default=None)
    parser.add_argument("--exclude-dataset", action="append", default=[])
    parser.add_argument("--source", choices=("hf", "kaggle"), default="hf",
                        help="Primary sampling source; Kaggle is used only when HF cannot satisfy quotas")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    api_key = args.api_key or CONFIG.api_key
    if not api_key and not args.dry_run:
        (api_key,) = require_env("BRAINTRUST_API_KEY")
    exclusions = tuple(dict.fromkeys(DEFAULT_EXCLUSIONS + tuple(args.exclude_dataset) + tuple(name for name, _ in SLICES)))
    existing_hashes = set()
    if api_key:
        existing_hashes = load_exclusion_hashes(args.project, exclusions, api_key, args.org)
    print(f"Exclusion hashes: {len(existing_hashes)}")

    if args.source == "kaggle":
        rows = load_kaggle_rows()
        print(f"Loaded {len(rows)} source rows from Kaggle fallback")
        slices = sample_slices(rows, existing_hashes)
    else:
        source_shards = download_source()
        rows = load_rows(source_shards)
        print(f"Loaded {len(rows)} source rows from the Hugging Face test split")
        try:
            slices = sample_slices(rows, existing_hashes)
        except RuntimeError as hf_error:
            print(f"HF source exhausted for a quota ({hf_error}); using Kaggle fallback...")
            slices = sample_slices(load_kaggle_rows(), existing_hashes)

    for dataset_name, records in slices.items():
        upload_slice(dataset_name, records, api_key or "", args.dry_run)


if __name__ == "__main__":
    main()
