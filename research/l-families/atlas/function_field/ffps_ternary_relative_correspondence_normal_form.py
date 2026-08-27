#!/usr/bin/env python3
"""Bounded exact replay for the ternary relative correspondence normal form."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_BLOBS = {
    (
        "e3903136912402a969abee7bfcf1ad5f9dfbd1a0",
        "research/l-families/atlas/function_field/FFPS_NATIVE_PARTIAL_FROBENIUS_VERDICT.md",
    ): "19939eb240ca6b2b6d5221954cec76fe0f5c4f9c",
    (
        "9ced25befb6dd88146809866a34a15fec034b096",
        "research/l-families/atlas/function_field/FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md",
    ): "21645bdb609320cf176893aa589af7a17c741d9a",
    (
        "464c3705fd9418be8fc03488109cc24dab6f5efd",
        "research/l-families/atlas/function_field/FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md",
    ): "ab16e6c0894e51303119692e67b2f2bf59ba73e4",
    (
        "05da4d1705d994dd02d650f321196f8464034ba8",
        "research/l-families/atlas/function_field/FFPS_CLOSED_POINT_ADAMS_COMPRESSION.md",
    ): "c79e52ebf0099fe416bc2c79dcb041cc21e025fb",
    (
        "1242951f9529435fd9100d8be6f0d4d4d6f24eae",
        "research/l-families/atlas/function_field/FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md",
    ): "9012f96b34a3ffe55b66282ba1e62bc02514b5c6",
    (
        "271ff4316f75100a2511b8bc75369457cb8e2b8e",
        "research/l-families/atlas/function_field/FFPS_GENERAL_CYCLIC_RESONANCE_NO_GO.md",
    ): "6c63def72b340f69be9caff41a619f23d2b66fd1",
    (
        "98af0db6e",
        "claims/lemmas/L-106191-source-dual-centered-double-incidence-correlation.md",
    ): "85c4ef92ead7d8b235f9c195c3c0acd16d16030f",
}

CONTROL_PANELS = ((7, 7), (7, 13))
GRAPH_DEPTH = 5


Matrix = tuple[tuple[Fraction, ...], ...]


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


def validate_ternary_residue_size(residue_size: int) -> None:
    if isinstance(residue_size, bool) or not isinstance(residue_size, int):
        raise TypeError("residue size must be an integer")
    if residue_size < 7 or residue_size % 6 != 1:
        raise ValueError("residue size must be at least 7 and congruent to 1 mod 6")


def sign_pair_count(residue_size: int) -> int:
    validate_ternary_residue_size(residue_size)
    return (residue_size - 1) // 2


def balanced_ternary_labels(residue_size: int) -> tuple[int, ...]:
    """Model an exact-order-three character on the sign-pair quotient."""

    count = sign_pair_count(residue_size)
    return tuple(index % 3 for index in range(count))


def bilateral_labels(
    left_residue_size: int,
    right_residue_size: int,
    alignment: int = 1,
) -> tuple[int, ...]:
    if alignment not in (-1, 1):
        raise ValueError("alignment must be +1 or -1")
    left = balanced_ternary_labels(left_residue_size)
    right = balanced_ternary_labels(right_residue_size)
    return tuple((x + alignment * y) % 3 for x, y in product(left, right))


def matrix_rank(matrix: Matrix) -> int:
    if not matrix or not matrix[0]:
        return 0
    column_count = len(matrix[0])
    if any(len(row) != column_count for row in matrix):
        raise ValueError("matrix must be rectangular")
    working = [list(row) for row in matrix]
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
        working[rank] = [value / pivot_value for value in working[rank]]
        for row in range(len(working)):
            if row == rank or not working[row][column]:
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


def centered_phase_gram(residue_size: int) -> Matrix:
    count = sign_pair_count(residue_size)
    return tuple(
        tuple(
            Fraction(residue_size * int(row == column) - 1) for column in range(count)
        )
        for row in range(count)
    )


def kronecker(left: Matrix, right: Matrix) -> Matrix:
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


def ternary_covariance_kernels(
    labels: tuple[int, ...],
) -> tuple[Matrix, Matrix, Matrix]:
    if not labels or set(labels) - {0, 1, 2}:
        raise ValueError("labels must be a nonempty ternary sequence")
    selected = tuple(
        tuple(Fraction(1, 2) if left == right else Fraction(-1, 4) for right in labels)
        for left in labels
    )
    hard = tuple(tuple(Fraction(1) + value for value in row) for row in selected)
    relative = tuple(tuple(Fraction(1) for _ in labels) for _ in labels)
    return hard, selected, relative


def hadamard(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right) or any(
        len(left_row) != len(right_row)
        for left_row, right_row in zip(left, right, strict=True)
    ):
        raise ValueError("Hadamard factors must have equal shape")
    return tuple(
        tuple(a * b for a, b in zip(left_row, right_row, strict=True))
        for left_row, right_row in zip(left, right, strict=True)
    )


def subtract(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right) or any(
        len(left_row) != len(right_row)
        for left_row, right_row in zip(left, right, strict=True)
    ):
        raise ValueError("matrix shapes must agree")
    return tuple(
        tuple(a - b for a, b in zip(left_row, right_row, strict=True))
        for left_row, right_row in zip(left, right, strict=True)
    )


def restrict_matrix(matrix: Matrix, indices: tuple[int, ...]) -> Matrix:
    return tuple(tuple(matrix[row][column] for column in indices) for row in indices)


def delete_atomic_diagonal(matrix: Matrix) -> Matrix:
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("atomic diagonal requires a square matrix")
    return tuple(
        tuple(
            Fraction(0) if row == column else value
            for column, value in enumerate(values)
        )
        for row, values in enumerate(matrix)
    )


def nonzero_count(matrix: Matrix) -> int:
    return sum(bool(value) for row in matrix for value in row)


def pullback_to_atoms(matrix: Matrix, atom_cells: tuple[int, ...]) -> Matrix:
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("cell kernel must be a nonempty square matrix")
    if not atom_cells:
        raise ValueError("atom map must be nonempty")
    if min(atom_cells) < 0 or max(atom_cells) >= len(matrix):
        raise ValueError("atom cell index is outside the physical kernel")
    return tuple(
        tuple(matrix[left_cell][right_cell] for right_cell in atom_cells)
        for left_cell in atom_cells
    )


def source_image_rank_certificate() -> dict[str, object]:
    left_residue_size, right_residue_size = 7, 13
    labels = bilateral_labels(left_residue_size, right_residue_size)
    hard, selected, _ = ternary_covariance_kernels(labels)
    native = kronecker(
        centered_phase_gram(left_residue_size),
        centered_phase_gram(right_residue_size),
    )
    kernels = {
        "hard": hadamard(native, hard),
        "relative": native,
        "selected": hadamard(native, selected),
    }
    atom_cells = (0, 0, 2, 5, 5, 7, 11)
    occupied_cell_count = len(set(atom_cells))
    ranks = {
        name: matrix_rank(pullback_to_atoms(kernel, atom_cells))
        for name, kernel in kernels.items()
    }
    if set(ranks.values()) != {occupied_cell_count}:
        raise ArithmeticError("source-image pullback rank law failed")
    return {
        "atom_count": len(atom_cells),
        "atom_to_cell_map": list(atom_cells),
        "occupied_cell_count": occupied_cell_count,
        "pullback_ranks": ranks,
        "theorem": (
            "before literal-atom deletion, pulling the positive-definite hard, "
            "selected, or relative native kernel back along any atom-to-cell "
            "map gives rank equal to the number of occupied distinct cells"
        ),
    }


def ternary_relative_panel(
    left_residue_size: int, right_residue_size: int
) -> dict[str, object]:
    labels = bilateral_labels(left_residue_size, right_residue_size)
    cell_count = len(labels)
    class_occupancy = [labels.count(label) for label in range(3)]
    if len(set(class_occupancy)) != 1:
        raise ArithmeticError("ternary classes are not equally occupied")

    hard, selected, relative = ternary_covariance_kernels(labels)
    if subtract(hard, selected) != relative:
        raise ArithmeticError("hard-selected relative identity failed")

    native = kronecker(
        centered_phase_gram(left_residue_size),
        centered_phase_gram(right_residue_size),
    )
    hard_native = hadamard(native, hard)
    selected_native = hadamard(native, selected)
    relative_native = subtract(hard_native, selected_native)
    if relative_native != native:
        raise ArithmeticError("common native lift did not preserve C-S=1")

    hard_support_ranks: list[int] = []
    hard_support_sizes: list[int] = []
    for missing_label in range(3):
        indices = tuple(
            index for index, label in enumerate(labels) if label != missing_label
        )
        hard_support_sizes.append(len(indices))
        hard_support_ranks.append(matrix_rank(restrict_matrix(native, indices)))

    atomic_relative = subtract(
        delete_atomic_diagonal(hard_native),
        delete_atomic_diagonal(selected_native),
    )
    expected_atomic_relative = delete_atomic_diagonal(native)
    if atomic_relative != expected_atomic_relative:
        raise ArithmeticError("Wick-relative identity failed")

    return {
        "cell_count": cell_count,
        "class_occupancy": class_occupancy,
        "cyclic_kernel_ranks": {
            "hard": matrix_rank(hard),
            "relative": matrix_rank(relative),
            "selected": matrix_rank(selected),
        },
        "hard_rotation_support_ranks": hard_support_ranks,
        "hard_rotation_support_sizes": hard_support_sizes,
        "left_residue_size": left_residue_size,
        "native_coupled_ranks": {
            "hard": matrix_rank(hard_native),
            "relative": matrix_rank(relative_native),
            "selected": matrix_rank(selected_native),
            "wick_relative": matrix_rank(atomic_relative),
        },
        "pair_support": {
            "hard": nonzero_count(hard),
            "relative": nonzero_count(relative),
            "selected": nonzero_count(selected),
            "total_pairs": cell_count * cell_count,
        },
        "right_residue_size": right_residue_size,
    }


def prime_factors(value: int) -> tuple[int, ...]:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    factors: list[int] = []
    remainder = value
    divisor = 2
    while divisor * divisor <= remainder:
        if remainder % divisor == 0:
            factors.append(divisor)
            while remainder % divisor == 0:
                remainder //= divisor
        divisor += 1
    if remainder > 1:
        factors.append(remainder)
    return tuple(factors)


def squarefree_divisor_mobius(value: int) -> tuple[tuple[int, int], ...]:
    factors = prime_factors(value)
    rows: list[tuple[int, int]] = []
    for mask in range(1 << len(factors)):
        divisor = 1
        parity = 0
        for index, prime in enumerate(factors):
            if mask & (1 << index):
                divisor *= prime
                parity += 1
        rows.append((divisor, -1 if parity % 2 else 1))
    return tuple(sorted(rows))


def correspondence_orbit(residue_size: int, depth: int) -> dict[str, object]:
    validate_ternary_residue_size(residue_size)
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 0:
        raise ValueError("depth must be a nonnegative integer")
    signatures = [(residue_size**power, 1) for power in range(depth + 1)]
    if len(signatures) != len(set(signatures)):
        raise ArithmeticError("Frobenius graph signatures unexpectedly collided")
    return {
        "centered_orbit_dimension": depth + 1,
        "depth": depth,
        "graph_equations": [f"y=x^{degree}" for degree, _ in signatures],
        "graph_signatures": signatures,
        "module_normal_form": (
            "the centered classes H_n=[Gamma_(Q^n)]-Q^-1[J] are linearly "
            "independent; T(H_n)=H_(n+1), so their orbit is one free "
            "E[T]-generator but no finite-dimensional E-space"
        ),
        "residue_size": residue_size,
        "with_background_dimension": depth + 2,
    }


def formal_divisor_shift_ledger(
    left_degree: int, right_degree: int
) -> dict[str, object]:
    left = squarefree_divisor_mobius(left_degree)
    right = squarefree_divisor_mobius(right_degree)
    left_sum = sum(mu for _, mu in left)
    right_sum = sum(mu for _, mu in right)
    top_terms = len(left) * len(right)
    surviving_components = top_terms
    if right_sum:
        surviving_components += len(left)
    if left_sum:
        surviving_components += len(right)
    if left_sum and right_sum:
        surviving_components += 1
    return {
        "background_coefficient_factor": left_sum * right_sum,
        "formal_warning": (
            "this is the sparse polynomial in partial-Frobenius graph shifts; "
            "it is not a closed-point Adams theorem for the native complex"
        ),
        "left_axis_coefficient_factor": right_sum,
        "left_degree": left_degree,
        "left_nonzero_mobius_divisors": len(left),
        "right_axis_coefficient_factor": left_sum,
        "right_degree": right_degree,
        "right_nonzero_mobius_divisors": len(right),
        "surviving_support_components": surviving_components,
        "top_graph_products": top_terms,
    }


def run(check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    panels = [ternary_relative_panel(left, right) for left, right in CONTROL_PANELS]
    orbit_rows = [correspondence_orbit(size, GRAPH_DEPTH) for size in (7, 13)]
    divisor_rows = [
        formal_divisor_shift_ledger(left, right)
        for left, right in ((6, 10), (12, 15), (1, 6))
    ]
    largest_matrix = max(int(row["cell_count"]) for row in panels)
    return {
        "source_contract": {
            "git_blobs": {
                f"{commit}:{path}": blob
                for (commit, path), blob in SOURCE_BLOBS.items()
            },
            "physical_coordinates": "X=Pc^2 and Y=Qd^2 before cyclic labelling",
            "relative_source_kernel": (
                "for k=3,t=2, K_C(g)=3/2 at g=1 and 3/4 otherwise; "
                "K_S(g)=1/2 at g=1 and -1/4 otherwise; K_C-K_S=1"
            ),
        },
        "physical_occupancy": {
            "all_q_theorem": (
                "for Q_i congruent to 1 mod 6, the sign-pair sector has "
                "m_i=(Q_i-1)/2 cells, every ternary class on the bilateral "
                "product has M/3 cells, and each rotated hard support has 2M/3"
            ),
            "finite_replay": panels,
            "scope": (
                "exact on the clean complete physical sector; the live "
                "owner/Boolean source image may be smaller and no global "
                "occupancy lower bound is claimed"
            ),
        },
        "relative_rank_theorem": {
            "all_q_theorem": (
                "if B is the positive-definite native phase/incidence Gram on "
                "the clean sign-pair product, then B_C=B hadamard K_C and "
                "B_S=B hadamard K_S are positive definite and B_C-B_S=B. "
                "All three have exact rank M. After common literal-atom "
                "deletion, the difference is B with its atomic diagonal "
                "removed and still has rank M for Q_1,Q_2 at least 7"
            ),
            "consequence": (
                "ternary relative cancellation removes the two selected C3 "
                "deck modes but does not cancel or compress the native "
                "Artin-Schreier/Wick incidence rank"
            ),
            "source_image_pullback": source_image_rank_certificate(),
        },
        "partial_frobenius_and_correspondences": {
            "commuting_partial_frobenius_created": False,
            "finite_dimensional_graph_closure": False,
            "orbit_rows": orbit_rows,
            "positive_normal_form": (
                "the surviving centered incidence is one free generator over "
                "the Frobenius-shift polynomial semigroup; bilateral incidence "
                "is one free E[T_x,T_y]-generator. This is sparse on every "
                "finite divisor grid, despite infinite E-dimension"
            ),
            "formal_divisor_ledgers": divisor_rows,
            "categorical_boundary": (
                "the shift module is a correspondence bookkeeping theorem, not "
                "an isomorphism under partial Frobenius and not the separable "
                "two-place Adams formula"
            ),
        },
        "proof_ledger": {
            "ternary_class_occupancy": "PROVED EXACT ON THE CLEAN PHYSICAL SECTOR",
            "hard_selected_relative_kernel": "PROVED EXACT PRE-EXTERNALIZATION",
            "native_coupled_rank": "PROVED EXACT ALL ELIGIBLE Q_1,Q_2",
            "wick_relative_rank": "PROVED EXACT ALL ELIGIBLE Q_1,Q_2",
            "partial_frobenius_isomorphism": "REFUTED FOR THE NATURAL RELATIVE INCIDENCE",
            "frobenius_graph_shift_module": "CONSTRUCTED EXACTLY",
            "finite_dimensional_correspondence_closure": (
                "REFUTED FOR THE NATURAL FROBENIUS-GRAPH SUPPORT CLASSES"
            ),
            "native_closed_point_adams_formula": "NOT CONSTRUCTED",
            "live_source_occupancy_lower_bound": "OPEN / NOT CLAIMED",
            "full_owner_boolean_relative_complex": "NOT CONSTRUCTED",
            "uniform_betti_or_trace_estimate": "NOT PROVED",
            "cysel_wcadd_wckum_rh_grh": "NOT PROVED",
        },
        "next_exact_gate": (
            "construct a trace functor on the Frobenius-graph shift module "
            "which realizes the independent closed-point degree extractor and "
            "has uniform complexity after owner/Boolean pushforward; otherwise "
            "prove that the live source image is genuinely sparse"
        ),
        "resource_caps": {
            "largest_exact_matrix_dimension": largest_matrix,
            "control_panels": [list(panel) for panel in CONTROL_PANELS],
            "graph_depth": GRAPH_DEPTH,
            "finite_field_element_enumeration": 0,
            "closed_place_enumeration": 0,
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
    args = parser.parse_args()
    result = run(check_sources=not args.no_source_check)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and canonical.read_text(encoding="utf-8") != rendered:
        raise SystemExit("canonical JSON fixture is stale")
    if not args.check:
        print(rendered, end="")


if __name__ == "__main__":
    main()
