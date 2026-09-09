#!/usr/bin/env python3
"""Exact bounded checks for the Architecture-E / E-Widder dossier.

This script uses only Python's standard library and rational arithmetic.
It checks finite algebraic controls only; it does not prove the analytic
continuation statements, the all-order inequalities for Riemann data, or RH.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Sequence


def poly_trim(coeffs: Sequence[Fraction]) -> list[Fraction]:
    out = list(coeffs)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mul(a: Sequence[Fraction], b: Sequence[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return poly_trim(out)


def poly_pow(a: Sequence[Fraction], exponent: int) -> list[Fraction]:
    if exponent < 0:
        raise ValueError("polynomial exponent must be nonnegative")
    out = [Fraction(1)]
    base = list(a)
    n = exponent
    while n:
        if n & 1:
            out = poly_mul(out, base)
        base = poly_mul(base, base)
        n >>= 1
    return out


def poly_derivative(a: Sequence[Fraction], order: int = 1) -> list[Fraction]:
    if order < 0:
        raise ValueError("derivative order must be nonnegative")
    out = list(a)
    for _ in range(order):
        if len(out) <= 1:
            return [Fraction(0)]
        out = [Fraction(i) * out[i] for i in range(1, len(out))]
    return poly_trim(out)


def poly_eval(a: Sequence[Fraction], x: Fraction) -> Fraction:
    result = Fraction(0)
    for coeff in reversed(a):
        result = result * x + coeff
    return result


def jet_add(a: Sequence[Fraction], b: Sequence[Fraction], order: int) -> list[Fraction]:
    return [
        (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        for i in range(order + 1)
    ]


def jet_mul(a: Sequence[Fraction], b: Sequence[Fraction], order: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(order + 1)]
    for n in range(order + 1):
        out[n] = sum(
            (a[j] if j < len(a) else 0)
            * (b[n - j] if n - j < len(b) else 0)
            for j in range(n + 1)
        )
    return out


def jet_inv(a: Sequence[Fraction], order: int) -> list[Fraction]:
    if not a or a[0] == 0:
        raise ZeroDivisionError("jet has zero constant term")
    out = [Fraction(0) for _ in range(order + 1)]
    out[0] = 1 / a[0]
    for n in range(1, order + 1):
        out[n] = -sum(
            (a[j] if j < len(a) else 0) * out[n - j]
            for j in range(1, n + 1)
        ) / a[0]
    return out


def jet_pow(a: Sequence[Fraction], exponent: int, order: int) -> list[Fraction]:
    if exponent < 0:
        return jet_pow(jet_inv(a, order), -exponent, order)
    out = [Fraction(1)] + [Fraction(0)] * order
    base = list(a) + [Fraction(0)] * max(0, order + 1 - len(a))
    n = exponent
    while n:
        if n & 1:
            out = jet_mul(out, base, order)
        base = jet_mul(base, base, order)
        n >>= 1
    return out


def derivative_from_jet(jet: Sequence[Fraction], order: int) -> Fraction:
    return jet[order] * factorial(order)


def check_widder_atom(max_k: int = 14) -> int:
    checks = 0
    points = [
        (Fraction(1, 7), Fraction(2, 5)),
        (Fraction(3, 2), Fraction(11, 6)),
        (Fraction(17, 9), Fraction(5, 13)),
    ]
    for k in range(1, max_k + 1):
        order = 2 * k - 1
        for u0, a in points:
            u = [u0, Fraction(1)] + [Fraction(0)] * (order - 1)
            denominator = jet_add(u, [a], order)
            f = jet_mul(jet_pow(u, k, order), jet_inv(denominator, order), order)
            lhs = (-1) ** (k - 1) * derivative_from_jet(f, order)
            rhs = Fraction(factorial(order)) * a**k / (u0 + a) ** (2 * k)
            if lhs != rhs:
                raise AssertionError(("widder_atom", k, u0, a, lhs, rhs))
            checks += 1
    return checks


def check_differential_recurrence(max_k: int = 10) -> int:
    checks = 0
    q = [Fraction(5), Fraction(-3), Fraction(7, 2), Fraction(11, 3), Fraction(-2, 5)]
    nodes = [Fraction(1, 3), Fraction(7, 5), Fraction(19, 7)]
    u_poly = [Fraction(0), Fraction(1)]
    for k in range(1, max_k + 1):
        gk = poly_mul(poly_pow(u_poly, k), q)
        gkp1 = poly_mul(poly_pow(u_poly, k + 1), q)
        for u0 in nodes:
            wk = (-1) ** (k - 1) * poly_eval(poly_derivative(gk, 2 * k - 1), u0)
            wk_prime = (-1) ** (k - 1) * poly_eval(poly_derivative(gk, 2 * k), u0)
            wk_second = (-1) ** (k - 1) * poly_eval(
                poly_derivative(gk, 2 * k + 1), u0
            )
            wk_plus_one = (-1) ** k * poly_eval(
                poly_derivative(gkp1, 2 * k + 1), u0
            )
            rhs = -u0 * wk_second - Fraction(2 * k + 1) * wk_prime
            if wk_plus_one != rhs:
                raise AssertionError(
                    ("widder_recurrence", k, u0, wk_plus_one, rhs, wk)
                )
            checks += 1
    return checks


def check_q_recurrence(max_k: int = 10) -> int:
    checks = 0
    q = [Fraction(2), Fraction(5, 3), Fraction(-7, 4), Fraction(1, 9), Fraction(3, 8)]
    nodes = [Fraction(2, 9), Fraction(5, 4), Fraction(23, 11)]
    u_poly = [Fraction(0), Fraction(1)]
    for k in range(0, max_k + 1):
        gk = poly_mul(poly_pow(u_poly, k), q)
        gkp1 = poly_mul(poly_pow(u_poly, k + 1), q)
        qk_poly = poly_derivative(gk, k)
        qkp1_poly = poly_derivative(gkp1, k + 1)
        qk_prime_poly = poly_derivative(qk_poly, 1)
        for u0 in nodes:
            lhs = poly_eval(qkp1_poly, u0)
            rhs = (
                u0 * poly_eval(qk_prime_poly, u0)
                + Fraction(k + 1) * poly_eval(qk_poly, u0)
            )
            if lhs != rhs:
                raise AssertionError(("Q_recurrence", k, u0, lhs, rhs))
            checks += 1
    return checks


def check_normalized_microscope(max_k: int = 16) -> int:
    checks = 0
    points = [
        (Fraction(1, 5), Fraction(7, 3)),
        (Fraction(9, 4), Fraction(11, 8)),
        (Fraction(31, 12), Fraction(5, 17)),
    ]
    for k in range(1, max_k + 1):
        for u, a in points:
            wk_atom = (
                Fraction(2 * factorial(2 * k - 1))
                * a**k
                / (u + a) ** (2 * k)
            )
            normalized = (
                (4 * u) ** k
                * wk_atom
                / Fraction(2 * factorial(2 * k - 1))
            )
            lam = 4 * u * a / (u + a) ** 2
            if normalized != lam**k:
                raise AssertionError(
                    ("normalized_microscope", k, u, a, normalized, lam**k)
                )
            if not (0 < lam <= 1):
                raise AssertionError(("lambda_range", u, a, lam))
            checks += 2
    return checks


def check_loewner_difference() -> int:
    checks = 0
    p = [Fraction(3, 2), Fraction(-5, 7), Fraction(11, 13), Fraction(2, 9)]
    p_prime = poly_derivative(p)
    tp = [Fraction(0)] + p
    tp_prime = poly_derivative(tp)
    nodes = [Fraction(1, 4), Fraction(9, 16), Fraction(25, 16), Fraction(49, 16)]
    roots = [Fraction(1, 2), Fraction(3, 4), Fraction(5, 4), Fraction(7, 4)]
    for i, ti in enumerate(nodes):
        xi = roots[i]
        for j, tj in enumerate(nodes):
            xj = roots[j]
            if i == j:
                rhs = poly_eval(tp_prime, ti) - ti * poly_eval(p_prime, ti)
            else:
                rhs = (
                    (poly_eval(tp, ti) - poly_eval(tp, tj))
                    - xi * xj * (poly_eval(p, ti) - poly_eval(p, tj))
                ) / (ti - tj)
            lhs = (
                xi * poly_eval(p, ti) + xj * poly_eval(p, tj)
            ) / (xi + xj)
            if lhs != rhs:
                raise AssertionError(("loewner_difference", i, j, lhs, rhs))
            checks += 1
    return checks


def main() -> None:
    counts = {
        "widder_atom": check_widder_atom(),
        "widder_recurrence": check_differential_recurrence(),
        "Q_recurrence": check_q_recurrence(),
        "normalized_microscope": check_normalized_microscope(),
        "loewner_difference": check_loewner_difference(),
    }
    total = sum(counts.values())
    print("PASS_ARCHITECTURE_E_WIDDER_EXACT_CHECKS")
    for name, count in counts.items():
        print(f"{name}={count}")
    print(f"total={total}")
    print("RH_UNPROVED")


if __name__ == "__main__":
    main()
