#!/usr/bin/env python3
"""Exact finite replay for the PR #498 cubic-wavelet/Vaughan successor.

The checker authenticates finite identities, symbolic Mellin moments, formal
Vaughan decompositions, endpoint third differences, and hostile firewalls.
It does not prove the balanced Type-II estimate or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from fractions import Fraction as F
from pathlib import Path
from typing import Dict, List, Tuple

VERDICT = "PASS_CUBIC_WAVELET_VAUGHAN_AND_CARRIER_REDUCTION"
BASE_SHA = "6cc0da2fa5711017e260ebdcea4ba8c22e453288"


def k(x: F) -> F:
    if x < 0 or x > 1:
        return F(0)
    return x * (1 - x) * (2 * x - 1) / 3


def w4(x: F) -> F:
    if x <= 0 or x > 1:
        return F(0)
    ans = k(x)
    if x <= F(1, 4):
        ans -= 4 * k(4 * x)
    return ans


def poly_mul(a: List[F], b: List[F]) -> List[F]:
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_pow(a: List[F], n: int) -> List[F]:
    out = [F(1)]
    for _ in range(n):
        out = poly_mul(out, a)
    return out


def endpoint_poly(r: int) -> List[F]:
    # G_r(x)=x^r(1-x)^r(2x-1), coefficients in ascending order.
    xr = [F(0)] * r + [F(1)]
    one_minus = poly_pow([F(1), F(-1)], r)
    return poly_mul(poly_mul(xr, one_minus), [F(-1), F(2)])


def poly_derivative(a: List[F]) -> List[F]:
    return [F(i) * a[i] for i in range(1, len(a))] or [F(0)]


def poly_integral_unit(a: List[F]) -> F:
    return sum((a[i] / F(i + 1) for i in range(len(a))), F(0))


def endpoint_family_checks() -> Dict[str, object]:
    checks = 0
    moments = {}
    for r in range(1, 7):
        g = endpoint_poly(r)
        gp = poly_derivative(g)
        wr = [x / 2 for x in gp]
        assert poly_integral_unit(wr) == 0
        c = poly_integral_unit(poly_mul(wr, wr))
        if r == 1:
            assert c == F(1, 20)
        if r == 2:
            assert c == F(1, 630)
        # Beta-integral numerator check at several rational s values.
        for sval in (F(1, 2), F(2, 3), F(3, 2), F(5, 3)):
            lhs = sum((g[j] / (sval + j) for j in range(len(g))), F(0))
            den = F(1)
            for j in range(r, 2 * r + 2):
                den *= sval + j
            rhs = F(math.factorial(r)) * (sval - 1) / den
            assert lhs == rhs
            checks += 1
        moments[str(r)] = str(c)
    return {"beta_checks": checks, "C_r": moments}


def mobius_table(n: int) -> List[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: List[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def primes_upto(n: int) -> List[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for q in range(p * p, n + 1, p):
                sieve[q] = False
    return [p for p in range(2, n + 1) if sieve[p]]


def formal_logs(n: int) -> Dict[int, F]:
    return {p: F((p % 19) + 2, (p % 13) + 3) for p in primes_upto(n)}


def formal_lambda(n: int, logs: Dict[int, F]) -> List[F]:
    lam = [F(0)] * (n + 1)
    for p, lp in logs.items():
        q = p
        while q <= n:
            lam[q] = lp
            if q > n // p:
                break
            q *= p
    return lam


def q4_source(n: int, lam: List[F], log2: F) -> List[F]:
    c = lam[:]
    for m in range(4, n + 1, 4):
        c[m] -= 4 * lam[m // 4]
    q = 4
    while q <= n:
        c[q] += 6 * log2  # 3 log 4
        if q > n // 4:
            break
        q *= 4
    return c


def wavelet_source(n: int, lam: List[F], log2: F) -> Tuple[F, F, F]:
    direct = sum((q4_source(n, lam, log2)[m] * k(F(m, n)) for m in range(1, n + 1)), F(0))
    prime_wavelet = sum((lam[m] * w4(F(m, n)) for m in range(1, n + 1)), F(0))
    gauge = F(0)
    q = 4
    while q <= n:
        gauge += 6 * log2 * k(F(q, n))
        if q > n // 4:
            break
        q *= 4
    return direct, prime_wavelet, gauge


def dirichlet_convolution(a: List[F], b: List[F], n: int) -> List[F]:
    out = [F(0)] * (n + 1)
    for d in range(1, n + 1):
        if a[d] == 0:
            continue
        for q in range(d, n + 1, d):
            out[q] += a[d] * b[q // d]
    return out


def vaughan_components(n: int, lam: List[F], mu: List[int], u: int, v: int) -> Tuple[List[F], List[F], List[F], List[F]]:
    logseq = [F(0)] * (n + 1)
    # Formal logarithm is recovered from Lambda * 1, avoiding transcendental input.
    for m in range(1, n + 1):
        logseq[m] = sum((lam[d] for d in range(1, m + 1) if m % d == 0), F(0))
    mu_small = [F(0)] * (n + 1)
    mu_large = [F(0)] * (n + 1)
    lam_small = [F(0)] * (n + 1)
    lam_large = [F(0)] * (n + 1)
    ones = [F(0)] + [F(1)] * n
    for m in range(1, n + 1):
        (mu_small if m <= u else mu_large)[m] = F(mu[m])
        (lam_small if m <= v else lam_large)[m] = lam[m]
    t1 = dirichlet_convolution(mu_small, logseq, n)
    t2a = dirichlet_convolution(mu_small, lam_small, n)
    t2 = dirichlet_convolution(t2a, ones, n)
    t2 = [-x for x in t2]
    t3 = lam_small
    t4a = dirichlet_convolution(mu_large, lam_large, n)
    t4 = dirichlet_convolution(t4a, ones, n)
    return t1, t2, t3, t4


def project(seq: List[F], n: int) -> F:
    return sum((seq[m] * w4(F(m, n)) for m in range(1, n + 1)), F(0))


def third_forward(values: List[F], i: int) -> F:
    return values[i + 3] - 3 * values[i + 2] + 3 * values[i + 1] - values[i]


def endpoint_cubic(seq: List[F], n: int) -> F:
    return 3 * n**3 * sum((seq[m] * k(F(m, n)) for m in range(1, n + 1)), F(0))


def hallless_operator_firewall(scale: int) -> Tuple[F, F, F]:
    # N=L^2, m,r in [3L/4,4L/5]. Their product ratio lies in [9/16,16/25],
    # where W=K is strictly positive. All-one coefficients force an operator
    # ratio growing like sqrt(N), so coefficient-blind l2 dispersion cannot close.
    assert scale % 20 == 0
    n = scale * scale
    lo = 3 * scale // 4
    hi = 4 * scale // 5
    indices = list(range(lo, hi + 1))
    total = sum((w4(F(m * r, n)) for m in indices for r in indices), F(0))
    norm_product = F(len(indices))
    ratio = total / norm_product
    assert total > 0 and ratio > 0
    return total, norm_product, ratio


def symbolic_moments() -> Dict[str, str]:
    # Integral W dx and integral W log x dx, represented as A+B*log(4).
    # Integral x^j log x dx = x^(j+1)(log x/(j+1)-1/(j+1)^2).
    small = {1: F(5), 2: F(-63), 3: F(170)}
    large = {1: F(-1, 3), 2: F(1), 3: F(-2, 3)}
    quarter = F(1, 4)
    mass = F(0)
    log_rational = F(0)
    log4_coeff = F(0)
    for power, coeff in small.items():
        mass += coeff * quarter ** (power + 1) / (power + 1)
        log_rational += coeff * quarter ** (power + 1) * (-F(1, (power + 1) ** 2))
        log4_coeff += coeff * quarter ** (power + 1) * (-F(1, power + 1))
    for power, coeff in large.items():
        mass += coeff * (F(1) - quarter ** (power + 1)) / (power + 1)
        # At 1 the log term vanishes; subtract the lower endpoint.
        log_rational += coeff * (
            -F(1, (power + 1) ** 2)
            + quarter ** (power + 1) * F(1, (power + 1) ** 2)
        )
        log4_coeff += coeff * quarter ** (power + 1) * F(1, power + 1)
    assert mass == 0
    assert log_rational == 0
    assert log4_coeff == 0
    return {"int_W": "0", "int_W_log_x": "0"}


def exact_integer_cell_sums() -> Dict[str, int]:
    checks = 0
    for y in range(4, 401):
        q, r = divmod(y, 4)
        lhs = sum((w4(F(m, y)) for m in range(1, y + 1)), F(0))
        if r == 0:
            rhs = F(0)
        elif r == 1:
            rhs = -F(8 * q * (q + 1), y**3)
        elif r == 2:
            rhs = -F(4 * q * (q + 1), 3 * (2 * q + 1) ** 3)
        else:
            rhs = -F(8 * q * (q + 1), y**3)
        assert lhs == rhs
        assert abs(lhs) <= F(2, 3 * y)
        checks += 1
    return {"integer_cell_sum_checks": checks}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("results/verification.json"))
    args = parser.parse_args()

    # Polynomial identity on a dense rational grid.
    wavelet_checks = 0
    for den in range(4, 101):
        for num in range(1, den + 1):
            x = F(num, den)
            expected = (5 * x - 63 * x * x + 170 * x * x * x) if x <= F(1, 4) else k(x)
            assert w4(x) == expected
            wavelet_checks += 1

    moments = symbolic_moments()
    cell_data = exact_integer_cell_sums()
    endpoint_family = endpoint_family_checks()

    source_checks = 0
    vaughan_checks = 0
    for n in range(16, 97):
        logs = formal_logs(n)
        lam = formal_lambda(n, logs)
        direct, prime_wavelet, gauge = wavelet_source(n, lam, logs[2])
        assert direct == prime_wavelet + gauge
        source_checks += 1

        mu = mobius_table(n)
        u = max(1, int(round(n ** (1 / 3))))
        while (u + 1) ** 3 <= n:
            u += 1
        while u**3 > n and u > 1:
            u -= 1
        v = u
        parts = vaughan_components(n, lam, mu, u, v)
        reconstructed = [sum((part[m] for part in parts), F(0)) for m in range(n + 1)]
        assert reconstructed == lam
        assert sum((project(list(part), n) for part in parts), F(0)) == prime_wavelet
        vaughan_checks += 1

    # Endpoint third-difference identity on arbitrary rational sources.
    rng = random.Random(93300)
    third_difference_checks = 0
    for length in range(12, 65):
        seq = [F(0)] + [F(rng.randint(-7, 7), rng.randint(1, 9)) for _ in range(length + 3)]
        p = [F(0)] * (length + 4)
        for n in range(1, length + 4):
            p[n] = endpoint_cubic(seq, n)
        for n in range(1, length):
            lhs = third_forward(p, n)
            rhs = F((n + 1) * (n + 2)) * (seq[n + 2] - seq[n + 1])
            assert lhs == rhs
            third_difference_checks += 1

    firewall = []
    for scale in (20, 40, 60, 80, 100):
        total, norms, ratio = hallless_operator_firewall(scale)
        firewall.append({
            "N": scale * scale,
            "bilinear_total": str(total),
            "l2_norm_product": str(norms),
            "ratio": str(ratio),
        })

    no_rh_inputs = [
        "exact finite convolution",
        "Chebyshev psi(x)<=4x",
        "divisor switching and tau bounds",
        "scaled trapezoid/Euler summation",
        "Vaughan identity",
        "Mellin inversion of the explicit compact kernel",
    ]
    forbidden_inputs = [
        "Riemann Hypothesis",
        "Mertens square-root cancellation",
        "PNT power-saving error",
        "CPBD estimate",
        "GRH large sieve",
        "J_Lambda-4sqrt bridge",
    ]

    payload = {
        "schema": "riemann.x93300.cubic-wavelet-vaughan.v1",
        "base_pr": 498,
        "base_sha": BASE_SHA,
        "endpoint_order_family": endpoint_family,
        "wavelet": {
            "grid_checks": wavelet_checks,
            "mellin_factor": "(1-4^(1-s))*(s-1)/(3*(s+1)*(s+2)*(s+3))",
            **moments,
            **cell_data,
        },
        "formal_arithmetic": {
            "source_rewrite_checks": source_checks,
            "vaughan_reconstruction_checks": vaughan_checks,
            "third_difference_checks": third_difference_checks,
        },
        "coefficient_blind_firewall": firewall,
        "input_audit": {
            "allowed_unconditional_inputs": no_rh_inputs,
            "forbidden_or_explicitly_open_inputs": forbidden_inputs,
            "balanced_type_ii_proved": False,
            "rh_established": False,
        },
        "verdict": VERDICT,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8", newline="\n")
    print(VERDICT)
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
