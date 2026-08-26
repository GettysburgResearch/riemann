#!/usr/bin/env python3
"""Exact rational replay for the Wick-centered domination boundary."""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_WICK_CENTERED_DOMINATION_BOUNDARY.md"
SOURCE_BLOBS = {
    (
        "271ff4316",
        "research/l-families/atlas/function_field/FFPS_GENERAL_CYCLIC_RESONANCE_NO_GO.md",
    ): "6c63def72b340f69be9caff41a619f23d2b66fd1",
    (
        "90a6aad54",
        "research/l-families/atlas/function_field/FFPS_MASK_AMPLIFIER_PARETO_FRONTIER.md",
    ): "e8adbeb51053e62096ad1590774f13d01094f0b0",
    (
        "464c3705f",
        "research/l-families/atlas/function_field/FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md",
    ): "ab16e6c0894e51303119692e67b2f2bf59ba73e4",
    (
        "6e4609dfe",
        "research/l-families/atlas/function_field/FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md",
    ): "9012f96b34a3ffe55b66282ba1e62bc02514b5c6",
}

MAX_K = 12
MAX_MULTIPLICITY = 10
MAX_MATRIX_ENTRIES = 160_000
MAX_FOURIER_K = 7
MAX_FOURIER_SCALAR_PRODUCTS = 200_000
MAX_WALL_SECONDS = 3.0

Matrix = tuple[tuple[Fraction, ...], ...]


def all_ones(size: int) -> Matrix:
    return tuple(tuple(Fraction(1) for _ in range(size)) for _ in range(size))


def identity(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(row == column) for column in range(size)) for row in range(size)
    )


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a - b for a, b in zip(left_row, right_row, strict=True))
        for left_row, right_row in zip(left, right, strict=True)
    )


def scale(scalar: Fraction, matrix: Matrix) -> Matrix:
    return tuple(tuple(scalar * entry for entry in row) for row in matrix)


def quadratic_form(matrix: Matrix, vector: tuple[Fraction, ...]) -> Fraction:
    return sum(
        (
            vector[row] * matrix[row][column] * vector[column]
            for row in range(len(vector))
            for column in range(len(vector))
        ),
        Fraction(),
    )


def average_outer(vectors: tuple[tuple[Fraction, ...], ...]) -> Matrix:
    if not vectors or not vectors[0]:
        raise ValueError("vectors must be nonempty")
    size = len(vectors[0])
    if any(len(vector) != size for vector in vectors):
        raise ValueError("vector sizes must agree")
    count = Fraction(len(vectors))
    return tuple(
        tuple(
            sum((vector[row] * vector[column] for vector in vectors), Fraction())
            / count
            for column in range(size)
        )
        for row in range(size)
    )


def translated_mask_covariance(
    order: int, retained_positions: tuple[int, ...]
) -> tuple[dict[str, object], int]:
    """Replay one translated hard mask without invoking its Fourier formula."""

    if order < 2:
        raise ValueError("order must be at least two")
    positions = tuple(sorted(set(retained_positions)))
    if (
        not positions
        or len(positions) == order
        or len(positions) != len(retained_positions)
        or any(position < 0 or position >= order for position in positions)
    ):
        raise ValueError("positions must define a nonempty proper subset")
    retained_size = len(positions)
    retained = frozenset(positions)
    weight = Fraction(order, retained_size)
    hard_vectors = tuple(
        tuple(
            weight if (phase - shift) % order in retained else Fraction()
            for phase in range(order)
        )
        for shift in range(order)
    )
    centered_vectors = tuple(
        tuple(entry - 1 for entry in vector) for vector in hard_vectors
    )
    hard = average_outer(hard_vectors)
    selected = subtract(hard, all_ones(order))
    selected_direct = average_outer(centered_vectors)
    if selected != selected_direct:
        raise ArithmeticError("centered translated-mask covariance failed")

    for row in range(order):
        for column in range(order):
            delta = (column - row) % order
            intersection = sum(
                1 for value in retained if (value + delta) % order in retained
            )
            expected = Fraction(order * intersection, retained_size * retained_size)
            if hard[row][column] != expected:
                raise ArithmeticError("autocorrelation kernel failed")
    selected_mass = Fraction(order, retained_size) - 1
    if any(hard[index][index] != 1 + selected_mass for index in range(order)):
        raise ArithmeticError("hard atomic coefficient failed")
    if any(sum(row, Fraction()) != 0 for row in selected):
        raise ArithmeticError("selected covariance does not kill principal line")

    scalar_products = 2 * order**3 + order * order * retained_size
    return (
        {
            "k": order,
            "positions": positions,
            "t": retained_size,
            "u": str(selected_mass),
            "hard_diagonal": str(1 + selected_mass),
            "selected_row_sum": "0",
        },
        scalar_products,
    )


def collision_blocks(
    order: int, retained_size: int, multiplicity: int
) -> dict[str, object]:
    if order < 2 or not 1 <= retained_size <= order:
        raise ValueError("require 1<=t<=k and k>=2")
    if multiplicity < 2:
        raise ValueError("collision multiplicity must be at least two")
    selected_mass = Fraction(order, retained_size) - 1
    principal = all_ones(multiplicity)
    selected = scale(selected_mass, principal)
    hard = scale(1 + selected_mass, principal)
    centered_principal = subtract(principal, identity(multiplicity))
    centered_selected = subtract(selected, scale(selected_mass, identity(multiplicity)))
    centered_hard = subtract(hard, scale(1 + selected_mass, identity(multiplicity)))
    if subtract(centered_hard, centered_principal) != centered_selected:
        raise ArithmeticError("centered relative identity failed")

    ones = tuple(Fraction(1) for _ in range(multiplicity))
    zero_sum = (Fraction(1), Fraction(-1), *([Fraction(0)] * (multiplicity - 2)))
    positive_value = quadratic_form(centered_selected, ones)
    negative_value = quadratic_form(centered_selected, zero_sum)
    if positive_value != selected_mass * multiplicity * (multiplicity - 1):
        raise ArithmeticError("positive collision eigenvalue failed")
    if negative_value != -2 * selected_mass:
        raise ArithmeticError("negative collision eigenvalue failed")

    repaired = subtract(
        scale(selected_mass, identity(multiplicity)),
        scale(-1, centered_selected),
    )
    if repaired != selected:
        raise ArithmeticError("sharp diagonal repair failed")
    return {
        "k": order,
        "t": retained_size,
        "m": multiplicity,
        "u": str(selected_mass),
        "positive_eigenvalue": str(selected_mass * (multiplicity - 1)),
        "negative_eigenvalue": str(-selected_mass),
        "negative_multiplicity": multiplicity - 1,
        "indefinite": bool(selected_mass),
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
    rows: list[dict[str, object]] = []
    named_matrix_entries = 0
    for order in range(2, MAX_K + 1):
        for retained_size in range(1, order):
            for multiplicity in range(2, MAX_MULTIPLICITY + 1):
                named_matrix_entries += 6 * multiplicity * multiplicity
                if named_matrix_entries > MAX_MATRIX_ENTRIES:
                    raise RuntimeError("matrix-entry cap exceeded")
                rows.append(collision_blocks(order, retained_size, multiplicity))

    mask_rows: list[dict[str, object]] = []
    fourier_scalar_products = 0
    for order in range(2, MAX_FOURIER_K + 1):
        for bit_mask in range(1, (1 << order) - 1):
            positions = tuple(
                position for position in range(order) if bit_mask & (1 << position)
            )
            row, cost = translated_mask_covariance(order, positions)
            mask_rows.append(row)
            fourier_scalar_products += cost
            if fourier_scalar_products > MAX_FOURIER_SCALAR_PRODUCTS:
                raise RuntimeError("Fourier scalar-product cap exceeded")
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return {
        "schema": "riemann.function_field.ffps_wick_centered_domination_boundary.v1",
        "status": "EXACT_SHARP_WICK_DOMINATION_BOUNDARY",
        "exact_theorems": {
            "uncentered": "Q_C=Q_P+Q_S with Q_S positive semidefinite",
            "centered": (
                "Q_C^circ-Q_P^circ is indefinite for every proper mask "
                "on a repeated-phase fibre"
            ),
            "collision_spectrum": "u*(m-1), then -u with multiplicity m-1",
            "sharp_repair": "Q_S^circ>=-u*D and coefficient u is minimal",
        },
        "finite_replay": {
            "rows": len(rows),
            "sample": next(
                row for row in rows if row["k"] == 3 and row["t"] == 2 and row["m"] == 4
            ),
            "translated_masks": len(mask_rows),
            "translated_mask_sample": next(
                row for row in mask_rows if row["k"] == 5 and row["positions"] == (0, 2)
            ),
        },
        "resource_ledger": {
            "named_matrix_entries_accounted": named_matrix_entries,
            "max_matrix_entries": MAX_MATRIX_ENTRIES,
            "fourier_scalar_products": fourier_scalar_products,
            "max_fourier_scalar_products": MAX_FOURIER_SCALAR_PRODUCTS,
            "finite_fields_enumerated": 0,
            "conductors_enumerated": 0,
            "l_function_zeros_enumerated": 0,
        },
        "open": [
            "full FFPS collision cleanup",
            "varying-conductor centered trace estimate",
            "RH and GRH",
        ],
    }


def run_checks() -> dict[str, object]:
    check_source_blobs()
    report = build_report()
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "uncentered hard covariance dominates",
        "u(J_m-I_m)",
        "No coefficient smaller than `u`",
        "relative signed route",
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
