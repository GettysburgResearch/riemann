#!/usr/bin/env python3
"""Exact regression for the finite Brownian-gamma / logarithmic Nörlund algebra.

This program deliberately proves only finite rational identities.  It does not
prove the real-zero theorem BLNRZ, RH, or any asymptotic zero statement.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "results" / "verification.json"


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))


def c_weight(N: int, n: int) -> Fraction:
    """C_{N,n}=4 (N!)^4 / ((N-n)!^2 (N+n)!^2)."""
    if not 1 <= n <= N:
        return Fraction(0)
    num = 4 * math.factorial(N) ** 4
    den = math.factorial(N - n) ** 2 * math.factorial(N + n) ** 2
    return Fraction(num, den)


def partial_fraction_coefficients(N: int, n: int) -> Tuple[Fraction, Fraction]:
    """Return A_{N,n}, B_{N,n} for L_N(q)."""
    C = c_weight(N, n)
    B = C * n**4
    sigma = sum(
        (Fraction(1, k * k - n * n) for k in range(1, N + 1) if k != n),
        Fraction(0),
    )
    A = -2 * B * sigma
    return A, B


def harmonic_sigma(N: int, n: int) -> Fraction:
    return Fraction(1, 2 * n) * (
        harmonic(N - n) - harmonic(N + n) + Fraction(3, 2 * n)
    )


def laplace_product(N: int, q: Fraction) -> Fraction:
    value = Fraction(1)
    for n in range(1, N + 1):
        value *= Fraction(n**4, (q + n * n) ** 2)
    return value


def laplace_partial_fraction(N: int, q: Fraction) -> Fraction:
    value = Fraction(0)
    for n in range(1, N + 1):
        A, B = partial_fraction_coefficients(N, n)
        value += A / (q + n * n) + B / (q + n * n) ** 2
    return value


def moment_from_partial_fractions(N: int, j: int) -> Fraction:
    """Exact E[S_N^j], S_N=sum Gamma(2,rate=n^2)."""
    total = Fraction(0)
    for n in range(1, N + 1):
        A, B = partial_fraction_coefficients(N, n)
        total += A * math.factorial(j) / n ** (2 * j + 2)
        total += B * math.factorial(j + 1) / n ** (2 * j + 4)
    return total


def moment_from_mgf(N: int, j: int) -> Fraction:
    """Coefficient extraction from prod_n (1-t/n^2)^(-2)."""
    coeff: List[Fraction] = [Fraction(0)] * (j + 1)
    coeff[0] = Fraction(1)
    for n in range(1, N + 1):
        factor = [Fraction(r + 1, n ** (2 * r)) for r in range(j + 1)]
        nxt = [Fraction(0)] * (j + 1)
        for a in range(j + 1):
            for b in range(j + 1 - a):
                nxt[a + b] += coeff[a] * factor[b]
        coeff = nxt
    return math.factorial(j) * coeff[j]


def dirichlet_polynomial_at_even_s(N: int, s: int) -> Fraction:
    """D_N(s)=m_N(s)/(pi^(-s/2) Gamma(1+s/2)), for even s>=0."""
    assert s >= 0 and s % 2 == 0
    total = Fraction(0)
    for n in range(1, N + 1):
        bracket = n * (harmonic(N + n) - harmonic(N - n)) + Fraction(s - 1, 2)
        total += c_weight(N, n) * bracket / n**s
    return total


def dirichlet_polynomial_from_moment(N: int, s: int) -> Fraction:
    """Independent value obtained from E[S_N^(s/2)]."""
    j = s // 2
    # m_N(s)=pi^(-j) E[S_N^j]
    # g(s)=pi^(-j) Gamma(1+j), hence D=E[S_N^j]/j!.
    return moment_from_mgf(N, j) / math.factorial(j)


def norlund_coefficients(N: int) -> Tuple[List[Fraction], List[Fraction]]:
    """Return alpha_n,beta_n with Dbar_N(s)=sum (alpha_n+beta_n*s)n^-s."""
    HN = harmonic(N)
    alpha = [Fraction(0)] * (N + 1)
    beta = [Fraction(0)] * (N + 1)
    for K in range(1, N + 1):
        weight = Fraction(1, K) / HN
        for n in range(1, K + 1):
            C = c_weight(K, n)
            h = n * (harmonic(K + n) - harmonic(K - n))
            alpha[n] += weight * C * (h - Fraction(1, 2))
            beta[n] += weight * C * Fraction(1, 2)
    return alpha, beta


def norlund_value_at_even_s(N: int, s: int) -> Fraction:
    alpha, beta = norlund_coefficients(N)
    return sum(
        ((alpha[n] + beta[n] * s) / n**s for n in range(1, N + 1)),
        Fraction(0),
    )


def norlund_direct_at_even_s(N: int, s: int) -> Fraction:
    HN = harmonic(N)
    return sum(
        (dirichlet_polynomial_at_even_s(K, s) / K for K in range(1, N + 1)),
        Fraction(0),
    ) / HN


def mutation_tests() -> Dict[str, bool]:
    tests: Dict[str, bool] = {}
    # The 3/(2n) term in the harmonic collapse is load-bearing.
    N, n = 7, 3
    wrong = Fraction(1, 2 * n) * (
        harmonic(N - n) - harmonic(N + n) + Fraction(1, n)
    )
    tests["wrong_harmonic_endpoint_rejected"] = wrong != harmonic_sigma(N, n)

    # Omitting the logarithmic 1/K Nörlund weight changes the producer.
    N, s = 8, 4
    wrong_mean = sum(
        (dirichlet_polynomial_at_even_s(K, s) for K in range(1, N + 1)),
        Fraction(0),
    ) / N
    tests["cesaro_substitution_rejected"] = wrong_mean != norlund_direct_at_even_s(N, s)

    # A missing double pole destroys normalization L_N(0)=1.
    N = 5
    bad = Fraction(0)
    for n in range(1, N + 1):
        A, _B = partial_fraction_coefficients(N, n)
        bad += A / (n * n)
    tests["missing_double_poles_rejected"] = bad != 1

    # The N=1 control must be Gamma(shape=2), not exponential.
    tests["shape_two_control"] = moment_from_mgf(1, 2) == Fraction(6)
    return tests


def main() -> None:
    counts = {
        "harmonic_collapses": 0,
        "laplace_rows": 0,
        "normalizations": 0,
        "moment_rows": 0,
        "dirichlet_rows": 0,
        "norlund_rows": 0,
    }

    for N in range(1, 17):
        for n in range(1, N + 1):
            direct = sum(
                (Fraction(1, k * k - n * n) for k in range(1, N + 1) if k != n),
                Fraction(0),
            )
            assert direct == harmonic_sigma(N, n)
            counts["harmonic_collapses"] += 1

        for q in (Fraction(0), Fraction(1, 3), Fraction(2), Fraction(17, 5)):
            assert laplace_product(N, q) == laplace_partial_fraction(N, q)
            counts["laplace_rows"] += 1

        assert laplace_partial_fraction(N, Fraction(0)) == 1
        counts["normalizations"] += 1

        for j in range(0, 7):
            assert moment_from_partial_fractions(N, j) == moment_from_mgf(N, j)
            counts["moment_rows"] += 1

        for s in (0, 2, 4, 6, 8):
            assert dirichlet_polynomial_at_even_s(N, s) == dirichlet_polynomial_from_moment(N, s)
            counts["dirichlet_rows"] += 1

    for N in range(1, 13):
        alpha, beta = norlund_coefficients(N)
        assert all(beta[n] > 0 for n in range(1, N + 1))
        assert all(alpha[n] > 0 for n in range(1, N + 1))
        for s in (0, 2, 4, 6):
            assert norlund_value_at_even_s(N, s) == norlund_direct_at_even_s(N, s)
            counts["norlund_rows"] += 1

    mutations = mutation_tests()
    assert all(mutations.values())

    payload = {
        "classification": "EXACT_RATIONAL_FINITE_ALGEBRA_ONLY",
        "verdict": "PASS_EXACT_BROWNIAN_GAMMA_NORLUND_ALGEBRA",
        "counts": counts,
        "mutations": mutations,
        "scope_exclusions": [
            "BLNRZ real-zero theorem",
            "raw-truncation off-line root certification",
            "asymptotic zero convergence",
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
