from __future__ import annotations

from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_ROOT.parent
LFR_ROOT = PROJECT_ROOT
DATA_DIR = LFR_ROOT / "lfr_pipeline" / "data"
OUTPUT_DIR = LFR_ROOT / "output"

__all__ = [
    "PACKAGE_ROOT",
    "PROJECT_ROOT",
    "LFR_ROOT",
    "DATA_DIR",
    "OUTPUT_DIR",
]
