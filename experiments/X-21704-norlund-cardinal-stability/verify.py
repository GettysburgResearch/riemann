#!/usr/bin/env python3
"""Exact regression for the Brownian--Norlund cardinal derivative identity.

This program uses only integers and fractions.Fraction.  It verifies finite
coefficient/cardinal identities.  It does not prove half-plane stability,
complete monotonicity, or RH.
"""
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "results" / "verification.json"


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))


def c_weight(K: int, n: int) -> Fraction:
    if not 1 <= n <= K:
        return Fraction(0)
    return Fraction(
        4 * math.factorial(K) ** 4,
        math.factorial(K - n) ** 2 * math.factorial(K + n) ** 2,
    )


def r_cardinal(K: int, n: int) -> Fraction:
    """R_K(n)=binom(2K,K-n)/binom(2K,K), with zero outside n<=K."""
    if not 0 <= n <= K:
        return Fraction(0)
    return Fraction(math.comb(2 * K, K - n), math.comb(2 * K, K))


def raw_beta(K: int, n: int) -> Fraction:
    return c_weight(K, n) / 2


def raw_beta_derivative(K: int, n: int) -> Fraction:
    """Derivative at x=n of 2 R_K(x)^2."""
    if not 1 <= n <= K:
        return Fraction(0)
    delta_h = harmonic(K + n) - harmonic(K - n)
    return -2 * delta_h * raw_beta(K, n)


def raw_alpha(K: int, n: int) -> Fraction:
    if not 1 <= n <= K:
        return Fraction(0)
    delta_h = harmonic(K + n) - harmonic(K - n)
    return c_weight(K, n) * (n * delta_h - Fraction(1, 2))


def norlund_coefficients(N: int):
    HN = harmonic(N)
    alpha = [Fraction(0)] * (N + 1)
    beta = [Fraction(0)] * (N + 1)
    beta_prime = [Fraction(0)] * (N + 1)
    for K in range(1, N + 1):
        w = Fraction(1, K) / HN
        for n in range(1, K + 1):
            alpha[n] += w * raw_alpha(K, n)
            beta[n] += w * raw_beta(K, n)
            beta_prime[n] += w * raw_beta_derivative(K, n)
    return alpha, beta, beta_prime


def mutation_tests():
    tests = {}
    K, n = 9, 4
    wrong_alpha = -n * raw_beta_derivative(K, n)
    tests["missing_product_derivative_rejected"] = wrong_alpha != raw_alpha(K, n)

    tests["unsquared_cardinal_rejected"] = 2 * r_cardinal(K, n) != raw_beta(K, n)

    N = 10
    HN = harmonic(N)
    log_beta = sum(
        (raw_beta(K, 2) / K for K in range(2, N + 1)), Fraction(0)
    ) / HN
    cesaro_beta = sum(
        (raw_beta(K, 2) for K in range(2, N + 1)), Fraction(0)
    ) / N
    tests["cesaro_weight_mutation_rejected"] = log_beta != cesaro_beta

    N, n, s = 12, 3, 6
    a, b, bp = norlund_coefficients(N)
    wrong = s * b[n] - n * bp[n]
    tests["wrong_mellin_power_rejected"] = wrong != a[n] + s * b[n]
    return tests


def main():
    counts = {
        "binomial_cardinal_rows": 0,
        "raw_derivative_rows": 0,
        "norlund_derivative_rows": 0,
        "mellin_sample_rows": 0,
    }

    for K in range(1, 25):
        for n in range(1, K + 1):
            R = r_cardinal(K, n)
            assert c_weight(K, n) == 4 * R * R
            counts["binomial_cardinal_rows"] += 1

            B = raw_beta(K, n)
            Bp = raw_beta_derivative(K, n)
            assert raw_alpha(K, n) == -B - n * Bp
            counts["raw_derivative_rows"] += 1

    for N in range(1, 19):
        alpha, beta, beta_prime = norlund_coefficients(N)
        for n in range(1, N + 1):
            assert beta[n] > 0
            assert alpha[n] == -beta[n] - n * beta_prime[n]
            counts["norlund_derivative_rows"] += 1
            for s in (0, 2, 4, 6, 8):
                sampled = (s - 1) * beta[n] - n * beta_prime[n]
                assert sampled == alpha[n] + s * beta[n]
                counts["mellin_sample_rows"] += 1

    mutations = mutation_tests()
    assert all(mutations.values())

    payload = {
        "classification": "EXACT_RATIONAL_FINITE_ALGEBRA_ONLY",
        "verdict": "PASS_EXACT_NORLUND_CARDINAL_DERIVATIVE_SAMPLING",
        "counts": counts,
        "mutations": mutations,
        "scope_exclusions": [
            "Norlund half-plane stability",
            "reciprocal complete monotonicity",
            "zero certification",
            "Riemann Hypothesis",
        ],
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["verdict"])
    print(json.dumps(counts, sort_keys=True))
    print(f"mutations {sum(mutations.values())}/{len(mutations)} PASS")
    print("proof-object SHA-256")
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
