"""Unit tests for scripts.create_fixed_size_dataset."""

import json

from PIL import Image

from scripts.datasets import create_fixed_size_dataset as cf
from src.image_utils import _pad_color_for_mode


class TestPadColorForMode:
    def test_grayscale_from_int(self):
        assert _pad_color_for_mode("L", 255) == 255

    def test_grayscale_from_tuple(self):
        assert _pad_color_for_mode("L", (200, 200, 200)) == 200

    def test_bilevel(self):
        assert _pad_color_for_mode("1", 255) == 1
        assert _pad_color_for_mode("1", 0) == 0

    def test_rgba_from_int(self):
        assert _pad_color_for_mode("RGBA", 255) == (255, 255, 255, 255)

    def test_rgba_from_tuple(self):
        assert _pad_color_for_mode("RGBA", (1, 2, 3, 4)) == (1, 2, 3, 4)

    def test_rgb_default(self):
        assert _pad_color_for_mode("RGB", 128) == (128, 128, 128)
        assert _pad_color_for_mode("RGB", (1, 2, 3)) == (1, 2, 3)


class TestResizeWithPadding:
    def test_output_matches_target_size(self):
        img = Image.new("L", (100, 50))
        out = cf.resize_with_padding(img, (200, 200))
        assert out.size == (200, 200)

    def test_preserves_aspect_ratio_by_padding(self):
        # Wide image scaled to fit width, padded vertically.
        img = Image.new("L", (200, 100), color=0)
        out = cf.resize_with_padding(img, (100, 100), fill=255)
        assert out.size == (100, 100)
        # Top row is padding (fill=255), middle contains the scaled black image.
        assert out.getpixel((50, 0)) == 255
        assert out.getpixel((50, 50)) == 0

    def test_converts_palette_mode(self):
        img = Image.new("P", (10, 10))
        out = cf.resize_with_padding(img, (20, 20))
        assert out.size == (20, 20)
        assert out.mode in ("RGB", "RGBA")

    def test_rgba_paste_uses_mask(self):
        img = Image.new("RGBA", (10, 20), color=(0, 0, 0, 255))
        out = cf.resize_with_padding(img, (20, 20))
        assert out.size == (20, 20)
        assert out.mode == "RGBA"

    def test_tiny_image_scales_to_at_least_one_pixel(self):
        img = Image.new("L", (1, 1000))
        out = cf.resize_with_padding(img, (10, 10))
        assert out.size == (10, 10)


class TestCollectClassImages:
    def test_uses_subdirectories_when_present(self, tmp_path):
        (tmp_path / "letter").mkdir()
        (tmp_path / "letter" / "a.png").write_bytes(b"x")
        (tmp_path / "invoice").mkdir()
        (tmp_path / "invoice" / "b.tif").write_bytes(b"x")

        result = cf._collect_class_images(
            tmp_path, ("letter", "invoice"), ("*.png", "*.tif")
        )
        assert len(result["letter"]) == 1
        assert len(result["invoice"]) == 1

    def test_infers_class_from_filename_prefix(self, tmp_path):
        (tmp_path / "letter_001.png").write_bytes(b"x")
        (tmp_path / "invoice_002.png").write_bytes(b"x")
        (tmp_path / "unrelated.png").write_bytes(b"x")

        result = cf._collect_class_images(
            tmp_path, ("letter", "invoice"), ("*.png",)
        )
        assert len(result["letter"]) == 1
        assert len(result["invoice"]) == 1

    def test_empty_when_nothing_matches(self, tmp_path):
        (tmp_path / "random.png").write_bytes(b"x")
        result = cf._collect_class_images(tmp_path, ("letter",), ("*.png",))
        assert result["letter"] == []


class TestCreateFixedSizeDataset:
    def test_resizes_all_and_writes_summary(self, tmp_path):
        in_dir = tmp_path / "in"
        in_dir.mkdir()
        Image.new("L", (50, 40)).save(in_dir / "a.png")
        Image.new("L", (80, 20)).save(in_dir / "b.jpg")
        out_dir = tmp_path / "out"

        cf.create_fixed_size_dataset(str(in_dir), str(out_dir), (32, 32))

        assert (out_dir / "images" / "a.png").exists()
        assert (out_dir / "images" / "b.jpg").exists()
        summary = json.loads((out_dir / "resize_summary.json").read_text())
        assert summary["total"] == 2
        assert summary["successful"] == 2
        assert summary["failed"] == 0
        assert Image.open(out_dir / "images" / "a.png").size == (32, 32)

    def test_records_failures(self, tmp_path):
        in_dir = tmp_path / "in"
        in_dir.mkdir()
        # Not a real image -> triggers error branch.
        (in_dir / "broken.png").write_bytes(b"not an image")
        out_dir = tmp_path / "out"

        cf.create_fixed_size_dataset(str(in_dir), str(out_dir), (16, 16))
        summary = json.loads((out_dir / "resize_summary.json").read_text())
        assert summary["failed"] == 1
        assert summary["successful"] == 0
        assert summary["details"][0]["status"] == "error"


class TestCreateSampledFixedSizeDataset:
    def test_samples_and_pads_across_datasets(self, tmp_path):
        ds = tmp_path / "ds"
        (ds / "letter").mkdir(parents=True)
        for i in range(3):
            Image.new("L", (40, 60)).save(ds / "letter" / f"l{i}.png")
        out_dir = tmp_path / "out"

        cf.create_sampled_fixed_size_dataset(
            {"dsA": str(ds)},
            str(out_dir),
            target_size=(20, 20),
            samples_per_class=2,
            seed=1,
        )

        images = list((out_dir / "images").glob("*.png"))
        assert len(images) == 2
        # Output filename encodes dataset + class.
        assert all(p.name.startswith("dsA__letter__") for p in images)
        summary = json.loads((out_dir / "resize_summary.json").read_text())
        assert summary["total_successful"] == 2
        assert summary["samples_per_class"] == 2

    def test_skips_missing_dataset_path(self, tmp_path):
        out_dir = tmp_path / "out"
        cf.create_sampled_fixed_size_dataset(
            {"missing": str(tmp_path / "nope")},
            str(out_dir),
            target_size=(10, 10),
            samples_per_class=1,
        )
        summary = json.loads((out_dir / "resize_summary.json").read_text())
        assert summary["total_successful"] == 0
        assert summary["details"][0]["status"] == "skipped"

    def test_samples_all_when_fewer_available(self, tmp_path):
        ds = tmp_path / "ds"
        (ds / "letter").mkdir(parents=True)
        Image.new("L", (10, 10)).save(ds / "letter" / "only.png")
        out_dir = tmp_path / "out"

        cf.create_sampled_fixed_size_dataset(
            {"dsA": str(ds)},
            str(out_dir),
            target_size=(8, 8),
            samples_per_class=10,
            seed=0,
        )
        summary = json.loads((out_dir / "resize_summary.json").read_text())
        assert summary["total_successful"] == 1
