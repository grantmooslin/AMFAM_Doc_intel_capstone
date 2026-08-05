"""
Build an 800-image RVL-CDIP sample slice (50 per class x 16 classes) and upload it
to a Braintrust dataset WITHOUT downloading the full RVL-CDIP corpus (~5GB+).

The script streams a single public Hugging Face parquet mirror of RVL-CDIP
(``jordyvl/rvl_cdip_100_examples_per_class``, train split = exactly 50 images per
class = 800 rows), converts each TIFF to a 1024x1024 grayscale PNG (aspect-ratio
preserving, white padding), and inserts every image into a Braintrust dataset as a
row attachment. The parquet is held in a temp file and deleted afterward, so no
full dataset is ever stored on your machine.

Prerequisites:
    pip install braintrust pyarrow Pillow requests
    Set BRAINTRUST_API_KEY in your .env file or environment. Runs and the dataset
    are written to the project that key can access (default: the "AMFAM v2"
    project in org cc595192-8420-461d-8111-1d3ca1b42948).

Usage:
    python scripts/braintrust/create_braintrust_800_dataset.py
    python scripts/braintrust/create_braintrust_800_dataset.py --dataset rvl_cdip_800
    python scripts/braintrust/create_braintrust_800_dataset.py --project "AMFAM v2"
    python scripts/braintrust/create_braintrust_800_dataset.py --images-per-class 50 --seed 42
    python scripts/braintrust/create_braintrust_800_dataset.py --output-dir ./fixed_size_sampled
"""

from __future__ import annotations

import argparse
import io
import os
import random
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import braintrust
import pyarrow.parquet as pq
import requests
from PIL import Image

from src.braintrust_config import load_braintrust_config
from src.constants import DOCUMENT_CLASSES
from src.env_utils import require_env
from src.image_utils import resize_with_padding

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_CONFIG = load_braintrust_config()
DEFAULT_ORG = _CONFIG.org_id
DEFAULT_PROJECT = _CONFIG.project_name
DEFAULT_PROJECT_ID = _CONFIG.project_id
DEFAULT_DATASET = "rvl_cdip_800"
DEFAULT_TARGET_SIZE = (1024, 1024)
DEFAULT_IMAGES_PER_CLASS = 50
DEFAULT_SEED = 42

# Public HF parquet mirror of RVL-CDIP with 100 examples per class.
# Train split contains exactly 50 images per class (800 rows).
SOURCE_PARQUET_URL = (
    "https://huggingface.co/datasets/jordyvl/rvl_cdip_100_examples_per_class/"
    "resolve/main/data/train-00000-of-00001-81f1d229db782541.parquet"
)

# RVL-CDIP numeric label order (0-15), as documented on the official dataset page.
RVL_CDIP_LABELS = [
    "letter",
    "form",
    "email",
    "handwritten",
    "advertisement",
    "scientific_report",
    "scientific_publication",
    "specification",
    "file_folder",
    "news_article",
    "budget",
    "invoice",
    "presentation",
    "questionnaire",
    "resume",
    "memo",
]


# ---------------------------------------------------------------------------
# Download + row loading (streamed, temp-only)
# ---------------------------------------------------------------------------

def download_parquet(url: str, cache_dir: Path) -> Path:
    """Stream the source parquet into a temp file (not the full dataset).

    Writes to a ``.part`` file and atomically renames it into place so an
    interrupted/flaky download never leaves a partial file that a later run
    would mistake for a valid cache.
    """
    dest = cache_dir / "rvl_cdip_source.parquet"
    if dest.exists() and dest.stat().st_size > 0:
        print(f"Using cached source parquet: {dest}")
        return dest

    part = cache_dir / "rvl_cdip_source.parquet.part"
    if part.exists():
        part.unlink()

    print(f"Downloading source parquet ({url})...")
    with requests.get(url, stream=True, timeout=600) as response:
        response.raise_for_status()
        total = int(response.headers.get("Content-Length", 0))
        written = 0
        with open(part, "wb") as f:
            for chunk in response.iter_content(chunk_size=1 << 20):
                f.write(chunk)
                written += len(chunk)
                if total:
                    pct = written / total * 100
                    print(f"\r  {written / 1e6:,.1f} / {total / 1e6:,.1f} MB ({pct:.0f}%)", end="", flush=True)
        print()
    os.replace(part, dest)
    print(f"Downloaded {dest.stat().st_size / 1e6:,.1f} MB to {dest}")
    return dest


def load_parquet_rows(parquet_path: Path) -> list[dict]:
    """Read all rows; return [{label, image_bytes, row_index}]."""
    table = pq.read_table(str(parquet_path))
    labels = table.column("label").to_pylist()
    images = table.column("image").to_pylist()
    rows = []
    for i, (label, image) in enumerate(zip(labels, images)):
        bytes_ = (image or {}).get("bytes")
        if bytes_ is None:
            print(f"  Skipping row {i}: missing image bytes")
            continue
        class_name = RVL_CDIP_LABELS[label] if isinstance(label, int) and 0 <= label < len(RVL_CDIP_LABELS) else str(label)
        rows.append({"label": class_name, "image_bytes": bytes_, "row_index": i})
    return rows


def sample_rows(rows: list[dict], images_per_class: int, seed: int) -> list[dict]:
    """Deterministically sample ``images_per_class`` images from each class."""
    by_class: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_class[row["label"]].append(row)

    rng = random.Random(seed)
    sampled: list[dict] = []
    for class_name in sorted(by_class):
        available = by_class[class_name]
        n = min(images_per_class, len(available))
        picked = rng.sample(available, n)
        for i, row in enumerate(picked):
            row["filename"] = f"rvl_cdip__{class_name}__{i + 1:04d}.png"
        sampled.extend(picked)

    print(f"Sampled {len(sampled)} images ({images_per_class} per class target)")
    for class_name in sorted(by_class):
        count = sum(1 for r in sampled if r["label"] == class_name)
        print(f"  {class_name:<24} {count}")
    return sampled


def to_png_bytes(tiff_bytes: bytes, target_size: tuple[int, int]) -> bytes:
    """Convert a TIFF blob to a fixed-size padded grayscale PNG (300 DPI metadata)."""
    with Image.open(io.BytesIO(tiff_bytes)) as img:
        if img.mode != "L":
            img = img.convert("L")
        padded = resize_with_padding(img, target_size, fill=255)
        buffer = io.BytesIO()
        padded.save(buffer, format="PNG", dpi=(300, 300))
        return buffer.getvalue()


# ---------------------------------------------------------------------------
# Braintrust upload + run logging
# ---------------------------------------------------------------------------

def upload_dataset(
    records: list[dict],
    project: str,
    project_id: str,
    org: str,
    dataset_name: str,
    api_key: str,
    target_size: tuple[int, int],
    source_url: str,
    seed: int,
) -> dict:
    """Insert all records into the Braintrust dataset and log a summary run."""
    braintrust.login(api_key=api_key)
    dataset = braintrust.init_dataset(project_id=project_id, name=dataset_name)

    experiment = braintrust.init_experiment(
        project_id=project_id,
        experiment=f"create-{dataset_name}",
        description=f"Build {len(records)}-image RVL-CDIP slice and store as Braintrust dataset '{dataset_name}'",
        metadata={
            "task": "dataset_creation",
            "project": project,
            "org": org,
            "dataset": dataset_name,
            "source_url": source_url,
            "target_size": list(target_size),
            "seed": seed,
            "images": len(records),
        },
    )

    inserted = 0
    failed = 0
    per_class = Counter()
    total_bytes = 0
    failures: list[str] = []

    for i, record in enumerate(records):
        class_name = record["label"]
        filename = record["filename"]
        try:
            png_bytes = to_png_bytes(record["image_bytes"], target_size)
            input_data = {
                "image": braintrust.Attachment(
                    data=png_bytes,
                    filename=filename,
                    content_type="image/png",
                ),
                "document_id": f"rvl_cdip_{record['row_index']}",
                "metadata": {
                    "class": class_name,
                    "placeholder": False,
                    "source_file": filename,
                    "source_index": record["row_index"],
                },
            }
            dataset.insert(
                input=input_data,
                expected=class_name,
                metadata={
                    "source": "rvl_cdip_hf_parquet",
                    "slice": f"{len(records)}_images",
                    "split": "train",
                    "seed": seed,
                },
            )
            inserted += 1
            per_class[class_name] += 1
            total_bytes += len(png_bytes)
        except Exception as e:
            failed += 1
            failures.append(f"{filename}: {e}")

        if (i + 1) % 50 == 0:
            print(f"  Inserted {i + 1}/{len(records)} records...")

    dataset.flush()
    dataset.close()

    n = max(1, len(records))
    experiment.log(
        input={"dataset": dataset_name, "records": len(records)},
        output={"inserted": inserted, "failed": failed, "dataset_name": dataset_name},
        scores={"insertion_rate": inserted / n, "failure_rate": failed / n},
        metrics={"images": inserted, "classes": len(per_class), "total_bytes": total_bytes},
        metadata={
            "per_class": dict(per_class),
            "failures": failures,
            "project": project,
            "org": org,
        },
    )
    experiment.close()

    return {"inserted": inserted, "failed": failed, "per_class": dict(per_class), "total_bytes": total_bytes}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=DEFAULT_PROJECT,
                        help=f"Display name of the Braintrust project (default: {DEFAULT_PROJECT})")
    parser.add_argument("--project-id", default=DEFAULT_PROJECT_ID,
                        help=f"Braintrust project id for the dataset and run (default: {DEFAULT_PROJECT_ID})")
    parser.add_argument("--org", default=DEFAULT_ORG,
                        help=f"Braintrust org id (default: {DEFAULT_ORG})")
    parser.add_argument("--dataset", default=DEFAULT_DATASET,
                        help=f"Braintrust dataset name (default: {DEFAULT_DATASET})")
    parser.add_argument("--images-per-class", type=int, default=DEFAULT_IMAGES_PER_CLASS,
                        help=f"Images to sample per class (default: {DEFAULT_IMAGES_PER_CLASS})")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED,
                        help=f"Random seed for sampling (default: {DEFAULT_SEED})")
    parser.add_argument("--target-size", type=int, nargs=2, default=list(DEFAULT_TARGET_SIZE),
                        metavar=("W", "H"),
                        help=f"Output image size W H (default: {DEFAULT_TARGET_SIZE[0]} {DEFAULT_TARGET_SIZE[1]})")
    parser.add_argument("--source-url", default=SOURCE_PARQUET_URL,
                        help="Parquet URL to stream images from")
    parser.add_argument("--output-dir", type=Path, default=None,
                        help="Optional: also write the processed PNGs here")
    parser.add_argument("--cache-dir", type=Path, default=Path(tempfile.gettempdir()) / "rvl_cdip_slice",
                        help="Directory for the temporary source parquet (default: tempdir)")
    args = parser.parse_args()

    (api_key,) = require_env("BRAINTRUST_API_KEY")
    target_size = (args.target_size[0], args.target_size[1])

    cache_dir = args.cache_dir
    cache_dir.mkdir(parents=True, exist_ok=True)
    parquet_path: Path | None = None
    try:
        parquet_path = download_parquet(args.source_url, cache_dir)
        rows = load_parquet_rows(parquet_path)
        print(f"Loaded {len(rows)} rows from source parquet")
        records = sample_rows(rows, args.images_per_class, args.seed)
    finally:
        # Do not keep the source parquet around.
        if parquet_path is not None:
            try:
                parquet_path.unlink()
                cache_dir.rmdir()
            except OSError:
                pass

    if len(records) != args.images_per_class * 16:
        print(f"Warning: expected {args.images_per_class * 16} records, got {len(records)}", file=sys.stderr)

    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        for record in records:
            png_bytes = to_png_bytes(record["image_bytes"], target_size)
            (args.output_dir / record["filename"]).write_bytes(png_bytes)
        print(f"Wrote {len(records)} PNGs to {args.output_dir}")

    print(f"\nUploading {len(records)} images to {args.project}/{args.dataset} (org {args.org})...")
    summary = upload_dataset(
        records,
        project=args.project,
        project_id=args.project_id,
        org=args.org,
        dataset_name=args.dataset,
        api_key=api_key,
        target_size=target_size,
        source_url=args.source_url,
        seed=args.seed,
    )
    print(f"\nDataset creation complete: {summary['inserted']} inserted, {summary['failed']} failed")
    print(f"Uploaded {summary['total_bytes'] / 1e6:,.1f} MB of PNG images to {args.project}/{args.dataset}")


if __name__ == "__main__":
    main()
