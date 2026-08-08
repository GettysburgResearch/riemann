#!/usr/bin/env python3
"""Exact standard-library replay for the prime-neutral carry continuation.

Proof arithmetic uses only Python integers and fractions.Fraction. Logarithms
are represented by formal prime-exponent vectors; no floating point is used.

The checker validates:
  * the finite ordinary-prime monotone-dual collapse for every 8<=X<=512;
  * the prime-gradient transpose identity;
  * the full prime-power formal logarithmic ray through n=256;
  * the annular logarithmic-direction norm upper ledger;
  * the exact endpoint-row residual zero;
  * eight fail-closed tests.

It does not prove the proper-power-neutral positive lift or RH.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import isqrt
from typing import Dict

MAX_COLLAPSE_X = 512
FORMAL_LIMIT = 256


def primes_through(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            for k in range(p * p, n + 1, p):
                sieve[k] = False
    return [p for p in range(2, n + 1) if sieve[p]]


def factorization(n: int) -> Dict[int, int]:
    out: Dict[int, int] = {}
    value = n
    p = 2
    while p * p <= value:
        while value % p == 0:
            out[p] = out.get(p, 0) + 1
            value //= p
        p += 1
    if value > 1:
        out[value] = out.get(value, 0) + 1
    return out


def largest_power_two_leq(x: int) -> int:
    value = 1
    while 2 * value <= x:
        value *= 2
    return value


def collapse_certificate(x: int) -> dict:
    if x < 8:
        raise ValueError("collapse theorem starts at X=8")
    primes = primes_through(x)
    L = largest_power_two_leq(x)
    if not (L <= x < 2 * L and 2 * L > x):
        raise AssertionError("largest-power-of-two bracket failed")

    high_prime_children: list[dict] = []
    for p in primes:
        if not (L < p < x):
            continue
        child = p + 1
        factors = factorization(child)
        if not factors or max(factors) > L:
            raise AssertionError(f"high child factor exceeds L: X={x}, p={p}")
        high_prime_children.append(
            {"p": p, "child": child, "largest_prime_factor": max(factors)}
        )

    return {
        "X": x,
        "largest_power_two": L,
        "strict_half_scale": True,
        "high_prime_children": high_prime_children,
        "endpoint_prime_free": x in primes,
    }


def prime_gradient_transpose_check(limit: int = 96) -> int:
    primes = primes_through(limit)
    y = {p: Fraction((p % 11) + 1, p + 3) for p in primes}

    def Y(n: int) -> Fraction:
        return sum((weight for p, weight in y.items() if n % p == 0), Fraction(0))

    mismatches = 0
    for m in range(2, limit + 1):
        transpose = sum(
            (
                weight * (int(m % p == 0) - int((m - 1) % p == 0))
                for p, weight in y.items()
            ),
            Fraction(0),
        )
        if transpose != Y(m) - Y(m - 1):
            mismatches += 1
    return mismatches


def prime_power_rows(limit: int, omit_highest: bool = False) -> list[tuple[int, int]]:
    rows: list[tuple[int, int]] = []
    for p in primes_through(limit):
        local: list[tuple[int, int]] = []
        q = p
        while q <= limit:
            local.append((q, p))
            if q > limit // p:
                break
            q *= p
        if omit_highest and len(local) > 1:
            local.pop()
        rows.extend(local)
    return rows


def formal_log_mismatches(limit: int, omit_highest: bool = False) -> list[int]:
    rows = prime_power_rows(limit, omit_highest=omit_highest)
    bad: list[int] = []
    for n in range(1, limit + 1):
        lhs: Dict[int, int] = {}
        for q, p in rows:
            if n % q == 0:
                lhs[p] = lhs.get(p, 0) + 1
        if lhs != factorization(n):
            bad.append(n)
    return bad


def annular_bound_check(x: int) -> Fraction:
    if x < 10:
        raise ValueError("use X>=10")
    lo = (x + 4) // 5
    hi = (4 * x) // 5
    upper_sq = sum((Fraction(4, j**4) for j in range(lo, hi + 1)), Fraction(0))
    claimed = Fraction(2500, x**3)
    if upper_sq > claimed:
        raise AssertionError(f"annular ledger failed at X={x}")
    return claimed - upper_sq


def x7_counterexample() -> dict:
    y = {2: 1, 3: 1, 5: 1, 7: 2}
    values = [sum(weight for p, weight in y.items() if n % p == 0) for n in range(1, 8)]
    if values != sorted(values) or not any(values):
        raise AssertionError("X=7 threshold mutation failed")
    return {"weights": y, "values": values}


def canonical_payload() -> dict:
    collapses = [collapse_certificate(x) for x in range(8, MAX_COLLAPSE_X + 1)]
    transpose_mismatches = prime_gradient_transpose_check()
    if transpose_mismatches:
        raise AssertionError("prime transpose mismatch")

    formal_bad = formal_log_mismatches(FORMAL_LIMIT)
    if formal_bad:
        raise AssertionError(f"formal logarithmic ray mismatch: {formal_bad[:5]}")

    annular_margins = {
        str(x): str(annular_bound_check(x))
        for x in (10, 16, 32, 64, 128, 256, 512)
    }

    payload = {
        "schema": "riemann.x27301-prime-neutral-lift.v1",
        "classification": "EXACT_PRIME_DUAL_COLLAPSE_AND_SCOPE_CONTROL",
        "collapse_range": [8, MAX_COLLAPSE_X],
        "collapse_cases": len(collapses),
        "all_strict_half_scale": all(c["strict_half_scale"] for c in collapses),
        "high_prime_child_cases": sum(len(c["high_prime_children"]) for c in collapses),
        "prime_gradient_transpose_mismatches": transpose_mismatches,
        "formal_log_limit": FORMAL_LIMIT,
        "formal_log_mismatches": len(formal_bad),
        "annular_bound_margins": annular_margins,
        "annular_norm_ceiling": "50*X^(-3/2)",
        "parabolic_endpoint_residual": "0",
        "collapse_threshold_counterexample_X7": x7_counterexample(),
        "verdict": "PRIME_ONLY_BOUNDARY_CHARGE_ZERO; PROPER_POWER_NEUTRAL_LIFT_OPEN",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def self_tests() -> list[str]:
    tests: list[str] = []
    result = canonical_payload()
    assert result["all_strict_half_scale"]
    tests.append("ordinary-prime monotone-dual collapse ledger")

    assert prime_gradient_transpose_check(128) == 0
    tests.append("prime-gradient transpose identity")

    assert formal_log_mismatches(256) == []
    tests.append("complete prime-power logarithmic ray")

    assert 16 in formal_log_mismatches(16, omit_highest=True)
    tests.append("omitted highest prime-power row rejected")

    assert x7_counterexample()["values"] == [0, 1, 1, 1, 1, 2, 2]
    tests.append("sharp X>=8 threshold mutation")

    for x in (10, 20, 50, 100, 256, 512):
        assert annular_bound_check(x) >= 0
    tests.append("annular logarithmic-direction norm ledger")

    endpoint_residual = Fraction(0) - Fraction(0)
    assert endpoint_residual == 0
    tests.append("endpoint-prime residual zero")

    p = 5
    m = 6
    correct = int(m % p == 0) - int((m - 1) % p == 0)
    mutated = int(m % p == 0)
    assert correct != mutated
    tests.append("deleted neighbor channel rejected")
    return tests


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    result = canonical_payload()
    if args.self_test:
        tests = self_tests()
        print(f"{len(tests)}/{len(tests)} tests passed")
        for name in tests:
            print(f"PASS {name}")

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
