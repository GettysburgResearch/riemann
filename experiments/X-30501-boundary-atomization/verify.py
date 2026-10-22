#!/usr/bin/env python3
"""Exact regression for the stopped-boundary atomic-norm lower bound.

Standard-library only. The checker verifies the rational inequalities and
integer band geometry used in L-30501/R-30501. It does not evaluate zeta,
Cycle Debt, or RH.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction


def top_band(endpoint: int) -> range:
    return range(endpoint // 3 + 1, (2 * endpoint) // 5 + 1)


def verify_rational_moat() -> dict[str, str]:
    # 9/16 < 1/sqrt(3).
    assert 3 * 9**2 < 16**2

    # Integral-test bound:
    # sum_{k>=2} (2k)^(-3/2) <= 5/8.
    inverse_power_tail = Fraction(5, 8)
    unshifted_difference_tail = inverse_power_tail / 2
    assert unshifted_difference_tail == Fraction(5, 16)

    # For m>=64 the shifted-even correction is at most 5/(8m).
    shift_error_at_64 = Fraction(5, 8 * 64)
    assert shift_error_at_64 < Fraction(1, 100)

    scaled_boundary_upper = (
        -Fraction(9, 16)
        + unshifted_difference_tail
        + shift_error_at_64
    )
    assert scaled_boundary_upper == -Fraction(123, 512)
    assert scaled_boundary_upper < -Fraction(1, 5)

    # log(5/4) > (1/4)/(5/4) = 1/5.
    logarithm_lower = Fraction(1, 5)
    weighted_node_moat = Fraction(1, 5) * logarithm_lower
    assert weighted_node_moat == Fraction(1, 25)

    return {
        "sum_2k_power_tail_upper": str(inverse_power_tail),
        "unshifted_difference_tail_upper": str(unshifted_difference_tail),
        "shift_error_m64_upper": str(shift_error_at_64),
        "scaled_boundary_upper": str(scaled_boundary_upper),
        "weighted_layer_node_moat": str(weighted_node_moat),
    }


def verify_band_geometry(limit: int = 4096) -> dict[str, int]:
    endpoint_cases = 0
    node_cases = 0
    stopped_endpoint_cases = 0

    for X in range(192, limit + 1):
        nodes = list(top_band(X))
        assert len(nodes) >= Fraction(X, 30)
        for m in nodes:
            assert m >= 64
            assert 3 * m > X
            assert 5 * m <= 2 * X

            # Endpoints below 2m do not contain source node m.
            for Y in (max(2, 2 * m - 2), 2 * m - 1):
                if Y >= 2:
                    assert Y // 2 < m

            # The two extreme endpoints imply the same inequalities for every
            # Y in [2m,X-1].
            if 2 * m <= X - 1:
                for Y in (2 * m, X - 1):
                    assert 3 * m > Y
                    assert 2 * m <= Y
                    source_support = Y // 2
                    assert m <= source_support
                    assert 2 * m > source_support
                    stopped_endpoint_cases += 1
            node_cases += 1
        endpoint_cases += 1

    return {
        "endpoint_cases": endpoint_cases,
        "top_band_node_cases": node_cases,
        "stopped_endpoint_geometry_cases": stopped_endpoint_cases,
        "limit_endpoint": limit,
    }


def verify_linear_count(limit: int = 100000) -> dict[str, str | int]:
    cases = 0
    weakest_scaled_count = None
    weakest_endpoint = None
    for X in range(192, limit + 1):
        count = len(list(top_band(X)))
        assert count >= Fraction(X, 30)
        atomic_lower = Fraction(count, 25)
        assert atomic_lower >= Fraction(X, 750)
        ratio = Fraction(count, X)
        if weakest_scaled_count is None or ratio < weakest_scaled_count:
            weakest_scaled_count = ratio
            weakest_endpoint = X
        cases += 1
    assert weakest_scaled_count is not None
    return {
        "cases": cases,
        "limit_endpoint": limit,
        "weakest_count_over_X": str(weakest_scaled_count),
        "weakest_endpoint": int(weakest_endpoint),
        "proved_atomic_lower": "X/750",
    }


def verify_source_type_mutation() -> dict[str, str]:
    # The raw boundary coefficient and divided eta-fiber coefficient are
    # different source types. An s=2 control makes this rational.
    k = 2
    q = 3
    raw_even = Fraction(1, (2 * k * q - 1) ** 2)
    divided_even = raw_even / (2 * k)
    assert raw_even == Fraction(1, 121)
    assert divided_even == Fraction(1, 484)
    assert raw_even != divided_even
    return {
        "raw_even_control": str(raw_even),
        "divided_even_control": str(divided_even),
        "verdict": "SOURCE_NORMALIZATION_MISMATCH_REJECTED",
    }


def main() -> None:
    result = {
        "schema": "X-30501-boundary-atomization-v1",
        "classification": (
            "EXACT_LINEAR_CRITICAL_BOUNDARY_ATOMIC_NORM_LOWER_BOUND"
        ),
        "checks": {
            "rational_moat": verify_rational_moat(),
            "band_geometry": verify_band_geometry(),
            "linear_count": verify_linear_count(),
            "source_type_mutation": verify_source_type_mutation(),
        },
        "does_not_prove": [
            "a linear lower bound for optimized Cycle Debt",
            "impossibility of structured pre-atomization recombination",
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
