#!/usr/bin/env python3
"""Exact verifier for the fixed-ratio Mertens-shell algebra (X-23401).

Standard library only. All analytic quantities used by the finite regression
are represented by integers or fractions.Fraction. The checker verifies finite
coefficient identities and the exact rational physical-block Gram. It does not
estimate the cofinal shell energy and does not prove RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any, Dict, List, Mapping, Tuple


class VerificationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise VerificationError(message)


def q(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    if isinstance(value, list) and len(value) == 2:
        return Fraction(int(value[0]), int(value[1]))
    if isinstance(value, dict) and set(value) == {"numerator", "denominator"}:
        return Fraction(int(value["numerator"]), int(value["denominator"]))
    fail(f"invalid rational value: {value!r}")


def qjson(value: Fraction) -> Dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def mobius_sieve(limit: int) -> List[int]:
    if limit < 1:
        fail("mobius limit must be positive")
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: List[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if n * p > limit:
                break
            composite[n * p] = True
            if n % p == 0:
                mu[n * p] = 0
                break
            mu[n * p] = -mu[n]
    return mu


def floor_q(value: Fraction) -> int:
    return value.numerator // value.denominator


def mertens(value: Fraction, mu: List[int]) -> int:
    n = floor_q(value)
    if n <= 0:
        return 0
    if n >= len(mu):
        fail(f"mobius table too short for M({value})")
    return sum(mu[1 : n + 1])


def shell(value: Fraction, c: Fraction, mu: List[int]) -> int:
    return mertens(value, mu) - mertens(c * value, mu)


def factorization(n: int) -> Dict[int, int]:
    if n < 1:
        fail("factorization input must be positive")
    out: Dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def is_prime_power(n: int) -> int | None:
    factors = factorization(n)
    if len(factors) == 1:
        return next(iter(factors))
    return None


LogVector = Dict[int, Fraction]


def vadd(a: Mapping[int, Fraction], b: Mapping[int, Fraction], scale: Fraction = Fraction(1)) -> LogVector:
    out: LogVector = dict(a)
    for p, value in b.items():
        out[p] = out.get(p, Fraction(0)) + scale * value
        if out[p] == 0:
            del out[p]
    return out


def vscale(a: Mapping[int, Fraction], scale: Fraction) -> LogVector:
    return {p: scale * value for p, value in a.items() if scale * value}


def log_vector(n: int) -> LogVector:
    return {p: Fraction(e) for p, e in factorization(n).items()}


def lambda_vector(n: int) -> LogVector:
    p = is_prime_power(n)
    return {p: Fraction(1)} if p is not None else {}


def kernel_pair(m: int, n: int, x0: Fraction, x1: Fraction, reciprocal_scale: Fraction) -> Fraction:
    lower = max(x0, Fraction(m), Fraction(n))
    upper = min(x1, reciprocal_scale * m, reciprocal_scale * n)
    if lower >= upper:
        return Fraction(0)
    return Fraction(1, 1) / lower - Fraction(1, 1) / upper


def partition_factorization(x0: Fraction, x1: Fraction, c: Fraction, mu: List[int]) -> Tuple[List[Fraction], List[List[int]], List[Fraction], Fraction]:
    nmax = floor_q(x1)
    points = {x0, x1}
    for n in range(1, nmax + 1):
        for point in (Fraction(n), Fraction(n, 1) / c):
            if x0 < point < x1:
                points.add(point)
    ordered = sorted(points)
    rows: List[List[int]] = []
    weights: List[Fraction] = []
    direct = Fraction(0)
    for left, right in zip(ordered, ordered[1:]):
        middle = (left + right) / 2
        active = [1 if c * middle < n <= middle else 0 for n in range(1, nmax + 1)]
        value = sum(mu[n] * active[n - 1] for n in range(1, nmax + 1))
        weight = Fraction(1, 1) / left - Fraction(1, 1) / right
        rows.append(active)
        weights.append(weight)
        direct += value * value * weight
    return ordered, rows, weights, direct


def verify(certificate: Mapping[str, Any]) -> Dict[str, Any]:
    if certificate.get("schema") != "riemann.x23401.fixed-ratio-shell.v1":
        fail("schema mismatch")

    c = q(certificate["c"])
    if not (Fraction(1, 2) < c < 1):
        fail("the one-prime barrier regression requires 1/2 < c < 1")
    reciprocal_scale = q(certificate["kernel_reciprocal_scale"])
    if reciprocal_scale != 1 / c:
        fail("kernel reciprocal scale is not 1/c")

    max_n = int(certificate["max_n"])
    x_start = int(certificate["x_start"])
    x_stop = int(certificate["x_stop"])
    max_order = int(certificate["max_difference_order"])
    if not (2 <= x_start <= x_stop <= max_n):
        fail("invalid x range")
    if max_order < 1:
        fail("difference order must be positive")

    mu = mobius_sieve(max_n)
    divisor_sign = int(certificate["divisor_recurrence_sign"])
    prime_sign = int(certificate["prime_renewal_sign"])
    binomial_base = int(certificate["binomial_sign_base"])
    mellin_c_sign = int(certificate["mellin_c_term_sign"])
    if divisor_sign not in (-1, 1) or prime_sign not in (-1, 1):
        fail("sign fields must be +/-1")
    if binomial_base not in (-1, 1) or mellin_c_sign not in (-1, 1):
        fail("sign fields must be +/-1")

    divisor_rows = 0
    prime_rows = 0
    difference_rows = 0
    barrier_rows = 0

    for x in range(x_start, x_stop + 1):
        lhs = shell(Fraction(x), c, mu)
        rhs = divisor_sign * sum(shell(Fraction(x, k), c, mu) for k in range(2, x + 1))
        if lhs != rhs:
            fail(f"divisor recurrence failed at x={x}: {lhs} != {rhs}")
        divisor_rows += 1

    for x in range(x_start, x_stop + 1):
        ix = shell(Fraction(x), c, mu)
        lhs = vscale(log_vector(x), Fraction(ix))
        for a in range(1, x + 1):
            ia = shell(Fraction(x, a), c, mu)
            if ia:
                lhs = vadd(lhs, lambda_vector(a), Fraction(prime_sign * ia))
        rhs: LogVector = {}
        for n in range(1, x + 1):
            if c * x < n <= x and mu[n]:
                term = vadd(log_vector(x), log_vector(n), Fraction(-1))
                rhs = vadd(rhs, term, Fraction(mu[n]))
        if lhs != rhs:
            fail(f"formal prime-renewal identity failed at x={x}")
        prime_rows += 1

    for order in range(1, max_order + 1):
        for x in range(1, x_stop + 1):
            point = Fraction(x)
            direct = sum((binomial_base ** j) * comb(order, j) * mertens((c ** j) * point, mu) for j in range(order + 1))
            shells = sum((binomial_base ** r) * comb(order - 1, r) * (mertens((c ** r) * point, mu) - mertens((c ** (r + 1)) * point, mu)) for r in range(order))
            if direct != shells:
                fail(f"high-order shell identity failed at order={order}, x={x}")
            difference_rows += 1

    mellin_rows = 0
    cutoff = int(certificate["mellin_cutoff"])
    if cutoff > max_n:
        fail("mellin cutoff exceeds mobius table")
    for s in map(int, certificate["mellin_orders"]):
        if s <= 0:
            fail("mellin order must be positive")
        lhs = Fraction(0)
        rhs_sum = Fraction(0)
        for n in range(1, cutoff + 1):
            lhs += mu[n] * (Fraction(1, n**s) - Fraction(1, 1) / (Fraction(n, 1) / c) ** s) / s
            rhs_sum += Fraction(mu[n], n**s)
        rhs = (Fraction(1) + mellin_c_sign * c**s) * rhs_sum / s
        if lhs != rhs:
            fail(f"finite Mellin identity failed at s={s}")
        mellin_rows += 1

    gram_rows = []
    for block in certificate["gram_blocks"]:
        x0 = q(block["x0"])
        x1 = q(block["x1"])
        if not (0 < x0 < x1):
            fail("invalid Gram block")
        nmax = floor_q(x1)
        if nmax >= len(mu):
            fail("mobius table too short for Gram block")
        pair_value = Fraction(0)
        matrix = [[Fraction(0) for _ in range(nmax)] for _ in range(nmax)]
        for m in range(1, nmax + 1):
            for n in range(1, nmax + 1):
                entry = kernel_pair(m, n, x0, x1, reciprocal_scale)
                matrix[m - 1][n - 1] = entry
                pair_value += mu[m] * mu[n] * entry

        _, rows, weights, direct_value = partition_factorization(x0, x1, c, mu)
        factor_matrix = [[Fraction(0) for _ in range(nmax)] for _ in range(nmax)]
        for row, weight in zip(rows, weights):
            if weight < 0:
                fail("negative Gram factor weight")
            for i, vi in enumerate(row):
                if not vi:
                    continue
                for j, vj in enumerate(row):
                    if vj:
                        factor_matrix[i][j] += weight
        if factor_matrix != matrix:
            fail(f"Gram factorization mismatch on [{x0},{x1}]")
        if pair_value != direct_value:
            fail(f"Gram quadratic mismatch on [{x0},{x1}]")
        if direct_value < 0:
            fail("negative square energy")
        gram_rows.append({"x0": qjson(x0), "x1": qjson(x1), "segments": len(rows), "energy": qjson(direct_value)})

    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        d = 2
        while d * d <= p:
            if p % d == 0:
                return False
            d += 1
        return True

    primes = [p for p in range(2, int(certificate["barrier_prime_max"]) + 1) if is_prime(p)]
    for x in range(x_start, x_stop + 1):
        for n in range(1, x + 1):
            if not (c * x < n <= x):
                continue
            for p in primes:
                if not (p * n > x):
                    fail("multiplication by one prime stayed in the shell")
                if not (Fraction(n, p) < c * x):
                    fail("division by one prime stayed in the shell")
                barrier_rows += 1

    result: Dict[str, Any] = {
        "schema": "riemann.x23401.fixed-ratio-shell.result.v1",
        "verified": True,
        "c": qjson(c),
        "max_n": max_n,
        "divisor_recurrence_rows": divisor_rows,
        "prime_renewal_rows": prime_rows,
        "high_order_rows": difference_rows,
        "finite_mellin_rows": mellin_rows,
        "one_prime_barrier_rows": barrier_rows,
        "gram_blocks": gram_rows,
        "verdict": "EXACT_FIXED_RATIO_MERTENS_SHELL_ALGEBRA_VERIFIED",
        "proof_boundary": "Finite integer/Fraction algebra and Gram factorization only; no cofinal shell-energy estimate, Type-II bound, Mertens estimate, or RH claim is certified.",
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode("utf-8")
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()

    expected = certificate.get("expected_proof_object_sha256")
    if expected is not None and result["proof_object_sha256"] != expected:
        fail("proof-object digest mismatch")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        certificate = json.loads(args.certificate.read_text())
        result = verify(certificate)
    except (OSError, ValueError, KeyError, TypeError, VerificationError) as exc:
        print(f"VERIFICATION_FAILED: {exc}")
        return 1
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
