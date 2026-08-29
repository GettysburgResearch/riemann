#!/usr/bin/env python3
"""Run all X-8455 reconnaissance scripts sequentially (or importable)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    ROOT / "comp1_windowed_scalar" / "run.py",
    ROOT / "comp2_five_notch" / "run.py",
    ROOT / "comp3_terminal_hankel" / "run.py",
    ROOT / "comp4_packet_floor" / "run.py",
    ROOT / "comp5_notch_moat" / "run.py",
]


def main() -> int:
    rc = 0
    for script in SCRIPTS:
        print(f"\n##### running {script.relative_to(ROOT)} #####\n")
        proc = subprocess.run([sys.executable, str(script)], cwd=str(ROOT))
        if proc.returncode != 0:
            rc = proc.returncode
            print(f"script failed: {script} rc={rc}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
