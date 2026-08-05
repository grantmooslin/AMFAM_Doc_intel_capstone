"""Unit tests for scripts.eda_dimensions_summary."""

from PIL import Image

from scripts.eda import eda_dimensions_summary as eds


class TestCollectDimensions:
    def test_missing_path_returns_error(self, tmp_path):
        data, error = eds.collect_dimensions(str(tmp_path / "nope"))
        assert data is None
        assert "does not exist" in error

    def test_empty_directory_reports_zero(self, tmp_path):
        data, error = eds.collect_dimensions(str(tmp_path))
        assert error is None
        assert data == {"count": 0, "skipped": 0}

    def test_computes_statistics(self, tmp_path):
        Image.new("L", (100, 200)).save(tmp_path / "a.png")
        Image.new("L", (200, 200)).save(tmp_path / "b.png")

        data, error = eds.collect_dimensions(str(tmp_path))
        assert error is None
        assert data["count"] == 2
        assert data["skipped"] == 0
        assert data["width"]["mean"] == 150.0
        assert data["width"]["min"] == 100
        assert data["width"]["max"] == 200
        assert data["height"]["mean"] == 200.0
        # aspect ratios: 0.5 and 1.0 -> mean 0.75
        assert data["aspect_ratio"]["mean"] == 0.75

    def test_single_image_has_zero_std(self, tmp_path):
        Image.new("L", (50, 50)).save(tmp_path / "only.png")
        data, _ = eds.collect_dimensions(str(tmp_path))
        assert data["count"] == 1
        assert data["width"]["std"] == 0.0

    def test_skips_unreadable_files(self, tmp_path):
        Image.new("L", (10, 10)).save(tmp_path / "good.png")
        (tmp_path / "bad.png").write_bytes(b"not an image")
        data, _ = eds.collect_dimensions(str(tmp_path))
        assert data["count"] == 1
        assert data["skipped"] == 1

    def test_recurses_into_subdirectories(self, tmp_path):
        sub = tmp_path / "sub"
        sub.mkdir()
        Image.new("L", (10, 10)).save(sub / "nested.png")
        data, _ = eds.collect_dimensions(str(tmp_path))
        assert data["count"] == 1
