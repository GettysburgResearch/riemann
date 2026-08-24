#!/usr/bin/env python3
"""Exact finite checks for L/T-106410.

This replay verifies the rational constants and exhaustive rational-grid
instances of the two channel inequalities.  It does not prove the cofinal bank
adapter or any Xi zero percentage.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def verify_grid() -> int:
    c = Fraction(1, 200)
    checks = 0
    # Scale L to one.  Test every rational u,v on a 1/120 grid.
    for iu in range(121):
        for iv in range(121):
            u = Fraction(iu, 120)
            v = Fraction(iv, 120)

            # Reflected channel.
            a_cross = (
                (1 - c * u) * v * v * (1 - c * v)
                + (1 + c * v) * u * u * (1 + c * u)
            )
            r_cross = 2 * c * (u + v) ** 2 * abs(u - v)
            assert a_cross >= 0
            assert r_cross * (1 - c) ** 2 <= 4 * c * a_cross
            checks += 1

            # Same-sign source at xi=u+v.  The pointwise proof after
            # integration uses |u-v|<=u+v and the symmetric second moment.
            xi = u + v
            r_same = c * xi * (u - v) ** 2
            a_same_pair = (
                (1 - c * u) * v * v * (1 + c * v)
                + (1 - c * v) * u * u * (1 + c * u)
            ) / 2
            assert a_same_pair >= 0
            # Symmetrized pairwise form of the integrated inequality.
            assert r_same * (1 - c) <= 4 * c * a_same_pair
            checks += 1
    return checks


def payload() -> dict[str, object]:
    checks = verify_grid()

    same_square = Fraction(64, 39601)
    cross_square = Fraction(640000, 1568239201)
    four_channel = 2 * same_square + 2 * cross_square
    assert 39601**2 == 1568239201
    assert four_channel == Fraction(6348928, 1568239201)
    assert four_channel < Fraction(1, 200)

    fixed_order = Fraction(599, 625)
    bandwidth_loss = Fraction(1, 1000)
    sharp_conclusion = (
        fixed_order
        - bandwidth_loss
        - 2 * four_channel * Fraction(999, 1000)
    )
    safe_conclusion = fixed_order - bandwidth_loss - Fraction(999, 100000)
    assert safe_conclusion == Fraction(94741, 100000)
    assert sharp_conclusion > safe_conclusion

    result: dict[str, object] = {
        "schema": "riemann.x106410.small-shift-bank.v1",
        "classification": "PASS_T106410_SMALL_SHIFT_ENDPOINT_BANK_ALGEBRA",
        "rational_grid_checks": checks,
        "same_sign_squared_constant": "64/39601",
        "reflected_squared_constant": "640000/1568239201",
        "four_channel_constant": "6348928/1568239201",
        "four_channel_below_one_over_200": True,
        "safe_conditional_fraction": "94741/100000",
        "safe_conditional_decimal": "0.94741",
        "sharp_conditional_decimal": f"{float(sharp_conclusion):.12f}",
        "endpointbank106410_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = payload()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
