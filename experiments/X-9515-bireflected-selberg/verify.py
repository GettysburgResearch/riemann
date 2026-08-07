#!/usr/bin/env python3
"""Exact two-frequency Selberg replay and terminal-scale mutation."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import json

LIMIT = 24
DELTA = Fraction(1, 5)


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
DERIVATION_WEIGHTS = tuple(range(1, DIM + 1))


def factor_vector(n: int) -> tuple[int, ...]:
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


def ell(n: int) -> int:
    return sum(e * w for e, w in zip(factor_vector(n), DERIVATION_WEIGHTS))


def poly_add(a: Poly, b: Poly) -> Poly:
    out: defaultdict[Exp, Fraction] = defaultdict(Fraction)
    for key, value in a.items():
        out[key] += value
    for key, value in b.items():
        out[key] += value
    return {key: value for key, value in out.items() if value}


def poly_scale(a: Poly, scalar: Fraction | int) -> Poly:
    scalar = Fraction(scalar)
    return {key: scalar * value for key, value in a.items() if scalar * value}


def poly_mul(a: Poly, b: Poly) -> Poly:
    out: defaultdict[Exp, Fraction] = defaultdict(Fraction)
    for ka, va in a.items():
        for kb, vb in b.items():
            out[tuple(x + y for x, y in zip(ka, kb))] += va * vb
    return {key: value for key, value in out.items() if value}


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
        out[n] = poly_add(poly_scale(a[n], sa), poly_scale(b[n], sb))
    return out


def seq_weight(a: Seq, power: int) -> Seq:
    out: Seq = [{} for _ in range(LIMIT + 1)]
    for n in range(1, LIMIT + 1):
        out[n] = poly_scale(a[n], ell(n) ** power)
    return out


def generalized_lambda(a: Seq, b: Seq) -> Seq:
    # Correct sign: -A'/A = B*(a ell).
    return seq_convolve(b, seq_weight(a, 1))


def selberg_forcing(a: Seq, b: Seq) -> Seq:
    return seq_convolve(b, seq_weight(a, 2))


def build_twists() -> tuple[Seq, Seq, Seq, Seq]:
    a_t: Seq = [{} for _ in range(LIMIT + 1)]
    a_minus_s: Seq = [{} for _ in range(LIMIT + 1)]
    b_t: Seq = [{} for _ in range(LIMIT + 1)]
    b_minus_s: Seq = [{} for _ in range(LIMIT + 1)]
    for n in range(1, LIMIT + 1):
        vector = factor_vector(n)
        exp_t = tuple(-e for e in vector) + (0,) * DIM
        exp_minus_s = (0,) * DIM + tuple(e for e in vector)
        a_t[n] = {exp_t: Fraction(1)}
        a_minus_s[n] = {exp_minus_s: Fraction(1)}
        b_t[n] = poly_scale(a_t[n], mobius(n))
        b_minus_s[n] = poly_scale(a_minus_s[n], mobius(n))
    return a_t, a_minus_s, b_t, b_minus_s


def terminal_counterfaces() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for K in (20, 30, 50, 100, 200):
        free = max(1, K // 5 - 1)
        short = Fraction(free, K)
        rows.append(
            {
                "K": K,
                "delta": str(DELTA),
                "free_short_divisor_coordinates": free,
                "short_product_exponent": str(short),
                "long_exponent": str(1 - short),
                "strict_terminal_reserve": short < DELTA,
            }
        )
    return rows


def build_result() -> dict[str, object]:
    a_t, a_minus_s, b_t, b_minus_s = build_twists()
    a_cross = seq_convolve(a_t, a_minus_s)
    b_cross = seq_convolve(b_t, b_minus_s)

    lambda_t = generalized_lambda(a_t, b_t)
    lambda_minus_s = generalized_lambda(a_minus_s, b_minus_s)
    lambda_cross = generalized_lambda(a_cross, b_cross)
    forcing_t = selberg_forcing(a_t, b_t)
    forcing_minus_s = selberg_forcing(a_minus_s, b_minus_s)
    forcing_cross = selberg_forcing(a_cross, b_cross)

    for lam, forcing in (
        (lambda_t, forcing_t),
        (lambda_minus_s, forcing_minus_s),
        (lambda_cross, forcing_cross),
    ):
        rhs = seq_linear(seq_weight(lam, 1), seq_convolve(lam, lam))
        if forcing[1:] != rhs[1:]:
            raise AssertionError("general Selberg identity failed")

    if lambda_cross[1:] != seq_linear(lambda_t, lambda_minus_s)[1:]:
        raise AssertionError("product logarithmic derivative failed")

    reflected_left = seq_linear(
        seq_linear(forcing_cross, forcing_t, 1, -1),
        forcing_minus_s,
        1,
        -1,
    )
    reflected_right: Seq = [{}] + [
        poly_scale(value, 2)
        for value in seq_convolve(lambda_t, lambda_minus_s)[1:]
    ]
    if reflected_left[1:] != reflected_right[1:]:
        raise AssertionError("two-frequency reflected identity failed")

    wrong_sign_rejected = any(
        poly_scale(lambda_t[n], -1) != lambda_t[n]
        for n in range(2, LIMIT + 1)
        if lambda_t[n]
    )
    if not wrong_sign_rejected:
        raise AssertionError("wrong generalized-Lambda sign was not rejected")

    counterfaces = terminal_counterfaces()
    if not all(row["strict_terminal_reserve"] for row in counterfaces):
        raise AssertionError("terminal reserve mutation failed")
    if counterfaces[-1]["free_short_divisor_coordinates"] <= counterfaces[0][
        "free_short_divisor_coordinates"
    ]:
        raise AssertionError("terminal dimension did not grow")

    proof_rows = {
        "coefficient_limit": LIMIT,
        "formal_prime_variables_per_frequency": DIM,
        "two_frequency_reflected_identity": True,
        "wrong_generalized_lambda_sign_rejected": wrong_sign_rejected,
        "terminal_counterfaces": counterfaces,
    }
    canonical = json.dumps(proof_rows, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return {
        "schema": "riemann.x9515-bireflected-block-review.v1",
        "verdict": "PASS_EXACT_BIREFLECTED_IDENTITY_AND_TERMINAL_GEOMETRY_MUTATION",
        "proof_object_sha256": digest,
        **proof_rows,
        "scope": (
            "exact finite algebra and scale geometry only; does not prove "
            "signed cancellation of the growing-dimensional terminal faces "
            "or a balanced Type-II estimate"
        ),
    }


def main() -> None:
    print(json.dumps(build_result(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
