"""Unit tests for the pure helpers in scripts.braintrust_openrouter_input."""

from scripts.braintrust import braintrust_openrouter_input as bi


class TestNearMissScore:
    def test_zero_when_prediction_correct(self):
        assert bi.near_miss_score("invoice", "invoice", "budget") == 0.0

    def test_one_when_runner_up_is_correct(self):
        assert bi.near_miss_score("budget", "invoice", "invoice") == 1.0

    def test_zero_when_runner_up_does_not_match(self):
        assert bi.near_miss_score("budget", "letter", "invoice") == 0.0

    def test_zero_when_no_runner_up_recorded(self):
        assert bi.near_miss_score("budget", "invoice", "") == 0.0


class TestExtractClassFromFilename:
    def test_extracts_middle_segment(self):
        name = "processed_balanced__invoice__0001.png"
        assert bi.extract_class_from_filename(name) == "invoice"

    def test_returns_unknown_without_delimiter(self):
        assert bi.extract_class_from_filename("nofields.png") == "unknown"

    def test_handles_extra_segments(self):
        name = "ds__letter__foo__bar.png"
        assert bi.extract_class_from_filename(name) == "letter"


class TestEncodeImageBase64:
    def test_round_trips(self, tmp_path):
        import base64

        raw = b"image-bytes"
        p = tmp_path / "x.png"
        p.write_bytes(raw)
        assert base64.b64decode(bi.encode_image_base64(p)) == raw


class TestLoadDatasetImages:
    def test_only_includes_valid_classes(self, tmp_path):
        # Valid class filenames.
        (tmp_path / "ds__invoice__001.png").write_bytes(b"x")
        (tmp_path / "ds__letter__002.png").write_bytes(b"x")
        # Invalid class -> excluded.
        (tmp_path / "ds__notaclass__003.png").write_bytes(b"x")
        # Non-png -> ignored by glob.
        (tmp_path / "ds__invoice__004.txt").write_bytes(b"x")

        dataset = bi.load_dataset_images(tmp_path)
        classes = sorted(d["expected"] for d in dataset)
        assert classes == ["invoice", "letter"]
        for d in dataset:
            assert set(d.keys()) == {"image_b64", "filename", "expected"}

    def test_empty_dir_returns_empty_list(self, tmp_path):
        assert bi.load_dataset_images(tmp_path) == []


class TestGetApiKeys:
    def test_returns_both_keys(self, monkeypatch):
        monkeypatch.setenv("OPENROUTER_API_KEY", "or-key")
        monkeypatch.setenv("BRAINTRUST_API_KEY", "bt-key")
        assert bi.get_api_keys() == ("or-key", "bt-key")

    def test_exits_when_any_missing(self, monkeypatch):
        import pytest
        from unittest import mock

        monkeypatch.setenv("OPENROUTER_API_KEY", "or-key")
        monkeypatch.delenv("BRAINTRUST_API_KEY", raising=False)
        with mock.patch("src.env_utils.load_dotenv_if_available"):
            with pytest.raises(SystemExit):
                bi.get_api_keys()
