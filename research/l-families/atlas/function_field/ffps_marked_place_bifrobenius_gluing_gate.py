#!/usr/bin/env python3
"""Bounded exact replay for the marked-place bifrobenius gluing gate."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

SOURCE_BLOBS = {
    (
        "98af0db6e",
        "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ): "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (
        "98af0db6e",
        "claims/lemmas/L-106131-wick-normal-ordering-additive-kummer-decomposition.md",
    ): "37722c3f36ec7d1681f34d4329a3795e5028f7ae",
    (
        "98af0db6e",
        "claims/lemmas/L-106191-source-dual-centered-double-incidence-correlation.md",
    ): "85c4ef92ead7d8b235f9c195c3c0acd16d16030f",
    (
        "98af0db6e",
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
    ): "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
    (
        "05da4d1705d994dd02d650f321196f8464034ba8",
        "research/l-families/atlas/function_field/FFPS_CLOSED_POINT_ADAMS_COMPRESSION.md",
    ): "c79e52ebf0099fe416bc2c79dcb041cc21e025fb",
    (
        "9ced25befb6dd88146809866a34a15fec034b096",
        "research/l-families/atlas/function_field/FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md",
    ): "21645bdb609320cf176893aa589af7a17c741d9a",
    (
        "e3903136912402a969abee7bfcf1ad5f9dfbd1a0",
        "research/l-families/atlas/function_field/FFPS_NATIVE_PARTIAL_FROBENIUS_VERDICT.md",
    ): "19939eb240ca6b2b6d5221954cec76fe0f5c4f9c",
    (
        "8192514ed68f50b8e2a9cff9e1bedab2478bb5c1",
        "research/l-families/atlas/function_field/FFPS_TERNARY_RELATIVE_CORRESPONDENCE_NORMAL_FORM.md",
    ): "4ee3c50f3cce3e7aa2dbd901b93fd50b713ea4bb",
    (
        "9c95eb3684dfd280e07b48fd5dca5f9efa716349",
        "research/l-families/atlas/function_field/FFPS_FROBENIUS_EXTENSION_TOWER_ALIASING.md",
    ): "3d16de5cf8b099b8348c470befcda6c6050aad9e",
    (
        "5c9462064aefe43164fcf5bc0b6d76b575e67a49",
        "research/l-families/atlas/function_field/FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md",
    ): "e7cb9133bb6b57ddbb1c7f1e350f1d2d0af7bd1a",
    (
        "464c3705fd9418be8fc03488109cc24dab6f5efd",
        "research/l-families/atlas/function_field/FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md",
    ): "ab16e6c0894e51303119692e67b2f2bf59ba73e4",
}

CONTROL_Q_LEFT = 5
CONTROL_CELLS_LEFT = 2
CONTROL_Q_RIGHT = 7
CONTROL_CELLS_RIGHT = 3
MAX_EXACT_MATRIX_DIMENSION = max(CONTROL_CELLS_LEFT**2, CONTROL_CELLS_RIGHT**2)


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def validate_positive_integer(value: int, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{label} must be a positive integer")


def divisors(value: int) -> tuple[int, ...]:
    validate_positive_integer(value, "value")
    return tuple(divisor for divisor in range(1, value + 1) if value % divisor == 0)


def mobius(value: int) -> int:
    validate_positive_integer(value, "value")
    remaining = value
    prime_count = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            prime_count += 1
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def irreducible_count(q: int, degree: int) -> int:
    validate_positive_integer(q, "q")
    validate_positive_integer(degree, "degree")
    if q < 2:
        raise ValueError("q must be at least two")
    numerator = sum(mobius(e) * q ** (degree // e) for e in divisors(degree))
    if numerator % degree:
        raise ArithmeticError("irreducible-count numerator is not divisible by degree")
    return numerator // degree


def centered_incidence(
    residue_size: int, cell_count: int
) -> tuple[tuple[int, ...], ...]:
    validate_positive_integer(residue_size, "residue size")
    validate_positive_integer(cell_count, "cell count")
    if cell_count > residue_size:
        raise ValueError("cell count cannot exceed residue size")
    return tuple(
        tuple(residue_size * int(row == column) - 1 for column in range(cell_count))
        for row in range(cell_count)
    )


def matrix_rank(matrix: tuple[tuple[int | Fraction, ...], ...]) -> int:
    if not matrix or not matrix[0]:
        return 0
    column_count = len(matrix[0])
    if any(len(row) != column_count for row in matrix):
        raise ValueError("matrix must be rectangular")
    working = [[Fraction(entry) for entry in row] for row in matrix]
    rank = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(rank, len(working)) if working[row][column]),
            None,
        )
        if pivot is None:
            continue
        working[rank], working[pivot] = working[pivot], working[rank]
        pivot_value = working[rank][column]
        working[rank] = [entry / pivot_value for entry in working[rank]]
        for row in range(len(working)):
            if row == rank or not working[row][column]:
                continue
            multiplier = working[row][column]
            working[row] = [
                entry - multiplier * pivot_entry
                for entry, pivot_entry in zip(working[row], working[rank], strict=True)
            ]
        rank += 1
        if rank == len(working):
            break
    return rank


def flatten(matrix: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(entry for row in matrix for entry in row)


def outer_product(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[tuple[int, ...], ...]:
    if not left or not right:
        raise ValueError("outer-product vectors must be nonempty")
    return tuple(tuple(a * b for b in right) for a in left)


def marked_block_correction_control() -> dict[str, object]:
    left = centered_incidence(CONTROL_Q_LEFT, CONTROL_CELLS_LEFT)
    right = centered_incidence(CONTROL_Q_RIGHT, CONTROL_CELLS_RIGHT)
    left_rank = matrix_rank(left)
    right_rank = matrix_rank(right)
    block_table = outer_product(flatten(left), flatten(right))
    block_rank = matrix_rank(block_table)
    if (left_rank, right_rank, block_rank) != (2, 3, 1):
        raise ArithmeticError("marked-block rank correction failed")
    return {
        "internal_left_matrix_rank": left_rank,
        "internal_right_matrix_rank": right_rank,
        "marked_place_block_separation_rank": block_rank,
        "left_block_coordinate_count": len(flatten(left)),
        "right_block_coordinate_count": len(flatten(right)),
        "meaning": (
            "large rank in the two atom coordinates inside either marked-place "
            "block does not imply large separation rank across the ell|rho blocks"
        ),
    }


def simultaneous_frobenius_control(q: int) -> dict[str, object]:
    validate_positive_integer(q, "q")
    if q < 2:
        raise ValueError("q must be at least two")
    diagonal = ((1, 0), (0, 1))
    one_axis = ((q, 0), (0, 1))
    simultaneous = ((q, 0), (0, q))
    return {
        "q": q,
        "artin_schreier_monomial": "h*Y",
        "simultaneous_image": "(h*Y)^q",
        "one_axis_h_image": "h^q*Y",
        "one_axis_Y_image": "h*Y^q",
        "trace_invariant_under_simultaneous_block_frobenius": True,
        "diagonal_support": diagonal,
        "one_axis_diagonal_support": one_axis,
        "simultaneous_diagonal_support": simultaneous,
        "simultaneous_reduced_support_preserved": True,
        "one_axis_reduced_support_preserved": diagonal == one_axis,
    }


def crossed_incidence_control(q: int) -> dict[str, object]:
    validate_positive_integer(q, "q")
    if q < 2:
        raise ValueError("q must be at least two")
    original = ((1, 0), (0, 1))
    root_only = ((q, 0), (0, 1))
    coefficient_only = ((1, 0), (0, q))
    if original == root_only or original == coefficient_only:
        raise ArithmeticError("crossed incidence unexpectedly stayed fixed")
    return {
        "universal_linear_incidence": "F_A(T)=T-A with alpha=A",
        "root_only_pullback_equation": "alpha^q-A=0",
        "coefficient_only_pullback_equation": "alpha-A^q=0",
        "original_support": original,
        "root_only_support": root_only,
        "coefficient_only_support": coefficient_only,
        "root_only_support_preserved": False,
        "coefficient_only_support_preserved": False,
        "allocation_trilemma": [
            {
                "allocation": "core c on rho/evaluation block",
                "crossed_object": "ell divides c (and the least-place selector)",
            },
            {
                "allocation": "core c on ell/selector block",
                "crossed_object": "evaluation and nonincidence of c at rho",
            },
            {
                "allocation": "duplicate c on both blocks",
                "crossed_object": "the equality diagonal c_ell=c_rho",
            },
        ],
    }


def frozen_source_cost_panel() -> dict[str, object]:
    rows = []
    for degree in range(1, 7):
        count = irreducible_count(3, degree)
        rows.append(
            {
                "degree": degree,
                "irreducible_place_count": count,
                "identity_incidence_submatrix_rank": count,
            }
        )
    return {
        "q": 3,
        "rows": rows,
        "conditional_scope": (
            "the identity-rank lower bound applies when a universal adapter "
            "retains one nonzero c=ell row for every place in the degree shell; "
            "it is not an occupancy theorem for the final live source"
        ),
        "finite_horizon_escape": (
            "freezing every F_q source label as a separate zero-dimensional "
            "summand supplies formal partial Frobenius but pays source-cardinality rank"
        ),
    }


def graph_shift_control() -> dict[str, object]:
    q = 3
    depth = 5
    signatures = [(q**n, 1) for n in range(depth + 1)]
    if len(set(signatures)) != depth + 1:
        raise ArithmeticError("graph-shift supports collided")
    a = 30
    b = 42
    left_nonzero = sum(1 for e in divisors(a) if mobius(e))
    right_nonzero = sum(1 for f in divisors(b) if mobius(f))
    return {
        "q": q,
        "graph_signatures": signatures,
        "distinct_through_depth": depth,
        "divisor_example": {"a": a, "b": b},
        "left_nonzero_mobius_slots": left_nonzero,
        "right_nonzero_mobius_slots": right_nonzero,
        "double_nonzero_mobius_slots": left_nonzero * right_nonzero,
        "firewall": (
            "support-symbol sparsity is not a closed-point trace theorem: a valid "
            "correspondence category must also transport extension level, Adams "
            "powers of stalk eigenvalues, Tate scalars, and cleanup cones"
        ),
    }


def source_factor_partition() -> dict[str, object]:
    return {
        "marked_place_blocks": {
            "ell": ["ell", "h", "Y=Q*d^2 mod ell", "Y'", "ell-incidence"],
            "rho": ["rho", "k", "X=P*c^2 mod rho", "X'", "rho-incidence"],
        },
        "crossed_edges": [
            "ell=P^-(c), while c also supplies X on the rho block",
            "rho=P^-(d), while d also supplies Y on the ell block",
            "the common core g is shared by both source sides",
            "coprimality, Boolean, shell, owner/core, and cleanup relations couple the sides",
        ],
        "local_constituent_verdict": (
            "the Artin-Schreier and centered-incidence constituents are not by "
            "themselves marked-place partial-Frobenius obstructions when all "
            "coordinates belonging to one place move simultaneously"
        ),
    }


def minimum_gluing_datum() -> list[str]:
    return [
        "one common pushed-forward native class K_nat on the ordered marked-place base",
        "commuting ell- and rho-partial Frobenius structures with the correct cocycle",
        "all independent extension-degree traces equal to the literal native source",
        "the product of the two partial Frobenii equals ordinary total Frobenius",
        "common equivariant hard/selected projectors realizing C-S=Pi_0",
        "common equivariant atomic, equal-product, root, owner/core, incidence, and resonant cleanup cones",
        "the signed varying-conductor recombination before every norm or absolute value",
        "uniform complexity bounds for every partial Adams transform after pushforward",
    ]


def run(check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    return {
        "status": (
            "exact marked-place axis correction and natural universal-source "
            "allocation obstruction; no absolute no-go after signed pushforward"
        ),
        "source_contract": {
            "git_blobs": {
                f"{commit}:{path}": blob
                for (commit, path), blob in SOURCE_BLOBS.items()
            },
            "factor_partition": source_factor_partition(),
        },
        "correction_theorem": marked_block_correction_control(),
        "simultaneous_block_frobenius": simultaneous_frobenius_control(3),
        "crossed_core_gluing": crossed_incidence_control(3),
        "frozen_source_cost": frozen_source_cost_panel(),
        "minimum_bifrobenius_gluing_datum": minimum_gluing_datum(),
        "conditional_signed_pushforward_frontier": {
            "natural_raw_coordinatewise_lift": "OBSTRUCTED BY CROSSED INCIDENCE",
            "finite_frozen_source_lift": "FORMALLY AVAILABLE WITH SOURCE-CARDINALITY COST",
            "exotic_structure_after_complete_signed_pushforward": "OPEN / NOT RULED OUT",
            "complete_native_relative_complex": "NOT CONSTRUCTED",
        },
        "correspondence_escape": graph_shift_control(),
        "proof_ledger": {
            "internal_QI_minus_J_rank": "RETAINED EXACT FROM THE PREDECESSOR",
            "internal_rank_implies_marked_place_nonseparability": "REFUTED BY THE BLOCK OUTER-PRODUCT CONTROL",
            "one_axis_AS_and_diagonal_obstructions": "RETAINED BUT NOT THE MARKED-PLACE ADAMS AXES",
            "simultaneous_marked_block_frobenius": "PROVED FORMALLY FOR THE LOCAL AS AND DIAGONAL CONSTITUENTS",
            "crossed_universal_divisor_incidence_failure": "PROVED BY DISTINCT SUPPORT",
            "coordinate_allocation_trilemma": "PROVED FOR THE NATURAL RAW UNIVERSALIZATION",
            "full_native_external_product": "NOT CONSTRUCTED",
            "full_native_commuting_partial_frobenii": "NOT CONSTRUCTED",
            "absolute_nonexistence_after_signed_pushforward": "NOT PROVED",
            "correspondence_level_closed_point_formula": "NOT CONSTRUCTED",
            "uniform_betti_or_trace_estimate": "NOT PROVED",
            "CYSEL_WCADD_WCKUM_RH_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "largest_exact_matrix_dimension": MAX_EXACT_MATRIX_DIMENSION,
            "largest_irreducible_count": irreducible_count(3, 6),
            "finite_field_element_enumeration": 0,
            "polynomial_enumeration": 0,
            "closed_place_enumeration": 0,
            "curve_or_point_count": 0,
            "l_function_or_zero_computation": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    args = parser.parse_args()
    result = run(check_sources=not args.no_source_check)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check:
        if canonical.read_text(encoding="utf-8") != rendered:
            raise SystemExit("canonical JSON fixture is stale")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
