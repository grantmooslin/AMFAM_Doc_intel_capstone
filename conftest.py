"""Pytest configuration: ensure the project root is importable as a package root."""

import sys
from pathlib import Path

# Use a non-interactive matplotlib backend so plotting code runs headless.
import matplotlib

matplotlib.use("Agg")

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
