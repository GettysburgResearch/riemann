#!/usr/bin/env python3
"""Bounded replay for the third-order odd-notch zero-density coefficient."""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path

MIN_H = 7
MAX_H = 200
ENUMERATION_MAX_H = 40

AffineLog2 = tuple[Fraction, Fraction]


def harmonic(number: int) -> Fraction:
    if isinstance(number, bool) or not isinstance(number, int) or number < 0:
        raise ValueError("harmonic index must be a nonnegative integer")
    return sum((Fraction(1, index) for index in range(1, number + 1)), Fraction(0))


def one_pinned_direct_weight(h_value: int) -> Fraction:
    """Principal q^M coefficient for profiles with one degree-(h-1) factor."""

    _validate_h(h_value)
    pinned = h_value - 1
    remaining = 3 * h_value + 2
    weight = Fraction(1, pinned * remaining)
    for degree in range(h_value + 1, remaining // 2 + 1):
        complement = remaining - degree
        if degree < complement:
            weight += Fraction(1, pinned * degree * complement)
        elif degree == complement:
            weight += Fraction(1, 2 * pinned * degree * degree)
    return weight


def one_pinned_harmonic_weight(h_value: int) -> Fraction:
    """The exact harmonic-number compression of ``one_pinned_direct_weight``."""

    _validate_h(h_value)
    return Fraction(
        1 + harmonic(2 * h_value + 1) - harmonic(h_value),
        (h_value - 1) * (3 * h_value + 2),
    )


def two_pinned_three_factor_weight(h_value: int) -> Fraction:
    """Weight of (h-1,h-1,2h+3), including the repeated-factor 1/2."""

    _validate_h(h_value)
    return Fraction(1, 2 * (h_value - 1) ** 2 * (2 * h_value + 3))


def fourth_order_profile_weight(h_value: int) -> Fraction:
    """The two remaining profile weights, both O(h^-4)."""

    _validate_h(h_value)
    two_pinned_four_factor = Fraction(
        1,
        2 * (h_value - 1) ** 2 * (h_value + 1) * (h_value + 2),
    )
    three_pinned = Fraction(1, 6 * (h_value - 1) ** 3 * (h_value + 4))
    return two_pinned_four_factor + three_pinned


def all_profile_principal_weight(h_value: int) -> Fraction:
    """Principal q^M coefficient of every m_h=0 second-boundary profile."""

    return (
        one_pinned_harmonic_weight(h_value)
        + two_pinned_three_factor_weight(h_value)
        + fourth_order_profile_weight(h_value)
    )


def _validate_h(h_value: int) -> None:
    if (
        isinstance(h_value, bool)
        or not isinstance(h_value, int)
        or h_value < MIN_H
        or h_value > MAX_H
    ):
        raise ValueError(f"h must be an integer in [{MIN_H}, {MAX_H}]")


def degree_profiles(h_value: int) -> tuple[tuple[int, ...], ...]:
    """Enumerate degree multisets only; no polynomial or field enumeration."""

    if h_value > ENUMERATION_MAX_H:
        raise ValueError("h exceeds the bounded degree-profile enumeration range")
    _validate_h(h_value)
    total = 4 * h_value + 1
    minimum = h_value - 1
    rows: list[tuple[int, ...]] = []

    def recurse(remaining: int, lower: int, row: tuple[int, ...]) -> None:
        if remaining == 0:
            if row and row[0] == minimum and h_value not in row:
                rows.append(row)
            return
        if remaining < lower:
            return
        for degree in range(lower, remaining + 1):
            if degree == h_value:
                continue
            recurse(remaining - degree, degree, (*row, degree))

    recurse(total, minimum, ())
    return tuple(rows)


def claimed_profiles(h_value: int) -> tuple[tuple[int, ...], ...]:
    """Closed profile list for h>=7."""

    _validate_h(h_value)
    pinned = h_value - 1
    remaining = 3 * h_value + 2
    rows = [(pinned, remaining)]
    rows.extend(
        (pinned, degree, remaining - degree)
        for degree in range(h_value + 1, remaining // 2 + 1)
    )
    rows.extend(
        (
            (pinned, pinned, 2 * h_value + 3),
            (pinned, pinned, h_value + 1, h_value + 2),
            (pinned, pinned, pinned, h_value + 4),
        )
    )
    return tuple(rows)


def profile_principal_weight(profile: tuple[int, ...]) -> Fraction:
    multiplicities = Counter(profile)
    denominator = 1
    for degree, multiplicity in multiplicities.items():
        denominator *= degree**multiplicity * math.factorial(multiplicity)
    return Fraction(1, denominator)


def enumerated_profile_weight(h_value: int) -> Fraction:
    return sum(map(profile_principal_weight, degree_profiles(h_value)), Fraction(0))


def affine_add(left: AffineLog2, right: AffineLog2) -> AffineLog2:
    return left[0] + right[0], left[1] + right[1]


def affine_scale(scalar: int | Fraction, value: AffineLog2) -> AffineLog2:
    return scalar * value[0], scalar * value[1]


def affine_render(value: AffineLog2) -> str:
    return f"{value[0]} + ({value[1]})*log(2)"


H_MINUS_2: AffineLog2 = (Fraction(1, 3), Fraction(1, 3))
H_MINUS_3_ONE_PINNED: AffineLog2 = (Fraction(7, 36), Fraction(1, 9))
H_MINUS_3_TWO_PINNED: AffineLog2 = (Fraction(1, 4), Fraction(0))
H_MINUS_3_TOTAL = affine_add(H_MINUS_3_ONE_PINNED, H_MINUS_3_TWO_PINNED)
M_MINUS_2 = affine_scale(16, H_MINUS_2)
M_MINUS_3 = affine_add(affine_scale(32, H_MINUS_2), affine_scale(64, H_MINUS_3_TOTAL))


def affine_float(value: AffineLog2) -> float:
    return float(value[0]) + float(value[1]) * math.log(2)


def validate() -> None:
    for h_value in range(MIN_H, ENUMERATION_MAX_H + 1):
        if one_pinned_direct_weight(h_value) != one_pinned_harmonic_weight(h_value):
            raise ArithmeticError("one-pinned harmonic compression failed")
        if set(degree_profiles(h_value)) != set(claimed_profiles(h_value)):
            raise ArithmeticError("closed degree-profile classification failed")
        if enumerated_profile_weight(h_value) != all_profile_principal_weight(h_value):
            raise ArithmeticError("all-profile principal weight failed")
    if H_MINUS_3_TOTAL != (Fraction(4, 9), Fraction(1, 9)):
        raise ArithmeticError("h^-3 coefficient reduction failed")
    if M_MINUS_3 != (Fraction(352, 9), Fraction(160, 9)):
        raise ArithmeticError("M^-3 normalization failed")


def run() -> dict[str, object]:
    validate()
    c2 = affine_float(H_MINUS_2)
    m2 = affine_float(M_MINUS_2)
    panels = []
    for h_value in (7, 10, 25, 50, 100, 200):
        weight = float(all_profile_principal_weight(h_value))
        conductor_degree = 4 * h_value + 1
        panels.append(
            {
                "h": h_value,
                "M": conductor_degree,
                "h_cubed_next_coefficient_estimate": h_value**3
                * (weight - c2 / h_value**2),
                "M_cubed_next_coefficient_estimate": conductor_degree**3
                * (weight - m2 / conductor_degree**2),
            }
        )
    return {
        "schema": "riemann.function_field.quadratic_second_boundary_zero_density.third_order.v1",
        "fixed_q_count": {
            "formula": ("delta_q*q^M*((1+log(2))/(3h^2)+(4+log(2))/(9h^3)+O_q(h^-4))"),
            "h_minus_2_coefficient": affine_render(H_MINUS_2),
            "h_minus_3_one_pinned": affine_render(H_MINUS_3_ONE_PINNED),
            "h_minus_3_two_pinned": affine_render(H_MINUS_3_TWO_PINNED),
            "h_minus_3_total": affine_render(H_MINUS_3_TOTAL),
            "same_local_probability": "delta_q=Prob(D3=0) for every profile",
        },
        "squarefree_density": {
            "formula": (
                "delta_q/(1-q^-1)*(16*(1+log(2))/(3M^2)"
                "+32*(11+5log(2))/(9M^3)+O_q(M^-4))"
            ),
            "M_minus_2_coefficient": affine_render(M_MINUS_2),
            "M_minus_3_coefficient": affine_render(M_MINUS_3),
        },
        "profile_classification": {
            "one_pinned": "(h-1,3h+2) and (h-1,d,3h+2-d)",
            "two_pinned_h_minus_3": "(h-1,h-1,2h+3)",
            "fourth_order_only": [
                "(h-1,h-1,h+1,h+2)",
                "(h-1,h-1,h-1,h+4)",
            ],
        },
        "convergence_panels": panels,
        "resource_caps": {
            "maximum_h": MAX_H,
            "maximum_enumerated_h": ENUMERATION_MAX_H,
            "polynomials_enumerated": 0,
            "irreducibles_enumerated": 0,
            "residue_classes_enumerated": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
