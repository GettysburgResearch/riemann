#!/usr/bin/env python3
"""Exact shared-parameter and Lagarias endpoint certificate for 55440, 720720."""

import argparse
import json
from fractions import Fraction
from math import isqrt, prod
from pathlib import Path

from lagarias_compact_integer import BITS, I, S


PIVOT = 13
FIRST_EXCLUDED = 17
LOWER_EXPONENTS = {2: 4, 3: 2, 5: 1, 7: 1, 11: 1, PIVOT: 0}
RESULT = Path(__file__).resolve().parents[1] / "results" / "lagarias_latest62_ca.json"


def is_prime(n):
    return n >= 2 and all(n % d != 0 for d in range(2, isqrt(n) + 1))


def prime_increment(p, k):
    """An outward interval for the crossing from exponent k-1 to k."""
    assert k >= 1
    ratio = Fraction(p ** (k + 1) - 1, p * (p**k - 1))
    return I(ratio).log() / I(p).log()


def product_and_sigma(exponents):
    return (
        prod(p**k for p, k in exponents.items()),
        prod((p ** (k + 1) - 1) // (p - 1) for p, k in exponents.items()),
    )


def endpoint(exponents, harmonic_bounds):
    n, sigma = product_and_sigma(exponents)
    low, high = harmonic_bounds[n]
    h = I(low, high, raw=True)
    b = h + h.exp() * h.log()
    gap_lower = b.lo - sigma * S
    assert gap_lower > 0, (n, gap_lower)
    return {
        "n": n,
        "prime_exponents": exponents,
        "sigma": sigma,
        "harmonic_scaled_interval": [h.lo, h.hi],
        "lagarias_rhs_scaled_interval": [b.lo, b.hi],
        "gap_lower_scaled": gap_lower,
        "integer_part_of_gap_lower": gap_lower // S,
    }


def certify():
    small_primes = [n for n in range(2, FIRST_EXCLUDED) if is_prime(n)]
    assert small_primes == list(LOWER_EXPONENTS)
    assert is_prime(FIRST_EXCLUDED)

    epsilon = prime_increment(PIVOT, 1)
    assert epsilon.lo > 0
    rows = []
    for p, k in LOWER_EXPONENTS.items():
        if p == PIVOT:
            next_threshold = prime_increment(p, 2)
            assert epsilon.lo > next_threshold.hi
            rows.append({
                "prime": p,
                "maximizing_exponents": [0, 1],
                "tie": "epsilon is defined by the exact p=13, k=1 threshold",
                "epsilon_minus_threshold_k2_lower_scaled": epsilon.lo - next_threshold.hi,
            })
            continue

        last = prime_increment(p, k)
        next_threshold = prime_increment(p, k + 1)
        assert last.lo > epsilon.hi, (p, k, last.lo, epsilon.hi)
        assert epsilon.lo > next_threshold.hi, (p, k + 1, epsilon.lo, next_threshold.hi)
        rows.append({
            "prime": p,
            "maximizing_exponents": [k],
            "threshold_k_minus_epsilon_lower_scaled": last.lo - epsilon.hi,
            "epsilon_minus_threshold_kplus1_lower_scaled": epsilon.lo - next_threshold.hi,
        })

    excluded = prime_increment(FIRST_EXCLUDED, 1)
    assert epsilon.lo > excluded.hi
    upper_exponents = LOWER_EXPONENTS | {PIVOT: 1}
    lower, _ = product_and_sigma(LOWER_EXPONENTS)
    upper, _ = product_and_sigma(upper_exponents)
    assert (lower, upper) == (55440, 720720)

    # Each reciprocal contributes a rounding error in [0, 1/S).
    harmonic_lower = 0
    harmonic_bounds = {}
    for n in range(1, upper + 1):
        harmonic_lower += S // n
        if n in (lower, upper):
            harmonic_bounds[n] = (harmonic_lower, harmonic_lower + n)

    return {
        "scale": S,
        "precision_bits": BITS,
        "epsilon_exact": "log(14/13) / log(13)",
        "epsilon_scaled_interval": [epsilon.lo, epsilon.hi],
        "prime_thresholds": rows,
        "exclusion": {
            "first_prime": FIRST_EXCLUDED,
            "epsilon_minus_first_threshold_lower_scaled": epsilon.lo - excluded.hi,
        },
        "endpoints": [
            endpoint(LOWER_EXPONENTS, harmonic_bounds),
            endpoint(upper_exponents, harmonic_bounds),
        ],
        "closed_interval": [lower, upper],
        "integer_count": upper - lower + 1,
        "requires_concavity_input": "proposals/independent_campaigns/lagarias_global_concavity_round2.md",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the recomputed certificate")
    args = parser.parse_args()
    if not __debug__:
        raise RuntimeError("certificate checks require Python assertions")
    result = certify()
    if args.write:
        RESULT.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert json.loads(json.dumps(result)) == json.loads(RESULT.read_text())
    print(f"Certified shared support and two endpoints, covering {result['integer_count']} integers by concavity")


if __name__ == "__main__":
    main()
