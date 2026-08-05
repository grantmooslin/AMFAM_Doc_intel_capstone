"""Re-invoke an evaluation until every dataset row has a final manifest status.

The eval runner (``braintrust_openrouter_input.py``) appends each row's outcome to
a local JSONL manifest the moment the model returns, so the manifest is the
durable checkpoint independent of Braintrust. If Braintrust score/credit limits
cap out or the process crashes mid-run, re-invoking the runner resumes from the
manifest (completed rows are skipped, failed rows re-attempted, unrecorded rows
run fresh) instead of duplicating work.

This script loops that re-invocation until ``--expected-rows`` unique filenames
have a final status, so the run persists to full completion regardless of
Braintrust availability. It uses the default OpenRouter key
(``OPENROUTER_API_KEY`` from ``.env``). Once complete it auto-scores the
manifest locally (``score_manifest.py``, no Braintrust credits) unless
``--no-score`` is passed.

Usage:
    python scripts/braintrust/resume_until_complete.py \\
        --dataset rvl_cdip_1600 --samples-per-class 70 \\
        --prompt-version v11.8 --model qwen/qwen3.7-flash --max-tokens 8192 \\
        --experiment-name qwen3.7-flash_v11.8_reasoning_1600_balanced_1120 \\
        --manifest reports/manifests/qwen3.7-flash_v11.8_1600_balanced_1120.jsonl \\
        --expected-rows 1120
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.braintrust_config import load_braintrust_config  # noqa: E402
from src.env_utils import require_env  # noqa: E402
from src.notify import play_failure  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "scripts" / "braintrust" / "braintrust_openrouter_input.py"
SCORER = ROOT / "scripts" / "braintrust" / "score_manifest.py"


def score_manifest(manifest: Path) -> None:
    """Score the completed manifest locally (no Braintrust scorer credits used)."""
    print("Scoring final results from the manifest (no Braintrust needed)...")
    try:
        subprocess.run(
            [sys.executable, str(SCORER), "--manifest", str(manifest)],
            cwd=ROOT,
            check=True,
            env=os.environ.copy(),
        )
    except subprocess.CalledProcessError as exc:
        print(f"WARNING: manifest scoring failed: {exc}", file=sys.stderr)


def manifest_unique_status_counts(path: Path) -> dict[str, int]:
    """Count the final status per unique filename (manifests are append-only)."""
    counts = {"completed": 0, "error": 0, "empty": 0}
    if not path.exists():
        return counts
    final: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines()[1:]:
        if line.strip():
            record = json.loads(line)
            final[record["filename"]] = record.get("status", "empty")
    for status in final.values():
        counts[status] = counts.get(status, 0) + 1
    return counts


def process_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def wait_for_process(pid: int, poll_seconds: int = 15) -> None:
    print(f"Waiting for existing eval process {pid} to exit...")
    while process_alive(pid):
        counts = manifest_unique_status_counts(MANIFEST)
        print(f"  waiting: {sum(counts.values())}/{EXPECTED_ROWS} rows attempted ({counts})")
        time.sleep(poll_seconds)
    print("Existing eval process has exited.")


def build_command(args: argparse.Namespace) -> list[str]:
    config = load_braintrust_config()
    cmd = [
        sys.executable,
        str(RUNNER),
        "--project",
        args.project,
        "--project-id",
        args.project_id,
        "--dataset-project",
        args.dataset_project,
        "--dataset",
        args.dataset,
        "--prompt-version",
        args.prompt_version,
        "--model",
        args.model,
        "--temperature",
        "0.1",
        "--max-tokens",
        str(args.max_tokens),
        "--experiment-name",
        args.experiment_name,
        "--manifest",
        str(args.manifest),
    ]
    if args.samples_per_class:
        cmd += ["--samples-per-class", str(args.samples_per_class), "--sample-seed", str(args.sample_seed)]
    if args.fallback_model:
        cmd += ["--fallback-model", args.fallback_model]
    return cmd


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default="AMFAMv2")
    parser.add_argument("--project-id", default="9e76bd46-19f7-4b4f-8fce-e36a2028237b")
    parser.add_argument("--dataset-project", default=None, help="Project holding the dataset (default: same as --project)")
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--samples-per-class", type=int, default=None,
                        help="Class-balanced subsample size; must match the manifest header")
    parser.add_argument("--sample-seed", type=int, default=42)
    parser.add_argument("--prompt-version", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--max-tokens", type=int, required=True,
                        help="Must match the manifest header max_tokens (rewrite the header to change it)")
    parser.add_argument("--experiment-name", required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--expected-rows", type=int, required=True)
    parser.add_argument("--wait-pid", type=int, default=0,
                        help="Wait for this PID to exit before starting the resume loop")
    parser.add_argument("--max-cycles", type=int, default=50)
    parser.add_argument("--sleep", type=int, default=15,
                        help="Seconds between resume attempts after a crash")
    parser.add_argument("--no-sound", action="store_true",
                        help="Disable the completion notification jingle")
    parser.add_argument("--no-score", action="store_true",
                        help="Do not auto-score the manifest when the run completes")
    parser.add_argument("--fallback-model", default=None,
                        help="Salvage model passed through to the eval runner "
                             "(salvages content-filtered rows that fail primary retries)")
    args = parser.parse_args()

    global EXPECTED_ROWS
    EXPECTED_ROWS = args.expected_rows
    global MANIFEST
    MANIFEST = args.manifest
    if args.dataset_project is None:
        args.dataset_project = args.project

    require_env("OPENROUTER_API_KEY", "BRAINTRUST_API_KEY")
    print(
        f"Resume-until-complete: {args.model} | prompt {args.prompt_version} | "
        f"max_tokens {args.max_tokens} | {args.dataset_project}/{args.dataset} | "
        f"experiment {args.experiment_name} | {EXPECTED_ROWS} expected rows"
    )
    print("OpenRouter key: default (OPENROUTER_API_KEY)")

    if args.wait_pid:
        wait_for_process(args.wait_pid)

    for cycle in range(1, args.max_cycles + 1):
        counts = manifest_unique_status_counts(args.manifest)
        attempted = sum(counts.values())
        print(f"[cycle {cycle}/{args.max_cycles}] {attempted}/{EXPECTED_ROWS} rows attempted ({counts})")
        if attempted >= EXPECTED_ROWS:
            print("ALL EXPECTED ROWS ATTEMPTED — evaluation fully complete.")
            if not args.no_score:
                score_manifest(args.manifest)
            return 0

        cmd = build_command(args)
        print("$ " + " ".join(cmd))
        result = subprocess.run(cmd, cwd=ROOT, env=os.environ.copy())
        if result.returncode != 0:
            print(
                f"eval exited with code {result.returncode}; resuming from manifest checkpoint...",
                file=sys.stderr,
            )
            if not args.no_sound:
                play_failure()
        time.sleep(args.sleep)

    if not args.no_sound:
        play_failure()
    sys.exit(f"did not reach {EXPECTED_ROWS} rows after {args.max_cycles} resume cycles")


if __name__ == "__main__":
    main()
