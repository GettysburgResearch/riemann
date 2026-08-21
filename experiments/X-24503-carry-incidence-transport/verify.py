#!/usr/bin/env python3
"""Exact standard-library replay for the finite carry transport identities."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import random
from typing import Dict, Iterable, List


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        p += 1
    return True


def prime_powers(X: int) -> List[int]:
    out = set()
    for p in range(2, X + 1):
        if not is_prime(p):
            continue
        q = p
        while q <= X:
            out.add(q)
            if q > X // p:
                break
            q *= p
    return sorted(out)


def carry_g(n: int, q: int) -> int:
    if n < q:
        return 0
    return (n // q) * (q - 1 - (n % q))


def v_coordinate(b: Dict[int, Fraction], q: int, X: int) -> Fraction:
    return sum(
        b.get(m, Fraction(0))
        * ((1 if m % q == 0 else 0) - (1 if (m - 1) % q == 0 else 0))
        for m in range(2, X + 1)
    )


def residuals(
    b: Dict[int, Fraction], targets: Dict[int, Fraction], X: int
) -> Dict[int, Fraction]:
    return {q: v_coordinate(b, q, X) - targets[q] for q in targets}


def apply_b_block(
    b: Dict[int, Fraction], A: int, B: int, t: Fraction
) -> Dict[int, Fraction]:
    out = dict(b)
    for m in range(A + 1, B + 1):
        out[m] = out.get(m, Fraction(0)) - t
    return out


def descending_repair(
    b: Dict[int, Fraction], targets: Dict[int, Fraction], X: int
) -> tuple[Dict[int, Fraction], Dict[int, Fraction]]:
    out = dict(b)
    corrections: Dict[int, Fraction] = {}
    for q in sorted(targets, reverse=True):
        r = v_coordinate(out, q, X) - targets[q]
        t = max(r, Fraction(0))
        corrections[q] = t
        out[q] = out.get(q, Fraction(0)) - t
    return out, corrections


def test_second_difference() -> int:
    checks = 0
    for X in range(2, 65):
        for q in range(2, X + 1):
            for m in range(2, X + 1):
                lhs = carry_g(m, q) - 2 * carry_g(m - 1, q) + carry_g(m - 2, q)
                rhs = (m - 1) * (
                    (1 if m % q == 0 else 0)
                    - (1 if (m - 1) % q == 0 else 0)
                )
                assert lhs == rhs
                checks += 1
    return checks


def test_block_transport() -> int:
    rng = random.Random(24503)
    checks = 0
    for X in range(8, 55):
        qs = prime_powers(X)
        for _ in range(20):
            b = {m: Fraction(rng.randint(-9, 9), rng.randint(1, 7)) for m in range(2, X + 1)}
            A = rng.randint(1, X - 1)
            B = rng.randint(A + 1, X)
            t = Fraction(rng.randint(-7, 7), rng.randint(1, 7))
            before = {q: v_coordinate(b, q, X) for q in qs}
            after_b = apply_b_block(b, A, B, t)
            after = {q: v_coordinate(after_b, q, X) for q in qs}
            for q in qs:
                expected = t * (
                    (1 if A % q == 0 else 0)
                    - (1 if B % q == 0 else 0)
                )
                assert after[q] - before[q] == expected
                checks += 1

            product = Fraction(1)
            for m in range(A + 1, B + 1):
                product *= Fraction(m, m - 1)
            assert product == Fraction(B, A)
            checks += 1
    return checks


def test_pure_prime_transfer() -> int:
    checks = 0
    for X in range(10, 80):
        primes = [p for p in range(2, X + 1) if is_prime(p)]
        if len(primes) < 2:
            continue
        A, B = primes[-2], primes[-1]
        if B > X:
            continue
        b = {m: Fraction(0) for m in range(2, X + 1)}
        t = Fraction(5, 7)
        out = apply_b_block(b, A, B, t)
        for q in prime_powers(X):
            delta = v_coordinate(out, q, X)
            if q == A:
                assert delta == t
            elif q == B:
                assert delta == -t
            else:
                assert delta == 0
            checks += 1
    return checks


def test_q_plus_one_sign() -> int:
    checks = 0
    X = 100
    for q in prime_powers(X - 1):
        t = Fraction(3, 11)
        b = {m: Fraction(0) for m in range(2, X + 1)}

        wrong = dict(b)
        wrong[q + 1] -= t
        assert v_coordinate(wrong, q, X) == t

        correct = dict(b)
        correct[q] -= t
        assert v_coordinate(correct, q, X) == -t
        checks += 2
    return checks


def test_descending_algorithm() -> int:
    rng = random.Random(24519)
    checks = 0
    for X in range(8, 75):
        qs = prime_powers(X)
        for _ in range(25):
            b = {m: Fraction(rng.randint(-20, 20), rng.randint(1, 9)) for m in range(2, X + 1)}
            targets = {q: Fraction(rng.randint(-6, 6), rng.randint(1, 7)) for q in qs}
            repaired, corrections = descending_repair(b, targets, X)
            final = residuals(repaired, targets, X)
            assert all(value <= 0 for value in final.values())

            # Reconstruct the exact triangular recurrence.
            initial = residuals(b, targets, X)
            for q in qs:
                rhs = initial[q]
                rhs -= sum(t for Q, t in corrections.items() if Q > q and Q % q == 0)
                rhs += sum(t for Q, t in corrections.items() if Q > q and (Q - 1) % q == 0)
                assert corrections[q] == max(rhs, Fraction(0))
                checks += 1
    return checks


def main() -> None:
    results = {
        "second_difference_checks": test_second_difference(),
        "block_transport_checks": test_block_transport(),
        "pure_prime_transfer_checks": test_pure_prime_transfer(),
        "q_plus_one_sign_checks": test_q_plus_one_sign(),
        "descending_algorithm_checks": test_descending_algorithm(),
    }
    payload = json.dumps(results, sort_keys=True, separators=(",", ":")).encode()
    results["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    results["verdict"] = "PASS_EXACT_CARRY_INCIDENCE_TRANSPORT"
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
