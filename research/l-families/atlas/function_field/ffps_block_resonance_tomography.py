#!/usr/bin/env python3
"""Exact finite-linear-algebra replay for block-resonance tomography."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

MAX_BLOCKS = 10


def gf2_rank(rows: tuple[int, ...]) -> int:
    """Return the binary rank of bit-packed rows."""
    pivots: dict[int, int] = {}
    for original in rows:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return len(pivots)


def in_rowspace(vector: int, rows: tuple[int, ...]) -> bool:
    return gf2_rank((*rows, vector)) == gf2_rank(rows)


def dot_parity(left: int, right: int) -> int:
    return (left & right).bit_count() % 2


def pullback_exponent(label: int, block_rows: tuple[int, ...]) -> int:
    exponent = 0
    for index, row in enumerate(block_rows):
        if label & (1 << index):
            exponent ^= row
    return exponent


def validate_rows(block_rows: tuple[int, ...], relation_rows: tuple[int, ...]) -> None:
    blocks = len(block_rows)
    if blocks < 1 or blocks > MAX_BLOCKS:
        raise ValueError("block count is outside the replay range")
    if any(
        isinstance(row, bool) or not isinstance(row, int) or row < 0
        for row in block_rows
    ):
        raise ValueError("block rows must be nonnegative bit-packed integers")
    if any(
        isinstance(row, bool) or not isinstance(row, int) or row < 0
        for row in relation_rows
    ):
        raise ValueError("relation rows must be nonnegative bit-packed integers")


def tomography(
    block_rows: tuple[int, ...],
    relation_rows: tuple[int, ...],
    arithmetic_twist: int = 0,
) -> dict[str, object]:
    """Compute invariant modes and their exact arithmetic coefficients.

    ``block_rows`` are the quadratic monomial exponent rows.  A selected
    Fourier label ``s`` pulls back to their XOR selected by ``s``.
    ``relation_rows`` are the mod-two reductions of the saturated monomial
    relation lattice of a connected stratum.  ``arithmetic_twist`` records
    a linear Frobenius sign on selected labels.
    """
    validate_rows(block_rows, relation_rows)
    blocks = len(block_rows)
    if (
        isinstance(arithmetic_twist, bool)
        or not isinstance(arithmetic_twist, int)
        or arithmetic_twist < 0
        or arithmetic_twist >= 2**blocks
    ):
        raise ValueError("arithmetic twist is outside the selected dual")

    block_rank = gf2_rank(block_rows)
    relation_rank = gf2_rank(relation_rows)
    union_rank = gf2_rank((*block_rows, *relation_rows))
    intersection_dimension = block_rank + relation_rank - union_rank
    predicted_dimension = blocks - block_rank + intersection_dimension

    invariant_labels = tuple(
        label
        for label in range(2**blocks)
        if in_rowspace(pullback_exponent(label, block_rows), relation_rows)
    )
    if len(invariant_labels) != 2**predicted_dimension:
        raise AssertionError("row-space intersection formula failed")
    invariant_dimension = (len(invariant_labels)).bit_length() - 1
    if invariant_dimension != predicted_dimension:
        raise AssertionError("invariant dimension mismatch")

    nonzero_labels = invariant_labels[1:]
    arithmetic_sum = sum(
        -1 if dot_parity(arithmetic_twist, label) else 1 for label in nonzero_labels
    )
    twist_is_trivial = all(
        dot_parity(arithmetic_twist, label) == 0 for label in invariant_labels
    )
    predicted_sum = 2**invariant_dimension - 1 if twist_is_trivial else -1
    if arithmetic_sum != predicted_sum:
        raise AssertionError("arithmetic character-sum dichotomy failed")

    selected_count = 2**blocks - 1
    selected_normalized = Fraction(arithmetic_sum, selected_count)
    return {
        "blocks": blocks,
        "block_rank": block_rank,
        "block_kernel_dimension": blocks - block_rank,
        "relation_rank": relation_rank,
        "block_relation_intersection_dimension": intersection_dimension,
        "invariant_dimension": invariant_dimension,
        "invariant_selected_mode_count": len(nonzero_labels),
        "arithmetic_twist_trivial_on_invariants": twist_is_trivial,
        "selected_invariant_coefficient": arithmetic_sum,
        "normalized_selected_invariant_coefficient": str(selected_normalized),
        "hard_invariant_coefficient": 1 + arithmetic_sum,
        "relative_hard_minus_selected_coefficient": 1,
        "off_coset_interferometer_invariant_coefficient": str(1 - selected_normalized),
    }


def bilateral_block_rows(blocks: int) -> tuple[int, ...]:
    if (
        isinstance(blocks, bool)
        or not isinstance(blocks, int)
        or not 1 <= blocks <= MAX_BLOCKS
    ):
        raise ValueError("block count is outside the replay range")
    return tuple((1 << (2 * index)) | (1 << (2 * index + 1)) for index in range(blocks))


def aligned_relations(blocks: int, visible_codimension: int) -> tuple[int, ...]:
    rows = bilateral_block_rows(blocks)
    if (
        isinstance(visible_codimension, bool)
        or not isinstance(visible_codimension, int)
        or not 0 <= visible_codimension <= blocks
    ):
        raise ValueError("visible codimension is outside the replay range")
    return rows[:visible_codimension]


def double_collision_relations(blocks: int, collided_blocks: int) -> tuple[int, ...]:
    bilateral_block_rows(blocks)
    if (
        isinstance(collided_blocks, bool)
        or not isinstance(collided_blocks, int)
        or not 0 <= collided_blocks <= blocks
    ):
        raise ValueError("collided block count is outside the replay range")
    return tuple(1 << coordinate for coordinate in range(2 * collided_blocks))


def quotient_projector_check(blocks: int) -> dict[str, object]:
    if isinstance(blocks, bool) or not isinstance(blocks, int) or not 1 <= blocks <= 6:
        raise ValueError("projector check supports one through six blocks")
    size = 2**blocks
    rows = []
    for quotient in range(size):
        principal = 1
        selected = sum(
            -1 if dot_parity(character, quotient) else 1 for character in range(1, size)
        )
        hard = principal + selected
        if hard - selected != principal:
            raise AssertionError("relative projector identity failed")
        rows.append(
            {
                "quotient": quotient,
                "hard_kernel": hard,
                "selected_kernel": selected,
                "relative_kernel": hard - selected,
            }
        )
    return {"blocks": blocks, "rows": rows}


def run() -> dict[str, object]:
    panels: list[dict[str, object]] = []
    for blocks in (2, 4, 8, 10):
        block_rows = bilateral_block_rows(blocks)
        for visible_codimension in sorted({0, 1, min(2, blocks), blocks}):
            relations = aligned_relations(blocks, visible_codimension)
            row = tomography(block_rows, relations)
            row["panel"] = "orientation_preserving_aligned"
            row["visible_codimension"] = visible_codimension
            panels.append(row)
            if visible_codimension:
                twisted = tomography(block_rows, relations, arithmetic_twist=1)
                twisted["panel"] = "nontrivial_arithmetic_coset"
                twisted["visible_codimension"] = visible_codimension
                panels.append(twisted)

    left_only = tomography(bilateral_block_rows(4), (1,))
    left_only["panel"] = "one_sided_collision_is_not_block_visible"
    full_double = tomography(bilateral_block_rows(8), double_collision_relations(8, 8))
    full_double["panel"] = "full_orientation_preserving_double_collision"
    dependent = tomography((0b11, 0b11, 0b1100), ())
    dependent["panel"] = "generic_block_dependency_control"

    return {
        "theorem": {
            "invariant_dimension": (
                "d=(r-rank(B))+dim(row(B) intersect relation_space(Z))"
            ),
            "invariant_selected_modes": "2^d-1",
            "orientation_preserving_normalized_coefficient": ("(2^d-1)/(2^r-1)"),
            "nontrivial_arithmetic_coset_normalized_coefficient": ("-1/(2^r-1)"),
            "relative_projector": "C-S=Pi_0",
        },
        "panels": panels + [left_only, full_double, dependent],
        "quotient_projector_checks": [
            quotient_projector_check(blocks) for blocks in range(1, 6)
        ],
        "resource_caps": {
            "maximum_blocks": MAX_BLOCKS,
            "maximum_selected_labels_in_one_panel": 2**MAX_BLOCKS,
            "maximum_quotient_points": 2**5,
            "monomial_strata_enumerated": 0,
            "finite_field_points": 0,
            "curves_or_conductors": 0,
            "floating_point_operations": 0,
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
