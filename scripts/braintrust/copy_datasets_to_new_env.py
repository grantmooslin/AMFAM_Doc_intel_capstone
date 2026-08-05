"""
Copy Braintrust image datasets from the current (source) environment into a
different Braintrust org/project (e.g. a fresh capstone account).

Source credentials come from ``braintrust.env`` / ``.env`` (the "previous"
environment). Destination credentials are passed explicitly so the script can
copy without changing the source config.

Attachments are uploaded to the destination object store WITH RETRIES and the
row is only inserted once its attachment is confirmed uploaded (the SDK's
background uploader is unreliable for bulk copies and can silently drop
objects, so we upload synchronously and pass the uploaded reference through).

Usage:
    python scripts/braintrust/copy_datasets_to_new_env.py \
      --datasets fixed_size_sampled fixed_size_sampled_320 \
      --dest-project-id 9e76bd46-... \
      --dest-project-name AMFAMv2 \
      --dest-org 4cb7718c-... \
      --dest-api-key sk-...   # or set BRAINTRUST_DEST_API_KEY in the shell
"""

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import braintrust

from src.braintrust_config import load_braintrust_config
from src.openrouter_classifier import VALID_CLASSES

API_BASE = "https://api.braintrust.dev"
MAX_UPLOAD_TRIES = 8


def load_dataset_rows(source_project: str, dataset_name: str, api_key: str) -> list[dict]:
    """Read every non-placeholder row of a dataset, downloading attachment bytes."""
    braintrust.login(api_key=api_key, force_login=True)
    dataset = braintrust.init_dataset(project=source_project, name=dataset_name)
    rows: list[dict] = []
    for i, row in enumerate(dataset):
        expected = row.get("expected")
        input_data = row.get("input") or {}
        attachment = input_data.get("image")
        metadata = input_data.get("metadata", {})

        if metadata.get("placeholder", False):
            continue
        if expected not in VALID_CLASSES or not attachment:
            continue

        filename = None
        try:
            reference = getattr(attachment, "reference", None) or {}
            filename = reference.get("filename")
        except (KeyError, AttributeError):
            pass
        if not filename:
            doc_id = input_data.get("document_id")
            filename = f"{doc_id}.png" if doc_id and doc_id != "generated" else f"document_{i + 1}.png"

        rows.append({
            "expected": expected,
            "image_bytes": bytes(attachment.data),
            "filename": filename,
            "input_metadata": dict(metadata),
            "row_metadata": dict(row.get("metadata") or {}),
        })
        if (i + 1) % 25 == 0:
            print(f"    Loaded {i + 1} rows from {source_project}/{dataset_name}")
    return rows


def upload_attachment_with_retry(image_bytes: bytes, filename: str) -> dict:
    """Upload one attachment to the logged-in (destination) org, retrying on
    transient S3 failures. Returns the attachment reference dict."""
    last_error = None
    for attempt in range(MAX_UPLOAD_TRIES):
        attachment = braintrust.Attachment(data=image_bytes, filename=filename, content_type="image/png")
        try:
            status = attachment.upload()
            if status.get("upload_status") == "error":
                last_error = RuntimeError(status.get("error_message") or "attachment upload error")
            else:
                return attachment.reference
        except Exception as e:  # noqa: BLE001 - retry transient S3/API failures
            last_error = e
        wait = 3 * (attempt + 1)
        print(f"    Upload attempt {attempt + 1}/{MAX_UPLOAD_TRIES} failed for {filename}; "
              f"retrying in {wait}s ({type(last_error).__name__})", file=sys.stderr)
        time.sleep(wait)
    raise last_error


def copy_dataset(
    source_project: str,
    dataset_name: str,
    source_key: str,
    dest_key: str,
    dest_project_id: str,
    dest_project_name: str,
    dest_org: str,
    verify: bool = True,
) -> dict:
    """Copy one dataset from the source project into the destination project."""
    print(f"Copying {source_project}/{dataset_name} ...")
    rows = load_dataset_rows(source_project, dataset_name, source_key)
    print(f"  {len(rows)} rows loaded")

    braintrust.login(api_key=dest_key, force_login=True)
    dataset = braintrust.init_dataset(
        project=dest_project_name, name=dataset_name, project_id=dest_project_id
    )

    inserted = 0
    failures: list[str] = []
    for record in rows:
        try:
            reference = upload_attachment_with_retry(record["image_bytes"], record["filename"])
            dataset.insert(
                input={
                    "image": reference,
                    "metadata": record["input_metadata"],
                },
                expected=record["expected"],
                metadata={"source": "copied_from_previous_env", **record["row_metadata"]},
            )
            inserted += 1
        except Exception as e:  # noqa: BLE001 - one bad row shouldn't abort the copy
            failures.append(f"{record['filename']}: {e}")
        if inserted % 50 == 0 and inserted:
            print(f"  Inserted {inserted}/{len(rows)} rows...")

    dataset.flush()
    dataset.close()
    print(f"  Done: {inserted} inserted, {len(failures)} failed")
    for failure in failures:
        print(f"    FAILED {failure}", file=sys.stderr)

    if verify and not failures:
        bad = verify_dataset(dest_key, dest_org, dest_project_id, dest_project_name, dataset_name)
        print(f"  Verification: {len(bad)} unreadable rows")
        for reason, fn in bad:
            print(f"    BAD {fn}: {reason}", file=sys.stderr)
        if bad:
            return {"dataset": dataset_name, "inserted": inserted, "failed": len(failures), "verify_failed": len(bad)}
    return {"dataset": dataset_name, "inserted": inserted, "failed": len(failures)}


def verify_dataset(dest_key: str, dest_org: str, dest_project_id: str, dest_project_name: str,
                   dataset_name: str) -> list[tuple[str, str]]:
    """Download every attachment in a destination dataset; return (reason, filename) for failures."""
    from src.braintrust_utils import fetch_attachment_bytes

    braintrust.login(api_key=dest_key, force_login=True)
    dataset = braintrust.init_dataset(project=dest_project_name, name=dataset_name,
                                      project_id=dest_project_id)
    bad: list[tuple[str, str]] = []
    checked = 0
    for row in dataset:
        input_data = row.get("input") or {}
        attachment = input_data.get("image")
        if attachment is None:
            bad.append(("no attachment", None))
            continue
        try:
            reference = getattr(attachment, "reference", None) or {}
            filename = reference.get("filename") or f"row_{checked}"
            data = fetch_attachment_bytes(dest_key, reference, dest_org)
            if not data:
                bad.append(("empty download", filename))
        except Exception as e:  # noqa: BLE001
            reference = getattr(attachment, "reference", None) or {}
            filename = reference.get("filename") or f"row_{checked}"
            bad.append((f"{type(e).__name__}: {e}"[:160], filename))
        checked += 1
        if checked % 100 == 0:
            print(f"  Verified {checked} rows...")
    print(f"  Verified {checked} rows total")
    return bad


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--datasets", nargs="+", required=True,
                        help="Dataset names to copy, e.g. fixed_size_sampled fixed_size_sampled_320")
    parser.add_argument("--source-project", default=None,
                        help="Source project name (default: from braintrust.env)")
    parser.add_argument("--source-api-key", default=None,
                        help="Source API key (default: BRAINTRUST_SOURCE_API_KEY env var, "
                             "then braintrust.env)")
    parser.add_argument("--dest-project-id", required=True,
                        help="Destination Braintrust project id")
    parser.add_argument("--dest-project-name", required=True,
                        help="Destination Braintrust project name")
    parser.add_argument("--dest-org", required=True,
                        help="Destination Braintrust organization id")
    parser.add_argument("--dest-api-key", default=None,
                        help="Destination API key (default: BRAINTRUST_DEST_API_KEY env var)")
    parser.add_argument("--no-verify", action="store_true",
                        help="Skip downloading every row to verify attachments")
    parser.add_argument("--delete-existing", action="store_true",
                        help="Delete an existing dataset of the same name in the destination first")
    args = parser.parse_args()

    import os

    dest_key = args.dest_api_key or os.environ.get("BRAINTRUST_DEST_API_KEY")
    if not dest_key:
        sys.exit("No destination API key: pass --dest-api-key or set BRAINTRUST_DEST_API_KEY")

    cfg = load_braintrust_config()
    source_key = args.source_api_key or os.environ.get("BRAINTRUST_SOURCE_API_KEY") or cfg.api_key
    if not source_key:
        sys.exit("No source API key found: pass --source-api-key or set BRAINTRUST_SOURCE_API_KEY")
    source_project = args.source_project or cfg.project_name

    if args.delete_existing:
        from src.braintrust_utils import delete_dataset_by_name
        for dataset_name in args.datasets:
            deleted = delete_dataset_by_name(dest_key, args.dest_project_id, dataset_name)
            print(f"Deleted existing {dataset_name} in destination: {deleted}")

    summary = []
    for dataset_name in args.datasets:
        summary.append(copy_dataset(
            source_project,
            dataset_name,
            source_key,
            dest_key,
            args.dest_project_id,
            args.dest_project_name,
            args.dest_org,
            verify=not args.no_verify,
        ))
    print("\nCopy summary:")
    for s in summary:
        print(f"  {s['dataset']}: {s['inserted']} inserted, {s['failed']} failed, "
              f"{s.get('verify_failed', 0)} unreadable")


if __name__ == "__main__":
    main()
