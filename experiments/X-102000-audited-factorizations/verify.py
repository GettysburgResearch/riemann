#!/usr/bin/env python3
"""Exact regression checks for the audited T-102000 continuation.

The replay certifies finite arithmetic identities and finite-truncation
bookkeeping only. It does not prove asymptotic energy bounds or RH.
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


def convolution(f: list[int], g: list[int], nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    for n in range(1, nmax + 1):
        out[n] = sum(f[d] * g[n // d] for d in divisors(n))
    return out


def n_balanced(v: Fraction, m: int) -> int:
    return sum(
        1
        for a in divisors(m)
        if Fraction(a, 1) > v and Fraction(m // a, 1) > v
    )


def largest_prime_factor(n: int) -> int:
    pmax = 1
    d = 2
    x = n
    while d * d <= x:
        while x % d == 0:
            pmax = d
            x //= d
        d += 1
    if x > 1:
        pmax = x
    return pmax


def check_source_factorizations(nmax: int = 96) -> int:
    mu = mobius_sieve(nmax)
    one = [0] + [1] * nmax
    eps = [0] * (nmax + 1)
    eps[1] = 1
    checks = 0

    for u in range(1, 10):
        mu_u = [0] * (nmax + 1)
        b_u = [0] * (nmax + 1)
        for n in range(1, nmax + 1):
            if n <= u:
                mu_u[n] = mu[n]
            else:
                b_u[n] = mu[n]

        mu_u_times_one = convolution(mu_u, one, nmax)
        a_u = [eps[n] - mu_u_times_one[n] for n in range(nmax + 1)]
        b_times_one = convolution(b_u, one, nmax)
        for n in range(1, nmax + 1):
            assert a_u[n] == b_times_one[n]
            checks += 1

        lhs = convolution(convolution(a_u, a_u, nmax), mu, nmax)
        rhs = convolution(b_u, a_u, nmax)
        for n in range(1, nmax + 1):
            assert lhs[n] == rhs[n]
            checks += 1

        # Pair coefficient: two Möbius wings versus gcd/single-wing form.
        for q in range(1, nmax + 1):
            pair = 0
            for d in divisors(q):
                e = q // d
                if d > u and e > u:
                    pair += mu[d] * mu[e]

            single = 0
            g = 1
            while g * g <= q:
                if q % (g * g) == 0:
                    m = q // (g * g)
                    if math.gcd(g, m) == 1 and mu[g] != 0 and mu[m] != 0:
                        single += mu[m] * n_balanced(Fraction(u, g), m)
                g += 1
            assert pair == single, (u, q, pair, single)
            checks += 1

    return checks


def check_largest_prime_recurrence(nmax: int = 120) -> int:
    mu = mobius_sieve(nmax)
    checks = 0
    for m in range(2, nmax + 1):
        if mu[m] == 0:
            continue
        p = largest_prime_factor(m)
        c = m // p
        for num in range(1, 13):
            for den in range(1, 5):
                v = Fraction(num, den)
                lhs = n_balanced(v, m)
                rhs_half = sum(
                    1
                    for a in divisors(c)
                    if Fraction(a, 1) > v
                    and Fraction(c // a, 1) > v / p
                )
                assert lhs == 2 * rhs_half, (m, p, c, v, lhs, rhs_half)
                assert mu[m] * lhs == -2 * mu[c] * rhs_half
                checks += 2
    return checks


def check_joint_survival() -> int:
    activities = [
        Fraction(1, 3),
        Fraction(1, 5),
        Fraction(2, 9),
        Fraction(1, 7),
        Fraction(3, 20),
        Fraction(1, 11),
    ]
    k = len(activities)
    left = [Fraction(1)] * k
    acc = Fraction(1)
    for i, r in enumerate(activities):
        left[i] = acc
        acc *= 1 - r

    right = [Fraction(1)] * k
    acc = Fraction(1)
    for j in range(k - 1, -1, -1):
        right[j] = acc
        acc *= 1 - activities[j]

    checks = 0
    for i in range(k):
        for j0 in range(i + 1, k):
            lhs = sum(
                activities[i] * activities[j] * left[i] * right[j]
                for j in range(j0, k)
            )
            # R_(j0-1) includes labels j0,...,k-1.
            r_before = (1 - activities[j0]) * right[j0]
            rhs = activities[i] * left[i] * (1 - r_before)
            assert lhs == rhs
            checks += 1
    return checks


def check_depth_thresholds() -> int:
    checks = 0
    for t in range(2, 200):
        above_square_root = [q for q in range(2, 300) if q * q > t][:20]
        for q1 in above_square_root:
            for q2 in above_square_root:
                assert q1 * q2 > t
                checks += 1
        for r in range(1, 6):
            qs = [q for q in range(2, 300) if q ** r > t][:r]
            if len(qs) == r:
                assert math.prod(qs) > t
                checks += 1
    return checks


def check_centered_kernel_bound() -> int:
    checks = 0
    # G(y)=-64[1-(1-sqrt(y))^3] for y<=1 and -64 afterwards.
    for n in range(0, 1001):
        x = Fraction(n, 1000)
        f = 1 - (1 - x) ** 3
        assert Fraction(0) <= f <= Fraction(1)
        g = -64 * f
        assert Fraction(-64) <= g <= Fraction(0)
        checks += 1

    # Four values in a double difference, each in [-64,0].
    import itertools

    extremes = [Fraction(-64), Fraction(0)]
    for vals in itertools.product(extremes, repeat=4):
        dd = vals[0] - vals[1] - vals[2] + vals[3]
        assert abs(dd) <= 256
        checks += 1
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    counts = {
        "source_factorization_checks": check_source_factorizations(),
        "largest_prime_recurrence_checks": check_largest_prime_recurrence(),
        "joint_survival_checks": check_joint_survival(),
        "depth_threshold_checks": check_depth_thresholds(),
        "centered_kernel_checks": check_centered_kernel_bound(),
    }
    result = {
        "verdict": "PASS_X_102000_AUDITED_FACTORIZATIONS",
        "arithmetic_class": "EXACT_INTEGER_FRACTION_WITH_FINITE_THRESHOLD_CHECKS",
        "counts": counts,
        "rh_established": False,
        "sow102008_proved": False,
        "field_energy_bounds_proved": False,
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
