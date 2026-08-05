"""Shared Braintrust environment configuration loader.

Reads the Braintrust org/project/dataset/experiment configuration from
``braintrust.env`` (the single source of truth for the AMFAM experiments),
falling back to ``.env`` for any variable the file does not set.

Every experiment/report/dataset script in ``scripts/`` calls
:func:`load_braintrust_config` so org/project/dataset/model can be adjusted in
one place. Command-line flags in the individual scripts still override the
config values per run.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

# Historical defaults kept so scripts still work even when the env file is
# missing a variable. braintrust.env (and braintrust.env.example) documents
# the canonical values.
DEFAULT_ORG_ID = "cc595192-8420-461d-8111-1d3ca1b42948"
DEFAULT_PROJECT_NAME = "AMFAM v2"
DEFAULT_PROJECT_ID = "ba0346b3-cad8-463d-b758-afddafd9f0d0"
DEFAULT_DATASET_PROJECT = "AMFAM v2"
DEFAULT_DATASET = "fixed_size_sampled"
DEFAULT_SMOKE_DATASET = "qwen_misclassification_smoke_v1_v11"
DEFAULT_MODEL = "qwen/qwen3.7-flash"
DEFAULT_API_BASE = "https://api.braintrust.dev"


@dataclass(frozen=True)
class BraintrustConfig:
    """Resolved Braintrust configuration for the current environment."""

    org_id: str
    project_id: str
    project_name: str
    dataset_project: str
    dataset: str
    smoke_dataset: str
    model: str
    api_base: str
    qwen_experiments: tuple[str, ...]
    api_key: str = ""
    data_api_key: str = ""


def _load_dotenv(path: Path) -> None:
    try:
        from dotenv import load_dotenv

        load_dotenv(path, override=False)
    except ImportError:
        pass


def load_braintrust_config(env_file: str | Path = "braintrust.env") -> BraintrustConfig:
    """Load and resolve the Braintrust configuration.

    ``braintrust.env`` is read first and takes precedence over ``.env`` for any
    variable both define, so it can act as the single source of truth while
    ``.env`` continues to fill gaps (e.g. OPENROUTER_API_KEY).
    """
    env_file = Path(env_file)
    if env_file.exists():
        _load_dotenv(env_file)
    _load_dotenv(Path(".env"))

    def get(name: str, default: str) -> str:
        value = os.environ.get(name)
        return value if value not in (None, "") else default

    experiments = tuple(e for e in os.environ.get("QWEN_EXPERIMENTS", "").split() if e)

    return BraintrustConfig(
        org_id=get("BRAINTRUST_ORG_ID", DEFAULT_ORG_ID),
        project_id=get("BRAINTRUST_PROJECT_ID", DEFAULT_PROJECT_ID),
        project_name=get("BRAINTRUST_PROJECT_NAME", DEFAULT_PROJECT_NAME),
        dataset_project=get("BRAINTRUST_DATASET_PROJECT", DEFAULT_DATASET_PROJECT),
        dataset=get("BRAINTRUST_DATASET", DEFAULT_DATASET),
        smoke_dataset=get("BRAINTRUST_SMOKE_DATASET", DEFAULT_SMOKE_DATASET),
        model=get("BRAINTRUST_MODEL", DEFAULT_MODEL),
        api_base=get("BRAINTRUST_API_BASE", DEFAULT_API_BASE),
        qwen_experiments=experiments,
        api_key=get("BRAINTRUST_API_KEY", ""),
        data_api_key=get("DATA_BRAINTRUST_KEY", ""),
    )
