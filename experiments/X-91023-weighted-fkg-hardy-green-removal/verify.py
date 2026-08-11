#!/usr/bin/env python3
"""Finite checks for L-91023--L-91026.

The replay checks exact finite weighted-FKG inequalities, the symmetric-square
conjugacy, causal Hardy transfer identities, and finite floating reconnaissance
for the final Green-removal density. It proves no asymptotic theorem or RH.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp

mp.mp.dps = 70


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    out: list[int] = []
    for p in range(2, n + 1):
        if sieve[p]:
            out.append(p)
            for k in range(p * p, n + 1, p):
                sieve[k] = False
    return out


def prime_factors(n: int) -> list[int]:
    out: list[int] = []
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            out.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        out.append(m)
    return out


def F_fraction(s: int, n: int) -> Fraction:
    ans = Fraction(1, 1)
    for p in prime_factors(n):
        ans *= Fraction(p**s - 1, p**s)
    return ans


def finite_product(s: int, N: int) -> Fraction:
    ans = Fraction(1, 1)
    for p in primes_upto(N):
        ans *= Fraction(p ** (s + 1) - 1, p ** (s + 1))
    return ans


def symmetric_square(a: mp.mpf, u: mp.mpf) -> mp.matrix:
    den = a * a + u * u
    rt2 = mp.sqrt(2)
    return mp.matrix(
        [
            [a * a, rt2 * a * u, u * u],
            [-rt2 * a * u, a * a - u * u, rt2 * a * u],
            [u * u, -rt2 * a * u, a * a],
        ]
    ) / den


def cauchy_U(a: mp.mpf, u: mp.mpf) -> mp.matrix:
    den = 4 * (a * a + u * u)
    return mp.matrix(
        [
            [4 * a * a + u * u, 2 * mp.sqrt(6) * a * u, mp.sqrt(15) * u * u],
            [-2 * mp.sqrt(6) * a * u, 4 * a * a - 4 * u * u, 2 * mp.sqrt(10) * a * u],
            [mp.sqrt(15) * u * u, -2 * mp.sqrt(10) * a * u, 4 * a * a - u * u],
        ]
    ) / den


def mat_max_abs(M: mp.matrix) -> mp.mpf:
    return max(abs(M[i, j]) for i in range(M.rows) for j in range(M.cols))


def impulse(m: int, c: mp.mpf, t: mp.mpf) -> mp.mpf:
    return mp.e ** (-c * t) * (
        t ** (m + 1) / mp.factorial(m + 1)
        - c * t ** (m + 2) / mp.factorial(m + 2)
    )


def f_float(s: mp.mpf, n: int) -> mp.mpf:
    ans = mp.mpf(1)
    for p in prime_factors(n):
        ans *= 1 - mp.power(p, -s)
    return ans


def scan_boundary(a: mp.mpf, N: int) -> dict[str, str]:
    s = 2 * a
    c0 = 1 / mp.zeta(1 + s)
    kappa = mp.sqrt(mp.mpf(275) / 14)
    A0 = mp.mpf(1)
    L0 = mp.mpf(0)
    min_b = mp.inf
    min_n = 1
    for n in range(1, N + 1):
        if n > 1:
            w = f_float(s, n) / n
            A0 += w
            L0 += w * mp.log(n)
        t = mp.log(n + 1)
        E0 = A0 - c0 * t
        E1 = t * A0 - L0 - c0 * t * t / 2
        B = -c0 + kappa * a * E0 + 4 * a * a * E1
        if B < min_b:
            min_b = B
            min_n = n
    return {
        "a": mp.nstr(a, 12),
        "minimum_B": mp.nstr(min_b, 24),
        "left_limit_at_log_n_plus_1": str(min_n),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    checks = 0
    exact_fkg_checks = 0
    max_symmetric_square_error = mp.mpf(0)
    max_hardy_laplace_error = mp.mpf(0)
    max_zero_mass_error = mp.mpf(0)
    min_first_cell = mp.inf
    min_eventual_margin = mp.inf

    for s in [1, 2, 3]:
        for N in range(2, 61):
            P = finite_product(s, N)
            weights = [
                [Fraction(N + 1 - n, 1) for n in range(1, N + 1)],
                [Fraction((N + 1 - n) ** 2, 1) for n in range(1, N + 1)],
                [Fraction(1, n) for n in range(1, N + 1)],
            ]
            for h in weights:
                lhs = sum(F_fraction(s, n) * h[n - 1] / n for n in range(1, N + 1))
                rhs = P * sum(h[n - 1] / n for n in range(1, N + 1))
                assert lhs >= rhs
                exact_fkg_checks += 1
    checks += exact_fkg_checks

    c = (mp.sqrt(5) + mp.sqrt(3)) / 4
    ss = (mp.sqrt(5) - mp.sqrt(3)) / 4
    O = mp.matrix([[c, 0, ss], [0, 1, 0], [-ss, 0, c]])
    for a in [mp.mpf("0.13"), mp.mpf("0.5"), mp.mpf("1.7")]:
        for u in [mp.mpf("0"), mp.mpf("0.31"), mp.mpf("2.4"), mp.mpf("8")]:
            err = mat_max_abs(O * symmetric_square(a, u) * O.T - cauchy_U(a, u))
            max_symmetric_square_error = max(max_symmetric_square_error, err)
            assert err < mp.mpf("1e-65")
            checks += 1

    for m in range(6):
        for c0 in [mp.mpf("0.2"), mp.mpf("0.9"), mp.mpf("3.1")]:
            for z in [mp.mpc("0.4", "0.2"), mp.mpc("1.3", "0.7")]:
                numeric = mp.quad(lambda t: mp.e ** (-z * t) * impulse(m, c0, t), [0, mp.inf])
                closed = z / (z + c0) ** (m + 3)
                err = abs(numeric - closed)
                max_hardy_laplace_error = max(max_hardy_laplace_error, err)
                assert err < mp.mpf("1e-58")
                checks += 1
            mass = mp.quad(lambda t: impulse(m, c0, t), [0, mp.inf])
            max_zero_mass_error = max(max_zero_mass_error, abs(mass))
            assert abs(mass) < mp.mpf("1e-60")
            checks += 1

    kappa = mp.sqrt(mp.mpf(275) / 14)
    L = mp.log(2)
    delta = 1 - L
    first_cell_samples: list[dict[str, str]] = []
    for a in [mp.mpf("0.005"), mp.mpf("0.02"), mp.mpf("0.1"), mp.mpf("0.3"),
              mp.mpf("0.5"), mp.mpf("1"), mp.mpf("3")]:
        c0 = 1 / mp.zeta(1 + 2 * a)
        vals = []
        for j in range(101):
            t = L * j / 100
            B = -c0 + kappa * a * (1 - c0 * t) + 4 * a * a * (t - c0 * t * t / 2)
            vals.append(B)
            assert B > 0
            checks += 1
        local_min = min(vals)
        min_first_cell = min(min_first_cell, local_min)
        T = max(mp.mpf(0), 1 - kappa * a * delta - 2 * a * a * L * L) / (4 * a * a * delta)
        if T > 0:
            margin = -1 + kappa * a * delta + 4 * a * a * delta * (T + 1) + 2 * a * a * L * L
            min_eventual_margin = min(min_eventual_margin, margin)
            assert margin > 0
            checks += 1
        first_cell_samples.append({
            "a": mp.nstr(a, 10),
            "minimum_sampled_first_cell_B": mp.nstr(local_min, 22),
            "explicit_eventual_threshold_T": mp.nstr(T, 18),
        })

    scans = [scan_boundary(mp.mpf(x), 20000) for x in
             ["0.01", "0.03", "0.05", "0.1", "0.2", "0.4", "0.8", "1.5", "3"]]
    assert all(mp.mpf(row["minimum_B"]) > 0 for row in scans)
    checks += len(scans)

    result: dict[str, Any] = {
        "classification": "PASS_WEIGHTED_FKG_HARDY_GREEN_REMOVAL",
        "checks": checks,
        "exact_weighted_fkg_checks": exact_fkg_checks,
        "max_symmetric_square_error": mp.nstr(max_symmetric_square_error, 12),
        "max_hardy_laplace_error": mp.nstr(max_hardy_laplace_error, 12),
        "max_zero_mass_error": mp.nstr(max_zero_mass_error, 12),
        "minimum_sampled_first_cell_boundary_density": mp.nstr(min_first_cell, 18),
        "minimum_eventual_bound_margin": mp.nstr(min_eventual_margin, 18),
        "first_cell_samples": first_cell_samples,
        "boundary_density_reconnaissance": scans,
        "scope": (
            "exact finite FKG consequences and transform algebra; "
            "floating finite boundary-density reconnaissance only; no CJHI or RH claim"
        ),
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print("PASS_WEIGHTED_FKG_HARDY_GREEN_REMOVAL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
