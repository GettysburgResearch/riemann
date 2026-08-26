#!/usr/bin/env python3
"""Exact replay for the odd-notch second-boundary zero-density constant."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

Q_PANELS = (3, 5, 7, 9, 11, 13)
MAX_Q = 13
MAX_PROFILE_H = 200


def rademacher_multiplicity(count: int, total: int) -> int:
    if abs(total) > count or (count + total) % 2:
        return 0
    return math.comb(count, (count + total) // 2)


def d3_local_zero_probability(q: int) -> Fraction:
    if (
        isinstance(q, bool)
        or not isinstance(q, int)
        or q < 3
        or q % 2 == 0
        or q > MAX_Q
    ):
        raise ValueError("q must be an odd integer in the replay range")
    degree_1_count = q
    degree_2_count = (q * q - q) // 2
    degree_3_count = (q**3 - q) // 3
    favorable = 0
    for s1 in range(-degree_1_count, degree_1_count + 1, 2):
        multiplicity_1 = rademacher_multiplicity(degree_1_count, s1)
        cubic_numerator = s1**3 + (2 - 3 * q) * s1
        if cubic_numerator % 6:
            raise AssertionError("complete-homogeneous cubic is not integral")
        cubic_term = cubic_numerator // 6
        for s2 in range(-degree_2_count, degree_2_count + 1, 2):
            target_s3 = -s1 * s2 - cubic_term
            multiplicity_3 = rademacher_multiplicity(degree_3_count, target_s3)
            if multiplicity_3:
                favorable += (
                    multiplicity_1
                    * rademacher_multiplicity(degree_2_count, s2)
                    * multiplicity_3
                )
    total_sign_packets = 2 ** (degree_1_count + degree_2_count + degree_3_count)
    return Fraction(favorable, total_sign_packets)


def leading_profile_weight(h: int) -> Fraction:
    """Coefficient of q^M from the leading two/three-factor profiles."""

    if isinstance(h, bool) or not isinstance(h, int) or h < 5 or h > MAX_PROFILE_H:
        raise ValueError("h is outside the replay range")
    pinned = h - 1
    weight = Fraction(1, pinned * (3 * h + 2))
    for degree in range(h + 1, (3 * h + 2) // 2 + 1):
        complement = 3 * h + 2 - degree
        if degree < complement:
            weight += Fraction(1, pinned * degree * complement)
        elif degree == complement:
            weight += Fraction(1, 2 * pinned * degree * degree)
    return weight


def polynomial_multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            result[left_degree + right_degree] += left_value * right_value
    return result


def polynomial_power(polynomial: list[Fraction], exponent: int) -> list[Fraction]:
    result = [Fraction(1)]
    for _ in range(exponent):
        result = polynomial_multiply(result, polynomial)
    return result


def gaussian_expectation(polynomial: list[Fraction]) -> Fraction:
    total = Fraction(0)
    for degree, coefficient in enumerate(polynomial):
        if degree % 2:
            continue
        moment = 1 if degree == 0 else math.prod(range(1, degree, 2))
        total += coefficient * moment
    return total


def chaos_even_moment(order: int) -> Fraction:
    """Moment of W=H_3(X)/6+XY/sqrt(2)+Z/sqrt(3), conditionally Gaussian."""

    if order not in (2, 4, 6):
        raise ValueError("the replay certifies only moments 2, 4, and 6")
    # Given X=x, W is normal with mean a=(x^3-3x)/6 and
    # variance v=x^2/2+1/3.  E[(a+sqrt(v)G)^m] is expanded exactly.
    mean = [Fraction(0), Fraction(-1, 2), Fraction(0), Fraction(1, 6)]
    variance = [Fraction(1, 3), Fraction(0), Fraction(1, 2)]
    conditional = [Fraction(0)]
    for gaussian_degree in range(0, order + 1, 2):
        gaussian_moment = (
            1 if gaussian_degree == 0 else math.prod(range(1, gaussian_degree, 2))
        )
        coefficient = Fraction(math.comb(order, gaussian_degree) * gaussian_moment)
        term = polynomial_multiply(
            polynomial_power(mean, order - gaussian_degree),
            polynomial_power(variance, gaussian_degree // 2),
        )
        if len(conditional) < len(term):
            conditional.extend([Fraction(0)] * (len(term) - len(conditional)))
        for degree, value in enumerate(term):
            conditional[degree] += coefficient * value
    return gaussian_expectation(conditional)


def run() -> dict[str, object]:
    local_rows = []
    for q in Q_PANELS:
        delta = d3_local_zero_probability(q)
        prefactor = delta * Fraction(16 * q, 3 * (q - 1))
        local_rows.append(
            {
                "q": q,
                "degree_1_irreducibles": q,
                "degree_2_irreducibles": (q * q - q) // 2,
                "degree_3_irreducibles": (q**3 - q) // 3,
                "delta_q": str(delta),
                "delta_q_numerator": delta.numerator,
                "delta_q_denominator": delta.denominator,
                "M_minus_2_coefficient": (f"({prefactor})*(1+log(2))"),
            }
        )

    profile_rows = []
    for h in (5, 10, 25, 50, 100, 200):
        weight = leading_profile_weight(h)
        profile_rows.append(
            {
                "h": h,
                "h_squared_profile_weight": str(h * h * weight),
            }
        )

    return {
        "exact_local_formula": {
            "D3": "S3+S1*S2+(S1^3+(2-3q)*S1)/6",
            "independent_sign_counts": "N1=q, N2=(q^2-q)/2, N3=(q^3-q)/3",
            "delta_q": "Prob(D3=0) under independent Rademacher signs",
        },
        "fixed_q_density_theorem": {
            "count": "delta_q*(1+log(2))*q^M/(3h^2)+O_q(q^M/h^3)",
            "squarefree_density": ("16*delta_q*(1+log(2))/(3*(1-q^-1)*M^2)+O_q(M^-3)"),
        },
        "large_q_weak_limit": {
            "law": "Z/sqrt(3)+X*Y/sqrt(2)+(X^3-3X)/6",
            "independent_standard_normals": ["X", "Y", "Z"],
            "second_moment": str(chaos_even_moment(2)),
            "fourth_moment": str(chaos_even_moment(4)),
            "sixth_moment": str(chaos_even_moment(6)),
            "local_limit_status": "conjectural; weak convergence does not prove delta_q asymptotics",
        },
        "local_probability_panels": local_rows,
        "profile_limit_panels": profile_rows,
        "resource_caps": {
            "maximum_q": MAX_Q,
            "maximum_profile_h": MAX_PROFILE_H,
            "residue_classes_enumerated": 0,
            "polynomials_enumerated": 0,
            "point_counts": 0,
            "floating_point_operations": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
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
