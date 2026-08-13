#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import isqrt
import json
import sys
from pathlib import Path

sys.set_int_max_str_digits(1000000)

DEN = 10**70
X = 4690
R = 67
S = 71


class Interval:
    def __init__(self, lo: Fraction, hi: Fraction):
        self.lo = lo
        self.hi = hi

    def __add__(self, other):
        if not isinstance(other, Interval):
            other = Interval(Fraction(other), Fraction(other))
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, Interval):
            other = Interval(Fraction(other), Fraction(other))
        values = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return Interval(min(values), max(values))

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, Interval):
            other = Interval(Fraction(other), Fraction(other))
        assert not (other.lo <= 0 <= other.hi)
        return self * Interval(1 / other.hi, 1 / other.lo)


def sqrt_interval(value: Fraction) -> Interval:
    value = Fraction(value)
    scaled = value.numerator * DEN * DEN // value.denominator
    lower = isqrt(scaled)
    return Interval(Fraction(lower, DEN), Fraction(lower + 1, DEN))


def inverse_sqrt_interval(value: int) -> Interval:
    root = sqrt_interval(Fraction(value))
    return Interval(1 / root.hi, 1 / root.lo)


def prefix_intervals(limit: int) -> list[Interval]:
    values = [Interval(Fraction(0), Fraction(0))]
    for n in range(1, limit + 1):
        values.append(values[-1] + inverse_sqrt_interval(n))
    return values


def endpoint_port(value: Fraction, prefixes: list[Interval]) -> Interval:
    value = Fraction(value)
    if value < 1:
        return Interval(Fraction(0), Fraction(0))
    n = value.numerator // value.denominator
    numerator = Interval(Fraction(2 * n), Fraction(2 * n))
    return numerator / sqrt_interval(value) - prefixes[n]


def verify() -> dict:
    prefixes = prefix_intervals(X)
    mixed = (
        endpoint_port(Fraction(X), prefixes)
        - endpoint_port(Fraction(X, R), prefixes)
        - endpoint_port(Fraction(X, S), prefixes)
        + endpoint_port(Fraction(X, R * S), prefixes)
    )

    assert mixed.hi < Fraction(-133, 100)
    assert X // R == 70
    assert X // S == 66
    assert Fraction(X, R * S) < 1

    return {
        "classification": "PASS_ROUGH_PORT_NON_TENSORIZATION_COUNTEREXAMPLE",
        "scales": [R, S],
        "x": X,
        "floors": {
            "x_over_67": X // R,
            "x_over_71": X // S,
            "x_over_product_below_one": True,
        },
        "mixed_detail_interval": {
            "lower_decimal": float(mixed.lo),
            "upper_decimal": float(mixed.hi),
        },
        "strict_gate": "upper < -133/100",
        "scope": (
            "Exact Fraction arithmetic with directed rational square-root "
            "enclosures of denominator 10^70."
        ),
    }


if __name__ == "__main__":
    result = verify()
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)
