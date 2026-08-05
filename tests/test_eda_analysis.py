"""Unit tests for scripts.eda_analysis.

The analysis methods save figures/reports to hard-coded absolute paths, so
``plt.savefig`` and ``open`` are patched to keep the tests hermetic; the focus
is on the data-processing logic (DataFrame construction, statistics, report).
"""

import json
from unittest.mock import mock_open, patch

import pytest
from PIL import Image

from scripts.eda import eda_analysis as ea


@pytest.fixture(autouse=True)
def _no_disk_writes():
    """Prevent the hard-coded absolute save paths from touching the filesystem."""
    with patch.object(ea.plt, "savefig"):
        yield


def _make_dataset(tmp_path, class_to_count):
    for class_name, count in class_to_count.items():
        d = tmp_path / class_name
        d.mkdir(parents=True)
        for i in range(count):
            Image.new("L", (100 + i, 200)).save(d / f"{class_name}_{i}.tif")
    return tmp_path


class TestInit:
    def test_discovers_sorted_classes(self, tmp_path):
        _make_dataset(tmp_path, {"invoice": 1, "advertisement": 1})
        eda = ea.DocumentDatasetEDA(str(tmp_path))
        assert eda.classes == ["advertisement", "invoice"]


class TestCollectImageData:
    def test_builds_dataframe(self, tmp_path):
        _make_dataset(tmp_path, {"letter": 2, "memo": 3})
        eda = ea.DocumentDatasetEDA(str(tmp_path))
        eda.collect_image_data()
        assert len(eda.df) == 5
        assert set(eda.df["class"]) == {"letter", "memo"}
        assert "aspect_ratio" in eda.df.columns

    def test_respects_sample_size(self, tmp_path):
        _make_dataset(tmp_path, {"letter": 10})
        eda = ea.DocumentDatasetEDA(str(tmp_path))
        eda.collect_image_data(sample_size=4)
        assert len(eda.df) == 4


class TestAnalyses:
    @pytest.fixture
    def eda(self, tmp_path):
        _make_dataset(tmp_path, {"letter": 3, "memo": 2})
        obj = ea.DocumentDatasetEDA(str(tmp_path))
        obj.collect_image_data()
        return obj

    def test_class_distribution_counts(self, eda):
        counts = eda.analyze_class_distribution()
        assert counts["letter"] == 3
        assert counts["memo"] == 2

    def test_dimension_and_size_and_mode_analyses_run(self, eda):
        # These populate/derive columns and produce plots (savefig patched).
        eda.analyze_image_dimensions()
        eda.analyze_file_sizes()
        assert "size_mb" in eda.df.columns
        eda.analyze_image_modes()

    def test_generate_summary_report(self, eda):
        eda.analyze_file_sizes()  # needed for size_mb column
        m = mock_open()
        with patch("builtins.open", m):
            report = eda.generate_summary_report()
        assert report["total_images"] == 5
        assert report["total_classes"] == 2
        assert set(report["class_distribution"]) == {"letter", "memo"}
        # The report is serialised to the (patched) report file.
        written = "".join(call.args[0] for call in m().write.call_args_list)
        assert json.loads(written)["total_images"] == 5
