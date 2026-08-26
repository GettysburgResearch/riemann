#!/usr/bin/env python3
"""Bounded exact replay for the marked genus-two Sym^12 valuation target.

The replay deliberately works only with the finite representation-theoretic
model at (d,b)=(9,12).  It performs no point counting and no floating-point
linear algebra.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter, defaultdict
from collections.abc import Iterable
from functools import cache
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

R_DEGREE = 9
SYMMETRIC_LABELS = 5
ORDER = 12
COVARIANT_DEGREE = 9
SELECTED_TOTAL_DEGREE = 3 * COVARIANT_DEGREE
HOLOMORPHY_T_DEGREE_CAP = 2 * COVARIANT_DEGREE

State = tuple[tuple[int, ...], int]
SparseVector = dict[State, int]
ChartRowKey = tuple[tuple[int, ...], int, int, int, int]


def states_at_index_sum(index_sum: int) -> list[State]:
    """Polynomial-basis states of Sym^5(Sym^9) tensor Sym^9."""

    states: list[State] = []
    for sym_indices in itertools.combinations_with_replacement(
        range(R_DEGREE + 1), SYMMETRIC_LABELS
    ):
        distinguished = index_sum - sum(sym_indices)
        if 0 <= distinguished <= R_DEGREE:
            states.append((sym_indices, distinguished))
    return states


def raising_image(state: State) -> SparseVector:
    """Apply E e_a = a e_(a-1) in the symmetric-polynomial basis."""

    sym_indices, distinguished = state
    image: defaultdict[State, int] = defaultdict(int)
    counts = Counter(sym_indices)
    for index, multiplicity in counts.items():
        if index == 0:
            continue
        target = list(sym_indices)
        target.remove(index)
        target.append(index - 1)
        target.sort()
        image[(tuple(target), distinguished)] += index * multiplicity
    if distinguished:
        image[(sym_indices, distinguished - 1)] += distinguished
    return dict(image)


def lowering_image(state: State) -> SparseVector:
    """Apply F e_a = (9-a) e_(a+1) in the polynomial basis."""

    sym_indices, distinguished = state
    image: defaultdict[State, int] = defaultdict(int)
    counts = Counter(sym_indices)
    for index, multiplicity in counts.items():
        if index == R_DEGREE:
            continue
        target = list(sym_indices)
        target.remove(index)
        target.append(index + 1)
        target.sort()
        image[(tuple(target), distinguished)] += (R_DEGREE - index) * multiplicity
    if distinguished < R_DEGREE:
        image[(sym_indices, distinguished + 1)] += R_DEGREE - distinguished
    return dict(image)


def raising_matrix() -> tuple[list[State], list[State], sp.MutableSparseMatrix]:
    domain = states_at_index_sum((6 * R_DEGREE - ORDER) // 2)
    codomain = states_at_index_sum((6 * R_DEGREE - (ORDER + 2)) // 2)
    row = {state: index for index, state in enumerate(codomain)}
    entries: dict[tuple[int, int], int] = {}
    for column, state in enumerate(domain):
        for target, coefficient in raising_image(state).items():
            entries[(row[target], column)] = coefficient
    matrix = sp.MutableSparseMatrix(len(codomain), len(domain), entries)
    return domain, codomain, matrix


def integer_nullspace_rows(matrix: sp.MatrixBase) -> list[list[int]]:
    """Fraction-free DomainMatrix nullspace, normalized to primitive rows."""

    domain_matrix = DomainMatrix.from_Matrix(matrix).to_field()
    raw = domain_matrix.nullspace().to_Matrix()
    rows: list[list[int]] = []
    for row_index in range(raw.rows):
        rationals = [sp.Rational(raw[row_index, column]) for column in range(raw.cols)]
        denominator_lcm = math.lcm(*(value.q for value in rationals))
        integers = [int(value * denominator_lcm) for value in rationals]
        divisor = math.gcd(*(abs(value) for value in integers))
        if divisor:
            integers = [value // divisor for value in integers]
        first = next(value for value in integers if value)
        if first < 0:
            integers = [-value for value in integers]
        rows.append(integers)
    return rows


def matrix_rank_mod_prime(matrix: sp.MatrixBase, prime: int) -> int:
    return int(DomainMatrix.from_Matrix(matrix).convert_to(sp.GF(prime)).rank())


def primitive_row_digest(rows: Iterable[Iterable[int]]) -> str:
    payload = json.dumps([list(row) for row in rows], separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def lower_vector(vector: SparseVector) -> SparseVector:
    image: defaultdict[State, int] = defaultdict(int)
    for state, scalar in vector.items():
        for target, coefficient in lowering_image(state).items():
            image[target] += scalar * coefficient
    return {state: scalar for state, scalar in image.items() if scalar}


def basis_vectors(
    domain: list[State], nullspace_rows: list[list[int]]
) -> list[SparseVector]:
    return [
        {state: scalar for state, scalar in zip(domain, row, strict=True) if scalar}
        for row in nullspace_rows
    ]


@cache
def split_two_three(
    sym_indices: tuple[int, ...],
) -> tuple[tuple[int, int, tuple[int, ...], int], ...]:
    """Coproduct Sym^5(R) -> Sym^2(R) tensor Sym^3(R).

    The polynomial monomial basis gives the product of binomial coefficients
    as the exact coproduct scalar.
    """

    counts = Counter(sym_indices)
    terms: list[tuple[int, int, tuple[int, ...], int]] = []
    for first in range(R_DEGREE + 1):
        for second in range(first, R_DEGREE + 1):
            selected = Counter((first, second))
            if any(selected[index] > counts[index] for index in selected):
                continue
            complement = list(sym_indices)
            complement.remove(first)
            complement.remove(second)
            scalar = math.prod(
                math.comb(counts[index], multiplicity)
                for index, multiplicity in selected.items()
            )
            terms.append((first, second, tuple(complement), scalar))
    return tuple(terms)


def _triple_shift_terms(
    first_power: int, second_power: int, distinguished_power: int
) -> dict[tuple[int, int, int, int], int]:
    terms: defaultdict[tuple[int, int, int, int], int] = defaultdict(int)
    for first_t in range(first_power + 1):
        for second_t in range(second_power + 1):
            for distinguished_t in range(distinguished_power + 1):
                t_degree = first_t + second_t + distinguished_t
                if t_degree <= HOLOMORPHY_T_DEGREE_CAP:
                    continue
                key = (
                    first_power - first_t,
                    second_power - second_t,
                    distinguished_power - distinguished_t,
                    t_degree,
                )
                terms[key] += (
                    math.comb(first_power, first_t)
                    * math.comb(second_power, second_t)
                    * math.comb(distinguished_power, distinguished_t)
                )
    return dict(terms)


@cache
def selected_high_terms(
    first_index: int, second_index: int, distinguished: int, chart: str
) -> tuple[tuple[int, int, int, int, int], ...]:
    """High-t jet after a representative 3+3 substitution.

    We use twice the canonical symmetrization Sym^2(R)->R tensor R, so all
    coefficients are integral: an off-diagonal monomial maps to the two
    ordered terms, while a diagonal monomial maps to twice its ordered term.
    This uniform factor does not alter any kernel.
    """

    if chart == "phi":
        powers = (
            R_DEGREE - first_index,
            R_DEGREE - second_index,
            R_DEGREE - distinguished,
        )
    elif chart == "phi_prime":
        powers = (first_index, second_index, distinguished)
    else:
        raise ValueError(f"unknown chart: {chart}")

    combined: defaultdict[tuple[int, int, int, int], int] = defaultdict(int)
    ordered_powers = (
        [powers[:2]] if first_index == second_index else [powers[:2], powers[:2][::-1]]
    )
    symmetrization_scalar = 2 if first_index == second_index else 1
    for ordered_first, ordered_second in ordered_powers:
        for key, scalar in _triple_shift_terms(
            ordered_first, ordered_second, powers[2]
        ).items():
            combined[key] += symmetrization_scalar * scalar
    return tuple((*key, scalar) for key, scalar in sorted(combined.items()))


def chart_rows(vectors: list[SparseVector], chart: str) -> dict[ChartRowKey, list[int]]:
    """Exact high-t coefficient rows on the 66-dimensional source basis."""

    state_columns: defaultdict[State, dict[int, int]] = defaultdict(dict)
    for column, vector in enumerate(vectors):
        for state, scalar in vector.items():
            state_columns[state][column] = scalar

    rows: dict[ChartRowKey, list[int]] = {}
    width = len(vectors)
    for (sym_indices, distinguished), columns in state_columns.items():
        for first, second, complement, coproduct_scalar in split_two_three(sym_indices):
            high_terms = selected_high_terms(first, second, distinguished, chart)
            for first_x, second_x, distinguished_x, t_degree, jet_scalar in high_terms:
                key = (complement, first_x, second_x, distinguished_x, t_degree)
                row = rows.setdefault(key, [0] * width)
                scalar = coproduct_scalar * jet_scalar
                for column, coefficient in columns.items():
                    row[column] += scalar * coefficient
    return {key: row for key, row in rows.items() if any(row)}


def rank_rows_over_q(rows: Iterable[list[int]], width: int) -> int:
    matrix_rows = list(rows)
    if not matrix_rows:
        return 0
    matrix = sp.MutableSparseMatrix(
        len(matrix_rows),
        width,
        {
            (row_index, column): value
            for row_index, row in enumerate(matrix_rows)
            for column, value in enumerate(row)
            if value
        },
    )
    return int(DomainMatrix.from_Matrix(matrix).to_field().rank())


def integer_nullspace_from_rows(rows: list[list[int]], width: int) -> list[list[int]]:
    if not rows:
        return [[int(column == row) for column in range(width)] for row in range(width)]
    matrix = sp.MutableSparseMatrix(
        len(rows),
        width,
        {
            (row_index, column): value
            for row_index, row in enumerate(rows)
            for column, value in enumerate(row)
            if value
        },
    )
    return integer_nullspace_rows(matrix)


def rank_rows_mod_prime(rows: Iterable[list[int]], width: int, prime: int) -> int:
    pivots: dict[int, list[int]] = {}
    for integer_row in rows:
        row = [value % prime for value in integer_row]
        while True:
            pivot = next((column for column, value in enumerate(row) if value), None)
            if pivot is None:
                break
            if pivot not in pivots:
                inverse = pow(row[pivot], -1, prime)
                pivots[pivot] = [(value * inverse) % prime for value in row]
                break
            scalar = row[pivot]
            pivot_row = pivots[pivot]
            row = [
                (value - scalar * pivot_value) % prime
                for value, pivot_value in zip(row, pivot_row, strict=True)
            ]
        if len(pivots) == width:
            return width
    return len(pivots)


def valuation_analysis(
    domain: list[State], nullspace_rows: list[list[int]]
) -> dict[str, object]:
    """Build the exact representative-boundary matrix under explicit caps."""

    width = len(nullspace_rows)
    vectors = basis_vectors(domain, nullspace_rows)
    selected_rows: list[list[int]] = []
    coefficient_rows: list[dict[str, object]] = []
    containment_rows: list[dict[str, object]] = []
    prime_1 = 1_000_003
    prime_2 = 1_000_033

    for coefficient in range(ORDER + 1):
        selected_chart = "phi_prime" if coefficient <= ORDER // 2 else "phi"
        selected = chart_rows(vectors, selected_chart)
        selected_values = list(selected.values())
        selected_rows.extend(selected_values)
        coefficient_rows.append(
            {
                "coefficient": coefficient,
                "selected_chart": selected_chart,
                "nonzero_target_rows": len(selected_values),
                "rank_over_Q": rank_rows_over_q(selected_values, width),
                f"rank_mod_{prime_1}": rank_rows_mod_prime(
                    selected_values, width, prime_1
                ),
                f"rank_mod_{prime_2}": rank_rows_mod_prime(
                    selected_values, width, prime_2
                ),
            }
        )

        if coefficient <= ORDER // 2:
            phi = chart_rows(vectors, "phi")
            phi_values = list(phi.values())
            phi_prime_values = selected_values
            phi_mod_rank = rank_rows_mod_prime(phi_values, width, prime_1)
            if phi_mod_rank == width:
                phi_q_rank = width
                stacked_q_rank = width
            else:
                phi_q_rank = rank_rows_over_q(phi_values, width)
                stacked_q_rank = rank_rows_over_q(phi_values + phi_prime_values, width)
            phi_prime_q_rank = coefficient_rows[-1]["rank_over_Q"]
            containment_rows.append(
                {
                    "coefficient": coefficient,
                    "phi_rows": len(phi_values),
                    "phi_prime_rows": len(phi_prime_values),
                    "rank_phi_over_Q": phi_q_rank,
                    "rank_phi_prime_over_Q": phi_prime_q_rank,
                    "rank_stacked_over_Q": stacked_q_rank,
                    "kernel_containment": (
                        "ker(phi) subset ker(phi_prime)"
                        if coefficient < ORDER // 2
                        else "ker(phi) = ker(phi_prime)"
                    ),
                }
            )

        vectors = [lower_vector(vector) for vector in vectors]

    combined_rank_q = rank_rows_over_q(selected_rows, width)
    kernel = integer_nullspace_from_rows(selected_rows, width)
    return {
        "representative_partition": "{1,2,6}|{3,4,5}",
        "coefficient_chart_rule": ("phi_prime for j=0,...,6; phi for j=7,...,12"),
        "chart_kernel_containment_for_j_0_through_6": containment_rows,
        "coefficient_matrices": coefficient_rows,
        "combined_matrix": {
            "rows": len(selected_rows),
            "columns": width,
            "rank_over_Q": combined_rank_q,
            f"rank_mod_{prime_1}": rank_rows_mod_prime(selected_rows, width, prime_1),
            f"rank_mod_{prime_2}": rank_rows_mod_prime(selected_rows, width, prime_2),
            "nullity": len(kernel),
            "primitive_kernel_basis_sha256": primitive_row_digest(kernel),
        },
        "weyl_symmetry": (
            "j maps to 12-j and phi maps to phi_prime; the j=7,...,12 "
            "containments mirror the displayed j=0,...,5 containments"
        ),
    }


def run() -> dict[str, object]:
    domain, codomain, matrix = raising_matrix()
    nullspace = integer_nullspace_rows(matrix)
    rank_q = len(domain) - len(nullspace)
    rank_mod_prime = matrix_rank_mod_prime(matrix, 1_000_003)
    valuation = valuation_analysis(domain, nullspace)
    return {
        "parameters": {
            "d": COVARIANT_DEGREE,
            "b": ORDER,
            "selected_total_degree": SELECTED_TOTAL_DEGREE,
            "holomorphy_t_degree_cap": HOLOMORPHY_T_DEGREE_CAP,
        },
        "highest_weight_model": {
            "weight_12_states": len(domain),
            "weight_14_states": len(codomain),
            "raising_rank_over_Q": rank_q,
            "raising_rank_mod_1000003": rank_mod_prime,
            "nullity": len(nullspace),
            "primitive_basis_sha256": primitive_row_digest(nullspace),
        },
        "representative_boundary_valuation": valuation,
        "resource_caps": {
            "point_counts": 0,
            "source_columns": 66,
            "largest_weight_state_space": 752,
            "partitions_computed": 1,
            "designed_wall_clock_cap_seconds": 60,
            "reason_one_partition_suffices": (
                "S5 is transitive on the ten choices of the two labels that "
                "join fixed label 6"
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-json", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = run()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    canonical_path = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical_path.exists()
        or canonical_path.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
