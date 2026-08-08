#!/usr/bin/env python3
"""Exact finite replay for L-26901 and R-26901.

Only Python's standard library is used.  Every arithmetic/sign check is exact.
The finite replay is regression evidence for the identities; the all-order
proofs are in the accompanying claim files.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path


LIMIT_N = 160
LIMIT_M = 30
EXPECTED_SHA256 = "b2ff53b948da65a81082fa9a14d7f990c227bb47a6bb592458655ccec7a03f95"


def mobius_table(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if n * p > limit:
                break
            composite[n * p] = True
            if n % p == 0:
                mu[n * p] = 0
                break
            mu[n * p] = -mu[n]
    return mu


MU = mobius_table(4 * LIMIT_N + 10)


def b2(n: int) -> int:
    return MU[n] - (MU[n // 2] if n % 2 == 0 else 0)


def omega2(n: int) -> Fraction:
    return Fraction(b2(n)) - Fraction(1, 2) * (
        b2(n // 2) if n % 2 == 0 else 0
    )


def carry(n: int, q: int, j: int) -> int:
    return n // q - j // q - (n - j) // q


def box(x: int, a: int) -> int:
    return int(a <= x < 2 * a)


def wavelet_value(x: int, m: int) -> Fraction:
    return Fraction(box(x, m)) - Fraction(box(x, 2 * m), 2)


def binary_level_count(x: int) -> int:
    return 0 if x <= 0 else x.bit_length()


def check_scaled_profiles() -> tuple[dict[str, int], dict[str, int], dict[str, int]]:
    scaled_cases = 0
    wavelet_cases = 0
    sign_cases = 0
    for n in range(1, LIMIT_N + 1):
        for m in range(1, min(LIMIT_M, n) + 1):
            for j in range(n + 1):
                lhs = sum(
                    Fraction(b2(k)) * carry(n, m * k, j)
                    for k in range(1, n // m + 1)
                )
                rhs = box(n, m) - box(j, m) - box(n - j, m)
                assert lhs == rhs, ("scaled b2", n, m, j, lhs, rhs)
                scaled_cases += 1

                lhs_wavelet = sum(
                    omega2(k) * carry(n, m * k, j)
                    for k in range(1, n // m + 1)
                )
                rhs_wavelet = (
                    wavelet_value(n, m)
                    - wavelet_value(j, m)
                    - wavelet_value(n - j, m)
                )
                assert lhs_wavelet == rhs_wavelet, (
                    "omega2 wavelet",
                    n,
                    m,
                    j,
                    lhs_wavelet,
                    rhs_wavelet,
                )
                wavelet_cases += 1

                if m <= n < 2 * m:
                    assert rhs_wavelet >= 0, ("inner sign", n, m, j, rhs_wavelet)
                    sign_cases += 1
                if 2 * m <= n < 4 * m:
                    assert rhs_wavelet <= 0, ("outer sign", n, m, j, rhs_wavelet)
                    sign_cases += 1

    return (
        {"cases": scaled_cases},
        {"cases": wavelet_cases},
        {"cases": sign_cases},
    )


def check_factor_five_kummer() -> tuple[dict[str, int], dict[str, int]]:
    far_cases = 0
    transition_negative = 0
    for m in range(1, LIMIT_M + 1):
        for n in range(4 * m, LIMIT_N + 1):
            numerator = math.prod(math.comb(n, j) for j in range(2 * m, 4 * m))
            denominator = math.prod(
                math.comb(n, j) ** 2 for j in range(m, 2 * m)
            )
            if n >= 5 * m:
                assert numerator >= denominator, ("factor five", n, m)
                far_cases += 1
            elif numerator < denominator:
                transition_negative += 1
    return {"cases": far_cases}, {"count": transition_negative}


def check_far_increment() -> dict[str, int]:
    cases = 0
    for m in range(1, LIMIT_M + 1):
        for n in range(4 * m, LIMIT_N):
            endpoint = n + 1
            numerator = 1
            denominator = 1
            for r in range(m):
                numerator *= (endpoint - m - r) ** 2
                denominator *= (endpoint - 2 * m - r) * (
                    endpoint - 3 * m - r
                )
            assert numerator > denominator, ("increment", n, m)
            cases += 1
    return {"cases": cases}


def check_factor_five_base() -> dict[str, int]:
    cases = 0
    for m in range(1, LIMIT_M + 1):
        n = 5 * m
        numerator = math.prod(math.comb(n, j) for j in range(2 * m, 4 * m))
        denominator = math.prod(
            math.comb(n, j) ** 2 for j in range(m, 2 * m)
        )
        assert numerator >= denominator, ("base product", m)
        for r in range(m):
            assert math.comb(n, 2 * m + r) >= math.comb(n, m + r), (
                "base pairing",
                m,
                r,
            )
        assert math.comb(n, 2 * m) >= math.comb(n, m)
        cases += 1
    return {"cases": cases}


def check_odd_mobius_carry() -> tuple[dict[str, int], dict[str, int], dict[str, int]]:
    prefix_cases = 0
    pointwise_cases = 0
    average_cases = 0

    for x in range(LIMIT_N + 1):
        lhs = sum(MU[q] * (x // q) for q in range(1, x + 1, 2))
        rhs = binary_level_count(x)
        assert lhs == rhs, ("odd prefix", x, lhs, rhs)
        prefix_cases += 1

    for n in range(1, LIMIT_N + 1):
        level = n.bit_length() - 1
        expected_average = Fraction(-(level + 1)) + Fraction(
            2 * (2 ** (level + 1) - 1), n + 1
        )
        actual_average = sum(
            Fraction(MU[q])
            * Fraction(sum(carry(n, q, j) for j in range(n + 1)), n + 1)
            for q in range(1, n + 1, 2)
        )
        assert actual_average == expected_average, (
            "odd average",
            n,
            actual_average,
            expected_average,
        )
        average_cases += 1

        for j in range(n + 1):
            lhs = sum(MU[q] * carry(n, q, j) for q in range(1, n + 1, 2))
            rhs = (
                binary_level_count(n)
                - binary_level_count(j)
                - binary_level_count(n - j)
            )
            assert lhs == rhs, ("odd pointwise", n, j, lhs, rhs)
            pointwise_cases += 1

    return (
        {"cases": prefix_cases},
        {"cases": pointwise_cases},
        {"cases": average_cases},
    )


def build_result() -> dict[str, object]:
    scaled, wavelet, signs = check_scaled_profiles()
    far, transition = check_factor_five_kummer()
    odd_prefix, odd_pointwise, odd_average = check_odd_mobius_carry()
    return {
        "schema": "X-26901-pointwise-dyadic-dipole-v1",
        "checks": {
            "scaled_b2_box_profile": scaled,
            "pointwise_omega2_wavelet": wavelet,
            "pointwise_sign_bands": signs,
            "factor_five_kummer_nonnegativity": far,
            "transition_negative_examples": transition,
            "far_field_increment_product": check_far_increment(),
            "factor_five_base_pairing": check_factor_five_base(),
            "odd_mobius_prefix": odd_prefix,
            "odd_pointwise_carry": odd_pointwise,
            "odd_average_carry": odd_average,
        },
        "scope": (
            "exact finite algebra/regression only; does not prove finite "
            "transition contraction, DSS, or RH"
        ),
    }


def main() -> None:
    result = build_result()
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    if digest != EXPECTED_SHA256:
        raise AssertionError(("proof-object digest mismatch", digest, EXPECTED_SHA256))
    result["sha256_without_digest"] = digest
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    path = Path(__file__).with_name("results") / "factor-five-verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
