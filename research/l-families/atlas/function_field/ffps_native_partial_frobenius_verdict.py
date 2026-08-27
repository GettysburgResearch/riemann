#!/usr/bin/env python3
"""Bounded exact replay for the native FFPS partial-Frobenius verdict."""

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
        "b870366141fe8d5f43d5b81f6e50a67d2a888070",
        "research/l-families/atlas/function_field/FFPS_CLOSED_POINT_ADAMS_COMPRESSION.md",
    ): "c79e52ebf0099fe416bc2c79dcb041cc21e025fb",
    (
        "b870366141fe8d5f43d5b81f6e50a67d2a888070",
        "research/l-families/atlas/function_field/FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md",
    ): "ab16e6c0894e51303119692e67b2f2bf59ba73e4",
    (
        "b870366141fe8d5f43d5b81f6e50a67d2a888070",
        "research/l-families/atlas/function_field/FFPS_CYCLIC_SHEAF_INVARIANT_AUDIT.md",
    ): "d531ef36d314549072052cc5b1ae1762c11d00e2",
    (
        "b870366141fe8d5f43d5b81f6e50a67d2a888070",
        "research/l-families/atlas/function_field/FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md",
    ): "e7cb9133bb6b57ddbb1c7f1e350f1d2d0af7bd1a",
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
}

RESIDUE_SIZES = (3, 5, 7, 11)
DEGREE_GROWTH_BASE = 3
DEGREE_GROWTH_CAP = 6


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
            raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def validate_positive_integer(value: int, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{label} must be a positive integer")


def centered_incidence_scaled(
    residue_size: int, cell_count: int
) -> tuple[tuple[int, ...], ...]:
    """Return residue_size*I-J on any cell_count distinct residue labels."""

    validate_positive_integer(residue_size, "residue size")
    validate_positive_integer(cell_count, "cell count")
    if cell_count > residue_size:
        raise ValueError("cell count cannot exceed the residue-field size")
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
    working = [[Fraction(value) for value in row] for row in matrix]
    rank = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(rank, len(working)) if working[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        working[rank], working[pivot] = working[pivot], working[rank]
        pivot_value = working[rank][column]
        working[rank] = [value / pivot_value for value in working[rank]]
        for row in range(len(working)):
            if row == rank or working[row][column] == 0:
                continue
            multiplier = working[row][column]
            working[row] = [
                current - multiplier * pivot_current
                for current, pivot_current in zip(
                    working[row], working[rank], strict=True
                )
            ]
        rank += 1
        if rank == len(working):
            break
    return rank


def kronecker_product(
    left: tuple[tuple[int, ...], ...], right: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    if not left or not right or not left[0] or not right[0]:
        raise ValueError("Kronecker factors must be nonempty")
    return tuple(
        tuple(
            left[left_row][left_column] * right[right_row][right_column]
            for left_column in range(len(left[0]))
            for right_column in range(len(right[0]))
        )
        for left_row in range(len(left))
        for right_row in range(len(right))
    )


def expected_centered_rank(residue_size: int, cell_count: int) -> int:
    validate_positive_integer(residue_size, "residue size")
    validate_positive_integer(cell_count, "cell count")
    if cell_count > residue_size:
        raise ValueError("cell count cannot exceed residue size")
    return residue_size - 1 if cell_count == residue_size else cell_count


def rank_panel() -> dict[str, object]:
    rows: list[dict[str, int]] = []
    for residue_size in RESIDUE_SIZES:
        sector_sizes = {
            "all_residues": residue_size,
            "nonzero_residues": residue_size - 1,
            "sign_pair_sector": (residue_size - 1) // 2,
        }
        for sector, cell_count in sector_sizes.items():
            matrix = centered_incidence_scaled(residue_size, cell_count)
            actual = matrix_rank(matrix)
            expected = expected_centered_rank(residue_size, cell_count)
            if actual != expected:
                raise ArithmeticError("centered-incidence rank formula failed")
            rows.append(
                {
                    "cell_count": cell_count,
                    "rank": actual,
                    "residue_size": residue_size,
                    "sector": sector,
                }
            )

    double_rows: list[dict[str, int]] = []
    for left_size, right_size in ((3, 5), (5, 7)):
        left = centered_incidence_scaled(left_size, left_size - 1)
        right = centered_incidence_scaled(right_size, right_size - 1)
        product = kronecker_product(left, right)
        actual = matrix_rank(product)
        expected = (left_size - 1) * (right_size - 1)
        if actual != expected:
            raise ArithmeticError("bilateral centered-incidence rank failed")
        double_rows.append(
            {
                "left_residue_size": left_size,
                "right_residue_size": right_size,
                "rank": actual,
            }
        )

    degree_growth = [
        {
            "base_field_size": DEGREE_GROWTH_BASE,
            "place_degree": degree,
            "residue_size": DEGREE_GROWTH_BASE**degree,
            "full_centered_rank": DEGREE_GROWTH_BASE**degree - 1,
            "nonzero_phase_sector_rank": DEGREE_GROWTH_BASE**degree - 1,
        }
        for degree in range(1, DEGREE_GROWTH_CAP + 1)
    ]
    return {
        "bilateral_rows": double_rows,
        "degree_growth": degree_growth,
        "one_place_rows": rows,
    }


def fourier_gram_certificate(residue_size: int, column_count: int) -> dict[str, int]:
    """The nonzero additive Fourier block has Gram QI-J on distinct columns."""

    gram = centered_incidence_scaled(residue_size, column_count)
    rank = matrix_rank(gram)
    expected = expected_centered_rank(residue_size, column_count)
    if rank != expected:
        raise ArithmeticError("nonzero Fourier Gram rank failed")
    return {
        "column_count": column_count,
        "gram_rank": rank,
        "residue_size": residue_size,
    }


def partial_frobenius_certificate(
    characteristic: int, frobenius_power: int
) -> dict[str, object]:
    validate_positive_integer(characteristic, "characteristic")
    validate_positive_integer(frobenius_power, "Frobenius power")
    if characteristic < 2 or any(
        characteristic % divisor == 0
        for divisor in range(2, int(characteristic**0.5) + 1)
    ):
        raise ValueError("characteristic must be prime")
    remaining = frobenius_power
    while remaining % characteristic == 0:
        remaining //= characteristic
    if remaining != 1:
        raise ValueError("Frobenius power must be a power of the characteristic")

    diagonal_support = frozenset({(0, 1), (1, 0)})
    partial_graph_support = frozenset({(0, 1), (frobenius_power, 0)})
    if diagonal_support == partial_graph_support:
        raise ArithmeticError("partial Frobenius unexpectedly preserved the diagonal")

    return {
        "artin_schreier_h_axis": {
            "difference": "(h^Q-h)x",
            "difference_degree_in_x": 1,
            "coboundary_obstruction": (
                "if G is rational and G^p-G is polynomial then G has no poles; "
                "if deg_x(G)>0 then deg_x(G^p-G)=p*deg_x(G)>1, while "
                "deg_x(G)=0 cannot produce x-dependence"
            ),
            "partial_isomorphism_exists": False,
        },
        "artin_schreier_x_axis": {
            "difference": "h(x^Q-x)",
            "difference_degree_in_h": 1,
            "partial_isomorphism_exists": False,
        },
        "characteristic": characteristic,
        "diagonal_support": sorted(diagonal_support),
        "frobenius_power": frobenius_power,
        "partial_graph_support": sorted(partial_graph_support),
        "supports_equal": False,
    }


def source_factor_graph() -> dict[str, object]:
    return {
        "frozen_member": (
            "W=sum_(P,Q,c,d) conjugate(A_(P,c))*B_(Q,d)*e_ell(-h Qd^2)*e_rho(k Pc^2)"
        ),
        "nodes": {
            "left_source": "(P,c), with marked place ell=P^-(c)",
            "right_source": "(Q,d), with marked place rho=P^-(d)",
            "left_physical": "X=Pc^2 in the rho residue field",
            "right_physical": "Y=Qd^2 in the ell residue field",
            "phase_variables": "h in F_ell^x, k in F_rho^x",
        },
        "edges": [
            "left source selects ell",
            "right source selects rho",
            "e_ell(-hY) crosses from ell to the right physical source",
            "e_rho(kX) crosses from rho to the left physical source",
            "coprimality, common-core, Boolean, shell, and cleanup constraints remain",
        ],
        "fixed_fibre_factorization": (
            "for fixed ell,rho and fixed source support, the two phase factors "
            "tensor; their individual Fourier separation ranks still grow with "
            "the residue cardinalities"
        ),
        "wick_image": (
            "(1_(x=x')-1/ell)(1_(y=y')-1/rho), with the literal atom "
            "omega=omega' removed but same-residue distinct atoms retained"
        ),
    }


def relative_cleanup_audit() -> dict[str, object]:
    rows = [
        {
            "operation": "clean cyclic hard-selected difference",
            "status": "PROVED EXACT ON THE CONSTRUCTED TORSOR",
            "reason": "C-S=Pi_0 as honest endomorphisms",
        },
        {
            "operation": "common E-linear pullback, pushforward, extension, or cone",
            "status": "PROVED FORMALLY",
            "reason": "a genuinely common equivariant functor preserves C-S=Pi_0",
        },
        {
            "operation": "literal atom diagonal and equal physical-product strata",
            "status": "CONDITIONALLY EQUIVARIANT",
            "reason": (
                "the relations are base-defined and deck-stable, but the native "
                "common source morphisms have not been constructed"
            ),
        },
        {
            "operation": "owner/core overlap and shared incidence",
            "status": "CONDITIONALLY EQUIVARIANT",
            "reason": (
                "they are source-base conditions if transported by one common "
                "map; that transport is an open adapter"
            ),
        },
        {
            "operation": "constant or resonant subquotient removal",
            "status": "NOT AUDITED GLOBALLY",
            "reason": (
                "matching multiplicity, Tate shift, arithmetic Frobenius scalar, "
                "and source coefficient are all required"
            ),
        },
        {
            "operation": "signed conductor recombination",
            "status": "FORMALLY LINEAR",
            "reason": (
                "it preserves an existing common identity, but cannot create the "
                "missing common source complex"
            ),
        },
    ]
    return {
        "all_native_cleanups_proved_equivariant": False,
        "common_relative_complex_constructed": False,
        "rows": rows,
        "safe_conclusion": (
            "the rank obstruction applies termwise to the native phase/incidence "
            "constituent; it is not a no-go for an unconstructed assembled "
            "relative C-S complex in which those constituents cancel first"
        ),
    }


def run(check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    ranks = rank_panel()
    fourier_rows = [
        fourier_gram_certificate(residue_size, (residue_size - 1) // 2)
        for residue_size in RESIDUE_SIZES
    ]
    frobenius_rows = [
        partial_frobenius_certificate(characteristic, characteristic)
        for characteristic in (3, 5, 7)
    ]
    return {
        "source_contract": {
            "git_blobs": {
                f"{commit}:{path}": blob
                for (commit, path), blob in SOURCE_BLOBS.items()
            },
            "factor_graph": source_factor_graph(),
        },
        "verdict": {
            "bounded_or_subpower_external_product": False,
            "commuting_partial_frobenius_on_natural_constituents": False,
            "statement": (
                "The universal Artin-Schreier phase block has rank Q-1 on all "
                "residues and rank m on every proper m-cell restriction; its "
                "Wick-centered incidence image has the same ranks. Thus a "
                "source-independent adapter valid on a full physical sector has "
                "rank comparable with Q=q^a, exponential in the place degree a. "
                "The natural AS line and diagonal incidence class also fail "
                "independent partial Frobenius invariance."
            ),
            "scope": (
                "exact no-go for termwise conductor-uniform externalization of "
                "the universal phase/incidence kernel; the actual native image "
                "would inherit the rank of its occupied residue cells, which has "
                "not been classified. This is not a no-go for a source-specific "
                "sparse image or an assembled signed relative complex that "
                "cancels the constituent before Adams extraction."
            ),
        },
        "rank_theorem": {
            "fourier_gram": "QI_m-J_m on m distinct physical residues",
            "rank": "m for m<Q, and Q-1 for m=Q",
            "bilateral_rank": "the product block has rank rank_left*rank_right",
            "finite_replay": ranks,
            "fourier_rows": fourier_rows,
        },
        "partial_frobenius": {
            "rows": frobenius_rows,
            "support_obstruction": (
                "partial Frobenius sends the diagonal x=y to the distinct graph "
                "x^Q=y over the geometric product"
            ),
        },
        "smallest_escapes": [
            (
                "retain the exact connected signed incidence/Kummer-Mobius "
                "combination before any absolute value and prove cancellation "
                "of the high-rank diagonal correspondences"
            ),
            (
                "construct the common relative C-S complex and show every "
                "cleanup is one common equivariant functor"
            ),
            (
                "prove a source-specific subpower bound for the number of "
                "occupied physical residue cells; no such bound is currently "
                "available"
            ),
            (
                "replace separable Adams inversion by a new correspondence-level "
                "closed-point trace formula that explicitly retains diagonals"
            ),
        ],
        "relative_cleanup": relative_cleanup_audit(),
        "proof_ledger": {
            "fourier_and_incidence_rank": "PROVED EXACT ALL Q BY GRAM SPECTRUM",
            "bilateral_rank_product": "PROVED EXACT",
            "artin_schreier_partial_frobenius_failure": (
                "PROVED BY ARTIN-SCHREIER COBBOUNDARY DEGREE"
            ),
            "diagonal_partial_frobenius_failure": (
                "PROVED BY DISTINCT GEOMETRIC SUPPORT"
            ),
            "clean_torsor_relative_projector": "IMPORTED PROVED EXACT",
            "full_native_relative_complex": "NOT CONSTRUCTED",
            "uniform_betti_or_trace_estimate": "NOT PROVED",
            "cysel_rh_grh": "NOT PROVED",
        },
        "resource_caps": {
            "largest_exact_matrix_dimension": 24,
            "residue_sizes": list(RESIDUE_SIZES),
            "finite_field_element_enumeration": 0,
            "point_counts": 0,
            "curves": 0,
            "l_functions": 0,
            "zeta_zeros": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    result = run(check_sources=not args.no_source_check)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and canonical.read_text(encoding="utf-8") != rendered:
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    if not args.check and not args.write_json:
        print(rendered, end="")


if __name__ == "__main__":
    main()
