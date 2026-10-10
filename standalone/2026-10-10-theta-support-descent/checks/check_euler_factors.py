#!/usr/bin/env python3
"""Exact algebra checks for the Euler and deformed-Gauss continuation notes.

Uses only integer polynomial arithmetic and fractions. These checks authenticate
the local identities, the literal masked case, and contour exponent arithmetic.
They do not establish analytic continuation, a zero-free region, or a moment
bound; those claims require the proofs and the explicitly stated inputs.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
from pathlib import Path


# Integer polynomials in x, z, q. Every key is the exponent triple.
ONE = {(0, 0, 0): 1}
X = {(1, 0, 0): 1}
Z = {(0, 1, 0): 1}
Q = {(0, 0, 1): 1}


def require(condition, label):
    """Acceptance checks remain active when Python runs with -O."""
    if not condition:
        raise AssertionError(label)


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, 0) + coefficient
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def scale(polynomial, coefficient):
    return {exponent: coefficient * value for exponent, value in polynomial.items()
            if coefficient * value}


def mul(*polynomials):
    result = ONE.copy()
    for polynomial in polynomials:
        product = {}
        for exponent, coefficient in result.items():
            for other_exponent, other_coefficient in polynomial.items():
                key = tuple(a + b for a, b in zip(exponent, other_exponent))
                product[key] = product.get(key, 0) + coefficient * other_coefficient
        result = {exponent: coefficient for exponent, coefficient in product.items()
                  if coefficient}
    return result


def power(polynomial, exponent):
    require(exponent >= 0, "negative polynomial exponent")
    return mul(*(polynomial for _ in range(exponent)))


def assert_zero(polynomial, label):
    if polynomial:
        raise AssertionError(f"{label}: nonzero exact polynomial {polynomial}")


def run():
    xz = mul(X, Z)
    one_minus_x = add(ONE, scale(X, -1))
    one_plus_z = add(ONE, Z)
    one_minus_z = add(ONE, scale(Z, -1))
    one_minus_xz = add(ONE, scale(xz, -1))
    one_minus_z2 = add(ONE, scale(power(Z, 2), -1))
    base_n = add(ONE, mul(add(Q, scale(ONE, -1)), X))

    # Main unmasked identity, after clearing nonzero denominators.
    assert_zero(add(
        mul(add(ONE, scale(X, -1), Z), one_minus_xz),
        scale(mul(one_minus_x, one_plus_z), -1),
        scale(mul(power(X, 2), Z), -1),
        mul(X, power(Z, 2)),
    ), "cubic_remainder_identity")

    # The actual n-prime factor, including q-1, not a unit-size replacement.
    assert_zero(add(
        mul(base_n, one_minus_z, one_minus_xz, one_plus_z),
        scale(mul(one_minus_z2, base_n, one_minus_xz), -1),
    ), "n_prime_factor_identity")

    linear_orders = []
    for j in range(13):
        removed = add(*(power(X, a) for a in range(1, j + 1)))
        assert_zero(add(
            X,
            scale(mul(one_minus_x, removed), -1),
            scale(power(X, j + 1), -1),
        ), f"linear_extraction_order_{j}")
        linear_orders.append(j)

    rational_cases = 0
    masked_cases = 0
    for q in (7, 13, 19, 31):
        for x in (F(0), F(1, 4), F(-1, 3), F(2, 7)):
            for z in (F(0), F(1, 5), F(-1, 4), F(3, 11)):
                old = (1 - x + z) * (1 - z) / (1 - x)
                prefix = (1 - z * z) / (1 - x * z)
                remainder = 1 + x * z * (x - z) / ((1 - x) * (1 + z))
                require(old == prefix * remainder, "rational cubic remainder")
                old_n = (1 + (q - 1) * x) * (1 - z) / (1 - x)
                remainder_n = ((1 + (q - 1) * x) * (1 - x * z)
                               / ((1 - x) * (1 + z)))
                require(old_n == prefix * remainder_n, "rational n-prime remainder")
                if x == 0 and z == 0:
                    require(old == prefix == remainder == old_n == remainder_n == 1,
                            "literal zero mask")
                    masked_cases += 1
                rational_cases += 1

    contour_cases = []
    for delta in (F(1, 32), F(1, 16), F(1, 8)):
        for move_w in (False, True):
            w = F(1, 2) + (delta if move_w else F(0))
            v = F(1, 2) - delta
            t = (v - w) / 3
            r = v + 1 - w
            mixed = w + v
            relative_d = v - F(1, 2) - 2 * t
            relative_q = 2 * t
            convexity_q = (max(F(0), 1 - r) + max(F(0), 1 - mixed)) / 2
            expected = ((delta / 3, -delta / 3) if move_w
                        else (-delta / 3, delta / 3))
            require((relative_d, relative_q + convexity_q) == expected,
                    "both angular numerator exponents")
            require(w > 0 and v > 0 and 2 * w + v > 1 and w + 2 * v > 1,
                    "cubic remainder contour domain")
            require(1 - 2 * delta == 2 * v, "new reciprocal argument")
            contour_cases.append({
                "delta": str(delta),
                "path": "coupled" if move_w else "fixed_w",
                "w": str(w), "v": str(v), "t": str(t),
                "r": str(r), "w_plus_v": str(mixed),
                "relative_d_power": str(relative_d),
                "relative_q_power_before_convexity": str(relative_q),
                "both_numerators_convexity_q_power": str(convexity_q),
                "combined_q_power": str(relative_q + convexity_q),
            })

    # In this one polynomial identity Z denotes y, so z=q*x*y is substituted.
    # It is the exact cancellation which removes the conditioned cube inverse.
    qx = mul(Q, X)
    assert_zero(add(qx, scale(mul(qx, Z), -1),
                    scale(mul(qx, add(ONE, scale(Z, -1))), -1)),
                "conditioned_cube_cancellation")

    completed_domain_cases = []
    for sigma in (F(-1, 3), F(-1, 12), F(0), F(1, 4), F(17, 36),
                  F(1, 2), F(3, 4), F(1), F(3, 2)):
        a = max(F(0), 1 - sigma, 1 - 2 * sigma)
        b = max(F(0), (1 - sigma) / 2, F(1, 2) - 2 * sigma)
        threshold = max(F(1), 2 - sigma, F(5, 2) - 3 * sigma / 2,
                        F(5, 2) - 3 * sigma)
        w = threshold + F(1, 100)
        v = w + 3 * sigma - F(3, 2)
        require(w + sigma > 2 + b, "divisor absolute convergence")
        require(w > 1 and v > 1, "conditioned local denominator safety")
        require(w + sigma > 2 and w + 3 * sigma / 2 > F(5, 2)
                and w + 3 * sigma > F(5, 2), "expanded convex tube")
        expected_q = (F(0) if sigma <= 0 else
                      sigma if sigma <= 1 else 2 * sigma - 1)
        require(2 * sigma - 1 + a == expected_q,
                "completed theta and Mellin scalar conductor powers")
        completed_domain_cases.append({
            "sigma": str(sigma), "w": str(w), "v": str(v),
            "row_conductor_exponent": str(a),
            "divisor_conductor_exponent": str(b),
            "combined_scalar_row_exponent": str(expected_q),
        })

    return {
        "status": "PASS",
        "arithmetic": "exact integer polynomials and fractions; no floating point",
        "symbolic_identities": ["cubic_remainder_identity", "n_prime_factor_identity",
                                "conditioned_cube_cancellation"],
        "linear_extraction_orders": linear_orders,
        "rational_local_cases": rational_cases,
        "literal_zero_mask_cases": masked_cases,
        "contour_cases": contour_cases,
        "completed_domain_cases": completed_domain_cases,
        "scope": "Local algebra and conductor-exponent arithmetic only; no analytic or moment validation.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "symbolic_identities": len(result["symbolic_identities"]),
        "linear_extraction_orders": len(result["linear_extraction_orders"]),
        "rational_local_cases": result["rational_local_cases"],
        "literal_zero_mask_cases": result["literal_zero_mask_cases"],
        "contour_cases": len(result["contour_cases"]),
        "completed_domain_cases": len(result["completed_domain_cases"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
