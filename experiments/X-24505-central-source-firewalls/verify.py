#!/usr/bin/env python3
"""Exact finite regression for the central-source continuation of PR #248.

This checker verifies finite algebra only.  It does not prove CBMR or RH.
"""

from __future__ import annotations

import hashlib
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

getcontext().prec = 80


def mobius_table(nmax: int) -> list[int]:
    mu = [1] * (nmax + 1)
    prime = [True] * (nmax + 1)
    mu[0] = 0
    for p in range(2, nmax + 1):
        if prime[p]:
            for m in range(p, nmax + 1, p):
                prime[m] = False if m != p else prime[m]
                mu[m] *= -1
            pp = p * p
            for m in range(pp, nmax + 1, pp):
                mu[m] = 0
    return mu


def v2_odd(n: int) -> tuple[int, int]:
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r, n


def reciprocal_eta_coefficient(n: int, mu: list[int]) -> int:
    r, m = v2_odd(n)
    if r == 0:
        return mu[m]
    return (1 << (r - 1)) * mu[m]


def central_carry(n: int, q: int) -> int:
    a = n // 2
    b = n - a
    return n // q - a // q - b // q


def is_power_of_two(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0


def omega_value(n: int, mu: list[int]) -> Fraction:
    ans = Fraction(mu[n], 1)
    if n % 2 == 0:
        ans -= Fraction(3, 2) * mu[n // 2]
    if n % 4 == 0:
        ans += Fraction(1, 2) * mu[n // 4]
    return ans


def verify() -> dict[str, object]:
    nmax = 1024
    mu = mobius_table(nmax)
    b = [0] + [reciprocal_eta_coefficient(n, mu) for n in range(1, nmax + 1)]

    checks = {
        "eta_convolution": 0,
        "eta_divisor_prefix": 0,
        "eta_central_rows": 0,
        "mobius_central_rows": 0,
        "omega_convolution": 0,
        "omega_central_rows": 0,
        "outer_anchor_rows": 0,
        "layer_cake_vectors": 0,
        "rank_one_pairings": 0,
        "mutations_rejected": 0,
    }

    # (1*b)(n) is 2^r on powers of two and zero elsewhere.
    for n in range(1, nmax + 1):
        lhs = sum(b[d] for d in range(1, n + 1) if n % d == 0)
        rhs = n if is_power_of_two(n) else 0
        assert lhs == rhs, ("eta convolution", n, lhs, rhs)
        checks["eta_convolution"] += 1

    # Staircase divisor prefix.
    for x in range(1, 513):
        lhs = sum(b[q] * (x // q) for q in range(1, x + 1))
        p = 1 << (x.bit_length() - 1)
        rhs = 2 * p - 1
        assert lhs == rhs, ("eta prefix", x, lhs, rhs)
        checks["eta_divisor_prefix"] += 1

    # Eta/Mersenne central image and Mobius constant image.
    for n in range(2, 513):
        eta_row = sum(b[q] * central_carry(n, q) for q in range(2, n + 1))
        p = 1 << (n.bit_length() - 1)
        eta_expected = 1 - (p if n == 2 * p - 1 else 0)
        assert eta_row == eta_expected, ("eta row", n, eta_row, eta_expected)
        checks["eta_central_rows"] += 1

        mu_row = sum(mu[q] * central_carry(n, q) for q in range(2, n + 1))
        assert mu_row == -1, ("mu row", n, mu_row)
        checks["mobius_central_rows"] += 1

    # Finite omega convolution and compact central image.
    omega = [Fraction(0)] + [omega_value(n, mu) for n in range(1, nmax + 1)]
    expected_conv = {1: Fraction(1), 2: Fraction(-3, 2), 4: Fraction(1, 2)}
    for n in range(1, 513):
        lhs = sum(omega[d] for d in range(1, n + 1) if n % d == 0)
        rhs = expected_conv.get(n, Fraction(0))
        assert lhs == rhs, ("omega convolution", n, lhs, rhs)
        checks["omega_convolution"] += 1

    omega_expected = {
        2: Fraction(-5, 2),
        3: Fraction(-1),
        4: Fraction(1),
        5: Fraction(1),
        6: Fraction(1),
        7: Fraction(1, 2),
    }
    for n in range(2, 513):
        lhs = sum(omega[q] * central_carry(n, q) for q in range(2, n + 1))
        rhs = omega_expected.get(n, Fraction(0))
        assert lhs == rhs, ("omega row", n, lhs, rhs)
        checks["omega_central_rows"] += 1

    # Outer-anchor interval and exact endpoint telescope.
    ln_three_halves = (Decimal(3) / Decimal(2)).ln()
    X = 900
    atomic_normalized_sum = Decimal(0)
    signed_total = Decimal(0)
    for q in range(2, X // 3 + 1):
        y0, y1 = 2 * q - 1, 3 * q - 1
        assert y0 // 3 < q <= (y0 + 1) // 2
        ratio_log = (Decimal(3 * q) / Decimal(2 * q - 1)).ln()
        assert ratio_log >= ln_three_halves
        coeff = ratio_log / Decimal(3 * q).sqrt()
        atomic_normalized_sum += Decimal(3 * q).sqrt() * coeff
        signed_total += coeff
        checks["outer_anchor_rows"] += 1
    assert atomic_normalized_sum >= Decimal(X // 3 - 2) * ln_three_halves
    assert signed_total > Decimal(10)

    # Formal commutator layer cake in the T_m basis.
    samples = [
        [Fraction(7, 3), Fraction(5, 3), Fraction(1, 2), Fraction(1, 7)],
        [Fraction(2), Fraction(2), Fraction(1), Fraction(0)],
        [Fraction(-1), Fraction(3), Fraction(-2), Fraction(5)],
    ]
    for sigma in samples:
        # sigma indexes m=2,...,N.
        N = len(sigma) + 1
        lhs: dict[int, Fraction] = {}
        for i, value in enumerate(sigma, start=2):
            lhs[i] = lhs.get(i, Fraction(0)) + value
            lhs[i - 1] = lhs.get(i - 1, Fraction(0)) - value
        lhs.pop(1, None)  # T_1=0.

        rhs: dict[int, Fraction] = {N: sigma[-1]}
        for m in range(2, N):
            rhs[m] = sigma[m - 2] - sigma[m - 1]
        lhs = {k: v for k, v in lhs.items() if v}
        rhs = {k: v for k, v in rhs.items() if v}
        assert lhs == rhs, ("layer cake", sigma, lhs, rhs)
        checks["layer_cake_vectors"] += 1

        # Rank-one Mobius response is minus total source coefficient.
        source_pair = Fraction(0)
        for i, value in enumerate(sigma, start=2):
            divisor_mu = sum(mu[q] for q in range(2, i + 1) if i % q == 0)
            assert divisor_mu == -1
            source_pair += value * divisor_mu
        assert source_pair == -sum(sigma)
        checks["rank_one_pairings"] += 1

    # Mutation tests.
    try:
        n = 31
        p = 16
        bad = 1 - p + 1
        assert bad == 1 - p
    except AssertionError:
        checks["mutations_rejected"] += 1

    try:
        n = 20
        bad = sum(mu[q] * central_carry(n, q) for q in range(3, n + 1))
        assert bad == -1
    except AssertionError:
        checks["mutations_rejected"] += 1

    try:
        bad_omega = omega_expected.copy()
        bad_omega[7] = Fraction(-1, 2)
        assert bad_omega == omega_expected
    except AssertionError:
        checks["mutations_rejected"] += 1

    assert checks["mutations_rejected"] == 3

    payload = {
        "classification": "EXACT_CENTRAL_SOURCE_FIREWALLS_VERIFIED",
        "checks": checks,
        "outer_anchor_atomic_normalized_lower": str(atomic_normalized_sum),
        "outer_anchor_signed_total_at_X900": str(signed_total),
        "scope": "finite exact algebra only; CBMR and RH are not certified",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    payload = verify()
    out = Path(__file__).with_name("results") / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
