"""Unit tests for src.monte_carlo simulation utilities."""

import random

import numpy as np

from src.monte_carlo import (
    confidence_score,
    draw_committee,
    majority_margin,
    normalize_dist,
    paired_delta_bootstrap,
    safe_div,
    shannon_entropy,
    uncertainty_phrases,
)


class TestNormalizeDist:
    def test_sums_to_one(self):
        dist = normalize_dist({"invoice": 2, "budget": 2})
        assert abs(sum(dist.values()) - 1.0) < 1e-12

    def test_empty_returns_empty(self):
        assert normalize_dist({}) == {}

    def test_single_label(self):
        assert normalize_dist({"form": 5}) == {"form": 1.0}


class TestShannonEntropy:
    def test_one_hot_is_zero(self):
        assert shannon_entropy({"invoice": 1.0}, normalized=True) == 0.0

    def test_uniform_is_one(self):
        dist = {"a": 0.5, "b": 0.5}
        assert abs(shannon_entropy(dist, normalized=True) - 1.0) < 1e-9

    def test_degenerate_empty(self):
        assert shannon_entropy({}, normalized=True) == 0.0


class TestMajorityMargin:
    def test_total_agreement(self):
        assert majority_margin({"invoice": 1.0}) == 1.0

    def test_half_half(self):
        assert abs(majority_margin({"a": 0.5, "b": 0.5})) < 1e-9

    def test_empty(self):
        assert majority_margin({}) == 0.0


class TestDrawCommittee:
    def test_degenerate_votes_are_constant(self):
        rng = random.Random(42)
        assert draw_committee({"invoice": 1.0}, 25, rng) == "invoice"

    def test_majority_wins(self):
        # Heavily favor one label; a 25-vote committee should almost always win it.
        rng = random.Random(7)
        dist = {"budget": 0.9, "invoice": 0.1}
        results = {draw_committee(dist, 25, rng) for _ in range(50)}
        assert "budget" in results

    def test_empty_dist(self):
        assert draw_committee({}, 3, random.Random(1)) == ""


class TestConfidenceScore:
    def test_high_confidence_degenerate(self):
        score = confidence_score({"invoice": 1.0}, near_miss_signal=False, uncertainty=False)
        assert score > 0.9

    def test_low_confidence_split(self):
        low = confidence_score({"invoice": 0.5, "budget": 0.5}, near_miss_signal=True,
                               uncertainty=True)
        high = confidence_score({"invoice": 1.0}, near_miss_signal=False, uncertainty=False)
        assert low < high

    def test_bounds(self):
        score = confidence_score({"a": 0.4, "b": 0.3, "c": 0.3}, near_miss_signal=True,
                                 uncertainty=True)
        assert 0.0 <= score <= 1.0


class TestUncertaintyPhrases:
    def test_detects_hesitation(self):
        assert uncertainty_phrases("I am not sure whether this is a form")

    def test_ignores_clean_trace(self):
        assert not uncertainty_phrases("INVOICE header with line items and amount due")

    def test_empty(self):
        assert not uncertainty_phrases("")


class TestPairedDeltaBootstrap:
    def test_p_win_high_when_a_clearly_better(self):
        deltas = [1.0, 1.0, 1.0, 1.0, 1.0, -1.0]
        result = paired_delta_bootstrap(deltas, n_boot=2000, seed=42)
        assert result["p_win"] > 0.9
        assert "mean" in result
        assert "ci_lo" in result and "ci_hi" in result

    def test_p_win_mid_when_tied(self):
        deltas = [1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 0.0, 0.0]
        result = paired_delta_bootstrap(deltas, n_boot=2000, seed=42)
        assert 0.0 < result["p_win"] < 1.0


class TestSafeDiv:
    def test_zero_denominator(self):
        assert safe_div(5.0, 0) == 0.0

    def test_normal(self):
        assert abs(safe_div(3.0, 2.0) - 1.5) < 1e-12
