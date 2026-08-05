"""Queue the v11.8 evaluation on the 800-image slice after the 480-image run.

Waits for the in-flight 480-image run (qwen3.7-flash_v0_reasoning_480) to fully
finish (all 480 rows recorded AND its process exited), then re-attempts any rows
it failed (finish_reason=length capouts and transient provider errors) at a higher
max_tokens budget so the 480 run completes cleanly, and only then preflights and
runs the v11.8 prompt with qwen3.7-flash at high reasoning on the rvl_cdip_800
dataset.

The 480 resume pass reuses the manifest's checkpoint (completed rows are skipped,
failed rows re-attempted) after bumping the manifest header's max_tokens to 8192.
It keeps the original run's default OpenRouter key. The v11.8 run uses the
RESEARCH FUNDING OpenRouter key (RESEARCH_FUNDING_API_KEY from .env). Braintrust
credentials come from braintrust.env (the new AMFAMv2 org/project/key).
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

from src.env_utils import require_env  # noqa: E402
from scripts.braintrust.run_eval_queue import verify_manifest  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "scripts" / "braintrust" / "braintrust_openrouter_input.py"
PREFLIGHT = ROOT / "scripts" / "braintrust" / "preflight_eval.py"

# Current in-flight 480-image run we must wait for and finish off.
PID_480 = 50927
DATASET_480 = "fixed_size_sampled_480"
EXPERIMENT_480 = "qwen3.7-flash_v0_reasoning_480"
MANIFEST_480 = ROOT / "reports" / "manifests" / "qwen3.7-flash_v0_480.jsonl"
EXPECTED_480_ROWS = 480
RESUME_MAX_TOKENS = 8192

# The queued v11.8 run on the 800-image slice.
PROJECT = "AMFAMv2"
PROJECT_ID = "9e76bd46-19f7-4b4f-8fce-e36a2028237b"
DATASET = "rvl_cdip_800"
PROMPT_VERSION = "v11.8"
MODEL = "qwen/qwen3.7-flash"
REASONING_EFFORT = "high"
MAX_TOKENS = 8192
EXPERIMENT_NAME = "qwen3.7-flash_v11.8_reasoning_800"
MANIFEST = ROOT / "reports" / "manifests" / f"{EXPERIMENT_NAME}.jsonl"
EXPECTED_ROWS = 800


def load_env() -> None:
    """Load braintrust.env first so its credentials (new API key) win over .env."""
    try:
        from dotenv import load_dotenv

        load_dotenv(ROOT / "braintrust.env", override=False)
        load_dotenv(ROOT / ".env", override=False)
    except ImportError:
        pass


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


def count_manifest_rows(path: Path) -> int:
    if not path.exists():
        return 0
    count = 0
    for line in path.read_text(encoding="utf-8").splitlines()[1:]:
        if line.strip():
            count += 1
    return count


def manifest_status_counts(path: Path) -> dict[str, int]:
    counts = {"completed": 0, "error": 0, "empty": 0}
    if not path.exists():
        return counts
    for line in path.read_text(encoding="utf-8").splitlines()[1:]:
        if line.strip():
            record = json.loads(line)
            counts[record.get("status", "empty")] = counts.get(record.get("status", "empty"), 0) + 1
    return counts


def manifest_unique_status_counts(path: Path) -> dict[str, int]:
    """Count final status per unique filename (append-only manifests repeat rows)."""
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


def set_manifest_max_tokens(path: Path, new_max: int) -> None:
    """Rewrite only the manifest header's max_tokens so a resume can use a larger budget."""
    lines = path.read_text(encoding="utf-8").splitlines()
    header = json.loads(lines[0])
    header["metadata"]["max_tokens"] = new_max
    lines[0] = json.dumps(header, sort_keys=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def wait_for_480(timeout_minutes: int) -> None:
    print(f"Waiting for the 480-image run process to exit (manifest: {MANIFEST_480.name})...")
    deadline = time.time() + timeout_minutes * 60
    while True:
        rows = count_manifest_rows(MANIFEST_480)
        alive = process_alive(PID_480)
        print(f"  480 run: {rows}/{EXPECTED_480_ROWS} rows (process {'running' if alive else 'exited'})")
        if not alive:
            print("  480 run process has exited.")
            return
        if time.time() > deadline:
            sys.exit(f"Aborting: timed out after {timeout_minutes} minutes waiting for the 480 run.")
        time.sleep(30)


def resume_480(default_env: dict, dry_run: bool) -> None:
    """Re-attempt failed/unprocessed rows in the 480 manifest at a higher budget.

    Reuses the manifest checkpoint so completed rows are skipped; failed rows are
    re-attempted and rows that were never recorded (e.g. after a crash) are run
    fresh. Runs at max_tokens RESUME_MAX_TOKENS to clear reasoning capouts.
    """
    counts = manifest_status_counts(MANIFEST_480)
    rows_done = sum(counts.values())
    failed = counts.get("error", 0) + counts.get("empty", 0)
    missing = max(0, EXPECTED_480_ROWS - rows_done)
    if failed == 0 and missing == 0:
        print(f"  480 run: all {counts['completed']} rows completed; no resume needed.")
        return

    print(
        f"  480 run: {counts['completed']} completed, {failed} failed "
        f"({counts.get('error', 0)} error, {counts.get('empty', 0)} empty), "
        f"{missing} not yet processed — resuming at max_tokens {RESUME_MAX_TOKENS}."
    )
    if not dry_run:
        backup = MANIFEST_480.with_suffix(".jsonl.bak")
        backup.write_text(MANIFEST_480.read_text(encoding="utf-8"), encoding="utf-8")
        set_manifest_max_tokens(MANIFEST_480, RESUME_MAX_TOKENS)

    resume_cmd = [
        sys.executable,
        str(RUNNER),
        "--project",
        PROJECT,
        "--project-id",
        PROJECT_ID,
        "--dataset-project",
        PROJECT,
        "--dataset",
        DATASET_480,
        "--prompt-version",
        "v0",
        "--model",
        MODEL,
        "--temperature",
        "0.1",
        "--max-tokens",
        str(RESUME_MAX_TOKENS),
        "--experiment-name",
        EXPERIMENT_480,
        "--manifest",
        str(MANIFEST_480),
    ]
    if dry_run:
        run(resume_cmd, dry_run=True, env=default_env)
    else:
        run_with_retry(resume_cmd, default_env)

    after = manifest_unique_status_counts(MANIFEST_480)
    remaining = after.get("error", 0) + after.get("empty", 0)
    print(f"  480 run after resume: {after.get('completed', 0)} completed, {remaining} failed")
    if remaining:
        print(
            f"  WARNING: {remaining} rows still failed after the resume pass; "
            f"the 480 experiment will report them as misses.",
            file=sys.stderr,
        )


def run(command: list[str], dry_run: bool, env: dict) -> None:
    print("$ " + " ".join(str(part) for part in command))
    if not dry_run:
        subprocess.run(command, cwd=ROOT, check=True, env=env)


def run_with_retry(command: list[str], env: dict, retries: int = 3) -> None:
    """Run a subprocess, re-invoking it if it crashes.

    Used for the 480 resume pass: the eval runner is crash-prone under Braintrust
    object-store timeouts, but it is idempotent via its manifest checkpoint, so a
    re-invocation resumes from completed rows instead of duplicating work.
    """
    for attempt in range(1, retries + 1):
        print(f"$ (attempt {attempt}/{retries}) " + " ".join(str(part) for part in command))
        try:
            subprocess.run(command, cwd=ROOT, check=True, env=env)
            return
        except subprocess.CalledProcessError as exc:
            print(f"  480 resume attempt {attempt} failed: {exc}", file=sys.stderr)
            if attempt < retries:
                print("  Re-invoking from manifest checkpoint...", file=sys.stderr)
                time.sleep(10)
    raise RuntimeError(f"480 resume failed after {retries} attempts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Print the queued commands without running them")
    parser.add_argument("--wait-timeout-minutes", type=int, default=360,
                        help="Give up waiting for the 480 run after this many minutes")
    args = parser.parse_args()

    load_env()
    (research_key,) = require_env("RESEARCH_FUNDING_API_KEY")
    default_env = os.environ.copy()
    research_env = default_env.copy()
    research_env["OPENROUTER_API_KEY"] = research_key

    print(
        f"Queued run: {MODEL} | prompt {PROMPT_VERSION} | reasoning {REASONING_EFFORT} | "
        f"max_tokens {MAX_TOKENS} | dataset {PROJECT}/{DATASET} | "
        f"experiment {EXPERIMENT_NAME}"
    )
    print("OpenRouter keys: v11.8 run = RESEARCH_FUNDING_API_KEY; 480 resume = default key")

    if not args.dry_run:
        wait_for_480(args.wait_timeout_minutes)
        resume_480(default_env, dry_run=False)
    else:
        print("(dry-run: skipping 480 wait and resume)")

    run(
        [
            sys.executable,
            str(PREFLIGHT),
            "--dataset",
            DATASET,
            "--prompt-version",
            PROMPT_VERSION,
        ],
        args.dry_run,
        research_env,
    )
    run(
        [
            sys.executable,
            str(RUNNER),
            "--project",
            PROJECT,
            "--project-id",
            PROJECT_ID,
            "--dataset-project",
            PROJECT,
            "--dataset",
            DATASET,
            "--prompt-version",
            PROMPT_VERSION,
            "--model",
            MODEL,
            "--reasoning-effort",
            REASONING_EFFORT,
            "--max-tokens",
            str(MAX_TOKENS),
            "--experiment-name",
            EXPERIMENT_NAME,
            "--manifest",
            str(MANIFEST),
        ],
        args.dry_run,
        research_env,
    )
    if not args.dry_run:
        verify_manifest(MANIFEST, EXPECTED_ROWS)
        print("QUEUE COMPLETE: 480 run finished cleanly; v11.8 run passed preflight, evaluation, and manifest verification")
    else:
        print("DRY RUN: commands printed above are the queued plan")


if __name__ == "__main__":
    main()
