#!/usr/bin/env python3
"""Exact finite replay for L-32301/L-32302.

Standard-library only.  This checker authenticates finite Markov and Möbius-floor
algebra.  It does not prove a cofinal sign theorem or RH.
"""
from __future__ import annotations

from fractions import Fraction
import json
import hashlib


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    comp = [False] * (n + 1)
    for m in range(2, n + 1):
        if not comp[m]:
            primes.append(m)
            mu[m] = -1
        for p in primes:
            if m * p > n:
                break
            comp[m * p] = True
            if m % p == 0:
                mu[m * p] = 0
                break
            mu[m * p] = -mu[m]
    return mu


def children(m: int) -> list[int]:
    return [m // 2, m - m // 2, (m + 2) // 3, m - (m + 2) // 3]


def q_transition(m: int, n: int) -> Fraction:
    mult = sum(1 for c in children(m) if c == n)
    return Fraction(n * mult, 2 * m)


def hitting(target: int, start: int) -> Fraction:
    if start < target:
        return Fraction(0)
    h = [Fraction(0) for _ in range(start + 1)]
    h[target] = Fraction(1)
    for m in range(target + 1, start + 1):
        h[m] = sum(q_transition(m, c) * h[c] for c in set(children(m)))
    return h[start]


def ternary_support(n: int) -> list[int]:
    lo = (3 * n + 1) // 2
    # ceil(3(n+1)/2)-1
    hi = (3 * (n + 1) + 1) // 2 - 1
    return [p for p in range(lo, min(hi, 2 * n - 1) + 1)]


def check_sparse_hitting(limit: int = 250) -> int:
    cases = 0
    for n in range(2, limit + 1):
        support = set(ternary_support(n)) | {2 * n - 1}
        for p in range(n + 1, 2 * n):
            exact = hitting(n, p)
            direct = q_transition(p, n)
            assert exact == direct, (n, p, exact, direct)
            if p not in support:
                assert exact == 0, (n, p, exact)
            cases += 1
    return cases


def check_mobius_floor(limit: int = 5000) -> int:
    mu = mobius_sieve(limit)
    cases = 0
    for m in range(2, limit + 1):
        value = -sum(mu[q] * (m // q) for q in range(2, m + 1))
        assert value == m - 1, (m, value)
        cases += 1
    return cases


def check_constant_split_defect(limit: int = 300) -> int:
    cases = 0
    for n in range(2, limit + 1):
        for j in range(1, n):
            defect = (n - 1) - (j - 1) - (n - j - 1)
            assert defect == 1
            cases += 1
    return cases


def main() -> None:
    checks = {
        "sparse_first_entrance_hitting": check_sparse_hitting(),
        "mobius_floor_affine_projection": check_mobius_floor(),
        "constant_affine_split_defect": check_constant_split_defect(),
    }
    payload = {
        "schema": "riemann.x32301.shakeup-firewalls.v1",
        "classification": "EXACT_SPARSE_FIRST_ENTRANCE_AND_RIESZ_FIREWALL_REPLAY",
        "checks": checks,
        "does_not_prove": [
            "the Mobius-Riesz one-sign inequality",
            "a five-adic source-specific contraction",
            "producer positivity",
            "RH",
        ],
    }
    canonical = json.dumps(payload, sort_keys=True).encode("utf-8")
    payload["sha256_without_digest"] = hashlib.sha256(canonical).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
