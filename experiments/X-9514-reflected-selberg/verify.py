#!/usr/bin/env python3
"""Exact finite Laurent-polynomial replay of L-9516.

The twist n^{-it} is represented by a Laurent monomial in one formal variable
per prime.  A completely additive integer derivation replaces log(n); the
Selberg algebra depends only on additivity and is therefore checked exactly.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import json

LIMIT = 30


def primes_upto(limit: int) -> list[int]:
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    out: list[int] = []
    for n in range(2, limit + 1):
        if sieve[n]:
            out.append(n)
            for m in range(n * n, limit + 1, n):
                sieve[m] = False
    return out


PRIMES = primes_upto(LIMIT)
PINDEX = {p: i for i, p in enumerate(PRIMES)}
DIM = len(PRIMES)
Exp = tuple[int, ...]
Poly = dict[Exp, Fraction]
Seq = list[Poly]


def factor_vector(n: int) -> Exp:
    vector = [0] * DIM
    remaining = n
    for p in PRIMES:
        while remaining % p == 0:
            vector[PINDEX[p]] += 1
            remaining //= p
        if remaining == 1:
            break
    if remaining != 1:
        raise AssertionError(f"factorization failed for {n}")
    return tuple(vector)


def mobius(n: int) -> int:
    vector = factor_vector(n)
    if any(e > 1 for e in vector):
        return 0
    return -1 if sum(vector) % 2 else 1


DERIVATION_WEIGHTS = tuple(range(1, DIM + 1))


def ell(n: int) -> int:
    return sum(e * w for e, w in zip(factor_vector(n), DERIVATION_WEIGHTS))


def poly_add(a: Poly, b: Poly) -> Poly:
    out: defaultdict[Exp, Fraction] = defaultdict(Fraction)
    for key, value in a.items():
        out[key] += value
    for key, value in b.items():
        out[key] += value
    return {key: value for key, value in out.items() if value}


def poly_scale(a: Poly, scalar: Fraction) -> Poly:
    return {key: scalar * value for key, value in a.items() if scalar * value}


def poly_mul(a: Poly, b: Poly) -> Poly:
    out: defaultdict[Exp, Fraction] = defaultdict(Fraction)
    for ka, va in a.items():
        for kb, vb in b.items():
            key = tuple(x + y for x, y in zip(ka, kb))
            out[key] += va * vb
    return {key: value for key, value in out.items() if value}


def monomial(vector: Exp, coefficient: int = 1) -> Poly:
    return {vector: Fraction(coefficient)} if coefficient else {}


def seq_convolve(a: Seq, b: Seq) -> Seq:
    out: Seq = [{} for _ in range(LIMIT + 1)]
    for n in range(1, LIMIT + 1):
        value: Poly = {}
        for d in range(1, n + 1):
            if n % d == 0:
                value = poly_add(value, poly_mul(a[d], b[n // d]))
        out[n] = value
    return out


def seq_linear(a: Seq, b: Seq, sa: int = 1, sb: int = 1) -> Seq:
    out: Seq = [{} for _ in range(LIMIT + 1)]
    for n in range(1, LIMIT + 1):
        out[n] = poly_add(
            poly_scale(a[n], Fraction(sa)),
            poly_scale(b[n], Fraction(sb)),
        )
    return out


def seq_weight(a: Seq, power: int) -> Seq:
    out: Seq = [{} for _ in range(LIMIT + 1)]
    for n in range(1, LIMIT + 1):
        out[n] = poly_scale(a[n], Fraction(ell(n) ** power))
    return out


def generalized_lambda(a: Seq, b: Seq) -> Seq:
    # -A'/A = B * (a ell).
    return seq_convolve(b, seq_weight(a, 1))


def selberg_forcing(a: Seq, b: Seq) -> Seq:
    return seq_convolve(b, seq_weight(a, 2))


def serialize_poly(poly: Poly) -> list[dict[str, object]]:
    rows = []
    for exponent, value in sorted(poly.items()):
        rows.append(
            {
                "exponent": list(exponent),
                "numerator": value.numerator,
                "denominator": value.denominator,
            }
        )
    return rows


def main() -> int:
    a_plus: Seq = [{} for _ in range(LIMIT + 1)]
    a_minus: Seq = [{} for _ in range(LIMIT + 1)]
    b_plus: Seq = [{} for _ in range(LIMIT + 1)]
    b_minus: Seq = [{} for _ in range(LIMIT + 1)]

    for n in range(1, LIMIT + 1):
        vector = factor_vector(n)
        plus = monomial(tuple(-e for e in vector))
        minus = monomial(vector)
        a_plus[n] = plus
        a_minus[n] = minus
        b_plus[n] = poly_scale(plus, Fraction(mobius(n)))
        b_minus[n] = poly_scale(minus, Fraction(mobius(n)))

    a_cross = seq_convolve(a_plus, a_minus)
    b_cross = seq_convolve(b_plus, b_minus)

    lambda_plus = generalized_lambda(a_plus, b_plus)
    lambda_minus = generalized_lambda(a_minus, b_minus)
    lambda_cross = generalized_lambda(a_cross, b_cross)

    forcing_plus = selberg_forcing(a_plus, b_plus)
    forcing_minus = selberg_forcing(a_minus, b_minus)
    forcing_cross = selberg_forcing(a_cross, b_cross)

    for lam, forcing in (
        (lambda_plus, forcing_plus),
        (lambda_minus, forcing_minus),
        (lambda_cross, forcing_cross),
    ):
        rhs = seq_linear(seq_weight(lam, 1), seq_convolve(lam, lam))
        if forcing[1:] != rhs[1:]:
            raise AssertionError("general Selberg identity failed")

    if lambda_cross[1:] != seq_linear(lambda_plus, lambda_minus)[1:]:
        raise AssertionError("product logarithmic derivative failed")

    reflected_left = seq_linear(
        seq_linear(forcing_cross, forcing_plus, 1, -1),
        forcing_minus,
        1,
        -1,
    )
    reflected_right: Seq = [{}] + [
        poly_scale(value, Fraction(2))
        for value in seq_convolve(lambda_plus, lambda_minus)[1:]
    ]

    if reflected_left[1:] != reflected_right[1:]:
        raise AssertionError("reflected Selberg identity failed")

    rows = [
        {
            "n": n,
            "left": serialize_poly(reflected_left[n]),
            "right": serialize_poly(reflected_right[n]),
        }
        for n in range(1, LIMIT + 1)
    ]
    canonical = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    result = {
        "schema": "riemann.x9514-reflected-selberg.v1",
        "verdict": "PASS_EXACT_L9516_REFLECTED_SELBERG_IDENTITY",
        "coefficient_limit": LIMIT,
        "formal_prime_variables": DIM,
        "proof_object_sha256": digest,
        "expected_sha256": "807779c2d1debb67eeb2d971dd244930e5296f3fc014f8197dee43645cc9d94f",
    }
    if digest != result["expected_sha256"]:
        raise AssertionError("proof-object digest mismatch")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
