#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path


def canonical_digest(obj: object) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def beta(n: int, q: int) -> F:
    if q > n:
        return F(0)
    k, r = divmod(n, q)
    return F(k * (q - 1 - r), n + 1)


def carry_endpoint(n: int, q: int) -> F:
    num = n + 1
    if num % q == 0:
        return F(0)
    m = num // q
    return F(m * ((m + 1) * q - num), num)


def interval_mass(m: int) -> F:
    # 2m * integral_m^(m+1) [(m+1)x^-3-x^-2] dx.
    def primitive(x: int) -> F:
        return -F(m * (m + 1), x * x) + F(2 * m, x)

    return primitive(m + 1) - primitive(m)


def interval_mellin(m: int, s: int) -> F:
    return (
        F(m * (m + 1), s + 2)
        * (F(1, m ** (s + 2)) - F(1, (m + 1) ** (s + 2)))
        - F(m, s + 1)
        * (F(1, m ** (s + 1)) - F(1, (m + 1) ** (s + 1)))
    )


def harmonic(M: int, k: int) -> F:
    return sum((F(1, m**k) for m in range(1, M + 1)), F(0))


def partial_mellin_closed(M: int, s: int) -> F:
    a = (
        2 * harmonic(M, s + 1)
        - F(1, (M + 1) ** s)
        + F(1, (M + 1) ** (s + 1))
    )
    b = (
        harmonic(M, s + 1)
        - F(1, (M + 1) ** s)
        + F(1, (M + 1) ** (s + 1))
    )
    return a / (s + 2) - b / (s + 1)


def rational_factor(s: int) -> F:
    half = F(2 * s + 1, 2)
    return F((s + 1) * (s + 2), 1) / (8 * s * half * half)


def partial_fraction_factor(s: int) -> F:
    half = F(2 * s + 1, 2)
    return F(1, s) - F(7, 8) / half - F(3, 16) / (half * half)


def main(path: str) -> int:
    cert = json.loads(Path(path).read_text())
    max_n = int(cert["max_carry_n"])
    max_m = int(cert["max_interval_m"])
    exponents = [int(x) for x in cert["mellin_exponents"]]
    cutoffs = [int(x) for x in cert["partial_cutoffs"]]

    carry_rows = 0
    for n in range(2, max_n + 1):
        for q in range(2, n + 1):
            assert beta(n, q) == carry_endpoint(n, q)
            carry_rows += 1

    for m in range(1, max_m + 1):
        assert interval_mass(m) == F(1, m * (m + 1))

    mellin_rows = 0
    for s in exponents:
        assert rational_factor(s) == partial_fraction_factor(s)
        for M in cutoffs:
            lhs = sum((interval_mellin(m, s) for m in range(1, M + 1)), F(0))
            assert lhs == partial_mellin_closed(M, s)
            mellin_rows += 1

    result = {
        "schema": "riemann.x23801-gamma-carry.result.v1",
        "verdict": "PASS_EXACT_GAMMA_CARRY_ALGEBRA",
        "certificate_sha256": canonical_digest(cert),
        "carry_rows_checked": carry_rows,
        "interval_masses_checked": max_m,
        "mellin_partial_rows_checked": mellin_rows,
        "partial_fraction_rows_checked": len(exponents),
        "sharp_total_mass": "1/2",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py certificate.json")
    raise SystemExit(main(sys.argv[1]))
