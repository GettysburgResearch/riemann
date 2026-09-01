#!/usr/bin/env python3
"""Exact bounded checks for the finite-height E-Widder cone.

The script uses only Python's standard library and ``Fraction`` arithmetic.
It authenticates algebraic identities and the declared rational height/order
budget.  It does not replay the Platt--Trudgian zero verification, prove the
canonical product, establish the continuum angular theorem, prove the
all-order E-Widder inequality, or prove RH.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Sequence

ComplexQ = tuple[Fraction, Fraction]


def cq(re: int | Fraction = 0, im: int | Fraction = 0) -> ComplexQ:
    return Fraction(re), Fraction(im)


def cadd(a: ComplexQ, b: ComplexQ) -> ComplexQ:
    return a[0] + b[0], a[1] + b[1]


def cneg(a: ComplexQ) -> ComplexQ:
    return -a[0], -a[1]


def cmul(a: ComplexQ, b: ComplexQ) -> ComplexQ:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def cnorm2(a: ComplexQ) -> Fraction:
    return a[0] * a[0] + a[1] * a[1]


def cinv(a: ComplexQ) -> ComplexQ:
    norm = cnorm2(a)
    if norm == 0:
        raise ZeroDivisionError("zero complex rational")
    return a[0] / norm, -a[1] / norm


def cdiv(a: ComplexQ, b: ComplexQ) -> ComplexQ:
    return cmul(a, cinv(b))


def cscale(a: ComplexQ, scalar: int | Fraction) -> ComplexQ:
    scalar = Fraction(scalar)
    return a[0] * scalar, a[1] * scalar


def cpow(a: ComplexQ, exponent: int) -> ComplexQ:
    if exponent < 0:
        return cpow(cinv(a), -exponent)
    out = cq(1)
    base = a
    n = exponent
    while n:
        if n & 1:
            out = cmul(out, base)
        base = cmul(base, base)
        n >>= 1
    return out


def jet_add(
    a: Sequence[ComplexQ], b: Sequence[ComplexQ], order: int
) -> list[ComplexQ]:
    return [
        cadd(a[i] if i < len(a) else cq(), b[i] if i < len(b) else cq())
        for i in range(order + 1)
    ]


def jet_mul(
    a: Sequence[ComplexQ], b: Sequence[ComplexQ], order: int
) -> list[ComplexQ]:
    out = [cq() for _ in range(order + 1)]
    for n in range(order + 1):
        total = cq()
        for j in range(n + 1):
            left = a[j] if j < len(a) else cq()
            right = b[n - j] if n - j < len(b) else cq()
            total = cadd(total, cmul(left, right))
        out[n] = total
    return out


def jet_inv(a: Sequence[ComplexQ], order: int) -> list[ComplexQ]:
    if not a or cnorm2(a[0]) == 0:
        raise ZeroDivisionError("jet has zero constant term")
    out = [cq() for _ in range(order + 1)]
    out[0] = cinv(a[0])
    for n in range(1, order + 1):
        total = cq()
        for j in range(1, n + 1):
            left = a[j] if j < len(a) else cq()
            total = cadd(total, cmul(left, out[n - j]))
        out[n] = cneg(cmul(out[0], total))
    return out


def jet_pow(a: Sequence[ComplexQ], exponent: int, order: int) -> list[ComplexQ]:
    if exponent < 0:
        return jet_pow(jet_inv(a, order), -exponent, order)
    out = [cq(1)] + [cq()] * order
    base = list(a) + [cq()] * max(0, order + 1 - len(a))
    n = exponent
    while n:
        if n & 1:
            out = jet_mul(out, base, order)
        base = jet_mul(base, base, order)
        n >>= 1
    return out


def derivative_from_jet(jet: Sequence[ComplexQ], order: int) -> ComplexQ:
    return cscale(jet[order], factorial(order))


def check_complex_widder_atoms() -> int:
    checks = 0
    atoms = [
        cq(Fraction(5, 3), Fraction(2, 7)),
        cq(Fraction(9, 4), Fraction(-3, 8)),
        cq(Fraction(13, 6), Fraction(5, 11)),
    ]
    points = [Fraction(3, 7), Fraction(11, 5)]
    indices = [(0, 0), (0, 1), (1, 2), (2, 3), (4, 2), (5, 4)]

    for a in atoms:
        for u0 in points:
            for n, k in indices:
                order = n + k
                u = [cq(u0), cq(1)] + [cq()] * max(0, order - 1)
                denominator = jet_add(u, [a], order)
                expression = jet_mul(
                    jet_pow(u, k, order), jet_inv(denominator, order), order
                )
                lhs = cscale(derivative_from_jet(expression, order), (-1) ** n)
                rhs = cscale(
                    cdiv(cpow(a, k), cpow(cadd(cq(u0), a), n + k + 1)),
                    factorial(n + k),
                )
                if lhs != rhs:
                    raise AssertionError(("complex_widder_atom", a, u0, n, k))
                checks += 1
    return checks


def check_diagonal_phase_formulas() -> int:
    checks = 0
    atoms = [
        cq(Fraction(7, 3), Fraction(2, 5)),
        cq(Fraction(11, 4), Fraction(-5, 9)),
        cq(Fraction(19, 7), Fraction(3, 8)),
    ]
    points = [Fraction(1, 6), Fraction(5, 4), Fraction(29, 10)]

    for a in atoms:
        a_re, a_im = a
        if a_re <= 0:
            raise AssertionError("test atom must lie in the right half-plane")
        for u in points:
            z = cdiv(a, cpow(cadd(cq(u), a), 2))
            denominator = cnorm2(cadd(cq(u), a)) ** 2
            expected_re = (
                a_re * (u + a_re) ** 2
                + a_im**2 * (2 * u + a_re)
            ) / denominator
            expected_im = a_im * (u**2 - cnorm2(a)) / denominator
            if z != (expected_re, expected_im):
                raise AssertionError(("phase_formula", a, u, z))
            if z[0] <= 0:
                raise AssertionError(("positive_real_part", a, u, z))
            # Algebraic form of |arg z| <= |arg a| in the right half-plane.
            if abs(z[1]) * a_re > abs(a_im) * z[0]:
                raise AssertionError(("angular_domination", a, u, z))
            checks += 3
    return checks


def check_published_budget() -> int:
    height = 3_000_000_000_000
    max_order = 4_710_000_000_000
    ratio = Fraction(max_order, height)
    if ratio != Fraction(157, 100):
        raise AssertionError(("height_order_ratio", ratio))

    # The analytic proof imports the elementary strict inequality pi > 3.14.
    # Here we authenticate only its exact rational consequence.
    twice_ratio = 2 * ratio
    if twice_ratio != Fraction(157, 50):
        raise AssertionError(("twice_ratio", twice_ratio))
    if not (twice_ratio == Fraction(314, 100)):
        raise AssertionError(("decimal_normalization", twice_ratio))
    return 3


def main() -> None:
    counts = {
        "complex_widder_atoms": check_complex_widder_atoms(),
        "diagonal_phase_formulas": check_diagonal_phase_formulas(),
        "published_budget": check_published_budget(),
    }
    print("PASS_FINITE_HEIGHT_WIDDER_CONE_EXACT_CHECKS")
    for name, count in counts.items():
        print(f"{name}={count}")
    print(f"total={sum(counts.values())}")
    print("IMPORTED_ZERO_HEIGHT_NOT_REPLAYED")
    print("ALL_ORDER_EW_OPEN")
    print("RH_UNPROVED")


if __name__ == "__main__":
    main()
