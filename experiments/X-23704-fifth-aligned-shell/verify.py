#!/usr/bin/env python3
"""Exact rational-interval replay for L-23710.

Arithmetic class: EXACT_INTEGER_AND_RATIONAL_INTERVAL.
No floating-point operation enters the verdict.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt

NMAX = 100
DIGITS = 70
SERIES_TERMS = 110


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @staticmethod
    def point(x: int | Fraction) -> "Interval":
        q = Fraction(x)
        return Interval(q, q)

    def __add__(self, other: int | Fraction | "Interval") -> "Interval":
        o = other if isinstance(other, Interval) else Interval.point(other)
        return Interval(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self) -> "Interval":
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: int | Fraction | "Interval") -> "Interval":
        o = other if isinstance(other, Interval) else Interval.point(other)
        return self + (-o)

    def __rsub__(self, other: int | Fraction | "Interval") -> "Interval":
        o = other if isinstance(other, Interval) else Interval.point(other)
        return o - self

    def __mul__(self, other: int | Fraction | "Interval") -> "Interval":
        o = other if isinstance(other, Interval) else Interval.point(other)
        values = (
            self.lo * o.lo,
            self.lo * o.hi,
            self.hi * o.lo,
            self.hi * o.hi,
        )
        return Interval(min(values), max(values))

    __rmul__ = __mul__

    def reciprocal(self) -> "Interval":
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        values = (1 / self.lo, 1 / self.hi)
        return Interval(min(values), max(values))

    def __truediv__(self, other: int | Fraction | "Interval") -> "Interval":
        o = other if isinstance(other, Interval) else Interval.point(other)
        return self * o.reciprocal()


def sqrt_integer(n: int) -> Interval:
    if n <= 0:
        raise ValueError("sqrt input must be positive")
    scale = 10**DIGITS
    target = n * scale * scale
    root = isqrt(target)
    lower = Fraction(root, scale)
    if root * root == target:
        return Interval(lower, lower)
    return Interval(lower, Fraction(root + 1, scale))


def _atanh_log(u: Fraction) -> Interval:
    """Outward bracket for log(u), assuming 1 <= u <= 2."""
    if not (1 <= u <= 2):
        raise ValueError("atanh log argument outside [1,2]")
    z = (u - 1) / (u + 1)
    total = Fraction(0)
    power = z
    for j in range(SERIES_TERMS):
        total += 2 * power / (2 * j + 1)
        power *= z * z
    remainder = 2 * power / ((2 * SERIES_TERMS + 1) * (1 - z * z))
    return Interval(total, total + remainder)


def log_rational(x: Fraction) -> Interval:
    if x <= 0:
        raise ValueError("log input must be positive")
    exponent = 0
    unit = x
    while unit >= 2:
        unit /= 2
        exponent += 1
    while unit < 1:
        unit *= 2
        exponent -= 1
    log_unit = _atanh_log(unit)
    log_two = _atanh_log(Fraction(2))
    return log_unit + exponent * log_two


def mobius_values(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    least = [0] * (limit + 1)
    primes: list[int] = []
    mu[1] = 1
    for n in range(2, limit + 1):
        if least[n] == 0:
            least[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if p > least[n] or n * p > limit:
                break
            least[n * p] = p
            mu[n * p] = 0 if p == least[n] else -mu[n]
    return mu


def run() -> dict[str, object]:
    mu = mobius_values(NMAX)
    b5 = [0] * (NMAX + 1)
    for n in range(1, NMAX + 1):
        b5[n] = mu[n] - (mu[n // 5] if n % 5 == 0 else 0)

    a_sum = Fraction(0)
    b_sum = Interval.point(0)
    c_sum = Interval.point(0)
    endpoints: dict[int, Interval] = {}
    cell_classes: dict[str, int] = {
        "increasing": 0,
        "A_nonpositive_no_interior_minimum": 0,
        "decreasing": 0,
    }

    for n in range(1, NMAX + 1):
        coefficient = b5[n]
        root = sqrt_integer(n)
        inv_root = root.reciprocal()
        log_n = Interval.point(0) if n == 1 else log_rational(Fraction(n))

        a_sum += Fraction(coefficient, n)
        b_sum += coefficient * inv_root
        c_sum += coefficient * (log_n * inv_root)

        value = (
            4 * root * Interval.point(a_sum)
            - (4 + log_n) * b_sum
            + c_sum
        )
        endpoints[n] = value

        if n == NMAX:
            continue

        if a_sum <= 0:
            # 2*A*sqrt(y)-B is nonincreasing. A critical point can only be a
            # maximum, so the cell minimum is attained at an endpoint.
            cell_classes["A_nonpositive_no_interior_minimum"] += 1
            continue

        left = 2 * Interval.point(a_sum) * sqrt_integer(n) - b_sum
        right = 2 * Interval.point(a_sum) * sqrt_integer(n + 1) - b_sum
        if left.lo >= 0:
            cell_classes["increasing"] += 1
        elif right.hi <= 0:
            cell_classes["decreasing"] += 1
        else:
            raise AssertionError(
                f"unresolved negative-to-positive derivative crossing in cell {n}"
            )

    if endpoints[1].lo != 0 or endpoints[1].hi != 0:
        raise AssertionError("the y=1 endpoint must be exactly zero")

    rational_floor = Fraction(9637, 10000)
    minimum_index = -1
    minimum_lower: Fraction | None = None
    for n in range(2, NMAX + 1):
        lower = endpoints[n].lo
        if lower <= rational_floor:
            raise AssertionError(f"endpoint {n} is not above the retained floor")
        if minimum_lower is None or lower < minimum_lower:
            minimum_lower = lower
            minimum_index = n

    if sum(cell_classes.values()) != NMAX - 1:
        raise AssertionError("not every cell was classified")

    return {
        "classification": "EXACT_FIFTH_ALIGNED_SHELL_ANNULUS_VERIFIED",
        "annulus": [1, NMAX],
        "endpoint_one": "0",
        "strict_endpoint_floor_for_N_ge_2": "9637/10000",
        "minimum_endpoint_index": minimum_index,
        "cell_classes": cell_classes,
        "unresolved_cells": 0,
        "arithmetic": "integers + fractions.Fraction outward intervals",
        "floating_point_used_in_verdict": False,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
