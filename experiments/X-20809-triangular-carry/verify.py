#!/usr/bin/env python3
"""Exact synthetic and ordinary Riemann reconnaissance for L-20815/T-20805."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from typing import Dict, List


def beta(n: int, q: int) -> Fraction:
    if not (2 <= q <= n):
        return Fraction(0)
    a, r = divmod(n, q)
    return Fraction(a * (q - 1 - r), n + 1)


def brute_beta(n: int, q: int) -> Fraction:
    total = 0
    for j in range(n + 1):
        total += n // q - j // q - (n - j) // q
    return Fraction(total, n + 1)


def backward_exact(target: Dict[int, Fraction], x: int) -> Dict[int, Fraction]:
    c: Dict[int, Fraction] = {}
    for n in range(x, 1, -1):
        used = sum(
            (c[m] * beta(m, n) for m in range(n + 1, x + 1)),
            Fraction(0),
        )
        c[n] = Fraction(n + 1, n - 1) * (target[n] - used)
    return c


def mobius_exact(n: int) -> List[int]:
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


def adjoint_exact(target: Dict[int, Fraction], x: int) -> Dict[int, Fraction]:
    mu = mobius_exact(x)
    u = [Fraction(0) for _ in range(x + 2)]
    for m in range(2, x + 1):
        u[m] = sum(
            (Fraction(mu[k]) * target[m * k] for k in range(1, x // m + 1)),
            Fraction(0),
        )
    z = [Fraction(0) for _ in range(x + 2)]
    for m in range(2, x + 1):
        z[m] = u[m] - u[m + 1]
    cap = [Fraction(0) for _ in range(x + 2)]
    tail = Fraction(0)
    for j in range(x, 1, -1):
        tail += j * z[j]
        cap[j] = tail / (j * (j - 1))
    return {
        j: (j + 1) * (cap[j] - cap[j + 1])
        for j in range(2, x + 1)
    }


def exact_synthetic() -> Dict[str, object]:
    x = 14
    c_true = {
        n: Fraction(n - 1, n * (n + 1))
        for n in range(2, x + 1)
    }
    target = {
        q: sum(
            (c_true[n] * beta(n, q) for n in range(q, x + 1)),
            Fraction(0),
        )
        for q in range(2, x + 1)
    }
    c_back = backward_exact(target, x)
    c_adj = adjoint_exact(target, x)

    for n in range(2, x + 1):
        for q in range(2, n + 1):
            assert beta(n, q) == brute_beta(n, q)
        assert c_back[n] == c_true[n]
        assert c_adj[n] == c_true[n]

    for n in range(2, x + 1):
        for q in range(2, n + 1):
            total_carry = sum(
                n // q - j // q - (n - j) // q
                for j in range(n + 1)
            )
            assert Fraction(total_carry, n + 1) == beta(n, q)

    digest = sum((target[q] for q in target), Fraction(0))
    minimum = min(c_true.values())
    return {
        "classification": (
            "PASS_EXACT_AVERAGED_CARRY_AND_ADJOINT_RECONSTRUCTION"
        ),
        "x": x,
        "coefficient_count": x - 1,
        "target_sum": f"{digest.numerator}/{digest.denominator}",
        "minimum_coefficient": (
            f"{minimum.numerator}/{minimum.denominator}"
        ),
    }


def ordinary_recon(x: int) -> Dict[str, object]:
    if x < 2:
        raise ValueError("x must be at least 2")
    mu = mobius_exact(x)
    w = [0.0] * (x + 1)
    for q in range(2, x + 1):
        w[q] = math.log(x / q) / math.sqrt(q)

    u = [0.0] * (x + 2)
    for k in range(1, x + 1):
        muk = mu[k]
        if muk == 0:
            continue
        for m in range(2, x // k + 1):
            u[m] += muk * w[m * k]

    z = [0.0] * (x + 2)
    for m in range(2, x + 1):
        z[m] = u[m] - u[m + 1]

    cap = [0.0] * (x + 2)
    tail = 0.0
    for j in range(x, 1, -1):
        tail += j * z[j]
        cap[j] = tail / (j * (j - 1))

    c = [0.0] * (x + 1)
    for j in range(2, x + 1):
        c[j] = (j + 1) * (cap[j] - cap[j + 1])

    log_fact = [0.0] * (x + 1)
    cumulative_log_fact = [0.0] * (x + 1)
    for n in range(1, x + 1):
        log_fact[n] = log_fact[n - 1] + math.log(n)
        cumulative_log_fact[n] = (
            cumulative_log_fact[n - 1] + log_fact[n]
        )

    averaged_binomial = [0.0] * (x + 1)
    for n in range(2, x + 1):
        averaged_binomial[n] = (
            log_fact[n]
            - 2.0 * cumulative_log_fact[n] / (n + 1)
        )

    is_prime = bytearray(b"\x01") * (x + 1)
    is_prime[0] = 0
    if x >= 1:
        is_prime[1] = 0
    for p in range(2, math.isqrt(x) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : x + 1 : p] = (
                b"\x00" * (((x - start) // p) + 1)
            )

    von_mangoldt = [0.0] * (x + 1)
    for p in range(2, x + 1):
        if not is_prime[p]:
            continue
        lp = math.log(p)
        pk = p
        while pk <= x:
            von_mangoldt[pk] = lp
            if pk > x // p:
                break
            pk *= p

    binomial_objective = math.fsum(
        c[n] * averaged_binomial[n] for n in range(2, x + 1)
    )
    prime_ramp = math.fsum(
        von_mangoldt[q] * w[q] for q in range(2, x + 1)
    )
    lead = 0.5 * math.fsum(n * c[n] for n in range(2, x + 1))
    positives = [c[n] for n in range(2, x + 1) if c[n] > 0.0]
    negative_count = sum(c[n] < -1e-12 for n in range(2, x + 1))

    return {
        "classification": "ORDINARY_RECONNAISSANCE_NOT_A_CERTIFICATE",
        "x": x,
        "negative_count_below_minus_1e_12": negative_count,
        "minimum_positive_coefficient": min(positives) if positives else 0.0,
        "endpoint_coefficient": c[x],
        "lead": lead,
        "lead_minus_4sqrtx": lead - 4.0 * math.sqrt(x),
        "coefficient_log_budget": math.fsum(
            c[n] * math.log(n + 1) for n in range(2, x + 1)
        ),
        "coefficient_sum": math.fsum(c[2:]),
        "binomial_objective": binomial_objective,
        "prime_ramp": prime_ramp,
        "identity_error": binomial_objective - prime_ramp,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, default=10_000)
    args = parser.parse_args()
    result = {
        "exact": exact_synthetic(),
        "ordinary": ordinary_recon(args.x),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
