#!/usr/bin/env python3
"""Exact replay for the atom-free/positive-semidefinite incompatibility."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

MAX_QUOTIENT_ORDER = 8
MAX_COSET_SIZE = 5
MAX_MATRIX_SIZE = MAX_QUOTIENT_ORDER * MAX_COSET_SIZE


def matvec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [
        sum(entry * value for entry, value in zip(row, vector, strict=True))
        for row in matrix
    ]


def scaled(vector: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * value for value in vector]


def off_coset_kernel(quotient_order: int, coset_size: int) -> list[list[Fraction]]:
    if (
        isinstance(quotient_order, bool)
        or not isinstance(quotient_order, int)
        or quotient_order < 2
        or quotient_order > MAX_QUOTIENT_ORDER
    ):
        raise ValueError("quotient_order is outside the replay range")
    if (
        isinstance(coset_size, bool)
        or not isinstance(coset_size, int)
        or coset_size < 1
        or coset_size > MAX_COSET_SIZE
    ):
        raise ValueError("coset_size is outside the replay range")
    coefficient = Fraction(quotient_order, quotient_order - 1)
    size = quotient_order * coset_size
    return [
        [
            Fraction(0) if row // coset_size == column // coset_size else coefficient
            for column in range(size)
        ]
        for row in range(size)
    ]


def signature_certificate(quotient_order: int, coset_size: int) -> dict[str, object]:
    kernel = off_coset_kernel(quotient_order, coset_size)
    size = quotient_order * coset_size
    positive = Fraction(size)
    negative = Fraction(-size, quotient_order - 1)
    zero = Fraction(0)

    constant = [Fraction(1)] * size
    if matvec(kernel, constant) != scaled(constant, positive):
        raise AssertionError("constant eigenline certificate failed")

    quotient_vectors = []
    for coset in range(1, quotient_order):
        vector = [Fraction(0)] * size
        for index in range(coset_size):
            vector[index] = 1
            vector[coset * coset_size + index] = -1
        if matvec(kernel, vector) != scaled(vector, negative):
            raise AssertionError("quotient eigenvector certificate failed")
        quotient_vectors.append(vector)

    within_vectors = []
    for coset in range(quotient_order):
        for offset in range(1, coset_size):
            vector = [Fraction(0)] * size
            vector[coset * coset_size] = 1
            vector[coset * coset_size + offset] = -1
            if matvec(kernel, vector) != scaled(vector, zero):
                raise AssertionError("within-coset null vector certificate failed")
            within_vectors.append(vector)

    diagonal_repair = -negative
    return {
        "quotient_order": quotient_order,
        "coset_size": coset_size,
        "atom_count": size,
        "positive_eigenvalue": str(positive),
        "positive_multiplicity": 1,
        "negative_eigenvalue": str(negative),
        "negative_multiplicity": len(quotient_vectors),
        "zero_eigenvalue": "0",
        "zero_multiplicity": len(within_vectors),
        "certificate_dimension": 1 + len(quotient_vectors) + len(within_vectors),
        "sharp_scalar_diagonal_repair": str(diagonal_repair),
        "literal_diagonal_before_repair": "0",
    }


def run() -> dict[str, object]:
    panels = [
        signature_certificate(quotient_order, coset_size)
        for quotient_order in (2, 4, 8)
        for coset_size in (1, 2, 5)
    ]
    return {
        "exact_theorems": {
            "zero_diagonal_psd": (
                "A Hermitian positive-semidefinite matrix with zero diagonal is zero"
            ),
            "principal_domination": (
                "K >= c vv* implies K_ii >= c |v_i|^2 for every i"
            ),
            "off_coset_signature": (
                "for h balanced cosets of size n: eigenvalues hn (once), "
                "-hn/(h-1) (h-1 times), and 0 (h(n-1) times)"
            ),
            "deduction": (
                "exact atom deletion and nontrivial positive principal domination "
                "cannot coexist in one quadratic kernel"
            ),
        },
        "panels": panels,
        "resource_caps": {
            "maximum_quotient_order": MAX_QUOTIENT_ORDER,
            "maximum_coset_size": MAX_COSET_SIZE,
            "maximum_matrix_size": MAX_MATRIX_SIZE,
            "floating_point_operations": 0,
            "point_counts": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
