#!/usr/bin/env python3
"""Exact rational replay for the cyclic torsor relative projector.

The all-k proof is in the companion note.  This script checks small cyclic
circulant matrices only.  It does not enumerate fields, places, conductors,
curves, L-functions, or zeros.
"""

from __future__ import annotations

import argparse
import itertools
import json
import subprocess
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md"
SOURCE_BLOBS = {
    (
        "271ff4316",
        "research/l-families/atlas/function_field/FFPS_GENERAL_CYCLIC_RESONANCE_NO_GO.md",
    ): "6c63def72b340f69be9caff41a619f23d2b66fd1",
    (
        "8b4559a54",
        "research/l-families/atlas/function_field/FFPS_CYCLIC_SHEAF_INVARIANT_AUDIT.md",
    ): "d531ef36d314549072052cc5b1ae1762c11d00e2",
    (
        "806f8c000",
        "research/l-families/atlas/function_field/FFPS_PRINCIPAL_ANOMALY_TRANSFER_DICHOTOMY.md",
    ): "47c148187db578357035926f8ff12419b0cf3652",
}

MAX_K = 8
MAX_SUBSETS = 512
MAX_MATRIX_ENTRIES = 100_000
MAX_WALL_SECONDS = 3.0

Matrix = tuple[tuple[Fraction, ...], ...]


def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right):
        raise ValueError("matrix dimensions differ")
    return tuple(
        tuple(a - b for a, b in zip(left_row, right_row, strict=True))
        for left_row, right_row in zip(left, right, strict=True)
    )


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    if not left or len(left[0]) != len(right):
        raise ValueError("matrix dimensions do not compose")
    columns = tuple(zip(*right, strict=True))
    return tuple(
        tuple(
            sum(a * b for a, b in zip(row, column, strict=True)) for column in columns
        )
        for row in left
    )


def kronecker(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a * b for a in left_row for b in right_row)
        for left_row in left
        for right_row in right
    )


def identity(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(row == column) for column in range(size)) for row in range(size)
    )


def principal_projector(order: int) -> Matrix:
    return tuple(tuple(Fraction(1, order) for _ in range(order)) for _ in range(order))


def shift_matrix(order: int, shift: int) -> Matrix:
    """Right-regular translation e_h -> e_(h+shift)."""

    return tuple(
        tuple(Fraction(row == (column + shift) % order) for column in range(order))
        for row in range(order)
    )


def trace_function_endomorphism(weights: tuple[Fraction, ...]) -> Matrix:
    """Return A_w=(1/k) sum_a w(-a) rho(a)."""

    order = len(weights)
    if order < 2:
        raise ValueError("weight function must live on a cyclic group of order >=2")
    return tuple(
        tuple(weights[(column - row) % order] / order for column in range(order))
        for row in range(order)
    )


def matrix_trace(matrix: Matrix) -> Fraction:
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("trace requires a square matrix")
    return sum((matrix[index][index] for index in range(len(matrix))), Fraction())


def cyclic_operators(
    order: int, retained: frozenset[int]
) -> tuple[Matrix, Matrix, Matrix]:
    if order < 2:
        raise ValueError("cyclic order must be at least two")
    if not retained or any(entry < 0 or entry >= order for entry in retained):
        raise ValueError("retained set must be a nonempty subset of C_k")
    size = len(retained)
    hard_kernel: list[Fraction] = []
    for shift in range(order):
        shifted = frozenset((entry + shift) % order for entry in retained)
        hard_kernel.append(Fraction(order * len(retained & shifted), size * size))
    selected_kernel = [value - 1 for value in hard_kernel]

    # The normalized convolution matrix has entry K(x-y)/k.
    hard = tuple(
        tuple(hard_kernel[(row - column) % order] / order for column in range(order))
        for row in range(order)
    )
    selected = tuple(
        tuple(
            selected_kernel[(row - column) % order] / order for column in range(order)
        )
        for row in range(order)
    )
    return hard, selected, principal_projector(order)


def check_one(order: int, retained: frozenset[int]) -> dict[str, object]:
    hard, selected, principal = cyclic_operators(order, retained)
    if matrix_subtract(hard, selected) != principal:
        raise ArithmeticError("hard-selected projector identity failed")
    if matrix_multiply(principal, principal) != principal:
        raise ArithmeticError("principal matrix is not idempotent")
    if matrix_multiply(selected, principal) != tuple(
        tuple(Fraction(0) for _ in range(order)) for _ in range(order)
    ):
        raise ArithmeticError("selected operator retained a principal component")
    if any(sum(row) != 1 for row in hard):
        raise ArithmeticError("hard operator does not preserve the principal line")
    if any(sum(row) != 0 for row in selected):
        raise ArithmeticError("selected operator has nonzero principal row sum")
    return {
        "order": order,
        "retained": sorted(retained),
        "selected_collision_mass": str(Fraction(order, len(retained)) - 1),
    }


def build_report() -> dict[str, object]:
    started = time.monotonic()
    subset_count = 0
    matrix_entries = 0
    summaries: list[dict[str, object]] = []
    for order in range(2, MAX_K + 1):
        order_count = 0
        for size in range(1, order):
            for entries in itertools.combinations(range(order), size):
                subset_count += 1
                order_count += 1
                matrix_entries += 3 * order * order
                if subset_count > MAX_SUBSETS or matrix_entries > MAX_MATRIX_ENTRIES:
                    raise RuntimeError("declared exact replay cap exceeded")
                check_one(order, frozenset(entries))
        summaries.append({"order": order, "proper_nonempty_masks": order_count})

    hard3, selected3, principal3 = cyclic_operators(3, frozenset({0, 1}))
    hard4, selected4, principal4 = cyclic_operators(4, frozenset({0, 1}))
    tensor_hard = kronecker(hard3, hard4)
    tensor_principal = kronecker(principal3, principal4)
    tensor_selected_total = matrix_subtract(tensor_hard, tensor_principal)
    if matrix_subtract(tensor_hard, tensor_selected_total) != tensor_principal:
        raise ArithmeticError("finite-product relative projector failed")
    expanded_selected = matrix_subtract(
        matrix_subtract(
            tensor_hard,
            kronecker(selected3, selected4),
        ),
        kronecker(selected3, principal4),
    )
    expanded_selected = matrix_subtract(
        expanded_selected, kronecker(principal3, selected4)
    )
    if expanded_selected != tensor_principal:
        raise ArithmeticError("tensor Fourier expansion failed")

    # Exact Frobenius-selector control for one arbitrary rational trace function.
    selector_weights = tuple(Fraction(value) for value in (3, -2, 5, 7, -11))
    selector = trace_function_endomorphism(selector_weights)
    for frobenius_class, expected in enumerate(selector_weights):
        observed = matrix_trace(
            matrix_multiply(selector, shift_matrix(5, frobenius_class))
        )
        if observed != expected:
            raise ArithmeticError("global torsor trace-selector identity failed")

    elapsed = time.monotonic() - started
    if elapsed > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return {
        "schema": "riemann.function_field.ffps_cyclic_torsor_relative_projector.v1",
        "status": "EXACT_ENDOMORPHISM_PROJECTOR_REPLAY",
        "finite_audit": summaries,
        "resource_ledger": {
            "subsets": subset_count,
            "matrix_entries": matrix_entries,
            "max_subsets": MAX_SUBSETS,
            "max_matrix_entries": MAX_MATRIX_ENTRIES,
            "max_wall_seconds": MAX_WALL_SECONDS,
        },
        "exact_identities": [
            "C_S-S_S=Pi_0",
            "S_S*Pi_0=0",
            "tensor(C_i)-S_total=tensor(Pi_0_i)",
            "Tr(A_w*Frob_phi)=w(phi)",
        ],
        "not_constructed": [
            "one varying-closed-place physical torsor",
            "equivariant full FFPS cleanup",
            "a conductor-uniform principal trace bound",
        ],
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


def run_checks() -> dict[str, object]:
    check_source_blobs()
    report = build_report()
    expected_subsets = sum(2**order - 2 for order in range(2, MAX_K + 1))
    if report["resource_ledger"]["subsets"] != expected_subsets:
        raise ArithmeticError("subset ledger mismatch")
    if expected_subsets != 494:
        raise ArithmeticError("frozen replay scope changed")
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "honest endomorphisms",
        "TORSOR UNDER SPLIT `mu_k`",
        "only Galois-orbit sums",
        "one varying-closed-place physical torsor",
        "RH or GRH | **UNPROVED**",
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
