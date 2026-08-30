#!/usr/bin/env python3
"""Exact fixed-fibre Wick occupancy algebra and bounded controls."""

from __future__ import annotations

import argparse
import ast
import json
import subprocess
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_SHARED_FIBRE_WICK_OCCUPANCY_SPECTRUM.md"
FIXTURE_PATH = HERE / "ffps_shared_fibre_wick_occupancy_spectrum.json"
SOURCE_LOCK_PATH = HERE / "ffps_shared_fibre_wick_occupancy_spectrum.sources.json"

SOURCE_BLOBS = {
    (
        "b8cf095e7446583af80cbe4ff5d04257b6901d97",
        "research/l-families/atlas/function_field/FFPS_MARKED_PLACE_SIGNED_DESCENT_GATE0.md",
    ): "aad29a0401d0f26c3dceadaaaaf017af6da95ec1",
    (
        "b8cf095e7446583af80cbe4ff5d04257b6901d97",
        "research/l-families/atlas/function_field/ffps_marked_place_signed_descent_gate0.sources.json",
    ): "b62cc787177e51bd89ef33307bd08916c16d8d1d",
    (
        "3a595dda92ef827a41e50d2395309692a93748ad",
        "research/l-families/atlas/function_field/FFPS_RELATIVE_TRACE_TENSOR_CLOSURE.md",
    ): "37647db8c43b983dc64bfc71a0c112539119a98a",
    (
        "3a595dda92ef827a41e50d2395309692a93748ad",
        "research/l-families/atlas/function_field/FFPS_RELATIVE_EXTERNAL_DIAGONAL_ADAMS.md",
    ): "884f2fc949bbd5b076df0c0c7afd4711f81ce37e",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ): "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106131-wick-normal-ordering-additive-kummer-decomposition.md",
    ): "37722c3f36ec7d1681f34d4329a3795e5028f7ae",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106191-source-dual-centered-double-incidence-correlation.md",
    ): "85c4ef92ead7d8b235f9c195c3c0acd16d16030f",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
    ): "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
}

CONTROL_PAIRS = ((3, 5), (3, 7), (5, 7))
HELD_OUT_PAIR = (7, 11)
MAX_SIMPLE_MATRIX_DIMENSION = 15
MAX_ENVELOPE_POINTS = 900

Matrix = tuple[tuple[Fraction, ...], ...]


def is_prime(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def validate_pair(ell: int, rho: int) -> tuple[int, int]:
    if not is_prime(ell) or not is_prime(rho):
        raise ValueError("ell and rho must be primes")
    if ell == 2 or rho == 2 or ell == rho:
        raise ValueError("ell and rho must be distinct odd primes")
    return ell, rho


def validate_character(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value not in (-1, 1):
        raise ValueError("quadratic class must be -1 or 1")
    return value


def legendre_symbol(value: int, prime: int) -> int:
    if not is_prime(prime) or prime == 2:
        raise ValueError("prime must be odd")
    residue = value % prime
    if residue == 0:
        return 0
    power = pow(residue, (prime - 1) // 2, prime)
    if power == 1:
        return 1
    if power == prime - 1:
        return -1
    raise ArithmeticError("Euler criterion failed")


def quadratic_class(prime: int, character: int) -> tuple[int, ...]:
    validate_character(character)
    if not is_prime(prime) or prime == 2:
        raise ValueError("prime must be odd")
    return tuple(
        residue
        for residue in range(1, prime)
        if legendre_symbol(residue, prime) == character
    )


def allowed_cells(
    ell: int, rho: int, sigma: int = 1, tau: int = 1
) -> tuple[tuple[int, int], ...]:
    """Physical (x mod ell, y mod rho) cells in one fixed owner-class fibre."""

    validate_pair(ell, rho)
    validate_character(sigma)
    validate_character(tau)
    x_character = legendre_symbol(-1, ell) * sigma
    return tuple(product(quadratic_class(ell, x_character), quadratic_class(rho, tau)))


def physical_residue_map(
    ell: int,
    rho: int,
    q_owner: int,
    v_cofactor: int,
    p_owner: int,
    u_cofactor: int,
) -> tuple[int, int]:
    """Map fixed-fibre owner/cofactor residues to the two additive phases."""

    validate_pair(ell, rho)
    residues = (
        (q_owner, ell, "Q mod ell"),
        (v_cofactor, ell, "v mod ell"),
        (p_owner, rho, "P mod rho"),
        (u_cofactor, rho, "u mod rho"),
    )
    for value, modulus, name in residues:
        if value % modulus == 0:
            raise ValueError(f"{name} must be a unit")
    x_value = (-q_owner * pow(rho, 2, ell) * pow(v_cofactor, 2, ell)) % ell
    y_value = (p_owner * pow(ell, 2, rho) * pow(u_cofactor, 2, rho)) % rho
    return x_value, y_value


def residue_envelope_counts(
    ell: int, rho: int, sigma: int = 1, tau: int = 1
) -> Counter[tuple[int, int]]:
    """Enumerate the ambient unit-residue envelope, not the live source."""

    validate_pair(ell, rho)
    validate_character(sigma)
    validate_character(tau)
    counts: Counter[tuple[int, int]] = Counter()
    for q_owner, v_cofactor, p_owner, u_cofactor in product(
        quadratic_class(ell, sigma),
        range(1, ell),
        quadratic_class(rho, tau),
        range(1, rho),
    ):
        counts[
            physical_residue_map(
                ell,
                rho,
                q_owner,
                v_cofactor,
                p_owner,
                u_cofactor,
            )
        ] += 1
        if sum(counts.values()) > MAX_ENVELOPE_POINTS:
            raise RuntimeError("residue-envelope cap exceeded")
    return counts


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def centered_incidence_matrix(prime: int) -> Matrix:
    """H_q=I-J/q on one fixed quadratic class of nonzero residues."""

    if not is_prime(prime) or prime == 2:
        raise ValueError("prime must be odd")
    size = (prime - 1) // 2
    return tuple(
        tuple(
            Fraction(int(row == column)) - Fraction(1, prime) for column in range(size)
        )
        for row in range(size)
    )


def kronecker(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right:
        raise ValueError("Kronecker factors must be nonempty")
    if any(len(row) != len(left[0]) for row in left):
        raise ValueError("left factor must be rectangular")
    if any(len(row) != len(right[0]) for row in right):
        raise ValueError("right factor must be rectangular")
    return tuple(
        tuple(
            left[left_row][left_column] * right[right_row][right_column]
            for left_column in range(len(left[0]))
            for right_column in range(len(right[0]))
        )
        for left_row in range(len(left))
        for right_row in range(len(right))
    )


def tensor_kernel(ell: int, rho: int) -> Matrix:
    validate_pair(ell, rho)
    return kronecker(centered_incidence_matrix(ell), centered_incidence_matrix(rho))


def atomic_diagonal(ell: int, rho: int) -> Fraction:
    validate_pair(ell, rho)
    return Fraction(ell - 1, ell) * Fraction(rho - 1, rho)


def identity_matrix(size: int) -> Matrix:
    if isinstance(size, bool) or not isinstance(size, int) or size < 1:
        raise ValueError("matrix size must be positive")
    return tuple(
        tuple(Fraction(int(row == column)) for column in range(size))
        for row in range(size)
    )


def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    if not left or len(left) != len(right):
        raise ValueError("matrix dimensions differ")
    if any(len(a) != len(b) for a, b in zip(left, right, strict=True)):
        raise ValueError("matrix dimensions differ")
    return tuple(
        tuple(a - b for a, b in zip(left_row, right_row, strict=True))
        for left_row, right_row in zip(left, right, strict=True)
    )


def scalar_matrix(value: Fraction, matrix: Matrix) -> Matrix:
    return tuple(tuple(value * entry for entry in row) for row in matrix)


def transpose(matrix: Matrix) -> Matrix:
    if not matrix or any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("matrix must be nonempty and rectangular")
    return tuple(
        tuple(matrix[row][column] for row in range(len(matrix)))
        for column in range(len(matrix[0]))
    )


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("matrix dimensions do not compose")
    if any(len(row) != len(left[0]) for row in left):
        raise ValueError("left matrix must be rectangular")
    if any(len(row) != len(right[0]) for row in right):
        raise ValueError("right matrix must be rectangular")
    right_t = transpose(right)
    return tuple(
        tuple(
            sum(
                (a * b for a, b in zip(left_row, right_column, strict=True)),
                Fraction(),
            )
            for right_column in right_t
        )
        for left_row in left
    )


def simple_complete_cell_wick_matrix(ell: int, rho: int) -> Matrix:
    kernel = tensor_kernel(ell, rho)
    dimension = len(kernel)
    return matrix_subtract(
        kernel,
        scalar_matrix(atomic_diagonal(ell, rho), identity_matrix(dimension)),
    )


def matrix_rank(matrix: Matrix) -> int:
    if not matrix:
        return 0
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("matrix must be rectangular")
    work = [list(row) for row in matrix]
    rank = 0
    for column in range(width):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][column]
        work[rank] = [entry / pivot_value for entry in work[rank]]
        for row in range(len(work)):
            if row == rank or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(work[row], work[rank], strict=True)
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


def aggregation_matrix(cell_count: int, assignments: tuple[int, ...]) -> Matrix:
    if (
        isinstance(cell_count, bool)
        or not isinstance(cell_count, int)
        or cell_count < 1
    ):
        raise ValueError("cell count must be positive")
    if not assignments:
        raise ValueError("at least one literal atom is required")
    if any(
        isinstance(cell, bool)
        or not isinstance(cell, int)
        or not 0 <= cell < cell_count
        for cell in assignments
    ):
        raise ValueError("atom assignment is outside the cell set")
    return tuple(
        tuple(Fraction(int(cell == assigned)) for assigned in assignments)
        for cell in range(cell_count)
    )


def occupancy_wick_matrix(ell: int, rho: int, assignments: tuple[int, ...]) -> Matrix:
    kernel = tensor_kernel(ell, rho)
    incidence = aggregation_matrix(len(kernel), assignments)
    pullback = matrix_multiply(transpose(incidence), matrix_multiply(kernel, incidence))
    return matrix_subtract(
        pullback,
        scalar_matrix(atomic_diagonal(ell, rho), identity_matrix(len(assignments))),
    )


def quadratic_form(matrix: Matrix, vector: tuple[Fraction, ...]) -> Fraction:
    if not matrix or len(matrix) != len(vector):
        raise ValueError("matrix and vector dimensions differ")
    if any(len(row) != len(vector) for row in matrix):
        raise ValueError("quadratic-form matrix must be square")
    return sum(
        (
            vector[row] * matrix[row][column] * vector[column]
            for row in range(len(vector))
            for column in range(len(vector))
        ),
        Fraction(),
    )


def aggregate_vector(
    cell_count: int,
    assignments: tuple[int, ...],
    vector: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    incidence = aggregation_matrix(cell_count, assignments)
    if len(assignments) != len(vector):
        raise ValueError("assignment and vector lengths differ")
    return tuple(
        sum(
            (entry * value for entry, value in zip(row, vector, strict=True)),
            Fraction(),
        )
        for row in incidence
    )


def direct_off_atomic_form(
    ell: int,
    rho: int,
    assignments: tuple[int, ...],
    vector: tuple[Fraction, ...],
) -> Fraction:
    kernel = tensor_kernel(ell, rho)
    if len(assignments) != len(vector):
        raise ValueError("assignment and vector lengths differ")
    return sum(
        (
            vector[left] * vector[right] * kernel[assignments[left]][assignments[right]]
            for left in range(len(vector))
            for right in range(len(vector))
            if left != right
        ),
        Fraction(),
    )


def strict_double_collision_matrix(assignments: tuple[int, ...]) -> Matrix:
    if not assignments:
        raise ValueError("at least one assignment is required")
    return tuple(
        tuple(
            Fraction(int(left != right and left_cell == right_cell))
            for right, right_cell in enumerate(assignments)
        )
        for left, left_cell in enumerate(assignments)
    )


def simple_spectrum(ell: int, rho: int) -> tuple[dict[str, object], ...]:
    validate_pair(ell, rho)
    m_ell = (ell - 1) // 2
    m_rho = (rho - 1) // 2
    a_ell = Fraction(ell + 1, 2 * ell)
    a_rho = Fraction(rho + 1, 2 * rho)
    diagonal = atomic_diagonal(ell, rho)
    rows = (
        ("mean_zero_x_mean_zero", Fraction(1) - diagonal, (m_ell - 1) * (m_rho - 1)),
        ("mean_zero_x_constant", a_rho - diagonal, m_ell - 1),
        ("constant_x_mean_zero", a_ell - diagonal, m_rho - 1),
        ("constant_x_constant", a_ell * a_rho - diagonal, 1),
    )
    return tuple(
        {
            "space": name,
            "eigenvalue": fraction_text(value),
            "multiplicity": multiplicity,
            "sign": 1 if value > 0 else -1 if value < 0 else 0,
        }
        for name, value, multiplicity in rows
    )


def simple_inertia(ell: int, rho: int) -> tuple[int, int, int]:
    positive = 0
    negative = 0
    zero = 0
    for row in simple_spectrum(ell, rho):
        multiplicity = int(row["multiplicity"])
        if row["sign"] == 1:
            positive += multiplicity
        elif row["sign"] == -1:
            negative += multiplicity
        else:
            zero += multiplicity
    return positive, negative, zero


def ambient_envelope_inertia(ell: int, rho: int) -> tuple[int, int, int]:
    """Inertia if every ambient residue preimage is retained once."""

    validate_pair(ell, rho)
    cells = ((ell - 1) // 2) * ((rho - 1) // 2)
    multiplicity = (ell - 1) * (rho - 1)
    diagonal = atomic_diagonal(ell, rho)
    cell_eigenvalues = (
        Fraction(1),
        Fraction(ell + 1, 2 * ell),
        Fraction(rho + 1, 2 * rho),
        Fraction(ell + 1, 2 * ell) * Fraction(rho + 1, 2 * rho),
    )
    if any(multiplicity * value <= diagonal for value in cell_eigenvalues):
        raise ArithmeticError("ambient cell-sum quotient is not positive")
    return cells, (multiplicity - 1) * cells, 0


def singular_rectangle_control() -> dict[str, object]:
    """The nontrivial incomplete-occupancy kernel at (ell,rho)=(5,11)."""

    ell, rho = 5, 11
    assignments = (0, 1, 2, 5, 6, 7)
    matrix = occupancy_wick_matrix(ell, rho, assignments)
    null_vector = tuple(Fraction(value) for value in (-1, -1, -1, 1, 1, 1))
    if matrix_rank(matrix) != 5:
        raise ArithmeticError("(5,11) rectangle did not have rank five")
    image = matrix_multiply(matrix, tuple((entry,) for entry in null_vector))
    if any(entry for row in image for entry in row):
        raise ArithmeticError("(5,11) rectangle null vector changed")
    scaled = scalar_matrix(Fraction(55), matrix)
    return {
        "ell": ell,
        "rho": rho,
        "occupied_cell_indices": list(assignments),
        "rank": matrix_rank(matrix),
        "null_vector": [fraction_text(entry) for entry in null_vector],
        "scaled_by": 55,
        "scaled_matrix": [[fraction_text(entry) for entry in row] for row in scaled],
    }


def verify_spectrum(ell: int, rho: int) -> None:
    matrix = simple_complete_cell_wick_matrix(ell, rho)
    expected_dimension = ((ell - 1) // 2) * ((rho - 1) // 2)
    if len(matrix) > MAX_SIMPLE_MATRIX_DIMENSION:
        raise RuntimeError("simple-matrix cap exceeded")
    if matrix_rank(matrix) != expected_dimension:
        raise ArithmeticError("simple complete-cell Wick matrix lost full rank")
    positive, negative, zero = simple_inertia(ell, rho)
    if positive + negative + zero != expected_dimension:
        raise ArithmeticError("simple spectrum multiplicities do not sum")
    if positive == 0 or negative == 0 or zero != 0:
        raise ArithmeticError(
            "simple complete-cell spectrum is not full-rank indefinite"
        )


def build_pair_panel(ell: int, rho: int, held_out: bool) -> dict[str, object]:
    validate_pair(ell, rho)
    cells = allowed_cells(ell, rho)
    counts = residue_envelope_counts(ell, rho)
    expected_fibre = (ell - 1) * (rho - 1)
    if set(counts) != set(cells):
        raise ArithmeticError("ambient residue map missed an allowed cell")
    if set(counts.values()) != {expected_fibre}:
        raise ArithmeticError("ambient residue-map fibres are not uniform")
    verify_spectrum(ell, rho)

    dimension = len(cells)
    simple_assignments = tuple(range(dimension))
    singleton = occupancy_wick_matrix(ell, rho, (0,))
    duplicate = occupancy_wick_matrix(ell, rho, (0, 0))
    contrast = (Fraction(1), Fraction(-1))
    if singleton != ((Fraction(0),),):
        raise ArithmeticError("literal singleton did not Wick-cancel")
    if aggregate_vector(dimension, (0, 0), contrast) != tuple(
        Fraction() for _ in range(dimension)
    ):
        raise ArithmeticError("duplicate-cell contrast did not push forward to zero")
    contrast_value = quadratic_form(duplicate, contrast)
    if contrast_value != -2 * atomic_diagonal(ell, rho):
        raise ArithmeticError("residue-forgetting counterfeit changed")
    if matrix_rank(strict_double_collision_matrix(simple_assignments)) != 0:
        raise ArithmeticError("strict-collision counterfeit should vanish")

    full_envelope_inertia = ambient_envelope_inertia(ell, rho)
    return {
        "ell": ell,
        "rho": rho,
        "held_out": held_out,
        "fixed_owner_class_cell_count": dimension,
        "ambient_residue_envelope_points": sum(counts.values()),
        "uniform_envelope_preimages_per_cell": expected_fibre,
        "centered_tensor_atomic_diagonal": fraction_text(atomic_diagonal(ell, rho)),
        "simple_complete_cell_spectrum": list(simple_spectrum(ell, rho)),
        "simple_complete_cell_rank": matrix_rank(
            simple_complete_cell_wick_matrix(ell, rho)
        ),
        "simple_complete_cell_inertia": {
            "positive": simple_inertia(ell, rho)[0],
            "negative": simple_inertia(ell, rho)[1],
            "zero": simple_inertia(ell, rho)[2],
        },
        "literal_singleton_rank": matrix_rank(singleton),
        "strict_collision_only_simple_rank": matrix_rank(
            strict_double_collision_matrix(simple_assignments)
        ),
        "same_cell_contrast_pushforward": [
            fraction_text(entry)
            for entry in aggregate_vector(dimension, (0, 0), contrast)
        ],
        "same_cell_contrast_wick_value": fraction_text(contrast_value),
        "full_ambient_envelope_inertia": {
            "positive": full_envelope_inertia[0],
            "negative": full_envelope_inertia[1],
            "zero": full_envelope_inertia[2],
        },
    }


def check_source_blobs() -> None:
    for (commit, path), expected_blob in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=4.0,
        )
        if completed.returncode:
            raise RuntimeError(
                "locked source object/path unavailable: "
                f"{commit}:{path}; fetch without merging via "
                f"git fetch --no-tags origin {commit}"
            )
        if completed.stdout.strip() != expected_blob:
            raise RuntimeError(f"source blob mismatch: {commit}:{path}")


def check_source_lock_manifest() -> None:
    manifest = json.loads(SOURCE_LOCK_PATH.read_text(encoding="utf-8"))
    observed = {
        (entry["commit"], entry["path"]): entry["git_blob"]
        for entry in manifest["sources"]
    }
    if observed != SOURCE_BLOBS:
        raise RuntimeError("source-lock manifest does not match producer constants")
    if manifest["predecessor_commit"] != ("b8cf095e7446583af80cbe4ff5d04257b6901d97"):
        raise RuntimeError("Wave-2 predecessor commit changed")


def build_report() -> dict[str, object]:
    panels = [build_pair_panel(ell, rho, held_out=False) for ell, rho in CONTROL_PAIRS]
    panels.append(build_pair_panel(*HELD_OUT_PAIR, held_out=True))
    return {
        "schema": (
            "riemann.function_field.ffps_shared_fibre_wick_occupancy_spectrum.v1"
        ),
        "status": "EXACT_FIXED_FIBRE_IDENTITY_AND_RESIDUE_FORGETTING_NO_GO",
        "arithmetic_class": "MIXED",
        "arithmetic_components": {
            "matrix_spectrum_and_quadratic_forms": "EXACT_RATIONAL",
            "complete_residue_envelope_counts": "CERTIFIED_INTEGER_COVERAGE",
        },
        "theorem_ledger": {
            "MPD-W2.1": "SHARED_FIBRE_OWNER_COFACTOR_RESIDUE_MAP_PROVED",
            "MPD-W2.2": "EXACT_ARBITRARY_OCCUPANCY_PULLBACK_IDENTITY_PROVED",
            "MPD-W2.3": "SIMPLE_COMPLETE_CELL_SPECTRUM_PROVED_ALL_DISTINCT_ODD_PRIMES",
            "MPD-W2.4": "RESIDUE_ONLY_FORGETTING_REFUTED",
            "MPD-W2.5": "LIVE_OCCUPANCY_AND_GLOBAL_SIGNED_RECOMBINATION_OPEN",
        },
        "ontology": {
            "fibre": "iota=(g,ell,rho,sigma,tau)",
            "pair_space": "(Omega x_I Omega) minus the literal relative diagonal",
            "independent_atom_coordinates": (
                "(Q mod ell,v mod ell,P mod rho,u mod rho) and primed copies"
            ),
            "shared_coordinates": "ell,rho,sigma,tau",
            "physical_map": (
                "x=-rho^2*(Q mod ell)*(v mod ell)^2 mod ell; "
                "y=ell^2*(P mod rho)*(u mod rho)^2 mod rho"
            ),
            "exact_scalar_sufficient_statistic": (
                "(physical aggregate Rz, literal diagonal energy sum |z_omega|^2)"
            ),
            "rejected": "independent marked-place pairs Z0 x Z1",
        },
        "finite_controls": panels,
        "incomplete_occupancy_countercontrol": singular_rectangle_control(),
        "not_proved": [
            "surjectivity or multiplicity of the complete live source on residue cells",
            "noncancellation in any complete native conductor fibre",
            "ONEPLACEWEIL for complete literal source amplitudes",
            "RELPARTFROB for the complete relative class",
            "WCADD106140 or WCCORR106191",
            "WCKUM106140",
            "ONEPLACETRACE or RELTRACE",
            "principal binding to the frozen consumer",
            "RH or GRH",
        ],
        "resource_ledger": {
            "control_pairs": len(CONTROL_PAIRS),
            "held_out_pairs": 1,
            "maximum_simple_matrix_dimension": max(
                panel["fixed_owner_class_cell_count"] for panel in panels
            ),
            "maximum_ambient_envelope_points": max(
                panel["ambient_residue_envelope_points"] for panel in panels
            ),
            "nontrivial_incomplete_occupancy_atoms": 6,
            "source_blobs_authenticated": len(SOURCE_BLOBS),
            "floating_point_operations": 0,
            "live_source_atoms_enumerated": 0,
            "conductor_families_estimated": 0,
        },
    }


def rendered_report() -> str:
    return json.dumps(build_report(), indent=2, sort_keys=True) + "\n"


def check_note_contract() -> None:
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "MPD-W2.2 — exact arbitrary-occupancy pullback",
        "shared marked fibre",
        "not an independent marked-place product",
        "literal diagonal energy",
        "residue-only forgetting no-go",
        "live occupancy remains open",
        "ONEPLACEWEIL",
        "RELTRACE",
        "principal binding",
        "RH and GRH remain unproved",
    ):
        if marker not in note:
            raise RuntimeError(f"note contract marker missing: {marker}")


def check_no_assert_statements() -> None:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    if any(isinstance(node, ast.Assert) for node in ast.walk(tree)):
        raise RuntimeError("producer must not use optimization-sensitive assert")


def run_checks() -> dict[str, object]:
    check_source_blobs()
    check_source_lock_manifest()
    check_note_contract()
    check_no_assert_statements()
    report = build_report()
    if FIXTURE_PATH.read_text(encoding="utf-8") != rendered_report():
        raise RuntimeError("canonical JSON fixture is stale")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = run_checks() if args.check else build_report()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
