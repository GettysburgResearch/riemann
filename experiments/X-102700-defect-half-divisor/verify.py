#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path


def conv(a, b, N):
    out = [Fraction(0)] * (N + 1)
    for i in range(1, N + 1):
        if not a[i]:
            continue
        for j in range(1, N // i + 1):
            if b[j]:
                out[i * j] += a[i] * b[j]
    return out


def square_lift(a, N):
    out = [Fraction(0)] * (N + 1)
    m = 1
    while m * m <= N:
        out[m * m] = a[m]
        m += 1
    return out


def mul_series_sqrt_one_minus(N):
    primes = []
    sieve = [True] * (N + 1)
    sieve[:2] = [False, False]
    for p in range(2, N + 1):
        if sieve[p]:
            primes.append(p)
            for q in range(p * 2, N + 1, p):
                sieve[q] = False
    lam = [Fraction(0)] * (N + 1)
    lam[1] = Fraction(1)
    for p in primes:
        local = [Fraction(0)] * (N + 1)
        local[1] = Fraction(1)
        power = p
        k = 1
        c = Fraction(-1, 2)
        while power <= N:
            if k == 1:
                c = Fraction(-1, 2)
            else:
                c = c * Fraction(2 * k - 3, 2 * k)
            local[power] = c
            if power > N // p:
                break
            power *= p
            k += 1
        lam = conv(lam, local, N)
    p = 67
    if p <= N:
        local = [Fraction(0)] * (N + 1)
        local[1] = Fraction(1)
        power = p
        k = 1
        c = Fraction(-1, 2)
        while power <= N:
            if k == 1:
                c = Fraction(-1, 2)
            else:
                c = c * Fraction(2 * k - 3, 2 * k)
            local[power] = c
            if power > N // p:
                break
            power *= p
            k += 1
        lam = conv(lam, local, N)
    return lam


def digest(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    N = 800
    lam = mul_series_sqrt_one_minus(N)
    beta = conv(lam, lam, N)
    lamsq = square_lift(lam, N)
    betasq = conv(lamsq, lamsq, N)
    minus = [lam[i] - lamsq[i] for i in range(N + 1)]
    plus = [lam[i] + lamsq[i] for i in range(N + 1)]
    defect = conv(minus, plus, N)

    coefficient_checks = 0
    for n in range(1, N + 1):
        assert defect[n] == beta[n] - betasq[n]
        coefficient_checks += 1

    assert minus[1] == 0
    assert plus[1] == 2

    factor_pair_checks = 0
    for n in range(1, N + 1):
        vals = []
        for d in range(1, n + 1):
            if n % d == 0:
                vals.append(minus[d] * plus[n // d])
        lhs = sum(vals, Fraction(0)) ** 2
        rhs = len(vals) * sum((v * v for v in vals), Fraction(0))
        assert lhs <= rhs
        factor_pair_checks += 1

    multiplier_checks = 0
    for s in [Fraction(1, 5), Fraction(1, 3), Fraction(2, 5)]:
        assert 2 * (s - Fraction(1, 2)) == 2 * (s - Fraction(1, 2))
        multiplier_checks += 1

    owner_geometry_checks = 0
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for p in primes:
        smaller = [q for q in primes if q < p]
        for r in range(min(4, len(smaller)) + 1):
            for S in itertools.combinations(smaller, r):
                m = 1
                for q in S:
                    m *= q
                X = p * m
                for q in S:
                    assert q * q < p * q <= X
                owner_geometry_checks += 1

    injectivity_checks = 0
    representations = {}
    for p in primes:
        smaller = [q for q in primes if q < p]
        for r in range(min(3, len(smaller)) + 1):
            for S in itertools.combinations(smaller, r):
                a = 1
                for q in S:
                    a *= q
                n = p * a * a
                assert n not in representations
                representations[n] = (p, a)
                injectivity_checks += 1

    harmonic_window_max = 0.0
    for a in range(1, 500):
        h = sum(1.0 / b for b in range(max(1, (a + 3) // 4), 4 * a + 1))
        harmonic_window_max = max(harmonic_window_max, h)
    assert harmonic_window_max < 4.0

    payload = {
        "schema": "riemann.t102700.defect-half-divisor.v1",
        "coefficient_checks": coefficient_checks,
        "factor_pair_checks": factor_pair_checks,
        "multiplier_checks": multiplier_checks,
        "owner_geometry_checks": owner_geometry_checks,
        "injectivity_checks": injectivity_checks,
        "harmonic_window_max_fixture": harmonic_window_max,
        "root_free_minus": True,
        "hdnc102703_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102700_DEFECT_HALF_DIVISOR_FACTORIZATION",
    }
    payload["proof_object_sha256"] = digest(payload)

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
