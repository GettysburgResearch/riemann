#!/usr/bin/env python3
"""Bounded replay for the closed-place scalable block tower."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

Q_PANELS = (3, 5, 7, 9, 11)
MAX_DEGREE = 8


def is_prime_power(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value and value % divisor:
        divisor += 1
    if divisor * divisor > value:
        return True
    while value % divisor == 0:
        value //= divisor
    return value == 1


def eligible_degree(q: int, degree: int) -> bool:
    if (
        isinstance(q, bool)
        or isinstance(degree, bool)
        or not isinstance(q, int)
        or not isinstance(degree, int)
        or q < 3
        or q % 2 == 0
        or not is_prime_power(q)
        or degree < 1
        or degree > MAX_DEGREE
    ):
        raise ValueError("use an odd replay cardinality and a positive bounded degree")
    return pow(q, degree, 4) == 1


def eligible_density(q: int) -> Fraction:
    if (
        isinstance(q, bool)
        or not isinstance(q, int)
        or q < 3
        or q % 2 == 0
        or not is_prime_power(q)
    ):
        raise ValueError("q must be an odd prime power")
    return Fraction(1) if q % 4 == 1 else Fraction(1, 2)


def block_leverage(left_norm: int, right_norm: int) -> Fraction:
    if left_norm < 5 or right_norm < 5:
        raise ValueError("eligible odd residue cardinalities are at least five")
    return Fraction(
        4 * (left_norm - 1) * (right_norm - 1),
        5 * left_norm * right_norm + left_norm + right_norm + 1,
    )


def density_exponent(alpha: float, density: float) -> float:
    if not 0 < alpha < density <= 1:
        raise ValueError("require 0<alpha<density<=1")
    return density - alpha + alpha * math.log(alpha / density)


def leverage_exponent(alpha: float) -> float:
    if alpha <= 0:
        raise ValueError("alpha must be positive")
    return alpha * math.log(5 / 4)


def balanced_alpha(density: float) -> float:
    lower = 1e-12
    upper = density - 1e-12
    for _ in range(80):
        middle = (lower + upper) / 2
        if density_exponent(middle, density) > leverage_exponent(middle):
            lower = middle
        else:
            upper = middle
    return (lower + upper) / 2


def q_panel(q: int) -> dict[str, object]:
    density = eligible_density(q)
    eligible = [
        degree for degree in range(1, MAX_DEGREE + 1) if eligible_degree(q, degree)
    ]
    if len(eligible) < 2:
        raise AssertionError("replay panel needs two eligible degrees")
    first_norm = q ** eligible[0]
    second_norm = q ** eligible[1]
    alpha = balanced_alpha(float(density))
    return {
        "q": q,
        "q_mod_4": q % 4,
        "eligible_degrees_through_8": eligible,
        "eligible_degree_density": str(density),
        "first_two_norms": [first_norm, second_norm],
        "sample_block_leverage": str(block_leverage(first_norm, second_norm)),
        "balanced_alpha": f"{alpha:.12f}",
        "balanced_exponent": f"{density_exponent(alpha, float(density)):.12f}",
    }


def run() -> dict[str, object]:
    return {
        "orientation": {
            "condition": "4 divides q^degree-1",
            "q_1_mod_4": "all closed-place degrees",
            "q_3_mod_4": "even closed-place degrees",
        },
        "squarefree_factor_count": {
            "eligible_density": "delta=1 if q=1 mod 4; delta=1/2 if q=3 mod 4",
            "rank": "r=floor(alpha*log n), 0<alpha<delta",
            "bad_probability": "n^(-c_delta(alpha)+o(1))",
            "c_delta": "delta-alpha+alpha*log(alpha/delta)",
        },
        "block_tower": {
            "source_scope": (
                "conditional on one clean pair N=P*G^2*C^2, M=Q*G^2*D^2; "
                "no universal FFPS source adapter"
            ),
            "leverage": "L_r<(4/5)^r=n^(-alpha*log(5/4)+o(1))",
            "selected_modes": "2^r-1",
            "every_mode_bilateral": True,
        },
        "panels": [q_panel(q) for q in Q_PANELS],
        "resource_caps": {
            "q_panels": len(Q_PANELS),
            "maximum_closed_place_degree": MAX_DEGREE,
            "bisection_steps_per_panel": 80,
            "polynomials_enumerated": 0,
            "closed_places_enumerated": 0,
            "curves_enumerated": 0,
            "point_counts": 0,
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
