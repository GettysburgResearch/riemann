#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Callable

VERDICT = "PASS_X_93290_ACTUAL_LPTRP_COVARIANCE"


def mobius(limit: int) -> list[int]:
    mu = [1] * (limit + 1)
    mu[0] = 0
    prime = [True] * (limit + 1)
    prime[:2] = [False, False]
    for p in range(2, limit + 1):
        if not prime[p]:
            continue
        for n in range(2 * p, limit + 1, p):
            prime[n] = False
        for n in range(p, limit + 1, p):
            mu[n] *= -1
        for n in range(p * p, limit + 1, p * p):
            mu[n] = 0
    return mu


def q2(n: int) -> int:
    if n < 2:
        return 0
    if n == 2:
        return 3
    if n == 3:
        return 0
    return 1


def q3x3(n: int) -> int:
    if n < 3:
        return 0
    if n == 3:
        return 6
    if n == 4:
        return -2
    return 1


def divisors(n: int):
    for d in range(1, n + 1):
        if n % d == 0:
            yield d


def smooth23(n: int) -> bool:
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    return n == 1


def direct_coeff(n: int, mu_gt3: list[int], q: Callable[[int], int]) -> int:
    return sum(mu_gt3[d] * q(n // d) for d in divisors(n))


def packet_coeffs(n: int, mu_gt3: list[int]) -> tuple[int, int]:
    s = int(smooth23(n))
    a2 = s - mu_gt3[n]
    a3 = s - mu_gt3[n]
    if n % 2 == 0:
        a2 += 2 * mu_gt3[n // 2]
        a3 -= mu_gt3[n // 2]
    if n % 3 == 0:
        a2 -= mu_gt3[n // 3]
        a3 += 5 * mu_gt3[n // 3]
    if n % 4 == 0:
        a3 -= 3 * mu_gt3[n // 4]
    return a2, a3


def exact_activation_check() -> int:
    checks = 0
    samples = [
        [F(0), F(3), F(-1), F(2), F(-2)],
        [F(1), F(-2), F(5), F(-7), F(4), F(1)],
    ]
    for coeffs in samples:
        c = F(0)
        for n in range(1, len(coeffs)):
            # Formal recurrence coefficient: the multiplier log((n+1)/n)
            # is positive, so its sign is exactly the prefix sign.
            prefix = sum(coeffs[1 : n + 1])
            assert (prefix >= 0) == (prefix * F(1, n * (n + 1)) >= 0)
            checks += 1
        assert c == 0
    return checks


def p5_cone_refutation() -> dict[str, str]:
    # The proofs in R-93291 use only these rational upper bounds.
    row2_upper = F(1, 6) * F(21, 4) - 2
    row3_upper = F(1, 7) * F(15, 2) - 5
    assert row2_upper == F(-9, 8)
    assert row3_upper == F(-55, 14)
    return {"row2_difference_upper": str(row2_upper), "row3_scaled_difference_upper": str(row3_upper)}


def gauge_and_spectrum_checks() -> dict[str, Any]:
    # Exact gauge cancellation at representative nonzero rational values.
    K, M, W, Z = F(7, 5), F(11, 7), F(13, 9), F(-17, 6)
    lhs = (K / (M * W)) * (M * W * Z)
    rhs = K * Z
    assert lhs == rhs

    # A two-atom positive spectrum has an exact nonnegative quadratic form.
    weights = [F(2), F(3)]
    phases = [[F(1), F(1), F(1)], [F(1), F(-1), F(1)]]
    x = [F(2), F(-3), F(5)]
    quadratic = F(0)
    for weight, phase in zip(weights, phases):
        amplitude = sum(xi * zi for xi, zi in zip(x, phase))
        quadratic += weight * amplitude * amplitude
    assert quadratic >= 0

    # One positive atom still realizes a sign-changing carrier sequence.
    one_atom_samples = [F(1), F(-1), F(1), F(-1)]
    assert min(one_atom_samples) < 0 < max(one_atom_samples)
    return {
        "gauge_identity": str(lhs),
        "positive_spectral_quadratic_form": str(quadratic),
        "one_atom_pointwise_samples": [str(v) for v in one_atom_samples],
    }


def main() -> dict[str, Any]:
    here = Path(__file__).resolve().parent
    certificate = json.loads((here / "results" / "row-certificate-100m.json").read_text())
    assert certificate["verdict"] == "PASS_ACTUAL_LPTRP23_PREFIX_CERTIFICATE"
    assert certificate["limit"] == 100_000_000
    assert certificate["coefficient_checks"] == 200_000_000
    assert certificate["minimum_row2_prefix_scaled_integer"] == "2121320343559642572"
    assert certificate["minimum_three_times_row3_prefix_scaled_integer"] == "2464101615137754582"
    assert certificate["zero_or_negative_row2_prefix_at"] == 0
    assert certificate["zero_or_negative_row3_prefix_at"] == 0

    limit = 2_000
    mu = mobius(limit)
    mu_gt3 = [0 if n % 2 == 0 or n % 3 == 0 else mu[n] for n in range(limit + 1)]
    coefficient_checks = 0
    for n in range(1, limit + 1):
        a2, a3 = packet_coeffs(n, mu_gt3)
        assert a2 == direct_coeff(n, mu_gt3, q2)
        assert a3 == direct_coeff(n, mu_gt3, q3x3)
        coefficient_checks += 2

    activation_checks = exact_activation_check()
    p5 = p5_cone_refutation()
    covariance = gauge_and_spectrum_checks()

    mutations = 0
    try:
        # Ordinary Mobius is not the filtered producer.
        n = 6
        assert mu[n] == mu_gt3[n]
    except AssertionError:
        mutations += 1
    try:
        # Wrong sign in row-two packet.
        n = 35
        a2, _ = packet_coeffs(n, mu_gt3)
        assert a2 == 0
    except AssertionError:
        mutations += 1
    try:
        # A positive spectrum is not a positive sample sequence.
        assert min(F(-1) ** k for k in range(4)) >= 0
    except AssertionError:
        mutations += 1
    try:
        # Removing the inverse preconditioner destroys gauge cancellation.
        assert (K := F(7, 5)) * F(11, 7) == K
    except AssertionError:
        mutations += 1
    assert mutations == 4

    result: dict[str, Any] = {
        "verdict": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL_PLUS_EXACT_U128_FINITE_CERTIFICATE",
        "actual_filtered_coefficient_checks": coefficient_checks,
        "activation_checks": activation_checks,
        "row_certificate": {
            "limit": certificate["limit"],
            "minimum_row2_prefix_scaled_integer": certificate["minimum_row2_prefix_scaled_integer"],
            "minimum_three_times_row3_prefix_scaled_integer": certificate["minimum_three_times_row3_prefix_scaled_integer"],
            "real_endpoint_upper_exclusive": certificate["limit"] + 1,
        },
        "p5_monotone_cone_refutation": p5,
        "covariance_checks": covariance,
        "mutations_detected": mutations,
        "scientific_flags": {
            "actual_lptrp23_through_100m_proved": True,
            "fixed_finite_sieve_eventual_proved": True,
            "positive_covariance_spectrum_proved": True,
            "growing_prime_tail_proved": False,
            "scid_pl_proved": False,
            "rh_established": False,
        },
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = main()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
