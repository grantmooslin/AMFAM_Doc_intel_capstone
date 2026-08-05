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

import argparse
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import braintrust
from openai import OpenAI

from src.braintrust_config import load_braintrust_config
from src.braintrust_utils import load_braintrust_dataset
from src.env_utils import require_env
from src.evaluation import ManifestStore, dataset_fingerprint, validate_dataset
from src.image_utils import encode_image_base64
from src.openrouter_classifier import VALID_CLASSES, clean_prediction
from src.openrouter_utils import OPENROUTER_BASE_URL, build_vision_messages
from src.prompts import get_prompt, DEFAULT_PROMPT_VERSION

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEFAULT_MAX_TOKENS = 4096  # Enough for reasoning trace + scratchpad + final label
MAX_TRIES = 3  # Retry transient provider failures (502s, token caps, empty responses)
ERROR_PREFIX = "ERROR: "  # Task output sentinel so failed rows get tracked scores
MAX_TOKENS_CAP = 32768  # Upper bound when growing max_tokens on "length" finish reasons (v17 fix: 16→32K)

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

    # Wrap OpenAI client pointed at OpenRouter with Braintrust logging.
    # Timeout prevents a stalled provider connection from hanging the run
    # forever; the retry loop above treats timeouts as transient failures.
    client = braintrust.wrap_openai(
        OpenAI(
            base_url=OPENROUTER_BASE_URL,
            api_key=openrouter_key,
            timeout=300,
        )
    )

    images_by_index = {i: d["image_b64"] for i, d in enumerate(dataset)}
    expected_by_index = {i: d["expected"] for i, d in enumerate(dataset)}

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

        # Build extra body based on model capabilities. Defaults aim for the
        # maximum reasoning the model family exposes; --reasoning-effort can
        # override (e.g. "medium" for a lighter run). qwen3.x runs at "high"
        # as the sweet spot for accuracy vs token burn.
        effort = reasoning_effort
        extra_body = {}
        if "kimi" in model.lower():
            extra_body = {"reasoning": {"enabled": True, "effort": effort or "xhigh"}}
        elif "gemini" in model.lower():
            extra_body = {"reasoning": {"effort": effort or "max"}, "include_reasoning": True}
        elif "qwen" in model.lower():
            # Qwen3.x are hybrid reasoning models; force thinking on and ask
            # OpenRouter to include the reasoning trace so we can log it.
            extra_body = {
                "reasoning": {"enabled": True, "effort": effort or "high"},
                "include_reasoning": True,
            }
        
        # Transient provider failures (Alibaba 502 "inappropriate content", token
        # caps, empty responses) return no usable content. Retry with backoff;
        # grow max_tokens when the model capped out mid-reasoning.
        tokens = max_tokens
        last_error = None
        attempts = 0
        for attempt in range(MAX_TRIES):
            attempts = attempt + 1
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=build_vision_messages(classification_prompt, image_b64),
                    max_tokens=tokens,
                    temperature=temperature,
                    extra_body=extra_body,
                )
                raw = response.choices[0].message.content or ""
                finish_reason = response.choices[0].finish_reason

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
                # Fall through so the post-retry handling records it as
                # status="empty" rather than wasting retries on the same prompt.
                break
            except Exception as e:  # noqa: BLE001 - retry transient provider errors
                last_error = e
                if attempt < MAX_TRIES - 1:
                    time.sleep(2 * (attempt + 1))
        else:
            if manifest:
                manifest.append({
                    "filename": filename,
                    "expected": expected,
                    "status": "error",
                    "predicted": "",
                    "attempts": attempts,
                    "error": str(last_error),
                })
            msg = f"{ERROR_PREFIX}{filename}: {last_error}"
            print(msg, file=sys.stderr)
            braintrust.current_span().log(
                metadata={"filename": filename, "error": str(last_error), "attempts": attempts}
            )
            return msg

        msg = response.choices[0].message
        reasoning_text = ""
        if hasattr(msg, "reasoning_content") and msg.reasoning_content:
            reasoning_text = msg.reasoning_content
        elif hasattr(msg, "reasoning") and msg.reasoning:
            reasoning_text = msg.reasoning

        # V4 wraps the final label in <label>...</label>; parse it first so the
        # scratchpad prose never leaks a wrong class into the prediction.
        predicted = extract_prediction(raw)

        if not predicted:
            if manifest:
                manifest.append({
                    "filename": filename,
                    "expected": expected,
                    "status": "empty",
                    "predicted": "",
                    "attempts": attempts,
                    "error": "response contained no valid class",
                })
            msg = f"{ERROR_PREFIX}{filename}: response contained no valid class"
            print(msg, file=sys.stderr)
            braintrust.current_span().log(
                metadata={"filename": filename, "error": "response contained no valid class", "attempts": attempts}
            )
            return msg

        if manifest:
            manifest.append({
                "filename": filename,
                "expected": expected,
                "status": "completed",
                "predicted": predicted,
                "attempts": attempts,
                "error": "",
            })

        # Log metadata for Braintrust UI — includes reasoning trace and prompt.
        # finish_reason is recorded so rows salvaged from truncated/errored
        # responses ("length" / "error") can be identified and audited.
        braintrust.current_span().log(
            metadata={
                "raw_response": raw,
                "reasoning": reasoning_text or "(reasoning not exposed by model)",
                "model": model,
                "prompt_version": prompt_version,
                "max_tokens": max_tokens,
                "filename": input_data["filename"],
                "finish_reason": finish_reason,
            }
        )

        return predicted

    def exact_match(output: str, expected: str) -> float:
        """Score 1.0 if prediction matches expected class, else 0.0."""
        return 1.0 if output == expected else 0.0

    def failed(output: str, expected: str) -> float:
        """Score 1.0 for rows the model failed to classify (error sentinel output)."""
        return 1.0 if output.startswith(ERROR_PREFIX) else 0.0

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
        scores=[exact_match, failed],
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
        description=f"{model} | prompt {prompt_version} | reasoning {reasoning_effort or resolved_effort} | temperature {temperature} | exact_match tracked",
    )

    print_classifications(result)


def print_classifications(result) -> None:
    """Print only the classification outcome: per-image labels and accuracy.

    Failed rows (ERROR_PREFIX sentinel output) count as misses in the totals
    but are not shown in the per-image listing."""
    rows = [
        (r.input["filename"], r.expected, r.output, r.expected == r.output)
        for r in result.results
        if r.error is None and not str(r.output).startswith(ERROR_PREFIX)
    ]
    failed_rows = [r for r in result.results if str(r.output).startswith(ERROR_PREFIX)]
    rows.sort(key=lambda row: (row[1], row[0]))

    for filename, expected, predicted, correct in rows:
        print(f"{'OK ' if correct else 'MISS'}  {expected:<24} {predicted:<24} {filename}")
    for r in failed_rows:
        print(f"FAIL {r.expected:<24} {'':<24} {r.input['filename']}")

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
        print(f"{len(failed_rows)} failed rows counted as misses (tracked as `failed` metric)")
    print(f"exact_match {correct}/{total} ({correct / total:.1%})" if total else "no results")


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
    )


if __name__ == "__main__":
    main()
