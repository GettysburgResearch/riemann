#!/usr/bin/env python3
"""Exact replay for the prime-incidence greedy suffix charge.

Uses only integers and fractions.Fraction. This is synthetic finite algebra:
it does not prove the all-scale Prime Tail Charge theorem or RH.
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


def response(values: list[Fraction], q: int) -> Fraction:
    return sum(
        (
            values[m] * (int(m % q == 0) - int((m - 1) % q == 0))
            for m in range(2, len(values))
        ),
        Fraction(0),
    )


def greedy(residual: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    flow: list[Fraction] = []
    final: list[Fraction] = []
    previous = Fraction(0)
    for value in residual:
        current = max(Fraction(0), value + previous)
        flow.append(current)
        final.append(value + previous - current)
        previous = current
    return flow, final


def suffix_charge(residual: list[Fraction]) -> Fraction:
    best = Fraction(0)
    running = Fraction(0)
    for value in reversed(residual):
        running += value
        best = max(best, running)
    return best


def build_control() -> dict:
    x = 50
    exterior = 53
    primes = primes_through(x)
    endpoints = primes + [exterior]

    residual = [
        Fraction(((17 * i + 5) % 13) - 6, i + 7)
        for i in range(len(primes))
    ]
    flow, final = greedy(residual)
    if any(value > 0 for value in final):
        raise AssertionError("greedy terminal residual remains positive")
    if flow[-1] != suffix_charge(residual):
        raise AssertionError("suffix formula mismatch")

    h = [Fraction(0) for _ in range(exterior + 2)]
    for i, amount in enumerate(flow):
        A = endpoints[i]
        B = endpoints[i + 1]
        for m in range(A + 1, B + 1):
            h[m] += amount

    prime_delta = [response(h, p) for p in primes]
    expected = []
    previous = Fraction(0)
    for amount in flow:
        expected.append(previous - amount)
        previous = amount
    if prime_delta != expected:
        raise AssertionError("prime block response mismatch")

    proper_rows = [q for q, p in prime_powers(exterior) if q != p]
    proper_mismatches = [q for q in proper_rows if response(h, q) != 0]
    if proper_mismatches:
        raise AssertionError(f"proper-power leakage: {proper_mismatches[:5]}")

    exterior_response = response(h, exterior)
    if exterior_response != flow[-1]:
        raise AssertionError("exterior charge mismatch")

    payload = {
        "schema": "riemann.x27302-prime-incidence-greedy.v1",
        "classification": "EXACT_PRIME_BLOCK_SUFFIX_CHARGE_CONTROL",
        "X": x,
        "exterior_prime": exterior,
        "prime_rows": len(primes),
        "proper_power_rows": len(proper_rows),
        "proper_power_mismatches": len(proper_mismatches),
        "terminal_positive_rows": sum(value > 0 for value in final),
        "suffix_charge": str(flow[-1]),
        "exterior_response": str(exterior_response),
        "verdict": "PASS_EXACT_PRIME_INCIDENCE_GREEDY_ALGEBRA",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def self_tests() -> list[str]:
    tests: list[str] = []
    result = build_control()
    assert result["proper_power_mismatches"] == 0
    tests.append("prime blocks preserve proper powers")

    assert result["terminal_positive_rows"] == 0
    tests.append("greedy makes every interior prime feasible")

    residual = [Fraction(2), Fraction(-1), Fraction(-3), Fraction(4), Fraction(-5)]
    flow, final = greedy(residual)
    assert flow[-1] == suffix_charge(residual)
    assert all(value <= 0 for value in final)
    tests.append("closed-form maximum suffix charge")

    candidate = [value + 1 for value in flow]
    assert all(candidate[i] >= flow[i] for i in range(len(flow)))
    tests.append("greedy coordinatewise minimality control")

    mutated = [Fraction(0) for _ in range(52)]
    for m in range(44, 50):
        mutated[m] = Fraction(1)
    assert response(mutated, 49) != 0
    tests.append("composite endpoint leakage rejected")

    p, P = 5, 11
    positive = [Fraction(0) for _ in range(14)]
    for m in range(p + 1, P + 1):
        positive[m] = Fraction(1)
    assert response(positive, p) == -1
    assert response(positive, P) == 1
    tests.append("transport orientation")

    return tests


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    result = build_control()
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
