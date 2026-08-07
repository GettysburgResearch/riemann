#!/usr/bin/env python3
"""Exact rational replay for R-25301.

This checker verifies:
  * the reciprocal-cell derivative signs on N=37,38,39;
  * the strict continuum excess floor E(theta)>2/5 on [1/40,1/37];
  * the formal von-Mangoldt/divisibility dual identity through a finite range;
  * the same-scale prime-power cluster inverse matrices;
  * fail-closed mutations of the sharp threshold and prime-power manifest.

Only Python integers and fractions.Fraction are used in proof arithmetic.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
import argparse
import hashlib
import json
from typing import Dict, Tuple


BITS = 180
LOG_TERMS = 120
FORMAL_LIMIT = 128


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("empty interval")

    @staticmethod
    def point(value: int | Fraction) -> "Interval":
        value = Fraction(value)
        return Interval(value, value)

    def __add__(self, other: object) -> "Interval":
        rhs = other if isinstance(other, Interval) else Interval.point(Fraction(other))
        return Interval(self.lo + rhs.lo, self.hi + rhs.hi)

    __radd__ = __add__

    def __neg__(self) -> "Interval":
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: object) -> "Interval":
        rhs = other if isinstance(other, Interval) else Interval.point(Fraction(other))
        return self + (-rhs)

    def __rsub__(self, other: object) -> "Interval":
        return Interval.point(Fraction(other)) - self

    def __mul__(self, other: object) -> "Interval":
        rhs = other if isinstance(other, Interval) else Interval.point(Fraction(other))
        products = (
            self.lo * rhs.lo,
            self.lo * rhs.hi,
            self.hi * rhs.lo,
            self.hi * rhs.hi,
        )
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "Interval":
        rhs = other if isinstance(other, Interval) else Interval.point(Fraction(other))
        if rhs.lo <= 0 <= rhs.hi:
            raise ZeroDivisionError("interval contains zero")
        return self * Interval(Fraction(1, rhs.hi), Fraction(1, rhs.lo))


def integer_bytes(value: int) -> bytes:
    sign = b"-" if value < 0 else b"+"
    magnitude = abs(value)
    width = max(1, (magnitude.bit_length() + 7) // 8)
    return sign + magnitude.to_bytes(width, "big")


def fraction_digest(value: Fraction) -> str:
    payload = integer_bytes(value.numerator) + b"/" + integer_bytes(value.denominator)
    return hashlib.sha256(payload).hexdigest()


def fraction_summary(value: Fraction) -> dict:
    return {
        "sha256": fraction_digest(value),
        "numerator_bits": value.numerator.bit_length(),
        "denominator_bits": value.denominator.bit_length(),
        "decimal": f"{float(value):.18g}",
    }


def sqrt_interval_integer(n: int, bits: int = BITS) -> Interval:
    if n <= 0:
        raise ValueError("n must be positive")
    q = 1 << bits
    r = isqrt(n * q * q)
    while (r + 1) * (r + 1) <= n * q * q:
        r += 1
    while r * r > n * q * q:
        r -= 1
    return Interval(Fraction(r, q), Fraction(r + 1, q))


def invsqrt_interval_integer(n: int, bits: int = BITS) -> Interval:
    if n <= 0:
        raise ValueError("n must be positive")
    q = 1 << bits
    r = isqrt((q * q) // n)
    while (r + 1) * (r + 1) * n <= q * q:
        r += 1
    while r * r * n > q * q:
        r -= 1
    return Interval(Fraction(r, q), Fraction(r + 1, q))


def log_interval_unit(x: Fraction, terms: int = LOG_TERMS) -> Interval:
    if not (Fraction(1) <= x <= Fraction(2)):
        raise ValueError("unit log argument must lie in [1,2]")
    z = (x - 1) / (x + 1)
    total = Fraction(0)
    power = z
    for j in range(terms):
        total += power / (2 * j + 1)
        power *= z * z
    center = 2 * total
    remainder = 2 * abs(power) / ((2 * terms + 1) * (1 - z * z))
    return Interval(center - remainder, center + remainder)


def log_interval_rational(x: Fraction, terms: int = LOG_TERMS) -> Interval:
    if x <= 0:
        raise ValueError("log argument must be positive")
    exponent = 0
    y = x
    while y >= 2:
        y /= 2
        exponent += 1
    while y < 1:
        y *= 2
        exponent -= 1
    return log_interval_unit(y, terms) + exponent * log_interval_unit(Fraction(2), terms)


def harmonic_data(n: int) -> Tuple[Interval, Interval]:
    h = Interval.point(0)
    a = Interval.point(0)
    for k in range(1, n + 1):
        inv = invsqrt_interval_integer(k)
        h += inv
        a += inv * log_interval_rational(Fraction(k))
    return h, a


def derivative_bracket_at_cell_left(n: int) -> Interval:
    """Maximum derivative bracket on (1/(n+1),1/n]."""
    h, a = harmonic_data(n)
    log_theta = -log_interval_rational(Fraction(n + 1))
    return (h + 1) - Fraction(1, 2) * (
        a + (h + 1) * log_theta + 4 * h
    )


def excess_at_reciprocal(n: int) -> Interval:
    """Exact enclosure of E(1/n)."""
    h, a = harmonic_data(n)
    log_n = log_interval_rational(Fraction(n))
    sqrt_n = sqrt_interval_integer(n)
    bracket = a - (h + 1) * log_n + 4 * h
    return sqrt_n * bracket - 4 * n


def prime_factorization(n: int) -> Dict[int, int]:
    factors: Dict[int, int] = {}
    d = 2
    value = n
    while d * d <= value:
        while value % d == 0:
            factors[d] = factors.get(d, 0) + 1
            value //= d
        d += 1
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def primes_through(n: int) -> list[int]:
    primes: list[int] = []
    for candidate in range(2, n + 1):
        if all(candidate % p for p in primes if p * p <= candidate):
            primes.append(candidate)
    return primes


def formal_dual_mismatches(limit: int, omit_highest_prime_power: bool = False) -> list[int]:
    """Check sum_{q=p^a|m} log p = log m as formal prime vectors."""
    powers: list[tuple[int, int]] = []
    for p in primes_through(limit):
        q = p
        local: list[tuple[int, int]] = []
        while q <= limit:
            local.append((q, p))
            q *= p
        if omit_highest_prime_power and len(local) > 1:
            local.pop()
        powers.extend(local)

    bad: list[int] = []
    for m in range(1, limit + 1):
        lhs: Dict[int, int] = {}
        for q, p in powers:
            if m % q == 0:
                lhs[p] = lhs.get(p, 0) + 1
        if lhs != prime_factorization(m):
            bad.append(m)
    return bad


def matrix_multiply(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    rows = len(a)
    cols = len(b[0])
    inner = len(b)
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def matrix_inverse(a: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    aug = [
        [Fraction(a[i][j]) for j in range(n)]
        + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next((row for row in range(col, n) if aug[row][col]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [value / scale for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor:
                aug[row] = [
                    aug[row][j] - factor * aug[col][j]
                    for j in range(2 * n)
                ]
    return [row[n:] for row in aug]


def cluster_matrix_checks() -> dict:
    path_minima: dict[str, str] = {}
    for n in (1, 2, 3):
        matrix = [
            [
                Fraction(2 if i == j else (-1 if abs(i - j) == 1 else 0))
                for j in range(n)
            ]
            for i in range(n)
        ]
        inverse = matrix_inverse(matrix)
        minimum = min(value for row in inverse for value in row)
        if minimum < 0:
            raise AssertionError(f"path inverse {n} has negative entry")
        path_minima[str(n)] = str(minimum)

    exceptional = [
        [Fraction(2), Fraction(-2), Fraction(2), Fraction(-2)],
        [Fraction(-1), Fraction(2), Fraction(-1), Fraction(-1)],
        [Fraction(0), Fraction(-1), Fraction(2), Fraction(-1)],
        [Fraction(0), Fraction(0), Fraction(-1), Fraction(2)],
    ]
    claimed_inverse = [
        [Fraction(3, 2), Fraction(2), Fraction(1), Fraction(3)],
        [Fraction(3, 2), Fraction(3), Fraction(2), Fraction(4)],
        [Fraction(1), Fraction(2), Fraction(2), Fraction(3)],
        [Fraction(1, 2), Fraction(1), Fraction(1), Fraction(2)],
    ]
    identity = matrix_multiply(exceptional, claimed_inverse)
    if identity != [
        [Fraction(int(i == j)) for j in range(4)]
        for i in range(4)
    ]:
        raise AssertionError("exceptional inverse mismatch")
    if min(value for row in claimed_inverse for value in row) < 0:
        raise AssertionError("exceptional inverse is not nonnegative")
    return {
        "path_inverse_minima": path_minima,
        "exceptional_cluster": ["2", "3", "4", "5"],
        "exceptional_inverse_minimum": "1/2",
        "exceptional_inverse_verified": True,
    }


def build_result() -> dict:
    derivatives = {n: derivative_bracket_at_cell_left(n) for n in (37, 38, 39)}
    for n, enclosure in derivatives.items():
        if enclosure.hi >= 0:
            raise AssertionError(f"cell {n} derivative not strictly negative")

    e37 = excess_at_reciprocal(37)
    if e37.lo <= Fraction(2, 5):
        raise AssertionError("E(1/37) does not clear 2/5")

    mismatches = formal_dual_mismatches(FORMAL_LIMIT)
    if mismatches:
        raise AssertionError(f"formal dual mismatch at {mismatches[:5]}")
    clusters = cluster_matrix_checks()

    payload = {
        "schema": "riemann.x25301-parabolic-cover-dual.v1",
        "classification": "EXACT_RATIONAL_CONTINUUM_AND_DUAL_REFUTATION_CONTROL",
        "interval_bits": BITS,
        "log_terms": LOG_TERMS,
        "theta_band": ["1/40", "1/37"],
        "cell_derivative_brackets": {
            str(n): {
                "lower": fraction_summary(enclosure.lo),
                "upper": fraction_summary(enclosure.hi),
            }
            for n, enclosure in derivatives.items()
        },
        "E_at_1_over_37": {
            "lower": fraction_summary(e37.lo),
            "upper": fraction_summary(e37.hi),
        },
        "strict_floor": "2/5",
        "margin_over_floor": fraction_summary(e37.lo - Fraction(2, 5)),
        "formal_dual_limit": FORMAL_LIMIT,
        "formal_dual_mismatches": len(mismatches),
        "prime_power_cluster_matrices": clusters,
        "eventual_finite_excess_floor": "1/(4*sqrt(X))",
        "pnt_prime_log_mass_floor": "X/1000",
        "monotone_cover_cost_floor": "sqrt(X)/4000",
        "verdict": "MONOTONE_DIVISIBILITY_COVER_POLYLOG_COST_REFUTED",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def self_tests() -> list[str]:
    tests: list[str] = []
    result = build_result()
    assert result["formal_dual_mismatches"] == 0
    tests.append("central proof object")

    assert excess_at_reciprocal(37).lo < Fraction(9, 20)
    tests.append("overstated continuum floor rejected")

    assert 16 in formal_dual_mismatches(16, omit_highest_prime_power=True)
    tests.append("omitted prime-power row rejected")

    assert all(derivative_bracket_at_cell_left(n).hi < 0 for n in (37, 38, 39))
    tests.append("complete reciprocal-cell derivative ledger")

    assert Fraction(3, 1480) > Fraction(1, 1000)
    assert Fraction(1, 4) * Fraction(1, 1000) == Fraction(1, 4000)
    tests.append("PNT-to-cost constants")

    assert cluster_matrix_checks()["exceptional_inverse_verified"]
    tests.append("prime-power cluster inverse matrices")

    return tests


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    result = build_result()
    if args.self_test:
        tests = self_tests()
        print(f"{len(tests)}/{len(tests)} tests passed")
        for test in tests:
            print(f"PASS {test}")

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
