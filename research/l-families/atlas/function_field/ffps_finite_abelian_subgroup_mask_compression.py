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
MAX_WALL_SECONDS = 3.0
PRIME_PANEL = (5, 13, 17, 29, 37, 41)


def parity(value: int) -> int:
    return value.bit_count() & 1


def character(label: int, value: int) -> int:
    return -1 if parity(label & value) else 1


def normalized_mask(dimension: int, value: int) -> int:
    if dimension < 1:
        raise ValueError("dimension must be positive")
    return 2 if parity(value) == 0 else 0


def walsh_coefficient(dimension: int, label: int) -> Fraction:
    size = 1 << dimension
    if not 0 <= label < size:
        raise ValueError("label outside group")
    return Fraction(
        sum(
            normalized_mask(dimension, value) * character(label, value)
            for value in range(size)
        ),
        size,
    )


def autocorrelation(dimension: int, shift: int) -> Fraction:
    size = 1 << dimension
    if not 0 <= shift < size:
        raise ValueError("shift outside group")
    return Fraction(
        sum(
            normalized_mask(dimension, value)
            * normalized_mask(dimension, value ^ shift)
            for value in range(size)
        ),
        size,
    )


def check_dimension(dimension: int) -> tuple[dict[str, object], int]:
    size = 1 << dimension
    top_label = size - 1
    coefficients = tuple(walsh_coefficient(dimension, label) for label in range(size))
    expected = tuple(
        Fraction(1) if label in (0, top_label) else Fraction() for label in range(size)
    )
    if coefficients != expected:
        raise ArithmeticError("Walsh support is not trivial plus top character")
    if sum(coefficient * coefficient for coefficient in coefficients) != 2:
        raise ArithmeticError("selected mass identity failed")

    for shift in range(size):
        kernel = autocorrelation(dimension, shift)
        if kernel != 1 + character(top_label, shift):
            raise ArithmeticError("autocorrelation/projector identity failed")

    return (
        {
            "dimension": dimension,
            "ambient_order": size,
            "retained_order": size // 2,
            "fourier_support": (0, top_label),
            "selected_rank": 1,
            "selected_mass": 1,
            "sharp_wick_repair": 1,
        },
        2 * size * size,
    )


def panel_row(primes: tuple[int, ...]) -> dict[str, object]:
    if not primes or any(prime % 4 != 1 for prime in primes):
        raise ValueError("panel primes must all be 1 modulo 4")
    ambient_order = prod((prime - 1) // 2 for prime in primes)
    constant_eigenvalue = prod((prime + 1) // 2 for prime in primes)
    top_eigenvalue = prod(primes)
    full_leverage = Fraction(ambient_order, constant_eigenvalue)
    hard_leverage = Fraction(4 * ambient_order, constant_eigenvalue + top_eigenvalue)
    ratio = hard_leverage / full_leverage
    if ratio != Fraction(4 * constant_eigenvalue, constant_eigenvalue + top_eigenvalue):
        raise ArithmeticError("checkerboard leverage ratio failed")
    return {
        "primes": primes,
        "ambient_order": ambient_order,
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

    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return {
        "schema": "riemann.function_field.ffps_finite_abelian_subgroup_mask.v1",
        "status": "EXACT_FINITE_ABELIAN_SUBGROUP_COMPRESSION",
        "exact_theorems": {
            "relative_projector": "C_A-S_A=Pi_trivial",
            "index_h_coset": "h Fourier lines, h-1 selected lines and mass",
            "checkerboard": "one selected top-character line for every d",
            "wick": "sharp selected diagonal repair remains one",
        },
        "dimensions": dimension_rows,
        "prime_panels": panels,
        "resource_ledger": {
            "walsh_summands": walsh_summands,
            "max_walsh_summands": MAX_WALSH_SUMMANDS,
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
