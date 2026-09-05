#!/usr/bin/env python3
"""Compatibility entrypoint; original pass-2 validator is archived verbatim."""
from pathlib import Path
import runpy
if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parents[1] / "validate_final.py"), run_name="__main__")
