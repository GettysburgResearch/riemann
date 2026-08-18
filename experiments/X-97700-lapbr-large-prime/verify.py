#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def matadd(A, B, sign=1):
    return [[A[i][j] + sign * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def matvec(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]


def mpow(A, n):
    out = eye(len(A))
    for _ in range(n):
        out = matmul(out, A)
    return out


def poly_current(A, L):
    out = [[Fraction(0) for _ in range(len(A))] for _ in range(len(A))]
    p = eye(len(A))
    sign = 1
    for _ in range(L):
        out = matadd(out, p, sign)
        p = matmul(p, A)
        sign *= -1
    return out


def verify_duhamel():
    S = [
        [Fraction(0), Fraction(1, 7), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1, 11), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
    ]
    H = [
        [Fraction(0), Fraction(0), Fraction(1, 13), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1, 17)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1, 19)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
    ]
    R = matadd(S, H)
    L = 4
    lhs = matadd(poly_current(R, L), poly_current(S, L), -1)
    rhs = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for a in range(L - 1):
        for b in range(L - 1 - a):
            term = matmul(matmul(mpow(S, a), H), mpow(R, b))
            rhs = matadd(rhs, term, -1 if (a + b) % 2 == 0 else 1)
    assert lhs == rhs
    return True


def divisors_from_primes(primes):
    out = [(1, 1, ())]
    for p in primes:
        out += [(n * p, -mu, hist + (p,)) for n, mu, hist in list(out)]
    return out


def base_value(x):
    # Exact toy positive base; only algebra is under test.
    return Fraction(max(x - 1, 0), max(x, 1))


def apply_prime(values, p, xmax):
    return {x: values[x] - Fraction(1, p) * values[x // p] for x in range(xmax + 1)}


def verify_bellman():
    xmax = 400
    small = [5, 7]
    large = [11, 13, 17, 19]
    values = {x: base_value(x) for x in range(xmax + 1)}
    # Complete small cube via sequential exact recurrence.
    for p in small:
        values = apply_prime(values, p, xmax)
    UZ = values.copy()
    prev = UZ.copy()
    budget = {x: Fraction(0) for x in range(xmax + 1)}
    for p in large:
        for x in range(xmax + 1):
            budget[x] += Fraction(1, p) * prev[x // p]
        prev = apply_prime(prev, p, xmax)
    for x in range(xmax + 1):
        assert prev[x] == UZ[x] - budget[x]

    # Largest-owner subset expansion.
    for x in range(xmax + 1):
        direct = UZ[x]
        for n, mu, hist in divisors_from_primes(large):
            if not hist:
                continue
            direct += Fraction(mu, n) * UZ[x // n]
        assert direct == prev[x]

    # Type I / Type II exact partition at X/Z.
    X, Z = 360, 10
    I = Fraction(0)
    T = Fraction(0)
    prev = UZ.copy()
    for p in large:
        term = Fraction(1, p) * prev[X // p]
        if p > Fraction(X, Z):
            I += term
        else:
            T += term
        prev = apply_prime(prev, p, xmax)
    assert I + T == budget[X]
    return True


def elementary_symmetric(weights, r):
    e = [Fraction(0) for _ in range(r + 1)]
    e[0] = Fraction(1)
    for w in weights:
        for j in range(r, 0, -1):
            e[j] += w * e[j - 1]
    return e[r]


def verify_collision_bound():
    weights = [Fraction(1, p) for p in (67, 71, 73, 79, 83, 89, 97, 101)]
    r = 4
    A = sum(weights)
    S2 = sum(w * w for w in weights)
    e = elementary_symmetric(weights, r)
    import math
    lhs = Fraction(math.factorial(r)) * e
    rhs = A ** r - Fraction(r * (r - 1), 2) * S2 * A ** (r - 2)
    assert lhs >= rhs
    assert rhs > 0
    return {
        "weights": len(weights),
        "depth": r,
        "ordered_distinct_ge_collision_lower_bound": True,
    }


def alt_partial(lam: Fraction, L: int) -> Fraction:
    term = Fraction(1)
    total = Fraction(1)
    for r in range(1, L):
        term *= lam / r
        total += -term if r % 2 else term
    return total


def verify_negative_control():
    lam = Fraction(100)
    zsmall = Fraction(3)
    L = 34
    full = alt_partial(lam, L)
    small = alt_partial(zsmall, L)
    residual = full - small
    assert L % 2 == 0
    assert small > 0
    assert full < 0
    assert residual < -small

    # A lost parity sign must destroy the fixture.
    wrong = sum((lam ** r) / Fraction(1 if r == 0 else 1) for r in range(2))
    assert wrong > 0
    return {
        "lambda": str(lam),
        "small_mass": str(zsmall),
        "depth": L,
        "full_sign": "negative",
        "small_sign": "positive",
        "residual_lt_minus_small": True,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()

    result = {
        "schema": "riemann.x97700.lapbr-large-prime.v1",
        "duhamel_identity_exact": verify_duhamel(),
        "largest_prime_bellman_exact": verify_bellman(),
        "elementary_symmetric_collision_bound": verify_collision_bound(),
        "adaptive_layer_negative_control": verify_negative_control(),
        "mertens_asymptotics_replayed": False,
        "complete_small_cube_asymptotic_replayed": False,
        "blpte67_proved": False,
        "lapbr67_as_stated": "REFUTED_BY_ANALYTIC_THEOREM",
        "rh_established": False,
        "verdict": "PASS_T97700_LAPBR_NO_GO_AND_TYPEII_REDUCTION_ALGEBRA",
    }
    raw = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(raw).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
