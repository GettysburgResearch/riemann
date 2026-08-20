#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import random
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T99722_OCE67_SCOPE_DIAGONAL_AND_PRIME_INTERVAL_FIREWALL"
PRIMES_100_200 = [
    101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
    157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
]


def canonical_digest(payload: dict[str, object]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def run() -> dict[str, object]:
    rng = random.Random(99722)
    convexity_checks = 0

    for _ in range(500):
        ar = Fraction(rng.randint(-30, 30), rng.randint(1, 30))
        ai = Fraction(rng.randint(-30, 30), rng.randint(1, 30))
        br = Fraction(rng.randint(-30, 30), rng.randint(1, 30))
        bi = Fraction(rng.randint(-30, 30), rng.randint(1, 30))
        r = Fraction(rng.randint(0, 100), 100)

        lhs = (ar - r * br) ** 2 + (ai - r * bi) ** 2
        rhs = (1 - r) * (ar * ar + ai * ai) + r * (
            (ar - br) ** 2 + (ai - bi) ** 2
        )
        assert rhs - lhs == r * (1 - r) * (br * br + bi * bi)
        assert lhs <= rhs
        convexity_checks += 1

    # Exact finite prime-interval separator at X=200.
    count = len(PRIMES_100_200)
    observation_square_lower = Fraction(count * count, 200)
    free_norm_square = Fraction(1)
    for p in PRIMES_100_200:
        free_norm_square *= Fraction(p + 1, p)

    assert count == 21
    assert free_norm_square < Fraction(6, 5)
    assert observation_square_lower / free_norm_square > Fraction(147, 80)

    # The compact-kernel diagonal estimate uses |K|<=3 and two disjoint
    # ratio-eight intervals.  The elementary harmonic bound is
    # sum_[a,8a] 1/n <= 1+log 8 < 10/3, hence 18(1+log8)<60.
    # Verify the rational comparison used after log(8)<7/3.
    diagonal_rational_upper = 18 * (Fraction(1) + Fraction(7, 3))
    assert diagonal_rational_upper == 60

    payload: dict[str, object] = {
        "schema": "riemann.x99722.oce67_cross_core.v1",
        "verdict": VERDICT,
        "base_pr": 660,
        "base_sha": "ca3c055307e6804ae904cb9105594dd3f2408ba3",
        "convexity_checks": convexity_checks,
        "compact_diagonal_bound": "<60",
        "finite_prime_interval": {
            "X": 200,
            "prime_count": count,
            "observation_square_lower": str(observation_square_lower),
            "free_norm_square_exact": str(free_norm_square),
            "free_norm_square_upper": "6/5",
            "squared_ratio_lower": "147/80",
        },
        "universal_branchwise_oce67": False,
        "source_orbit_oce67_proved": False,
        "cross_core_gram_proved": False,
        "rh_established": False,
    }
    payload["proof_object_sha256"] = canonical_digest(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = run()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
