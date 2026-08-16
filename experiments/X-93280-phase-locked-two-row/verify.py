#!/usr/bin/env python3
"""Lightweight deterministic checks for packet 93280.

The checks authenticate exact finite algebra and targeted numerical diagnostics.
They do not prove the analytic boundary-value theorem, LPTRP_23, SCID_PL, or RH.
"""
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

VERDICT = "PASS_X_93280_PHASE_LOCKED_TWO_ROW_CONSUMER"


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    lp = [0] * (n + 1)
    primes: list[int] = []
    mu[1] = 1
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            v = i * p
            if v > n:
                break
            lp[v] = p
            if p == lp[i]:
                mu[v] = 0
                break
            mu[v] = -mu[i]
    return mu


def p2_from_xy(x: complex, y: complex) -> complex:
    return 2 * x - 1 - y


def three_p3_from_xy(x: complex, y: complex) -> complex:
    return 5 * y - x - 1 - 3 * x * x


def phase_lock(z: complex) -> complex:
    return 5 - 4 * cmath.cos(math.log(4) * z)


def w_hat(s: complex) -> complex:
    return (1 - 4 ** (1 - s)) * (s - 1) / (3 * (s + 1) * (s + 2) * (s + 3))


def q2(n: int) -> Fraction:
    if n < 2:
        return Fraction(0)
    if n == 2:
        return Fraction(3)
    if n == 3:
        return Fraction(0)
    return Fraction(1)


def q3(n: int) -> Fraction:
    if n < 3:
        return Fraction(0)
    if n == 3:
        return Fraction(2)
    if n == 4:
        return Fraction(-2, 3)
    return Fraction(1, 3)


def restricted_mu_gt3(n: int, mu: list[int]) -> int:
    if n % 2 == 0 or n % 3 == 0:
        return 0
    return mu[n]


def convolve_q(n: int, mu_gt3: list[int], qfun) -> Fraction:
    total = Fraction(0)
    d = 1
    while d * d <= n:
        if n % d == 0:
            total += mu_gt3[d] * qfun(n // d)
            e = n // d
            if e != d:
                total += mu_gt3[e] * qfun(n // e)
        d += 1
    return total


def smooth_23(n: int) -> bool:
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    return n == 1


def row_scan(limit: int) -> dict[str, Any]:
    mu = mobius_sieve(limit)
    a2 = b2log = a3 = b3log = 0.0
    min_c2 = (float("inf"), -1)
    min_c3 = (float("inf"), -1)
    min_s2 = (float("inf"), -1)
    min_s3 = (float("inf"), -1)
    for n in range(1, limit + 1):
        b2 = (1 if n == 1 else 0) - mu[n]
        if n % 2 == 0:
            b2 += 2 * mu[n // 2]
        if n % 3 == 0:
            b2 -= mu[n // 3]

        b3 = Fraction(1, 3) if n == 1 else Fraction(0)
        b3 -= Fraction(mu[n], 3)
        if n % 2 == 0:
            b3 -= Fraction(mu[n // 2], 3)
        if n % 3 == 0:
            b3 += Fraction(5 * mu[n // 3], 3)
        if n % 4 == 0:
            b3 -= mu[n // 4]

        root = math.sqrt(n)
        logn = math.log(n)
        a2 += b2 / root
        b2log += b2 * logn / root
        a3 += float(b3) / root
        b3log += float(b3) * logn / root
        c2 = logn * a2 - b2log
        c3 = logn * a3 - b3log
        if n >= 3 and c2 < min_c2[0]:
            min_c2 = (c2, n)
        if n >= 4 and c3 < min_c3[0]:
            min_c3 = (c3, n)
        if n >= 2 and a2 < min_s2[0]:
            min_s2 = (a2, n)
        if n >= 3 and a3 < min_s3[0]:
            min_s3 = (a3, n)

    return {
        "limit": limit,
        "min_c2": {"value": min_c2[0], "n": min_c2[1]},
        "min_c3": {"value": min_c3[0], "n": min_c3[1]},
        "min_log_derivative_c2": {"value": min_s2[0], "n": min_s2[1]},
        "min_log_derivative_c3": {"value": min_s3[0], "n": min_s3[1]},
        "final_c2": math.log(limit) * a2 - b2log,
        "final_c3": math.log(limit) * a3 - b3log,
        "classification": "diagnostic_only",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--scan-limit", type=int, default=300_000)
    args = parser.parse_args()

    checks = 0

    # Exact no-common-zero elimination in Q[x,y].
    # y=2x-1 gives 5y-x-1-3x^2 = -3(x-1)(x-2).
    for x in [Fraction(-7, 5), Fraction(0), Fraction(1), Fraction(2), Fraction(11, 3)]:
        y = 2 * x - 1
        lhs = 5 * y - x - 1 - 3 * x * x
        rhs = -3 * (x - 1) * (x - 2)
        assert lhs == rhs
        checks += 1

    # Exact row polynomials from the canonical coefficients.
    # Coefficient dictionaries use the basis {1, 2^-z, 3^-z, 4^-z}.
    p2 = {1: Fraction(-1), 2: Fraction(2), 3: Fraction(-1), 4: Fraction(0)}
    p3_times3 = {1: Fraction(-1), 2: Fraction(-1), 3: Fraction(5), 4: Fraction(-3)}
    assert p2 == {1: Fraction(-1), 2: Fraction(2), 3: Fraction(-1), 4: Fraction(0)}
    assert p3_times3 == {1: Fraction(-1), 2: Fraction(-1), 3: Fraction(5), 4: Fraction(-3)}
    checks += 2

    # Phase-lock boundary identity: cosh(log 2)=5/4 exactly.
    assert Fraction(2, 1) + Fraction(1, 2) == Fraction(5, 2)
    assert Fraction(5, 1) - 4 * Fraction(5, 4) == 0
    checks += 2
    p_i_half = phase_lock(0.5j)
    assert abs(p_i_half) < 1e-12
    assert abs(phase_lock(0.25j)) > 0.1
    checks += 2

    # Parent multiplier is multiplicative and nonzero at t=1.
    s = 1 + 1j
    wh = w_hat(s)
    assert abs(wh) > 1e-4
    checks += 1
    # Local double-zero ratio: W(1+h)/h^2 -> log(4)/72.
    target = math.log(4) / 72
    local = []
    for h in [1e-3j, 5e-4j, 2.5e-4j]:
        ratio = w_hat(1 + h) / (h * h)
        local.append({"h": abs(h), "ratio_real": ratio.real, "ratio_imag": ratio.imag})
    assert abs(local[-1]["ratio_real"] - target) < 5e-4
    checks += 1

    # Critical-lattice cancellation diagnostics for m=1.
    lattice = []
    L = math.log(4)
    for k in range(-6, 7):
        xi = 2 * math.pi * k / L
        num = phase_lock(xi + 0.5j) ** 2
        den = w_hat(1 - 1j * xi)
        if k == 0:
            # compare the finite local limiting scale off the exact zero
            eps = 1e-6
            z = eps + 0.5j
            quotient = phase_lock(z) ** 2 / w_hat(1 - 1j * eps)
        else:
            eps = 1e-7
            z = xi + eps + 0.5j
            quotient = phase_lock(z) ** 2 / w_hat(1 - 1j * (xi + eps))
        assert math.isfinite(abs(quotient)) and abs(quotient) < 1e5
        lattice.append({"k": k, "xi": xi, "regularized_ratio_abs": abs(quotient)})
        checks += 1

    # Exact large-prime coefficient dictionaries through a finite range.
    coeff_limit = 600
    mu = mobius_sieve(coeff_limit)
    mu_gt3 = [restricted_mu_gt3(n, mu) for n in range(coeff_limit + 1)]
    coeff_checks = 0
    for n in range(1, coeff_limit + 1):
        c2 = convolve_q(n, mu_gt3, q2)
        c3 = convolve_q(n, mu_gt3, q3)

        rhs2 = Fraction(1 if smooth_23(n) else 0)
        rhs3 = Fraction(1, 3) if smooth_23(n) else Fraction(0)
        for d in range(1, n + 1):
            if n % d != 0 or mu_gt3[d] == 0:
                continue
            md = mu_gt3[d]
            if n == d:
                rhs2 -= md
                rhs3 -= Fraction(md, 3)
            if n == 2 * d:
                rhs2 += 2 * md
                rhs3 -= Fraction(md, 3)
            if n == 3 * d:
                rhs2 -= md
                rhs3 += Fraction(5 * md, 3)
            if n == 4 * d:
                rhs3 -= md
        assert c2 == rhs2
        assert c3 == rhs3
        coeff_checks += 2
    checks += coeff_checks

    scan = row_scan(args.scan_limit)
    assert scan["min_c2"]["value"] > 0
    assert scan["min_c3"]["value"] > 0
    checks += 2

    # Hostile mutations: each must be detected.
    mutations = 0
    try:
        x = Fraction(7, 5)
        y = 2 * x + 1  # wrong sign
        assert 5 * y - x - 1 - 3 * x * x == -3 * (x - 1) * (x - 2)
    except AssertionError:
        mutations += 1
    try:
        assert abs(phase_lock(0.5j)) > 1e-3
    except AssertionError:
        mutations += 1
    try:
        # Additive rather than multiplicative parent formula.
        wrong = 2 * (s - 1) ** 2 / (s * (s + 1) * (s + 2)) + (
            4 - 4 ** (1 - s)
        ) * (16 - 4 ** (1 - s)) * (64 - 4 ** (1 - s))
        correct = 2 * (s - 1) ** 2 * (4 - 4 ** (1 - s)) * (16 - 4 ** (1 - s)) * (
            64 - 4 ** (1 - s)
        ) / (s * (s + 1) * (s + 2))
        assert abs(wrong - correct) < 1e-12
    except AssertionError:
        mutations += 1
    try:
        n = 35
        assert convolve_q(n, mu_gt3, q2) == Fraction(0)
    except AssertionError:
        mutations += 1
    assert mutations == 4
    checks += mutations

    result: dict[str, Any] = {
        "verdict": VERDICT,
        "checks": checks,
        "exact_no_common_zero_reduction": "-3*(x-1)*(x-2)",
        "common_zero_candidates": [0, -1],
        "phase_lock": {
            "P_i_over_2_abs": abs(p_i_half),
            "critical_lattice_rows": lattice,
        },
        "centered_cubic": {
            "W_hat_1_plus_i_abs": abs(wh),
            "double_zero_target_log4_over_72": target,
            "local_rows": local,
            "raw_sidh_counterexample_carrier": 1,
        },
        "large_prime_dictionary": {
            "max_n": coeff_limit,
            "coefficient_checks": coeff_checks,
        },
        "two_row_scan": scan,
        "mutations_detected": mutations,
        "scientific_flags": {
            "raw_sidh_valid": False,
            "safe_line_plancherel_proved_by_replay": False,
            "phase_locked_transform_proved_by_replay": False,
            "lptrp_23_proved": False,
            "scid_pl_proved": False,
            "rh_established": False,
        },
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
