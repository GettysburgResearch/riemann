#!/usr/bin/env python3
"""Replay one terminal stream at several arithmetic strengths.

Each rung runs in a fresh process. A rung passes only if every stored terminal
is reconstructed with the same strict mathematical classification.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict
import json
from pathlib import Path
import subprocess
import sys
from typing import Sequence

from certmath import RobinParameters

RUNGS = [
    ("deliberately_weak_64", RobinParameters(64, 8, 8, 100)),
    ("first_passing_72", RobinParameters(72, 10, 10, 200)),
    ("control_96", RobinParameters(96, 16, 16, 1_000)),
    ("control_160", RobinParameters(160, 56, 56, 30_000)),
    ("production_256", RobinParameters(256, 88, 88, 250_000)),
]


def run_ladder(certificate_path: Path) -> dict[str, object]:
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    results: list[dict[str, object]] = []
    probe = Path(__file__).with_name("parameter_probe.py")
    for label, params in RUNGS:
        print(f"replaying {label}...", flush=True)
        completed = subprocess.run(
            [
                sys.executable,
                str(probe),
                str(certificate_path),
                "--label",
                label,
                "--bits",
                str(params.bits),
                "--log-terms",
                str(params.log_terms),
                "--exp-terms",
                str(params.exp_terms),
                "--harmonic-cutoff",
                str(params.harmonic_cutoff),
            ],
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        results.append(json.loads(completed.stdout))
    return {
        "schema": "riemann.robin.canonical-tree.parameter-ladder.v1",
        "certificate_sha256": certificate["certificate_sha256"],
        "finite_region": certificate["finite_region"],
        "rungs": results,
        "acceptance_rule": (
            "every stored terminal must be reconstructed with the same strict "
            "classification; the first unsupported prune or leaf rejects the rung"
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate")
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    result = run_ladder(Path(args.certificate))
    Path(args.output).write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
