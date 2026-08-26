#!/usr/bin/env python3
"""Bounded replay for the weighted rich-core transfer firewall."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

ROUGH_PRIMES = (103, 107, 79, 83)
OWNER_LEFT = 5 * 7
OWNER_RIGHT = 13 * 17


def subset_product(support: tuple[int, ...], mask: int) -> int:
    value = 1
    for index, prime in enumerate(support):
        if mask & (1 << index):
            value *= prime
    return value


def boolean_a(support: tuple[int, ...], cutoff: int) -> int:
    """The coefficient a_U=epsilon-mu_U star 1 on one squarefree support."""
    if cutoff < 1 or len(set(support)) != len(support):
        raise ValueError("use a positive cutoff and a squarefree labelled support")
    size = len(support)
    truncated_mobius_sum = 0
    for mask in range(1 << size):
        if subset_product(support, mask) <= cutoff:
            truncated_mobius_sum += -1 if mask.bit_count() % 2 else 1
    return (1 if size == 0 else 0) - truncated_mobius_sum


def boolean_b(support: tuple[int, ...], cutoff: int) -> int:
    """The coefficient b_U=a_U star a_U star mu_sf by labelled partitions."""
    if len(set(support)) != len(support):
        raise ValueError("support must be squarefree")
    total = 0
    size = len(support)
    # State 0 goes to the first a_U factor, 1 to the second, and 2 to mu_sf.
    for states in itertools.product(range(3), repeat=size):
        first = tuple(support[i] for i, state in enumerate(states) if state == 0)
        second = tuple(support[i] for i, state in enumerate(states) if state == 1)
        mobius_size = sum(state == 2 for state in states)
        total += (
            boolean_a(first, cutoff)
            * boolean_a(second, cutoff)
            * (-1) ** mobius_size
        )
    return total


def eligible_count(support: tuple[int, ...]) -> int:
    return sum(prime % 4 == 1 for prime in support)


def l1_majorant_bad_exponent(alpha: float, weight: float = 5.0) -> float:
    if not 0 < alpha < weight / 2:
        raise ValueError("require 0<alpha<weight/2")
    optimizer = 2 * alpha / weight
    return weight / 2 + alpha - alpha * math.log(optimizer)


def l1_majorant_saving(alpha: float, weight: float = 5.0) -> float:
    return weight - l1_majorant_bad_exponent(alpha, weight)


def exact_shell_panel() -> dict[str, object]:
    left_support = ROUGH_PRIMES[:2]
    right_support = ROUGH_PRIMES[2:]
    left_core = math.prod(left_support)
    right_core = math.prod(right_support)
    left_physical = OWNER_LEFT * left_core**2
    right_physical = OWNER_RIGHT * right_core**2
    horizon = math.ceil(max(left_physical, right_physical) / 8)
    cutoff = math.floor(horizon ** (1 / 6))
    if not all(prime > cutoff for prime in ROUGH_PRIMES):
        raise AssertionError("fixture is not in the rough Boolean sector")
    return {
        "owners": [OWNER_LEFT, OWNER_RIGHT],
        "core_supports": [list(left_support), list(right_support)],
        "cores": [left_core, right_core],
        "physical_products": [left_physical, right_physical],
        "horizon": horizon,
        "boolean_cutoff": cutoff,
        "ratio_eight_shell_multipliers": [
            f"{left_physical / horizon:.12f}",
            f"{right_physical / horizon:.12f}",
        ],
        "eligible_counts": [eligible_count(left_support), eligible_count(right_support)],
        "boolean_coefficients": [
            boolean_b(left_support, cutoff),
            boolean_b(right_support, cutoff),
        ],
    }


def run() -> dict[str, object]:
    alpha = 0.274064461784
    rough_formula = []
    replay_primes = (103, 107, 127, 131, 139, 151, 163, 167)
    for size in range(1, len(replay_primes) + 1):
        support = replay_primes[:size]
        rough_formula.append(
            {
                "support_size": size,
                "computed_b_U": boolean_b(support, 39),
                "formula_1_plus_minus_1_to_k": 1 + (-1) ** size,
            }
        )
    return {
        "frozen_boolean_source": {
            "coefficient": "b_U=a_U star a_U star mu_sf",
            "uniform_pointwise_majorant": "abs(b_U(n))<=5^omega(n)",
            "rough_support_formula": "b_U(S)=1+(-1)^|S| if every p in S exceeds U",
        },
        "exact_clean_shell_counterfixture": exact_shell_panel(),
        "weighted_rankin_majorant": {
            "alpha": alpha,
            "bad_l1_log_exponent": f"{l1_majorant_bad_exponent(alpha):.12f}",
            "full_l1_log_exponent": "5",
            "relative_log_saving": f"{l1_majorant_saving(alpha):.12f}",
            "scope": "Boolean coefficient majorant only; not the full physical FFPS source",
        },
        "rough_formula_panels": rough_formula,
        "resource_caps": {
            "maximum_support_size": len(replay_primes),
            "maximum_labelled_partitions": 3 ** len(replay_primes),
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
