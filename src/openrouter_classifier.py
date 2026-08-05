"""
OpenRouter Vision Model Document Classifier
Sends only the document image to a vision-capable LLM for classification
"""

import json
import os
import re
from pathlib import Path
from typing import Union
import requests

from src.constants import DOCUMENT_CLASSES
from src.image_utils import encode_image_base64
from src.openrouter_utils import OPENROUTER_API_URL, build_vision_messages
from src.prompts import get_prompt

# Recommended vision models on OpenRouter
VISION_MODELS = []

CLASSIFICATION_PROMPT = get_prompt("v14")

VALID_CLASSES = list(DOCUMENT_CLASSES)


def clean_prediction(text: Union[str, None]) -> str:
    """Extract valid class name from LLM response using word boundary matching"""
    if not text:
        return ""
    text = text.strip().lower()
    tagged = re.search(r"<label>\s*([^<\s][^<]*?)\s*</label>", text, flags=re.DOTALL)
    if tagged and tagged.group(1).strip() in VALID_CLASSES:
        return tagged.group(1).strip()
    for line in reversed(text.splitlines()):
        candidate = line.strip().strip("`*_ ").lower()
        if candidate in VALID_CLASSES:
            return candidate
    for cls in VALID_CLASSES:
        # Use word boundary matching to avoid substring false positives
        # e.g., "information" should not match "form"
        if re.search(r'\b' + re.escape(cls) + r'\b', text):
            return cls
    return text


def extract_runner_up(text: str) -> str:
    """Extract the model's runner-up (second-choice) label from the reasoning trace.

    The classification prompt's scratchpad procedure ends with a
    ``Runner-up: <label>, ruled out because ...`` line naming the label the model
    almost picked. Returns the FIRST valid class name appearing after that marker
    (positional, not ``VALID_CLASSES`` order), or "" when no marker/class is
    present. ``text`` may be a reasoning_content trace or a raw final answer.
    """
    if not text:
        return ""
    import re
    marker = re.search(r"(?i)runner[- ]?up\s*:?\s*(.+)", text)
    if not marker:
        return ""
    remainder = marker.group(1).lower()
    candidates = [
        (match.start(), cls)
        for cls in VALID_CLASSES
        for match in [re.search(r"\b" + re.escape(cls) + r"\b", remainder)]
        if match
    ]
    if not candidates:
        return ""
    return min(candidates, key=lambda pair: pair[0])[1]


def classify_image(api_key: str, image_path: Path, model: str = "openai/gpt-4o") -> dict:
    """
    Classify a document image using a vision model through OpenRouter API.
    Sends only the image to the vision model - no OCR text or feature data.
    """
    image_base64 = encode_image_base64(image_path)

    payload = {
        "model": model,
        "messages": build_vision_messages(CLASSIFICATION_PROMPT, image_base64),
        # Reasoning models may consume most of the response budget before the
        # final label. Keep the standalone path safe for the same models used
        # by the Braintrust evaluator.
        "max_tokens": 4096,
        "temperature": 0.1
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        OPENROUTER_API_URL,
        headers=headers,
        json=payload,
        timeout=60
    )

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        try:
            error_body = response.json()
        except Exception:
            error_body = response.text
        print(f"OpenRouter API error ({response.status_code}): {error_body}")
        raise

    result = response.json()

    try:
        prediction = result["choices"][0]["message"].get("content") or ""
    except (KeyError, IndexError, AttributeError):
        prediction = ""

    cleaned = clean_prediction(prediction)

    return {
        "status": "success" if cleaned else "empty_response",
        "classification": cleaned,
        "raw_response": prediction,
        "model": model,
        "usage": result.get("usage", {})
    }


if __name__ == "__main__":
    API_KEY = os.environ.get("OPENROUTER_API_KEY", "your-api-key-here")

    IMAGE_PATH = Path(r"c:\Users\grant\AMFAM\processed_balanced_dataset\images\advertisement_0000139610_page_0001.png")

    result = classify_image(API_KEY, IMAGE_PATH)
    print(json.dumps(result, indent=2))
