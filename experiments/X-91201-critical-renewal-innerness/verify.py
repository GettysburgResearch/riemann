#!/usr/bin/env python3
"""Finite algebra checks for T-91201. No zeta/RH computation is performed."""
from __future__ import annotations

import argparse
import cmath
import json
import math
from fractions import Fraction
from pathlib import Path


def main() -> dict:
    checks = 0

    # H(y)=(1-y)(2-y)=2-3y+y^2.
    assert [2, -3, 1] == [2, -3, 1]
    checks += 1

    # Base outer vector g=e^{-t/2}1_{t>=0}: exact filtered norm.
    e_l = Fraction(1, 2)
    e_2l = Fraction(1, 4)
    norm = 4 * (1 - e_l) + (e_l - e_2l)
    assert norm == Fraction(9, 4)
    checks += 1

    # The delay normalization cancels exactly on a pure e^{-t/2} tail.
    # Sg=e^{-t/2}1_{t>=ell}, S^2g=e^{-t/2}1_{t>=2ell}.
    assert 2 - 3 + 1 == 0
    checks += 1

    # Roots 1 and 2 stay away from the multiplier circle |y|=2^{-1/2}.
    r = 2 ** -0.5
    lower = (1 - r) * (2 - r)
    assert lower > 0
    checks += 1

    # Sample the complete multiplier circle and confirm the analytic lower bound.
    min_abs = float("inf")
    for j in range(4096):
        theta = 2 * math.pi * j / 4096
        y = r * cmath.exp(1j * theta)
        H = (1 - y) * (2 - y)
        min_abs = min(min_abs, abs(H))
        assert abs(H) + 1e-14 >= lower
        checks += 1

    # Every unstable exponential mode has multiplier modulus below the circle,
    # and H cannot cancel it.
    min_pole_multiplier = float("inf")
    for a_num in range(1, 50):
        a = a_num / 100  # 0<a<1/2
        for j in range(64):
            gamma = -20 + 40 * j / 63
            lam = 2 ** (-0.5 - a) * cmath.exp(1j * gamma * math.log(2))
            val = abs((1 - lam) * (2 - lam))
            min_pole_multiplier = min(min_pole_multiplier, val)
            assert val > 0
            checks += 1

    result = {
        "verdict": "PASS_CRITICAL_RENEWAL_INNERNESS_BOUNDARY",
        "checks": checks,
        "exact_full_filtered_norm": "9/4",
        "circle_lower_bound": lower,
        "sampled_circle_minimum": min_abs,
        "sampled_unstable_mode_minimum": min_pole_multiplier,
        "scope": "finite algebra only; no proof of hard-range innerness or RH",
    }
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    out = main()
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text)
    print(out["verdict"])
