#!/usr/bin/env python3
"""Bounded replay for Boolean depth recombination and core-shell envelopes."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIREWALL_PATH = HERE / "ffps_weighted_rich_core_transfer_firewall.py"
SPEC = importlib.util.spec_from_file_location("weighted_rich_firewall", FIREWALL_PATH)
assert SPEC and SPEC.loader
weighted_rich_firewall = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(weighted_rich_firewall)

REPLAY_PRIMES = (2, 3, 5, 7, 11, 13)


def recombined_boolean_b(support: tuple[int, ...], cutoff: int) -> int:
    """Coefficient of mu_>U star mu_>U star 1 by three-box assignments."""
    if cutoff < 1 or len(set(support)) != len(support):
        raise ValueError("use a positive cutoff and squarefree support")
    total = 0
    size = len(support)
    for states in itertools.product(range(3), repeat=size):
        first_mask = sum((state == 0) << index for index, state in enumerate(states))
        second_mask = sum((state == 1) << index for index, state in enumerate(states))
        first = weighted_rich_firewall.subset_product(support, first_mask)
        second = weighted_rich_firewall.subset_product(support, second_mask)
        if first > cutoff and second > cutoff:
            first_size = sum(state == 0 for state in states)
            second_size = sum(state == 1 for state in states)
            total += (-1) ** (first_size + second_size)
    return total


def shell_bad_exponent(alpha: float, weight: float) -> float:
    if not 0 < alpha < weight / 2:
        raise ValueError("require 0<alpha<weight/2")
    optimizer = 2 * alpha / weight
    return weight / 2 + alpha - 1 - alpha * math.log(optimizer)


def shell_full_exponent(weight: float) -> float:
    if weight <= 0:
        raise ValueError("weight must be positive")
    return weight - 1


def shell_saving(alpha: float, weight: float) -> float:
    return shell_full_exponent(weight) - shell_bad_exponent(alpha, weight)


def identity_panels() -> list[dict[str, object]]:
    panels: list[dict[str, object]] = []
    for size in range(2, len(REPLAY_PRIMES) + 1):
        support = REPLAY_PRIMES[:size]
        divisors = sorted(
            {
                weighted_rich_firewall.subset_product(support, mask)
                for mask in range(1 << size)
            }
        )
        max_absolute = 0
        for cutoff in divisors:
            original = weighted_rich_firewall.boolean_b(support, cutoff)
            recombined = recombined_boolean_b(support, cutoff)
            if original != recombined:
                raise AssertionError("Boolean depth recombination failed")
            max_absolute = max(max_absolute, abs(original))
        panels.append(
            {
                "support_size": size,
                "cutoff_cells_checked": len(divisors),
                "maximum_absolute_coefficient": max_absolute,
                "three_box_majorant": 3**size,
            }
        )
    return panels


def run() -> dict[str, object]:
    alpha = 0.274064461784
    return {
        "depth_recombination": {
            "identity": "b_U=mu_>U star mu_>U star 1_sf",
            "coefficient_formula": (
                "sum over disjoint R,S,T with R*S*T=n, R>U, S>U of mu(R)*mu(S)"
            ),
            "uniform_three_box_majorant": "abs(b_U(n))<=3^omega(n)",
        },
        "fixed_ratio_core_shells": {
            "rank": "r=floor(alpha*log log x)",
            "l1": {
                "majorant_weight": 3,
                "full_shell_log_exponent": f"{shell_full_exponent(3):.12f}",
                "bad_shell_log_exponent": f"{shell_bad_exponent(alpha, 3):.12f}",
                "relative_log_saving": f"{shell_saving(alpha, 3):.12f}",
            },
            "l2_diagonal": {
                "majorant_weight": 9,
                "full_shell_log_exponent": f"{shell_full_exponent(9):.12f}",
                "bad_shell_log_exponent": f"{shell_bad_exponent(alpha, 9):.12f}",
                "relative_log_saving": f"{shell_saving(alpha, 9):.12f}",
            },
            "scope": (
                "uniform Boolean core-coefficient envelopes after indicator shell deletion; "
                "not a bound for the Hilbert-valued observed FFPS current"
            ),
        },
        "common_core": {
            "l1_factor": "sum_g mu^2(g)*9^omega(g)/g^2 < infinity",
            "l2_factor": "sum_g mu^2(g)*81^omega(g)/g^4 < infinity",
        },
        "identity_panels": identity_panels(),
        "resource_caps": {
            "maximum_support_size": len(REPLAY_PRIMES),
            "maximum_three_box_assignments": 3 ** len(REPLAY_PRIMES),
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
