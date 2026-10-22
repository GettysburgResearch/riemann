#!/usr/bin/env python3
"""Directed finite constants for L-90012.

This authenticates the finite radical/square-root/logarithm evaluations used in
the explicit moat-decrease theorem.  The symbolic inequalities and the imported
Rosser--Schoenfeld theta bound remain in the written proof.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

from mpmath import iv

iv.dps = 70


def upper(x) -> float:
    return float(x.b)


def lower(x) -> float:
    return float(x.a)


def sieve(n: int) -> list[int]:
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if is_prime[p]:
            is_prime[p * p : n + 1 : p] = b"\x00" * (
                (n - p * p) // p + 1
            )
    return [p for p in range(2, n + 1) if is_prime[p]]


def s_prefix(k: int):
    return iv.fsum(1 / iv.sqrt(j) for j in range(1, k + 1))


def quotient_constants() -> dict:
    u = {}
    v = {}
    w = {}
    for k in range(1, 16):
        u[k] = 1 + s_prefix(k) - 2 * k / iv.sqrt(k + 1)
        v[k] = (
            1
            + (s_prefix(k - 1) if k > 1 else 0)
            - 2 * (k - 1) / iv.sqrt(iv.mpf(k) + iv.mpf(1) / 4)
        )
        if k <= 9:
            w[k] = u[k] * iv.sqrt(k + 1)

    if upper(u[10]) >= -0.0092:
        raise AssertionError("u_10 certificate failed")
    if upper(v[15]) >= -0.0142:
        raise AssertionError("v_15 certificate failed")
    if lower(w[9]) <= 0:
        raise AssertionError("w_9 positivity failed")
    gaps = []
    for k in range(1, 9):
        gap = w[k] - w[k + 1]
        if lower(gap) <= 0:
            raise AssertionError(f"w monotonicity failed at {k}")
        gaps.append({"K": k, "lower_gap": lower(gap)})

    boundary = iv.mpf("0.5") * iv.fsum(v[k] * iv.sqrt(k) for k in range(1, 15))
    if upper(boundary) >= 3.32:
        raise AssertionError("boundary constant failed")

    return {
        "u_10": [lower(u[10]), upper(u[10])],
        "v_15": [lower(v[15]), upper(v[15])],
        "w_gaps": gaps,
        "boundary_half_sum": [lower(boundary), upper(boundary)],
    }


def moat_at_2000() -> dict:
    x = 2000
    primes = sieve(x)
    lograd = [iv.mpf(0) for _ in range(x + 1)]
    for p in primes:
        lp = iv.log(p)
        for m in range(p, x + 1, p):
            lograd[m] += lp

    sx = iv.sqrt(x)
    lx = iv.log(x)
    j_prime = iv.mpf(0)
    for m in range(2, x + 1):
        sm = iv.sqrt(m)
        b = 2 * sm * (lx - iv.log(m) - 2 * (1 - sm / sx))
        j_prime += b * (lograd[m] - lograd[m - 1])

    higher_ramp = iv.mpf(0)
    for p in primes:
        lp = iv.log(p)
        q = p * p
        while q <= x:
            higher_ramp += lp / iv.sqrt(q) * (lx - iv.log(q))
            q *= p

    moat = j_prime + higher_ramp - 4 * sx
    if not (-29.417 < lower(moat) and upper(moat) < -29.416):
        raise AssertionError("M(2000) interval left the retained bracket")

    return {
        "J_prime": [lower(j_prime), upper(j_prime)],
        "higher_prime_power_ramp": [lower(higher_ramp), upper(higher_ramp)],
        "moat": [lower(moat), upper(moat)],
    }


def main() -> None:
    result = {
        "classification": "PASS_EXPLICIT_PRIME_POWER_MOAT_DECREASE_CONSTANTS",
        "quotient_constants": quotient_constants(),
        "X_2000": moat_at_2000(),
        "scope": (
            "Directed finite constants only. Symbolic monotonicity, the "
            "prime-power summation, and the imported theta bound are in L-90012."
        ),
    }
    out = Path(__file__).with_name("results") / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(out)


if __name__ == "__main__":
    main()
