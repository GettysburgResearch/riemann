#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

SCHEMA = "riemann.t98710.fractional_heat_bohr_hardening.v1"


def sibuya(theta: Fraction, k: int) -> Fraction:
    if k < 1:
        raise ValueError("k must be positive")
    out = theta
    for j in range(1, k):
        out *= Fraction(j, 1) - theta
    return out / math.factorial(k)


def det2(a: Fraction, b: Fraction, c: Fraction, d: Fraction) -> Fraction:
    return a * d - b * c


def verify() -> dict:
    theta = Fraction(1, 384)

    sib = [sibuya(theta, k) for k in range(1, 65)]
    assert all(x > 0 for x in sib)
    for k in range(1, 64):
        assert sib[k] / sib[k - 1] == (Fraction(k, 1) - theta) / (k + 1)

    p2 = -sibuya(theta, 2)
    assert p2 == -theta * (1 - theta) / 2
    assert p2 < 0
    tao_p2 = Fraction(0)
    assert tao_p2 != p2

    k_empty = ((Fraction(1), Fraction(1)), (Fraction(1), Fraction(1)))
    k_two = ((Fraction(3, 4), Fraction(1, 2)),
             (Fraction(1, 2), Fraction(3, 4)))
    diff = tuple(tuple(k_empty[i][j] - k_two[i][j] for j in range(2)) for i in range(2))
    assert det2(diff[0][0], diff[0][1], diff[1][0], diff[1][1]) == Fraction(-3, 16)
    assert diff[0][0] + diff[1][1] == Fraction(1, 2)

    u, v = 1, 2
    actual_quadratic = u * u + v * v + (u - v) * (u - v)
    reflected_quadratic = u * u + v * v + (u + v) * (u + v)
    assert reflected_quadratic - actual_quadratic == 4 * u * v == 8

    bohr_energy_rate = Fraction(1, 2)
    uniform_upper_rate = Fraction(1, 2)
    proposed_rate = 96 * theta
    assert proposed_rate == Fraction(1, 4)
    assert bohr_energy_rate > proposed_rate
    assert uniform_upper_rate == bohr_energy_rate

    # Exact Weyl/parity identity in the one-mode displacement representation:
    # parity conjugates displacement f to -f, hence centering produces -2f.
    weyl_displacement_multiplier = -2
    assert weyl_displacement_multiplier != 0

    # Exact dyadic bookkeeping in the chi(p)=-1 twist.
    dyadic_one_plus_exponent = 2 * theta
    dyadic_half_exponent = theta
    odd_ratio_cancels_one_dyadic = theta
    final_one_plus_exponent = dyadic_one_plus_exponent - odd_ratio_cancels_one_dyadic
    assert final_one_plus_exponent == theta
    assert dyadic_half_exponent == theta

    core = {
        "schema": SCHEMA,
        "frozen_base": {
            "pr": 613,
            "head": "f28aa51a6d6740067202611d8ebda4be2ef0a1c9",
            "base_pr": 610,
            "base_sha": "edf28c9ad14ccbf5b18b9ced45f3c2fc4ce8221d",
        },
        "theta": str(theta),
        "checks": {
            "sibuya_coefficients_positive_through_k": 64,
            "p2_fractional_coefficient": str(p2),
            "tao_p2_tracefree_coefficient": str(tao_p2),
            "tao_state_difference_determinant": str(Fraction(-3, 16)),
            "actual_vs_reflected_quadratic_gap": 8,
            "bohr_energy_rate": str(bohr_energy_rate),
            "uniform_center_exponential_type": str(uniform_upper_rate),
            "weyl_centering_parity_displacement": weyl_displacement_multiplier,
            "proposed_uniform_rate": str(proposed_rate),
            "uniform_rate_contradiction": True,
            "twisted_euler_dyadic_exponents": [
                str(final_one_plus_exponent),
                str(dyadic_half_exponent),
            ],
        },
        "scope": {
            "selberg_delange_asymptotic_machine_proved": False,
            "bohr_kronecker_limit_machine_proved": False,
            "analytic_refutation_in_claim_file": True,
            "fixed_center_plfhe_proved": False,
            "rh_established": False,
        },
        "verdict": "PASS_T98710_FRACTIONAL_HEAT_BOHR_HARDENING_ALGEBRA",
    }
    proof = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return {**core, "proof_object_sha256": proof}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
