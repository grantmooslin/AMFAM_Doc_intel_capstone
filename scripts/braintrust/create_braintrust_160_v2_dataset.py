"""
Build a fresh balanced 160-image RVL-CDIP dataset (``fixed_size_sampled_v2``)
that is DISJOINT from the original ``fixed_size_sampled`` 160-image set.

This slice is used to test whether the classification prompt keeps its >90%
accuracy regardless of which 160-image slice is pulled from the dataset.

Composition:
    * 10 images per class x 16 classes = 160 total.
    * Fresh RVL-CDIP test images come from the public Hugging Face parquet
      mirror ``jordyvl/rvl_cdip_100_examples_per_class``, sampled
      deterministically with seed 1738.
    * Fresh images are converted to 1024x1024 grayscale PNGs (aspect-ratio
      preserving, white padding, 300 DPI metadata) and are de-duplicated
      against the original 160 images by raw pixel hash, so no image in the
      original ``fixed_size_sampled`` appears here.
    * The dataset is deleted and recreated so it is safe to rerun.

Prerequisites:
    pip install braintrust pyarrow Pillow requests
    Set BRAINTRUST_API_KEY (reads ``braintrust.env`` via ``src.braintrust_config``).

Usage:
    python scripts/braintrust/create_braintrust_160_v2_dataset.py
    python scripts/braintrust/create_braintrust_160_v2_dataset.py --output-dir fixed_size_sampled_v2
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import io
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
from src.braintrust_utils import load_braintrust_dataset
from src.braintrust_utils import delete_dataset_by_name
from src.env_utils import require_env
from src.image_utils import resize_with_padding

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_CONFIG = load_braintrust_config()
DEFAULT_ORG = _CONFIG.org_id
DEFAULT_PROJECT = _CONFIG.project_name
DEFAULT_PROJECT_ID = _CONFIG.project_id
DEFAULT_DATASET = "fixed_size_sampled_v2"
SOURCE_DATASET = "fixed_size_sampled"
TARGET_PER_CLASS = 10
DEFAULT_TARGET_SIZE = (1024, 1024)
DEFAULT_SEED = 1738

# Public HF parquet mirror of RVL-CDIP with 100 examples per class.
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
    """Stream the source parquet into a temp file (not the full dataset)."""
    dest = cache_dir / "rvl_cdip_source.parquet"
    if dest.exists() and dest.stat().st_size > 0:
        print(f"Using cached source parquet: {dest}")
        return dest

    print(f"Downloading source parquet ({url})...")
    with requests.get(url, stream=True, timeout=600) as response:
        response.raise_for_status()
        total = int(response.headers.get("Content-Length", 0))
        written = 0
        with open(dest, "wb") as f:
            for chunk in response.iter_content(chunk_size=1 << 20):
                f.write(chunk)
                written += len(chunk)
                if total:
                    pct = written / total * 100
                    print(f"\r  {written / 1e6:,.1f} / {total / 1e6:,.1f} MB ({pct:.0f}%)", end="", flush=True)
        print()
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


def to_png_bytes(tiff_bytes: bytes, target_size: tuple[int, int]) -> bytes:
    """Convert a TIFF blob to a fixed-size padded grayscale PNG (300 DPI metadata)."""
    with Image.open(io.BytesIO(tiff_bytes)) as img:
        if img.mode != "L":
            img = img.convert("L")
        padded = resize_with_padding(img, target_size, fill=255)
        buffer = io.BytesIO()
        padded.save(buffer, format="PNG", dpi=(300, 300))
        return buffer.getvalue()


def pixel_hash(png_bytes: bytes) -> str:
    """md5 of raw grayscale pixels; identical source images hash the same."""
    with Image.open(io.BytesIO(png_bytes)) as img:
        if img.mode != "L":
            img = img.convert("L")
        return hashlib.md5(img.tobytes()).hexdigest()


# ---------------------------------------------------------------------------
# Fresh image sampling (deterministic, de-duplicated against the originals)
# ---------------------------------------------------------------------------

def sample_fresh_rows(
    rows: list[dict],
    originals: list[dict],
    seed: int,
    target_size: tuple[int, int],
    extra_exclusions: list[dict] | None = None,
    target_per_class: int = TARGET_PER_CLASS,
) -> list[dict]:
    """Sample 10 fresh images per class so the new slice is disjoint from the 160.

    ``originals`` already have ``png_bytes`` set. Fresh candidates that are
    pixel-identical to an original (or an ``extra_exclusions`` record, or an
    earlier accepted fresh image) are skipped. Returns records shaped like
    ``{label, png_bytes, filename, source_index, row_index}``.
    """
    by_class: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_class[row["label"]].append(row)

    existing = Counter(r["label"] for r in originals)
    used_hashes = {pixel_hash(r["png_bytes"]) for r in originals}
    for record in extra_exclusions or []:
        used_hashes.add(pixel_hash(record["png_bytes"]))

    rng = random.Random(seed)
    fresh: list[dict] = []
    skipped = 0
    for class_name in sorted(by_class):
        needed = target_per_class
        candidates = list(by_class[class_name])
        rng.shuffle(candidates)
        accepted = 0
        for row in candidates:
            if accepted >= needed:
                break
            png_bytes = to_png_bytes(row["image_bytes"], target_size)
            h = pixel_hash(png_bytes)
            if h in used_hashes:
                skipped += 1
                continue
            used_hashes.add(h)
            fresh.append({
                "label": class_name,
                "png_bytes": png_bytes,
                "filename": f"rvl_cdip__{class_name}__{accepted + 1:04d}.png",
                "source_index": row["row_index"],
                "row_index": row["row_index"],
            })
            accepted += 1
        if accepted < needed:
            raise RuntimeError(
                f"{class_name}: only {accepted} fresh images found, need {needed}"
            )

    print(f"Sampled {len(fresh)} fresh images; skipped {skipped} pixel duplicates")
    for class_name in sorted(by_class):
        print(f"  {class_name:<24} 0 + {sum(1 for r in fresh if r['label'] == class_name)} = {TARGET_PER_CLASS} (disjoint from existing {existing.get(class_name, 0)})")
    return fresh


# ---------------------------------------------------------------------------
# Upload
# ---------------------------------------------------------------------------

def upload_dataset(
    fresh: list[dict],
    project: str,
    project_id: str,
    org: str,
    dataset_name: str,
    api_key: str,
    source_url: str,
    seed: int,
    output_dir: Path | None,
) -> dict:
    """Insert the fresh rows into a Braintrust dataset (deleted first)."""
    braintrust.login(api_key=api_key)
    dataset = braintrust.init_dataset(project_id=project_id, name=dataset_name)

    experiment = braintrust.init_experiment(
        project_id=project_id,
        experiment=f"create-{dataset_name}",
        description=f"Build {len(fresh)}-image RVL-CDIP slice (10/class x 16, disjoint from fixed_size_sampled) "
                    f"and store as Braintrust dataset '{dataset_name}'",
        metadata={
            "task": "dataset_creation",
            "project": project,
            "org": org,
            "dataset": dataset_name,
            "source_url": source_url,
            "target_size": list(DEFAULT_TARGET_SIZE),
            "seed": seed,
            "images": len(fresh),
        },
    )

    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=True)
        for record in fresh:
            (output_dir / record["filename"]).write_bytes(record["png_bytes"])
        print(f"Wrote {len(fresh)} PNGs to {output_dir}")

    inserted = 0
    failed = 0
    per_class = Counter()
    total_bytes = 0
    failures: list[str] = []

    for i, record in enumerate(fresh):
        class_name = record["label"]
        filename = record["filename"]
        try:
            input_data = {
                "image": braintrust.Attachment(
                    data=record["png_bytes"],
                    filename=filename,
                    content_type="image/png",
                ),
                "document_id": f"rvl_cdip_{record['source_index']}",
                "metadata": {
                    "class": class_name,
                    "placeholder": False,
                    "source_file": filename,
                    "subset": "fresh_160_v2",
                },
            }
            dataset.insert(
                input=input_data,
                expected=class_name,
                metadata={
                    "source": "rvl_cdip_hf_parquet",
                    "slice": f"{len(fresh)}_images",
                    "split": "test",
                    "seed": seed,
                },
            )
            inserted += 1
            per_class[class_name] += 1
            total_bytes += len(record["png_bytes"])
        except Exception as e:  # noqa: BLE001 - one bad row shouldn't abort the build
            failed += 1
            failures.append(f"{filename}: {e}")

        if (i + 1) % 50 == 0:
            print(f"  Inserted {i + 1}/{len(fresh)} records...")

    dataset.flush()
    dataset.close()

    n = max(1, len(fresh))
    experiment.log(
        input={"dataset": dataset_name, "records": len(fresh)},
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
                        help=f"Braintrust project id (default: {DEFAULT_PROJECT_ID})")
    parser.add_argument("--org", default=DEFAULT_ORG,
                        help=f"Braintrust org id (default: {DEFAULT_ORG})")
    parser.add_argument("--dataset", default=DEFAULT_DATASET,
                        help=f"Braintrust dataset name (default: {DEFAULT_DATASET})")
    parser.add_argument("--source-dataset", default=SOURCE_DATASET,
                        help=f"Existing dataset whose images must not overlap (default: {SOURCE_DATASET})")
    parser.add_argument("--exclude-dataset", default="fixed_size_sampled_480",
                        help="Additional dataset whose images must also be excluded (default: fixed_size_sampled_480)")
    parser.add_argument("--target-per-class", type=int, default=TARGET_PER_CLASS,
                        help=f"Target images per class (default: {TARGET_PER_CLASS})")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED,
                        help=f"Random seed for fresh sampling (default: {DEFAULT_SEED})")
    parser.add_argument("--target-size", type=int, nargs=2, default=list(DEFAULT_TARGET_SIZE),
                        metavar=("W", "H"),
                        help=f"Output image size W H (default: {DEFAULT_TARGET_SIZE[0]} {DEFAULT_TARGET_SIZE[1]})")
    parser.add_argument("--source-url", default=SOURCE_PARQUET_URL,
                        help="Parquet URL to stream fresh images from")
    parser.add_argument("--output-dir", type=Path, default=None,
                        help="Optional: also write all 160 PNGs here")
    args = parser.parse_args()

    (api_key,) = require_env("BRAINTRUST_API_KEY")
    target_size = (args.target_size[0], args.target_size[1])

    print(f"Loading original 160 from {args.project}/{args.source_dataset} (org {args.org})...")
    originals = load_braintrust_dataset(
        args.project, args.source_dataset, dataset_api_key=api_key, org_id=args.org
    )
    for record in originals:
        record["png_bytes"] = base64.b64decode(record["image_b64"])
        record["label"] = record["expected"]
        del record["image_b64"]
    print(f"Loaded {len(originals)} originals")
    for class_name, count in sorted(Counter(r["label"] for r in originals).items()):
        print(f"  {class_name:<24} {count}")

    print(f"Loading exclusion set from {args.project}/{args.exclude_dataset} (org {args.org})...")
    exclusions = load_braintrust_dataset(
        args.project, args.exclude_dataset, dataset_api_key=api_key, org_id=args.org
    )
    for record in exclusions:
        record["png_bytes"] = base64.b64decode(record["image_b64"])
    print(f"Loaded {len(exclusions)} exclusion images")

    cache_dir = Path(tempfile.gettempdir()) / "rvl_cdip_slice_v2"
    cache_dir.mkdir(parents=True, exist_ok=True)
    try:
        parquet_path = download_parquet(args.source_url, cache_dir)
        rows = load_parquet_rows(parquet_path)
        print(f"Loaded {len(rows)} rows from source parquet")
        fresh = sample_fresh_rows(
            rows,
            originals,
            args.seed,
            target_size,
            extra_exclusions=exclusions,
            target_per_class=args.target_per_class,
        )
    finally:
        # Do not keep the source parquet around.
        try:
            parquet_path.unlink()
            cache_dir.rmdir()
        except OSError:
            pass

    expected = args.target_per_class * 16
    total = len(fresh)
    if total != expected:
        print(f"Warning: expected {expected} total images, got {total}", file=sys.stderr)

    deleted = delete_dataset_by_name(api_key, args.project_id, args.dataset)
    if deleted:
        print(f"Deleted existing dataset {args.dataset} ({deleted})")
    print(f"\nUploading {total} images to {args.project}/{args.dataset} (org {args.org})...")
    summary = upload_dataset(
        fresh,
        project=args.project,
        project_id=args.project_id,
        org=args.org,
        dataset_name=args.dataset,
        api_key=api_key,
        source_url=args.source_url,
        seed=args.seed,
        output_dir=args.output_dir,
    )
    print(f"\nDataset creation complete: {summary['inserted']} inserted, {summary['failed']} failed")
    print(f"Uploaded {summary['total_bytes'] / 1e6:,.1f} MB of PNG images to {args.project}/{args.dataset}")


if __name__ == "__main__":
    main()
