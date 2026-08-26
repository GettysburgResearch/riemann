#!/usr/bin/env python3
"""Exact replay for positive atom-free higher-order U-statistics."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

MAX_ATOMS = 8
MAX_ORDER = 4


def ordered_distinct_energy(masses: tuple[Fraction, ...], order: int) -> Fraction:
    if not masses or len(masses) > MAX_ATOMS or any(mass < 0 for mass in masses):
        raise ValueError("masses must be a bounded nonempty nonnegative tuple")
    if (
        isinstance(order, bool)
        or not isinstance(order, int)
        or order < 2
        or order > MAX_ORDER
        or order > len(masses)
    ):
        raise ValueError("order is outside the replay range")
    return sum(
        math.prod(masses[index] for index in indices)
        for indices in itertools.permutations(range(len(masses)), order)
    )


def delocalization_lower_bound(masses: tuple[Fraction, ...], order: int) -> Fraction:
    total = sum(masses)
    if total <= 0:
        raise ValueError("the total mass must be positive")
    alpha = max(masses) / total
    if (order - 1) * alpha >= 1:
        return Fraction(0)
    return total**order * math.prod(1 - step * alpha for step in range(order))


def uniform_certificate(support_size: int, order: int) -> dict[str, object]:
    if support_size > MAX_ATOMS:
        raise ValueError("support exceeds the replay cap")
    masses = (Fraction(1, support_size),) * support_size
    energy = ordered_distinct_energy(masses, order)
    lower = delocalization_lower_bound(masses, order)
    return {
        "support_size": support_size,
        "order": order,
        "ordered_distinct_energy": str(energy),
        "delocalization_lower_bound": str(lower),
        "equality": energy == lower,
        "closed_form": str(
            Fraction(
                math.prod(range(support_size - order + 1, support_size + 1)),
                support_size**order,
            )
        ),
    }


def run() -> dict[str, object]:
    uniform_rows = [
        uniform_certificate(support_size, order)
        for support_size in range(2, MAX_ATOMS + 1)
        for order in range(2, min(MAX_ORDER, support_size) + 1)
    ]
    control_masses = (
        Fraction(1, 3),
        Fraction(1, 4),
        Fraction(1, 6),
        Fraction(1, 8),
        Fraction(1, 12),
        Fraction(1, 24),
    )
    control_rows = []
    for order in (2, 3):
        energy = ordered_distinct_energy(control_masses, order)
        lower = delocalization_lower_bound(control_masses, order)
        control_rows.append(
            {
                "order": order,
                "energy": str(energy),
                "lower_bound": str(lower),
                "verified": energy >= lower,
            }
        )
    return {
        "exact_theorem": {
            "masses": "a_i>=0, A=sum_i a_i, max_i a_i<=alpha*A",
            "U_k": "sum over ordered distinct i_1,...,i_k of product_j a_(i_j)",
            "lower_bound": "U_k>=A^k*product_(j=0)^(k-1)(1-j*alpha)",
            "principal_corollary": (
                "|sum_i z_i|^(2k)<=N^k*U_k/product_(j=0)^(k-1)(1-j*alpha)"
            ),
            "range": "(k-1)*alpha<1",
            "sharpness": "equality for uniform mass on s atoms when alpha=1/s",
        },
        "uniform_equality_panels": uniform_rows,
        "nonuniform_controls": control_rows,
        "resource_caps": {
            "maximum_atoms": MAX_ATOMS,
            "maximum_order": MAX_ORDER,
            "largest_ordered_tuple_count": math.perm(MAX_ATOMS, MAX_ORDER),
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
