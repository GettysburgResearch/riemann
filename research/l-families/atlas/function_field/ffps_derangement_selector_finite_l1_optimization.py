#!/usr/bin/env python3
"""Exact finite weighted-L1 optimization for derangement-supported selectors."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from collections import Counter
from fractions import Fraction
from functools import cache
from pathlib import Path

Partition = tuple[int, ...]
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MIN_DEGREE = 2
MAX_DEGREE = 10

EXACT_SELECTOR_COMMIT = "691166b8c31f9b8e3790a9687d8fce55493f6831"
BOUNDARY_GATE_COMMIT = "961603fd0a4fd33299b94c8eaafa11ce53bd3e50"
SOURCE_BLOBS = {
    EXACT_SELECTOR_COMMIT: {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_EXACT_CYCLE_SELECTOR_MASS_NO_GO.md"
        ): "d136159ea9f0fa41600e673dc2c6ef1a2ad2f10f",
        (
            "research/l-families/atlas/function_field/"
            "ffps_exact_cycle_selector_mass_no_go.py"
        ): "5058f33f18457df07340a5653a456575b4174cde",
        (
            "research/l-families/atlas/function_field/"
            "ffps_exact_cycle_selector_mass_no_go.json"
        ): "8fa0af46cd52e7ec766821d2189ac877f8548904",
        "tests/test_ffps_exact_cycle_selector_mass_no_go.py": (
            "6b2f3de0a36b2470ab33172cc8f45ec6f9e2a561"
        ),
    },
    BOUNDARY_GATE_COMMIT: {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_RELATIVE_BOUNDARY_TRACE_TOWER_GATE.md"
        ): "cc8b649848a2e7425989a553628d9c830f56f6d1",
        (
            "research/l-families/atlas/function_field/"
            "ffps_relative_boundary_trace_tower_gate.py"
        ): "64790fc7d57976ad7176f828c690d953e30e03f5",
        (
            "research/l-families/atlas/function_field/"
            "ffps_relative_boundary_trace_tower_gate.json"
        ): "6e5947a1650498d060201a1242b609e135eb40a0",
        "tests/test_ffps_relative_boundary_trace_tower_gate.py": (
            "41853e4e3bc7d814fb9a61dc72f822c1461e71dd"
        ),
    },
}


def check_source_blobs() -> None:
    """Authenticate the exact-selector and boundary-gate source packets."""

    for commit, rows in SOURCE_BLOBS.items():
        for path, expected in rows.items():
            completed = subprocess.run(
                ["git", "rev-parse", f"{commit}:{path}"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=2,
            )
            if completed.stdout.strip() != expected:
                raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


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
    """Return the partitions of total in reverse lexicographic order."""

    validate_degree(total, allow_zero=True)
    if total == 0:
        return ((),)
    upper = total if largest is None else min(total, largest)
    rows: list[Partition] = []
    for first in range(upper, 0, -1):
        for tail in partitions(total - first, first):
            rows.append((first, *tail))
    return tuple(rows)


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
        has_square = any(
            (row + 1, column) in strip
            and (row, column + 1) in strip
            and (row + 1, column + 1) in strip
            for row, column in strip
        )
        if has_square:
            continue
        height = len({row for row, _ in strip}) - 1
        removals.append((remainder, height))
    return tuple(removals)


@cache
def character(partition: Partition, cycle_type: Partition) -> int:
    """Murnaghan--Nakayama character value chi_partition(cycle_type)."""

    if sum(partition) != sum(cycle_type):
        raise ValueError("partition and cycle type must have the same size")
    if not cycle_type:
        return int(not partition)
    size = cycle_type[0]
    return sum(
        (-1) ** height * character(remainder, cycle_type[1:])
        for remainder, height in rim_hook_removals(partition, size)
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


def centralizer_size(cycle_type: Partition) -> int:
    result = 1
    for cycle_length, multiplicity in Counter(cycle_type).items():
        result *= cycle_length**multiplicity * math.factorial(multiplicity)
    return result


def is_hook(partition: Partition) -> bool:
    return bool(partition) and all(row_length == 1 for row_length in partition[1:])


def predecessors(partition: Partition) -> tuple[Partition, ...]:
    """Shapes obtained by removing one corner."""

    result: list[Partition] = []
    for row, row_length in enumerate(partition):
        if row + 1 < len(partition) and partition[row + 1] == row_length:
            continue
        reduced = list(partition)
        reduced[row] -= 1
        if reduced[row] == 0:
            reduced.pop(row)
        result.append(tuple(reduced))
    return tuple(result)


# Each dictionary is an exact class-basis dual certificate. Unlisted classes
# have coefficient zero. Every listed non-cycle class contains a fixed point.
DUAL_CERTIFICATES: dict[int, dict[Partition, Fraction]] = {
    2: {(2,): Fraction(1)},
    3: {(1, 1, 1): Fraction(-1, 3), (3,): Fraction(4, 3)},
    4: {(2, 1, 1): Fraction(-1), (4,): Fraction(2)},
    5: {
        (3, 1, 1): Fraction(-1),
        (2, 2, 1): Fraction(-5, 4),
        (1, 1, 1, 1, 1): Fraction(1, 20),
        (5,): Fraction(16, 5),
    },
    6: {
        (4, 1, 1): Fraction(-4, 3),
        (3, 2, 1): Fraction(-32, 9),
        (2, 1, 1, 1, 1): Fraction(5, 9),
        (6,): Fraction(16, 3),
    },
    7: {
        (5, 1, 1): Fraction(1, 5),
        (4, 2, 1): Fraction(-15, 2),
        (3, 3, 1): Fraction(-7, 3),
        (3, 1, 1, 1, 1): Fraction(1, 3),
        (2, 2, 1, 1, 1): Fraction(5, 4),
        (1, 1, 1, 1, 1, 1, 1): Fraction(-13, 140),
        (7,): Fraction(64, 7),
    },
    8: {
        (6, 1, 1): Fraction(1327, 186),
        (5, 2, 1): Fraction(-1881, 155),
        (5, 1, 1, 1): Fraction(-252, 155),
        (4, 3, 1): Fraction(-1503, 124),
        (4, 2, 1, 1): Fraction(1103, 248),
        (4, 1, 1, 1, 1): Fraction(-351, 248),
        (3, 3, 1, 1): Fraction(-599, 558),
        (3, 2, 2, 1): Fraction(-1103, 744),
        (3, 2, 1, 1, 1): Fraction(823, 372),
        (3, 1, 1, 1, 1, 1): Fraction(913, 2232),
        (2, 2, 2, 1, 1): Fraction(1837, 1488),
        (2, 2, 1, 1, 1, 1): Fraction(-1103, 1488),
        (2, 1, 1, 1, 1, 1, 1): Fraction(673, 7440),
        (1, 1, 1, 1, 1, 1, 1, 1): Fraction(1483, 22320),
        (8,): Fraction(16),
    },
    9: {
        (7, 1, 1): Fraction(15943, 665),
        (6, 2, 1): Fraction(-4599, 190),
        (5, 3, 1): Fraction(-84694, 4275),
        (5, 1, 1, 1, 1): Fraction(-5359, 855),
        (4, 4, 1): Fraction(-50593, 4560),
        (4, 2, 1, 1, 1): Fraction(1171, 456),
        (3, 3, 1, 1, 1): Fraction(-83, 270),
        (3, 2, 2, 1, 1): Fraction(1393, 190),
        (3, 1, 1, 1, 1, 1, 1): Fraction(29789, 25650),
        (2, 2, 2, 2, 1): Fraction(-919, 3648),
        (2, 2, 1, 1, 1, 1, 1): Fraction(-233, 480),
        (1, 1, 1, 1, 1, 1, 1, 1, 1): Fraction(-63829, 1149120),
        (9,): Fraction(256, 9),
    },
    10: {
        (8, 1, 1): Fraction(11941, 165),
        (7, 2, 1): Fraction(-46252, 1155),
        (7, 1, 1, 1): Fraction(25532, 1155),
        (6, 3, 1): Fraction(-13516, 297),
        (6, 2, 1, 1): Fraction(-2656, 165),
        (6, 1, 1, 1, 1): Fraction(-4679, 297),
        (5, 4, 1): Fraction(-30326, 825),
        (5, 3, 1, 1): Fraction(-2146, 99),
        (5, 2, 2, 1): Fraction(11761, 1650),
        (5, 2, 1, 1, 1): Fraction(-9508, 825),
        (5, 1, 1, 1, 1, 1): Fraction(-19411, 4950),
        (4, 4, 1, 1): Fraction(1189, 264),
        (4, 3, 2, 1): Fraction(-3793, 990),
        (4, 3, 1, 1, 1): Fraction(-3668, 495),
        (4, 2, 2, 1, 1): Fraction(14027, 660),
        (4, 2, 1, 1, 1, 1): Fraction(-10249, 1980),
        (4, 1, 1, 1, 1, 1, 1): Fraction(35617, 9900),
        (3, 3, 3, 1): Fraction(2650, 297),
        (3, 3, 2, 1, 1): Fraction(18989, 1485),
        (3, 3, 1, 1, 1, 1): Fraction(-2326, 1485),
        (3, 2, 2, 2, 1): Fraction(-2179, 594),
        (3, 2, 2, 1, 1, 1): Fraction(8011, 660),
        (3, 2, 1, 1, 1, 1, 1): Fraction(1643, 594),
        (3, 1, 1, 1, 1, 1, 1, 1): Fraction(6731, 5940),
        (2, 2, 2, 2, 1, 1): Fraction(-5523, 1760),
        (2, 2, 2, 1, 1, 1, 1): Fraction(-2969, 1485),
        (2, 2, 1, 1, 1, 1, 1, 1): Fraction(-5773, 13200),
        (2, 1, 1, 1, 1, 1, 1, 1, 1): Fraction(-31657, 103950),
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1): Fraction(-15971, 184800),
        (10,): Fraction(256, 5),
    },
}

EXPECTED_STRICT_SLACK = {
    4: Fraction(1),
    5: Fraction(1),
    6: Fraction(2, 3),
    7: Fraction(5, 7),
    8: Fraction(19, 31),
    9: Fraction(63, 95),
    10: Fraction(34, 55),
}


def selector_coefficients(degree: int) -> dict[Partition, Fraction]:
    """Coefficients of the exact d-cycle indicator."""

    validate_degree(degree)
    cycle = (degree,)
    return {
        partition: Fraction(character(partition, cycle), degree)
        for partition in partitions(degree)
    }


def evaluate_coefficients(
    coefficients: dict[Partition, Fraction], cycle_type: Partition
) -> Fraction:
    return sum(
        coefficient * character(partition, cycle_type)
        for partition, coefficient in coefficients.items()
    )


def weighted_l1(coefficients: dict[Partition, Fraction]) -> Fraction:
    return sum(
        dimension(partition) * abs(coefficient)
        for partition, coefficient in coefficients.items()
    )


def hook_only_branching_diagnostic(degree: int) -> dict[str, object]:
    """Test the dual ansatz with all nonhook predecessor potentials set to zero."""

    validate_degree(degree)
    mass = Fraction(2 ** (degree - 1), degree)
    ratios: list[tuple[Fraction, int]] = []
    for k in range(1, degree - 2):
        potential = (-1) ** k * (
            sum(math.comb(degree - 1, j) for j in range(k + 1)) - (k + 1) * mass
        )
        near_hook = (degree - 1 - k, 2, *([1] * (k - 1)))
        ratios.append((abs(potential) / dimension(near_hook), k))
    maximum = max((ratio for ratio, _ in ratios), default=Fraction(0))
    return {
        "maximum_nonhook_capacity_ratio": str(maximum),
        "feasible": maximum <= 1,
        "first_violation_k": next((k for ratio, k in ratios if ratio > 1), None),
    }


def verify_degree(degree: int) -> dict[str, object]:
    validate_degree(degree)
    shapes = partitions(degree)
    cycle_types = shapes

    for left in shapes:
        if character(left, (1,) * degree) != dimension(left):
            raise AssertionError("hook-length dimension and identity trace disagree")
        for right in shapes:
            inner_product = sum(
                Fraction(
                    character(left, cycle_type) * character(right, cycle_type),
                    centralizer_size(cycle_type),
                )
                for cycle_type in cycle_types
            )
            if inner_product != int(left == right):
                raise AssertionError("character-row orthogonality failed")

    coefficients = selector_coefficients(degree)
    fixedpoint_types = tuple(
        cycle_type for cycle_type in cycle_types if 1 in cycle_type
    )
    other_derangements = tuple(
        cycle_type
        for cycle_type in cycle_types
        if 1 not in cycle_type and cycle_type != (degree,)
    )
    for cycle_type in fixedpoint_types:
        if evaluate_coefficients(coefficients, cycle_type) != 0:
            raise AssertionError("exact selector did not vanish on a fixed-point class")
    if evaluate_coefficients(coefficients, (degree,)) != 1:
        raise AssertionError("exact selector lost its d-cycle normalization")

    for predecessor in partitions(degree - 1):
        restricted_coefficient = sum(
            coefficients[partition]
            for partition in shapes
            if predecessor in predecessors(partition)
        )
        if restricted_coefficient != 0:
            raise AssertionError("Young-branching restriction did not vanish")

    mass = weighted_l1(coefficients)
    expected_mass = Fraction(2 ** (degree - 1), degree)
    if mass != expected_mass:
        raise AssertionError("exact-cycle weighted mass changed")

    certificate = DUAL_CERTIFICATES[degree]
    if certificate.get((degree,), Fraction(0)) != expected_mass:
        raise AssertionError("dual objective does not equal the candidate mass")
    if any(
        cycle_type != (degree,) and 1 not in cycle_type for cycle_type in certificate
    ):
        raise AssertionError("dual certificate has forbidden derangement support")

    dual_values: dict[Partition, Fraction] = {}
    nonhook_slacks: list[Fraction] = []
    for partition in shapes:
        dual_value = sum(
            value * character(partition, cycle_type)
            for cycle_type, value in certificate.items()
        )
        irreducible_dimension = dimension(partition)
        if abs(dual_value) > irreducible_dimension:
            raise AssertionError("dual character bound failed")
        dual_values[partition] = dual_value
        if is_hook(partition):
            k = degree - partition[0]
            if dual_value != (-1) ** k * irreducible_dimension:
                raise AssertionError("dual hook saturation failed")
        else:
            nonhook_slacks.append(
                Fraction(irreducible_dimension - abs(dual_value), irreducible_dimension)
            )

    minimum_slack: Fraction | None = min(nonhook_slacks, default=None)
    if degree >= 4 and minimum_slack != EXPECTED_STRICT_SLACK[degree]:
        raise AssertionError("strict nonhook dual slack changed")

    nonzero_primal = [
        {
            "partition": list(partition),
            "coefficient": str(coefficient),
            "dimension": dimension(partition),
        }
        for partition, coefficient in coefficients.items()
        if coefficient
    ]
    dual_rows = [
        {"cycle_type": list(cycle_type), "coefficient": str(value)}
        for cycle_type, value in certificate.items()
        if value
    ]
    return {
        "degree": degree,
        "irreducibles": len(shapes),
        "fixedpoint_constraints": len(fixedpoint_types),
        "derangement_classes": len(other_derangements) + 1,
        "free_derangement_values": len(other_derangements),
        "candidate": "exact d-cycle indicator",
        "candidate_nonzero_coefficients": nonzero_primal,
        "weighted_l1_optimum": str(mass),
        "exact_cycle_mass": str(expected_mass),
        "optimum_to_exact_cycle_ratio": "1",
        "dual_certificate": dual_rows,
        "minimum_relative_nonhook_dual_slack": (
            str(minimum_slack) if minimum_slack is not None else "not applicable"
        ),
        "unique_optimizer": True,
        "hook_only_branching_diagnostic": hook_only_branching_diagnostic(degree),
    }


def run(check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    panels = [verify_degree(degree) for degree in range(MIN_DEGREE, MAX_DEGREE + 1)]
    partition_counts = [
        len(partitions(degree)) for degree in range(MIN_DEGREE, MAX_DEGREE + 1)
    ]
    return {
        "schema": "riemann.function_field.ffps_derangement_selector_finite_l1.v1",
        "status": (
            "exact finite optimization through d=10; all-d optimality remains conjectural"
        ),
        "frozen_sources": SOURCE_BLOBS,
        "problem": {
            "coefficient_field": (
                "real or complex characteristic-zero coefficients; certificates rational"
            ),
            "constraints": (
                "Q((d))=1 and Q(mu)=0 for every cycle type mu containing 1"
            ),
            "equivalent_root_incidence_condition": (
                "Perm_d*Q=0 pointwise, equivalently Res_(S_(d-1))^(S_d) Q=0"
            ),
            "character_expansion": "Q=sum_lambda a_lambda*chi_lambda",
            "objective": "minimize sum_lambda dim(lambda)*abs(a_lambda)",
        },
        "finite_theorem": {
            "degrees": "2<=d<=10",
            "optimum": "2^(d-1)/d",
            "unique_optimizer": "Q=1_(d-cycle)",
            "proof": (
                "exact Murnaghan-Nakayama character tables plus explicit strict "
                "rational LP-dual certificates"
            ),
            "all_d_claim": False,
        },
        "panels": panels,
        "all_d_frontier": {
            "conjecture": (
                "for every d>=2 the unique optimum remains the exact d-cycle indicator"
            ),
            "proved": False,
            "forced_hook_predecessor_potential": (
                "x_k=(-1)^k*(sum_(j=0)^k binom(d-1,j)-(k+1)*2^(d-1)/d)"
            ),
            "zero_interior_potential_ansatz": (
                "works through d=7 but violates a nonhook capacity first at d=8; "
                "an all-d proof needs propagated interior Young-lattice potentials"
            ),
        },
        "scope": {
            "characteristic": 0,
            "category": "full semisimple class-function algebra of S_d",
            "native_ffps_adapter_constructed": False,
            "asymptotic_selector_bound_proved": False,
            "rh_proved": False,
            "grh_proved": False,
            "novelty_claimed": False,
        },
        "resource_caps": {
            "maximum_degree": MAX_DEGREE,
            "maximum_irreducibles": max(partition_counts),
            "partitions_checked": sum(partition_counts),
            "character_table_entries": sum(count**2 for count in partition_counts),
            "orthogonality_summands": sum(count**3 for count in partition_counts),
            "dual_character_inequalities": sum(partition_counts),
            "external_lp_calls_in_replay": 0,
            "floating_point_steps_in_replay": 0,
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
