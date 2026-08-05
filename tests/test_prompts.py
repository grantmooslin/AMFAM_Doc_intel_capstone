import unittest

from src.prompts import DEFAULT_PROMPT_VERSION, get_prompt, list_prompt_versions
from src.openrouter_classifier import clean_prediction


class PromptTests(unittest.TestCase):
    def test_v14_is_registered_and_default(self):
        self.assertEqual(DEFAULT_PROMPT_VERSION, "v17.2")
        self.assertIn("v14", list_prompt_versions())
        prompt = get_prompt("v14")
        self.assertIn("v14 production precedence", prompt)
        self.assertIn("specialist science", prompt)

    def test_unknown_version_fails_loudly(self):
        with self.assertRaisesRegex(ValueError, "Unknown prompt version"):
            get_prompt("v999")

    def test_prediction_parser_prefers_final_label(self):
        response = "Reasoning mentions budget and form.\n<label>invoice</label>"
        self.assertEqual(clean_prediction(response), "invoice")


if __name__ == "__main__":
    unittest.main()
