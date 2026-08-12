#!/usr/bin/env python3
"""Finite regression for the Cauchy-square / Clark / Jordan bridge.

Checks exact algebraic identities and high-precision synthetic controls.
It does not prove any prime-side monotonicity theorem or RH.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp

mp.mp.dps = 70


def line_p(a: mp.mpf, u: mp.mpf) -> mp.mpf:
    return a / (a*a + u*u)


def line_n(a: mp.mpf, u: mp.mpf) -> mp.mpf:
    return a**4 / (a*a + u*u)**2


def line_c(a: mp.mpf, u: mp.mpf) -> mp.mpf:
    return u*u / (a*a + u*u)**3


def pair_p(a: mp.mpf, d: mp.mpf, u: mp.mpf) -> mp.mpf:
    z = mp.mpc(d, u)
    return mp.re(2*a / (a*a - z*z))


def pair_n(a: mp.mpf, d: mp.mpf, u: mp.mpf) -> mp.mpf:
    z = mp.mpc(d, u)
    return 2*mp.re(a**4 / (a*a - z*z)**2)


def pair_c(a: mp.mpf, d: mp.mpf, u: mp.mpf) -> mp.mpf:
    z = mp.mpc(d, u)
    return -2*mp.re(z*z / (a*a - z*z)**3)


def line_n_ft(a: mp.mpf, xi: mp.mpf) -> mp.mpf:
    return mp.pi*a/2 * (1+a*abs(xi))*mp.e**(-a*abs(xi))


def pair_n_ft_inside(a: mp.mpf, d: mp.mpf, xi: mp.mpf) -> mp.mpf:
    return mp.pi*a * (1+a*abs(xi))*mp.e**(-a*abs(xi))*mp.cosh(d*xi)


def prime_factors(n: int) -> list[int]:
    out = []
    p = 2
    m = n
    while p*p <= m:
        if m % p == 0:
            out.append(p)
            while m % p == 0:
                m //= p
        p += 1 if p == 2 else 2
    if m > 1:
        out.append(m)
    return out


def jordan_ratio_coefficient(a: int, n: int) -> Fraction:
    value = Fraction(n**a, 1)
    for p in prime_factors(n):
        value *= Fraction(p**(2*a)-1, p**(2*a))
    return value


def sieve_ratio_coefficient(a: int, n: int) -> Fraction:
    value = Fraction(1, 1)
    for p in prime_factors(n):
        value *= Fraction(p**(2*a)-1, p**(2*a))
    return value


def dyadic_increment(a: mp.mpf, u: mp.mpf) -> mp.mpf:
    return line_n(2*a, u)-line_n(a, u)


def dyadic_channel_square(a: mp.mpf, u: mp.mpf) -> mp.mpf:
    den = (a*a+u*u)*(4*a*a+u*u)
    g1 = 2*mp.sqrt(6)*a**3*u/den
    g2 = mp.sqrt(15)*a**2*u**2/den
    return g1*g1+g2*g2


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n+1) if n % d == 0]


def phi(n: int) -> int:
    value = n
    for p in prime_factors(n):
        value = value // p * (p-1)
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    checks = 0
    max_primitive_error = mp.mpf(0)
    max_derivative_error = mp.mpf(0)
    max_integral_error = mp.mpf(0)
    max_fourier_error = mp.mpf(0)
    max_clark_error = mp.mpf(0)
    max_totient_error = mp.mpf(0)

    for a in [mp.mpf("0.17"), mp.mpf("0.41"), mp.mpf("0.73")]:
        for u in [mp.mpf("0"), mp.mpf("0.23"), mp.mpf("1.4"), mp.mpf("5.0")]:
            p = line_p(a, u)
            pp = mp.diff(lambda aa: line_p(aa, u), a)
            n1 = (a*p-a*a*pp)/2
            err = abs(n1-line_n(a,u))
            max_primitive_error = max(max_primitive_error, err)
            assert err < mp.mpf("1e-60")
            nd = mp.diff(lambda aa: line_n(aa,u), a)
            err = abs(nd-4*a**3*line_c(a,u))
            max_derivative_error = max(max_derivative_error, err)
            assert err < mp.mpf("1e-60")
            checks += 2

    for a,d,u in [
        (mp.mpf("0.51"),mp.mpf("0.18"),mp.mpf("0")),
        (mp.mpf("0.51"),mp.mpf("0.18"),mp.mpf("0.7")),
        (mp.mpf("0.31"),mp.mpf("0.42"),mp.mpf("0.2")),
        (mp.mpf("0.74"),mp.mpf("0.49"),mp.mpf("1.8")),
    ]:
        p = pair_p(a,d,u)
        pp = mp.diff(lambda aa: pair_p(aa,d,u), a)
        n1 = (a*p-a*a*pp)/2
        err = abs(n1-pair_n(a,d,u))
        max_primitive_error = max(max_primitive_error, err)
        assert err < mp.mpf("1e-58")
        nd = mp.diff(lambda aa: pair_n(aa,d,u), a)
        err = abs(nd-4*a**3*pair_c(a,d,u))
        max_derivative_error = max(max_derivative_error, err)
        assert err < mp.mpf("1e-57")
        checks += 2

    matched_right_derivatives = []
    y = mp.mpf("0.23")
    for delta in [mp.mpf("1e-2"), mp.mpf("1e-3"), mp.mpf("1e-4")]:
        a = y + delta
        derivative = 4*a**3*pair_c(a,y,mp.mpf(0))
        assert derivative < 0
        matched_right_derivatives.append(mp.nstr(derivative, 22))
        checks += 1

    projector_samples = []
    for a,d in [
        (mp.mpf("0.5"),mp.mpf("0.2")),
        (mp.mpf("0.3"),mp.mpf("0.1")),
        (mp.mpf("0.5"),mp.mpf("0.7")),
    ]:
        i0 = mp.quad(lambda uu: pair_n(a,d,uu), [-mp.inf, mp.inf])
        i2 = mp.quad(lambda uu: uu*uu*pair_n(a,d,uu), [-mp.inf, mp.inf])
        e0 = mp.pi*a if d < a else mp.mpf(0)
        e2 = mp.pi*a*(a*a-d*d) if d < a else mp.mpf(0)
        err = max(abs(i0-e0), abs(i2-e2))
        max_integral_error = max(max_integral_error, err)
        assert err < mp.mpf("1e-48")
        projector_samples.append({
            "a": mp.nstr(a,8), "d": mp.nstr(d,8),
            "mass": mp.nstr(i0,22), "expected_mass": mp.nstr(e0,22),
            "second_moment": mp.nstr(i2,22), "expected_second_moment": mp.nstr(e2,22),
        })
        checks += 2

    for a in [mp.mpf("0.3"),mp.mpf("0.7")]:
        i0 = mp.quad(lambda uu: line_n(a,uu), [-mp.inf, mp.inf])
        i2 = mp.quad(lambda uu: uu*uu*line_n(a,uu), [-mp.inf, mp.inf])
        assert abs(i0-mp.pi*a/2) < mp.mpf("1e-50")
        assert abs(i2-mp.pi*a**3/2) < mp.mpf("1e-50")
        checks += 2

    for a,xi in [
        (mp.mpf("0.4"),mp.mpf("0")),
        (mp.mpf("0.4"),mp.mpf("0.8")),
        (mp.mpf("0.7"),mp.mpf("2.1")),
    ]:
        if xi == 0:
            numeric = mp.quad(lambda uu: line_n(a,uu), [-mp.inf,mp.inf])
        else:
            numeric = 2*mp.quadosc(lambda uu: line_n(a,uu)*mp.cos(xi*uu), [0,mp.inf], omega=xi)
        closed = line_n_ft(a,xi)
        err = abs(numeric-closed)
        max_fourier_error = max(max_fourier_error,err)
        assert err < mp.mpf("1e-42")
        checks += 1
    for a,d,xi in [
        (mp.mpf("0.5"),mp.mpf("0.2"),mp.mpf("0")),
        (mp.mpf("0.5"),mp.mpf("0.2"),mp.mpf("0.9")),
        (mp.mpf("0.7"),mp.mpf("0.4"),mp.mpf("1.7")),
    ]:
        if xi == 0:
            numeric = mp.quad(lambda uu: pair_n(a,d,uu), [-mp.inf,mp.inf])
        else:
            numeric = 2*mp.quadosc(lambda uu: pair_n(a,d,uu)*mp.cos(xi*uu), [0,mp.inf], omega=xi)
        closed = pair_n_ft_inside(a,d,xi)
        err = abs(numeric-closed)
        max_fourier_error = max(max_fourier_error,err)
        assert err < mp.mpf("1e-38")
        checks += 1

    for a,u in [
        (mp.mpf("0.2"),mp.mpf("0.3")),
        (mp.mpf("0.6"),mp.mpf("1.1")),
        (mp.mpf("0.4"),mp.mpf("3.0")),
    ]:
        factor = lambda xx: (-a+1j*xx)/(a+1j*xx)
        phase_derivative = mp.im(mp.diff(factor,u)/factor(u))
        expected = -2*a/(a*a+u*u)
        err = abs(phase_derivative-expected)
        max_clark_error = max(max_clark_error,err)
        assert err < mp.mpf("1e-60")
        soft = a**2*(a/(a*a+u*u))**2
        assert abs(soft-line_n(a,u)) < mp.mpf("1e-60")
        checks += 2

    exact_jordan_checks = 0
    for a in [1,2,3]:
        for n in range(1,101):
            ca = jordan_ratio_coefficient(a,n)
            assert ca > 0
            exact_jordan_checks += 1
    for a,b in [(1,1),(1,2),(2,3)]:
        for n in range(1,81):
            lhs = jordan_ratio_coefficient(a+b,n)
            rhs = sum(
                jordan_ratio_coefficient(a,d)*d**b
                *jordan_ratio_coefficient(b,n//d)*Fraction(1,(n//d)**a)
                for d in divisors(n)
            )
            assert lhs == rhs
            exact_jordan_checks += 1
    checks += exact_jordan_checks

    for n in range(1,80):
        numeric = mp.sqrt(n)
        for p in prime_factors(n):
            numeric *= 1-mp.mpf(1)/p
        expected = mp.mpf(phi(n))/mp.sqrt(n)
        err = abs(numeric-expected)
        max_totient_error = max(max_totient_error,err)
        assert err < mp.mpf("1e-60")
        checks += 1

    max_dyadic_square_error = mp.mpf(0)
    for a in [mp.mpf("0.11"),mp.mpf("0.37"),mp.mpf("0.81")]:
        for u in [mp.mpf("0"),mp.mpf("0.07"),mp.mpf("0.9"),mp.mpf("4.2")]:
            lhs = dyadic_increment(a,u)
            rhs = dyadic_channel_square(a,u)
            err = abs(lhs-rhs)
            max_dyadic_square_error = max(max_dyadic_square_error,err)
            assert lhs >= -mp.mpf("1e-65") and err < mp.mpf("1e-60")
            checks += 1

    exact_sieve_checks = 0
    for a in [1,2,3]:
        for n in range(1,101):
            qa = sieve_ratio_coefficient(a,n)
            assert 0 < qa <= 1
            exact_sieve_checks += 1
    for a,b in [(1,1),(1,2),(2,3)]:
        for n in range(1,81):
            lhs = sieve_ratio_coefficient(a+b,n)
            rhs = sum(
                sieve_ratio_coefficient(a,d)
                *sieve_ratio_coefficient(b,n//d)
                *Fraction(1,(n//d)**(2*a))
                for d in divisors(n)
            )
            assert lhs == rhs
            exact_sieve_checks += 1
    checks += exact_sieve_checks

    result: dict[str,Any] = {
        "classification": "PASS_CAUCHY_SQUARE_CLARK_JORDAN_BRIDGE",
        "checks": checks,
        "exact_jordan_cocycle_checks": exact_jordan_checks,
        "exact_sieve_cocycle_checks": exact_sieve_checks,
        "max_dyadic_two_channel_square_error": mp.nstr(max_dyadic_square_error,12),
        "max_primitive_identity_error": mp.nstr(max_primitive_error,12),
        "max_curvature_derivative_error": mp.nstr(max_derivative_error,12),
        "max_projector_integral_error": mp.nstr(max_integral_error,12),
        "max_fourier_transform_error": mp.nstr(max_fourier_error,12),
        "max_clark_phase_error": mp.nstr(max_clark_error,12),
        "max_totient_specialization_error": mp.nstr(max_totient_error,12),
        "matched_pair_right_derivatives": matched_right_derivatives,
        "projector_samples": projector_samples,
        "scope": "finite algebra and synthetic high-precision controls only; no prime-side monotonicity or RH claim",
    }
    text = json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.json is not None:
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(text,encoding="utf-8")
    else:
        print(text,end="")
    print("PASS_CAUCHY_SQUARE_CLARK_JORDAN_BRIDGE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
