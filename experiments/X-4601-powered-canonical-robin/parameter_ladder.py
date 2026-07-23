#!/usr/bin/env python3
"""Run fresh-process arithmetic replay rungs for a powered Robin certificate."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

RUNGS = [
    {"label": "deliberately-weak", "bits": 64, "log_terms": 8, "exp_terms": 8, "harmonic_cutoff": 100},
    {"label": "control-72", "bits": 72, "log_terms": 10, "exp_terms": 10, "harmonic_cutoff": 200},
    {"label": "control-96", "bits": 96, "log_terms": 16, "exp_terms": 16, "harmonic_cutoff": 1000},
    {"label": "control-128", "bits": 128, "log_terms": 32, "exp_terms": 32, "harmonic_cutoff": 10000},
    {"label": "production-160", "bits": 160, "log_terms": 56, "exp_terms": 56, "harmonic_cutoff": 30000},
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    probe = Path(__file__).with_name("parameter_probe.py")
    results = []
    for rung in RUNGS:
        command = [
            sys.executable,
            str(probe),
            args.certificate,
            "--bits",
            str(rung["bits"]),
            "--log-terms",
            str(rung["log_terms"]),
            "--exp-terms",
            str(rung["exp_terms"]),
            "--harmonic-cutoff",
            str(rung["harmonic_cutoff"]),
        ]
        completed = subprocess.run(command, capture_output=True, text=True, check=False)
        if not completed.stdout.strip():
            raise RuntimeError(f"probe produced no JSON: {completed.stderr}")
        payload = json.loads(completed.stdout)
        payload["label"] = rung["label"]
        payload["returncode"] = completed.returncode
        results.append(payload)

    output = {
        "schema": "riemann.robin.powered-canonical.parameter-ladder.v1",
        "certificate": args.certificate,
        "rungs": results,
        "proof_boundary": (
            "Each rung is a fresh-process replay of the same exact terminal stream. "
            "Rejection is fail-closed; acceptance proves only the stated finite region."
        ),
    }
    Path(args.output).write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
