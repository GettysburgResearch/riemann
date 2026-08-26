#!/usr/bin/env python3
"""Bounded exact ledger for the sharp C2^r relative branch projector."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

MAX_BLOCKS = 10


def dot_parity(left: int, right: int) -> int:
    return (left & right).bit_count() % 2


def fraction_text(value: Fraction) -> str:
    return str(value)


def validate_block_data(blocks: int, inertia_vector: int) -> None:
    if (
        isinstance(blocks, bool)
        or not isinstance(blocks, int)
        or not 1 <= blocks <= MAX_BLOCKS
    ):
        raise ValueError("block count is outside the replay range")
    if (
        isinstance(inertia_vector, bool)
        or not isinstance(inertia_vector, int)
        or not 0 <= inertia_vector < 2**blocks
    ):
        raise ValueError("inertia vector is outside the block dual")


def character_counts(blocks: int, inertia_vector: int) -> dict[str, int]:
    """Count principal/selected characters after restriction to local inertia."""
    validate_block_data(blocks, inertia_vector)
    size = 2**blocks
    selected_trivial = sum(
        dot_parity(label, inertia_vector) == 0 for label in range(1, size)
    )
    selected_sign = size - 1 - selected_trivial
    return {
        "group_order": size,
        "selected_trivial": selected_trivial,
        "selected_sign": selected_sign,
        "hard_trivial": selected_trivial + 1,
        "hard_sign": selected_sign,
    }


def virtual_row(trivial: Fraction, sign: Fraction) -> dict[str, str]:
    """Return exact invariants of a virtual C2 character a*1+b*kappa."""
    return {
        "trivial_coefficient": fraction_text(trivial),
        "sign_coefficient": fraction_text(sign),
        "virtual_rank": fraction_text(trivial + sign),
        "virtual_inertia_invariants": fraction_text(trivial),
        "signed_tame_artin_conductor": fraction_text(sign),
        "absolute_ramified_character_mass": fraction_text(abs(sign)),
    }


def local_inertia_ledger(blocks: int, inertia_vector: int = 1) -> dict[str, object]:
    """Compute all normalization variants at one tame inertia generator."""
    counts = character_counts(blocks, inertia_vector)
    size = counts["group_order"]
    hard = (
        Fraction(counts["hard_trivial"]),
        Fraction(counts["hard_sign"]),
    )
    selected = (
        Fraction(counts["selected_trivial"]),
        Fraction(counts["selected_sign"]),
    )
    principal = (Fraction(1), Fraction(0))
    selected_average = tuple(value / (size - 1) for value in selected)
    relative = tuple(hard[index] - selected[index] for index in range(2))
    hard_minus_selected_average = tuple(
        hard[index] - selected_average[index] for index in range(2)
    )
    atom_free = tuple(principal[index] - selected_average[index] for index in range(2))
    raw_atom_free = tuple((size - 1) * value for value in atom_free)

    if inertia_vector:
        expected = (size // 2 - 1, size // 2)
        if (counts["selected_trivial"], counts["selected_sign"]) != expected:
            raise AssertionError("nonzero inertia does not have the hyperplane census")
    if relative != principal:
        raise AssertionError("hard-minus-selected is not the principal character")

    return {
        "blocks": blocks,
        "inertia_vector": inertia_vector,
        "is_branch": bool(inertia_vector),
        "character_counts": counts,
        "objects": {
            "hard_C": virtual_row(*hard),
            "unnormalized_selected_S": virtual_row(*selected),
            "principal_Pi0": virtual_row(*principal),
            "relative_C_minus_S": virtual_row(*relative),
            "normalized_selected_average": virtual_row(*selected_average),
            "C_minus_normalized_selected_average": virtual_row(
                *hard_minus_selected_average
            ),
            "atom_free_Pi0_minus_normalized_selected_average": virtual_row(*atom_free),
            "integral_atom_free_numerator": virtual_row(*raw_atom_free),
        },
    }


def extension_ledger(blocks: int, place_degree: int) -> dict[str, object]:
    """Compare zero and termwise middle extension at one branch place."""
    validate_block_data(blocks, 1)
    if (
        isinstance(place_degree, bool)
        or not isinstance(place_degree, int)
        or place_degree < 1
    ):
        raise ValueError("place degree must be a positive integer")
    size = 2**blocks
    rows = {
        "hard_C": {
            "generic_rank": size,
            "inertia_invariants": size // 2,
            "zero_extension_stalk_rank": 0,
            "middle_extension_stalk_rank": size // 2,
            "zero_extension_conductor_coefficient": size,
            "middle_extension_conductor_coefficient": size // 2,
        },
        "unnormalized_selected_S": {
            "generic_rank": size - 1,
            "inertia_invariants": size // 2 - 1,
            "zero_extension_stalk_rank": 0,
            "middle_extension_stalk_rank": size // 2 - 1,
            "zero_extension_conductor_coefficient": size - 1,
            "middle_extension_conductor_coefficient": size // 2,
        },
        "relative_C_minus_S": {
            "generic_rank": 1,
            "inertia_invariants": 1,
            "zero_extension_stalk_rank": 0,
            "middle_extension_stalk_rank": 1,
            "zero_extension_conductor_coefficient": 1,
            "middle_extension_conductor_coefficient": 0,
        },
    }
    relative = rows["relative_C_minus_S"]
    return {
        "blocks": blocks,
        "place_degree": place_degree,
        "rows": rows,
        "relative_zero_extension_conductor_degree": (
            relative["zero_extension_conductor_coefficient"] * place_degree
        ),
        "relative_middle_extension_conductor_degree": (
            relative["middle_extension_conductor_coefficient"] * place_degree
        ),
        "boundary_skyscraper_length": place_degree,
    }


def boundary_trace(place_degrees: tuple[int, ...], extension_degree: int) -> int:
    """Trace of the constant reduced boundary over F_(q^extension_degree)."""
    if not place_degrees or any(
        isinstance(degree, bool) or not isinstance(degree, int) or degree < 1
        for degree in place_degrees
    ):
        raise ValueError("place degrees must be a nonempty tuple of positives")
    if (
        isinstance(extension_degree, bool)
        or not isinstance(extension_degree, int)
        or extension_degree < 1
    ):
        raise ValueError("extension degree must be a positive integer")
    return sum(degree for degree in place_degrees if extension_degree % degree == 0)


def run() -> dict[str, object]:
    panels = [local_inertia_ledger(blocks) for blocks in (1, 2, 4, 8, 10)]
    unbranched_control = local_inertia_ledger(5, inertia_vector=0)
    degrees = (3, 5, 11)
    boundary_tower = [
        {
            "extension_degree": extension_degree,
            "boundary_trace": boundary_trace(degrees, extension_degree),
        }
        for extension_degree in (1, 3, 5, 11, 15, 33, 55, 165, 330)
    ]
    return {
        "theorem": {
            "open_relative_object": "C-S=Pi_0=E_U",
            "zero_extension_class": "[j_! E_U]=[E_X]-[i_* E_D]",
            "middle_extension_object": "ME(C)-ME(S)=E_X",
            "relative_zero_extension_conductor_degree": "deg(D)",
            "relative_middle_extension_conductor_degree": "0",
            "boundary_trace": "sum_(v in D, deg(v)|m) deg(v)",
            "supply_tax_verdict": (
                "ramified Kummer sectors cancel, but the common-open boundary "
                "retains the largest place degree"
            ),
        },
        "local_branch_panels": panels,
        "unbranched_control": unbranched_control,
        "extension_panels": [
            extension_ledger(blocks, place_degree=37) for blocks in (1, 2, 4, 8)
        ],
        "boundary_trace_panel": {
            "place_degrees": list(degrees),
            "rows": boundary_tower,
        },
        "resource_caps": {
            "maximum_blocks": MAX_BLOCKS,
            "maximum_character_labels": 2**MAX_BLOCKS,
            "finite_field_points": 0,
            "closed_places_enumerated": 0,
            "curves_or_pushforwards_computed": 0,
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
