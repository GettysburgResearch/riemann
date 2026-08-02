#!/usr/bin/env python3
"""Compatibility wrapper for the offline archival capture utility."""

from pathlib import Path
import runpy

TARGET = Path(__file__).resolve().parents[2] / "internal" / "tools" / "capture_snapshot.py"
runpy.run_path(str(TARGET), run_name="__main__")
