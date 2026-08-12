from __future__ import annotations

from fractions import Fraction
from math import isqrt
import json

SCALE = 10**35
LOG_TERMS = 90
MAXX = 4489
PRIMES61 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]


class FI:
    __slots__ = ("lo", "hi")

    def __init__(self, lo: int, hi: int | None = None):
        self.lo = lo
        self.hi = lo if hi is None else hi

    @staticmethod
    def frac(q: Fraction) -> "FI":
        n, d = q.numerator, q.denominator
        return FI((n * SCALE) // d, -((-n * SCALE) // d))

    def __add__(self, other: "FI") -> "FI":
        return FI(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other: "FI") -> "FI":
        return FI(self.lo - other.hi, self.hi - other.lo)

    def __mul__(self, other: "FI") -> "FI":
        values = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return FI(min(values) // SCALE, -((-max(values)) // SCALE))

    def mul_frac(self, q: Fraction) -> "FI":
        n, d = q.numerator, q.denominator
        if n >= 0:
            return FI((self.lo * n) // d, -((-self.hi * n) // d))
        return FI((self.hi * n) // d, -((-self.lo * n) // d))


def sqrt_i(n: int) -> FI:
    root = isqrt(n * SCALE * SCALE)
    return FI(root, root + 1)


def inv_pos(x: FI) -> FI:
    return FI((SCALE * SCALE) // x.hi, -((-SCALE * SCALE) // x.lo))


def atanh_log_fraction(m: Fraction) -> FI:
    """Rigorous log(m) enclosure for 1 <= m <= 2."""
    z = (m - 1) / (m + 1)
    z2 = z * z
    power = z
    series = Fraction(0)
    for j in range(LOG_TERMS):
        series += power / Fraction(2 * j + 1)
        power *= z2
    tail = power / Fraction(2 * LOG_TERMS + 1) / (1 - z2)
    return FI.frac(2 * series) + FI(0, FI.frac(2 * tail).hi)


LOG2 = atanh_log_fraction(Fraction(2, 1))


def log_int(n: int) -> FI:
    if n == 1:
        return FI(0)
    exponent = n.bit_length() - 1
    mantissa = Fraction(n, 1 << exponent)
    return atanh_log_fraction(mantissa) + LOG2.mul_frac(Fraction(exponent))


INV_SQRT = [FI(0)] * (MAXX + 1)
LOG = [FI(0)] * (MAXX + 1)
for n in range(1, MAXX + 1):
    INV_SQRT[n] = inv_pos(sqrt_i(n))
    LOG[n] = log_int(n)

DIVISORS = [(1, 1)]
for q in PRIMES61:
    DIVISORS += [(d * q, -mu) for d, mu in list(DIVISORS)]
SMALL_DIVISORS = sorted((d, mu) for d, mu in DIVISORS if d <= MAXX)


def component_coefficient(j: int, m: int) -> Fraction:
    if m < j:
        return Fraction(0)
    if m == j:
        return Fraction(j + 1, j - 1)
    if m == j + 1:
        return -Fraction((j + 1) * (j - 2), j * (j - 1))
    return Fraction(2, j * (j - 1))


def coefficient_array(j: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(MAXX + 1)]
    for divisor, mu in SMALL_DIVISORS:
        max_m = MAXX // divisor
        if j > max_m:
            continue
        out[divisor * j] += mu * component_coefficient(j, j)
        if j + 1 <= max_m:
            out[divisor * (j + 1)] += mu * component_coefficient(j, j + 1)
        tail = mu * component_coefficient(j, j + 2)
        for m in range(j + 2, max_m + 1):
            out[divisor * m] += tail
    return out


def scan() -> tuple[int, int, dict[str, tuple[int, tuple[int, int, int, int]]]]:
    inv67 = INV_SQRT[67]
    minima = {name: (10**100, None) for name in ("parent", "bonus", "raw")}
    cells = 0
    checks = 0

    for j in range(2, 67):
        coefficients = coefficient_array(j)
        parent_c = FI(0)
        parent_d = FI(0)
        child_c = FI(0)
        child_d = FI(0)

        for k in range(1, MAXX):
            b = coefficients[k]
            if b:
                term = INV_SQRT[k].mul_frac(b)
                parent_c = parent_c + term
                parent_d = parent_d + term * LOG[k]

            if k % 67 == 0:
                m = k // 67
                b_child = coefficients[m]
                if b_child:
                    term = INV_SQRT[m].mul_frac(b_child)
                    child_c = child_c + term
                    child_d = child_d + term * LOG[k]

            if k < 67 * j:
                continue

            quantities = {
                "parent": (parent_c, parent_d),
                "bonus": (parent_c - child_c, parent_d - child_d),
                "raw": (
                    parent_c - inv67 * child_c,
                    parent_d - inv67 * child_d,
                ),
            }

            for endpoint in (k, k + 1):
                for name, (coefficient, constant) in quantities.items():
                    value = coefficient * LOG[endpoint] - constant
                    checks += 1
                    if value.lo < minima[name][0]:
                        minima[name] = (value.lo, (j, k, endpoint, value.hi))
                    if value.lo <= 0:
                        raise AssertionError((name, j, k, endpoint, value.lo, value.hi))
            cells += 1

    return cells, checks, minima


if __name__ == "__main__":
    cells, checks, minima = scan()
    thresholds = {
        "parent": SCALE // 100,
        "bonus": SCALE // 100,
        "raw": 3 * SCALE // 250,
    }
    output = {
        "classification": "PASS_FIXED67_FIRST_ENTRY_ROW_AUDIT",
        "scale": SCALE,
        "log_terms": LOG_TERMS,
        "cells": cells,
        "endpoint_quantity_checks": checks,
        "certified_bounds": {
            "parent": "1/100",
            "dilation_bonus": "1/100",
            "raw_splice": "3/250",
        },
        "minima": {},
    }
    for name, (lower, witness) in minima.items():
        assert lower > thresholds[name], (name, lower, thresholds[name])
        row, cell_left, endpoint, upper = witness
        output["minima"][name] = {
            "lower_fixed": str(lower),
            "upper_fixed": str(upper),
            "lower_decimal": f"{lower / SCALE:.18f}",
            "upper_decimal": f"{upper / SCALE:.18f}",
            "row": row,
            "cell_left": cell_left,
            "endpoint": endpoint,
        }
    print(json.dumps(output, indent=2, sort_keys=True))
