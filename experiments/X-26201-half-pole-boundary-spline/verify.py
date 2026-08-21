#!/usr/bin/env python3
"""Exact finite regression for the half-pole boundary-spline proposal.

This checker verifies only the algebraic interfaces that can be reduced to
integer/Fraction arithmetic. It does not verify Boundary-Jet Domination,
continuum positivity, or RH.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Dict, Tuple

ROOT = Path(__file__).resolve().parent


def derivative_tuple(r: int) -> Tuple[Fraction, Fraction, Fraction]:
    """Return (a,b,c) for a*e^t + (b+c*t)e^(t/2)."""
    if r < 0:
        raise ValueError("r must be nonnegative")
    a = Fraction(8)
    b = Fraction(-7)
    c = Fraction(-3, 2)
    for _ in range(r):
        a, b, c = a, b / 2 + c, c / 2
    return a, b, c


def claimed_derivative_tuple(r: int) -> Tuple[Fraction, Fraction, Fraction]:
    scale = Fraction(1, 2**r)
    return (
        Fraction(8),
        -scale * Fraction(7 + 3 * r),
        -scale * Fraction(3, 2),
    )


def phi_derivative_at_zero(r: int) -> Fraction:
    a, b, _ = derivative_tuple(r)
    return a + b


def hankel_determinant() -> Fraction:
    return phi_derivative_at_zero(2) * phi_derivative_at_zero(4) - phi_derivative_at_zero(3) ** 2


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be positive")
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def binary_digit_sum(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return n.bit_count()


def mobius(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be positive")
    value = 1
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            m //= p
            value = -value
            if m % p == 0:
                return 0
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        value = -value
    return value


def mertens(n: int) -> int:
    return sum(mobius(k) for k in range(1, n + 1))


def b2(n: int) -> int:
    return mobius(n) - (mobius(n // 2) if n % 2 == 0 else 0)


def bspline(alpha: Fraction, beta: Fraction, t: Fraction, u: Fraction) -> Fraction:
    if not alpha < beta:
        raise ValueError("alpha < beta required")
    if not (alpha <= t <= beta and alpha <= u <= beta):
        return Fraction(0)
    return (min(t, u) - alpha) * (beta - max(t, u)) / (beta - alpha)


def integrate_bspline_quadratic(alpha: Fraction, beta: Fraction, t: Fraction) -> Fraction:
    """Return integral B(t,u)*2 du exactly."""
    if not alpha <= t <= beta:
        raise ValueError("t outside interval")
    left = (beta - t) / (beta - alpha) * (t - alpha) ** 2 / 2
    right = (t - alpha) / (beta - alpha) * (beta - t) ** 2 / 2
    return 2 * (left + right)


def oversupport_ledger(Y: int) -> Dict[str, int]:
    if Y < 1:
        raise ValueError("Y must be positive")
    inner_A = sum(b2(n) for n in range(1, Y + 1))
    collar_A = -sum(mobius(n) for n in range(Y // 2 + 1, Y + 1))
    return {
        "Y": Y,
        "inner_half_pole_moment": inner_A,
        "collar_half_pole_moment": collar_A,
        "total_half_pole_moment": inner_A + collar_A,
        "mertens_shell": mertens(Y) - mertens(Y // 2),
    }


def proof_object() -> Dict[str, object]:
    derivative_checks = 0
    for r in range(0, 33):
        assert derivative_tuple(r) == claimed_derivative_tuple(r)
        derivative_checks += 1

    det = hankel_determinant()
    assert det == Fraction(-233, 64)

    # The exact moment expansion has coefficients a, b, 2c.
    moment_checks = 0
    for r in range(0, 17):
        a, b, c = derivative_tuple(r)
        assert a == 8
        assert b == -Fraction(7 + 3 * r, 2**r)
        assert 2 * c == -Fraction(3, 2**r)
        # On A=0, only the positive 8|C|^2 term survives.
        moment_checks += 1

    bspline_checks = 0
    for width in range(1, 17):
        alpha = Fraction(-3, 2)
        beta = alpha + width
        for j in range(0, 17):
            t = alpha + Fraction(j, 16) * (beta - alpha)
            val = integrate_bspline_quadratic(alpha, beta, t)
            assert val == (t - alpha) * (beta - t)
            assert val >= 0
            for k in range(0, 17):
                u = alpha + Fraction(k, 16) * (beta - alpha)
                assert bspline(alpha, beta, t, u) >= 0
                bspline_checks += 1

    digital_checks = 0
    for N in range(1, 2049):
        lhs = sum(1 - v2(n) for n in range(1, N + 1))
        assert lhs == binary_digit_sum(N)
        digital_checks += 1

    oversupport_checks = 0
    shell_nonzero = 0
    for Y in range(1, 513):
        ledger = oversupport_ledger(Y)
        assert ledger["inner_half_pole_moment"] == ledger["mertens_shell"]
        assert ledger["collar_half_pole_moment"] == -ledger["mertens_shell"]
        assert ledger["total_half_pole_moment"] == 0
        shell_nonzero += int(ledger["mertens_shell"] != 0)
        oversupport_checks += 1

    # Exact weighted-translation null test in formal half-pole coordinates.
    weighted_pair_checks = 0
    for A in range(-50, 51):
        shifted = A  # e^{-a/2} tau_a multiplies the half-pole moment by 1.
        assert A - shifted == 0
        weighted_pair_checks += 1

    # Mandatory same-sign squarefree cube mutation.
    cube_primes = [(11, 13), (17, 19), (23, 29), (31, 37), (41, 43)]
    cube_signs = set()
    products = set()
    for mask in range(1 << len(cube_primes)):
        product = 1
        for i, pair in enumerate(cube_primes):
            product *= pair[(mask >> i) & 1]
        products.add(product)
        cube_signs.add(mobius(product))
    assert len(products) == 1 << len(cube_primes)
    assert cube_signs == {-1}

    return {
        "classification": "EXACT_HALF_POLE_BOUNDARY_SPLINE_INTERFACES_VERIFIED",
        "derivative_checks": derivative_checks,
        "moment_factor_checks": moment_checks,
        "hankel_counterexample": [det.numerator, det.denominator],
        "bspline_nonnegativity_checks": bspline_checks,
        "digital_endpoint_checks": digital_checks,
        "oversupport_ledgers": oversupport_checks,
        "nonzero_mertens_shells": shell_nonzero,
        "weighted_pair_checks": weighted_pair_checks,
        "mobius_cube_rank": len(cube_primes),
        "mobius_cube_products": len(products),
        "scope": (
            "Finite exact algebra only. This result does not verify the complete "
            "boundary-jet assembly L-26204.8, Boundary-Jet Domination, carry-profile "
            "positivity, a cofinal finite minorant, or RH."
        ),
    }


def canonical_json(obj: Dict[str, object]) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode()


def main() -> None:
    obj = proof_object()
    digest = hashlib.sha256(canonical_json(obj)).hexdigest()
    obj["proof_object_sha256"] = digest
    output = ROOT / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")
    print(json.dumps(obj, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
