#!/usr/bin/env python3
"""Replay one terminal certificate under a weak-to-strong parameter ladder."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
from typing import Sequence


RUNGS = [
    ("deliberately_weak_64", 64, 8, 8, 100),
    ("first_passing_72", 72, 10, 10, 200),
    ("control_96", 96, 16, 16, 1_000),
    ("control_160", 160, 56, 56, 30_000),
    ("production_256", 256, 88, 88, 250_000),
]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate")
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)

    results: list[dict[str, object]] = []
    probe = Path(__file__).with_name("parameter_probe.py")
    for label, bits, log_terms, exp_terms, cutoff in RUNGS:
        print(f"replaying {label}...", flush=True)
        completed = subprocess.run(
            [
                sys.executable,
                str(probe),
                args.certificate,
                "--label",
                label,
                "--bits",
                str(bits),
                "--log-terms",
                str(log_terms),
                "--exp-terms",
                str(exp_terms),
                "--harmonic-cutoff",
                str(cutoff),
            ],
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        lines = [line for line in completed.stdout.splitlines() if line.strip()]
        if len(lines) != 1:
            raise RuntimeError(f"unexpected probe output for {label}")
        results.append(json.loads(lines[0]))

    payload = {
        "schema": "riemann.robin.canonical-tree.parameter-ladder.v1",
        "certificate": args.certificate,
        "fresh_process_per_rung": True,
        "rungs": results,
        "interpretation": (
            "The weak rung must fail closed. Accepted stronger rungs must retain a "
            "strict all-integer normalized bound below one."
        ),
    }
    Path(args.output).write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
