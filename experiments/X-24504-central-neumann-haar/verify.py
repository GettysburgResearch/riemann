#!/usr/bin/env python3
"""Exact/directed verifier for the central-Neumann Haar potential.

Exact Fraction checks validate the finite algebra on rational targets.
A directed Decimal computation certifies that pure central positivity is false
for the actual critical target at X=10050, n=11.

This checker proves no asymptotic variation estimate and no RH claim.
"""
from __future__ import annotations

from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction
import hashlib
import json


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            m = n * p
            if m > limit:
                break
            composite[m] = True
            if n % p == 0:
                mu[m] = 0
                break
            mu[m] = -mu[n]
    return mu


def central_carry(n: int, q: int) -> int:
    j = n // 2
    return n // q - j // q - (n - j) // q


def exact_checks() -> dict[str, int]:
    X = 64
    mu = mobius_sieve(X)
    # A deliberately irregular rational target with zero padding.
    w = [Fraction(0) for _ in range(X + 2)]
    for q in range(2, X + 1):
        w[q] = Fraction((X - q) * (q + 3), q * (X + 5))

    U = [Fraction(0) for _ in range(X + 2)]
    for m in range(1, X + 1):
        for k in range(1, X // m + 1):
            q = k * m
            if q >= 2:
                U[m] += mu[k] * w[q]
    R = [Fraction(0) for _ in range(X + 2)]
    for n in range(1, X + 1):
        R[n] = U[n] - U[n + 1]

    incoming = [Fraction(0) for _ in range(X + 2)]
    A = [Fraction(0) for _ in range(X + 2)]
    recurrence_rows = 0
    for n in range(X, 1, -1):
        A[n] = R[n] + incoming[n]
        j = n // 2
        incoming[j] += A[n]
        incoming[n - j] += A[n]
        recurrence_rows += 1

    # Tent Green formula and Haar potential.
    A_tent = [Fraction(0) for _ in range(X + 2)]
    G = [Fraction(0) for _ in range(X + 2)]
    tent_rows = 0
    haar_blocks = 0
    for n in range(2, X + 1):
        scale = 1
        while scale * (n - 1) < X:
            for m in range(
                max(1, scale * (n - 1) + 1),
                min(X, scale * (n + 1) - 1) + 1,
            ):
                k = max(Fraction(0), Fraction(scale - abs(m - scale * n)))
                A_tent[n] += k * R[m]
                if k:
                    tent_rows += 1
            left = max(1, scale * (n - 1) + 1)
            right = min(X, scale * n)
            for m in range(left, right + 1):
                G[n] += U[m]
                haar_blocks += 1
            scale *= 2

    assert A[2:] == A_tent[2:]
    for n in range(2, X + 1):
        assert A[n] == G[n] - G[n + 1]
        rhs = U[n]
        if 2 * n - 1 <= X:
            rhs += G[2 * n - 1]
        if 2 * n <= X:
            rhs += G[2 * n]
        assert G[n] == rhs

    # Exact central-column saturation.
    saturation_rows = 0
    for q in range(2, X + 1):
        load = sum(A[n] * central_carry(n, q) for n in range(q, X + 1))
        assert load == w[q]
        saturation_rows += 1

    # Dyadic shell linearity at Y=floor(X/2).
    Y = X // 2
    wY = [Fraction(0) for _ in range(Y + 2)]
    for q in range(2, Y + 1):
        wY[q] = Fraction((Y - q) * (q + 3), q * (Y + 5))

    def central_inverse(target: list[Fraction], endpoint: int) -> list[Fraction]:
        mu0 = mobius_sieve(endpoint)
        u0 = [Fraction(0) for _ in range(endpoint + 2)]
        for m in range(1, endpoint + 1):
            for k in range(1, endpoint // m + 1):
                q = k * m
                if q >= 2:
                    u0[m] += mu0[k] * target[q]
        inc0 = [Fraction(0) for _ in range(endpoint + 2)]
        out = [Fraction(0) for _ in range(endpoint + 2)]
        for n in range(endpoint, 1, -1):
            out[n] = u0[n] - u0[n + 1] + inc0[n]
            j = n // 2
            inc0[j] += out[n]
            inc0[n - j] += out[n]
        return out

    AY = central_inverse(wY, Y)
    shell_target = [Fraction(0) for _ in range(X + 2)]
    for q in range(2, X + 1):
        shell_target[q] = w[q] - (wY[q] if q <= Y else 0)
    BS = central_inverse(shell_target, X)
    shell_rows = 0
    for n in range(2, X + 1):
        assert A[n] == BS[n] + (AY[n] if n <= Y else 0)
        shell_rows += 1

    return {
        "recurrence_rows": recurrence_rows,
        "tent_terms": tent_rows,
        "haar_terms": haar_blocks,
        "saturation_rows": saturation_rows,
        "shell_rows": shell_rows,
    }


PREC = 100
LOW = Context(prec=PREC, rounding=ROUND_FLOOR)
HIGH = Context(prec=PREC, rounding=ROUND_CEILING)
Interval = tuple[Decimal, Decimal]
ZERO: Interval = (Decimal(0), Decimal(0))


def iadd(a: Interval, b: Interval) -> Interval:
    return LOW.add(a[0], b[0]), HIGH.add(a[1], b[1])


def ineg(a: Interval) -> Interval:
    return -a[1], -a[0]


def isub(a: Interval, b: Interval) -> Interval:
    return iadd(a, ineg(b))


def directed_counterexample() -> dict[str, object]:
    X = 10050
    target_n = 11
    mu = mobius_sieve(X)
    target = [ZERO for _ in range(X + 2)]
    dx = Decimal(X)
    for q in range(2, X):
        dq = Decimal(q)
        log_lo = LOW.subtract(LOW.ln(dx), HIGH.ln(dq))
        log_hi = HIGH.subtract(HIGH.ln(dx), LOW.ln(dq))
        sqrt_lo = LOW.sqrt(dq)
        sqrt_hi = HIGH.sqrt(dq)
        target[q] = (
            LOW.divide(log_lo, sqrt_hi),
            HIGH.divide(log_hi, sqrt_lo),
        )

    U = [ZERO for _ in range(X + 2)]
    for k in range(1, X + 1):
        if mu[k] == 0:
            continue
        for m in range(1, X // k + 1):
            q = k * m
            if q < 2:
                continue
            term = target[q] if mu[k] > 0 else ineg(target[q])
            U[m] = iadd(U[m], term)

    incoming = [ZERO for _ in range(X + 2)]
    coefficient = [ZERO for _ in range(X + 2)]
    for n in range(X, 1, -1):
        coefficient[n] = iadd(isub(U[n], U[n + 1]), incoming[n])
        j = n // 2
        incoming[j] = iadd(incoming[j], coefficient[n])
        incoming[n - j] = iadd(incoming[n - j], coefficient[n])

    interval = coefficient[target_n]
    assert interval[1] < 0
    return {
        "X": X,
        "index": target_n,
        "coefficient_interval": [str(interval[0]), str(interval[1])],
        "strictly_negative": True,
        "precision": PREC,
    }


def main() -> None:
    exact = exact_checks()
    counterexample = directed_counterexample()
    payload = {
        "schema": "riemann.x24504.central-neumann-haar.v1",
        "verdict": "PASS_EXACT_HAAR_AND_DIRECTED_CENTRAL_NEGATIVITY",
        "exact": exact,
        "counterexample": counterexample,
    }
    payload["content_sha256"] = hashlib.sha256(
        json.dumps(payload, sort_keys=True).encode("utf-8")
    ).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
