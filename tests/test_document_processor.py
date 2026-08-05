"""Unit tests for src.document_processor."""

import json
from unittest.mock import patch

import pytest
from PIL import Image

from src import document_processor as dp


@pytest.fixture
def processor(tmp_path):
    return dp.DocumentProcessor(tmp_path / "out", dpi=300)


class TestInit:
    def test_creates_output_directories(self, tmp_path):
        proc = dp.DocumentProcessor(tmp_path / "out", dpi=150)
        assert proc.images_dir.is_dir()
        assert proc.json_dir.is_dir()
        assert proc.dpi == 150
        assert proc.output_dir == tmp_path / "out"


class TestOptimizeImage:
    def test_converts_to_grayscale(self, processor):
        img = Image.new("RGB", (100, 100), color=(255, 0, 0))
        out = processor._optimize_image(img)
        assert out.mode == "L"

    def test_resizes_when_dpi_differs(self, processor):
        # No DPI metadata -> assumed 72 -> scaled to 300.
        img = Image.new("L", (72, 144))
        out = processor._optimize_image(img)
        assert out.size == (300, 600)

    def test_no_resize_when_dpi_matches(self, processor):
        img = Image.new("L", (300, 300))
        img.info["dpi"] = (300, 300)
        out = processor._optimize_image(img)
        assert out.size == (300, 300)

    def test_handles_scalar_dpi_metadata(self, processor):
        img = Image.new("L", (150, 150))
        img.info["dpi"] = 150
        out = processor._optimize_image(img)
        assert out.size == (300, 300)


class TestSaveImage:
    def test_saves_with_expected_filename(self, processor):
        img = Image.new("L", (10, 10))
        path = processor._save_image(img, "mydoc", 3)
        assert path.name == "mydoc_page_0003.png"
        assert path.exists()
        assert path.parent == processor.images_dir


class TestSaveJson:
    def test_writes_json_file(self, processor):
        data = {"a": 1, "b": [1, 2, 3]}
        path = processor._save_json(data, "doc")
        assert path.name == "doc_ocr_results.json"
        assert json.loads(path.read_text(encoding="utf-8")) == data


class TestExtractOcr:
    def test_builds_word_boxes_and_skips_empty(self, processor):
        ocr_data = {
            "text": ["Hello", "  ", "World"],
            "left": [1, 0, 5],
            "top": [2, 0, 6],
            "width": [10, 0, 20],
            "height": [3, 0, 4],
        }
        with patch.object(dp.pytesseract, "image_to_data", return_value=ocr_data):
            words = processor._extract_ocr_with_bounding_boxes(Image.new("L", (5, 5)))

        assert words == [
            {"text": "Hello", "bounding_box": [1, 2, 11, 5]},
            {"text": "World", "bounding_box": [5, 6, 25, 10]},
        ]


class TestProcessTiff:
    def test_process_tiff_end_to_end(self, processor, tmp_path):
        tiff = tmp_path / "sample.tif"
        Image.new("L", (300, 300)).save(tiff, dpi=(300, 300))

        ocr_data = {
            "text": ["word"],
            "left": [0],
            "top": [0],
            "width": [5],
            "height": [5],
        }
        with patch.object(dp.pytesseract, "image_to_data", return_value=ocr_data):
            summary = processor.process_tiff(tiff, class_label="letter")

        assert summary["status"] == "success"
        assert summary["class_label"] == "letter"
        assert summary["total_pages"] == 1
        assert summary["total_words"] == 1
        assert (processor.images_dir / "sample_page_0001.png").exists()

        saved = json.loads((processor.json_dir / "sample_ocr_results.json").read_text())
        assert saved["document_info"]["class_label"] == "letter"
        assert saved["document_info"]["total_words_extracted"] == 1

    def test_process_tiff_reraises_on_failure(self, processor, tmp_path):
        with pytest.raises(Exception):
            processor.process_tiff(tmp_path / "does_not_exist.tif")


class TestProcessPdf:
    def test_process_pdf_from_path(self, processor, tmp_path):
        pages = [Image.new("L", (300, 300)), Image.new("L", (300, 300))]
        ocr_data = {"text": ["a"], "left": [0], "top": [0], "width": [1], "height": [1]}

        with patch.object(dp, "convert_from_path", return_value=pages) as mock_conv, patch.object(
            dp.pytesseract, "image_to_data", return_value=ocr_data
        ):
            summary = processor.process_pdf(tmp_path / "doc.pdf")

        mock_conv.assert_called_once()
        assert summary["status"] == "success"
        assert summary["total_pages"] == 2
        assert summary["total_words"] == 2
        assert len(summary["saved_images"]) == 2

    def test_process_pdf_from_bytes_autonames(self, processor):
        pages = [Image.new("L", (300, 300))]
        ocr_data = {"text": [], "left": [], "top": [], "width": [], "height": []}
        with patch.object(dp, "convert_from_bytes", return_value=pages), patch.object(
            dp.pytesseract, "image_to_data", return_value=ocr_data
        ):
            summary = processor.process_pdf(b"%PDF-bytes", is_bytes=True)

        assert summary["status"] == "success"
        assert summary["document_name"].startswith("document_")
        assert summary["total_words"] == 0

    def test_convert_error_propagates(self, processor, tmp_path):
        with patch.object(dp, "convert_from_path", side_effect=RuntimeError("bad pdf")):
            with pytest.raises(RuntimeError):
                processor.process_pdf(tmp_path / "doc.pdf")


class TestBatchProcessor:
    def test_no_pdfs_returns_empty(self, tmp_path):
        batch = dp.BatchProcessor(tmp_path / "in", tmp_path / "out")
        batch.input_dir.mkdir(parents=True, exist_ok=True)
        assert batch.process_batch() == []

    def test_processes_each_pdf_and_records_errors(self, tmp_path):
        in_dir = tmp_path / "in"
        in_dir.mkdir()
        (in_dir / "a.pdf").write_bytes(b"a")
        (in_dir / "b.pdf").write_bytes(b"b")

        batch = dp.BatchProcessor(in_dir, tmp_path / "out")

        def fake_process(pdf_path, document_name):
            if document_name == "a":
                return {"status": "success", "document_name": "a"}
            raise ValueError("boom")

        with patch.object(batch.processor, "process_pdf", side_effect=fake_process):
            results = batch.process_batch()

        by_name = {r["document_name"]: r for r in results}
        assert by_name["a"]["status"] == "success"
        assert by_name["b"]["status"] == "error"
        assert "boom" in by_name["b"]["error"]


class TestClassOrganizedBatchProcessor:
    def test_no_subdirs_returns_empty(self, tmp_path):
        in_dir = tmp_path / "in"
        in_dir.mkdir()
        batch = dp.ClassOrganizedBatchProcessor(in_dir, tmp_path / "out")
        assert batch.process_batch() == []

    def test_processes_class_dirs(self, tmp_path):
        in_dir = tmp_path / "in"
        (in_dir / "letter").mkdir(parents=True)
        (in_dir / "letter" / "x.tif").write_bytes(b"x")
        (in_dir / "invoice").mkdir(parents=True)
        (in_dir / "invoice" / "y.tiff").write_bytes(b"y")
        (in_dir / "empty").mkdir(parents=True)  # no tiffs -> skipped

        batch = dp.ClassOrganizedBatchProcessor(in_dir, tmp_path / "out")

        def fake_process(tiff_path, document_name, class_label):
            return {"status": "success", "document_name": document_name, "class_label": class_label}

        with patch.object(batch.processor, "process_tiff", side_effect=fake_process):
            results = batch.process_batch()

        assert len(results) == 2
        labels = sorted(r["class_label"] for r in results)
        assert labels == ["invoice", "letter"]
        names = {r["document_name"] for r in results}
        assert "letter_x" in names and "invoice_y" in names

    def test_records_errors(self, tmp_path):
        in_dir = tmp_path / "in"
        (in_dir / "letter").mkdir(parents=True)
        (in_dir / "letter" / "x.tif").write_bytes(b"x")

        batch = dp.ClassOrganizedBatchProcessor(in_dir, tmp_path / "out")
        with patch.object(batch.processor, "process_tiff", side_effect=ValueError("nope")):
            results = batch.process_batch()

        assert results[0]["status"] == "error"
        assert results[0]["class_label"] == "letter"


class TestConvenienceFunctions:
    def test_process_pdf_file(self, tmp_path):
        with patch.object(dp.DocumentProcessor, "process_pdf", return_value={"status": "success"}) as m:
            out = dp.process_pdf_file(tmp_path / "a.pdf", tmp_path / "out")
        assert out == {"status": "success"}
        _, kwargs = m.call_args
        assert kwargs["is_bytes"] is False

    def test_process_pdf_bytes(self, tmp_path):
        with patch.object(dp.DocumentProcessor, "process_pdf", return_value={"status": "success"}) as m:
            out = dp.process_pdf_bytes(b"data", "docname", tmp_path / "out")
        assert out == {"status": "success"}
        _, kwargs = m.call_args
        assert kwargs["is_bytes"] is True
        assert kwargs["document_name"] == "docname"
