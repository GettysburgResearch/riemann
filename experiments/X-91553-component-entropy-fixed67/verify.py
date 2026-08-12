#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import isqrt
import json
import sys
from pathlib import Path

sys.set_int_max_str_digits(100000)


@dataclass(frozen=True)
class I:
    lo: Fraction
    hi: Fraction

    def __add__(self, other):
        other = as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_i(other))

    def __rsub__(self, other):
        return as_i(other) - self

    def __mul__(self, other):
        other = as_i(other)
        values = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return I(min(values), max(values))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_i(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return as_i(other) / self


def as_i(value):
    if isinstance(value, I):
        return value
    if not isinstance(value, Fraction):
        value = Fraction(value)
    return I(value, value)


DEN = 10**80


@lru_cache(maxsize=None)
def sqrt_q(value):
    value = Fraction(value)
    scaled = (value.numerator * DEN * DEN) // value.denominator
    root = isqrt(scaled)
    return I(Fraction(root, DEN), Fraction(root + 1, DEN))


@lru_cache(maxsize=None)
def log_q(value, terms: int = 220):
    value = Fraction(value)
    if value <= 0:
        raise ValueError("log argument must be positive")

    exponent = 0
    reduced = value
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    while reduced < 1:
        reduced *= 2
        exponent -= 1

    z = (reduced - 1) / (reduced + 1)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += power / Fraction(2 * j + 1)
        power *= z2
    tail = 2 * power / (Fraction(2 * terms + 1) * (1 - z2))
    log_reduced = I(2 * partial, 2 * partial + tail)
    if reduced == 1:
        log_reduced = I(Fraction(0), Fraction(0))

    z = Fraction(1, 3)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += power / Fraction(2 * j + 1)
        power *= z2
    tail = 2 * power / (Fraction(2 * terms + 1) * (1 - z2))
    log_two = I(2 * partial, 2 * partial + tail)

    return log_reduced + exponent * log_two


@lru_cache(maxsize=None)
def invsqrt(n: int):
    return 1 / sqrt_q(Fraction(n))


def entropy_at_integer(endpoint: int):
    total = I(Fraction(0), Fraction(0))
    for q in range(2, endpoint + 1):
        total += (
            log_q(Fraction(q))
            * invsqrt(q)
            * log_q(Fraction(endpoint, q))
        )
    return total


def certify():
    checks = 0

    entropy_67 = entropy_at_integer(67)
    base_margin = entropy_67 - 5 * (sqrt_q(Fraction(67)) - 1)
    assert base_margin.lo > 3
    checks += 1

    prefix = [I(Fraction(0), Fraction(0)) for _ in range(537)]
    running = I(Fraction(0), Fraction(0))
    for q in range(2, 537):
        running += log_q(Fraction(q)) * invsqrt(q)
        prefix[q] = running

    minimum = None
    for n in range(67, 536):
        child_floor = n // 67
        right = Fraction(n + 1)
        derivative = (
            prefix[n]
            - prefix[child_floor]
            - Fraction(5, 2)
            * (
                sqrt_q(right)
                - sqrt_q(Fraction(n + 1, 67))
            )
        )
        assert derivative.lo > 22
        checks += 1
        record = (derivative.lo, n, child_floor)
        if minimum is None or record[0] < minimum[0]:
            minimum = record

    result = {
        "classification": "PASS_COMPONENT_ENTROPY_FIXED67_DOMINATION",
        "checks": checks,
        "base_margin": {
            "lower_decimal": float(base_margin.lo),
            "certified_above": "3",
            "endpoint": 67,
        },
        "finite_cell_derivative_checks": 469,
        "minimum_derivative": {
            "lower_decimal": float(minimum[0]),
            "parent_cell_left": minimum[1],
            "child_floor": minimum[2],
            "certified_above": "22",
        },
        "analytic_tail": (
            "For Y>=536, integers in (Y/4,Y] give the elementary lower "
            "bound in L-91553.12."
        ),
        "scope": (
            "Exact Fraction arithmetic with directed rational square-root and "
            "logarithm enclosures. This certifies the finite interval part of "
            "the fixed-67 entropy-score domination, not native root-amplitude "
            "normalization or RH."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    certify()
