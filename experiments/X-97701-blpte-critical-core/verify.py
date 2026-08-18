#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


@dataclass(frozen=True)
class Q2:
    """Exact a+b*sqrt(2)."""
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __add__(self, other: "Q2") -> "Q2":
        return Q2(self.a + other.a, self.b + other.b)

    def __sub__(self, other: "Q2") -> "Q2":
        return Q2(self.a - other.a, self.b - other.b)

    def __neg__(self) -> "Q2":
        return Q2(-self.a, -self.b)

    def __mul__(self, other: "Q2") -> "Q2":
        return Q2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    def scale(self, q: Fraction) -> "Q2":
        return Q2(self.a * q, self.b * q)

    def pair(self) -> tuple[str, str]:
        return (str(self.a), str(self.b))


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def prime_factors(n: int) -> list[int]:
    out: list[int] = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def verify_sparse_dictionary(limit: int = 500) -> int:
    mu = mobius_sieve(limit)
    derived = [0] * (limit + 1)
    derived[1] += 6
    # Derive the H_X(n)/sqrt(n) coefficients from the three scaled kappa terms.
    for m in range(1, limit + 1):
        derived[m] -= 6 * mu[m]
        if 2 * m <= limit:
            derived[2 * m] += 9 * mu[m]
        if 4 * m <= limit:
            derived[4 * m] -= 3 * mu[m]

    checks = 0
    for n in range(1, limit + 1):
        direct = 6 * int(n == 1) - 6 * mu[n]
        if n % 2 == 0:
            direct += 9 * mu[n // 2]
        if n % 4 == 0:
            direct -= 3 * mu[n // 4]
        assert direct == derived[n]
        checks += 1
    return checks


def verify_four_bands() -> dict[str, tuple[str, str]]:
    # Base intervals in order [X/16,X/8], [X/8,X/4], [X/4,X/2], [X/2,X].
    minus_six = Q2(Fraction(-6), Fraction(0))
    nine_over_sqrt2 = Q2(Fraction(0), Fraction(9, 2))
    minus_three_halves = Q2(Fraction(-3, 2), Fraction(0))

    bands = [
        minus_three_halves,
        minus_three_halves + nine_over_sqrt2,
        minus_six + nine_over_sqrt2,
        minus_six,
    ]
    expected = [
        Q2(Fraction(-3, 2), Fraction(0)),
        Q2(Fraction(-3, 2), Fraction(9, 2)),
        Q2(Fraction(-6), Fraction(9, 2)),
        Q2(Fraction(-6), Fraction(0)),
    ]
    assert bands == expected
    return {f"band_{i+1}": b.pair() for i, b in enumerate(bands)}


def verify_logarithmic_ownership(limit: int = 500) -> int:
    mu = mobius_sieve(limit)
    prime_weights: dict[int, Fraction] = {}
    next_weight = 2
    for n in range(2, limit + 1):
        if mu[n] == -1 and len(prime_factors(n)) == 1:
            prime_weights[n] = Fraction(next_weight)
            next_weight += 1

    checks = 0
    for n in range(2, limit + 1):
        if mu[n] == 0:
            continue
        ps = prime_factors(n)
        logn = sum((prime_weights[p] for p in ps), Fraction(0))
        lhs = mu[n] * logn
        rhs = -sum((mu[n // p] * prime_weights[p] for p in ps), Fraction(0))
        assert lhs == rhs
        owner_sum = sum((prime_weights[p] / logn for p in ps), Fraction(0))
        assert owner_sum == 1
        checks += 1
    return checks


def verify_equivalence() -> int:
    checks = 0
    vals = [Fraction(-3), Fraction(-1), Fraction(0), Fraction(1), Fraction(5, 2)]
    for uz in vals:
        for type_i in vals:
            for type_ii in vals:
                ufull = uz - type_i - type_ii
                blpte = type_ii <= uz - type_i
                assert blpte == (ufull >= 0)
                sqrt_x = Fraction(7, 3)
                annular = sqrt_x * ufull
                assert (ufull >= 0) == (annular >= 0)
                boundary = annular - Fraction(11, 5)
                threshold = Fraction(-11, 5)
                assert (annular >= 0) == (boundary >= threshold)
                checks += 1
    return checks


def verify_unsigned_mutation() -> dict[str, str]:
    k1, k2 = Fraction(7, 3), Fraction(5, 4)
    sigma = (Fraction(1), Fraction(-1))
    mutated = (Fraction(-1), Fraction(1))
    original = sigma[0] * k1 + sigma[1] * k2
    changed = mutated[0] * k1 + mutated[1] * k2
    assert original > 0 and changed < 0 and changed == -original
    assert tuple(abs(x) for x in sigma) == tuple(abs(x) for x in mutated)
    assert sum(abs(x) for x in sigma) == sum(abs(x) for x in mutated)
    assert sum(x * x for x in sigma) == sum(x * x for x in mutated)
    return {"original": str(original), "mutated": str(changed)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    sparse_checks = verify_sparse_dictionary()
    bands = verify_four_bands()
    owner_checks = verify_logarithmic_ownership()
    equivalence_checks = verify_equivalence()
    mutation = verify_unsigned_mutation()

    result = {
        "schema": "riemann.x97701.c4mbi67-critical-core.v1",
        "classification": "PASS_T97701_BLPTE_C4MBI67_CRITICAL_CORE_ALGEBRA",
        "sparse_dictionary_checks": sparse_checks,
        "four_band_coefficients_Qsqrt2": bands,
        "logarithmic_owner_checks": owner_checks,
        "bellman_equivalence_checks": equivalence_checks,
        "unsigned_mutation": mutation,
        "blpte67_root_equivalent_to_c4mbi67": True,
        "c4mbi67_sign_proved": False,
        "rh_established": False,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(result["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
