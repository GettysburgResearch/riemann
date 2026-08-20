#!/usr/bin/env python3
"""Exact regressions for the L-102009/L-102010 ratio-four factorization.

This replay checks finite arithmetic/source identities, the two-box piecewise
differential identities, and the sharp Hardy multiplier bound. It does not
prove HHFE102010 or RH.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
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


def divisors(n: int) -> list[int]:
    out: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    return sorted(out)


def conv(f: list[Fraction], g: list[Fraction], nmax: int) -> list[Fraction]:
    out = [Fraction(0)] * (nmax + 1)
    for n in range(1, nmax + 1):
        out[n] = sum((f[d] * g[n // d] for d in divisors(n)), Fraction(0))
    return out


def factorization(n: int) -> dict[int, int]:
    fac: dict[int, int] = {}
    x = n
    p = 2
    while p * p <= x:
        while x % p == 0:
            fac[p] = fac.get(p, 0) + 1
            x //= p
        p += 1
    if x > 1:
        fac[x] = fac.get(x, 0) + 1
    return fac


def eta_prime_power(k: int) -> Fraction:
    return Fraction(math.comb(2 * k, k), 4**k)


def eta(n: int) -> Fraction:
    ans = Fraction(1)
    for k in factorization(n).values():
        ans *= eta_prime_power(k)
    return ans


def check_eta_square(nmax: int = 128) -> int:
    checks = 0
    for k in range(0, 41):
        lhs = sum((eta_prime_power(j) * eta_prime_power(k - j)
                   for j in range(k + 1)), Fraction(0))
        assert lhs == 1
        checks += 1

    eta_values = [Fraction(0)] + [eta(n) for n in range(1, nmax + 1)]
    eta_square = conv(eta_values, eta_values, nmax)
    for n in range(1, nmax + 1):
        assert eta_square[n] == 1
        checks += 1
    return checks


def check_half_completed_source(nmax: int = 96) -> int:
    mu_int = mobius_sieve(nmax)
    mu = [Fraction(x) for x in mu_int]
    one = [Fraction(0)] + [Fraction(1)] * nmax
    eps = [Fraction(0)] * (nmax + 1)
    eps[1] = 1
    eta_values = [Fraction(0)] + [eta(n) for n in range(1, nmax + 1)]
    checks = 0

    for u in range(1, 10):
        mu_u = [Fraction(0)] * (nmax + 1)
        b_u = [Fraction(0)] * (nmax + 1)
        for n in range(1, nmax + 1):
            if n <= u:
                mu_u[n] = mu[n]
            else:
                b_u[n] = mu[n]

        a_u = [eps[n] - conv(mu_u, one, nmax)[n]
               for n in range(nmax + 1)]
        h_u = conv(b_u, eta_values, nmax)

        balanced = conv(conv(a_u, a_u, nmax), mu, nmax)
        symmetric = conv(h_u, h_u, nmax)
        for n in range(1, nmax + 1):
            assert balanced[n] == symmetric[n]
            if n <= u:
                assert h_u[n] == 0
            checks += 1
    return checks


def check_piecewise_kernels() -> int:
    checks = 0
    # Put y=x^2. On [1,2], A=2(x-1), D=(x/2)d/dx.
    # On [2,4], A=(2-x)sqrt(2), so only the sqrt(2) coefficient is stored.
    for j in range(1, 100):
        x = Fraction(1) + Fraction(j, 100) * (Fraction(1414, 1000) - 1)
        A = 2 * (x - 1)
        DA = x
        assert DA - A / 2 == 1
        assert DA + 3 * A / 2 == 4 * x - 3
        checks += 2

    root2_lo = Fraction(1414, 1000)
    for j in range(1, 100):
        x = root2_lo + Fraction(j, 100) * (2 - root2_lo)
        A_coeff = 2 - x
        DA_coeff = -x / 2
        assert DA_coeff - A_coeff / 2 == -1
        assert DA_coeff + 3 * A_coeff / 2 == 3 - 2 * x
        checks += 2
    return checks


def check_hardy_norm() -> int:
    checks = 0
    for n in range(0, 1001):
        t = Fraction(n, 37)
        lhs = t * t + Fraction(9, 4)
        rhs = 9 * (t * t + Fraction(1, 4))
        assert lhs <= rhs
        assert rhs - lhs == 8 * t * t
        checks += 2
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    counts = {
        "eta_square_checks": check_eta_square(),
        "half_completed_source_checks": check_half_completed_source(),
        "piecewise_kernel_checks": check_piecewise_kernels(),
        "hardy_norm_checks": check_hardy_norm(),
    }
    result = {
        "verdict": "PASS_X_102010_RATIOFOUR_HALF_DIVISOR_FACTORIZATION",
        "arithmetic_class": "EXACT_INTEGER_FRACTION",
        "counts": counts,
        "hhfe102010_proved": False,
        "rh_established": False,
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
