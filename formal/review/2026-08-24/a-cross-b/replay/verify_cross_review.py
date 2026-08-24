#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import comb
import json
from pathlib import Path
import sympy as sp


def eta_coeff(k: int) -> Fraction:
    return Fraction(comb(2 * k, k), 4 ** k)


def factorint(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def eta(n: int) -> Fraction:
    if n == 0:
        return Fraction(0)
    out = Fraction(1)
    for k in factorint(n).values():
        out *= eta_coeff(k)
    return out


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def conv(f, g, n: int) -> Fraction:
    if n == 0:
        return Fraction(0)
    return sum((f(d) * g(n // d) for d in divisors(n)), Fraction(0))


def moebius(n: int) -> Fraction:
    if n == 0:
        return Fraction(0)
    fac = factorint(n)
    if any(k > 1 for k in fac.values()):
        return Fraction(0)
    return Fraction(-1 if len(fac) % 2 else 1)


def native_euler(xs: list[tuple[Fraction, Fraction]]) -> Fraction:
    out = Fraction(1)
    for r, u in xs:
        out *= 1 - r * u
    return out


def first_owner(xs: list[tuple[Fraction, Fraction]]) -> Fraction:
    if not xs:
        return Fraction(1)
    r, u = xs[0]
    tail = xs[1:]
    return (1-r) * first_owner(tail) + r * (1-u) * native_euler(tail)


def finite_abel(f, g, n: int) -> tuple[Fraction, Fraction]:
    lhs = sum((f(i) * g(i) for i in range(n)), Fraction(0))
    sng = sum((g(i) for i in range(n)), Fraction(0))
    rhs = f(max(n - 1, 0)) * sng
    rhs -= sum(
        ((f(i + 1) - f(i)) * sum((g(j) for j in range(i + 1)), Fraction(0))
         for i in range(max(n - 1, 0))),
        Fraction(0),
    )
    return lhs, rhs


def main() -> None:
    a, b, alpha, q, x = sp.symbols('a b alpha q x')
    row2 = 2*a - 1 - b
    row3s = 5*b - a - 1 - 3*a**2
    five_three = sp.expand(5*row2 + row3s)
    target = -3*(a-1)*(a-2)
    assert sp.expand(five_three-target) == 0
    assert sp.expand(row3s.subs(b, 2*a-1)-target) == 0

    four = x - (alpha+2)*(x*q) + (2*alpha+1)*(x*q**2) - alpha*(x*q**3)
    assert sp.expand(four - x*(1-q)**2*(1-alpha*q)) == 0

    # The three-tap constraint determinant is (q-1)^2, so it is invertible for q != 1.
    M = sp.Matrix([[1,1,1],[0,1,2],[1,q,q**2]])
    assert sp.factor(M.det()) == (q-1)**2

    eta_antidiagonal_checked = 0
    for n in range(0, 51):
        assert sum((eta_coeff(k)*eta_coeff(n-k) for k in range(n+1)), Fraction(0)) == 1
        eta_antidiagonal_checked += 1

    eta_dirichlet_checked = 0
    for n in range(1, 501):
        assert conv(eta, eta, n) == 1
        eta_dirichlet_checked += 1

    # Finite exact one-field convolution identity on a nonmultiplicative rational fixture.
    coeffs = {1: Fraction(2), 2: Fraction(-1,3), 3: Fraction(5,7), 4: Fraction(2,5), 6: Fraction(-4,9)}
    def bfun(n: int) -> Fraction:
        return coeffs.get(n, Fraction(0))
    def beta(n: int) -> Fraction:
        return conv(bfun, eta, n)
    def beta_sq(n: int) -> Fraction:
        return conv(beta, beta, n)
    def lhs_one_field(n: int) -> Fraction:
        return conv(beta_sq, moebius, n)
    def rhs_one_field(n: int) -> Fraction:
        return conv(bfun, bfun, n)
    one_field_checked = 0
    for n in range(1, 121):
        assert lhs_one_field(n) == rhs_one_field(n)
        one_field_checked += 1

    first_owner_fixtures = [
        [],
        [(Fraction(1,3), Fraction(2,5))],
        [(Fraction(1,3), Fraction(2,5)), (Fraction(2,7), Fraction(-1,4))],
        [(Fraction(1,5), Fraction(3,7)), (Fraction(2,9), Fraction(5,11)), (Fraction(1,4), Fraction(-2,3))],
    ]
    for xs in first_owner_fixtures:
        assert first_owner(xs) == native_euler(xs)

    abel_checked = 0
    f = lambda n: Fraction(3*n*n - 2*n + 5, n+1)
    g = lambda n: Fraction((-1)**n * (2*n+1), n+2)
    for n in range(0, 41):
        left, right = finite_abel(f, g, n)
        assert left == right
        abel_checked += 1

    result = {
        "verdict": "PASS_LIGHT_EXACT_ARITHMETIC_REPLAY",
        "row_factorizations": True,
        "three_tap_determinant": "(q - 1)^2",
        "eta_antidiagonal_cases": eta_antidiagonal_checked,
        "eta_dirichlet_cases": eta_dirichlet_checked,
        "one_field_convolution_cases": one_field_checked,
        "first_owner_generic_fixtures": len(first_owner_fixtures),
        "finite_abel_cases": abel_checked,
        "scope_warning": "This replay verifies finite algebra only; it does not establish Lean compilation or the stronger canonical first-owner, wavelet-frame, source-typing, or Mellin-consumer statements.",
        "rh_proved": False,
    }
    out = Path(__file__).with_name("verification.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))

if __name__ == "__main__":
    main()
