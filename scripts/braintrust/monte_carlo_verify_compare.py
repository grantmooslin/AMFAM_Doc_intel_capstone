"""Compare verification eval results against the Monte Carlo simulator's predictions.

Reads the ``mc_verify_*`` manifests produced by ``monte_carlo_verify.py --run-eval``
and reports, for each slice:

1. **Escalation slice** — measured accuracy of the base run on the
   low-confidence tail vs the simulated ``p_correct`` per image (from the corpus
   confidence study), plus the escalated run's measured accuracy vs the assumed
   ``--escalated-acc``.
2. **Exemplar slice** — measured accuracy of the base prompt (v17.2) vs the
   exemplar-appended prompt (v18) on the same top-confusion-pair images, with a
   paired breakdown, so the simulated error-flip gain can be checked against
   reality.

Zero model spend: this only reads manifests.

Usage:
    python scripts/braintrust/monte_carlo_verify_compare.py
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # noqa: E402

from src.constants import DOCUMENT_CLASSES  # noqa: E402
from src.monte_carlo import safe_div

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFESTS_DIR = ROOT / "reports" / "manifests"
DEFAULT_CORPUS = ROOT / "reports" / "monte_carlo" / "corpus.jsonl"
OUTPUT_DIR = ROOT / "reports" / "monte_carlo"

VALID_CLASSES = set(DOCUMENT_CLASSES)


def load_manifest_rows(path: Path) -> dict[str, dict]:
    """Return {filename: record} for a manifest (last state per filename)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    final: dict[str, dict] = {}
    for line in lines[1:]:
        if not line.strip():
            continue
        record = json.loads(line)
        final[record["filename"]] = record
    return final


def row_correct(record: dict) -> bool:
    if record.get("status") != "completed":
        return False
    return (record.get("predicted") or "").strip().lower() == (record.get("expected") or "").lower()


def summarize(rows: dict[str, dict]) -> dict:
    completed = [r for r in rows.values() if r.get("status") == "completed"]
    correct = sum(1 for r in completed if row_correct(r))
    return {
        "rows": len(rows),
        "completed": len(completed),
        "correct": correct,
        "accuracy": safe_div(correct, len(rows)),
    }


def run() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifests-dir", type=Path, default=DEFAULT_MANIFESTS_DIR)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--alpha", type=float, default=0.03,
                        help="Escalation fraction used when building the verification slice")
    parser.add_argument("--top-pairs", type=int, default=6)
    args = parser.parse_args()

    esc = f"mc_verify_escalation_{int(args.alpha * 100)}pct"
    esc_base = load_manifest_rows(args.manifests_dir / f"{esc}_base.jsonl") \
        if (args.manifests_dir / f"{esc}_base.jsonl").exists() else {}
    esc_esc = load_manifest_rows(args.manifests_dir / f"{esc}_esc.jsonl") \
        if (args.manifests_dir / f"{esc}_esc.jsonl").exists() else {}

    ex = f"mc_verify_exemplar_{args.top_pairs}"
    ex_base = load_manifest_rows(args.manifests_dir / f"{ex}_base.jsonl") \
        if (args.manifests_dir / f"{ex}_base.jsonl").exists() else {}
    ex_ex = load_manifest_rows(args.manifests_dir / f"{ex}_exemplar.jsonl") \
        if (args.manifests_dir / f"{ex}_exemplar.jsonl").exists() else {}

    lines = ["# Verification: Measured vs Simulated",
             "",
             "## Escalation slice (low-confidence tail)",
             ""]
    if not esc_base and not esc_esc:
        lines += ["*No escalation manifests found yet.*", ""]
    else:
        b = summarize(esc_base)
        e = summarize(esc_esc)
        lines += [
            f"| run | rows | correct | accuracy |",
            "|---|---:|---:|---:|",
            f"| base (v11.8) | {b['rows']} | {b['correct']} | {b['accuracy']:.3f} |",
            f"| escalated (max effort) | {e['rows']} | {e['correct']} | {e['accuracy']:.3f} |",
            "",
            "**Simulated reference:** corpus `p_correct` mean on these images and the",
            "assumed escalated accuracy (~0.90). Compare measured vs simulated to",
            "validate the confidence ordering.",
            "",
        ]
        # Per-image simulated p_correct vs measured on the base run.
        sim_by_file: dict[str, float] = {}
        for line in args.corpus.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            if rec.get("status") != "completed":
                continue
            key = rec["filename"]
            entry = sim_by_file.setdefault(key, {"ok": 0, "n": 0})
            entry["ok"] += int((rec.get("predicted") or "").strip().lower() == rec["expected"])
            entry["n"] += 1
        matched = 0
        sim_ok = 0
        meas_ok = 0
        for filename, rec in esc_base.items():
            sim = sim_by_file.get(filename)
            if sim is None:
                continue
            matched += 1
            sim_ok += safe_div(sim["ok"], sim["n"])
            meas_ok += int(row_correct(rec))
        if matched:
            lines += [
                f"**Paired check:** {matched} images matched to corpus sim; "
                f"simulated mean p_correct = {safe_div(sim_ok, matched):.3f}, "
                f"measured base accuracy = {safe_div(meas_ok, matched):.3f}.",
                "",
            ]

    lines += ["## Exemplar slice (top confusion pairs)",
              ""]
    if not ex_base and not ex_ex:
        lines += ["*No exemplar manifests found yet.*", ""]
    else:
        b = summarize(ex_base)
        e = summarize(ex_ex)
        lines += [
            f"| run | rows | correct | accuracy |",
            "|---|---:|---:|---:|",
            f"| base (v17.2) | {b['rows']} | {b['correct']} | {b['accuracy']:.3f} |",
            f"| exemplar (v18) | {e['rows']} | {e['correct']} | {e['accuracy']:.3f} |",
            "",
        ]
        if b["rows"] and e["rows"]:
            delta = e["accuracy"] - b["accuracy"]
            lines += [
                f"**Delta (v18 - v17.2): {delta:+.3f}** "
                f"({'exemplar gain confirmed' if delta > 0 else 'no gain measured'}).",
                "",
                "### Per-image flips",
                "",
                "| filename | expected | base | exemplar |",
                "|---|---|---|---|",
            ]
            for filename in sorted(set(ex_base) & set(ex_ex)):
                expected = ex_base[filename].get("expected", "")
                b_pred = (ex_base[filename].get("predicted") or "").strip().lower()
                e_pred = (ex_ex[filename].get("predicted") or "").strip().lower()
                lines.append(f"| `{filename}` | `{expected}` | {b_pred} | {e_pred} |")

    path = OUTPUT_DIR / "verification_results.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report saved: {path}")
    print("\n" + "\n".join(lines))


if __name__ == "__main__":
    run()
