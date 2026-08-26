#!/usr/bin/env python3
"""Exact degree-profile replay for the odd-notch second-boundary reduction."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "QUADRATIC_FAMILY_SECOND_BOUNDARY_TRACE_ZERO_REDUCTION.md"
SOURCE_BLOBS = {
    (
        "1205d4bed7812d9bf883c820ceb901e8fe00b7c0",
        "research/l-families/atlas/function_field/QUADRATIC_FAMILY_FIRST_BOUNDARY_TRACE_ZERO_DENSITY.md",
    ): "f2a6be22e720be40aa19abb3405c5c8bf6b2ec63",
    (
        "0b9f407f10ab8b12f22526af8a08b870baaef0e9",
        "research/l-families/atlas/function_field/QUADRATIC_FAMILY_NOTCH_PARITY_SIEVE.md",
    ): "38f1b6e95f9a7eb6756450673ff067308886a0ff",
    (
        "4fc8930e14eaa3863d3f3edc151c056d7d5aedce",
        "research/l-families/atlas/function_field/QUADRATIC_FAMILY_NOTCH_DEPTH_PHASE_DIAGRAM.md",
    ): "01cefa8a55c9b1ae1a0b5bed9c11fe323fb6764e",
}

MIN_H = 5
MAX_H = 80
CONTROL_Q = (3, 5, 7)
CONTROL_H = (5, 8, 20)
EXPANDED_H = (5, 6, 7, 8, 20, 40, 80)
MAX_PROFILES = 100_000
MAX_WALL_SECONDS = 3.0


def _fixed_partitions(
    total: int, length: int, minimum: int
) -> tuple[tuple[int, ...], ...]:
    if length < 1 or minimum < 1:
        raise ValueError("partition length and minimum must be positive")
    if length == 1:
        return ((total,),) if total >= minimum else ()
    rows: list[tuple[int, ...]] = []
    for first in range(minimum, total // length + 1):
        for tail in _fixed_partitions(total - first, length - 1, first):
            rows.append((first, *tail))
    return tuple(rows)


def second_boundary_profiles(h_value: int) -> tuple[tuple[int, ...], ...]:
    if isinstance(h_value, bool) or not isinstance(h_value, int) or h_value < MIN_H:
        raise ValueError(f"h must be an integer at least {MIN_H}")
    conductor_degree = 4 * h_value + 1
    minimum_degree = h_value - 1
    rows: list[tuple[int, ...]] = []
    for factor_count in range(2, conductor_degree // minimum_degree + 1):
        for tail in _fixed_partitions(
            conductor_degree - minimum_degree,
            factor_count - 1,
            minimum_degree,
        ):
            rows.append((minimum_degree, *tail))
    return tuple(rows)


def notch_coefficients(profile: tuple[int, ...], h_value: int) -> tuple[int, int]:
    coefficients = [0] * (h_value + 1)
    coefficients[0] = 1
    for degree in profile:
        for index in range(degree, h_value + 1):
            coefficients[index] += coefficients[index - degree]
    return coefficients[h_value - 1], coefficients[h_value]


def classify_profile(h_value: int, profile: tuple[int, ...]) -> dict[str, object]:
    expected_degree = 4 * h_value + 1
    minimum_degree = h_value - 1
    if (
        h_value < MIN_H
        or not profile
        or tuple(sorted(profile)) != profile
        or profile[0] != minimum_degree
        or sum(profile) != expected_degree
    ):
        raise ValueError("profile is not on the declared second boundary")
    minimum_multiplicity = profile.count(minimum_degree)
    h_multiplicity = profile.count(h_value)
    coefficient_minimum, coefficient_h = notch_coefficients(profile, h_value)
    if coefficient_minimum != minimum_multiplicity or coefficient_h != h_multiplicity:
        raise ArithmeticError("second-boundary coefficient reduction failed")

    if h_multiplicity % 2:
        branch = "nonzero_by_parity"
        zero_condition = "impossible because S is odd"
    elif h_multiplicity == 0:
        branch = "primitive_exterior_cubic"
        zero_condition = "D_3=0"
    else:
        exceptional = (h_value - 1, h_value, h_value, h_value + 2)
        if profile != exceptional:
            raise ArithmeticError("even positive m_h escaped the exceptional profile")
        branch = "exceptional_mixed_trace"
        zero_condition = "D_3+2*D_1=0"

    return {
        "h": h_value,
        "M": expected_degree,
        "profile": profile,
        "m_h_minus_1": minimum_multiplicity,
        "m_h": h_multiplicity,
        "residual": f"{minimum_multiplicity}*D_3+{h_multiplicity}*D_1",
        "branch": branch,
        "zero_condition": zero_condition,
    }


def residual_value(
    h_value: int, profile: tuple[int, ...], d1_value: int, d3_value: int
) -> int:
    if d1_value % 2 != 1 or d3_value % 2 != 0:
        raise ValueError("second-boundary parity requires D_1 odd and D_3 even")
    row = classify_profile(h_value, profile)
    return row["m_h_minus_1"] * d3_value + row["m_h"] * d1_value


def _divisors(value: int) -> tuple[int, ...]:
    return tuple(divisor for divisor in range(1, value + 1) if value % divisor == 0)


def _mobius(value: int) -> int:
    remaining = value
    prime_factors = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            prime_factors += 1
            if remaining % divisor == 0:
                return 0
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        prime_factors += 1
    return -1 if prime_factors % 2 else 1


def irreducible_count(q_value: int, degree: int) -> int:
    if q_value < 2 or degree < 1:
        raise ValueError("q and degree must be positive in the irreducible formula")
    numerator = sum(
        _mobius(divisor) * q_value ** (degree // divisor)
        for divisor in _divisors(degree)
    )
    if numerator % degree:
        raise ArithmeticError("irreducible-count numerator is not divisible by degree")
    return numerator // degree


def exceptional_profile_count(q_value: int, h_value: int) -> dict[str, object]:
    if q_value < 3 or q_value % 2 == 0 or h_value < MIN_H:
        raise ValueError("require odd q>=3 and h>=5")
    conductor_degree = 4 * h_value + 1
    count = (
        irreducible_count(q_value, h_value - 1)
        * math.comb(irreducible_count(q_value, h_value), 2)
        * irreducible_count(q_value, h_value + 2)
    )
    bound_denominator = 2 * (h_value - 1) * h_value * h_value * (h_value + 2)
    if count * bound_denominator > q_value**conductor_degree:
        raise ArithmeticError("exceptional-profile upper bound failed")
    return {
        "q": q_value,
        "h": h_value,
        "M": conductor_degree,
        "profile": (h_value - 1, h_value, h_value, h_value + 2),
        "exact_count": count,
        "q_to_M": q_value**conductor_degree,
        "upper_bound_denominator": bound_denominator,
    }


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2.0,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"source blob mismatch: {commit}:{path}")


def build_report() -> dict[str, object]:
    started = time.monotonic()
    profile_count = 0
    aggregate_branches = {
        "nonzero_by_parity": 0,
        "primitive_exterior_cubic": 0,
        "exceptional_mixed_trace": 0,
    }
    rows: list[dict[str, object]] = []
    for h_value in range(MIN_H, MAX_H + 1):
        profiles = second_boundary_profiles(h_value)
        profile_count += len(profiles)
        if profile_count > MAX_PROFILES:
            raise RuntimeError("degree-profile cap exceeded")
        branches = {
            "nonzero_by_parity": 0,
            "primitive_exterior_cubic": 0,
            "exceptional_mixed_trace": 0,
        }
        exceptional_profiles: list[tuple[int, ...]] = []
        for profile in profiles:
            classified = classify_profile(h_value, profile)
            branch = str(classified["branch"])
            branches[branch] += 1
            aggregate_branches[branch] += 1
            if branch == "exceptional_mixed_trace":
                exceptional_profiles.append(profile)
        expected_exceptional = (h_value - 1, h_value, h_value, h_value + 2)
        if exceptional_profiles != [expected_exceptional]:
            raise ArithmeticError("exceptional degree profile is not unique")
        if h_value in EXPANDED_H:
            rows.append(
                {
                    "h": h_value,
                    "n": 2 * h_value + 1,
                    "M": 4 * h_value + 1,
                    "degree_profiles": len(profiles),
                    **branches,
                }
            )

    count_controls = [
        exceptional_profile_count(q_value, h_value)
        for q_value in CONTROL_Q
        for h_value in CONTROL_H
    ]
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return {
        "schema": "riemann.function_field.quadratic_second_boundary_trace_zero.v1",
        "status": "EXACT_SECOND_BOUNDARY_EXTERIOR_CUBIC_REDUCTION",
        "exact_theorem": {
            "scope": "odd prime powers q; odd n=2h+1>=11",
            "residual": "S=m_(h-1)*D_3+m_h*D_1",
            "parity": "D_1 odd, D_3 even, so every zero has even m_h",
            "generic_zero_branch": "m_h=0 and D_3=0",
            "exceptional_zero_branch": ("profile (h-1,h,h,h+2) and D_3+2*D_1=0"),
            "density_firewall": "whole layer O_q(M^-2); exception O_q(M^-4)",
            "remaining_gate": (
                "rough-profile residue-class distribution modulo R_(<=3)"
            ),
        },
        "profile_replay": {
            "h_min": MIN_H,
            "h_max": MAX_H,
            "profiles_checked": profile_count,
            "aggregate_branches": aggregate_branches,
            "rows": rows,
        },
        "exceptional_count_controls": count_controls,
        "resource_ledger": {
            "maximum_profiles": MAX_PROFILES,
            "profiles_checked": profile_count,
            "polynomials_enumerated": 0,
            "irreducibles_enumerated": 0,
            "finite_field_elements_enumerated": 0,
            "l_function_zeros_enumerated": 0,
        },
        "open": [
            "density of D_3=0 residue classes",
            "rough-profile residue-class equidistribution",
            "connected-cumulant zeros",
            "individual L-function zeros, RH, and GRH",
        ],
    }


def run_checks() -> dict[str, object]:
    check_source_blobs()
    report = build_report()
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "exterior-cubic character-zero condition",
        "D_3+2D_1=0",
        "new `c/M` term",
        "finite local residue statistic",
        "no trace-zero density theorem",
        "not zeros of an individual `L`-function",
    ):
        if marker not in note:
            raise RuntimeError(f"note contract marker missing: {marker}")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = run_checks() if args.check else build_report()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
