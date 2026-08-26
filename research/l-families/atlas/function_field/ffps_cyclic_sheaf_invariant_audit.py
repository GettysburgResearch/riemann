#!/usr/bin/env python3
"""Exact bounded audit for the ternary FFPS selected-mode Kummer system.

The calculation is deliberately tiny.  It works in the cyclotomic ring
Q[zeta_3] and in the exponent lattice F_3^2.  It neither enumerates finite
fields nor constructs a varying-conductor sheaf.  Its purpose is to certify
the coefficient rigidity and connected-subtorus invariant tests used in
FFPS_CYCLIC_SHEAF_INVARIANT_AUDIT.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_PATH = HERE / "ffps_cyclic_sheaf_invariant_audit.json"

SCHEMA = "riemann.function_field.ffps_cyclic_sheaf_invariant_audit.v1"
MAX_EXACT_OPERATIONS = 2_000
MAX_OUTPUT_BYTES = 32_768
MAX_WALL_SECONDS = 3.0


@dataclass
class Guard:
    operations: int = 0

    def use(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increment must be nonnegative")
        if self.operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.operations += amount


# Store a+b*zeta, with zeta^2+zeta+1=0.
Cyclo = tuple[int, int]
ROOTS: tuple[Cyclo, ...] = ((1, 0), (0, 1), (-1, -1))


def add(left: Cyclo, right: Cyclo, guard: Guard) -> Cyclo:
    guard.use()
    return left[0] + right[0], left[1] + right[1]


def norm(value: Cyclo, guard: Guard) -> int:
    guard.use()
    a, b = value
    return a * a - a * b + b * b


def root_power(exponent: int, guard: Guard) -> Cyclo:
    guard.use()
    return ROOTS[exponent % 3]


def mask_fourier_rows(guard: Guard) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for retained in combinations(range(3), 2):
        norms: dict[str, str] = {}
        for mode in (1, 2):
            total = (0, 0)
            for exponent in retained:
                total = add(total, root_power(-mode * exponent, guard), guard)
            squared_norm = Fraction(norm(total, guard), 4)
            norms[str(mode)] = str(squared_norm)
        rows.append(
            {
                "retained_exponents": list(retained),
                "mode_squared_norms": norms,
            }
        )
    if any(row["mode_squared_norms"] != {"1": "1/4", "2": "1/4"} for row in rows):
        raise ArithmeticError("ternary two-point mask Fourier rigidity failed")
    return rows


def rank_mod3(rows: list[list[int]], guard: Guard) -> int:
    matrix = [
        [entry % 3 for entry in row] for row in rows if any(entry % 3 for entry in row)
    ]
    if not matrix:
        return 0
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("ragged exponent matrix")
    rank = 0
    for column in range(width):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]), None
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = 1 if matrix[rank][column] == 1 else 2
        matrix[rank] = [(inverse * entry) % 3 for entry in matrix[rank]]
        guard.use(width)
        for index in range(len(matrix)):
            if index == rank:
                continue
            factor = matrix[index][column]
            if factor:
                matrix[index] = [
                    (entry - factor * pivot_entry) % 3
                    for entry, pivot_entry in zip(
                        matrix[index], matrix[rank], strict=True
                    )
                ]
                guard.use(width)
        rank += 1
        if rank == len(matrix):
            break
    return rank


def in_row_span(vector: list[int], relations: list[list[int]], guard: Guard) -> bool:
    before = rank_mod3(relations, guard)
    after = rank_mod3([*relations, vector], guard)
    return before == after


def invariant_rows(guard: Guard) -> list[dict[str, object]]:
    alignments = {
        "product": [1, 1],
        "quotient": [1, -1],
    }
    rows: list[dict[str, object]] = []
    for alignment, exponent in alignments.items():
        opposite = alignments["quotient" if alignment == "product" else "product"]
        strata = {
            "generic_pair_torus": [],
            "x_collision_only": [[1, 0]],
            "y_collision_only": [[0, 1]],
            "aligned_compensating_resonance": [exponent],
            "opposite_compensating_resonance": [opposite],
            "double_physical_collision": [[1, 0], [0, 1]],
            "atomic_diagonal_physical_image": [[1, 0], [0, 1]],
        }
        for stratum, relations in strata.items():
            mode_results = {
                str(mode): in_row_span(
                    [(mode * coordinate) % 3 for coordinate in exponent],
                    relations,
                    guard,
                )
                for mode in (1, 2)
            }
            if len(set(mode_results.values())) != 1:
                raise ArithmeticError(
                    "the two faithful cubic modes disagree on invariants"
                )
            invariant_rank = 2 if mode_results["1"] else 0
            rows.append(
                {
                    "alignment": alignment,
                    "mode_exponent_mod_3": [coordinate % 3 for coordinate in exponent],
                    "stratum": stratum,
                    "relation_rows_mod_3": [
                        [coordinate % 3 for coordinate in relation]
                        for relation in relations
                    ],
                    "mode_geometrically_trivial": mode_results,
                    "selected_rank_two_invariant_multiplicity": invariant_rank,
                }
            )
    expected = {
        "generic_pair_torus": 0,
        "x_collision_only": 0,
        "y_collision_only": 0,
        "aligned_compensating_resonance": 2,
        "opposite_compensating_resonance": 0,
        "double_physical_collision": 2,
        "atomic_diagonal_physical_image": 2,
    }
    for row in rows:
        if row["selected_rank_two_invariant_multiplicity"] != expected[row["stratum"]]:
            raise ArithmeticError("connected-subtorus invariant classification failed")
    return rows


def common_base_panel(guard: Guard) -> dict[str, object]:
    field_size = 7
    local_dimension = (field_size - 1) // 2
    coordinate_count = local_dimension**2
    constant_denominator = (local_dimension + 1) ** 2
    full_denominator = field_size**2
    density = Fraction(2, 3)
    guard.use(12)
    hard = 1 / (
        Fraction(constant_denominator, coordinate_count) * density**2
        + Fraction(full_denominator, coordinate_count) * density * (1 - density)
    )
    full = Fraction(coordinate_count, constant_denominator)
    soft = full + Fraction(coordinate_count, full_denominator) * (1 - density) / density
    wick_residual = hard * (field_size - 1) ** 2 - Fraction(3, 2) ** 2
    if not (hard < full < soft):
        raise ArithmeticError("same-characteristic ternary hard/soft ordering failed")
    if wick_residual <= 0:
        raise ArithmeticError("same-characteristic Wick residual should be positive")
    return {
        "base_field": "F_7",
        "closed_places": "two distinct degree-one places",
        "local_physical_dimensions": [local_dimension, local_dimension],
        "hard_leverage": str(hard),
        "complete_leverage": str(full),
        "soft_complete_metric_leverage": str(soft),
        "wick_atomic_residual": str(wick_residual),
        "ordering": "L_hard < L_full < L_soft",
    }


def canonical_bytes(payload: dict[str, object]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def build_payload() -> dict[str, object]:
    started = time.monotonic()
    guard = Guard()
    masks = mask_fourier_rows(guard)
    invariants = invariant_rows(guard)
    common_panel = common_base_panel(guard)
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return {
        "schema": SCHEMA,
        "scope": {
            "proved": (
                "exact ternary Fourier coefficients and F_3 exponent-lattice invariant tests "
                "for connected monomial subtori"
            ),
            "not_constructed": (
                "the universal varying-closed-place source complex, its Betti bounds, or CYSEL"
            ),
            "enumeration": {
                "finite_fields": False,
                "closed_places": False,
                "conductors": False,
                "curves": False,
                "l_functions": False,
                "zeros": False,
            },
        },
        "ternary_mask_fourier": {
            "k": 3,
            "retained_size": 2,
            "rows": masks,
            "conclusion": (
                "every two-point ternary hard mask has |gamma_1|^2=|gamma_2|^2=1/4; "
                "rotation cannot tune the selected rank-two Kummer system"
            ),
        },
        "same_characteristic_control": common_panel,
        "invariant_test": {
            "ratio_coordinates": ["R_X=X_1/X_2", "R_Y=Y_1/Y_2"],
            "general_criterion": (
                "on a geometrically integral stratum Z, the selected mode is geometrically "
                "constant iff R_X*R_Y^epsilon is a cube in the function field of Z"
            ),
            "connected_monomial_subtorus_rows": invariants,
            "conclusion": (
                "the generic pair torus has no invariant, but the aligned compensating "
                "resonance and double physical collision each have invariant multiplicity two"
            ),
        },
        "fixed_fibre_complexity": {
            "selected_modes": 2,
            "selected_rank": 2,
            "mode_rank": 1,
            "orientation_cover_degree_on_two_physical_atoms": 16,
            "physical_pair_torus_dimension": 4,
            "ratio_torus_dimension": 2,
            "physical_pair_coordinate_boundary_divisors": 8,
            "ramification": "tame Kummer; Swan conductor zero on the fixed torus",
            "warning": (
                "these fixed-fibre constants do not bound the ranks or Betti numbers introduced "
                "by irreducibility, Boolean incidence, degree shells, or varying closed places"
            ),
        },
        "resource_ledger": {
            "exact_operations": guard.operations,
            "max_exact_operations": MAX_EXACT_OPERATIONS,
            "max_output_bytes": MAX_OUTPUT_BYTES,
            "max_wall_seconds": MAX_WALL_SECONDS,
        },
    }


def envelope(payload: dict[str, object]) -> dict[str, object]:
    digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
    return {"payload_sha256": digest, "payload": payload}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    result = envelope(build_payload())
    encoded = canonical_bytes(result)
    if len(encoded) > MAX_OUTPUT_BYTES:
        raise RuntimeError("output-byte cap exceeded")
    if args.check:
        if not OUTPUT_PATH.exists():
            raise SystemExit("canonical fixture is missing")
        if OUTPUT_PATH.read_bytes() != encoded:
            raise SystemExit("canonical fixture drifted")
        return
    OUTPUT_PATH.write_bytes(encoded)


if __name__ == "__main__":
    main()
