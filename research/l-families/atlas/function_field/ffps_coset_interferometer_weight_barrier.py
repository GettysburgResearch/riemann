#!/usr/bin/env python3
"""Exact bounded replay for the coset-interferometer weight barrier.

Only prime fields and integer/rational arithmetic are used.  The additive
characters enter through their exact autocorrelation identities, so no
floating-point cyclotomic approximation is needed.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

MAX_PRIME = 29
MAX_TENSOR_RANK = 5


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, math.isqrt(value) + 1))


def legendre(value: int, prime: int) -> int:
    residue = value % prime
    if residue == 0:
        return 0
    symbol = pow(residue, (prime - 1) // 2, prime)
    return 1 if symbol == 1 else -1


def additive_autocorrelation(prime: int, quadratic: bool) -> list[int]:
    """Return C(t)=sum_x w(x+t)w(x), with w(0)=0."""

    if not is_prime(prime) or prime == 2 or prime > MAX_PRIME:
        raise ValueError("prime must be an odd prime at most MAX_PRIME")
    weight = [
        legendre(value, prime) if quadratic else int(value != 0)
        for value in range(prime)
    ]
    return [
        sum(weight[(value + shift) % prime] * weight[value] for value in range(prime))
        for shift in range(prime)
    ]


def fourier_power_from_correlation(correlation: list[int]) -> int:
    """Evaluate sum_t C(t)e_p(t) when C is constant off zero."""

    if len(correlation) < 3 or any(
        value != correlation[1] for value in correlation[1:]
    ):
        raise ValueError("correlation must be constant away from zero")
    # sum_{t != 0} e_p(t) = -1.
    return correlation[0] - correlation[1]


def barrier_row(prime: int, rank: int) -> dict[str, object]:
    if not is_prime(prime) or prime == 2 or prime > MAX_PRIME:
        raise ValueError("prime must be an odd prime at most MAX_PRIME")
    if (
        isinstance(rank, bool)
        or not isinstance(rank, int)
        or not 1 <= rank <= MAX_TENSOR_RANK
    ):
        raise ValueError("rank must be an integer in the replay range")

    quotient_order = 2**rank
    principal_energy = 1
    selected_total = (prime + 1) ** rank - 1
    selected_average = Fraction(selected_total, quotient_order - 1)
    interferometer = Fraction(1) - selected_average
    literal_atomic_mass = (prime - 1) ** rank
    separate_triangle_bound = abs(interferometer) + selected_average
    return {
        "prime": prime,
        "rank": rank,
        "quotient_order": quotient_order,
        "principal_trace": (-1) ** rank,
        "principal_energy": principal_energy,
        "selected_total_energy": selected_total,
        "selected_average_energy": str(selected_average),
        "interferometer": str(interferometer),
        "literal_atomic_mass": literal_atomic_mass,
        "interferometer_has_literal_atomic_diagonal": False,
        "separate_triangle_bound_for_principal_energy": str(separate_triangle_bound),
        "exact_reconstruction": str(interferometer + selected_average),
    }


def run() -> dict[str, object]:
    correlation_rows = []
    for prime in (3, 5, 7, 13):
        trivial = additive_autocorrelation(prime, quadratic=False)
        quadratic = additive_autocorrelation(prime, quadratic=True)
        correlation_rows.append(
            {
                "prime": prime,
                "trivial_correlation": trivial,
                "quadratic_correlation": quadratic,
                "trivial_additive_sum_squared": fourier_power_from_correlation(trivial),
                "quadratic_gauss_sum_squared": fourier_power_from_correlation(
                    quadratic
                ),
            }
        )

    panels = [barrier_row(prime, rank) for prime in (3, 5, 13) for rank in range(1, 5)]
    return {
        "model": {
            "atom_space": "(F_p^times)^r",
            "atom_weight": "psi(x_1+...+x_r)",
            "quotient_phase": "(kappa(x_1),...,kappa(x_r)) in C_2^r",
            "principal_trace": "(-1)^r",
            "nonprincipal_mode_energy": "p^|S| for nonempty S subset {1,...,r}",
        },
        "exact_identities": {
            "selected_total_energy": "(p+1)^r-1",
            "selected_average_energy": "((p+1)^r-1)/(2^r-1)",
            "interferometer": "1-((p+1)^r-1)/(2^r-1)",
            "deduction": (
                "same-coset and literal-atom deletion does not lower the quadratic "
                "weight; principal recovery depends on exact cancellation with the "
                "selected average"
            ),
        },
        "autocorrelation_certificates": correlation_rows,
        "panels": panels,
        "resource_caps": {
            "maximum_prime": MAX_PRIME,
            "maximum_tensor_rank": MAX_TENSOR_RANK,
            "largest_autocorrelation_cells": MAX_PRIME**2,
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
