#!/usr/bin/env python3
"""Exact replay for squarefree composite collector blocks.

Uses only Python integers and fractions.Fraction.  It does not prove the
all-scale Squarefree Collector Lift or RH.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import isqrt


def primes_through(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            for k in range(p * p, n + 1, p):
                sieve[k] = False
    return [p for p in range(2, n + 1) if sieve[p]]


def prime_powers(n: int) -> list[tuple[int, int]]:
    rows: list[tuple[int, int]] = []
    for p in primes_through(n):
        q = p
        while q <= n:
            rows.append((q, p))
            if q > n // p:
                break
            q *= p
    return rows


def factorization(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
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


def squarefree(n: int) -> bool:
    return all(exponent == 1 for exponent in factorization(n).values())


def block(a: int, b: int, amount: Fraction) -> list[Fraction]:
    if not (1 <= a < b):
        raise ValueError("require 1<=A<B")
    values = [Fraction(0) for _ in range(b + 2)]
    for m in range(a + 1, b + 1):
        values[m] = amount
    return values


def response(values: list[Fraction], q: int) -> Fraction:
    return sum(
        (
            values[m] * (int(m % q == 0) - int((m - 1) % q == 0))
            for m in range(2, len(values))
        ),
        Fraction(0),
    )


def build_result() -> dict:
    a, b = 30, 43
    amount = Fraction(7, 5)
    if not (squarefree(a) and squarefree(b)):
        raise AssertionError("control endpoints must be squarefree")

    values = block(a, b, amount)
    prime_response = {
        p: response(values, p)
        for p in primes_through(b)
        if response(values, p)
    }
    expected = {
        2: -amount,
        3: -amount,
        5: -amount,
        43: amount,
    }
    if prime_response != expected:
        raise AssertionError(f"prime response mismatch: {prime_response}")

    proper_rows = [q for q, p in prime_powers(b) if q != p]
    proper_mismatches = [q for q in proper_rows if response(values, q)]
    if proper_mismatches:
        raise AssertionError(f"proper-power leakage: {proper_mismatches}")

    incidence_change = sum(prime_response.values(), Fraction(0))
    if incidence_change != -2 * amount:
        raise AssertionError("incidence compression mismatch")

    payload = {
        "schema": "riemann.x27303-squarefree-collector.v1",
        "classification": "EXACT_SQUAREFREE_COLLECTOR_INCIDENCE_CONTROL",
        "A": a,
        "B": b,
        "amount": str(amount),
        "prime_response": {str(p): str(value) for p, value in prime_response.items()},
        "proper_power_rows": proper_rows,
        "proper_power_mismatches": len(proper_mismatches),
        "prime_incidence_change": str(incidence_change),
        "omega_A": len(factorization(a)),
        "omega_B": len(factorization(b)),
        "formal_objective_ratio": "43/30",
        "verdict": "PASS_EXACT_SQUAREFREE_COLLECTOR_ALGEBRA",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def self_tests() -> list[str]:
    tests: list[str] = []
    result = build_result()
    assert result["proper_power_mismatches"] == 0
    tests.append("squarefree endpoints preserve every proper power")

    assert result["prime_incidence_change"] == "-14/5"
    tests.append("composite collector compresses prime incidence")

    amount = Fraction(1)
    mutated = block(12, 43, amount)
    assert response(mutated, 4) == -amount
    tests.append("nonsquarefree source endpoint rejected")

    mutated_target = block(30, 44, amount)
    assert response(mutated_target, 4) == amount
    tests.append("nonsquarefree target endpoint rejected")

    control = block(30, 43, amount)
    assert response(control, 2) == -amount
    assert response(control, 43) == amount
    tests.append("collector orientation")

    return tests


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    result = build_result()
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
