#!/usr/bin/env python3
"""Directed finite verifier for the mixed one-third/half Pascal renewal.

This checks one fixed endpoint only. It does not certify MPR cofinally and does
not prove RH.
"""
from __future__ import annotations

from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR
import json

PREC = 90
LOW = Context(prec=PREC, rounding=ROUND_FLOOR)
HIGH = Context(prec=PREC, rounding=ROUND_CEILING)
X = 4096

Interval = tuple[Decimal, Decimal]
ZERO: Interval = (Decimal(0), Decimal(0))


def add(a: Interval, b: Interval) -> Interval:
    return LOW.add(a[0], b[0]), HIGH.add(a[1], b[1])


def sub(a: Interval, b: Interval) -> Interval:
    return LOW.subtract(a[0], b[1]), HIGH.subtract(a[1], b[0])


def scale(a: Interval, numerator: int, denominator: int) -> Interval:
    n = Decimal(numerator)
    d = Decimal(denominator)
    return (
        LOW.divide(LOW.multiply(a[0], n), d),
        HIGH.divide(HIGH.multiply(a[1], n), d),
    )


def target_interval(q: int) -> Interval:
    if q == X:
        return ZERO
    dx = Decimal(X)
    dq = Decimal(q)
    log_low = LOW.subtract(LOW.ln(dx), HIGH.ln(dq))
    log_high = HIGH.subtract(HIGH.ln(dx), LOW.ln(dq))
    sqrt_low = LOW.sqrt(dq)
    sqrt_high = HIGH.sqrt(dq)
    return LOW.divide(log_low, sqrt_high), HIGH.divide(log_high, sqrt_low)


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


def main() -> None:
    mu = mobius_sieve(X)
    target = [ZERO for _ in range(X + 2)]
    for q in range(2, X + 1):
        target[q] = target_interval(q)

    multiple_mobius = [ZERO for _ in range(X + 2)]
    for k in range(1, X + 1):
        if mu[k] == 0:
            continue
        for m in range(1, X // k + 1):
            q = k * m
            if q < 2:
                continue
            term = target[q]
            if mu[k] < 0:
                term = (-term[1], -term[0])
            multiple_mobius[m] = add(multiple_mobius[m], term)

    divergence = [ZERO for _ in range(X + 1)]
    for n in range(1, X + 1):
        divergence[n] = sub(multiple_mobius[n], multiple_mobius[n + 1])

    incoming = [ZERO for _ in range(X + 1)]
    coefficient = [ZERO for _ in range(X + 1)]
    for n in range(X, 1, -1):
        coefficient[n] = add(divergence[n], incoming[n])
        j3 = max(1, n // 3)
        j2 = max(1, n // 2)
        term3 = scale(coefficient[n], 31, 32)
        term2 = scale(coefficient[n], 1, 32)
        incoming[j3] = add(incoming[j3], term3)
        incoming[n - j3] = add(incoming[n - j3], term3)
        incoming[j2] = add(incoming[j2], term2)
        incoming[n - j2] = add(incoming[n - j2], term2)

    uncertified = [n for n in range(2, X) if coefficient[n][0] <= 0]
    strict = [(coefficient[n][0], n) for n in range(2, X) if coefficient[n][0] > 0]
    terminal = add(divergence[1], incoming[1])
    verdict = (
        "PASS_DIRECTED_FINITE_MIXED_PASCAL"
        if not uncertified and terminal[0] <= 0 <= terminal[1]
        else "FAIL"
    )
    result = {
        "schema": "riemann.x23803.mixed-pascal-directed.v1",
        "verdict": verdict,
        "X": X,
        "precision": PREC,
        "weights": ["31/32", "1/32"],
        "strict_positive_rows": len(strict),
        "uncertified_rows": uncertified,
        "minimum_strict_lower": str(min(strict)[0]) if strict else None,
        "minimum_strict_index": min(strict)[1] if strict else None,
        "terminal_divergence_interval": [str(terminal[0]), str(terminal[1])],
        "scope": "finite directed check only; not MPR/BCT/RH",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if verdict != "PASS_DIRECTED_FINITE_MIXED_PASCAL":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
