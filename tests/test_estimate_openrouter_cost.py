"""Unit tests for scripts.estimate_openrouter_cost."""

from unittest.mock import patch

from scripts.openrouter import estimate_openrouter_cost as ec


class TestBuildMarkdownSection:
    def test_includes_token_counts_and_actual_cost(self):
        usage = {
            "prompt_tokens": 1000,
            "completion_tokens": 5,
            "total_tokens": 1005,
            "cost": 0.001234,
            "cost_details": {
                "upstream_inference_prompt_cost": 0.001,
                "upstream_inference_completions_cost": 0.000234,
            },
        }
        section = ec.build_markdown_section("openai/gpt-4o", usage, [800, 25000], 3.0, 15.0)

        assert "## Model: `openai/gpt-4o`" in section
        assert "**Prompt tokens:** 1,000" in section
        assert "**Total tokens:** 1,005" in section
        assert "Actual upstream cost:" in section
        # Actual cost projection scales linearly.
        assert "**$0.99**" in section  # 0.001234 * 800

    def test_derives_total_when_missing(self):
        usage = {"prompt_tokens": 10, "completion_tokens": 2}
        section = ec.build_markdown_section("m", usage, [1], 1.0, 1.0)
        assert "**Total tokens:** 12" in section

    def test_uses_price_projection_without_actual_cost(self):
        usage = {"prompt_tokens": 1_000_000, "completion_tokens": 0, "total_tokens": 1_000_000}
        section = ec.build_markdown_section("m", usage, [1], 4.0, 8.0)
        # 1M prompt tokens * $4/M = $4.0000
        assert "**$4.0000**" in section
        assert "Actual upstream cost:" not in section


class TestUpdateMarkdown:
    def test_creates_file_with_header_and_section(self, tmp_path):
        md = tmp_path / "calc.md"
        ec.update_markdown(md, "## Model: `m1`\n\ncontent\n", "m1")
        text = md.read_text(encoding="utf-8")
        assert "# OpenRouter Token and Cost Calculation" in text
        assert "## Model: `m1`" in text
        assert "## Notes" in text

    def test_replaces_existing_section(self, tmp_path):
        md = tmp_path / "calc.md"
        ec.update_markdown(md, "## Model: `m1`\n\nold\n", "m1")
        ec.update_markdown(md, "## Model: `m1`\n\nnew\n", "m1")
        text = md.read_text(encoding="utf-8")
        assert "new" in text
        assert "old" not in text
        assert text.count("## Model: `m1`") == 1

    def test_adds_new_section_without_duplicating(self, tmp_path):
        md = tmp_path / "calc.md"
        ec.update_markdown(md, "## Model: `m1`\n\naaa\n", "m1")
        ec.update_markdown(md, "## Model: `m2`\n\nbbb\n", "m2")
        text = md.read_text(encoding="utf-8")
        assert "## Model: `m1`" in text
        assert "## Model: `m2`" in text

    def test_appends_when_no_notes_section(self, tmp_path):
        md = tmp_path / "calc.md"
        md.write_text("# Title\n\nsome body\n", encoding="utf-8")
        ec.update_markdown(md, "## Model: `m1`\n\nx\n", "m1")
        text = md.read_text(encoding="utf-8")
        assert "## Model: `m1`" in text
        assert text.index("some body") < text.index("## Model: `m1`")

    def test_escapes_regex_special_chars_in_model(self, tmp_path):
        md = tmp_path / "calc.md"
        model = "org/model.v1+beta"
        ec.update_markdown(md, f"## Model: `{model}`\n\nfirst\n", model)
        ec.update_markdown(md, f"## Model: `{model}`\n\nsecond\n", model)
        text = md.read_text(encoding="utf-8")
        assert text.count(f"## Model: `{model}`") == 1
        assert "second" in text and "first" not in text


class TestEstimateCostForDataset:
    def _usage(self):
        return {"prompt_tokens": 100, "completion_tokens": 10, "total_tokens": 110}

    def test_projects_tokens_without_pricing(self):
        with patch.object(ec, "classify_image", return_value={"usage": self._usage()}):
            out = ec.estimate_cost_for_dataset("key", "img.png", model="m", num_images=5)
        assert out["estimated_total_prompt_tokens"] == 500
        assert out["estimated_total_completion_tokens"] == 50
        assert out["estimated_total_tokens"] == 550
        assert "cost_note" in out
        assert "estimated_total_cost_usd" not in out

    def test_projects_cost_with_pricing(self):
        with patch.object(ec, "classify_image", return_value={"usage": self._usage()}):
            out = ec.estimate_cost_for_dataset(
                "key",
                "img.png",
                model="m",
                num_images=1_000_000,
                input_price_per_million=2.0,
                output_price_per_million=6.0,
            )
        # 100 prompt tokens * 1e6 imgs = 1e8 tokens -> $200; completion 10*1e6=1e7 -> $60
        assert out["estimated_input_cost_usd"] == 200.0
        assert out["estimated_output_cost_usd"] == 60.0
        assert out["estimated_total_cost_usd"] == 260.0

    def test_derives_total_tokens_when_absent(self):
        usage = {"prompt_tokens": 7, "completion_tokens": 3}
        with patch.object(ec, "classify_image", return_value={"usage": usage}):
            out = ec.estimate_cost_for_dataset("key", "img.png", num_images=2)
        assert out["single_image_total_tokens"] == 10
        assert out["estimated_total_tokens"] == 20


class TestGetApiKey:
    def test_returns_key_from_env(self, monkeypatch):
        monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-test")
        assert ec.get_api_key() == "sk-or-test"

    def test_exits_when_missing(self, monkeypatch):
        monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
        import pytest
        from unittest import mock

        with mock.patch("src.env_utils.load_dotenv_if_available"):
            with pytest.raises(SystemExit):
                ec.get_api_key()
