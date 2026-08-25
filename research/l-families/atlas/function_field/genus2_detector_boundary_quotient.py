#!/usr/bin/env python3
"""Exact low-weight boundary filtration for the genus-two quintic family.

The five input character means are already proved for every odd prime power
by the genus-two moment packet.  This module performs only exact integer
linear algebra on their q^{-1},...,q^{-5} coefficient vectors.  It does not
enumerate a finite field or infer a high-weight/cohomological formula.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence

import genus2_q_scan as upstream


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_detector_boundary_quotient.json"
NOTE_PATH = HERE / "GENUS2_DETECTOR_BOUNDARY_QUOTIENT.md"
TEST_PATH = ROOT / "tests" / "test_genus2_detector_boundary_quotient.py"
UPSTREAM_PATH = HERE / "genus2_q_scan.py"
MOMENT_NOTE_PATH = HERE / "GENUS2_MOMENT_IDENTITY.md"
NULL_MODULE_PATH = HERE / "VIRTUAL_CHARACTER_NULL_DIRECTIONS.md"

BASIS = ("chi_(0,1)", "chi_(2,0)", "chi_(0,2)", "chi_(2,1)", "chi_(4,0)")
POWERS = (1, 2, 3, 4, 5)

# Columns are the exact coefficients of q^-1,...,q^-5 in the five proved
# character means, in BASIS order.
MEAN_COLUMNS: dict[str, tuple[int, ...]] = {
    "chi_(0,1)": (-1, 1, 0, -1, 0),
    "chi_(2,0)": (0, 0, 1, -1, 0),
    "chi_(0,2)": (-1, 0, 0, 0, -1),
    "chi_(2,1)": (0, 0, 2, -1, -2),
    "chi_(4,0)": (0, 0, 0, 0, -3),
}

# F^m consists of combinations whose exact family mean is O(q^-m).
# Each tuple below is a saturated Z-basis written in BASIS coordinates.
FILTRATION_BASES: dict[int, tuple[tuple[int, ...], ...]] = {
    1: (
        (1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0),
        (0, 0, 0, 0, 1),
    ),
    2: (
        (0, 1, 0, 0, 0),
        (1, 0, -1, 0, 0),
        (0, 0, 0, 1, 0),
        (0, 0, 0, 0, 1),
    ),
    3: (
        (0, 1, 0, 0, 0),
        (0, 0, 0, 1, 0),
        (0, 0, 0, 0, 1),
    ),
    4: (
        (0, 2, 0, -1, 0),
        (0, 0, 0, 0, 1),
    ),
    5: ((0, 0, 0, 0, 1),),
    6: (),
}


def _sha256_lf(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def coefficient_matrix() -> tuple[tuple[int, ...], ...]:
    """Return rows indexed by q^-power and columns indexed by BASIS."""

    return tuple(
        tuple(MEAN_COLUMNS[label][row] for label in BASIS)
        for row in range(len(POWERS))
    )


def matrix_vector(
    matrix: Sequence[Sequence[int]], vector: Sequence[int]
) -> tuple[int, ...]:
    if any(len(row) != len(vector) for row in matrix):
        raise ValueError("matrix/vector dimension mismatch")
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def exact_mean_coefficients(vector: Sequence[int]) -> tuple[int, ...]:
    if len(vector) != len(BASIS):
        raise ValueError("detector vector has the wrong dimension")
    return matrix_vector(coefficient_matrix(), vector)


def evaluate_laurent(coefficients: Sequence[int], q: int) -> Fraction:
    if q <= 1:
        raise ValueError("q must exceed one")
    if len(coefficients) != len(POWERS):
        raise ValueError("coefficient vector has the wrong dimension")
    return sum(
        (Fraction(coefficient, q**power) for power, coefficient in zip(POWERS, coefficients)),
        Fraction(0),
    )


def detector_mean(vector: Sequence[int], q: int) -> Fraction:
    return evaluate_laurent(exact_mean_coefficients(vector), q)


def _bareiss_determinant(matrix: Sequence[Sequence[int]]) -> int:
    """Fraction-free determinant for the fixed small square matrix."""

    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a nonempty square matrix")
    work = [list(row) for row in matrix]
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if work[pivot_index][pivot_index] == 0:
            swap = next(
                (
                    row
                    for row in range(pivot_index + 1, size)
                    if work[row][pivot_index]
                ),
                None,
            )
            if swap is None:
                return 0
            work[pivot_index], work[swap] = work[swap], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = work[row][column] * pivot - work[row][pivot_index] * work[pivot_index][column]
                if numerator % previous:
                    raise ArithmeticError("Bareiss division ceased to be exact")
                work[row][column] = numerator // previous
        previous = pivot
        for row in range(pivot_index + 1, size):
            work[row][pivot_index] = 0
    return sign * work[-1][-1]


def _fraction_rref(
    matrix: Sequence[Sequence[int]],
) -> tuple[list[list[Fraction]], tuple[int, ...]]:
    if not matrix:
        return [], ()
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("ragged matrix")
    work = [[Fraction(value) for value in row] for row in matrix]
    pivots: list[int] = []
    pivot_row = 0
    for column in range(width):
        selected = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if selected is None:
            continue
        work[pivot_row], work[selected] = work[selected], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            multiple = work[row][column]
            work[row] = [
                left - multiple * right
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(work):
            break
    return work, tuple(pivots)


def _primitive_integer(vector: Iterable[Fraction]) -> tuple[int, ...]:
    values = tuple(vector)
    denominator = 1
    for value in values:
        denominator = math.lcm(denominator, value.denominator)
    integers = [value.numerator * (denominator // value.denominator) for value in values]
    divisor = 0
    for value in integers:
        divisor = math.gcd(divisor, abs(value))
    if divisor:
        integers = [value // divisor for value in integers]
    first = next((value for value in integers if value), 1)
    if first < 0:
        integers = [-value for value in integers]
    return tuple(integers)


def rational_nullspace_basis(
    matrix: Sequence[Sequence[int]], width: int = len(BASIS)
) -> tuple[tuple[int, ...], ...]:
    """Return canonical primitive vectors for the rational nullspace."""

    if not matrix:
        return tuple(
            tuple(1 if row == column else 0 for row in range(width))
            for column in range(width)
        )
    reduced, pivots = _fraction_rref(matrix)
    free = tuple(column for column in range(width) if column not in pivots)
    basis: list[tuple[int, ...]] = []
    for free_column in free:
        vector = [Fraction(0) for _ in range(width)]
        vector[free_column] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_column]
        basis.append(_primitive_integer(vector))
    return tuple(basis)


def leading_power(coefficients: Sequence[int]) -> int | None:
    return next(
        (power for power, coefficient in zip(POWERS, coefficients) if coefficient),
        None,
    )


def _combination_label(vector: Sequence[int]) -> str:
    terms: list[str] = []
    for coefficient, label in zip(vector, BASIS):
        if not coefficient:
            continue
        terms.append(f"{coefficient:+d}*{label}")
    return " ".join(terms).lstrip("+") or "0"


def _verify_upstream_means() -> None:
    for q in (3, 5, 7, 9, 11, 13):
        expected = upstream.candidate_low_weight_character_means(q)
        actual = {
            label: evaluate_laurent(MEAN_COLUMNS[label], q) for label in BASIS
        }
        if actual != expected:
            raise ArithmeticError(f"upstream character mean drift at q={q}")


def _verify_filtration(matrix: tuple[tuple[int, ...], ...]) -> None:
    for order, expected_basis in FILTRATION_BASES.items():
        prefix = matrix[: order - 1]
        actual = rational_nullspace_basis(prefix)
        # RREF chooses a canonical free-variable basis.  The declared saturated
        # bases use the same normalization in this triangular matrix.
        if actual != expected_basis:
            raise ArithmeticError(
                f"boundary filtration drift at F^{order}: {actual} != {expected_basis}"
            )
        for vector in expected_basis:
            if any(matrix_vector(prefix, vector)):
                raise ArithmeticError(f"declared F^{order} vector is not in the kernel")


def build_fixture() -> dict[str, object]:
    _verify_upstream_means()
    matrix = coefficient_matrix()
    determinant = _bareiss_determinant(matrix)
    if determinant != 3:
        raise ArithmeticError(f"boundary matrix determinant drifted: {determinant}")
    _verify_filtration(matrix)

    inverse_numerator = (1, -1, -2, -2, -1)
    # The image congruence is the obstruction to integrality of c_40 in the
    # explicit inverse formula.
    left_mod_three = tuple(
        sum(inverse_numerator[row] * matrix[row][column] for row in range(5))
        for column in range(5)
    )
    if any(value % 3 for value in left_mod_three):
        raise ArithmeticError("claimed index-three image congruence failed")

    distinguished = {
        "balanced_symmetry_detector_B": (0, 1, -1, 0, 0),
        "first_q^-2_cancellation": (1, 0, -1, 0, 0),
        "first_q^-3_cancellation": (0, 1, 0, 0, 0),
        "first_q^-4_cancellation": (0, -2, 0, 1, 0),
        "first_q^-5_cancellation": (0, 0, 0, 0, 1),
    }
    distinguished_rows = []
    for name, vector in distinguished.items():
        coefficients = exact_mean_coefficients(vector)
        distinguished_rows.append(
            {
                "name": name,
                "basis_vector": list(vector),
                "character_combination": _combination_label(vector),
                "mean_coefficients_q^-1_through_q^-5": list(coefficients),
                "leading_power": leading_power(coefficients),
                "l1_support": sum(abs(value) for value in vector),
            }
        )

    filtration_rows = []
    for order, basis in FILTRATION_BASES.items():
        filtration_rows.append(
            {
                "order": order,
                "definition": f"F^{order}={{D: mean_q(D)=O(q^-{order})}}",
                "rank": len(basis),
                "basis_vectors": [list(vector) for vector in basis],
                "basis_labels": [_combination_label(vector) for vector in basis],
            }
        )

    return {
        "schema": "riemann.function_field.genus2_detector_boundary_quotient.v1",
        "status": "EXACT_ALL_ODD_Q_LOW_WEIGHT_BOUNDARY_FILTRATION",
        "scope": {
            "family": "all monic squarefree quintics over F_q, q an odd prime power",
            "character_lattice": list(BASIS),
            "finite_field_enumeration": False,
            "random_sampling": False,
            "cohomological_identification": False,
            "rh_or_grh_implication": False,
        },
        "coefficient_convention": {
            "rows": [f"q^-{power}" for power in POWERS],
            "columns": list(BASIS),
            "matrix": [list(row) for row in matrix],
            "meaning": "M*c is the exact coefficient vector of the proved family mean",
        },
        "theorems": {
            "injectivity": {
                "determinant": determinant,
                "statement": "No nonzero detector in the declared low-weight lattice has identically zero family mean for every odd prime power q.",
            },
            "cokernel": {
                "order": abs(determinant),
                "smith_invariants": [1, 1, 1, 1, 3],
                "image_congruence": "m1-m2-2*m3-2*m4-m5 == 0 (mod 3)",
                "inverse": {
                    "c_01": "m2",
                    "c_02": "-m1-m2",
                    "c_21": "m2+m3+m4",
                    "c_20": "-2*m2-m3-2*m4",
                    "c_40": "(m1-m2-2*m3-2*m4-m5)/3",
                },
            },
            "boundary_filtration": filtration_rows,
            "rank_sequence_F1_through_F6": [
                len(FILTRATION_BASES[order]) for order in range(1, 7)
            ],
            "interpretation": (
                "Each successive q^-j boundary channel removes exactly one rank. "
                "The unique line surviving cancellation through q^-4 is chi_(4,0), "
                "whose exact mean is -3*q^-5."
            ),
        },
        "distinguished_detectors": distinguished_rows,
        "separation_firewalls": {
            "B": (
                "B=chi_(2,0)-chi_(0,2) has an exactly symmetric USp(4) Haar law, "
                "but its arithmetic mean begins at q^-1; compact symmetry and finite-q "
                "boundary suppression are different design constraints."
            ),
            "R6": (
                "R6 is outside the proved low-weight lattice.  The quotient does not "
                "evaluate mean(R6), identify a Siegel form, or turn the q=3,5,7 values "
                "into an all-q theorem."
            ),
        },
        "smallest_next_theorem": (
            "Extend the exact boundary matrix by one independently proved high-weight "
            "mean (preferably chi_(0,3) or R6), then recompute the saturated filtration."
        ),
        "provenance": {
            "frozen_atlas_commit": "10446e8ea9c55162c317810f63c1f7a379466459",
            "source_hashes_lf_sha256": {
                "producer": _sha256_lf(Path(__file__)),
                "note": _sha256_lf(NOTE_PATH),
                "test": _sha256_lf(TEST_PATH),
                "upstream_character_means": _sha256_lf(UPSTREAM_PATH),
                "all_q_moment_proof_note": _sha256_lf(MOMENT_NOTE_PATH),
                "null_module_note": _sha256_lf(NULL_MODULE_PATH),
            },
            "work_units": {
                "matrix_entries": 25,
                "filtration_levels": 6,
                "finite_field_candidates": 0,
            },
        },
    }


def _canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()
    fixture = build_fixture()
    rendered = _canonical(fixture)
    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            raise SystemExit("genus-two detector boundary fixture drifted")
        print("PASS_GENUS2_DETECTOR_BOUNDARY_QUOTIENT")
        return
    if args.stdout:
        print(rendered, end="")
        return
    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
