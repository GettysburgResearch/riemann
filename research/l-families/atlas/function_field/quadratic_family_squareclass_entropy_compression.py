#!/usr/bin/env python3
"""Bounded replay for odd-notch squareclass entropy compression."""

from __future__ import annotations

import argparse
import itertools
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FUNCTION_FIELD_PATH = "research/l-families/atlas/function_field"
SOURCE_COMMIT = "c6d68eaaf3d55e9a9deffcb6e08f3cb5fcdfb7e9"
DISCREPANCY_CONSTANT = 614_400
MAX_FACTORS = 5
SAFE_INPUTS = ((3, 250, 3), (5, 300, 2), (9, 100, 1))
ORBIT_INPUTS = ((2, 3), (3, 4))

SOURCE_BLOBS = {
    (
        SOURCE_COMMIT,
        f"{FUNCTION_FIELD_PATH}/QUADRATIC_FAMILY_PROFILE_CHI_SQUARE_BRIDGE.md",
    ): "8bf123cdc595152eda3030f13705db4df2d7f695",
    (
        SOURCE_COMMIT,
        f"{FUNCTION_FIELD_PATH}/quadratic_family_profile_chi_square_bridge.py",
    ): "43fdb4000656dd958d8636efd3c122ca15174cf5",
    (
        SOURCE_COMMIT,
        f"{FUNCTION_FIELD_PATH}/quadratic_family_profile_chi_square_bridge.json",
    ): "c8a0a340cd57332322cb36ae4f268b8aef6ab86d",
    (
        SOURCE_COMMIT,
        "tests/test_quadratic_family_profile_chi_square_bridge.py",
    ): "c2a0fa71c87096199bfce367793457570a451dc0",
}


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"source blob mismatch: {commit}:{path}")


def _is_prime_power(value: int) -> bool:
    candidate = 3
    while candidate * candidate <= value and value % candidate != 0:
        candidate += 2
    if candidate * candidate > value:
        return True
    remaining = value
    while remaining % candidate == 0:
        remaining //= candidate
    return remaining == 1


def _validate_q(q_value: int) -> None:
    if (
        isinstance(q_value, bool)
        or not isinstance(q_value, int)
        or q_value < 3
        or q_value % 2 == 0
        or not _is_prime_power(q_value)
    ):
        raise ValueError("q must be an odd prime power")


def _validate_h_depth(h_value: int, depth: int) -> None:
    if isinstance(h_value, bool) or not isinstance(h_value, int) or h_value < 2:
        raise ValueError("h must be an integer at least two")
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 1:
        raise ValueError("depth must be a positive integer")
    if h_value - depth <= 2 * depth + 1:
        raise ValueError("the compression requires d=h-j>r=2j+1")


def _divisors(value: int) -> tuple[int, ...]:
    return tuple(divisor for divisor in range(1, value + 1) if value % divisor == 0)


def _mobius(value: int) -> int:
    remaining = value
    parity = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            parity += 1
            if remaining % prime == 0:
                return 0
        prime += 1
    if remaining > 1:
        parity += 1
    return -1 if parity % 2 else 1


def irreducible_count(q_value: int, degree: int) -> int:
    _validate_q(q_value)
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 1:
        raise ValueError("degree must be a positive integer")
    numerator = sum(
        _mobius(divisor) * q_value ** (degree // divisor)
        for divisor in _divisors(degree)
    )
    if numerator % degree:
        raise ArithmeticError("irreducible-count formula lost integrality")
    return numerator // degree


def modulus_degree(q_value: int, top_degree: int) -> int:
    return sum(
        degree * irreducible_count(q_value, degree)
        for degree in range(1, top_degree + 1)
    )


def squareclass_dimension(q_value: int, top_degree: int) -> int:
    return sum(
        irreducible_count(q_value, degree) for degree in range(1, top_degree + 1)
    )


def orbit_coordinate_count(q_value: int, top_degree: int) -> int:
    count = 1
    for degree in range(1, top_degree + 1):
        count *= irreducible_count(q_value, degree) + 1
    return count


def compression_parameters(q_value: int, h_value: int, depth: int) -> dict[str, object]:
    _validate_q(q_value)
    _validate_h_depth(h_value, depth)
    total_degree = 4 * h_value + 1
    top_degree = 2 * depth + 1
    minimum_degree = h_value - depth
    ell = modulus_degree(q_value, top_degree)
    dimension = squareclass_dimension(q_value, top_degree)
    half_squareclass = 1 << (2 * dimension) <= q_value**total_degree
    explicit_safe = q_value ** (total_degree - top_degree) >= (
        2 * DISCREPANCY_CONSTANT * total_degree**11 * (ell + 1) ** 10 * (1 << dimension)
    )
    return {
        "q": q_value,
        "h": h_value,
        "j": depth,
        "M": total_degree,
        "d": minimum_degree,
        "r": top_degree,
        "ell_r": ell,
        "K_r": dimension,
        "full_residue_wall_crossed": ell > total_degree,
        "squareclass_half_wall_safe": half_squareclass,
        "explicit_gate_safe": explicit_safe,
    }


def walsh_transform(values: tuple[int, ...]) -> tuple[int, ...]:
    size = len(values)
    if size < 1 or size & (size - 1):
        raise ValueError("Walsh input length must be a positive power of two")
    transformed = list(values)
    span = 1
    while span < size:
        for start in range(0, size, 2 * span):
            for offset in range(span):
                left = transformed[start + offset]
                right = transformed[start + span + offset]
                transformed[start + offset] = left + right
                transformed[start + span + offset] = left - right
        span *= 2
    return tuple(transformed)


def squareclass_gate(
    counts_by_profile: tuple[tuple[int, ...], ...],
    zero_sets: tuple[tuple[int, ...], ...],
    beta: Fraction,
) -> dict[str, object]:
    if not counts_by_profile or len(counts_by_profile) != len(zero_sets):
        raise ValueError("profiles and zero sets must be nonempty and aligned")
    cube_size = len(counts_by_profile[0])
    if cube_size < 1 or cube_size & (cube_size - 1):
        raise ValueError("profile rows must have squareclass-cube length")
    if any(len(row) != cube_size for row in counts_by_profile):
        raise ValueError("profile rows must have equal length")
    if not 0 <= beta <= 1:
        raise ValueError("beta must lie in [0,1]")
    totals = tuple(sum(row) for row in counts_by_profile)
    if any(total <= 0 for total in totals):
        raise ValueError("each profile must have positive mass")
    for indices in zero_sets:
        if len(set(indices)) != len(indices) or any(
            index < 0 or index >= cube_size for index in indices
        ):
            raise ValueError("zero-set indices are invalid")
        if Fraction(len(indices), cube_size) > beta:
            raise ValueError("a zero set exceeds beta density")

    total = sum(totals)
    zero_total = 0
    discrepancy_squared = Fraction(0)
    parseval_discrepancy = Fraction(0)
    for row, profile_total, indices in zip(
        counts_by_profile, totals, zero_sets, strict=True
    ):
        zero_total += sum(row[index] for index in indices)
        centered_squared = sum(
            (Fraction(value) - Fraction(profile_total, cube_size)) ** 2 for value in row
        )
        discrepancy_squared += Fraction(cube_size, profile_total) * centered_squared
        spectrum = walsh_transform(row)
        parseval_discrepancy += Fraction(
            sum(value * value for value in spectrum[1:]), profile_total
        )
    discrepancy_squared /= total
    parseval_discrepancy /= total
    if discrepancy_squared != parseval_discrepancy:
        raise ArithmeticError("Walsh Parseval identity failed")
    normalized_zero = Fraction(zero_total, total)
    excess = max(Fraction(0), normalized_zero - beta)
    return {
        "cube_size": cube_size,
        "T": total,
        "Z": zero_total,
        "normalized_zero": str(normalized_zero),
        "beta": str(beta),
        "Q_squared": str(discrepancy_squared),
        "parseval_Q_squared": str(parseval_discrepancy),
        "squared_gate_holds": excess * excess <= beta * discrepancy_squared,
    }


def orbit_ledger(degree_sizes: tuple[int, ...]) -> dict[str, object]:
    if not degree_sizes or any(
        isinstance(size, bool) or not isinstance(size, int) or size < 1
        for size in degree_sizes
    ):
        raise ValueError("degree sizes must be positive integers")
    total_variables = sum(degree_sizes)
    if total_variables > 12:
        raise ValueError("orbit replay is capped at twelve variables")
    multiplicities = []
    for weights in itertools.product(*(range(size + 1) for size in degree_sizes)):
        multiplicity = math.prod(
            math.comb(size, weight)
            for size, weight in zip(degree_sizes, weights, strict=True)
        )
        multiplicities.append(multiplicity)
    return {
        "degree_sizes": list(degree_sizes),
        "K": total_variables,
        "orbit_coordinates": len(multiplicities),
        "sum_orbit_multiplicities": sum(multiplicities),
        "squareclass_characters": 1 << total_variables,
        "binomial_identity_holds": sum(multiplicities) == 1 << total_variables,
    }


def run() -> dict[str, object]:
    check_source_blobs()
    finite_gate = squareclass_gate(
        (
            (3, 1, 0, 0, 0, 0, 0, 0),
            (0, 0, 2, 0, 1, 1, 0, 0),
        ),
        ((0, 1), (2, 3)),
        Fraction(1, 4),
    )
    safe_panels = [compression_parameters(*values) for values in SAFE_INPUTS]
    if not all(
        panel["full_residue_wall_crossed"]
        and panel["squareclass_half_wall_safe"]
        and panel["explicit_gate_safe"]
        for panel in safe_panels
    ):
        raise ArithmeticError("the strict compression controls must be safe")
    orbit_panels = [orbit_ledger(values) for values in ORBIT_INPUTS]
    if not all(panel["binomial_identity_holds"] for panel in orbit_panels):
        raise ArithmeticError("orbit multiplicities did not recover the cube")
    return {
        "schema": "quadratic_family_squareclass_entropy_compression.v1",
        "source_commit": SOURCE_COMMIT,
        "theorems": {
            "full_unit_characters_replaced_by_quadratic_squareclasses": True,
            "squareclass_fourier_support_size": "2^K_r",
            "discrepancy_constant": DISCREPANCY_CONSTANT,
            "half_squareclass_wall_implies_gate_asymptotically": True,
            "depth_extension": "log_q(M)+log_q(log(M))+O_q(1)",
            "krawtchouk_projection_exact": True,
            "constituent_triangle_bound_recovers_2^K_r": True,
        },
        "finite_gate": finite_gate,
        "strict_compression_controls": safe_panels,
        "orbit_ledgers": orbit_panels,
        "open_gate": {
            "name": "KRAWLS",
            "proved": False,
            "conditional_orbit_entropy": "R_r=product_e(I_q(e)+1)",
            "conditional_scale": "for fixed eps>0, r<(sqrt(2)-eps)*sqrt(M)",
        },
        "claim_boundary": {
            "individual_L_function_zero": False,
            "integer_rh_or_grh": False,
            "number_field_transfer": False,
            "external_novelty": False,
            "unconditional_mesoscopic_depth": False,
        },
        "resource_caps": {
            "maximum_irreducible_degree": 7,
            "maximum_finite_cube_size": 8,
            "maximum_orbit_variables": 7,
            "polynomials_enumerated": 0,
            "irreducibles_enumerated": 0,
            "characters_enumerated": 0,
            "conductors_enumerated": 0,
            "zeros_enumerated": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = run()
    artifact_path = HERE / "quadratic_family_squareclass_entropy_compression.json"
    canonical = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.check:
        if not artifact_path.exists():
            raise FileNotFoundError(artifact_path)
        if artifact_path.read_text(encoding="utf-8") != canonical:
            raise RuntimeError("stored squareclass artifact is stale")
    print(canonical, end="")


if __name__ == "__main__":
    main()
