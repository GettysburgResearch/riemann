#!/usr/bin/env python3
"""Exact replay for the four-phase rich-core FFPS source candidate."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

MAX_PRIME = 10_000


def is_prime(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return value == divisor
        divisor += 1
    return True


def eligible_prime(value: int) -> bool:
    return is_prime(value) and value % 4 == 1 and value <= MAX_PRIME


def block_leverage(left_prime: int, right_prime: int) -> Fraction:
    if not eligible_prime(left_prime) or not eligible_prime(right_prime):
        raise ValueError("block primes must be primes congruent to one modulo four")
    numerator = 4 * (left_prime - 1) * (right_prime - 1)
    denominator = 5 * left_prime * right_prime + left_prime + right_prime + 1
    return Fraction(numerator, denominator)


def four_phase_panel(primes: tuple[int, int, int, int]) -> dict[str, object]:
    if len(set(primes)) != 4:
        raise ValueError("the four source phase primes must be distinct")
    ell_1, rho_1, ell_2, rho_2 = primes
    first = block_leverage(ell_1, rho_1)
    second = block_leverage(ell_2, rho_2)
    return {
        "phase_primes": list(primes),
        "cross_blocks": [[ell_1, rho_1], [ell_2, rho_2]],
        "block_leverages": [str(first), str(second)],
        "joint_leverage": str(first * second),
        "strict_contraction": first < 1 and second < 1,
    }


def run() -> dict[str, object]:
    modes = {
        "tau_1": ["Y_mod_ell_1", "X_mod_rho_1"],
        "tau_2": ["Y_mod_ell_2", "X_mod_rho_2"],
        "tau_1_tau_2": [
            "Y_mod_ell_1",
            "X_mod_rho_1",
            "Y_mod_ell_2",
            "X_mod_rho_2",
        ],
    }
    return {
        "source_partition": {
            "left_core_condition": "at least two distinct prime divisors 1 mod 4",
            "right_core_condition": "at least two distinct prime divisors 1 mod 4",
            "canonical_choice": "the two least eligible divisors on each side",
            "nonzero_phase_source": (
                "squarefree a=g*c,b=g*d with gcd(g,c*d)=gcd(c,d)=1 and "
                "gcd(c,Q)=gcd(d,P)=1"
            ),
            "owner_sector_splits": [
                "kappa_ell_i(Q)=sigma_i",
                "kappa_rho_i(P)=tau_i",
            ],
            "phase_identity": "(-1)^4=1",
            "physical_coordinates": [
                "Y=Q*d^2 mod ell_1",
                "X=P*c^2 mod rho_1",
                "Y=Q*d^2 mod ell_2",
                "X=P*c^2 mod rho_2",
            ],
        },
        "quotient": {
            "group": "C2^2",
            "nonprincipal_modes": modes,
            "every_mode_is_bilateral": all(
                any(label.startswith("X_") for label in support)
                and any(label.startswith("Y_") for label in support)
                for support in modes.values()
            ),
        },
        "leverage_identity": {
            "two_prime_block": "4*(p-1)*(q-1)/(5*p*q+p+q+1)",
            "strict_gap_numerator": "p*q+5*p+5*q-3",
            "panels": [
                four_phase_panel((5, 13, 17, 29)),
                four_phase_panel((13, 17, 29, 37)),
                four_phase_panel((17, 29, 37, 41)),
            ],
        },
        "ambient_density": {
            "bad_log_weight": "O((log x)^(1/2)*log log x)",
            "all_log_weight": "log x+O(1)",
            "bad_relative_weight": "O(log log x/(log x)^(1/2))",
            "scope": "ambient reduced cores only; not an FFPS source-mass theorem",
        },
        "resource_caps": {
            "maximum_prime_checked": MAX_PRIME,
            "prime_panels": 12,
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
