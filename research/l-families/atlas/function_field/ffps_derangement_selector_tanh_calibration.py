#!/usr/bin/env python3
"""Exact descent-parity calibration for the derangement-selector dual."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from collections import Counter
from fractions import Fraction
from functools import cache
from itertools import pairwise
from pathlib import Path

Partition = tuple[int, ...]
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MIN_DEGREE = 2
MAX_DEGREE = 10

FINITE_OPTIMUM_COMMIT = "6d9e66033c1a00066935cceed9ca66b76b67fd99"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_DERANGEMENT_SELECTOR_FINITE_L1_OPTIMIZATION.md"
    ): "602742ff6bafa9a9cbb4f563129feaad74e0184d",
    (
        "research/l-families/atlas/function_field/"
        "ffps_derangement_selector_finite_l1_optimization.py"
    ): "bf46f94efecb76eca788d6597eac8a2995dba00f",
    (
        "research/l-families/atlas/function_field/"
        "ffps_derangement_selector_finite_l1_optimization.json"
    ): "4c3bb43266e10d0e99d259f093664992f38130c5",
    "tests/test_ffps_derangement_selector_finite_l1_optimization.py": (
        "125a3e4dccb66070eb791f083944094106cfb952"
    ),
}


def check_source_blobs() -> None:
    """Authenticate the exact finite optimization packet used as context."""

    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{FINITE_OPTIMUM_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(
                f"frozen source blob mismatch: {FINITE_OPTIMUM_COMMIT}:{path}"
            )


def validate_degree(degree: int, *, allow_zero: bool = False) -> None:
    lower = 0 if allow_zero else MIN_DEGREE
    if (
        isinstance(degree, bool)
        or not isinstance(degree, int)
        or not lower <= degree <= MAX_DEGREE
    ):
        raise ValueError(f"degree must lie in [{lower},{MAX_DEGREE}]")


@cache
def partitions(total: int, largest: int | None = None) -> tuple[Partition, ...]:
    """Return partitions in reverse lexicographic order."""

    validate_degree(total, allow_zero=True)
    if total == 0:
        return ((),)
    upper = total if largest is None else min(total, largest)
    return tuple(
        (first, *tail)
        for first in range(upper, 0, -1)
        for tail in partitions(total - first, first)
    )


def dimension(partition: Partition) -> int:
    """Hook-length dimension of the irreducible indexed by partition."""

    degree = sum(partition)
    denominator = 1
    for row, row_length in enumerate(partition):
        for column in range(row_length):
            denominator *= (
                row_length
                - column
                + sum(lower_length > column for lower_length in partition[row + 1 :])
            )
    return math.factorial(degree) // denominator


def is_hook(partition: Partition) -> bool:
    return bool(partition) and all(row_length == 1 for row_length in partition[1:])


@cache
def tableau_row_words(partition: Partition) -> tuple[tuple[int, ...], ...]:
    """Rows occupied by 1,...,d across all standard tableaux of a shape."""

    if not partition:
        return ((),)
    words: list[tuple[int, ...]] = []
    for row, row_length in enumerate(partition):
        if row + 1 < len(partition) and partition[row + 1] == row_length:
            continue
        predecessor = list(partition)
        predecessor[row] -= 1
        if predecessor[row] == 0:
            predecessor.pop(row)
        words.extend(word + (row,) for word in tableau_row_words(tuple(predecessor)))
    return tuple(words)


def descent_count(row_word: tuple[int, ...]) -> int:
    return sum(next_row > row for row, next_row in pairwise(row_word))


def descent_parity_coefficient(partition: Partition) -> int:
    return sum((-1) ** descent_count(word) for word in tableau_row_words(partition))


def cells(partition: Partition) -> frozenset[tuple[int, int]]:
    return frozenset(
        (row, column)
        for row, row_length in enumerate(partition)
        for column in range(row_length)
    )


@cache
def rim_hook_removals(
    partition: Partition, size: int
) -> tuple[tuple[Partition, int], ...]:
    """Enumerate border-strip removals as (remaining shape, height)."""

    remaining_size = sum(partition) - size
    if size < 1 or remaining_size < 0:
        return ()
    diagram = cells(partition)
    removals: list[tuple[Partition, int]] = []
    for remainder in partitions(remaining_size):
        if len(remainder) > len(partition) or any(
            remainder[row] > partition[row] for row in range(len(remainder))
        ):
            continue
        strip = diagram - cells(remainder)
        if len(strip) != size:
            continue
        seen: set[tuple[int, int]] = set()
        stack = [next(iter(strip))]
        while stack:
            cell = stack.pop()
            if cell in seen:
                continue
            seen.add(cell)
            row, column = cell
            for neighbor in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ):
                if neighbor in strip and neighbor not in seen:
                    stack.append(neighbor)
        if seen != strip:
            continue
        if any(
            (row + 1, column) in strip
            and (row, column + 1) in strip
            and (row + 1, column + 1) in strip
            for row, column in strip
        ):
            continue
        removals.append((remainder, len({row for row, _ in strip}) - 1))
    return tuple(removals)


@cache
def character(partition: Partition, cycle_type: Partition) -> int:
    """Murnaghan--Nakayama character value."""

    if sum(partition) != sum(cycle_type):
        raise ValueError("partition and cycle type must have the same size")
    if not cycle_type:
        return int(not partition)
    size = cycle_type[0]
    return sum(
        (-1) ** height * character(remainder, cycle_type[1:])
        for remainder, height in rim_hook_removals(partition, size)
    )


def centralizer_size(cycle_type: Partition) -> int:
    result = 1
    for cycle_length, multiplicity in Counter(cycle_type).items():
        result *= cycle_length**multiplicity * math.factorial(multiplicity)
    return result


@cache
def tanh_coefficient(power: int) -> Fraction:
    """Coefficient of x**power in tanh(x), from tanh'=1-tanh^2."""

    if power < 1:
        return Fraction(0)
    if power == 1:
        return Fraction(1)
    quadratic_coefficient = sum(
        (
            tanh_coefficient(left) * tanh_coefficient(power - 1 - left)
            for left in range(1, power - 1)
        ),
        start=Fraction(0),
    )
    return -quadratic_coefficient / power


def predicted_class_transform(degree: int, cycle_count: int) -> Fraction:
    """z_mu*[p_mu]tanh(A), depending only on length(mu)."""

    validate_degree(degree)
    if not 1 <= cycle_count <= degree:
        raise ValueError("cycle_count must lie between one and degree")
    return (
        tanh_coefficient(cycle_count)
        * math.factorial(cycle_count)
        * 2 ** (degree - cycle_count)
    )


def matrix_rank(rows: list[list[int]]) -> int:
    """Exact rational rank of a small integer matrix."""

    if not rows:
        return 0
    matrix = [[Fraction(entry) for entry in row] for row in rows]
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        pivot_value = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / pivot_value for entry in matrix[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(
                    matrix[row], matrix[pivot_row], strict=True
                )
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def verify_degree(degree: int) -> dict[str, object]:
    validate_degree(degree)
    shapes = partitions(degree)
    coefficients = {
        partition: descent_parity_coefficient(partition) for partition in shapes
    }
    tableau_count = 0
    nonhook_ratios: list[Fraction] = []
    for partition, coefficient in coefficients.items():
        irreducible_dimension = dimension(partition)
        words = tableau_row_words(partition)
        tableau_count += len(words)
        if len(words) != irreducible_dimension:
            raise AssertionError("tableau count and hook-length dimension disagree")
        if abs(coefficient) > irreducible_dimension:
            raise AssertionError("descent-parity coefficient escaped its dimension")
        if is_hook(partition):
            depth = degree - partition[0]
            if coefficient != (-1) ** depth * irreducible_dimension:
                raise AssertionError("hook saturation failed")
        else:
            if abs(coefficient) >= irreducible_dimension:
                raise AssertionError("nonhook descent-parity capacity is not strict")
            nonhook_ratios.append(Fraction(abs(coefficient), irreducible_dimension))

    transforms: dict[Partition, Fraction] = {}
    for cycle_type in shapes:
        transform = sum(
            coefficients[partition] * character(partition, cycle_type)
            for partition in shapes
        )
        expected = predicted_class_transform(degree, len(cycle_type))
        if transform != expected:
            raise AssertionError("cycle-count transform formula failed")
        transforms[cycle_type] = transform

    cycle = (degree,)
    if transforms[cycle] != 2 ** (degree - 1):
        raise AssertionError("full-cycle transform changed")
    residual_types = [
        cycle_type
        for cycle_type, value in transforms.items()
        if 1 not in cycle_type and cycle_type != cycle and value
    ]
    nonhooks = [partition for partition in shapes if not is_hook(partition)]
    noncycle_derangements = [
        cycle_type
        for cycle_type in shapes
        if 1 not in cycle_type and cycle_type != cycle
    ]
    zero_hook_projection_rank = matrix_rank(
        [
            [character(partition, cycle_type) for partition in nonhooks]
            for cycle_type in noncycle_derangements
        ]
    )
    if zero_hook_projection_rank != len(noncycle_derangements):
        raise AssertionError("zero-hook derangement projection lost surjectivity")
    transform_by_cycle_count = {
        str(cycle_count): str(predicted_class_transform(degree, cycle_count))
        for cycle_count in range(1, degree + 1)
        if predicted_class_transform(degree, cycle_count)
    }
    return {
        "degree": degree,
        "partitions": len(shapes),
        "standard_tableaux": tableau_count,
        "hook_shapes": sum(is_hook(partition) for partition in shapes),
        "cycle_dual_mass": str(Fraction(transforms[cycle], degree)),
        "transform_by_cycle_count": transform_by_cycle_count,
        "forbidden_derangement_residual_types": [
            list(cycle_type) for cycle_type in residual_types
        ],
        "noncycle_derangement_coordinates": len(noncycle_derangements),
        "zero_hook_projection_rank": zero_hook_projection_rank,
        "maximum_nonhook_absolute_ratio": str(max(nonhook_ratios, default=Fraction(0))),
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    panels = [verify_degree(degree) for degree in range(MIN_DEGREE, MAX_DEGREE + 1)]
    return {
        "schema": "riemann.function_field.ffps_selector_tanh_calibration.v1",
        "status": (
            "exact all-degree symbolic identity with bounded finite replay; "
            "the contractive correction and all-degree selector optimum remain open"
        ),
        "frozen_source": {
            "commit": FINITE_OPTIMUM_COMMIT,
            "blobs": SOURCE_BLOBS,
        },
        "theorem": {
            "coefficient": ("b_(d,lambda)=sum_(T in SYT(lambda)) (-1)^des(T)"),
            "frobenius_series": (
                "sum_(d>=1,lambda|-d) b_(d,lambda)s_lambda t^d="
                "tanh(sum_(r>=1) 2^(r-1)p_r t^r/r)"
            ),
            "hook_saturation": ("b_(d,(d-k,1^k))=(-1)^k*binom(d-1,k)"),
            "class_transform": (
                "sum_lambda b_(d,lambda)chi_lambda(mu)="
                "[x^ell]tanh(x)*ell!*2^(d-ell), ell=length(mu)"
            ),
            "full_cycle_dual_mass": "2^(d-1)/d",
            "even_cycle_global_firewall": (
                "the exact cycle indicator is the unique weighted-L1 minimizer "
                "against arbitrary real or complex perturbations supported on "
                "derangement types with an even number of cycles"
            ),
            "escape_requirement": (
                "any cheaper selector must use an odd cycle-count stratum ell>=3"
            ),
            "quantifier": "every integer d>=1 and every partition mu of d",
        },
        "reduced_frontier": {
            "projection": "pi_0 sets p_1=0",
            "algebraic_zero_hook_lift": (
                "exists for every p_d-coefficient-zero derangement polynomial"
            ),
            "needed_correction": (
                "find a Schur function R_d with zero hook coefficients, "
                "pi_0(R_d)=[t^d](A-tanh(A)), and "
                "abs(b_(d,lambda)+[s_lambda]R_d)<=dim(lambda)"
            ),
            "strict_version_for_uniqueness": (
                "require strict inequality on every nonhook"
            ),
            "proved_for_all_d": False,
        },
        "finite_replay": panels,
        "scope": {
            "characteristic": 0,
            "native_ffps_adapter_constructed": False,
            "all_degree_weighted_l1_optimum_proved": False,
            "rh_proved": False,
            "grh_proved": False,
            "novelty_claimed": False,
        },
        "resource_caps": {
            "maximum_replay_degree": MAX_DEGREE,
            "external_lp_calls": 0,
            "floating_point_steps": 0,
            "finite_field_points": 0,
            "curves_or_sheaves": 0,
            "l_functions_or_zeros": 0,
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
