#!/usr/bin/env python3
"""Bounded exact replay for closed-point Adams compression.

The proof is in the companion note.  This script checks divisor inversion on
synthetic exact Frobenius eigenvalue packets and finite-abelian character
profiles.  It enumerates no finite field, polynomial, place, curve,
L-function, or zero.
"""

from __future__ import annotations

import argparse
import itertools
import json
import subprocess
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_CLOSED_POINT_ADAMS_COMPRESSION.md"
JSON_PATH = HERE / "ffps_closed_point_adams_compression.json"

SOURCE_BLOBS = {
    (
        "464c3705f",
        "research/l-families/atlas/function_field/FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md",
    ): "ab16e6c0894e51303119692e67b2f2bf59ba73e4",
    (
        "961603fd0",
        "research/l-families/atlas/function_field/FFPS_RELATIVE_BOUNDARY_TRACE_TOWER_GATE.md",
    ): "cc8b649848a2e7425989a553628d9c830f56f6d1",
    (
        "691166b8c",
        "research/l-families/atlas/function_field/FFPS_EXACT_CYCLE_SELECTOR_MASS_NO_GO.md",
    ): "d136159ea9f0fa41600e673dc2c6ef1a2ad2f10f",
    (
        "c81e69db1",
        "research/l-families/atlas/function_field/FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md",
    ): "1cb3c9613308474e9ad80de4d8d18e86a18a1b97",
}

MAX_DEGREE = 12
KERNEL_COEFFICIENTS = (Fraction(1), Fraction(2), Fraction(-1, 3))


def validate_positive_integer(value: int, name: str = "value") -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")


def divisors(value: int) -> tuple[int, ...]:
    validate_positive_integer(value)
    return tuple(divisor for divisor in range(1, value + 1) if value % divisor == 0)


def mobius(value: int) -> int:
    validate_positive_integer(value)
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


def divisor_count(value: int) -> int:
    return len(divisors(value))


def selector_mass(left_degree: int, right_degree: int) -> Fraction:
    validate_positive_integer(left_degree, "left degree")
    validate_positive_integer(right_degree, "right degree")
    return Fraction(2 ** (left_degree + right_degree - 2), left_degree * right_degree)


def _point_count(degree: int) -> int:
    return 1 + degree % 2


def _synthetic_eigenvalues(
    term: int, side: int, degree: int, point: int
) -> tuple[int, ...]:
    """Small exact eigenvalue packet for one synthetic closed point."""

    if term not in range(len(KERNEL_COEFFICIENTS)):
        raise ValueError("synthetic kernel term is out of range")
    if side not in (0, 1):
        raise ValueError("synthetic side must be zero or one")
    if point not in range(_point_count(degree)):
        raise ValueError("synthetic closed-point index is out of range")
    first = ((term + 2 * side + degree + point) % 5) - 2
    second = ((2 * term + side + degree + 2 * point) % 5) - 2
    return (first, second)


def _point_trace(term: int, side: int, degree: int, point: int, power: int) -> int:
    validate_positive_integer(power, "Adams power")
    return sum(
        eigenvalue**power
        for eigenvalue in _synthetic_eigenvalues(term, side, degree, point)
    )


def synthetic_prime_trace(term: int, side: int, degree: int, power: int) -> int:
    return sum(
        _point_trace(term, side, degree, point, power)
        for point in range(_point_count(degree))
    )


def synthetic_point_sum(term: int, side: int, extension: int, power: int) -> int:
    """A_extension(psi^power V) from the exact closed-orbit expansion."""

    return sum(
        degree * synthetic_prime_trace(term, side, degree, power * extension // degree)
        for degree in divisors(extension)
    )


def one_place_inversion(degree: int, term: int, side: int, power: int = 1) -> int:
    return sum(
        mobius(adams) * synthetic_point_sum(term, side, degree // adams, power * adams)
        for adams in divisors(degree)
    )


def synthetic_pair_prime_trace(
    left_degree: int,
    right_degree: int,
    left_power: int = 1,
    right_power: int = 1,
) -> Fraction:
    return sum(
        coefficient
        * synthetic_prime_trace(term, 0, left_degree, left_power)
        * synthetic_prime_trace(term, 1, right_degree, right_power)
        for term, coefficient in enumerate(KERNEL_COEFFICIENTS)
    )


def synthetic_separable_point_sum(
    left_extension: int,
    right_extension: int,
    left_power: int,
    right_power: int,
) -> Fraction:
    return sum(
        coefficient
        * synthetic_point_sum(term, 0, left_extension, left_power)
        * synthetic_point_sum(term, 1, right_extension, right_power)
        for term, coefficient in enumerate(KERNEL_COEFFICIENTS)
    )


def two_place_inversion(
    left_degree: int,
    right_degree: int,
    left_power: int = 1,
    right_power: int = 1,
) -> Fraction:
    return sum(
        mobius(left_adams)
        * mobius(right_adams)
        * synthetic_separable_point_sum(
            left_degree // left_adams,
            right_degree // right_adams,
            left_power * left_adams,
            right_power * right_adams,
        )
        for left_adams in divisors(left_degree)
        for right_adams in divisors(right_degree)
    )


def synthetic_diagonal_prime_trace(degree: int, power: int = 1) -> Fraction:
    """P_degree(delta K) for the synthetic external kernel."""

    return sum(
        coefficient
        * sum(
            _point_trace(term, 0, degree, point, power)
            * _point_trace(term, 1, degree, point, power)
            for point in range(_point_count(degree))
        )
        for term, coefficient in enumerate(KERNEL_COEFFICIENTS)
    )


def synthetic_diagonal_point_sum(extension: int, power: int) -> Fraction:
    return sum(
        degree * synthetic_diagonal_prime_trace(degree, power * extension // degree)
        for degree in divisors(extension)
    )


def diagonal_inversion(degree: int, power: int = 1) -> Fraction:
    return sum(
        mobius(adams) * synthetic_diagonal_point_sum(degree // adams, power * adams)
        for adams in divisors(degree)
    )


Character = tuple[int, int, int, int, int, int]


def physical_adams_profile(
    left_adams: int,
    right_adams: int,
    *,
    alignment: int = 1,
    modes: tuple[int, ...] = (0, 1, 2),
) -> Counter[Character]:
    """Multiplicity profile after two partial Adams operations.

    A key is (alpha_X1, alpha_X2, alpha_Y1, alpha_Y2, cubic_X,
    cubic_Y), with quadratic entries modulo two and cubic entries modulo
    three.
    """

    validate_positive_integer(left_adams, "left Adams power")
    validate_positive_integer(right_adams, "right Adams power")
    if alignment not in (-1, 1):
        raise ValueError("alignment must be plus or minus one")
    if not modes or any(mode not in (0, 1, 2) for mode in modes):
        raise ValueError("cubic modes must be a nonempty subset of 0,1,2")
    profile: Counter[Character] = Counter()
    for left_bits in itertools.product(range(2), repeat=2):
        for right_bits in itertools.product(range(2), repeat=2):
            for mode in modes:
                key = (
                    *(left_adams * bit % 2 for bit in left_bits),
                    *(right_adams * bit % 2 for bit in right_bits),
                    left_adams * mode % 3,
                    alignment * right_adams * mode % 3,
                )
                profile[key] += 1
    return profile


def complexity_panel(left_degree: int, right_degree: int) -> dict[str, object]:
    left_tau = divisor_count(left_degree)
    right_tau = divisor_count(right_degree)
    diagonal_terms = left_tau if left_degree == right_degree else 0
    cycle_mass = selector_mass(left_degree, right_degree)
    return {
        "left_degree": left_degree,
        "right_degree": right_degree,
        "divisor_pair_terms": left_tau * right_tau,
        "distinct_diagonal_terms": diagonal_terms,
        "regular_character_line_evaluations": 48
        * (left_tau * right_tau + diagonal_terms),
        "coefficient_space_selector_mass": str(cycle_mass),
        "coefficient_space_regular_rank_mass": str(48 * cycle_mass),
    }


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3.0,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"source blob mismatch: {commit}:{path}")


def run_exact_checks() -> dict[str, int]:
    one_place_checks = 0
    two_place_checks = 0
    diagonal_checks = 0
    character_checks = 0
    for degree in range(1, MAX_DEGREE + 1):
        for term in range(len(KERNEL_COEFFICIENTS)):
            for side in (0, 1):
                for power in (1, 2):
                    recovered = one_place_inversion(degree, term, side, power)
                    expected = degree * synthetic_prime_trace(term, side, degree, power)
                    if recovered != expected:
                        raise ArithmeticError("one-place Adams inversion failed")
                    one_place_checks += 1
        recovered_diagonal = diagonal_inversion(degree)
        expected_diagonal = degree * synthetic_diagonal_prime_trace(degree)
        if recovered_diagonal != expected_diagonal:
            raise ArithmeticError("diagonal Adams inversion failed")
        diagonal_checks += 1
        for right_degree in range(1, MAX_DEGREE + 1):
            recovered_pair = two_place_inversion(degree, right_degree)
            expected_pair = (
                degree * right_degree * synthetic_pair_prime_trace(degree, right_degree)
            )
            if recovered_pair != expected_pair:
                raise ArithmeticError("two-place Adams inversion failed")
            two_place_checks += 1
    for left_adams in range(1, MAX_DEGREE + 1):
        for right_adams in range(1, MAX_DEGREE + 1):
            for alignment in (-1, 1):
                regular = physical_adams_profile(
                    left_adams, right_adams, alignment=alignment
                )
                selected = physical_adams_profile(
                    left_adams,
                    right_adams,
                    alignment=alignment,
                    modes=(1, 2),
                )
                relative = physical_adams_profile(
                    left_adams,
                    right_adams,
                    alignment=alignment,
                    modes=(0,),
                )
                if sum(regular.values()) != 48:
                    raise ArithmeticError("regular Adams rank changed")
                if sum(selected.values()) != 32:
                    raise ArithmeticError("selected Adams rank changed")
                if sum(relative.values()) != 16:
                    raise ArithmeticError("relative Adams rank changed")
                if regular != selected + relative:
                    raise ArithmeticError("hard-selected relative profile failed")
                character_checks += 1
    return {
        "one_place_inversions": one_place_checks,
        "two_place_inversions": two_place_checks,
        "diagonal_inversions": diagonal_checks,
        "partial_adams_profiles": character_checks,
    }


def build_report() -> dict[str, object]:
    checks = run_exact_checks()
    panels = [
        complexity_panel(left, right)
        for left, right in ((3, 5), (8, 8), (11, 12), (12, 12))
    ]
    return {
        "schema": "riemann.function_field.ffps_closed_point_adams_compression.v1",
        "status": "EXACT_CLOSED_POINT_ADAMS_COMPRESSION",
        "identities": {
            "one_place": "d P_d(V) = sum_{e|d} mu(e) A_{d/e}(psi^e V)",
            "two_place": "ab P_{a,b}(K) = sum_{e|a,f|b} mu(e)mu(f) A_sep_{a/e,b/f}(psi_1^e psi_2^f K)",
            "equal_degree_distinct": "P_ne_{a,a}(K)=P_{a,a}(K)-P_a(delta K)",
        },
        "category_gate": "finite external-product trace kernel or commuting partial Frobenii",
        "physical_adams_ranks": {
            "regular": 48,
            "selected_underlying": 32,
            "relative": 16,
            "hard_underlying": 48,
            "selected_weighted_line_mass": 8,
            "hard_weighted_line_mass": 24,
        },
        "complexity_panels": panels,
        "exact_checks": checks,
        "resource_ledger": {
            "max_degree": MAX_DEGREE,
            "finite_fields_enumerated": 0,
            "polynomials_enumerated": 0,
            "closed_places_enumerated": 0,
            "source_atoms_enumerated": 0,
        },
        "not_proved": [
            "native owner-Boolean-Artin-Schreier separable FFPS adapter",
            "uniform pushed-forward Betti or signed trace estimate",
            "CYSEL, WCADD106140, WCKUM106140, RH, or GRH",
        ],
    }


def run_checks() -> dict[str, object]:
    check_source_blobs()
    report = build_report()
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "extension-field recombination",
        "one diagonal Frobenius structure",
        "underlying ranks 32 and 16",
        "native owner/Boolean/Artin--Schreier separable adapter | **NOT CONSTRUCTED**",
        "RH, or GRH | **NOT PROVED**",
    ):
        if marker not in note:
            raise RuntimeError(f"note scope firewall missing: {marker}")
    canonical = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    if report != canonical:
        raise RuntimeError("canonical JSON does not match exact replay")
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        parser.error("choose --check")
    print(json.dumps(run_checks(), indent=2))


if __name__ == "__main__":
    main()
