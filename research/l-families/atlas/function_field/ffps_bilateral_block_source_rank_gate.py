#!/usr/bin/env python3
"""Exact replay for the bilateral block-interferometer source-rank gate."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

MAX_PRIME = 29


def single_block_leverage(prime: int) -> Fraction:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 5
        or prime > MAX_PRIME
        or prime % 4 != 1
    ):
        raise ValueError("prime must be an eligible 1 mod 4 panel prime")
    return Fraction(4 * (prime - 1), 3 * prime + 1)


def character_value(character: int, point: int) -> int:
    return -1 if (character & point).bit_count() % 2 else 1


def quotient_kernel(selected_characters: tuple[int, ...]) -> list[list[Fraction]]:
    if not selected_characters or any(
        character not in (1, 2, 3) for character in selected_characters
    ):
        raise ValueError("selected characters must be a nonempty subset of C2^2 dual")
    if len(set(selected_characters)) != len(selected_characters):
        raise ValueError("selected characters must be distinct")
    return [
        [
            Fraction(1)
            - Fraction(
                sum(
                    character_value(character, left) * character_value(character, right)
                    for character in selected_characters
                ),
                len(selected_characters),
            )
            for right in range(4)
        ]
        for left in range(4)
    ]


def run() -> dict[str, object]:
    clean_kernel = quotient_kernel((3,))
    full_kernel = quotient_kernel((1, 2, 3))
    singleton_rows = [
        {
            "prime": prime,
            "leverage": str(single_block_leverage(prime)),
            "strict_contraction": single_block_leverage(prime) < 1,
        }
        for prime in (5, 13, 17, 29)
    ]
    pair_rows = [
        {
            "primes": [left, right],
            "two_singleton_block_leverage": str(
                single_block_leverage(left) * single_block_leverage(right)
            ),
        }
        for left, right in ((5, 13), (5, 17), (13, 17))
    ]
    return {
        "bilateral_fourier_ledger": {
            "quotient": "C2^2",
            "nonprincipal_characters": {
                "1": "left single-sided/root mode",
                "2": "right single-sided/root mode",
                "3": "double-nonprincipal checkerboard mode",
            },
            "clean_selected_rank": 1,
            "full_selected_rank": 2,
            "clean_kernel": [[str(value) for value in row] for row in clean_kernel],
            "full_kernel": [[str(value) for value in row] for row in full_kernel],
            "clean_equivalence_classes": [[0, 3], [1, 2]],
            "deduction": (
                "after the single-sided modes are removed, the four bilateral cosets "
                "coarsen to the two classes of the product checkerboard"
            ),
        },
        "singleton_block_formula": "4*(p-1)/(3*p+1)",
        "singleton_panels": singleton_rows,
        "two_singleton_panels": pair_rows,
        "source_arity_gate": {
            "current_joint_physical_phase_coordinates": 2,
            "minimum_coordinates_for_two_strictly_improving_blocks": 4,
            "reason": (
                "every eligible singleton block has leverage at least one, so each "
                "strictly improving block needs at least two local phase factors"
            ),
        },
        "resource_caps": {
            "maximum_prime": MAX_PRIME,
            "quotient_points": 4,
            "matrix_cells": 16,
            "point_counts": 0,
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
