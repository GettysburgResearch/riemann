#!/usr/bin/env python3
"""Exact replay for stable-tail transport in the selector Young lattice."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from functools import cache
from itertools import pairwise
from pathlib import Path

Partition = tuple[int, ...]
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "9ced25befb6dd88146809866a34a15fec034b096"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_SELECTOR_YOUNG_LATTICE_PROPAGATION_OBSTRUCTION.md"
    ): "92b9010d1f15f093c17fc3f035e1d8b8ba95903b",
    (
        "research/l-families/atlas/function_field/"
        "ffps_selector_young_lattice_propagation_obstruction.py"
    ): "8a10eb6d1c5e787a5e5b1467311ebe6e2d3b5e9c",
    (
        "research/l-families/atlas/function_field/"
        "ffps_selector_young_lattice_propagation_obstruction.json"
    ): "9f3b9097873bc579941366234522f86ce0f84374",
    "tests/test_ffps_selector_young_lattice_propagation_obstruction.py": (
        "394611aa05f0d38ea2bff962f8801aa1dda83e18"
    ),
}
MIN_DEGREE = 5
MAX_DEGREE = 64
MAX_TAIL_SIZE = 8
PANEL_DEGREE = 32
PANEL_TAILS: tuple[Partition, ...] = (
    (),
    (1,),
    (2,),
    (1, 1),
    (2, 1),
    (3, 1),
    (3, 2),
    (3, 2, 1),
)


def check_source_blobs() -> None:
    """Authenticate the audited propagation packet."""

    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {SOURCE_COMMIT}:{path}")


def validate_degree(degree: int) -> None:
    if (
        isinstance(degree, bool)
        or not isinstance(degree, int)
        or not MIN_DEGREE <= degree <= MAX_DEGREE
    ):
        raise ValueError(f"degree must lie in [{MIN_DEGREE},{MAX_DEGREE}]")


def validate_partition(partition: Partition) -> None:
    if not isinstance(partition, tuple) or any(
        isinstance(part, bool) or not isinstance(part, int) or part < 1
        for part in partition
    ):
        raise ValueError("partition must be a tuple of positive integers")
    if any(left < right for left, right in pairwise(partition)):
        raise ValueError("partition parts must be weakly decreasing")
    if sum(partition) > MAX_TAIL_SIZE:
        raise ValueError(f"tail size must not exceed {MAX_TAIL_SIZE}")


@cache
def partitions(total: int, largest: int | None = None) -> tuple[Partition, ...]:
    if (
        isinstance(total, bool)
        or not isinstance(total, int)
        or not 0 <= total <= MAX_TAIL_SIZE
    ):
        raise ValueError(f"total must lie in [0,{MAX_TAIL_SIZE}]")
    if total == 0:
        return ((),)
    upper = total if largest is None else min(total, largest)
    return tuple(
        (first, *tail)
        for first in range(upper, 0, -1)
        for tail in partitions(total - first, first)
    )


@cache
def predecessors(partition: Partition) -> tuple[Partition, ...]:
    validate_partition(partition)
    result: list[Partition] = []
    for row, row_length in enumerate(partition):
        if row + 1 < len(partition) and partition[row + 1] == row_length:
            continue
        predecessor = list(partition)
        predecessor[row] -= 1
        if predecessor[row] == 0:
            predecessor.pop(row)
        result.append(tuple(predecessor))
    return tuple(result)


def is_column(partition: Partition) -> bool:
    validate_partition(partition)
    return all(part == 1 for part in partition)


@cache
def transport_coefficient(partition: Partition) -> int:
    """Positive absorbing-column path weight a_beta."""

    validate_partition(partition)
    if is_column(partition):
        return len(partition) + 1
    return sum(transport_coefficient(pred) for pred in predecessors(partition))


def minimum_stable_degree(partition: Partition) -> int:
    validate_partition(partition)
    return sum(partition) + (partition[0] if partition else 0) + 1


def stable_potential_shape(degree: int, partition: Partition) -> Partition:
    validate_degree(degree)
    validate_partition(partition)
    if degree < minimum_stable_degree(partition):
        raise ValueError("degree is below the stable-tail range")
    return (degree - 1 - sum(partition), *partition)


def stable_ambient_shape(degree: int, partition: Partition) -> Partition:
    validate_degree(degree)
    validate_partition(partition)
    if degree < minimum_stable_degree(partition):
        raise ValueError("degree is below the stable-tail range")
    return (degree - sum(partition), *partition)


def dimension(partition: Partition) -> int:
    """Hook-length dimension."""

    if not partition:
        return 1
    total = sum(partition)
    denominator = 1
    for row, row_length in enumerate(partition):
        for column in range(row_length):
            denominator *= (
                row_length
                - column
                + sum(lower > column for lower in partition[row + 1 :])
            )
    return math.factorial(total) // denominator


def cycle_dual_mass(degree: int) -> Fraction:
    validate_degree(degree)
    return Fraction(2 ** (degree - 1), degree)


def hook_potential(degree: int, depth: int) -> Fraction:
    validate_degree(degree)
    if (
        isinstance(depth, bool)
        or not isinstance(depth, int)
        or not 0 <= depth <= degree - 2
    ):
        raise ValueError(f"hook depth must lie in [0,{degree - 2}]")
    partial = sum(math.comb(degree - 1, index) for index in range(depth + 1))
    return (-1) ** depth * (partial - (depth + 1) * cycle_dual_mass(degree))


def column_error(degree: int, height: int) -> int:
    validate_degree(degree)
    if (
        isinstance(height, bool)
        or not isinstance(height, int)
        or not 0 <= height <= MAX_TAIL_SIZE
    ):
        raise ValueError(f"column height must lie in [0,{MAX_TAIL_SIZE}]")
    return sum(math.comb(degree - 1, index) for index in range(height + 1))


@cache
def transport_error(degree: int, partition: Partition) -> int:
    """Recursive exact error E_beta(d)."""

    validate_degree(degree)
    validate_partition(partition)
    if degree < minimum_stable_degree(partition):
        raise ValueError("degree is below the stable-tail range")
    if is_column(partition):
        return column_error(degree, len(partition))
    ambient = stable_ambient_shape(degree, partition)
    return dimension(ambient) + sum(
        transport_error(degree, pred) for pred in predecessors(partition)
    )


def verify_tail(degree: int, partition: Partition) -> dict[str, object]:
    coefficient = transport_coefficient(partition)
    error = transport_error(degree, partition)
    if is_column(partition):
        if coefficient != len(partition) + 1:
            raise AssertionError("column transport coefficient failed")
        if error != column_error(degree, len(partition)):
            raise AssertionError("column error failed")
    else:
        preds = predecessors(partition)
        if coefficient != sum(transport_coefficient(pred) for pred in preds):
            raise AssertionError("transport recursion failed")
        expected_error = dimension(stable_ambient_shape(degree, partition)) + sum(
            transport_error(degree, pred) for pred in preds
        )
        if error != expected_error:
            raise AssertionError("error recursion failed")
    return {
        "tail": list(partition),
        "tail_size": sum(partition),
        "potential_shape": list(stable_potential_shape(degree, partition)),
        "transport_coefficient": coefficient,
        "exact_error": error,
        "error_to_cycle_mass": str(Fraction(error, 1) / cycle_dual_mass(degree)),
    }


def verify_three_row_cancellation(index: int) -> dict[str, int]:
    if (
        isinstance(index, bool)
        or not isinstance(index, int)
        or not 2 <= index <= MAX_TAIL_SIZE - 1
    ):
        raise ValueError(f"index must lie in [2,{MAX_TAIL_SIZE - 1}]")
    row = transport_coefficient((index,))
    current = transport_coefficient((index, 1))
    previous = transport_coefficient((index - 1, 1))
    if row != 2 or current != 2 * index + 1 or previous != 2 * index - 1:
        raise AssertionError("three-row coefficient formula failed")
    signed_sum = current - row - previous
    if signed_sum != 0:
        raise AssertionError("three-row leading cancellation failed")
    return {
        "index": index,
        "current_three_row_coefficient": current,
        "two_row_coefficient": row,
        "previous_three_row_coefficient": previous,
        "signed_sum": signed_sum,
    }


def verify_hook_transpose(degree: int) -> None:
    validate_degree(degree)
    sign = (-1) ** (degree - 1)
    for depth in range(degree - 1):
        opposite = degree - 2 - depth
        if hook_potential(degree, opposite) != sign * hook_potential(degree, depth):
            raise AssertionError("signed hook-transpose identity failed")


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    for degree in range(MIN_DEGREE, MAX_DEGREE + 1):
        verify_hook_transpose(degree)
        for size in range(MAX_TAIL_SIZE + 1):
            for partition in partitions(size):
                if degree >= minimum_stable_degree(partition):
                    verify_tail(degree, partition)
    three_row = [
        verify_three_row_cancellation(index) for index in range(2, MAX_TAIL_SIZE)
    ]
    return {
        "theorem": {
            "stable_tail_bound": ("|(-1)^(m+1) Re X_beta-a_beta*2^(d-1)/d|<=E_beta(d)"),
            "fixed_tail_asymptotic": (
                "Re X_beta=(-1)^(m+1)*a_beta*2^(d-1)/d+O_beta(d^m)"
            ),
            "transpose_reduction": (
                "existence implies a real lift with x_(nu')=(-1)^(d-1)x_nu"
            ),
            "remaining_gate": "bulk Young-lattice matching",
        },
        "scope": {
            "global_extension_constructed": False,
            "all_degree_optimum_proved": False,
            "linear_programming_used": False,
            "floating_point_used": False,
            "maximum_tail_size": MAX_TAIL_SIZE,
            "maximum_degree": MAX_DEGREE,
        },
        "panels": [verify_tail(PANEL_DEGREE, tail) for tail in PANEL_TAILS],
        "three_row_cancellations": three_row,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="run exact checks")
    parser.add_argument("--write", action="store_true", help="refresh canonical JSON")
    args = parser.parse_args()
    payload = run(check_sources=True)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    output = HERE / "ffps_selector_stable_tail_transport.json"
    if args.write:
        output.write_text(rendered, encoding="utf-8")
    elif args.check:
        if output.read_text(encoding="utf-8") != rendered:
            raise RuntimeError("canonical JSON is stale; run with --write")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
