#!/usr/bin/env python3
"""Exact finite regression for the carry Green factorization.

Arithmetic class: EXACT_RATIONAL / EXACT_INTEGER.
This checker authenticates finite algebra and one elementary transcendental
sign gate by rational enclosures. It does not test positive phase renewal,
asymptotics, the square-screw transfer, or the Riemann Hypothesis.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from math import isqrt
import json

N = 72


def mobius_sieve(n: int) -> list[int]:
    mu = [1] * (n + 1)
    composite = [False] * (n + 1)
    primes: list[int] = []
    mu[0] = 0
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


def beta(n: int, q: int) -> Fraction:
    if not (2 <= q <= n):
        return Fraction(0)
    return Fraction((n // q) * (q - 1 - (n % q)), n + 1)


def floor_total(n: int, q: int) -> int:
    return sum(j // q for j in range(n + 1))


def solve_c(x: int, w: list[Fraction]) -> list[Fraction]:
    c = [Fraction(0) for _ in range(x + 2)]
    for q in range(x, 1, -1):
        rhs = w[q]
        for n in range(q + 1, x + 1):
            rhs -= c[n] * beta(n, q)
        c[q] = rhs / beta(q, q)
    return c


def prime_exponents(n: int) -> dict[int, int]:
    out: dict[int, int] = defaultdict(int)
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] += 1
            n //= d
        d += 1
    if n > 1:
        out[n] += 1
    return dict(out)


def add_vec(
    dst: dict[int, Fraction],
    src: dict[int, int | Fraction],
    scale: Fraction,
) -> None:
    for p, e in src.items():
        dst[p] = dst.get(p, Fraction(0)) + scale * e
        if dst[p] == 0:
            del dst[p]


def log_factorial_vec(n: int) -> dict[int, int]:
    out: dict[int, Fraction] = {}
    for k in range(2, n + 1):
        add_vec(out, prime_exponents(k), Fraction(1))
    return {p: int(e) for p, e in out.items()}


def row_log_vec(n: int) -> dict[int, Fraction]:
    # (n+1) G_n = (n+1) log(n!) - 2 sum_{j=0}^n log(j!).
    out: dict[int, Fraction] = {}
    add_vec(out, log_factorial_vec(n), Fraction(n + 1))
    for j in range(2, n + 1):
        add_vec(out, log_factorial_vec(j), Fraction(-2))
    return out


def log_integer_interval(x: int, terms: int = 220) -> tuple[Fraction, Fraction]:
    """Rational enclosure of log(x) using the atanh series."""
    if x <= 0:
        raise ValueError("x must be positive")
    if x == 1:
        return Fraction(0), Fraction(0)
    z = Fraction(x - 1, x + 1)
    total = Fraction(0)
    power = z
    z2 = z * z
    for j in range(terms):
        total += 2 * power / (2 * j + 1)
        power *= z2
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return total, total + tail


def reciprocal_sqrt_interval(x: int, digits: int = 60) -> tuple[Fraction, Fraction]:
    """Rational enclosure of 1/sqrt(x)."""
    scale = 10**digits
    q = isqrt((scale * scale) // x)
    lo = Fraction(q, scale)
    hi = Fraction(q + 1, scale)
    assert lo * lo * x <= 1
    assert hi * hi * x > 1
    return lo, hi


def canonical(obj: object) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def main() -> None:
    mu = mobius_sieve(N)
    counts = {
        "floor_rows": 0,
        "green_rows": 0,
        "delta_rows": 0,
        "symbolic_targets": 0,
        "entropy_rows": 0,
        "outer_derivative_gates": 0,
        "mutations_rejected": 0,
    }

    for n in range(2, N + 1):
        for q in range(2, n + 1):
            lhs = (n + 1) * beta(n, q)
            rhs = (n + 1) * (n // q) - 2 * floor_total(n, q)
            assert lhs == rhs
            counts["floor_rows"] += 1

    for n in range(2, N + 1):
        for m in range(2, n + 1):
            lhs = sum(
                Fraction(mu[k]) * beta(n, m * k)
                for k in range(1, n // m + 1)
            )
            rhs = Fraction(2 * m - n - 1, n + 1)
            assert lhs == rhs
            counts["green_rows"] += 1

    for m in range(2, N + 1):
        for q in range(2, m + 1):
            lhs = (m + 1) * beta(m, q) - m * beta(m - 1, q)
            rhs = Fraction(m if m % q == 0 else 0) - Fraction(m // q)
            assert lhs == rhs
            counts["delta_rows"] += 1

    for x in (12, 19, 31, 47):
        targets: list[list[Fraction]] = []
        targets.append(
            [Fraction(0)] * 2
            + [Fraction(x - q, q * (x + 1)) for q in range(2, x + 1)]
        )
        targets.append(
            [Fraction(0)] * 2
            + [
                Fraction((x - q) ** 2, (q + 1) * (x + 3) ** 2)
                for q in range(2, x + 1)
            ]
        )
        for w0 in targets:
            w = w0 + [Fraction(0)] * max(0, x + 2 - len(w0))
            c = solve_c(x, w)
            u = [Fraction(0) for _ in range(x + 2)]
            for m in range(2, x + 1):
                u[m] = sum(
                    Fraction(mu[k]) * w[m * k]
                    for k in range(1, x // m + 1)
                )
            s = [Fraction(0) for _ in range(x + 3)]
            for m in range(x, 1, -1):
                s[m] = s[m + 1] + c[m] / (m + 1)
            for m in range(2, x + 1):
                green = sum(
                    c[n] * Fraction(2 * m - n - 1, n + 1)
                    for n in range(m, x + 1)
                )
                assert green == u[m]
                r = m * u[m] + sum(u[k] for k in range(m + 1, x + 1))
                assert s[m] == r / (m * (m - 1))
                assert c[m] == (m + 1) * (s[m] - s[m + 1])
            counts["symbolic_targets"] += 1

    prev: dict[int, Fraction] = {}
    for m in range(2, N + 1):
        cur = row_log_vec(m)
        delta: dict[int, Fraction] = dict(cur)
        add_vec(delta, prev, Fraction(-1))
        rhs: dict[int, Fraction] = {}
        add_vec(rhs, prime_exponents(m), Fraction(m - 1))
        add_vec(rhs, log_factorial_vec(m - 1), Fraction(-1))
        assert delta == rhs
        prev = cur
        counts["entropy_rows"] += 1

    log2_lo, _ = log_integer_interval(2)
    log3_lo, _ = log_integer_interval(3)
    _, log5_hi = log_integer_interval(5)
    invsqrt2_lo, invsqrt2_hi = reciprocal_sqrt_interval(2)
    invsqrt3_lo, invsqrt3_hi = reciprocal_sqrt_interval(3)

    c_lo = 1 - invsqrt2_hi - invsqrt3_hi
    gate_lo = (
        c_lo * (1 + log5_hi / 2)
        + (invsqrt2_lo * log2_lo + invsqrt3_lo * log3_lo) / 2
    )
    assert gate_lo > Fraction(48, 1000)
    counts["outer_derivative_gates"] = 1

    mutations = []
    mutations.append(
        any(
            sum(
                Fraction(mu[k]) * beta(n, m * k)
                for k in range(1, n // m + 1)
            )
            != Fraction(2 * m - n, n + 1)
            for n in range(2, 18)
            for m in range(2, n + 1)
        )
    )
    mutations.append(
        any(
            (m + 1) * beta(m, q) - m * beta(m - 1, q)
            != Fraction(m if m % q == 0 else 0)
            for m in range(2, 18)
            for q in range(2, m + 1)
        )
    )
    mutations.append(
        any(
            Fraction(2 * m - n - 1, n)
            != sum(
                Fraction(mu[k]) * beta(n, m * k)
                for k in range(1, n // m + 1)
            )
            for n in range(3, 18)
            for m in range(2, n + 1)
        )
    )
    mutations.append(
        row_log_vec(9)
        != {
            **row_log_vec(9),
            2: row_log_vec(9).get(2, Fraction(0)) + 1,
        }
    )
    assert all(mutations)
    counts["mutations_rejected"] = len(mutations)

    proof_object = {
        "arithmetic_class": "EXACT_RATIONAL_AND_INTEGER",
        "cutoff": N,
        "counts": counts,
        "outer_derivative_gate_lower_gt": "6/125",
        "scope": (
            "finite algebra and one elementary sign gate only; "
            "phase renewal, asymptotics, square-screw transfer, and RH not tested"
        ),
    }
    digest = sha256(canonical(proof_object).encode("utf-8")).hexdigest()
    print("PASS_EXACT_CARRY_GREEN_FACTORIZATION")
    print(canonical(proof_object))
    print("proof_object_sha256=" + digest)


if __name__ == "__main__":
    main()
