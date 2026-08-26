#!/usr/bin/env python3
"""Bounded replay for the scalable rich-core block source tower."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

MAX_BLOCKS = 8
ELIGIBLE_PRIMES = (5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113, 137, 149)


def block_leverage(left_prime: int, right_prime: int) -> Fraction:
    if (
        left_prime not in ELIGIBLE_PRIMES
        or right_prime not in ELIGIBLE_PRIMES
        or left_prime == right_prime
    ):
        raise ValueError("use two distinct replay primes congruent to one modulo four")
    return Fraction(
        4 * (left_prime - 1) * (right_prime - 1),
        5 * left_prime * right_prime + left_prime + right_prime + 1,
    )


def tower_panel(blocks: int) -> dict[str, object]:
    if (
        isinstance(blocks, bool)
        or not isinstance(blocks, int)
        or not 1 <= blocks <= MAX_BLOCKS
    ):
        raise ValueError("blocks is outside the replay range")
    pairs = [
        (ELIGIBLE_PRIMES[2 * index], ELIGIBLE_PRIMES[2 * index + 1])
        for index in range(blocks)
    ]
    factors = [block_leverage(left, right) for left, right in pairs]
    joint = math.prod(factors, start=Fraction(1))
    principal_weight = math.prod(
        (Fraction(prime + 1, prime - 1) for pair in pairs for prime in pair),
        start=Fraction(1),
    )
    return {
        "blocks": blocks,
        "phase_coordinates": 2 * blocks,
        "selected_modes": 2**blocks - 1,
        "cross_pairs": [list(pair) for pair in pairs],
        "leverage_factors": [str(factor) for factor in factors],
        "joint_leverage": str(joint),
        "uniform_upper_bound": str(Fraction(4, 5) ** blocks),
        "all_blocks_contract": all(factor < Fraction(4, 5) for factor in factors),
        "principal_local_weight_product": str(principal_weight),
    }


def density_exponent(alpha: float) -> float:
    if not 0 < alpha < 0.5:
        raise ValueError("alpha must lie strictly between zero and one half")
    return 0.5 - alpha + alpha * math.log(2 * alpha)


def leverage_exponent(alpha: float) -> float:
    if not 0 < alpha < 0.5:
        raise ValueError("alpha must lie strictly between zero and one half")
    return alpha * math.log(5 / 4)


def balanced_alpha() -> float:
    lower = 1e-9
    upper = 0.5 - 1e-9
    for _ in range(80):
        middle = (lower + upper) / 2
        if density_exponent(middle) > leverage_exponent(middle):
            lower = middle
        else:
            upper = middle
    return (lower + upper) / 2


def run() -> dict[str, object]:
    alpha_rows = []
    for numerator in (1, 2, 3, 4):
        alpha = numerator / 10
        alpha_rows.append(
            {
                "alpha": f"{alpha:.1f}",
                "bad_core_log_exponent": f"{density_exponent(alpha):.12f}",
                "leverage_log_exponent": f"{leverage_exponent(alpha):.12f}",
            }
        )
    optimum = balanced_alpha()
    return {
        "all_rank_source": {
            "rich_condition": "omega_1(c),omega_1(d)>=r",
            "canonical_phase_primes": "the first r divisors 1 mod 4 on each side",
            "phase_identity": "(-1)^(2r)=1",
            "quotient": "C2^r",
            "every_nonprincipal_quotient_mode": "contains a nonprincipal phase on both source sides",
        },
        "exact_leverage": {
            "block_factor": "4*(p-1)*(q-1)/(5*p*q+p+q+1)<4/5",
            "tower_bound": "L_r<(4/5)^r",
            "panels": [tower_panel(blocks) for blocks in (1, 2, 3, 5, 8)],
        },
        "ambient_growing_rank_frontier": {
            "rank": "r=floor(alpha*log log x), 0<alpha<1/2",
            "bad_relative_log_weight": "(log x)^(-c(alpha)+o(1))",
            "c_alpha": "1/2-alpha+alpha*log(2*alpha)",
            "leverage": "(log x)^(-alpha*log(5/4)+o(1))",
            "panels": alpha_rows,
            "balanced_alpha": f"{optimum:.12f}",
            "balanced_exponent": f"{density_exponent(optimum):.12f}",
            "scope": "ambient squarefree cores and formal Gram only",
        },
        "complexity_ledger": {
            "selected_mode_count": "2^r-1",
            "equal_degree_path_average_betti": "e*r-2+e*r/(2^r-1)",
            "equal_degree_path_average_energy_rank": (
                "e^2*r^2+(e^2-4e)*r+4+O_e(r^2*2^-r)"
            ),
            "growing_rank_consequence": (
                "O_e((log log x)^2) only for fixed equal place degree e"
            ),
            "status": (
                "separate fixed-degree path model, not a native varying-place complex"
            ),
        },
        "conditional_principal_atomic_ledger": {
            "local_weight": "C_r=product_(selected p) (p+1)/(p-1)",
            "uniform_growth": "C_r=O(log(2r)) for 2r distinct primes 1 mod 4",
            "weighted_atom": "at most C_r/(g^2*c*d*P*Q)",
            "condition": (
                "uses the natural generalized source-dual weight g^2*product(p)"
            ),
        },
        "resource_caps": {
            "maximum_blocks": MAX_BLOCKS,
            "prime_panels": len(ELIGIBLE_PRIMES),
            "bisection_steps": 80,
            "source_atoms_enumerated": 0,
            "conductors_enumerated": 0,
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
