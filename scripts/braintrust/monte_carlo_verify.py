"""Spend-minimal verification of the Monte Carlo simulator's predictions.

Builds two small Braintrust datasets and prints (or, with ``--run-eval``,
executes) the eval commands that test the simulator against reality:

1. **Escalation verification** — the ``alpha`` fraction of lowest-confidence
   images (from the ensemble/confidence study). Eval'ing them at the base config
   measures the *real* accuracy of the low-confidence tail and checks it against
   the simulated ``p_correct``; eval'ing them through the escalated path (stronger
   model or higher reasoning effort) checks the ``--escalated-acc`` assumption.

2. **Exemplar verification** — images from the top confusion pairs targeted by
   the exemplar miner, so a base prompt vs exemplar-appended prompt eval on the
   same slice can confirm the simulated error-flip gain.

Datasets are built idempotently (deterministic row ids, delete-then-recreate)
and reuse the slice images, so no downloads are repeated. No model credits are
spent unless ``--run-eval`` is passed; the default is a dry-run that prints the
exact commands.

Usage:
    python scripts/braintrust/monte_carlo_verify.py --alpha 0.03
    python scripts/braintrust/monte_carlo_verify.py --alpha 0.03 --run-eval --eval-kind escalation
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # noqa: E402

import braintrust

from src.braintrust_config import load_braintrust_config
from src.braintrust_utils import delete_dataset_by_name, load_braintrust_dataset

from scripts.braintrust.monte_carlo_ensemble import load_observations, build_confidence

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CORPUS = ROOT / "reports" / "monte_carlo" / "corpus.jsonl"
SLICE_DATASETS = [
    "fixed_size_sampled",
    "fixed_size_sampled_v2",
    "fixed_size_sampled_v3",
    "fixed_size_sampled_320",
    "fixed_size_sampled_480",
    "rvl_cdip_800",
    "rvl_cdip_1600",
]


def load_images(config, api_key: str) -> dict[str, bytes]:
    """Download source PNGs from every slice dataset, keyed by filename."""
    source_key = config.data_api_key or None
    by_filename: dict[str, bytes] = {}
    for ds_name in SLICE_DATASETS:
        try:
            recs = load_braintrust_dataset(
                config.dataset_project, ds_name,
                dataset_api_key=source_key, org_id=config.org_id, api_base=config.api_base,
            )
        except Exception as exc:  # noqa: BLE001 - one missing slice shouldn't abort
            print(f"  SKIP {ds_name}: {exc}", file=sys.stderr)
            continue
        for rec in recs:
            by_filename.setdefault(rec["filename"], base64.b64decode(rec["image_b64"]))
        print(f"  {ds_name}: {len(recs)} records (unique images: {len(by_filename)})")
    print(f"Total unique images: {len(by_filename)}")
    return by_filename


def upload_dataset(config, api_key: str, dataset_name: str, rows: list[tuple[str, dict]]) -> None:
    """Delete any existing dataset and insert rows into a fresh one."""
    for attempt in range(1, 4):
        try:
            deleted = delete_dataset_by_name(api_key, config.project_id, dataset_name,
                                             config.api_base)
            if deleted:
                print(f"Deleted existing dataset {dataset_name} ({deleted})")
            braintrust.login(api_key=api_key, force_login=True)
            dataset = braintrust.init_dataset(project_id=config.project_id, name=dataset_name)
            for i, (row_id, row) in enumerate(rows):
                dataset.insert(input=row["input"], expected=row["expected"],
                               metadata=row["metadata"], id=row_id)
            dataset.flush()
            print(f"Dataset ready: {dataset_name} ({len(rows)} rows)")
            return
        except Exception as exc:  # noqa: BLE001 - retry transient network failures
            if attempt == 3:
                raise
            print(f"Upload attempt {attempt} failed ({exc}); retrying in 30s...", file=sys.stderr)
            time.sleep(30)


def row_for(filename: str, expected: str, image_bytes: bytes, tag: str) -> tuple[str, dict]:
    """One dataset row embedding the real PNG with deterministic id."""
    row_id = hashlib.md5(f"{filename}:{tag}".encode("utf-8")).hexdigest()
    return row_id, {
        "input": {
            "image": braintrust.Attachment(data=image_bytes, filename=filename,
                                           content_type="image/png"),
            "filename": filename,
            "metadata": {"tag": tag},
        },
        "expected": expected,
        "metadata": {"tag": tag},
    }


def build_escalation_dataset(config, api_key, images, alpha: float, min_images: int) -> list:
    """Select the lowest-confidence ``alpha`` fraction and build a dataset."""
    observations = load_observations(DEFAULT_CORPUS)
    conf = build_confidence(observations)
    rows = sorted(conf.values(), key=lambda r: r["confidence"])
    n_esc = max(min_images, int(round(alpha * len(rows))))
    selected = rows[:n_esc]
    dataset_rows = []
    skipped = 0
    for r in selected:
        image_bytes = images.get(r["filename"])
        if image_bytes is None:
            skipped += 1
            continue
        dataset_rows.append(row_for(r["filename"], r["expected"], image_bytes, "escalation"))
    name = f"mc_verify_escalation_{int(alpha * 100)}pct"
    upload_dataset(config, api_key, name, dataset_rows)
    print(f"  selected {len(selected)} candidates, {len(dataset_rows)} uploaded "
          f"({skipped} missing images)")
    return dataset_rows


def build_exemplar_dataset(config, api_key, images, top_pairs: int, per_pair: int) -> list:
    """Select misclassified images from the top confusion pairs."""
    counts: Counter = Counter()
    by_pair: dict[tuple[str, str], list[tuple[str, str]]] = {}
    for line in DEFAULT_CORPUS.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        if rec.get("status") != "completed":
            continue
        expected = rec.get("expected")
        predicted = (rec.get("predicted") or "").strip().lower()
        if predicted == expected:
            continue
        pair = (expected, predicted)
        counts[pair] += 1
        by_pair.setdefault(pair, []).append((rec["filename"], expected))
    dataset_rows = []
    used = set()
    for pair, count in counts.most_common(top_pairs):
        added = 0
        for filename, expected in by_pair.get(pair, []):
            if filename in used or added >= per_pair:
                continue
            image_bytes = images.get(filename)
            if image_bytes is None:
                continue
            used.add(filename)
            dataset_rows.append(row_for(filename, expected, image_bytes,
                                        f"exemplar_{pair[0]}->{pair[1]}"))
            added += 1
        if added:
            print(f"  pair {pair[0]}->{pair[1]}: {added} images")
    name = f"mc_verify_exemplar_top{top_pairs}"
    upload_dataset(config, api_key, name, dataset_rows)
    return dataset_rows


def eval_command(dataset: str, experiment: str, manifest: str,
                 extra: str = "") -> str:
    runner = "scripts/braintrust/braintrust_openrouter_input.py"
    return (f"python {runner} --dataset {dataset} "
            f"--experiment-name {experiment} --manifest reports/manifests/{manifest} "
            f"--no-sound {extra}").strip()


def run() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--alpha", type=float, default=0.03,
                        help="Escalation fraction of lowest-confidence images to verify")
    parser.add_argument("--min-escalation-images", type=int, default=48,
                        help="Floor on escalation dataset size")
    parser.add_argument("--top-pairs", type=int, default=6,
                        help="Top confusion pairs for the exemplar verification slice")
    parser.add_argument("--per-pair", type=int, default=8,
                        help="Images per pair in the exemplar verification slice")
    parser.add_argument("--run-eval", action="store_true",
                        help="Actually run the evals (spends model credits)")
    parser.add_argument("--eval-kind", choices=["escalation", "exemplar", "both"],
                        default="both")
    args = parser.parse_args()

    config = load_braintrust_config()
    api_key = config.api_key or os.environ.get("BRAINTRUST_API_KEY")
    if not api_key:
        sys.exit("BRAINTRUST_API_KEY not set")
    print(f"Environment: org {config.org_id} / project {config.project_name}")

    images = load_images(config, api_key)

    commands = []

    if args.eval_kind in ("escalation", "both"):
        print(f"\n=== Escalation verification (alpha={args.alpha:.0%}) ===")
        build_escalation_dataset(config, api_key, images, args.alpha,
                                 args.min_escalation_images)
        ds = f"mc_verify_escalation_{int(args.alpha * 100)}pct"
        commands.append(eval_command(
            ds, f"mc_verify_escalation_{int(args.alpha * 100)}pct_base",
            f"mc_verify_escalation_{int(args.alpha * 100)}pct_base.jsonl",
            "--prompt-version v11.8"))
        commands.append(eval_command(
            ds, f"mc_verify_escalation_{int(args.alpha * 100)}pct_esc",
            f"mc_verify_escalation_{int(args.alpha * 100)}pct_esc.jsonl",
            "--prompt-version v11.8 --reasoning-effort max"))

    if args.eval_kind in ("exemplar", "both"):
        print(f"\n=== Exemplar verification (top {args.top_pairs} pairs) ===")
        build_exemplar_dataset(config, api_key, images, args.top_pairs, args.per_pair)
        ds = f"mc_verify_exemplar_top{args.top_pairs}"
        commands.append(eval_command(
            ds, f"mc_verify_exemplar_{args.top_pairs}_base",
            f"mc_verify_exemplar_{args.top_pairs}_base.jsonl",
            "--prompt-version v17.2"))
        commands.append(eval_command(
            ds, f"mc_verify_exemplar_{args.top_pairs}_exemplar",
            f"mc_verify_exemplar_{args.top_pairs}_exemplar.jsonl",
            "--prompt-version v18"))

    print("\n" + "=" * 70)
    print("Verification eval commands (run to spend a small, targeted eval)")
    print("=" * 70)
    for cmd in commands:
        print(f"\n  {cmd}")

    if args.run_eval:
        import subprocess
        for cmd in commands:
            real = cmd.split("#")[0].strip()
            print(f"\n>>> {real}")
            subprocess.run(real.split(), cwd=ROOT, check=True)


if __name__ == "__main__":
    run()
