#!/usr/bin/env python3
"""Exact bounded replay for finite-abelian subgroup-mask compression."""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from fractions import Fraction
from itertools import pairwise
from math import prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_FINITE_ABELIAN_SUBGROUP_MASK_COMPRESSION.md"
SOURCE_BLOBS = {
    (
        "6e4609dfe",
        "research/l-families/atlas/function_field/FFPS_CORRELATED_MASK_AMPLIFIER.md",
    ): "4569c521e99e8c591f1694126605f8abee8a75f8",
    (
        "6e4609dfe",
        "research/l-families/atlas/function_field/FFPS_CHECKERBOARD_SOURCE_BRIDGE.md",
    ): "15c32de6182407e65a6d41d593f7542945bf704e",
    (
        "464c3705f",
        "research/l-families/atlas/function_field/FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md",
    ): "ab16e6c0894e51303119692e67b2f2bf59ba73e4",
    (
        "7ad6f127d",
        "research/l-families/atlas/function_field/FFPS_WICK_CENTERED_DOMINATION_BOUNDARY.md",
    ): "cde24e9ce59c064ddfd8b711a2d42fd4daa3ee60",
}

MAX_DIMENSION = 8
MAX_WALSH_SUMMANDS = 180_000
MAX_DIRECT_MATRIX_ENTRIES = 256
MAX_WALL_SECONDS = 3.0
PRIME_PANEL = (5, 13, 17, 29, 37, 41)

Matrix = tuple[tuple[Fraction, ...], ...]


def parity(value: int) -> int:
    return value.bit_count() & 1


def character(label: int, value: int) -> int:
    return -1 if parity(label & value) else 1


def normalized_mask(dimension: int, value: int) -> int:
    if dimension < 1:
        raise ValueError("dimension must be positive")
    return 2 if parity(value) == 0 else 0


def walsh_coefficient(dimension: int, label: int) -> Fraction:
    group_order = 1 << dimension
    if not 0 <= label < group_order:
        raise ValueError("label outside group")
    return Fraction(
        sum(
            normalized_mask(dimension, value) * character(label, value)
            for value in range(group_order)
        ),
        group_order,
    )


def autocorrelation(dimension: int, shift: int) -> Fraction:
    group_order = 1 << dimension
    if not 0 <= shift < group_order:
        raise ValueError("shift outside group")
    return Fraction(
        sum(
            normalized_mask(dimension, value)
            * normalized_mask(dimension, value ^ shift)
            for value in range(group_order)
        ),
        group_order,
    )


def check_dimension(dimension: int) -> tuple[dict[str, object], int]:
    group_order = 1 << dimension
    top_label = group_order - 1
    coefficients = tuple(
        walsh_coefficient(dimension, label) for label in range(group_order)
    )
    expected = tuple(
        Fraction(1) if label in (0, top_label) else Fraction()
        for label in range(group_order)
    )
    if coefficients != expected:
        raise ArithmeticError("Walsh support is not trivial plus top character")
    if sum(coefficient * coefficient for coefficient in coefficients) != 2:
        raise ArithmeticError("selected mass identity failed")

    for shift in range(group_order):
        kernel = autocorrelation(dimension, shift)
        if kernel != 1 + character(top_label, shift):
            raise ArithmeticError("autocorrelation/projector identity failed")

    return (
        {
            "dimension": dimension,
            "group_order": group_order,
            "retained_group_order": group_order // 2,
            "fourier_support": (0, top_label),
            "selected_rank": 1,
            "selected_mass": 1,
            "sharp_wick_repair": 1,
        },
        2 * group_order * group_order,
    )


def matrix_vector(matrix: Matrix, vector: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    if not matrix or any(len(row) != len(vector) for row in matrix):
        raise ValueError("matrix-vector dimensions must agree")
    return tuple(
        sum(
            (entry * value for entry, value in zip(row, vector, strict=True)),
            Fraction(),
        )
        for row in matrix
    )


def kronecker(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right:
        raise ValueError("Kronecker factors must be nonempty")
    return tuple(
        tuple(
            left_entry * right_entry
            for left_entry in left_row
            for right_entry in right_row
        )
        for left_row in left
        for right_row in right
    )


def local_square_phase_gram(prime: int) -> Matrix:
    if prime < 5 or prime % 4 != 1:
        raise ValueError("square-phase control requires p=1 modulo 4 and p>=5")
    dimension = (prime - 1) // 2
    return tuple(
        tuple(
            Fraction(prime - 1 if row == column else -1) for column in range(dimension)
        )
        for row in range(dimension)
    )


def legendre_sign_vector(prime: int) -> tuple[Fraction, ...]:
    dimension = (prime - 1) // 2
    residues = {value * value % prime for value in range(1, prime)}
    vector = tuple(
        Fraction(1 if representative in residues else -1)
        for representative in range(1, dimension + 1)
    )
    if sum(vector, Fraction()) != 0:
        raise ArithmeticError("Legendre control vector is not balanced")
    return vector


def tensor_vector(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    return tuple(
        left_entry * right_entry for left_entry in left for right_entry in right
    )


def wick_spectrum_witness() -> tuple[dict[str, object], int]:
    centered_selected: Matrix = (
        (Fraction(), Fraction(1)),
        (Fraction(1), Fraction()),
    )
    positive = (Fraction(1), Fraction(1))
    negative = (Fraction(1), Fraction(-1))
    positive_image = matrix_vector(centered_selected, positive)
    negative_image = matrix_vector(centered_selected, negative)
    if positive_image != positive or negative_image != tuple(
        -value for value in negative
    ):
        raise ArithmeticError("Wick collision spectrum failed")
    positive_value = sum(
        (value * image for value, image in zip(positive, positive_image, strict=True)),
        Fraction(),
    )
    negative_value = sum(
        (value * image for value, image in zip(negative, negative_image, strict=True)),
        Fraction(),
    )
    if positive_value != 2 or negative_value != -2:
        raise ArithmeticError("Wick collision witnesses failed")
    return (
        {
            "matrix": ((0, 1), (1, 0)),
            "positive_eigenvalue": 1,
            "negative_eigenvalue": -1,
            "positive_quadratic_value": 2,
            "negative_quadratic_value": -2,
            "sharp_diagonal_repair": 1,
        },
        4,
    )


def direct_checkerboard_5_13() -> tuple[dict[str, object], int]:
    primes = (5, 13)
    local_grams = tuple(local_square_phase_gram(prime) for prime in primes)
    gram = kronecker(local_grams[0], local_grams[1])
    top = tensor_vector(*(legendre_sign_vector(prime) for prime in primes))
    native_amplitude = len(gram)
    constant_eigenvalue = prod((prime + 1) // 2 for prime in primes)
    top_eigenvalue = prod(primes)
    ones = (Fraction(1),) * native_amplitude
    if matrix_vector(gram, ones) != (Fraction(constant_eigenvalue),) * native_amplitude:
        raise ArithmeticError("direct constant Gram eigenline failed")
    if matrix_vector(gram, top) != tuple(
        Fraction(top_eigenvalue) * value for value in top
    ):
        raise ArithmeticError("direct top-character Gram eigenline failed")

    support = tuple(index for index, value in enumerate(top) if value == 1)
    restricted = tuple(
        tuple(gram[row][column] for column in support) for row in support
    )
    restricted_ones = (Fraction(1),) * len(support)
    row_sums = matrix_vector(restricted, restricted_ones)
    expected_row_sum = Fraction(constant_eigenvalue + top_eigenvalue, 2)
    if row_sums != (expected_row_sum,) * len(support):
        raise ArithmeticError("direct restricted Gram row sum failed")
    gram_energy = sum(row_sums, Fraction())
    if gram_energy != 258:
        raise ArithmeticError("direct restricted Gram energy failed")

    optimizer = tuple(
        Fraction(native_amplitude) * row_sum / gram_energy for row_sum in row_sums
    )
    if optimizer != (Fraction(2),) * len(support):
        raise ArithmeticError("direct restricted optimizer is not uniform weight two")
    dual_solution = tuple(Fraction(2, expected_row_sum) for _ in support)
    if matrix_vector(restricted, dual_solution) != optimizer:
        raise ArithmeticError("direct restricted Gram solve failed")
    restricted_leverage = sum(
        (
            weight * solution
            for weight, solution in zip(optimizer, dual_solution, strict=True)
        ),
        Fraction(),
    )
    if restricted_leverage != Fraction(24, 43):
        raise ArithmeticError("direct restricted leverage failed")

    return (
        {
            "primes": primes,
            "native_amplitude": native_amplitude,
            "full_matrix_order": native_amplitude,
            "retained_coordinates": len(support),
            "constant_eigenvalue": constant_eigenvalue,
            "top_eigenvalue": top_eigenvalue,
            "restricted_gram_energy": int(gram_energy),
            "restricted_row_sum": str(expected_row_sum),
            "optimizer_weight": "2",
            "restricted_leverage": str(restricted_leverage),
            "complete_tensor_leverage": str(
                Fraction(native_amplitude, constant_eigenvalue)
            ),
        },
        sum(len(matrix) * len(matrix[0]) for matrix in local_grams)
        + native_amplitude * native_amplitude
        + len(support) * len(support),
    )


def panel_row(primes: tuple[int, ...]) -> dict[str, object]:
    if not primes or any(prime % 4 != 1 for prime in primes):
        raise ValueError("panel primes must all be 1 modulo 4")
    native_amplitude = prod((prime - 1) // 2 for prime in primes)
    constant_eigenvalue = prod((prime + 1) // 2 for prime in primes)
    top_eigenvalue = prod(primes)
    full_leverage = Fraction(native_amplitude, constant_eigenvalue)
    hard_leverage = Fraction(4 * native_amplitude, constant_eigenvalue + top_eigenvalue)
    ratio = hard_leverage / full_leverage
    if ratio != Fraction(4 * constant_eigenvalue, constant_eigenvalue + top_eigenvalue):
        raise ArithmeticError("checkerboard leverage ratio failed")
    return {
        "primes": primes,
        "native_amplitude": native_amplitude,
        "constant_eigenvalue": constant_eigenvalue,
        "top_eigenvalue": top_eigenvalue,
        "full_leverage": str(full_leverage),
        "hard_leverage": str(hard_leverage),
        "hard_to_full_ratio": str(ratio),
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
    dimension_rows: list[dict[str, object]] = []
    walsh_summands = 0
    for dimension in range(1, MAX_DIMENSION + 1):
        row, cost = check_dimension(dimension)
        dimension_rows.append(row)
        walsh_summands += cost
        if walsh_summands > MAX_WALSH_SUMMANDS:
            raise RuntimeError("Walsh summand cap exceeded")

    panels = [
        panel_row(PRIME_PANEL[:length]) for length in range(1, len(PRIME_PANEL) + 1)
    ]
    for left, right in pairwise(panels[1:]):
        if Fraction(right["hard_to_full_ratio"]) >= Fraction(
            left["hard_to_full_ratio"]
        ):
            raise ArithmeticError("panel ratio failed to decrease")

    wick_witness, wick_matrix_entries = wick_spectrum_witness()
    direct_gram, gram_matrix_entries = direct_checkerboard_5_13()
    direct_matrix_entries = wick_matrix_entries + gram_matrix_entries
    if direct_matrix_entries > MAX_DIRECT_MATRIX_ENTRIES:
        raise RuntimeError("direct matrix-entry cap exceeded")

    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return {
        "schema": "riemann.function_field.ffps_finite_abelian_subgroup_mask.v2",
        "status": "EXACT_FINITE_ABELIAN_SUBGROUP_COMPRESSION",
        "exact_theorems": {
            "relative_projector": "C_A-S_A=Pi_trivial",
            "index_h_coset": "h Fourier lines, h-1 selected lines and mass",
            "checkerboard": "one selected top-character line for every d",
            "wick": "sharp selected diagonal repair one, witnessed at u=1",
            "direct_checkerboard_5_13": (
                "12x12 Gram, six retained coordinates, optimizer two, leverage 24/43"
            ),
        },
        "dimensions": dimension_rows,
        "prime_panels": panels,
        "wick_spectrum_witness": wick_witness,
        "direct_checkerboard_5_13": direct_gram,
        "resource_ledger": {
            "walsh_summands": walsh_summands,
            "max_walsh_summands": MAX_WALSH_SUMMANDS,
            "direct_matrix_entries_accounted": direct_matrix_entries,
            "max_direct_matrix_entries": MAX_DIRECT_MATRIX_ENTRIES,
            "conductors_enumerated": 0,
            "curves_enumerated": 0,
            "l_function_zeros_enumerated": 0,
        },
        "open": [
            "growing-factor physical source realization",
            "rank-one tensor conductor and Betti bound after cleanup",
            "varying-conductor trace estimate",
            "RH and GRH",
        ],
    }


def run_checks() -> dict[str, object]:
    check_source_blobs()
    report = build_report()
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "quotient compression",
        "one selected Fourier line",
        "rank is one for every `d`",
        "native amplitude",
        "independently reconstructs the `(5,13)` restricted Gram",
        "`J_2-I_2` with both eigenvectors",
        "growing-`d` physical source | **OPEN**",
        "RH, or GRH | **OPEN / RH-BEARING**",
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
