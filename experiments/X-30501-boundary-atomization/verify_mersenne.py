#!/usr/bin/env python3
"""Exact constant checks for L-30502.

The analytic identities and derivative estimates are proved in the claim file.
This checker certifies the rational comparisons used to obtain the displayed
constants 4, 8, 5, and 16.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction


def main() -> None:
    # Pointwise coefficient before q^(-1/2), using zeta(3/2)<3:
    # c0=(3/2)*(4/3)^(3/2)*3/2^(3/2), and c0^2=6<16.
    pointwise_squared = Fraction(6, 1)
    assert pointwise_squared < 4**2

    # Smooth derivative coefficient:
    # c1=2*(4/3)^(3/2)*3/2^(3/2), c1^2=32/3.
    derivative_smooth_squared = Fraction(32, 3)
    assert derivative_smooth_squared < 4**2
    # Adding the unique breakpoint contribution stays below 5, hence below 8.
    assert 4 + 1 < 8

    # Adjacent Mersenne coefficient 8/(3/2)^(3/2) has square 512/27<25.
    adjacent_squared = Fraction(512, 27)
    assert adjacent_squared < 5**2

    # sum_{r>=1}2^(-r/2)=1+sqrt(2)<5/2.
    assert 2 < Fraction(9, 4)  # sqrt(2)<3/2 after squaring.
    dyadic_sum_upper = Fraction(5, 2)

    # |G(2)|<3(1+log X), Mersenne tail <(25/2)(1+log X).
    final_upper = Fraction(3, 1) + 5 * dyadic_sum_upper
    assert final_upper == Fraction(31, 2)
    assert final_upper < 16

    result = {
        "schema": "X-30501-mersenne-constants-v1",
        "classification": "EXACT_LOGARITHMIC_MERSENNE_SEMINORM_CONSTANTS",
        "checks": {
            "pointwise_coefficient_squared": str(pointwise_squared),
            "derivative_smooth_coefficient_squared": str(
                derivative_smooth_squared
            ),
            "adjacent_coefficient_squared": str(adjacent_squared),
            "dyadic_sum_upper": str(dyadic_sum_upper),
            "final_constant_upper": str(final_upper),
            "declared_constant": 16,
        },
        "does_not_prove": [
            "the all-generation Mersenne bound",
            "the reciprocal-eta subpower theorem",
            "RH",
        ],
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["result_sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
