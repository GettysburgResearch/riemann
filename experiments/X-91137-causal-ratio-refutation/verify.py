#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import isqrt
import json
import sys
from pathlib import Path

sys.set_int_max_str_digits(1_000_000)
DEN = 10**50
TERMS = 120


class I:
    def __init__(self, lo, hi=None):
        self.lo = Fraction(lo)
        self.hi = Fraction(lo if hi is None else hi)

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
        values = (self.lo * other.lo, self.lo * other.hi,
                  self.hi * other.lo, self.hi * other.hi)
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
    return value if isinstance(value, I) else I(value)


@lru_cache(maxsize=None)
def sqrt_i(value):
    value = Fraction(value)
    scaled = (value.numerator * DEN * DEN) // value.denominator
    lower = isqrt(scaled)
    exact = lower * lower * value.denominator == value.numerator * DEN * DEN
    upper = lower if exact else lower + 1
    return I(Fraction(lower, DEN), Fraction(upper, DEN))


@lru_cache(maxsize=None)
def log_i(value):
    value = Fraction(value)
    exponent = 0
    reduced = value
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    while reduced < 1:
        reduced *= 2
        exponent -= 1

    def base(z):
        z2 = z * z
        power = z
        partial = Fraction(0)
        for k in range(TERMS):
            partial += power / Fraction(2 * k + 1)
            power *= z2
        partial *= 2
        tail = 2 * power / (Fraction(2 * TERMS + 1) * (1 - z2))
        return I(partial, partial + tail)

    return base((reduced - 1) / (reduced + 1)) + exponent * base(Fraction(1, 3))


def invsqrt_i(n):
    return 1 / sqrt_i(Fraction(n))


def main():
    row = 66
    prime = 67
    z = Fraction(133, 2)
    parent = prime * z
    n_parent = parent.numerator // parent.denominator

    c = Fraction(2, row * (row - 1))
    a = Fraction(row + 2, row) * invsqrt_i(row)
    b = invsqrt_i(row + 1)

    h_lower = I(0)
    lower_boundary = I(0)
    for m in range(1, row):
        inv = invsqrt_i(m)
        h_lower += inv
        lower_boundary += inv * (log_i(parent) - log_i(Fraction(m)))

    lattice_lower = 4 * sqrt_i(parent) - 4 - 2 * log_i(parent)
    q_parent_lower = (
        c * lattice_lower - c * lower_boundary
        + a * (log_i(parent) - log_i(Fraction(row)))
        - b * (log_i(parent) - log_i(Fraction(row + 1)))
    ).lo

    harmonic_upper = 2 * sqrt_i(Fraction(n_parent)) - 1
    c_parent_upper = (c * harmonic_upper - c * h_lower + a - b).hi

    gamma = Fraction(row + 1, row - 1) * invsqrt_i(row)
    q_child = gamma * (log_i(z) - log_i(Fraction(row)))
    c_child = gamma
    r = 1 / sqrt_i(Fraction(prime))

    numerator_lower = (I(q_parent_lower) - r * q_child).lo
    derivative_upper = (I(c_parent_upper) - r * c_child).hi
    denominator_upper = ((5 * sqrt_i(parent) - 3)
                         - r * (5 * sqrt_i(z) - 3)).hi
    denominator_derivative_lower = (
        Fraction(5, 2) * sqrt_i(parent)
        - r * Fraction(5, 2) * sqrt_i(z)
    ).lo

    derivative_numerator_upper = (
        derivative_upper * denominator_upper
        - numerator_lower * denominator_derivative_lower
    )

    assert q_parent_lower > Fraction(968, 10_000)
    assert c_parent_upper < Fraction(596, 10_000)
    assert derivative_numerator_upper < Fraction(-152, 100)

    result = {
        "classification": "PASS_CAUSAL_RATIO_CONTINUOUS_MONOTONICITY_REFUTATION",
        "row": row,
        "p": prime,
        "z": str(z),
        "parent_endpoint": str(parent),
        "Q_parent_lower_decimal": float(q_parent_lower),
        "C_parent_upper_decimal": float(c_parent_upper),
        "log_derivative_numerator_upper_decimal": float(derivative_numerator_upper),
        "certified_below": "-1.52",
        "scope": "Exact rational interval arithmetic refutes continuous causal row-per-score monotonicity. It does not refute discrete divisor ordering or RH."
    }
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
