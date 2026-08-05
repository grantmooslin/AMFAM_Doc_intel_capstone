"""Unit tests for scripts.run_tiff_processing.main."""

from unittest.mock import MagicMock, mock_open, patch

from scripts.datasets import run_tiff_processing as rtp


class TestMain:
    def test_runs_processor_and_writes_summary(self):
        results = [
            {"status": "success", "class_label": "letter"},
            {"status": "success", "class_label": "letter"},
            {"status": "success", "class_label": "invoice"},
            {"status": "error", "document_name": "x"},
        ]
        fake_proc = MagicMock()
        fake_proc.process_batch.return_value = results

        m = mock_open()
        with patch.object(rtp, "ClassOrganizedBatchProcessor", return_value=fake_proc) as ctor, patch(
            "builtins.open", m
        ), patch.object(rtp.json, "dump") as dump:
            rtp.main()

        ctor.assert_called_once()
        fake_proc.process_batch.assert_called_once()
        # The summary written to disk is the processor's results list.
        dumped = dump.call_args[0][0]
        assert dumped == results
