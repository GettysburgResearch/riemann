#!/usr/bin/env python3
"""Bounded exact replay for the universal ternary norm-torsor packet.

The proof is in the companion note.  This script checks only integer exponent
vectors, rational cycle-selector masses, and fixed rank/conductor ledgers.  It
enumerates no finite field, polynomial, place, curve, L-function, or zero.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md"
JSON_PATH = HERE / "ffps_ternary_universal_norm_torsor.json"

SOURCE_BLOBS = {
    (
        "8b4559a54",
        "research/l-families/atlas/function_field/FFPS_CYCLIC_SHEAF_INVARIANT_AUDIT.md",
    ): "d531ef36d314549072052cc5b1ae1762c11d00e2",
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
}

MAX_DEGREE = 8
ORIENTATION_DEGREE = 16
CUBIC_REGULAR_RANK = 3
FULL_PHYSICAL_RANK = ORIENTATION_DEGREE * CUBIC_REGULAR_RANK
SELECTED_PHYSICAL_RANK = ORIENTATION_DEGREE * 2
RELATIVE_PHYSICAL_RANK = ORIENTATION_DEGREE


def validate_degree(degree: int) -> None:
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 1:
        raise ValueError("place degree must be a positive integer")


def _prime_factorization(value: int) -> dict[int, int]:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        raise ValueError("field cardinality must be an integer at least two")
    remaining = value
    factors: dict[int, int] = {}
    prime = 2
    while prime * prime <= remaining:
        while remaining % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            remaining //= prime
        prime += 1
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def validate_base_cardinality(cardinality: int) -> None:
    factors = _prime_factorization(cardinality)
    if len(factors) != 1:
        raise ValueError("field cardinality must be a prime power")
    if cardinality % 6 != 1:
        raise ValueError("ternary split norm-torsor requires q congruent to 1 mod 6")


def selector_rank_mass(degree: int) -> Fraction:
    """Absolute semisimple rank mass of the exact d-cycle selector."""

    validate_degree(degree)
    return Fraction(2 ** (degree - 1), degree)


def product_selector_rank_mass(left_degree: int, right_degree: int) -> Fraction:
    return selector_rank_mass(left_degree) * selector_rank_mass(right_degree)


def toric_boundary_components(left_degree: int, right_degree: int) -> int:
    validate_degree(left_degree)
    validate_degree(right_degree)
    return 6 * (left_degree + right_degree)


def regular_conductor_bound(left_degree: int, right_degree: int) -> int:
    return FULL_PHYSICAL_RANK * toric_boundary_components(left_degree, right_degree)


def physical_exponent_vector(
    left_degree: int, right_degree: int, mode: int, alignment: int
) -> tuple[int, ...]:
    """Order-six exponents of the descended physical selected line.

    Coordinate order is X1, X2, Y1, Y2 after geometric splitting.  Entries
    are reduced modulo six.
    """

    validate_degree(left_degree)
    validate_degree(right_degree)
    if mode not in (1, 2):
        raise ValueError("ternary selected mode must be one or two")
    if alignment not in (-1, 1):
        raise ValueError("relative alignment must be plus or minus one")
    return (
        *((mode % 6,) * left_degree),
        *((-mode % 6,) * left_degree),
        *((alignment * mode % 6,) * right_degree),
        *((-alignment * mode % 6,) * right_degree),
    )


def descended_invariant_multiplicity(*, is_cube: bool, is_sixth_power: bool) -> int:
    """Invariant count for xi(F) plus xi^2(F) on the physical base."""

    if is_sixth_power and not is_cube:
        raise ValueError("every sixth power is a cube")
    return int(is_sixth_power) + int(is_cube)


def oriented_invariant_multiplicity(*, orientation_unit_is_cube: bool) -> int:
    """Invariant count for the two faithful cubic lines on the norm cover."""

    return 2 if orientation_unit_is_cube else 0


def degree_panel(left_degree: int, right_degree: int) -> dict[str, object]:
    boundary = toric_boundary_components(left_degree, right_degree)
    selector_mass = product_selector_rank_mass(left_degree, right_degree)
    plus_mode_one = physical_exponent_vector(left_degree, right_degree, 1, 1)
    minus_mode_two = physical_exponent_vector(left_degree, right_degree, 2, -1)
    if any(exponent == 0 for exponent in plus_mode_one):
        raise ArithmeticError("faithful order-six mode lost a generic coordinate")
    if any(exponent == 0 for exponent in minus_mode_two):
        raise ArithmeticError("faithful cubic mode lost a generic coordinate")
    if len(plus_mode_one) != 2 * (left_degree + right_degree):
        raise ArithmeticError("geometric exponent-vector length mismatch")
    return {
        "left_degree": left_degree,
        "right_degree": right_degree,
        "selected_norm_exponent_coordinates": len(plus_mode_one),
        "orientation_base_coordinates": 3 * (left_degree + right_degree),
        "toric_boundary_components": boundary,
        "regular_conductor_bound": regular_conductor_bound(left_degree, right_degree),
        "selector_rank_mass": str(selector_mass),
        "canonical_termwise_rank_masses": {
            "regular": str(FULL_PHYSICAL_RANK * selector_mass),
            "selected": str(SELECTED_PHYSICAL_RANK * selector_mass),
            "relative": str(RELATIVE_PHYSICAL_RANK * selector_mass),
        },
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


def build_report() -> dict[str, object]:
    panels = [
        degree_panel(left_degree, right_degree)
        for left_degree in range(1, MAX_DEGREE + 1)
        for right_degree in range(1, MAX_DEGREE + 1)
    ]
    if descended_invariant_multiplicity(is_cube=False, is_sixth_power=False) != 0:
        raise ArithmeticError("generic descended invariant count must vanish")
    if descended_invariant_multiplicity(is_cube=True, is_sixth_power=False) != 1:
        raise ArithmeticError("cube-only descended invariant count must be one")
    if descended_invariant_multiplicity(is_cube=True, is_sixth_power=True) != 2:
        raise ArithmeticError("sixth-power descended invariant count must be two")
    if oriented_invariant_multiplicity(orientation_unit_is_cube=False) != 0:
        raise ArithmeticError("generic oriented invariant count must vanish")
    if oriented_invariant_multiplicity(orientation_unit_is_cube=True) != 2:
        raise ArithmeticError("resonant oriented invariant count must be two")
    for cardinality in (7, 13, 25, 49):
        validate_base_cardinality(cardinality)
    return {
        "schema": "riemann.function_field.ffps_ternary_universal_norm_torsor.v1",
        "status": "EXACT_VARYING_PLACE_NORM_TORSOR_NORMAL_FORM",
        "base_condition": "q is a prime power congruent to 1 modulo 6",
        "universal_physical_ranks": {
            "orientation_cover_degree": ORIENTATION_DEGREE,
            "cubic_regular_rank": CUBIC_REGULAR_RANK,
            "regular_pushforward": FULL_PHYSICAL_RANK,
            "selected_pushforward": SELECTED_PHYSICAL_RANK,
            "relative_pushforward": RELATIVE_PHYSICAL_RANK,
        },
        "invariant_law": {
            "oriented": "2 iff U is a cube, otherwise 0",
            "physical_descent": "1_[F sixth]+1_[F cube]",
            "generic": 0,
        },
        "degree_panels": panels,
        "resource_ledger": {
            "max_degree": MAX_DEGREE,
            "degree_pairs": len(panels),
            "finite_fields_enumerated": 0,
            "polynomials_enumerated": 0,
            "places_enumerated": 0,
        },
        "not_proved": [
            "full owner-Boolean-Artin-Schreier FFPS source adapter",
            "joint cancellation of the exact cycle-selector mass",
            "uniform pushed-forward Betti or signed trace estimate",
            "CYSEL, WCADD106140, WCKUM106140, RH, or GRH",
        ],
    }


def run_checks() -> dict[str, object]:
    check_source_blobs()
    report = build_report()
    if report["resource_ledger"]["degree_pairs"] != MAX_DEGREE**2:
        raise ArithmeticError("degree-pair replay count changed")
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "one varying-closed-place physical",
        "rank \\(48\\)",
        "linear toric",
        "full owner/Boolean/phase FFPS source adapter | **NOT CONSTRUCTED**",
        "RH, or GRH | **NOT PROVED**",
    ):
        if marker not in note:
            raise RuntimeError(f"note firewall missing: {marker}")
    return report


def write_report(report: dict[str, object]) -> None:
    JSON_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if not args.check and not args.write:
        parser.error("choose --check or --write")
    report = run_checks()
    if args.write:
        write_report(report)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
