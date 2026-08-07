#!/usr/bin/env python3
"""Exact rational verifier for the outer parabolic-seed margin.

No floating point is used in any acceptance decision.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from math import isqrt
import json


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @staticmethod
    def exact(x: int | Fraction) -> "Interval":
        q = Fraction(x)
        return Interval(q, q)

    def __add__(self, other: object) -> "Interval":
        rhs = other if isinstance(other, Interval) else Interval.exact(other)  # type: ignore[arg-type]
        return Interval(self.lo + rhs.lo, self.hi + rhs.hi)

    __radd__ = __add__

    def __neg__(self) -> "Interval":
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: object) -> "Interval":
        rhs = other if isinstance(other, Interval) else Interval.exact(other)  # type: ignore[arg-type]
        return self + (-rhs)

    def __rsub__(self, other: object) -> "Interval":
        return Interval.exact(other) - self  # type: ignore[arg-type]

    def __mul__(self, other: object) -> "Interval":
        rhs = other if isinstance(other, Interval) else Interval.exact(other)  # type: ignore[arg-type]
        products = (
            self.lo * rhs.lo,
            self.lo * rhs.hi,
            self.hi * rhs.lo,
            self.hi * rhs.hi,
        )
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def reciprocal(self) -> "Interval":
        if self.lo <= 0:
            raise ValueError("reciprocal requires a positive interval")
        return Interval(1 / self.hi, 1 / self.lo)

    def __truediv__(self, other: object) -> "Interval":
        rhs = other if isinstance(other, Interval) else Interval.exact(other)  # type: ignore[arg-type]
        return self * rhs.reciprocal()

    def __rtruediv__(self, other: object) -> "Interval":
        return Interval.exact(other) / self  # type: ignore[arg-type]


SQRT_BITS = 64
LOG_TERMS = 28
EXP_TERMS = 36
CELL_MAX = 27
MARGIN = Fraction(1, 50)
LIPSCHITZ = 149
FINITE_X_THRESHOLD = 104_301


def sqrt_interval(x: int | Fraction, bits: int = SQRT_BITS) -> Interval:
    value = Fraction(x)
    if value < 0:
        raise ValueError("sqrt of negative number")
    denominator = 1 << bits
    scaled_num = value.numerator * denominator * denominator
    scaled_den = value.denominator
    root = isqrt(scaled_num // scaled_den)
    while (root + 1) ** 2 * scaled_den <= scaled_num:
        root += 1
    while root * root * scaled_den > scaled_num:
        root -= 1
    lo = Fraction(root, denominator)
    if root * root * scaled_den == scaled_num:
        return Interval(lo, lo)
    return Interval(lo, Fraction(root + 1, denominator))


def power_of_two(exponent: int) -> Fraction:
    if exponent >= 0:
        return Fraction(1 << exponent)
    return Fraction(1, 1 << (-exponent))


def floor_log2(value: Fraction) -> int:
    exponent = value.numerator.bit_length() - value.denominator.bit_length()
    while power_of_two(exponent) > value:
        exponent -= 1
    while power_of_two(exponent + 1) <= value:
        exponent += 1
    return exponent


def log_unit_interval(value: Fraction, terms: int = LOG_TERMS) -> Interval:
    """Bounds log(value) for 1 <= value <= 2 by the atanh series."""
    if not (Fraction(1) <= value <= Fraction(2)):
        raise ValueError("unit log reduction failed")
    z = (value - 1) / (value + 1)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for index in range(terms):
        partial += power / (2 * index + 1)
        power *= z2
    lo = 2 * partial
    # The omitted positive terms are bounded by replacing every denominator
    # by the first omitted denominator.
    remainder = 2 * power / ((2 * terms + 1) * (1 - z2))
    return Interval(lo, lo + remainder)


def log_interval(x: int | Fraction, terms: int = LOG_TERMS) -> Interval:
    value = Fraction(x)
    if value <= 0:
        raise ValueError("log requires positive input")
    if value == 1:
        return Interval.exact(0)
    exponent = floor_log2(value)
    reduced = value / power_of_two(exponent)
    return log_unit_interval(reduced, terms) + exponent * log_unit_interval(Fraction(2), terms)


def exp_upper(x: Fraction, terms: int = EXP_TERMS) -> Fraction:
    """Exact rational upper bound for exp(x), for x >= 0."""
    if x < 0:
        raise ValueError("this verifier only needs nonnegative exp arguments")
    term = Fraction(1)
    partial = term
    for n in range(1, terms + 1):
        term = term * x / n
        partial += term
    first_omitted = term * x / (terms + 1)
    ratio_bound = x / (terms + 2)
    if ratio_bound >= 1:
        raise ValueError("exp tail ratio is not contractive")
    return partial + first_omitted / (1 - ratio_bound)


def critical_maximum_upper(cell: int) -> Fraction:
    """Upper bound for the global maximum of the N-cell formula E_N."""
    harmonic = Interval.exact(0)
    logarithmic = Interval.exact(0)
    for k in range(1, cell + 1):
        inverse_sqrt = Interval.exact(1) / sqrt_interval(k)
        harmonic += inverse_sqrt
        logarithmic += log_interval(k) * inverse_sqrt

    exponent = (logarithmic + 2 * harmonic - 2) / (2 * (harmonic + 1))
    exponential_upper = exp_upper(exponent.hi)
    maximum = 2 * (harmonic + 1) * exponential_upper - 4 * cell
    return maximum.hi


def proof_object(cell_max: int = CELL_MAX, margin: Fraction = MARGIN) -> dict[str, object]:
    rows = []
    for cell in range(2, cell_max + 1):
        upper = critical_maximum_upper(cell)
        rows.append(
            {
                "cell": cell,
                "upper_lt_minus_margin": upper < -margin,
                # Display only a non-authoritative decimal; acceptance uses Fraction.
                "upper_decimal": f"{float(upper):.15g}",
            }
        )

    return {
        "arithmetic": "EXACT_RATIONAL",
        "sqrt_bits": SQRT_BITS,
        "log_terms": LOG_TERMS,
        "exp_terms": EXP_TERMS,
        "cells": rows,
        "margin": "1/50",
        "lipschitz_bound": LIPSCHITZ,
        "finite_X_threshold": FINITE_X_THRESHOLD,
        "lipschitz_integer_check": 28**3 < LIPSCHITZ**2,
        "remainder_threshold_check": 28 * LIPSCHITZ * 50 < 2 * FINITE_X_THRESHOLD,
        "all_cells_pass": all(bool(row["upper_lt_minus_margin"]) for row in rows),
    }


def verify() -> dict[str, object]:
    result = proof_object()
    if not result["all_cells_pass"]:
        raise AssertionError("one reciprocal cell failed the 1/50 margin")
    if not result["lipschitz_integer_check"]:
        raise AssertionError("149 does not dominate 28^(3/2)")
    if not result["remainder_threshold_check"]:
        raise AssertionError("finite-X threshold does not dominate the Taylor remainder")

    # Adversarial mutations.
    if proof_object(cell_max=28)["all_cells_pass"]:
        raise AssertionError("mutation failed: cell 28 should not satisfy the margin")
    if proof_object(margin=Fraction(1, 40))["all_cells_pass"]:
        raise AssertionError("mutation failed: 1/40 is too strong at cell 27")

    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = sha256(canonical).hexdigest()
    result["verdict"] = "PASS_EXACT_OUTER_PARABOLIC_SEED_MARGIN"
    return result


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
