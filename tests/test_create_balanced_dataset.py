"""Unit tests for scripts.create_balanced_dataset."""

import json

from scripts.datasets import create_balanced_dataset as cb


def _make_source(tmp_path, class_to_count):
    src = tmp_path / "source"
    for class_name, count in class_to_count.items():
        d = src / class_name
        d.mkdir(parents=True)
        for i in range(count):
            (d / f"{class_name}_{i:03d}.tif").write_bytes(b"tiff")
    return src


class TestInit:
    def test_discovers_sorted_classes_and_makes_output(self, tmp_path):
        src = _make_source(tmp_path, {"invoice": 1, "advertisement": 1})
        out = tmp_path / "out"
        creator = cb.BalancedDatasetCreator(str(src), str(out), samples_per_class=1)
        assert creator.classes == ["advertisement", "invoice"]
        assert out.is_dir()


class TestSampleImages:
    def test_samples_exact_count_per_class(self, tmp_path):
        src = _make_source(tmp_path, {"letter": 10, "memo": 8})
        out = tmp_path / "out"
        creator = cb.BalancedDatasetCreator(str(src), str(out), samples_per_class=5)

        log = creator.sample_images()

        by_class = {entry["class"]: entry for entry in log}
        assert by_class["letter"]["sampled"] == 5
        assert by_class["memo"]["sampled"] == 5
        assert len(list((out / "letter").glob("*.tif"))) == 5
        # Log persisted to disk.
        saved = json.loads((out / "sampling_log.json").read_text())
        assert len(saved) == 2

    def test_takes_all_when_fewer_than_requested(self, tmp_path):
        src = _make_source(tmp_path, {"resume": 3})
        out = tmp_path / "out"
        creator = cb.BalancedDatasetCreator(str(src), str(out), samples_per_class=5)

        log = creator.sample_images()
        assert log[0]["available"] == 3
        assert log[0]["sampled"] == 3
        assert log[0]["percentage"] == 100.0


class TestVerifyDataset:
    def test_reports_ok_mismatch_and_missing(self, tmp_path):
        src = _make_source(tmp_path, {"form": 5, "email": 5, "budget": 5})
        out = tmp_path / "out"
        creator = cb.BalancedDatasetCreator(str(src), str(out), samples_per_class=5)
        creator.sample_images()

        # Force a mismatch by deleting one sampled file.
        form_files = list((out / "form").glob("*.tif"))
        form_files[0].unlink()
        # Force a missing class dir.
        for f in (out / "email").glob("*.tif"):
            f.unlink()
        (out / "email").rmdir()

        log = creator.verify_dataset()
        status = {entry["class"]: entry["status"] for entry in log}
        assert status["budget"] == "OK"
        assert status["form"] == "MISMATCH"
        assert status["email"] == "MISSING"
        saved = json.loads((out / "verification_log.json").read_text())
        assert len(saved) == 3
