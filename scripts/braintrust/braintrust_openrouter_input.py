"""
Braintrust Prompt Evaluation for Document Classification

Runs the classification prompt against the sampled dataset (16 classes) and logs
results to Braintrust for prompt iteration in their UI. Images are pulled from a
Braintrust dataset by default; a local directory of PNGs can be used instead.

Prerequisites:
    pip install braintrust openai
    Set BRAINTRUST_API_KEY and OPENROUTER_API_KEY in your .env file.

Usage:
    python scripts/braintrust/braintrust_openrouter_input.py
    python scripts/braintrust/braintrust_openrouter_input.py --dataset fixed_size_sampled
    python scripts/braintrust/braintrust_openrouter_input.py --images-dir path/to/images
    python scripts/braintrust/braintrust_openrouter_input.py --prompt-version v4 --model qwen/qwen3.7-flash
    python scripts/braintrust/braintrust_openrouter_input.py --experiment-name qwen3.7-flash_v4_reasoning
"""

from __future__ import annotations

import argparse
import os
import random
import re
import sys
import threading
import time
from collections import Counter, defaultdict, deque
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import braintrust
from openai import OpenAI

from src.braintrust_config import load_braintrust_config
from src.braintrust_utils import load_braintrust_dataset
from src.env_utils import require_env
from src.evaluation import ManifestStore, dataset_fingerprint, validate_dataset
from src.image_utils import encode_image_base64
from src.notify import play_failure, play_success
from src.openrouter_classifier import VALID_CLASSES, clean_prediction, extract_runner_up
from src.openrouter_utils import OPENROUTER_BASE_URL, build_vision_messages
from src.prompts import get_prompt, DEFAULT_PROMPT_VERSION

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEFAULT_MAX_TOKENS = 4096  # Enough for reasoning trace + scratchpad + final label
MAX_TRIES = 3  # Retry transient provider failures (502s, token caps, empty responses)
ERROR_PREFIX = "ERROR: "  # Task output sentinel so failed rows get tracked scores
MAX_TOKENS_CAP = 32768  # Upper bound when growing max_tokens on "length" finish reasons (v17 fix: 16→32K)

# Resilience tuning (429 key failover / upstream rate limits / content filters).
RATE_LIMIT_BACKOFF = (5, 15, 45)  # Seconds between retries on 429 (upstream shared-pool throttling)
TRANSIENT_BACKOFF = (2, 4)  # Seconds between retries on transient/network errors
QUOTA_HINTS = ("limit", "quota", "balance", "credit")
CONTENT_FILTER_HINTS = ("inappropriate content", "data_inspection_failed", "content filter")


def _backoff_for(schedule: tuple[int, ...], attempt: int) -> float:
    """Return the backoff delay for ``attempt`` using the given schedule."""
    return float(schedule[min(attempt, len(schedule) - 1)])


def _response_status_code(exc: Exception) -> int | None:
    response = getattr(exc, "response", None)
    if response is not None:
        status = getattr(response, "status_code", None)
        if isinstance(status, int):
            return status
    return None


def _is_rate_limit(exc: Exception) -> bool:
    """429 or an upstream "rate limit" message (OpenRouter/Alibaba shared pool)."""
    msg = str(exc).lower()
    return _response_status_code(exc) == 429 or "rate limit" in msg or "rate-limited" in msg


def _is_quota_error(exc: Exception) -> bool:
    """403/401 key or credit limits (e.g. weekly key limit exceeded)."""
    code = _response_status_code(exc)
    if code not in (401, 403) and "Error code: 403" not in str(exc):
        return False
    return any(hint in str(exc).lower() for hint in QUOTA_HINTS)


def _is_content_filter(exc: Exception) -> bool:
    """Provider-side safety moderation rejecting the input image."""
    msg = str(exc).lower()
    return any(hint in msg for hint in CONTENT_FILTER_HINTS)


def _retry_after_seconds(exc: Exception) -> float | None:
    """Honor a Retry-After header from the provider, if present."""
    response = getattr(exc, "response", None)
    if response is not None:
        headers = getattr(response, "headers", None) or {}
        retry_after = headers.get("retry-after")
        if retry_after:
            try:
                return float(retry_after)
            except (TypeError, ValueError):
                pass
    return None


def _build_openai_client(api_key: str) -> "OpenAI":
    """Create the OpenRouter-backed OpenAI client with Braintrust logging."""
    return braintrust.wrap_openai(
        OpenAI(base_url=OPENROUTER_BASE_URL, api_key=api_key, timeout=300)
    )


def _candidate_keys(primary: str) -> list[str]:
    """Return the OpenRouter keys to try: the configured key first, then the
    alternate research-funding key (if set and different) for failover."""
    keys = [primary]
    alternate = os.environ.get("RESEARCH_FUNDING_API_KEY")
    if alternate and alternate not in keys:
        keys.append(alternate)
    return keys


class AdaptiveThrottle:
    """Reduce request rate after a burst of upstream 429s.

    OpenRouter's shared provider pool throttles qwen models when an eval runs at
    8-way concurrency. After two 429s inside a short window, subsequent requests
    pause for a growing cooldown so the shared pool recovers.
    """

    def __init__(self, window_seconds: float = 30.0, min_cooldown: float = 2.0,
                 max_cooldown: float = 30.0) -> None:
        self.window = window_seconds
        self.min_cooldown = min_cooldown
        self.max_cooldown = max_cooldown
        self._recent_429: deque[float] = deque()
        self._lock = threading.Lock()

    def record_429(self) -> None:
        with self._lock:
            self._recent_429.append(time.monotonic())
            self._trim()

    def _trim(self) -> None:
        cutoff = time.monotonic() - self.window
        while self._recent_429 and self._recent_429[0] < cutoff:
            self._recent_429.popleft()

    def wait_if_throttled(self) -> None:
        with self._lock:
            self._trim()
            n = len(self._recent_429)
            if n < 2:
                return
            cooldown = min(self.max_cooldown, self.min_cooldown * (2 ** (n - 1)))
        time.sleep(cooldown)


def _build_extra_body(model: str, effort: str | None) -> dict:
    """Build the request extra body based on model capabilities."""
    extra_body: dict = {}
    if "kimi" in model.lower():
        extra_body = {"reasoning": {"enabled": True, "effort": effort or "xhigh"}}
    elif "gemini" in model.lower():
        extra_body = {"reasoning": {"effort": effort or "max"}, "include_reasoning": True}
    elif "qwen" in model.lower():
        extra_body = {
            "reasoning": {"enabled": True, "effort": effort or "high"},
            "include_reasoning": True,
        }
    return extra_body


def _extract_reasoning(message) -> str:
    if hasattr(message, "reasoning_content") and message.reasoning_content:
        return message.reasoning_content
    if hasattr(message, "reasoning") and message.reasoning:
        return message.reasoning
    return ""


def _safe_span_log(**kwargs) -> None:
    """Log Braintrust span metadata without letting an outage fail the row.

    A Braintrust API hiccup must never turn a successful classification into a
    failed row; the manifest is the durable record, not the span log.
    """
    try:
        braintrust.current_span().log(**kwargs)
    except Exception as exc:  # noqa: BLE001 - logging must not raise
        print(f"WARNING: could not log span metadata to Braintrust: {exc}", file=sys.stderr)

_CONFIG = load_braintrust_config()
PROJECT_NAME = _CONFIG.project_name
PROJECT_ID = _CONFIG.project_id
ORG_ID = _CONFIG.org_id
BRAINTRUST_API_BASE = _CONFIG.api_base.rstrip("/")
DEFAULT_DATASET_PROJECT = _CONFIG.dataset_project
DEFAULT_DATASET = _CONFIG.dataset
DEFAULT_MODEL = _CONFIG.model


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def quiet_reporter() -> braintrust.Reporter:
    """Reporter that suppresses Braintrust's score summary so stdout carries only
    the classification results. Task errors are still surfaced on stderr."""
    def report_eval(evaluator, result, verbose, jsonl) -> bool:
        failures = [r for r in result.results if r.error]
        for failure in failures:
            print(f"ERROR {failure.input['filename']}: {failure.error}", file=sys.stderr)
        return not failures

    def report_run(results, verbose, jsonl) -> bool:
        return all(results)

    return braintrust.Reporter(
        "classification-only",
        report_eval=report_eval,
        report_run=report_run,
    )


def get_api_keys() -> tuple[str, str]:
    """Load required API keys from environment."""
    return require_env("OPENROUTER_API_KEY", "BRAINTRUST_API_KEY")


def extract_class_from_filename(filename: str) -> str:
    """
    Extract the ground-truth class from the fixed-size dataset filename.
    Format: processed_balanced__{class}__{original_name}.png
    """
    parts = filename.split("__")
    if len(parts) >= 2:
        return parts[1]
    return "unknown"


def sample_balanced(dataset: list[dict], samples_per_class: int, seed: int = 42) -> list[dict]:
    """Deterministically subsample ``samples_per_class`` rows per class.

    Returns a class-balanced subset of the dataset (each class contributes the
    same number of rows). Preserves unique filenames so ``validate_dataset``
    still passes.
    """
    by_class: dict[str, list[dict]] = defaultdict(list)
    for row in dataset:
        by_class[row["expected"]].append(row)

    rng = random.Random(seed)
    sampled: list[dict] = []
    for cls in sorted(by_class):
        available = by_class[cls]
        n = min(samples_per_class, len(available))
        sampled.extend(rng.sample(available, n))
    rng.shuffle(sampled)
    return sampled


def load_dataset_images(dataset_dir: Path) -> list[dict]:
    """
    Load all images from a local fixed-size dataset directory.
    Returns list of records with base64 image contents and expected class.
    """
    dataset = []
    for img_path in sorted(dataset_dir.glob("*.png")):
        expected_class = extract_class_from_filename(img_path.name)
        if expected_class in VALID_CLASSES:
            dataset.append({
                "image_b64": encode_image_base64(img_path),
                "filename": img_path.name,
                "expected": expected_class,
            })
    return dataset


def extract_prediction(text: str) -> str:
    """Prefer the ``<label>...</label>`` output tag (V4 format), then fall back
    to scanning the raw output for any valid class name."""
    if not text:
        return ""
    match = re.search(r"<label>\s*([^<\s][^<]*?)\s*</label>", text, flags=re.IGNORECASE | re.DOTALL)
    if match:
        candidate = match.group(1).strip().lower()
        if candidate in VALID_CLASSES:
            return candidate
    return clean_prediction(text)


def near_miss_score(output: str, expected: str, runner_up: str) -> float:
    """Score 1.0 if the model's prediction was wrong AND its runner-up label
    (second choice) was the correct answer — a near miss. Else 0.0."""
    if output == expected:
        return 0.0
    return 1.0 if runner_up == expected else 0.0


def _response_cost(response) -> float:
    """Actual billed USD cost for a completion, from OpenRouter's usage.cost.

    Falls back to the standard OpenAI Usage fields when ``cost`` is absent.
    """
    usage = getattr(response, "usage", None)
    if usage is None:
        return 0.0
    cost = getattr(usage, "cost", None)
    if cost is None and hasattr(usage, "model_extra"):
        cost = (usage.model_extra or {}).get("cost")
    try:
        return float(cost or 0.0)
    except (TypeError, ValueError):
        return 0.0


# ---------------------------------------------------------------------------
# Braintrust Eval
# ---------------------------------------------------------------------------

def run_eval(
    dataset: list[dict],
    model: str = DEFAULT_MODEL,
    prompt_version: str = DEFAULT_PROMPT_VERSION,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    temperature: float = 0.1,
    reasoning_effort: str | None = None,
    project_id: str = PROJECT_ID,
    experiment_name: str = None,
    dataset_name: str = DEFAULT_DATASET,
    manifest_path: str | Path | None = None,
    max_concurrency: int = 8,
    sound: bool = True,
    fallback_model: str | None = None,
) -> None:
    """Run the classification prompt against the dataset and log to Braintrust."""
    validate_dataset(dataset)
    if max_tokens <= 0:
        raise ValueError("max_tokens must be positive")
    openrouter_key = os.environ.get("OPENROUTER_API_KEY")
    braintrust_key = os.environ.get("BRAINTRUST_API_KEY")
    
    # Initialize braintrust with proper login and project using eval API key
    braintrust.login(api_key=braintrust_key)
    
    # Get the appropriate prompt version
    classification_prompt = get_prompt(prompt_version)

    if experiment_name is None:
        experiment_name = f"{model.split('/')[-1]}_p{prompt_version}"

    # Effective reasoning effort used when --reasoning-effort is not passed.
    # qwen3.x runs at "high" (not max) to avoid burning tokens; kimi and
    # gemini default to their families' maximum effort.
    if reasoning_effort:
        resolved_effort = reasoning_effort
    elif "kimi" in model.lower():
        resolved_effort = "xhigh"
    elif "gemini" in model.lower():
        resolved_effort = "max"
    elif "qwen" in model.lower():
        resolved_effort = "high"
    else:
        resolved_effort = "high"

    manifest = None
    if manifest_path:
        manifest = ManifestStore(
            manifest_path,
            {
                "experiment_name": experiment_name,
                "dataset": dataset_name,
                "dataset_size": len(dataset),
                "dataset_fingerprint": dataset_fingerprint(dataset),
                "model": model,
                "prompt_version": prompt_version,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "reasoning_effort": reasoning_effort,
            },
        )
        manifest.initialize()

    # Wrap OpenAI client pointed at OpenRouter with Braintrust logging. The
    # client lives in a mutable box so a key-quota 403 can fail over to the
    # alternate key without rebuilding the eval. Timeout prevents a stalled
    # provider connection from hanging the run forever.
    keys = _candidate_keys(openrouter_key)
    client_box: dict = {"client": _build_openai_client(keys[0])}
    throttle = AdaptiveThrottle()
    fallback_client_box: dict | None = None
    if fallback_model:
        fallback_client_box = {"client": _build_openai_client(keys[0])}

    images_by_index = {i: d["image_b64"] for i, d in enumerate(dataset)}
    expected_by_index = {i: d["expected"] for i, d in enumerate(dataset)}

    # Per-row actual cost: {index: billed USD from OpenRouter's usage.cost}.
    # Written by classify_document after the successful completion; read by the
    # cost Braintrust scorer. Single writer per key; the eval awaits each task
    # before running its scorers, so reads always see the completed write.
    cost_by_index: dict[int, float] = {}

    @braintrust.traced
    def classify_document(input_data: dict) -> str:
        """Classify a single document image via the vision model."""
        image_b64 = images_by_index[input_data["index"]]
        filename = input_data["filename"]
        expected = expected_by_index[input_data["index"]]

        if manifest:
            cached = manifest.get_completed(filename)
            if cached:
                braintrust.current_span().log(
                    metadata={"cached": True, "filename": filename, "prompt_version": prompt_version}
                )
                return cached["predicted"]

        extra_body = _build_extra_body(model, reasoning_effort)

        # Retry with per-error backoff; grow max_tokens on capouts; fail over to
        # the alternate OpenRouter key on quota 403s; throttle on upstream 429s.
        # Bounded by MAX_TRIES attempts per configured key.
        tokens = max_tokens
        last_error = None
        attempts = 0
        raw = ""
        finish_reason = None
        reasoning_text = ""
        predicted = ""
        key_switched = False
        for attempt in range(1, MAX_TRIES * max(1, len(keys)) + 1):
            attempts = attempt
            throttle.wait_if_throttled()
            try:
                response = client_box["client"].chat.completions.create(
                    model=model,
                    messages=build_vision_messages(classification_prompt, image_b64),
                    max_tokens=tokens,
                    temperature=temperature,
                    extra_body=extra_body,
                )
                raw = response.choices[0].message.content or ""
                finish_reason = response.choices[0].finish_reason
                reasoning_text = _extract_reasoning(response.choices[0].message)

                # Try to extract a prediction from whatever text the model
                # returned. Truncated (finish_reason=length) and provider-errored
                # responses often still contain a valid classification label.
                # Salvaging these rescues ~10 % of samples that would otherwise
                # be counted as evaluation failures.
                predicted = extract_prediction(raw)
                if predicted:
                    break

                if raw.strip() == "" or finish_reason == "error":
                    raise RuntimeError(
                        f"model returned no usable content (finish_reason={finish_reason})"
                    )
                if finish_reason == "length":
                    old_tokens = tokens
                    tokens = min(tokens * 2, MAX_TOKENS_CAP)
                    raise RuntimeError(
                        f"model hit max_tokens={old_tokens} (finish_reason=length); retrying with {tokens}"
                    )
                # Valid finish_reason but no recognizable class in the text.
                # Stop retrying so the post-retry handling records status="empty".
                break
            except Exception as e:  # noqa: BLE001 - retry transient provider errors
                last_error = e
                if _is_quota_error(e):
                    # OpenRouter key/credit limit: fail over to the next key once.
                    try:
                        current = keys.index(client_box["client"].api_key)
                    except ValueError:
                        current = 0
                    if current + 1 < len(keys):
                        client_box["client"] = _build_openai_client(keys[current + 1])
                        key_switched = True
                        print(
                            f"WARN: OpenRouter key quota/limit; failing over to alternate key for {filename}",
                            file=sys.stderr,
                        )
                        continue
                    print(f"ERROR: all OpenRouter keys exhausted for {filename}", file=sys.stderr)
                    break
                if _is_rate_limit(e):
                    throttle.record_429()
                    time.sleep(_retry_after_seconds(e) or _backoff_for(RATE_LIMIT_BACKOFF, attempts))
                else:
                    time.sleep(_backoff_for(TRANSIENT_BACKOFF, attempts))

        # Fallback-model salvage: rows that fail primary retries (content
        # filters, empty responses) get one attempt through --fallback-model.
        used_fallback = False
        if not predicted and fallback_model and fallback_client_box:
            try:
                fallback_response = fallback_client_box["client"].chat.completions.create(
                    model=fallback_model,
                    messages=build_vision_messages(classification_prompt, image_b64),
                    max_tokens=min(tokens, MAX_TOKENS_CAP),
                    temperature=temperature,
                    extra_body=_build_extra_body(fallback_model, reasoning_effort),
                )
                fallback_raw = fallback_response.choices[0].message.content or ""
                fallback_pred = extract_prediction(fallback_raw)
                if fallback_pred:
                    predicted = fallback_pred
                    raw = fallback_raw
                    finish_reason = fallback_response.choices[0].finish_reason
                    reasoning_text = _extract_reasoning(fallback_response.choices[0].message)
                    used_fallback = True
            except Exception as e:  # noqa: BLE001 - fallback must never raise
                print(f"WARNING: fallback model failed for {filename}: {e}", file=sys.stderr)

        # Near-miss tracking: capture the label the model named as its runner-up
        # in the reasoning trace (its second choice). Local scoring reads this
        # to flag rows where the correct answer was the runner-up.
        runner_up = ""
        row_cost = 0.0
        if predicted:
            runner_up = extract_runner_up(reasoning_text or raw)
            last_response = fallback_response if used_fallback else response
            row_cost = _response_cost(last_response)
            cost_by_index[input_data["index"]] = row_cost

        if not predicted:
            status = "error" if last_error is not None or raw.strip() == "" else "empty"
            error_msg = str(last_error) if last_error is not None else "response contained no valid class"
            if manifest:
                manifest.append({
                    "filename": filename,
                    "expected": expected,
                    "status": status,
                    "tag": "ERROR!",
                    "predicted": "",
                    "attempts": attempts,
                    "error": error_msg,
                })
            msg = f"{ERROR_PREFIX}{filename}: {error_msg}"
            print(msg, file=sys.stderr)
            _safe_span_log(
                metadata={
                    "filename": filename,
                    "error": error_msg,
                    "attempts": attempts,
                    "key_switched": key_switched,
                }
            )
            return msg

        if manifest:
            tag = "OK" if predicted.strip().lower() == expected.strip().lower() else "MISS!"
            manifest.append({
                "filename": filename,
                "expected": expected,
                "status": "completed",
                "tag": tag,
                "predicted": predicted,
                "attempts": attempts,
                "error": "",
                "fallback": used_fallback,
                "runner_up": runner_up,
                "cost": row_cost,
            })

        # Log metadata for Braintrust UI — includes reasoning trace and prompt.
        # finish_reason is recorded so rows salvaged from truncated/errored
        # responses ("length" / "error") can be identified and audited.
        _safe_span_log(
            metadata={
                "raw_response": raw,
                "reasoning": reasoning_text or "(reasoning not exposed by model)",
                "model": fallback_model if used_fallback else model,
                "prompt_version": prompt_version,
                "max_tokens": max_tokens,
                "filename": input_data["filename"],
                "finish_reason": finish_reason,
                "fallback": used_fallback,
                "key_switched": key_switched,
                "runner_up": runner_up,
                "cost": row_cost,
            }
        )

        return predicted

    def exact_match(output: str, expected: str) -> float:
        """Score 1.0 if prediction matches expected class, else 0.0."""
        return 1.0 if output == expected else 0.0

    def failure(output: str, expected: str) -> float:
        """Score 1.0 for rows the model failed to classify (error sentinel output)."""
        return 1.0 if output.startswith(ERROR_PREFIX) else 0.0

    def cost(input: dict) -> float:
        """Actual billed USD cost OpenRouter reported for this row's completion.

        Cost is captured from ``usage.cost`` on the successful response by
        classify_document. Cached rows (replayed from the manifest without an
        API call) score 0.0 for this run.
        """
        return cost_by_index.get(input.get("index"), 0.0)

    result = braintrust.Eval(
        PROJECT_NAME,
        data=lambda: [
            {
                "input": {
                    "index": i,
                    "filename": d["filename"],
                },
                "expected": d["expected"],
                "filename": d["filename"],
            }
            for i, d in enumerate(dataset)
        ],
        task=classify_document,
        scores=[exact_match, failure, cost],
        max_concurrency=max_concurrency,
        reporter=quiet_reporter(),
        project_id=project_id,
        experiment_name=experiment_name,
        metadata={
            "prompt": classification_prompt,
            "prompt_version": prompt_version,
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "reasoning": reasoning_effort or resolved_effort,
            "dataset": f"{DEFAULT_DATASET_PROJECT}/{dataset_name}",
            "manifest": str(manifest_path) if manifest_path else None,
        },
        description=f"{model} | prompt {prompt_version} | reasoning {reasoning_effort or resolved_effort} | temperature {temperature} | Braintrust scorers: exact_match, failure, cost (near-miss scored locally via score_manifest)",
    )

    failed_count = print_classifications(result)

    # Catchall completion alert: any failed/errored row means the run finished
    # with failures (failure motif); otherwise play the success jingle.
    if sound:
        if failed_count:
            play_failure()
        else:
            play_success()


def print_classifications(result) -> int:
    """Print only the classification outcome: per-image labels and accuracy.

    Failed rows (ERROR_PREFIX sentinel output) count as misses in the totals
    but are not shown in the per-image listing. Returns the failed row count.
    """
    rows = [
        (r.input["filename"], r.expected, r.output, r.expected == r.output)
        for r in result.results
        if r.error is None and not str(r.output).startswith(ERROR_PREFIX)
    ]
    failed_rows = [r for r in result.results if str(r.output).startswith(ERROR_PREFIX)]
    rows.sort(key=lambda row: (row[1], row[0]))

    for filename, expected, predicted, correct in rows:
        print(f"{'OK ' if correct else 'MISS!'}  {expected:<24} {predicted:<24} {filename}")
    for r in failed_rows:
        print(f"ERROR! {r.expected:<24} {'':<24} {r.input['filename']}")

    per_class = Counter()
    per_class_correct = Counter()
    for _, expected, _, correct in rows:
        per_class[expected] += 1
        per_class_correct[expected] += int(correct)
    for r in failed_rows:
        per_class[r.expected] += 1

    print()
    for cls in sorted(per_class):
        total = per_class[cls]
        correct = per_class_correct[cls]
        print(f"{cls:<24} {correct}/{total} ({correct / total:.0%})")

    total = len(rows) + len(failed_rows)
    correct = sum(1 for row in rows if row[3])
    print()
    if failed_rows:
        print(f"{len(failed_rows)} failed rows counted as misses (tracked as `failure` metric)")
    print(f"exact_match {correct}/{total} ({correct / total:.1%})" if total else "no results")
    return len(failed_rows)


def main() -> None:
    # Loads .env and validates both keys are present before anything else.
    get_api_keys()

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=PROJECT_NAME,
                        help="Braintrust project for evaluation (where results are logged)")
    parser.add_argument("--project-id", default=PROJECT_ID,
                        help=f"Braintrust project id for evaluation (default: {PROJECT_ID})")
    parser.add_argument("--dataset-project", default=DEFAULT_DATASET_PROJECT,
                        help="Braintrust project holding the dataset")
    parser.add_argument("--dataset", default=DEFAULT_DATASET,
                        help="Braintrust dataset name to classify")
    parser.add_argument("--images-dir", type=Path, default=None,
                        help="Classify local PNGs instead of a Braintrust dataset")
    parser.add_argument("--limit", type=int, default=None,
                        help="Classify only the first N images")
    parser.add_argument("--samples-per-class", type=int, default=None,
                        help="Deterministically subsample N images per class (class-balanced subset)")
    parser.add_argument("--sample-seed", type=int, default=42,
                        help="Random seed for --samples-per-class subsampling (default: 42)")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Model to use for classification (default: {DEFAULT_MODEL})")
    parser.add_argument("--prompt-version", default=DEFAULT_PROMPT_VERSION,
                        help=f"Prompt version to use (v1-v14) (default: {DEFAULT_PROMPT_VERSION})")
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS,
                        help=f"Maximum tokens for model response (default: {DEFAULT_MAX_TOKENS})")
    parser.add_argument("--temperature", type=float, default=0.1,
                        help="Sampling temperature for the model (default: 0.1)")
    parser.add_argument("--reasoning-effort", default=None,
                        help="Override reasoning effort (minimal/low/medium/high/xhigh/max); "
                             "defaults: qwen=high, kimi=xhigh, gemini=max")
    parser.add_argument("--experiment-name", default=None,
                        help="Braintrust experiment name (default: {model-slug}_p{prompt-version})")
    parser.add_argument("--manifest", type=Path, default=None,
                        help="JSONL checkpoint manifest for resuming an interrupted run")
    parser.add_argument("--max-concurrency", type=int, default=8,
                        help="Maximum concurrent API calls (default: 8)")
    parser.add_argument("--no-sound", action="store_true",
                        help="Disable the completion notification jingle")
    parser.add_argument("--fallback-model", default=None,
                        help="Salvage model for rows that fail all primary retries "
                             "(e.g. content-filtered images); tried once per failed row")
    args = parser.parse_args()

    if args.images_dir:
        dataset = load_dataset_images(args.images_dir)
    else:
        # Load the dataset with the default BRAINTRUST_API_KEY; if a separate
        # source-account key (DATA_BRAINTRUST_KEY) is configured, use it instead.
        source_key = os.environ.get("DATA_BRAINTRUST_KEY")
        dataset = load_braintrust_dataset(
            args.dataset_project, args.dataset, source_key, org_id=ORG_ID, api_base=BRAINTRUST_API_BASE
        )

    if args.samples_per_class:
        dataset = sample_balanced(dataset, args.samples_per_class, args.sample_seed)
        per_class = Counter(d["expected"] for d in dataset)
        print(f"Balanced subsample: {len(dataset)} images ({args.samples_per_class} per class x {len(per_class)} classes)")

    if args.limit:
        dataset = dataset[:args.limit]

    if not dataset:
        sys.exit("No labeled images found to classify.")

    validate_dataset(dataset)
    print(f"Running evaluation with {args.model} using prompt {args.prompt_version} on {len(dataset)} images")
    print(f"Evaluation project: {args.project} ({args.project_id}), Dataset from: {args.dataset_project}/{args.dataset}")
    run_eval(
        dataset,
        model=args.model,
        prompt_version=args.prompt_version,
        max_tokens=args.max_tokens,
        temperature=args.temperature,
        reasoning_effort=args.reasoning_effort,
        project_id=args.project_id,
        experiment_name=args.experiment_name,
        dataset_name=args.dataset,
        manifest_path=args.manifest,
        max_concurrency=args.max_concurrency,
        sound=not args.no_sound,
        fallback_model=args.fallback_model,
    )


if __name__ == "__main__":
    main()
