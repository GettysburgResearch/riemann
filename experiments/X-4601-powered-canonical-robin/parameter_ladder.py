#!/usr/bin/env python3
"""Replay a powered Robin terminal stream under several exact parameter rungs."""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

from verify import Verifier, load_certificate

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

    certificate = load_certificate(args.certificate)
    results = []
    for rung in RUNGS:
        candidate = copy.deepcopy(certificate)
        candidate["parameters"] = {
            "bits": rung["bits"],
            "log_terms": rung["log_terms"],
            "exp_terms": rung["exp_terms"],
            "harmonic_cutoff": rung["harmonic_cutoff"],
        }
        try:
            replay = Verifier(candidate).replay()
            payload = {
                "accepted": True,
                "parameters": candidate["parameters"],
                "status": replay["status"],
                "counts": replay["counts"],
                "all_integer_normalized_ratio_upper": replay[
                    "all_integer_consequence"
                ]["normalized_ratio_upper"],
                "all_integer_normalized_ratio_upper_decimal_outward": replay[
                    "all_integer_consequence"
                ]["normalized_ratio_upper_decimal_outward"],
            }
        except Exception as exc:
            payload = {
                "accepted": False,
                "parameters": candidate["parameters"],
                "reason": f"{type(exc).__name__}: {exc}",
            }
        payload["label"] = rung["label"]
        results.append(payload)

    output = {
        "schema": "riemann.robin.powered-canonical.parameter-ladder.v1",
        "certificate": args.certificate,
        "rungs": results,
        "proof_boundary": (
            "Every rung replays the same exact terminal stream with replacement "
            "outward parameters. Rejection is fail-closed."
        ),
    }
    Path(args.output).write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
