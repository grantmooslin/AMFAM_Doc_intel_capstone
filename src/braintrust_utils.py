"""Shared Braintrust HTTP, attachment, and experiment helpers.

Used by the eval runner (``scripts/braintrust_openrouter_input.py``), the
report generator (``scripts/braintrust_report.py``), and the smoke-test
dataset builder (``scripts/braintrust/create_misclassification_smoke_dataset.py``) so the
Braintrust wire protocol (experiment fetch, attachment downloads, dataset
loading) lives in one place.
"""

import base64
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import requests

from src.constants import DOCUMENT_CLASSES

VALID_CLASSES = DOCUMENT_CLASSES
DEFAULT_ATTACHMENT_WORKERS = 8
EXPERIMENT_FETCH_RETRIES = 6


# ---------------------------------------------------------------------------
# Experiment + dataset HTTP helpers
# ---------------------------------------------------------------------------

def _v1_api_base(api_base: str) -> str:
    """Ensure an api_base points at the REST endpoints under ``/v1``.

    Configs use ``https://api.braintrust.dev`` (no suffix), while the
    experiment/dataset REST endpoints live under ``https://api.braintrust.dev/v1``.
    """
    api_base = api_base.rstrip("/")
    return f"{api_base}/v1" if not api_base.endswith("/v1") else api_base


def list_experiments(api_key: str, project_id: str, api_base: str = "https://api.braintrust.dev/v1") -> list[dict]:
    """Return metadata for every experiment in a project."""
    resp = requests.get(
        f"{_v1_api_base(api_base)}/experiment",
        headers={"Authorization": f"Bearer {api_key}"},
        params={"project_id": project_id, "limit": 200},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json().get("objects", [])


def list_datasets(api_key: str, project_id: str, api_base: str = "https://api.braintrust.dev/v1") -> list[dict]:
    """Return metadata for every dataset in a project."""
    resp = requests.get(
        f"{_v1_api_base(api_base)}/dataset",
        headers={"Authorization": f"Bearer {api_key}"},
        params={"project_id": project_id, "limit": 200},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json().get("objects", [])


def delete_dataset_by_name(
    api_key: str,
    project_id: str,
    name: str,
    api_base: str = "https://api.braintrust.dev/v1",
) -> str | None:
    """Delete a dataset by name if it exists; return its id or None."""
    headers = {"Authorization": f"Bearer {api_key}"}
    for dataset in list_datasets(api_key, project_id, api_base):
        if dataset.get("name") == name:
            dataset_id = dataset["id"]
            resp = requests.delete(f"{_v1_api_base(api_base)}/dataset/{dataset_id}", headers=headers, timeout=60)
            resp.raise_for_status()
            return dataset_id
    return None


def fetch_experiment_rows(
    api_key: str,
    experiment_id: str,
    api_base: str = "https://api.braintrust.dev/v1",
    max_retries: int = EXPERIMENT_FETCH_RETRIES,
    timeout: int = 300,
) -> list[dict]:
    """Fetch every event (span) of an experiment, retrying on rate limits."""
    headers = {"Authorization": f"Bearer {api_key}"}
    rows: list[dict] = []
    cursor = None
    while True:
        body = {"limit": 100}
        if cursor:
            body["cursor"] = cursor
        for attempt in range(max_retries):
            try:
                resp = requests.post(
                    f"{_v1_api_base(api_base)}/experiment/{experiment_id}/fetch",
                    headers=headers,
                    json=body,
                    timeout=timeout,
                )
                resp.raise_for_status()
                break
            except requests.exceptions.HTTPError as e:
                if resp.status_code == 429 and attempt < max_retries - 1:
                    wait = min(30, 10 * (2 ** attempt))
                    print(f"  Rate limited, waiting {wait}s (retry {attempt + 1}/{max_retries})")
                    time.sleep(wait)
                elif attempt < max_retries - 1:
                    wait = 5 * (attempt + 1)
                    print(f"  Retry {attempt + 1}/{max_retries} after {wait}s ({e})")
                    time.sleep(wait)
                else:
                    raise
            except requests.exceptions.Timeout as e:
                if attempt < max_retries - 1:
                    wait = 10 * (attempt + 1)
                    print(f"  Timeout, retry {attempt + 1}/{max_retries} after {wait}s")
                    time.sleep(wait)
                else:
                    raise
        data = resp.json()
        batch = data.get("events", [])
        rows.extend(batch)
        cursor = data.get("cursor")
        if not cursor or not batch:
            break
    return rows


def resolve_prompt_version(experiment_meta: dict) -> str:
    """Return the prompt version (e.g. ``v8.5``) for an experiment.

    Prefers the experiment's ``metadata.prompt_version``, then parses the
    version out of the experiment name (``qwen3.7-flash_v8.5_reasoning``).
    """
    metadata = experiment_meta.get("metadata") or {}
    version = metadata.get("prompt_version")
    if version:
        return str(version)
    match = re.search(r"_v(\d+(?:\.\d+)?)_", experiment_meta.get("name") or "")
    return f"v{match.group(1)}" if match else "unknown"


# ---------------------------------------------------------------------------
# Misclassification analysis
# ---------------------------------------------------------------------------

def index_span_metadata(rows: list[dict]) -> dict[str, dict]:
    """Index span-level metadata (reasoning, filename) by root_span_id."""
    span_meta: dict[str, dict] = {}
    for row in rows:
        root = row.get("root_span_id") or row.get("span_id") or ""
        metadata = row.get("metadata") or {}
        if metadata.get("reasoning") or metadata.get("filename"):
            span_meta.setdefault(root, {}).update(metadata)
    return span_meta


def find_misses(rows: list[dict], span_meta: dict[str, dict] | None = None) -> list[dict]:
    """Return every scored-but-wrong task row.

    Each result dict has ``expected``, ``predicted``, ``filename``, ``reasoning``,
    and ``metrics``. Rows without a valid ``expected``/``output`` are skipped.
    """
    if span_meta is None:
        span_meta = index_span_metadata(rows)

    misses: list[dict] = []
    for row in rows:
        expected = row.get("expected")
        output = row.get("output")
        if expected not in VALID_CLASSES or not output:
            continue
        predicted = str(output).strip().lower()
        if predicted == expected:
            continue

        root = row.get("root_span_id") or ""
        meta = dict(row.get("metadata") or {})
        meta.update(span_meta.get(root, {}))
        input_data = row.get("input") or {}
        misses.append({
            "expected": expected,
            "predicted": predicted,
            "filename": str(meta.get("filename") or "") or str(input_data.get("filename") or ""),
            "reasoning": str(meta.get("reasoning") or ""),
            "metrics": dict(row.get("metrics") or {}),
        })
    return misses


# ---------------------------------------------------------------------------
# Attachment / dataset loading
# ---------------------------------------------------------------------------

def fetch_attachment_bytes(
    api_key: str,
    reference: dict,
    org_id: str,
    api_base: str = "https://api.braintrust.dev",
) -> bytes:
    """Download an already-uploaded Braintrust attachment's bytes directly."""
    params = {
        "filename": reference["filename"],
        "content_type": reference["content_type"],
        "org_id": org_id,
    }
    if reference["type"] == "braintrust_attachment":
        params["key"] = reference["key"]
    elif reference["type"] == "external_attachment":
        params["url"] = reference["url"]
    else:
        raise RuntimeError(f"Unknown attachment type: {reference['type']}")

    resp = requests.get(
        f"{api_base}/attachment",
        params=params,
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=60,
    )
    resp.raise_for_status()
    download_url = resp.json()["downloadUrl"]

    data = requests.get(download_url, timeout=120)
    data.raise_for_status()
    return data.content


def load_braintrust_dataset(
    project: str,
    dataset_name: str,
    dataset_api_key: str | None = None,
    org_id: str = "",
    api_base: str = "https://api.braintrust.dev",
) -> list[dict]:
    """Load a Braintrust dataset's images as base64 records.

    Returns ``[{image_b64, filename, expected}]``. Rows without a stored
    attachment (placeholder rows) or an invalid label are skipped. Attachments
    are downloaded in parallel.
    """
    import braintrust

    api_key = dataset_api_key or os.environ.get("BRAINTRUST_API_KEY")
    if api_key:
        force = dataset_api_key is not None
        braintrust.login(api_key=api_key, force_login=force)

    dataset = braintrust.init_dataset(project=project, name=dataset_name)
    pending = []
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
            if doc_id and doc_id != "generated":
                filename = f"{doc_id}.png"
            else:
                filename = f"document_{i + 1}.png"

        pending.append((expected, attachment, filename))

    records: list[dict] = []
    failures = []

    def grab(item):
        _, attachment, _ = item
        try:
            return fetch_attachment_bytes(api_key, attachment.reference, org_id, api_base), None
        except Exception as e:  # noqa: BLE001 - one bad row shouldn't abort the eval
            return None, str(e)

    with ThreadPoolExecutor(max_workers=DEFAULT_ATTACHMENT_WORKERS) as pool:
        for (expected, _, filename), (image_bytes, error) in zip(pending, pool.map(grab, pending)):
            if error is not None:
                failures.append((expected, filename, error))
                continue
            records.append({
                "image_b64": base64.b64encode(image_bytes).decode("utf-8"),
                "filename": filename,
                "expected": expected,
            })

    for expected, filename, error in failures:
        print(f"SKIP {expected:<24} {filename}: {error}", file=sys.stderr)
    if failures:
        print(f"WARNING: skipped {len(failures)} rows with unreadable attachments", file=sys.stderr)

    return records
