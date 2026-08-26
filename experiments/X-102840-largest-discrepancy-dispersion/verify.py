#!/usr/bin/env python3
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from pathlib import Path


def digest(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

    ramanujan_checks = 0
    max_error = 0.0
    for ell in primes:
        for N in range(ell, 10 * ell + 1, ell):
            for M in range(1, 3 * ell):
                if M % ell == 0:
                    continue
                total = sum(
                    cmath.exp(2j * math.pi * h * (N - M) / ell)
                    for h in range(1, ell)
                )
                error = abs(1 + total)
                max_error = max(max_error, error)
                assert error < 1e-10
                ramanujan_checks += 1

    phase_checks = 0
    max_ratio = 0.0
    max_arg = None
    root8 = math.sqrt(8.0)
    for ell in primes:
        for B in (1, 2, 3, 5, 8, 13, 21, 34, 55, 89):
            total = 0.0
            for b in range(B, 2 * B):
                for bp in range(B, 2 * B):
                    if not (1 / root8 < b / bp < root8):
                        continue
                    if (b * b - bp * bp) % ell == 0:
                        total += 1 / (b * bp)
            lhs = ell * total
            rhs = 1 + ell / B
            ratio = lhs / rhs
            if ratio > max_ratio:
                max_ratio = ratio
                max_arg = [ell, B, lhs, rhs]
            assert lhs <= 10 * rhs + 1e-12
            phase_checks += 1

    payload = {
        "schema": "riemann.t102840.additive-dispersion.v1",
        "ramanujan_nonzero_phase_checks": ramanujan_checks,
        "ramanujan_max_error": max_error,
        "square_core_phase_fixture_checks": phase_checks,
        "square_core_bound_constant_fixture": 10,
        "square_core_max_ratio": max_ratio,
        "square_core_max_ratio_arg": max_arg,
        "zero_phase_absent": True,
        "qdsp102840_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102840_LARGEST_DISCREPANCY_DISPERSION",
    }
    payload["proof_object_sha256"] = digest(payload)

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
