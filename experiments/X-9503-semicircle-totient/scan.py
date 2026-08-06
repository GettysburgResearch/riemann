#!/usr/bin/env python3
"""Ordinary-floating reconnaissance for T-9501.

The totient sieve is exact integer arithmetic. Square roots, summation, pi, and
the final scaled error are ordinary binary64 and are NOT proof-grade.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

DEFAULT_CUTOFFS = [
    100,
    200,
    500,
    1_000,
    2_000,
    5_000,
    10_000,
    20_000,
    50_000,
    100_000,
    200_000,
    500_000,
    1_000_000,
    2_000_000,
]


def phi_sieve(limit: int) -> list[int]:
    if limit < 2:
        raise ValueError("limit must be at least two")
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for multiple in range(p, limit + 1, p):
                phi[multiple] -= phi[multiple] // p
    return phi


def observable(phi: list[int], x: int) -> dict[str, float | int]:
    if not 2 <= x < len(phi):
        raise ValueError("x is outside the totient table")
    terms = (
        (phi[n] / n) * math.sqrt(1.0 - (n / x) ** 2)
        for n in range(1, x)
    )
    value = (2.0 / x) * math.fsum(terms)
    error = value - 3.0 / math.pi
    return {
        "x": x,
        "semicircle_totient_value": value,
        "error_from_3_over_pi": error,
        "scaled_x_3_over_2_error": error * x**1.5,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cutoffs", nargs="*", type=int, default=DEFAULT_CUTOFFS)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cutoffs = sorted(set(args.cutoffs))
    if not cutoffs or cutoffs[0] < 2:
        parser.error("all cutoffs must be at least two")

    started = time.perf_counter()
    phi = phi_sieve(max(cutoffs))
    rows = [observable(phi, x) for x in cutoffs]
    payload = {
        "schema": "riemann.semicircle-totient-reconnaissance.v1",
        "experiment_id": "X-9503",
        "status": "EMPIRICAL_BINARY64_NOT_CERTIFIED",
        "theorem_target": "T-9501",
        "cutoffs": cutoffs,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "proof_boundary": (
            "phi(n) is exact, but square roots, pi, fsum, subtraction, and "
            "scaled errors are ordinary binary64. No row certifies an RH bound."
        ),
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
