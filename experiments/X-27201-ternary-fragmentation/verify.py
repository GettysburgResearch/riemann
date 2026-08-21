#!/usr/bin/env python3
"""Exact algebraic replay for deterministic ternary fragmentation.

Scope: finite rational targets and exact floor identities only. The checker does
not prove positivity for the logarithmic target or RH.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parent


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


def children(n: int) -> Tuple[int, int]:
    a = (n + 2) // 3
    return a, n - a


def carry(n: int, j: int, q: int) -> int:
    return n // q - j // q - (n - j) // q


def continuum_ternary_carry(n: int, q: int) -> int:
    return n // q - n // (3 * q) - (2 * n) // (3 * q)


def ternary_correction(n: int, q: int) -> int:
    a, _ = children(n)
    return int(n % 3 != 0 and a % q == 0)


def target_divergence(w: List[Fraction]) -> Tuple[List[Fraction], List[Fraction]]:
    X = len(w) - 1
    mu = mobius_table(X)
    u = [Fraction(0) for _ in range(X + 2)]
    for m in range(2, X + 1):
        u[m] = sum(Fraction(mu[k]) * w[m * k] for k in range(1, X // m + 1))
    r = [Fraction(0) for _ in range(X + 1)]
    for m in range(2, X + 1):
        r[m] = u[m] - u[m + 1]
    r[1] = -sum(Fraction(m) * r[m] for m in range(2, X + 1))
    return u, r


def ternary_flow(r: List[Fraction]) -> List[Fraction]:
    X = len(r) - 1
    incoming = [Fraction(0) for _ in range(X + 1)]
    A = [Fraction(0) for _ in range(X + 1)]
    for n in range(X, 1, -1):
        A[n] = r[n] + incoming[n]
        a, b = children(n)
        incoming[a] += A[n]
        incoming[b] += A[n]
    A[1] = r[1] + incoming[1]
    return A


def divergence(A: List[Fraction]) -> List[Fraction]:
    X = len(A) - 1
    out = [Fraction(0) for _ in range(X + 1)]
    for n in range(2, X + 1):
        out[n] += A[n]
        a, b = children(n)
        out[a] -= A[n]
        out[b] -= A[n]
    return out


def loads(A: List[Fraction]) -> List[Fraction]:
    X = len(A) - 1
    w = [Fraction(0) for _ in range(X + 1)]
    for q in range(2, X + 1):
        w[q] = sum(A[n] * carry(n, children(n)[0], q) for n in range(q, X + 1))
    return w


def tails(A: List[Fraction]) -> List[Fraction]:
    X = len(A) - 1
    S = [Fraction(0) for _ in range(3 * X + 3)]
    for n in range(X, 0, -1):
        S[n] = S[n + 1] + A[n]
    return S


def base3_digit_sum(n: int) -> int:
    s = 0
    while n:
        s += n % 3
        n //= 3
    return s


def v3(n: int) -> int:
    v = 0
    while n and n % 3 == 0:
        n //= 3
        v += 1
    return v


def proof_object() -> dict:
    split_identity_checks = 0
    for n in range(2, 181):
        a, _ = children(n)
        for q in range(2, n + 1):
            lhs = carry(n, a, q)
            rhs = continuum_ternary_carry(n, q) - ternary_correction(n, q)
            assert lhs == rhs
            split_identity_checks += 1

    digit_checks = 0
    for N in range(1, 2001):
        assert sum(1 - 2 * v3(n) for n in range(1, N + 1)) == base3_digit_sum(N)
        digit_checks += 1

    target_checks = 0
    renewal_checks = 0
    correction_checks = 0
    mutation_failures = 0
    for X in (12, 20, 36, 60):
        w = [Fraction(0) for _ in range(X + 1)]
        for q in range(2, X + 1):
            w[q] = Fraction((X - q) * (X + q + 1), X * q * (q + 1))

        u, r = target_divergence(w)
        A = ternary_flow(r)
        assert divergence(A) == r
        got = loads(A)
        for q in range(2, X + 1):
            assert got[q] == w[q]
            target_checks += 1

        S = tails(A)
        for n in range(2, X + 1):
            alpha = (3 * n + 1) // 2
            beta = 3 * n - 2
            assert S[n] == u[n] + S[alpha] + S[beta]
            assert A[n] == S[n] - S[n + 1]
            renewal_checks += 2

        for q in range(2, X + 1):
            lhs = sum(A[n] * continuum_ternary_carry(n, q) for n in range(q, X + 1))
            E = [Fraction(0) for _ in range((X + 2) // 3 + 2)]
            for m in range(1, len(E)):
                for idx in (3 * m - 2, 3 * m - 1):
                    if 2 <= idx <= X:
                        E[m] += A[idx]
            rhs = w[q] + sum(E[m] for m in range(q, len(E), q))
            assert lhs == rhs
            correction_checks += 1

        bad = False
        for n in range(2, X + 1):
            wrong_j = n // 3
            if wrong_j < 1:
                continue
            for q in range(2, n + 1):
                if carry(n, wrong_j, q) != continuum_ternary_carry(n, q) - ternary_correction(n, q):
                    bad = True
                    break
            if bad:
                break
        assert bad
        mutation_failures += 1

    obj = {
        "classification": "EXACT_TERNARY_FRAGMENTATION_ALGEBRA_VERIFIED",
        "split_identity_checks": split_identity_checks,
        "base3_digit_checks": digit_checks,
        "target_load_checks": target_checks,
        "tail_renewal_checks": renewal_checks,
        "source_correction_checks": correction_checks,
        "mutation_failures": mutation_failures,
        "scope": (
            "Exact finite rational algebra only. This checker does not prove "
            "nonnegativity of the ternary coefficients for the logarithmic target, "
            "MFT, TFP, the sharp prime-ramp bound, or RH."
        ),
    }
    raw = (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode()
    obj["proof_object_sha256"] = hashlib.sha256(raw).hexdigest()
    return obj


def main() -> None:
    obj = proof_object()
    out = ROOT / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")
    print(json.dumps(obj, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
