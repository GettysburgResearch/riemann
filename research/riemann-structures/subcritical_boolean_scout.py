#!/usr/bin/env python3
"""Small deterministic Proth-certificate scout for the declared SCB windows.

This is a fixture search, not proof of the cofinal PNT assertion. All large
accepted primes carry the elementary Proth certificate proved in the note.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import isqrt

MAX_CANDIDATES = 5000
BASES = (3, 5, 7, 11, 13)
WINDOWS = {
    "A": (Fraction(101, 100), Fraction(51, 50), Fraction(1)),
    "B": (Fraction(1), Fraction(101, 100), Fraction(3, 4)),
    "ell": (Fraction(51, 50), Fraction(409, 400), Fraction(1, 4)),
    "rho": (Fraction(411, 400), Fraction(103, 100), Fraction(1, 4)),
    "p": (Fraction(3200, 4000), Fraction(3201, 4000), Fraction(1)),
    "q": (Fraction(4800, 4000), Fraction(4801, 4000), Fraction(1)),
    "r": (Fraction(3203, 4000), Fraction(3204, 4000), Fraction(1)),
    "s": (Fraction(4803, 4000), Fraction(4804, 4000), Fraction(1)),
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def trial_prime(n: int) -> bool:
    require(type(n) is int and 0 <= n < 100_000, "trial prime cap/type")
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def verify_proth(n: int, exponent: int, odd_part: int, witness: int) -> bool:
    require(
        all(type(x) is int for x in (n, exponent, odd_part, witness)),
        "certificate integer type",
    )
    require(2 <= exponent <= 32 and 1 <= odd_part < 2**exponent, "Proth range")
    require(odd_part % 2 == 1 and n == odd_part * 2**exponent + 1, "Proth form")
    require(1 < witness < n < 2**64, "witness/prime cap")
    return pow(witness, (n - 1) // 2, n) == n - 1


def prime_in_window(
    lo: Fraction, hi: Fraction, scale_exponent: int
) -> dict[str, int | str]:
    require(
        type(lo) is Fraction and type(hi) is Fraction and lo < hi, "exact open window"
    )
    require(type(scale_exponent) is int and 4 <= scale_exponent <= 60, "scale cap")
    if hi < 100_000:
        start = lo.numerator // lo.denominator + 1
        for count, n in enumerate(
            range(start, (hi.numerator - 1) // hi.denominator + 1), 1
        ):
            require(count <= MAX_CANDIDATES, "trial candidate cap")
            if trial_prime(n):
                return {
                    "prime": n,
                    "method": "EXACT_TRIAL_DIVISION",
                    "candidates": count,
                }
        raise ValueError("no small prime in this fixture window")
    exponent = scale_exponent // 2 + 1
    step = 2**exponent
    start = (lo.numerator - lo.denominator) // (lo.denominator * step) + 1
    if start % 2 == 0:
        start += 1
    for count in range(1, MAX_CANDIDATES + 1):
        odd_part = start + 2 * (count - 1)
        n = odd_part * step + 1
        if n >= hi:
            break
        require(lo < n, "open lower bound")
        require(odd_part < step, "Proth square-root hypothesis")
        for witness in BASES:
            if verify_proth(n, exponent, odd_part, witness):
                return {
                    "prime": n,
                    "method": "PROTH",
                    "exponent": exponent,
                    "odd_part": odd_part,
                    "witness": witness,
                    "candidates": count,
                }
    raise ValueError("no certified prime within bounded Proth search")


def scout(j: int) -> dict[str, object]:
    require(type(j) is int and 20 <= j <= 60 and j % 4 == 0, "dyadic fixture exponent")
    result = {"j": j, "U": 2**j, "prime_windows": {}}
    for label, (lower, upper, power) in WINDOWS.items():
        e = j * power
        require(e.denominator == 1, "integer source scale")
        exponent = int(e)
        lo, hi = lower * 2**exponent, upper * 2**exponent
        row = prime_in_window(lo, hi, exponent)
        row["lower"] = str(lo)
        row["upper"] = str(hi)
        result["prime_windows"][label] = row
    primes = [row["prime"] for row in result["prime_windows"].values()]
    require(len(set(primes)) == 8 and 67 not in primes, "physical label disjointness")
    return result


def main() -> None:
    results = []
    for j in (52, 56, 60):
        try:
            results.append(scout(j))
        except ValueError as error:
            results.append(
                {"j": j, "status": "NO_BOUNDED_FIXTURE", "reason": str(error)}
            )
    print(json.dumps({"status": "SCOUT_COMPLETE", "results": results}, indent=2))


if __name__ == "__main__":
    main()
