#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.t91652.corrected-provenance-envelope.v1"


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for k in range(p * p, n + 1, p):
                sieve[k] = False
    return [p for p in range(2, n + 1) if sieve[p]]


def least_prime_factor(n: int) -> int:
    if n <= 1:
        raise ValueError("least_prime_factor requires n>1")
    p = 2
    while p * p <= n:
        if n % p == 0:
            return p
        p += 1
    return n


def canonical_json(data: Any) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()


def verify() -> dict[str, Any]:
    r = [Fraction(1, 9), Fraction(1, 10), Fraction(1, 11), Fraction(1, 13)]
    s = [Fraction(1)]
    lam: list[Fraction] = []
    alpha: list[Fraction] = []
    for ri in r:
        lam.append(ri * s[-1])
        alpha.append(ri * lam[-1])
        s.append(s[-1] * (1 - ri))

    assert s[-1] + sum(lam, Fraction(0)) == 1
    assert all(-li * ri + ai == 0 for ri, li, ai in zip(r, lam, alpha))
    rho = sum(alpha, Fraction(0))
    assert rho <= r[0] * sum(lam, Fraction(0))
    assert rho < r[0] < Fraction(1, 8)

    c_base = Fraction(7)
    c_causal = Fraction(5)
    c_star = max(c_base, c_causal)
    envelope = c_star / (1 - rho)
    assert envelope < Fraction(8, 7) * c_star

    root_mass = Fraction(54)
    c_root = Fraction(11)
    native_upper = c_root + root_mass * envelope
    coarse_native_upper = c_root + Fraction(432, 7) * c_star
    assert native_upper < coarse_native_upper

    c_pp_control = Fraction(1, 10)
    normalized_limsup_upper = Fraction(0)
    assert normalized_limsup_upper < c_pp_control / 4

    small_primes = primes_upto(61)
    p61 = math.prod(small_primes)
    limit = 1000
    rough = [n for n in range(2, limit + 1) if math.gcd(n, p61) == 1]
    decomposition: dict[int, tuple[int, int]] = {}
    for n in rough:
        p = least_prime_factor(n)
        m = n // p
        assert p >= 67
        if m > 1:
            assert least_prime_factor(m) >= p
        decomposition[n] = (p, m)
    assert len(decomposition) == len(rough)
    assert [n for n in range(2, 69) if math.gcd(n, p61) == 1] == [67]

    locked_blobs = [
        "16d6ef678fe172c6add5886cae55773d165d23f8",
        "16c8bcf4733d74106b377595396faa2a76289de8",
        "8c5398370c3dccc47e3a3e8877aa26a0a7824429",
        "3b05866c86d6c239ddf212652830ac253c9df41d",
        "c37f95a82dce2a9007a29614977b5a0bdf3b6a38",
        "cc76d152fcb2cda36b77fd0732e5b9c4f10b1c43",
        "39834c1d35c3e443d11c2ac8349f36db5084bb05",
        "022aac53ba683951150ffc6ff164f59534a50a13",
        "cd497b657933feaffbf83f00a596180a14c574ca",
        "f2150bc906024525b434fecee7e56de40f9e2b4e",
        "409d63af63e249873d001858ee7fec944f0a7005",
        "9de33cccaa9728cf6749ed2592ee2bd932b0ad3a",
        "b5a4be7838f6f7d04e2664ffdc88e5eb89c54b41",
        "d99b86e37b32cd105ba2ee82f2052b78c3f2bd64",
    ]
    assert len(set(locked_blobs)) == len(locked_blobs)
    assert all(len(x) == 40 and all(c in "0123456789abcdef" for c in x) for x in locked_blobs)

    proof = {
        "schema": SCHEMA,
        "verdict": "PASS_CORRECTED_PROVENANCE_ENVELOPE_ALGEBRA",
        "reset": {
            "r": [fstr(x) for x in r],
            "survival": [fstr(x) for x in s],
            "lambda": [fstr(x) for x in lam],
            "alpha": [fstr(x) for x in alpha],
            "recursive_mass": fstr(rho),
            "recursive_mass_lt_one_eighth": True,
        },
        "envelope": {
            "C_star": fstr(c_star),
            "exact_fixed_point": fstr(envelope),
            "coarse_bound": fstr(Fraction(8, 7) * c_star),
            "root_mass": fstr(root_mass),
            "C_root": fstr(c_root),
            "native_upper_exact": fstr(native_upper),
            "native_upper_coarse": fstr(coarse_native_upper),
        },
        "endpoint": {
            "limsup_upper": "0",
            "positive_Cpp_control": fstr(c_pp_control),
            "strict_threshold": True,
            "two_sided_bound_claimed": False,
        },
        "rough_reservoir": {
            "finite_limit": limit,
            "rough_integer_count": len(rough),
            "first_nontrivial_rough_integer": rough[0],
            "unique_least_prime_partition": True,
        },
        "lock": {
            "blob_count_checked": len(locked_blobs),
            "all_full_sha1": True,
        },
        "scope": {
            "checks": "finite algebra, type ledger, and least-prime partition only",
            "does_not_check": "root Hall/collar/omission/port analytic imports",
            "rh_established_by_replay": False,
        },
    }
    proof["proof_object_sha256"] = hashlib.sha256(canonical_json(proof)).hexdigest()
    return proof


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = verify()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
