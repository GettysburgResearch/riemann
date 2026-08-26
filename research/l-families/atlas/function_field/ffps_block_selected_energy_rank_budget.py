#!/usr/bin/env python3
"""Exact replay for block-path selected-energy cohomological rank budgets."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

MAX_BLOCKS = 12
MAX_PLACE_DEGREE = 5


def betti_number(place_degree: int, subset_size: int) -> int:
    return 2 * place_degree * subset_size - 2


def rank_budget(blocks: int, place_degree: int) -> dict[str, object]:
    if (
        isinstance(blocks, bool)
        or not isinstance(blocks, int)
        or blocks < 1
        or blocks > MAX_BLOCKS
    ):
        raise ValueError("blocks is outside the replay range")
    if (
        isinstance(place_degree, bool)
        or not isinstance(place_degree, int)
        or place_degree < 1
        or place_degree > MAX_PLACE_DEGREE
    ):
        raise ValueError("place_degree is outside the replay range")

    mode_count = 2**blocks - 1
    total_betti = sum(
        math.comb(blocks, size) * betti_number(place_degree, size)
        for size in range(1, blocks + 1)
    )
    total_square = sum(
        math.comb(blocks, size) * betti_number(place_degree, size) ** 2
        for size in range(1, blocks + 1)
    )
    closed_total_betti = 2 * place_degree * blocks * 2 ** (blocks - 1) - 2 * mode_count
    closed_total_square = (
        2**blocks
        * (place_degree**2 * blocks * (blocks + 1) - 4 * place_degree * blocks + 4)
        - 4
    )
    if total_betti != closed_total_betti or total_square != closed_total_square:
        raise AssertionError("closed rank-budget formula failed")
    return {
        "blocks": blocks,
        "place_degree": place_degree,
        "selected_mode_count": mode_count,
        "total_first_moment_rank": total_betti,
        "average_first_moment_rank": str(Fraction(total_betti, mode_count)),
        "total_selected_energy_rank": total_square,
        "average_selected_energy_rank": str(Fraction(total_square, mode_count)),
        "asymptotic_average_selected_energy_rank": (
            f"{place_degree**2}*r^2{place_degree**2 - 4 * place_degree:+d}*r+4+O(2^-r)"
        ),
    }


def run() -> dict[str, object]:
    panels = [
        rank_budget(blocks, place_degree)
        for place_degree in (1, 2, 3)
        for blocks in (1, 2, 3, 5, 8, 12)
    ]
    return {
        "exact_formula": {
            "mode_betti": "b_S=2e|S|-2",
            "average_betti": "(2er2^(r-1)-2(2^r-1))/(2^r-1)",
            "average_betti_square": ("(2^r*(e^2*r*(r+1)-4er+4)-4)/(2^r-1)"),
            "deduction": (
                "the selected average has linear first-moment rank but quadratic "
                "second-moment tensor rank"
            ),
        },
        "panels": panels,
        "resource_caps": {
            "maximum_blocks": MAX_BLOCKS,
            "maximum_place_degree": MAX_PLACE_DEGREE,
            "largest_subset_size_sum": MAX_BLOCKS,
            "subsets_enumerated": 0,
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
