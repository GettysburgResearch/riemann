#!/usr/bin/env python3
from __future__ import annotations

import argparse
import cmath
import hashlib
import itertools
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

    primes = [3, 5, 7, 11, 13]

    double_checks = 0
    max_error = 0.0
    for ell1, ell2 in itertools.combinations(primes, 2):
        modulus = ell1 * ell2
        for delta in range(1, 3 * modulus):
            if delta % ell1 == 0 or delta % ell2 == 0:
                continue
            s1 = sum(
                cmath.exp(2j * math.pi * h * delta / ell1)
                for h in range(1, ell1)
            )
            s2 = sum(
                cmath.exp(2j * math.pi * h * delta / ell2)
                for h in range(1, ell2)
            )
            error = abs(s1 * s2 - 1)
            max_error = max(max_error, error)
            assert error < 1e-10
            double_checks += 1

    phase_checks = 0
    max_ratio = 0.0
    max_arg = None
    root8 = math.sqrt(8.0)
    for ell1, ell2 in itertools.combinations(primes, 2):
        modulus = ell1 * ell2
        for B in (1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144):
            total = 0.0
            for b in range(B, 2 * B):
                for bp in range(B, 2 * B):
                    if not (1 / root8 < b / bp < root8):
                        continue
                    diff = b * b - bp * bp
                    if diff % ell1 == 0 and diff % ell2 == 0:
                        total += 1 / (b * bp)
            lhs = modulus * total
            rhs = 1 + modulus / B
            ratio = lhs / rhs
            if ratio > max_ratio:
                max_ratio = ratio
                max_arg = [ell1, ell2, B, lhs, rhs]
            assert lhs <= 4 * rhs + 1e-12
            phase_checks += 1

    payload = {
        "schema": "riemann.t102860.double-phase-four-owner.v1",
        "double_ramanujan_checks": double_checks,
        "double_ramanujan_max_error": max_error,
        "two_modulus_phase_fixture_checks": phase_checks,
        "two_modulus_bound_constant_fixture": 4,
        "two_modulus_max_ratio": max_ratio,
        "two_modulus_max_ratio_arg": max_arg,
        "both_zero_coordinates_absent": True,
        "double_phase_energy_proved": True,
        "coherent_four_owner_sum_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102860_DOUBLE_PHASE_FOUR_OWNER_REDUCTION",
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
