"""Unit tests for src.openrouter_classifier."""

import base64
from unittest.mock import MagicMock, patch

import pytest

from src import openrouter_classifier as oc


class TestCleanPrediction:
    def test_returns_empty_for_none(self):
        assert oc.clean_prediction(None) == ""

    def test_returns_empty_for_empty_string(self):
        assert oc.clean_prediction("") == ""

    def test_extracts_exact_class(self):
        assert oc.clean_prediction("invoice") == "invoice"

    def test_is_case_insensitive(self):
        assert oc.clean_prediction("INVOICE") == "invoice"

    def test_strips_whitespace(self):
        assert oc.clean_prediction("  letter  ") == "letter"

    def test_extracts_class_embedded_in_sentence(self):
        assert oc.clean_prediction("This document is a resume.") == "resume"

    def test_returns_cleaned_text_when_no_class_matches(self):
        assert oc.clean_prediction("Totally Unknown") == "totally unknown"

    def test_matches_first_valid_class_in_order(self):
        # "budget" precedes "invoice" in VALID_CLASSES ordering.
        text = "could be budget or invoice"
        assert oc.clean_prediction(text) == "budget"

    def test_all_valid_classes_round_trip(self):
        for cls in oc.VALID_CLASSES:
            assert oc.clean_prediction(cls) == cls


class TestExtractRunnerUp:
    def test_returns_empty_for_none_or_blank(self):
        assert oc.extract_runner_up(None) == ""
        assert oc.extract_runner_up("") == ""

    def test_extracts_label_after_runner_up_marker(self):
        text = (
            "<scratchpad>\nquestionnaire: yes ...\n"
            "Runner-up: form, ruled out because the page is a printed survey instrument "
            "(check 4), which precedes the generic form check.\n</scratchpad>"
        )
        assert oc.extract_runner_up(text) == "form"

    def test_first_positional_class_wins(self):
        # "budget" appears before "invoice" positionally; VALID_CLASSES order
        # (budget, invoice, ...) agrees, but a later-in-string class must not win.
        text = "Runner-up: budget, though it also resembled an invoice."
        assert oc.extract_runner_up(text) == "budget"

    def test_no_marker_returns_empty(self):
        assert oc.extract_runner_up("just a scratchpad with no runner-up line") == ""

    def test_marker_without_valid_class_returns_empty(self):
        assert oc.extract_runner_up("Runner-up: none — everything else ruled out") == ""

    def test_accepts_runner_up_variants(self):
        assert oc.extract_runner_up("runner up: letter, ruled out by the salutation") == "letter"
        assert oc.extract_runner_up("Runner-up: letter") == "letter"

    def test_ignores_reason_text_mentions_before_marker(self):
        text = "form looked plausible here. Runner-up: letter, ruled out by the salutation."
        assert oc.extract_runner_up(text) == "letter"


class TestEncodeImage:
    def test_encodes_file_contents_to_base64(self, tmp_path):
        raw = b"\x89PNG fake bytes"
        img = tmp_path / "img.png"
        img.write_bytes(raw)
        encoded = oc.encode_image_base64(img)
        assert base64.b64decode(encoded) == raw

    def test_missing_file_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            oc.encode_image_base64(tmp_path / "missing.png")


def _mock_response(status=200, json_body=None, raise_http=False):
    resp = MagicMock()
    resp.status_code = status
    resp.json.return_value = json_body or {}
    if raise_http:
        import requests

        resp.raise_for_status.side_effect = requests.exceptions.HTTPError("boom")
    else:
        resp.raise_for_status.return_value = None
    return resp


class TestClassifyImage:
    @patch("src.openrouter_classifier.requests.post")
    @patch("src.openrouter_classifier.encode_image_base64", return_value="ZmFrZQ==")
    def test_success_path_builds_payload_and_parses(self, _enc, mock_post, tmp_path):
        body = {
            "choices": [{"message": {"content": "Invoice"}}],
            "usage": {"prompt_tokens": 10, "completion_tokens": 2},
        }
        mock_post.return_value = _mock_response(json_body=body)

        result = oc.classify_image("key-123", tmp_path / "x.png", model="test/model")

        assert result["status"] == "success"
        assert result["classification"] == "invoice"
        assert result["raw_response"] == "Invoice"
        assert result["model"] == "test/model"
        assert result["usage"] == body["usage"]

        # Verify request construction.
        _, kwargs = mock_post.call_args
        assert kwargs["headers"]["Authorization"] == "Bearer key-123"
        payload = kwargs["json"]
        assert payload["model"] == "test/model"
        content = payload["messages"][0]["content"]
        assert content[0]["text"] == oc.CLASSIFICATION_PROMPT
        assert content[1]["image_url"]["url"] == "data:image/png;base64,ZmFrZQ=="

    @patch("src.openrouter_classifier.requests.post")
    @patch("src.openrouter_classifier.encode_image_base64", return_value="ZmFrZQ==")
    def test_empty_response_sets_status(self, _enc, mock_post, tmp_path):
        body = {"choices": [{"message": {"content": ""}}], "usage": {}}
        mock_post.return_value = _mock_response(json_body=body)

        result = oc.classify_image("k", tmp_path / "x.png")
        assert result["status"] == "empty_response"
        assert result["classification"] == ""

    @patch("src.openrouter_classifier.requests.post")
    @patch("src.openrouter_classifier.encode_image_base64", return_value="ZmFrZQ==")
    def test_malformed_choices_default_to_empty(self, _enc, mock_post, tmp_path):
        mock_post.return_value = _mock_response(json_body={"choices": []})
        result = oc.classify_image("k", tmp_path / "x.png")
        assert result["status"] == "empty_response"
        assert result["classification"] == ""
        assert result["usage"] == {}

    @patch("src.openrouter_classifier.requests.post")
    @patch("src.openrouter_classifier.encode_image_base64", return_value="ZmFrZQ==")
    def test_http_error_is_raised(self, _enc, mock_post, tmp_path):
        import requests

        resp = _mock_response(status=401, json_body={"error": "unauthorized"}, raise_http=True)
        mock_post.return_value = resp
        with pytest.raises(requests.exceptions.HTTPError):
            oc.classify_image("bad", tmp_path / "x.png")
