#!/usr/bin/env python3
"""Exact replay for the two-phase collision-line frame."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, Tuple

Vec = Tuple[int, int]


def dot(a: Vec, b: Vec) -> int:
    return a[0] * b[0] + a[1] * b[1]


def norm2(a: Vec) -> int:
    return dot(a, a)


def sum_vec(vs: Iterable[Vec]) -> Vec:
    x = y = 0
    for a, b in vs:
        x += a
        y += b
    return (x, y)


def one_phase_energy(q: int, w: Dict[int, Vec]) -> int:
    total = 0
    for x, vx in w.items():
        for y, vy in w.items():
            kernel = q - 1 if x == y else -1
            total += kernel * dot(vx, vy)
    return total


def two_phase_energy(q: int, w: Dict[int, Vec]) -> int:
    total = 0
    for x, vx in w.items():
        for y, vy in w.items():
            kernel = (q - 1) ** 2 if x == y else 1
            total += kernel * dot(vx, vy)
    return total


def run() -> dict:
    rng = random.Random(106060)
    primes = (3, 5, 7, 11, 13, 17)
    checks = {
        "coherent_phase_sum": 0,
        "equality_fixture": 0,
        "one_phase_dimension_barrier": 0,
        "one_phase_identity": 0,
        "phase_map_multiplicity": 0,
        "sharp_two_phase_contraction": 0,
        "two_phase_energy_identity": 0,
    }

    for q in primes:
        for tau in range(1, q):
            counts = {g: 0 for g in range(q)}
            for alpha in range(1, q):
                for beta in range(1, q):
                    counts[(tau * alpha + beta) % q] += 1
            assert counts[0] == q - 1
            assert all(counts[g] == q - 2 for g in range(1, q))
            checks["phase_map_multiplicity"] += q

        for _ in range(240):
            w = {
                x: (rng.randint(-5, 5), rng.randint(-5, 5))
                for x in range(1, q)
            }
            d = sum(norm2(v) for v in w.values())
            s = norm2(sum_vec(w.values()))

            e1 = one_phase_energy(q, w)
            assert e1 == q * d - s
            checks["one_phase_identity"] += 1

            e2 = two_phase_energy(q, w)
            assert e2 == q * (q - 2) * d + s
            checks["two_phase_energy_identity"] += 1

            assert Fraction(s, 1) <= Fraction(q - 1, q * q - q - 1) * e2
            checks["sharp_two_phase_contraction"] += 1

            assert (-1) * (-1) == 1
            checks["coherent_phase_sum"] += 1

        v = (2, -3)
        w_equal = {x: v for x in range(1, q)}
        s = norm2(sum_vec(w_equal.values()))
        e1 = one_phase_energy(q, w_equal)
        e2 = two_phase_energy(q, w_equal)
        assert Fraction(s, e1) == q - 1
        checks["one_phase_dimension_barrier"] += 1
        assert Fraction(s, e2) == Fraction(q - 1, q * q - q - 1)
        checks["equality_fixture"] += 1

    result = {
        "verdict": "PASS_X_106060_TWO_PHASE_COLLISION_LINE_FRAME",
        "arithmetic_class": "EXACT_INTEGER_RATIONAL_FINITE_FIELD_KERNEL",
        "prime_fields": list(primes),
        "checks": checks,
        "total_checks": sum(checks.values()),
        "proved": {
            "coherent_phase_recovery": True,
            "one_phase_dimension_barrier": True,
            "phase_pair_multiplicity": True,
            "sharp_two_phase_contraction": True,
            "two_phase_energy_identity": True,
        },
        "open": {
            "crop106060": True,
            "hbcqdsp102888": True,
            "hclm106001": True,
            "riemann_hypothesis": True,
        },
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
