"""Unit tests for the ALE + stop-word reasoning-trace visualization.

Covers the reasoning-trace parser, the ALE estimator, the stop-word
tokenizer, and the hasty-stop ranking used by
``scripts/braintrust/ale_stopword_visual.py``.
"""

import numpy as np

from scripts.braintrust.ale_stopword_visual import (
    accumulated_local_effects,
    build_rows,
    parse_reasoning,
    stop_word_analysis,
    tokenize_evidence,
)

V11_TRACE = """The user wants me to classify a scanned business document.

**Pre-scan:**
- Mail-client header block: Yes. "From:", "Sent:", "To:", "Subject:".

**Check 1: file_folder**
- Evidence: No, there is body content (email text).
- Result: not this check.

**Check 2: handwritten**
- Evidence: No, it's typed text.
- Result: not this check.

**Check 11: correspondence -> email**
- Evidence: Mail-client header block: "From: Carnovale, Mary E.",
  "Subject: FW: Nova Stuff". This is clearly an email.
- Stop here.
"""

V0_TRACE = """**2. Apply the classification rules:**
- **Check 1: advertisement?** No.
- **Check 2: budget?** No.
- **Check 7: invoice?** Yes. The header says "MONTHLY INVOICE".
"""

V0_LABEL_TRACE = """**2. Evaluate against categories:**
- **advertisement**: No.
- **budget**: No.
- **file_folder**: Yes. The tab says "LEGAL". This is a file folder tab.
- **form**: No fields.
"""


class TestParseReasoning:
    def test_v11_header_format(self):
        parsed = parse_reasoning(V11_TRACE)
        assert parsed is not None
        assert parsed["format"] == "header"
        assert parsed["checks_walked"] == 3
        assert parsed["stop_position"] == 11
        assert "Carnovale" in parsed["stop_evidence"]

    def test_v0_check_eval_format(self):
        parsed = parse_reasoning(V0_TRACE)
        assert parsed is not None
        assert parsed["format"] == "check-eval"
        assert parsed["stop_position"] == 7
        assert parsed["checks_walked"] == 3

    def test_v0_label_eval_format(self):
        parsed = parse_reasoning(V0_LABEL_TRACE)
        assert parsed is not None
        assert parsed["format"] == "label-eval"
        assert parsed["stop_position"] == 4  # file_folder is the 4th class

    def test_empty_returns_none(self):
        assert parse_reasoning("") is None
        assert parse_reasoning("  \n  ") is None

    def test_no_stop_when_all_negative(self):
        trace = (
            "**Check 1: file_folder**\n- Evidence: None.\n- Result: not this check.\n"
            "**Check 2: handwritten**\n- Evidence: No.\n- Result: not this check."
        )
        parsed = parse_reasoning(trace)
        assert parsed is not None
        assert parsed["stop_position"] is None
        assert parsed["checks_walked"] == 2


class TestTokenizeEvidence:
    def test_prefers_quoted_spans(self):
        toks = tokenize_evidence('header says "MONTHLY INVOICE" and "AMOUNT DUE"')
        assert "monthly" in toks
        assert "invoice" in toks
        assert "amount" in toks
        assert "header" not in toks  # unquoted prose dropped when quotes present

    def test_falls_back_to_full_text(self):
        toks = tokenize_evidence("facsimile transmission cover sheet present")
        assert "facsimile" in toks

    def test_filters_stopwords(self):
        toks = tokenize_evidence('"the page is not this check"')
        assert "the" not in toks
        assert "page" not in toks  # generic word filtered
        assert "check" in toks

    def test_empty(self):
        assert tokenize_evidence("") == []
        assert tokenize_evidence(None) == []


class TestAccumulatedLocalEffects:
    def test_returns_curve_and_ci(self):
        rng = np.random.default_rng(42)
        x = rng.uniform(0, 100, 500)
        y = (x > 50).astype(float)
        res = accumulated_local_effects(x, y, n_bins=10, n_boot=50)
        assert res is not None
        assert len(res["centers"]) == len(res["ale"]) == 10
        assert len(res["ci_lo"]) == len(res["ci_hi"]) == 10
        assert np.all(res["ci_lo"] <= res["ci_hi"] + 1e-9)

    def test_high_x_increases_accuracy(self):
        rng = np.random.default_rng(1)
        x = rng.uniform(0, 100, 800)
        y = (x > 50).astype(float) + rng.uniform(0, 0.2, 800)
        y = np.clip(y, 0, 1)
        res = accumulated_local_effects(x, y, n_bins=10, n_boot=30)
        assert res["ale"][-1] > res["ale"][0]

    def test_constant_feature_returns_none(self):
        x = [5.0] * 100
        y = [0.0] * 100
        assert accumulated_local_effects(x, y, n_bins=5) is None

    def test_too_few_points_returns_none(self):
        res = accumulated_local_effects([1, 2], [0, 1], n_bins=5)
        assert res is None


class TestStopWordAnalysis:
    def _rows(self):
        # 3 traces: word 'invoice' stops early + wrong; 'letter' stops late + right
        return [
            {"stop_position": 7, "stop_evidence": '"INVOICE" header "AMOUNT DUE"',
             "correct": False},
            {"stop_position": 3, "stop_evidence": '"INVOICE" header "AMOUNT DUE"',
             "correct": False},
            {"stop_position": 11, "stop_evidence": '"Dear" salutation "Sincerely"',
             "correct": True},
            {"stop_position": 12, "stop_evidence": '"Dear" salutation "Sincerely"',
             "correct": True},
            {"stop_position": 9, "stop_evidence": '"Dear" salutation',
             "correct": True},
        ]

    def test_ranks_hasty_words_first(self):
        words = stop_word_analysis(self._rows(), min_count=2)
        assert words, "expected at least one ranked word"
        assert words[0]["word"] == "invoice"
        assert words[0]["hasty_score"] > 0
        # The correct-only word ('dear') should not outrank the hasty one.
        correct_words = [w for w in words if w["error_rate"] == 0.0]
        assert all(w["hasty_score"] < words[0]["hasty_score"] for w in correct_words)

    def test_respects_min_count(self):
        words = stop_word_analysis(self._rows(), min_count=5)
        assert all(w["freq"] >= 5 for w in words)

    def test_empty_rows(self):
        assert stop_word_analysis([], min_count=2) == []
        assert stop_word_analysis([{"stop_position": None}], min_count=2) == []


class TestBuildRows:
    def test_filters_non_completed_and_no_reasoning(self):
        records = [
            {"reasoning": "", "status": "completed", "predicted": "email",
             "expected": "email"},
            {"reasoning": V11_TRACE, "status": "completed", "predicted": "email",
             "expected": "email"},
        ]
        rows = build_rows(records)
        assert len(rows) == 1
        assert rows[0]["correct"] is True
        assert rows[0]["stop_position"] == 11

    def test_correctness_flag(self):
        records = [
            {"reasoning": V11_TRACE, "status": "completed", "predicted": "memo",
             "expected": "email"},
        ]
        rows = build_rows(records)
        assert rows[0]["correct"] is False
