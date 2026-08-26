#!/usr/bin/env python3
"""Exact replay for the corrected bilateral block source/leverage gate."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

MAX_PRIME = 29

FROZEN_PR_751_HEAD = "98af0db6ec7f77d6333a77a3dac53c4698852f43"
SOURCE_LEDGER = {
    "L-106120": {
        "git_blob": "a8d829dc10611adb7bfb4853902bdff0ab02a065",
        "evidence": "equation (8): PP, P-NP, NP-P, NP-NP all retained",
    },
    "T-106121": {
        "git_blob": "9111983ae4bf199a8315310a9ce090561430c33b",
        "evidence": "Section 1: both one-collision mixed channels retained",
    },
    "L-106131": {
        "git_blob": "37722c3f36ec7d1681f34d4329a3795e5028f7ae",
        "evidence": "equation (13): full four-channel Wick tensor split",
    },
    "T-106140": {
        "git_blob": "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
        "evidence": "equation (6): mixed and double-NP channels recombined",
    },
}


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


def bilateral_checkerboard_leverage(left: int, right: int) -> Fraction:
    """Leverage when both live phase factors form one checkerboard block."""
    single_block_leverage(left)
    single_block_leverage(right)
    if left == right:
        raise ValueError("the bilateral marked primes must be distinct")
    return Fraction(
        4 * (left - 1) * (right - 1),
        5 * left * right + left + right + 1,
    )


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
    product_only_kernel = quotient_kernel((3,))
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
            "one_two_factor_block_leverage": str(
                bilateral_checkerboard_leverage(left, right)
            ),
            "rank_two_contracts": (
                single_block_leverage(left) * single_block_leverage(right) < 1
            ),
            "rank_one_contracts": bilateral_checkerboard_leverage(left, right) < 1,
        }
        for left, right in ((5, 13), (5, 17), (13, 17))
    ]
    return {
        "frozen_source": {
            "head": FROZEN_PR_751_HEAD,
            "claims": SOURCE_LEDGER,
        },
        "bilateral_fourier_ledger": {
            "quotient": "C2^2",
            "nonprincipal_characters": {
                "1": "left mixed principal--nonprincipal mode",
                "2": "right mixed nonprincipal--principal mode",
                "3": "double-nonprincipal checkerboard mode",
            },
            "native_quotient_rank": 2,
            "native_nonprincipal_character_count": 3,
            "mixed_channels_retained": True,
            "full_kernel": [[str(value) for value in row] for row in full_kernel],
            "product_only_comparison": {
                "native_source_forces_this_truncation": False,
                "kernel": [
                    [str(value) for value in row] for row in product_only_kernel
                ],
                "equivalence_classes": [[0, 3], [1, 2]],
                "interpretation": (
                    "the existing one-block double-NP checkerboard is a legitimate "
                    "subfamily, not a clean-source collapse"
                ),
            },
            "correction": (
                "L-106120/L-106131/T-106140 retain both mixed modes, so the "
                "previous claimed rank-one clean-source collapse was false"
            ),
        },
        "singleton_block_formula": "4*(p-1)/(3*p+1)",
        "singleton_panels": singleton_rows,
        "two_singleton_panels": pair_rows,
        "source_arity_gate": {
            "current_joint_physical_phase_coordinates": 2,
            "current_native_quotient_rank": 2,
            "current_rank_two_partition": "{ell}|{rho}",
            "current_rank_two_partition_contracts": False,
            "minimum_coordinates_for_two_strictly_improving_blocks": 4,
            "reason": (
                "every eligible singleton block has leverage at least one, so each "
                "strictly improving block needs at least two local phase factors"
            ),
            "native_four_phase_candidate": {
                "coordinates": ["X_1", "Y_1", "X_2", "Y_2"],
                "blocks": ["epsilon(X_1)*epsilon(Y_1)", "epsilon(X_2)*epsilon(Y_2)"],
                "status": "design specification; source identity not yet proved",
            },
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
