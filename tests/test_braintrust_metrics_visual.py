"""Unit tests for scripts.braintrust_metrics_visual."""

from unittest.mock import MagicMock, patch

import pytest

from scripts.braintrust import braintrust_metrics_visual as bmv


@pytest.fixture(autouse=True)
def _redirect_output(tmp_path, monkeypatch):
    monkeypatch.setattr(bmv, "OUTPUT_DIR", tmp_path)
    return tmp_path


def _results():
    return [
        {"expected": "invoice", "output": "invoice", "correct": True, "reasoning": "", "filename": "a.png"},
        {"expected": "invoice", "output": "letter", "correct": False, "reasoning": "looks like a letter", "filename": "b.png"},
        {"expected": "letter", "output": "letter", "correct": True, "reasoning": "", "filename": "c.png"},
    ]


class TestPlotPerClassAccuracy:
    def test_writes_chart(self, _redirect_output):
        bmv.plot_per_class_accuracy(_results(), "exp1")
        assert (_redirect_output / "per_class_accuracy_exp1.png").exists()

    def test_handles_empty_results(self, _redirect_output):
        bmv.plot_per_class_accuracy([], "empty")
        assert (_redirect_output / "per_class_accuracy_empty.png").exists()


class TestBuildConfusionMatrix:
    def test_writes_png_and_markdown(self, _redirect_output):
        bmv.build_confusion_matrix(_results(), "exp1")
        assert (_redirect_output / "confusion_matrix_exp1.png").exists()
        md = (_redirect_output / "confusion_matrix_exp1.md").read_text(encoding="utf-8")
        assert "Confusion Matrix" in md
        assert "Overall Accuracy" in md
        # invoice -> letter is the single confused pair.
        assert "Top Confused Pairs" in md
        assert "`invoice`" in md


class TestExtractMisclassificationReasoning:
    def test_no_errors_returns_early(self, _redirect_output, capsys):
        clean = [{"expected": "letter", "output": "letter", "correct": True, "reasoning": "", "filename": "a"}]
        bmv.extract_misclassification_reasoning(clean, "exp1")
        assert not (_redirect_output / "misclassification_reasoning_exp1.md").exists()
        assert "No misclassifications" in capsys.readouterr().out

    def test_writes_reasoning_grouped_by_pair(self, _redirect_output):
        bmv.extract_misclassification_reasoning(_results(), "exp1")
        md = (_redirect_output / "misclassification_reasoning_exp1.md").read_text(encoding="utf-8")
        assert "invoice → letter" in md
        assert "looks like a letter" in md
        assert "b.png" in md


class TestPrintDocSection:
    def test_returns_section_with_accuracy(self):
        meta = {
            "prompt_tokens_avg": 1000.0,
            "completion_tokens_avg": 50.0,
            "reasoning_tokens_avg": 0.0,
            "cached_tokens_avg": 0.0,
            "duration_avg": 2.5,
        }
        section = bmv.print_doc_section(_results(), "exp1", meta)
        assert "exp1" in section
        assert "Accuracy" in section
        # 2/3 correct -> 66.67%
        assert "66.67%" in section

    def test_handles_zero_results(self):
        meta = {
            "prompt_tokens_avg": 0.0,
            "completion_tokens_avg": 0.0,
            "reasoning_tokens_avg": 0.0,
            "cached_tokens_avg": 0.0,
            "duration_avg": 0.0,
        }
        section = bmv.print_doc_section([], "empty", meta)
        assert "0.00%" in section


def _resp(json_body, status=200):
    r = MagicMock()
    r.status_code = status
    r.json.return_value = json_body
    r.raise_for_status.return_value = None
    return r


class TestFetchExperimentResults:
    def test_fetches_and_filters_rows(self, monkeypatch):
        monkeypatch.setenv("BRAINTRUST_API_KEY", "bt-key")

        project_resp = _resp({"objects": [{"id": "p1", "name": bmv.PROJECT_NAME}]})
        exp_resp = _resp({"objects": [
            {"id": "e1", "name": "old", "created": "2020"},
            {"id": "e2", "name": "new", "created": "2021"},
        ]})
        fetch_resp = _resp({
            "events": [
                {"expected": "invoice", "output": "invoice", "metrics": {"prompt_tokens": 100, "completion_tokens": 5, "duration": 1.0}},
                {"expected": "letter", "output": "invoice", "metrics": {}},
                {"expected": "notaclass", "output": "invoice"},  # filtered out
                {"expected": "", "output": "x"},  # filtered out
            ],
            "cursor": None,
        })

        with patch.object(bmv.requests, "get", side_effect=[project_resp, exp_resp]), patch.object(
            bmv.requests, "post", return_value=fetch_resp
        ):
            results, name, meta = bmv.fetch_experiment_results()

        assert name == "new"  # most recent by created
        assert len(results) == 2
        assert meta["prompt_tokens_avg"] == 100
        assert meta["total_rows"] == 4

    def test_targets_named_experiment(self, monkeypatch):
        monkeypatch.setenv("BRAINTRUST_API_KEY", "bt-key")
        project_resp = _resp({"objects": [{"id": "p1", "name": bmv.PROJECT_NAME}]})
        exp_resp = _resp({"objects": [
            {"id": "e1", "name": "alpha", "created": "2020"},
            {"id": "e2", "name": "beta", "created": "2021"},
        ]})
        fetch_resp = _resp({"events": [], "cursor": None})

        with patch.object(bmv.requests, "get", side_effect=[project_resp, exp_resp]), patch.object(
            bmv.requests, "post", return_value=fetch_resp
        ):
            _, name, _ = bmv.fetch_experiment_results("alpha")
        assert name == "alpha"

    def test_missing_api_key_exits(self, monkeypatch):
        monkeypatch.delenv("BRAINTRUST_API_KEY", raising=False)
        with pytest.raises(SystemExit):
            bmv.fetch_experiment_results()

    def test_unknown_project_exits(self, monkeypatch):
        monkeypatch.setenv("BRAINTRUST_API_KEY", "bt-key")
        project_resp = _resp({"objects": [{"id": "p1", "name": "some-other-project"}]})
        with patch.object(bmv.requests, "get", return_value=project_resp):
            with pytest.raises(SystemExit):
                bmv.fetch_experiment_results()
