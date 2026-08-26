#!/usr/bin/env python3
"""Bounded replay for the exact Boolean half-source diagonal gain."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIREWALL_PATH = HERE / "ffps_weighted_rich_core_transfer_firewall.py"
SPEC = importlib.util.spec_from_file_location("weighted_rich_firewall", FIREWALL_PATH)
assert SPEC and SPEC.loader
weighted_rich_firewall = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(weighted_rich_firewall)

REPLAY_PRIMES = (2, 3, 5, 7, 11, 13)
HALF_SOURCE_WEIGHT = Fraction(3, 2)
HALF_SOURCE_SQUARE_WEIGHT = Fraction(9, 4)


def original_half_source(support: tuple[int, ...], cutoff: int) -> Fraction:
    """Coefficient of f_U=a_U star h, with h(S)=(-1/2)^|S|."""
    if cutoff < 1 or len(set(support)) != len(support):
        raise ValueError("use a positive cutoff and squarefree support")
    total = Fraction(0)
    size = len(support)
    for first_mask in range(1 << size):
        first = tuple(
            support[index] for index in range(size) if first_mask & (1 << index)
        )
        tail_size = size - first_mask.bit_count()
        total += weighted_rich_firewall.boolean_a(first, cutoff) * Fraction(
            (-1) ** tail_size, 2**tail_size
        )
    return total


def recombined_half_source(support: tuple[int, ...], cutoff: int) -> Fraction:
    """Coefficient of mu_>U star q, with q(S)=2^-|S|."""
    if cutoff < 1 or len(set(support)) != len(support):
        raise ValueError("use a positive cutoff and squarefree support")
    total = Fraction(0)
    size = len(support)
    for first_mask in range(1 << size):
        first_product = weighted_rich_firewall.subset_product(support, first_mask)
        if first_product > cutoff:
            first_size = first_mask.bit_count()
            tail_size = size - first_size
            total += Fraction((-1) ** first_size, 2**tail_size)
    return total


def bad_tail_log_exponent(alpha: float, weight: float = 9 / 4) -> float:
    if not 0 < alpha < weight / 2:
        raise ValueError("require 0<alpha<weight/2")
    optimizer = 2 * alpha / weight
    return weight / 2 + alpha - 1 - alpha * math.log(optimizer)


def tail_log_saving(alpha: float, weight: float = 9 / 4) -> float:
    return weight - 1 - bad_tail_log_exponent(alpha, weight)


def identity_panels() -> list[dict[str, object]]:
    panels: list[dict[str, object]] = []
    for size in range(1, len(REPLAY_PRIMES) + 1):
        support = REPLAY_PRIMES[:size]
        cutoffs = sorted(
            {
                weighted_rich_firewall.subset_product(support, mask)
                for mask in range(1 << size)
            }
        )
        maximum = Fraction(0)
        for cutoff in cutoffs:
            original = original_half_source(support, cutoff)
            recombined = recombined_half_source(support, cutoff)
            if original != recombined:
                raise AssertionError("half-source recombination failed")
            maximum = max(maximum, abs(original))
        panels.append(
            {
                "support_size": size,
                "cutoff_cells_checked": len(cutoffs),
                "maximum_absolute_coefficient": str(maximum),
                "three_halves_majorant": str(HALF_SOURCE_WEIGHT**size),
            }
        )
    return panels


def run() -> dict[str, object]:
    alpha = 0.274064461784
    return {
        "half_source": {
            "identity": "f_U=mu_>U star q, q(S)=2^(-omega(S))",
            "coefficient_formula": (
                "sum over coprime R*T=n, R>U of mu(R)*2^(-omega(T))"
            ),
            "support": "f_U(n)!=0 implies n>U",
            "uniform_majorant": "abs(f_U(n))<=(3/2)^omega(n)",
        },
        "owner_core_source_diagonal": {
            "physical_shape": "n=p*a^2 with (p,a)=1",
            "horizon_bound": (
                "sum_(p*a^2<=C*Y) abs(f_U(a))^2/(p*a^2) "
                "<< Y^(-1/6)*(log Y)^(5/4)*log log Y"
            ),
            "moving_cutoff": "U=floor(Y^(1/6))",
            "owner_range": "p<=C*Y/U^2",
        },
        "poor_half_core": {
            "rank": "r=floor(alpha*log log Y)",
            "square_majorant_weight": str(HALF_SOURCE_SQUARE_WEIGHT),
            "full_tail_log_exponent": f"{float(HALF_SOURCE_SQUARE_WEIGHT - 1):.12f}",
            "bad_tail_log_exponent": f"{bad_tail_log_exponent(alpha):.12f}",
            "relative_log_saving": f"{tail_log_saving(alpha):.12f}",
        },
        "identity_panels": identity_panels(),
        "resource_caps": {
            "maximum_support_size": len(REPLAY_PRIMES),
            "maximum_two_box_assignments": 2 ** len(REPLAY_PRIMES),
            "source_atoms_enumerated": 0,
            "conductors_enumerated": 0,
            "curves_enumerated": 0,
            "point_counts": 0,
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
