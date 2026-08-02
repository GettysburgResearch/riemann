#!/usr/bin/env python3
"""Compatibility wrapper for the current front-door validator."""

from pathlib import Path
import runpy

TARGET = Path(__file__).resolve().parents[2] / "internal" / "tools" / "validate_front_door.py"
runpy.run_path(str(TARGET), run_name="__main__")
