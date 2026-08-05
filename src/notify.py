"""Local completion notification sounds (macOS).

Synthesizes retro "Mario-style" jingles with numpy and plays them through
``afplay`` so a long-running job can announce itself when it finishes. Pure
Python — no external audio package or asset files required.

Sound selection:
- ``play_success()`` — rising C-major power-up arpeggio (Super Mario Bros.
  mushroom/power-up style), for successful completion.
- ``play_failure()`` — slow descending game-over motif, for abandoned runs.

If playback fails (no ``afplay``), falls back to a terminal beep via AppleScript.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import wave

try:
    import numpy as np
except ImportError:  # pragma: no cover - numpy is a hard dependency of the repo
    np = None

SAMPLE_RATE = 44100

# Note frequencies (Hz), scientific pitch notation.
NOTES = {
    "A3": 220.00, "B3": 246.94, "C4": 261.63, "D4": 293.66, "E4": 329.63,
    "F4": 349.23, "G4": 392.00, "A4": 440.00, "B4": 493.88, "C5": 523.25,
    "D5": 587.33, "E5": 659.25, "F5": 698.46, "G5": 783.99, "A5": 880.00,
    "B5": 987.77, "C6": 1046.50, "D6": 1174.66, "E6": 1318.51, "F6": 1396.91,
    "G6": 1567.98, "A6": 1760.00, "B6": 1975.53, "C7": 2093.00, "E7": 2637.02,
    "G7": 3135.96,
}

# Mario power-up arpeggio: short rising notes then a held top note.
SUCCESS_SEQUENCE = [
    ("C5", 0.09), ("E5", 0.09), ("G5", 0.09), ("C6", 0.09),
    ("E6", 0.09), ("G6", 0.09), ("C7", 0.09), ("C7", 0.55),
]

# Slow descending game-over motif.
FAILURE_SEQUENCE = [
    ("E5", 0.30), ("C5", 0.30), ("A4", 0.30), ("F4", 0.55),
]


def _tone(freq: float, duration: float, amplitude: float = 0.30) -> np.ndarray:
    """One note with a rounded (square-ish) retro tone and soft envelopes."""
    n = int(SAMPLE_RATE * duration)
    if n == 0:
        return np.array([], dtype=np.float64)
    t = np.arange(n) / SAMPLE_RATE
    # Odd harmonics at 1/k amplitudes give a warm square-wave timbre.
    tone = (
        np.sin(2 * np.pi * freq * t)
        + 0.5 * np.sin(2 * np.pi * 2 * freq * t)
        + (1.0 / 3.0) * np.sin(2 * np.pi * 3 * freq * t)
    )
    tone *= amplitude
    # 5 ms attack and 25 ms release to avoid clicks.
    attack = min(8, n)
    release = min(25, max(0, n - attack))
    envelope = np.ones(n)
    envelope[:attack] = np.linspace(0, 1, attack)
    if release > 0:
        envelope[-release:] *= np.linspace(1, 0, release)
    return tone * envelope


def _sequence_to_samples(sequence: list[tuple[str, float]]) -> np.ndarray:
    parts = [_tone(NOTES[name], duration) for name, duration in sequence]
    gap = int(SAMPLE_RATE * 0.01)  # 10 ms gap between notes
    silence = np.zeros(gap)
    with_gaps: list[np.ndarray] = []
    for part in parts:
        with_gaps.extend([part, silence])
    return np.concatenate(with_gaps)


def _write_wav(samples: np.ndarray, path: str) -> None:
    pcm = (np.clip(samples, -1.0, 1.0) * 32767).astype(np.int16)
    with wave.open(path, "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)
        wav.writeframes(pcm.tobytes())


def _play(samples: np.ndarray) -> None:
    if np is None:
        return
    try:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            _write_wav(samples, tmp.name)
            path = tmp.name
        if shutil.which("afplay"):
            subprocess.run(["afplay", path], check=True)
        else:  # pragma: no cover - non-macOS fallback
            subprocess.run(["osascript", "-e", "beep"], check=True)
    finally:
        try:
            os.unlink(path)
        except OSError:
            pass


def play_success() -> None:
    """Play a Mario power-up style jingle for a successful completion."""
    try:
        _play(_sequence_to_samples(SUCCESS_SEQUENCE))
    except Exception as exc:  # pragma: no cover - never crash the caller
        print(f"warning: could not play success sound: {exc}", file=__import__("sys").stderr)


def play_failure() -> None:
    """Play a descending game-over motif for an abandoned run."""
    try:
        _play(_sequence_to_samples(FAILURE_SEQUENCE))
    except Exception as exc:  # pragma: no cover - never crash the caller
        print(f"warning: could not play failure sound: {exc}", file=__import__("sys").stderr)


if __name__ == "__main__":
    # Quick self-test: play the success jingle and exit.
    play_success()
