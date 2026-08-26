#!/usr/bin/env python3
"""Bounded exact replay for the relative-boundary trace-tower gate.

No finite field, closed place, curve, or sheaf is enumerated.  The replay only
uses integer cycle types, divisor sums, and rational representation-ring
normalizations.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

MAX_REPLAY_DEGREE = 8


def validate_degree(degree: int) -> None:
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 1:
        raise ValueError("degree must be a positive integer")


def validate_cycle_type(cycle_type: tuple[int, ...]) -> None:
    if not cycle_type:
        raise ValueError("cycle type must be nonempty")
    for degree in cycle_type:
        validate_degree(degree)


def partitions(total: int, largest: int | None = None) -> list[tuple[int, ...]]:
    """Return the integer partitions of ``total`` in decreasing order."""
    validate_degree(total)
    upper = total if largest is None else min(total, largest)
    rows: list[tuple[int, ...]] = []
    for first in range(upper, 0, -1):
        if first == total:
            rows.append((first,))
        elif first < total:
            for tail in partitions(total - first, first):
                rows.append((first, *tail))
    return rows


def multiply_polynomials(left: list[int], right: list[int]) -> list[int]:
    product = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            product[left_index + right_index] += left_value * right_value
    return product


def standard_exterior_alternating_sum(cycle_type: tuple[int, ...]) -> int:
    """Compute det(1-g | Std) exactly from the cycle type of ``g``.

    On the permutation representation,

        det(1-t g) = product_c (1-t^c).

    Dividing once by ``1-t`` removes the invariant line and evaluating at
    ``t=1`` gives the alternating exterior-power character of ``Std``.
    """
    validate_cycle_type(cycle_type)
    polynomial = [1]
    for cycle_length in cycle_type:
        factor = [1, *([0] * (cycle_length - 1)), -1]
        polynomial = multiply_polynomials(polynomial, factor)

    # If polynomial = (1-t) quotient, then p_i = q_i-q_(i-1).
    quotient: list[int] = []
    previous = 0
    for coefficient in polynomial[:-1]:
        current = coefficient + previous
        quotient.append(current)
        previous = current
    if polynomial[-1] != -quotient[-1]:
        raise AssertionError("exact division by 1-t failed")
    return sum(quotient)


def irreducible_cycle_selector_trace(cycle_type: tuple[int, ...]) -> Fraction:
    """Trace of d^-1 Lambda_{-1}(Std_d) on the given cycle type."""
    validate_cycle_type(cycle_type)
    degree = sum(cycle_type)
    return Fraction(standard_exterior_alternating_sum(cycle_type), degree)


def permutation_trace(cycle_type: tuple[int, ...]) -> int:
    """Trace on the universal-root permutation representation."""
    validate_cycle_type(cycle_type)
    return cycle_type.count(1)


def selected_incidence_trace(cycle_type: tuple[int, ...]) -> Fraction:
    """Trace of Perm_d tensor d^-1 Lambda_{-1}(Std_d)."""
    return permutation_trace(cycle_type) * irreducible_cycle_selector_trace(cycle_type)


def fixed_boundary_trace(place_degrees: tuple[int, ...], extension_degree: int) -> int:
    """Trace of a fixed reduced divisor over F_(q^extension_degree)."""
    if not place_degrees:
        raise ValueError("place-degree profile must be nonempty")
    for degree in place_degrees:
        validate_degree(degree)
    validate_degree(extension_degree)
    return sum(degree for degree in place_degrees if extension_degree % degree == 0)


def divisors(value: int) -> list[int]:
    validate_degree(value)
    return [divisor for divisor in range(1, value + 1) if value % divisor == 0]


def mobius(value: int) -> int:
    validate_degree(value)
    remaining = value
    prime_count = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            if remaining % prime == 0:
                return 0
            prime_count += 1
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def recover_degree_profile(
    trace_tower: dict[int, int], maximum_degree: int
) -> dict[int, int]:
    """Recover closed-place multiplicities by exact Moebius inversion."""
    validate_degree(maximum_degree)
    if any(degree not in trace_tower for degree in range(1, maximum_degree + 1)):
        raise ValueError("trace tower is missing an extension degree")
    recovered: dict[int, int] = {}
    for degree in range(1, maximum_degree + 1):
        weighted_count = sum(
            mobius(degree // divisor) * trace_tower[divisor]
            for divisor in divisors(degree)
        )
        if weighted_count % degree:
            raise ValueError("trace tower is not an integral divisor profile")
        recovered[degree] = weighted_count // degree
    return recovered


def selector_absolute_rank_mass(degree: int) -> Fraction:
    """Absolute generic-rank mass of d^-1 Lambda_{-1}(Std_d)."""
    validate_degree(degree)
    return Fraction(2 ** (degree - 1), degree)


def run() -> dict[str, object]:
    cycle_panels: list[dict[str, object]] = []
    for degree in range(1, MAX_REPLAY_DEGREE + 1):
        cycle_types = partitions(degree)
        rows = [
            {
                "cycle_type": list(cycle_type),
                "fixed_roots": permutation_trace(cycle_type),
                "selector_trace": str(irreducible_cycle_selector_trace(cycle_type)),
                "selected_incidence_trace": str(selected_incidence_trace(cycle_type)),
            }
            for cycle_type in cycle_types
        ]
        cycle_panels.append(
            {
                "degree": degree,
                "cycle_types_checked": len(cycle_types),
                "selector_absolute_rank_mass": str(selector_absolute_rank_mass(degree)),
                "rows": rows,
            }
        )

    fixed_profile = (2, 3, 5, 5)
    maximum_degree = max(fixed_profile)
    trace_tower = {
        extension: fixed_boundary_trace(fixed_profile, extension)
        for extension in range(1, maximum_degree + 1)
    }
    recovered = recover_degree_profile(trace_tower, maximum_degree)
    return {
        "theorem": {
            "fixed_divisor_base_shadow": (
                "B_D(1)=0 when the fixed divisor has no degree-one place"
            ),
            "fixed_divisor_tower": "B_D(m)=sum_(d|m) d*N_d",
            "tower_no_go": ("Moebius inversion recovers every N_d from the full tower"),
            "cycle_selector": (
                "Q_d=d^-1*Lambda_-1(Std_d) has trace one exactly on d-cycles"
            ),
            "universal_incidence_cancellation": (
                "[Perm_d tensor Q_d]=0 in R(S_d) tensor Q for d>1"
            ),
            "firewall": (
                "the universal selector reselects over every residue field; "
                "it is not the constant-weight extension tower of one fixed place"
            ),
        },
        "cycle_panels": cycle_panels,
        "fixed_divisor_panel": {
            "place_degrees": list(fixed_profile),
            "trace_tower": {str(key): value for key, value in trace_tower.items()},
            "recovered_multiplicities": {
                str(key): value for key, value in recovered.items()
            },
        },
        "resource_caps": {
            "maximum_cycle_degree": MAX_REPLAY_DEGREE,
            "cycle_types_checked": sum(
                len(partitions(degree)) for degree in range(1, MAX_REPLAY_DEGREE + 1)
            ),
            "finite_field_points": 0,
            "closed_places_enumerated": 0,
            "curves_or_sheaves_constructed": 0,
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
