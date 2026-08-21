#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import comb
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parent


def mobius_table(n: int) -> List[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: List[int] = []
    lp = [0] * (n + 1)
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if p > lp[i] or i * p > n:
                break
            lp[i * p] = p
            if p == lp[i]:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def beta(n: int, q: int) -> Fraction:
    k, r = divmod(n, q)
    return Fraction(k * (q - 1 - r), n + 1)


def carry_count(n: int, q: int) -> int:
    return sum(n // q - j // q - (n - j) // q for j in range(n + 1))


def v_p(n: int, p: int) -> int:
    total = 0
    while n:
        n //= p
        total += n
    return total


def binomial_v_p(n: int, j: int, p: int) -> int:
    return v_p(n, p) - v_p(j, p) - v_p(n - j, p)


def prime_powers(n: int) -> Dict[int, List[int]]:
    out: Dict[int, List[int]] = {}
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if not sieve[p]:
            continue
        out[p] = []
        q = p
        while q <= n:
            out[p].append(q)
            q *= p
        for m in range(p * p, n + 1, p):
            sieve[m] = False
    return out


def inverse_from_w(w: List[Fraction], mu: List[int], X: int) -> List[Fraction]:
    u = [Fraction(0) for _ in range(X + 3)]
    for m in range(2, X + 1):
        u[m] = sum(Fraction(mu[k]) * w[m * k] for k in range(1, X // m + 1))
    tail = [Fraction(0) for _ in range(X + 4)]
    for m in range(X, 1, -1):
        tail[m] = tail[m + 1] + u[m]
    c = [Fraction(0) for _ in range(X + 1)]
    for j in range(2, X + 1):
        c[j] = (
            Fraction(j + 1) * (j * u[j] - (j - 2) * u[j + 1])
            + 2 * tail[j + 2]
        ) / (j * (j - 1))
    return c


def reconstruct(c: List[Fraction], X: int) -> List[Fraction]:
    w = [Fraction(0) for _ in range(X + 1)]
    for q in range(2, X + 1):
        w[q] = sum(c[n] * beta(n, q) for n in range(q, X + 1))
    return w


def aligned_b2(n: int, mu: List[int]) -> int:
    return mu[n] - (mu[n // 2] if n % 2 == 0 else 0)


def aligned_a2(n: int) -> int:
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v + 1


def dirichlet_convolution(a: List[int], b: List[int], N: int) -> List[int]:
    c = [0] * (N + 1)
    for d in range(1, N + 1):
        if a[d] == 0:
            continue
        for m in range(1, N // d + 1):
            if b[m]:
                c[d * m] += a[d] * b[m]
    return c


def digit_sum_2(n: int) -> int:
    return n.bit_count()


def c2(n: int) -> int:
    v = 0
    m = n
    while m % 2 == 0:
        m //= 2
        v += 1
    return 1 - v


def main() -> None:
    N = 80
    mu = mobius_table(N)

    carry_checks = 0
    for n in range(2, 41):
        for q in range(2, n + 1):
            assert carry_count(n, q) == (n + 1) * beta(n, q)
            carry_checks += 1

    affine_checks = 0
    for n in range(2, 61):
        for m in range(2, n + 1):
            lhs = sum(Fraction(mu[k]) * beta(n, m * k)
                      for k in range(1, n // m + 1))
            rhs = Fraction(2 * m - n - 1, n + 1)
            assert lhs == rhs
            affine_checks += 1

    X = 24
    w = [Fraction(0) for _ in range(X + 1)]
    for q in range(2, X + 1):
        w[q] = Fraction((3 * q + 5) % 17 - 8, q + 7)
    c = inverse_from_w(w, mu, X)
    assert reconstruct(c, X) == w

    valuation_checks = 0
    for n in range(2, 31):
        for p, powers in prime_powers(n).items():
            lhs = sum(binomial_v_p(n, j, p) for j in range(n + 1))
            rhs = sum((n + 1) * beta(n, q) for q in powers)
            assert lhs == rhs
            valuation_checks += 1

    b = [0] * (N + 1)
    a = [0] * (N + 1)
    for n in range(1, N + 1):
        b[n] = aligned_b2(n, mu)
        a[n] = aligned_a2(n)
    conv = dirichlet_convolution(a, b, N)
    assert conv[1] == 1
    assert all(conv[n] == 0 for n in range(2, N + 1))

    digit_checks = 0
    running = 0
    for n in range(1, N + 1):
        running += c2(n)
        assert running == digit_sum_2(n)
        digit_checks += 1

    derivative_checks = 0
    for r in range(0, 65):
        assert 8 * (2 ** r) >= 7 + 3 * r
        assert 8 * (2 ** r) >= 3
        derivative_checks += 1

    proof_fields = {
        "verdict": "SYNTHETIC_CARRY_GREEN_ALGEBRA_VERIFIED",
        "carry_checks": carry_checks,
        "affine_mobius_checks": affine_checks,
        "inverse_reconstruction_X": X,
        "valuation_checks": valuation_checks,
        "dyadic_inverse_checks": N,
        "binary_digit_checks": digit_checks,
        "green_derivative_checks": derivative_checks,
        "scope": (
            "Finite exact algebra only. This result does not verify the quotient-layer "
            "identity L-23603.15, continuum positivity, the cofinal minorant, or RH."
        ),
    }
    canonical = json.dumps(proof_fields, sort_keys=True, separators=(",", ":")).encode()
    proof_fields["proof_object_sha256"] = sha256(canonical).hexdigest()
    out = ROOT / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(proof_fields, indent=2, sort_keys=True) + "\n")
    print(json.dumps(proof_fields, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
