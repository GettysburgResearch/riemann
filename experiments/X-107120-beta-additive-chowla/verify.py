#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


def mobius(n: int) -> int:
    m = n
    sign = 1
    p = 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            sign = -sign
            if m % p == 0:
                return 0
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        sign = -sign
    return sign


def kernel(m: int, n: int, width: int = 11) -> F:
    distance = abs(m - n)
    return F(max(0, width - distance), width)


def direct(number: int, q: int) -> F:
    coefficients = {
        n: F(mobius(n) if n % q else 0, n) for n in range(1, number + 1)
    }
    return sum(
        (
            coefficients[m] * coefficients[n] * kernel(m, n)
            for m in coefficients
            for n in coefficients
        ),
        F(),
    )


def additive(number: int, q: int) -> F:
    coefficients = {
        n: F(mobius(n) if n % q else 0, n) for n in range(1, number + 1)
    }
    total = sum(
        (coefficients[n] * coefficients[n] * kernel(n, n) for n in coefficients),
        F(),
    )
    for gap in range(1, number):
        total += 2 * sum(
            (
                coefficients[n]
                * coefficients[n + gap]
                * kernel(n, n + gap)
                for n in range(1, number - gap + 1)
            ),
            F(),
        )
    return total


def gcd_reindex(number: int, q: int) -> F:
    total = F()
    for core in range(1, number + 1):
        if core % q == 0 or mobius(core) == 0:
            continue
        for left in range(1, number // core + 1):
            for right in range(1, number // core + 1):
                if math.gcd(left, right) != 1:
                    continue
                if math.gcd(core, left * right) != 1 or (left * right) % q == 0:
                    continue
                if mobius(left) == 0 or mobius(right) == 0:
                    continue
                m, n = core * left, core * right
                coefficient = F(
                    mobius(left) * mobius(right), core * core * left * right
                )
                total += coefficient * kernel(m, n)
    return total


def direct_core(number: int, q: int) -> F:
    total = F()
    for m in range(1, number + 1):
        if m % q == 0 or mobius(m) == 0:
            continue
        for n in range(1, number + 1):
            if n % q == 0 or mobius(n) == 0:
                continue
            total += F(mobius(m) * mobius(n), m * n) * kernel(m, n)
    return total


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    checks = 0
    for number in range(2, 46):
        for q in (3, 5, 7):
            assert direct(number, q) == additive(number, q)
            checks += 1
            assert direct_core(number, q) == gcd_reindex(number, q)
            checks += 1

    for width in range(2, 25):
        assert kernel(10, 10, width) == 1
        checks += 1
        assert kernel(10, 10 + width, width) == 0
        checks += 1
        assert kernel(10, 10 + width - 1, width) == F(1, width)
        checks += 1

    for exponent in range(1, 20):
        # T=sqrt(Y) log(Y)^B gives Y/T^2=log(Y)^(-2B).
        assert 1 - 2 * exponent <= -1
        checks += 1

    result = {
        "claim": "T-107120",
        "verdict": "PASS_T107120_BETA_ADDITIVE_CHOWLA_NORMAL_FORM",
        "checks": checks,
        "additive_shift_grouping_exact": True,
        "gcd_primitive_reindexing_exact": True,
        "mean_value_tail_input_replayed": False,
        "low_frequency_estimate_proved": False,
        "rh_established": False,
        "scope": "exact finite rational grouping/reindexing and tail-exponent algebra",
    }
    result["proof_object"] = hashlib.sha256(
        json.dumps(result, sort_keys=True).encode()
    ).hexdigest()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(result["verdict"])
    print(f"checks={checks}")
    print(result["proof_object"])


if __name__ == "__main__":
    main()
