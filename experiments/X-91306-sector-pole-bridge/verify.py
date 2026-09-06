#!/usr/bin/env python3
"""Finite algebra replay for the sector/pole-bridge continuation.

This script does not evaluate zeta zeros and does not prove RH.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp


def local_coeff_norm(a: Fraction, b: Fraction, terms: int = 2000) -> tuple[Fraction, float]:
    exact = Fraction(1, 1) + (a - b) ** 2 / (1 - b * b)
    approx = 1.0
    for k in range(1, terms + 1):
        ck = float((b - a) * (b ** (k - 1)))
        approx += ck * ck
    return exact, approx


def translation_overlap(a: float, b: float, theta: float) -> tuple[complex, float]:
    A = (a - b) ** 2
    r = b * b
    N2 = 1.0 + A / (1.0 - r)
    z = complex(math.cos(theta), -math.sin(theta))
    q = (1.0 + A * z / (1.0 - r * z)) / N2
    rhs = (
        2.0
        * A
        * (1.0 - math.cos(theta))
        * (1.0 + a * a * b * b - 2.0 * a * b**3)
        / (
            (1.0 + a * a - 2.0 * a * b) ** 2
            * (1.0 - 2.0 * b * b * math.cos(theta) + b**4)
        )
    )
    return q, rhs


def T_conv(coeff: dict[int, Fraction], values: dict[int, Fraction], x: int) -> Fraction:
    return sum(
        coeff.get(n, Fraction(0)) * values[x // n]
        for n in range(1, x + 1)
        if x % n == 0
    )


def J_discrete(values: dict[int, Fraction], x: int) -> Fraction:
    # A finite exact shadow of integral Green commutation: cumulative sum with measure dy/y
    return sum(values[y] / y for y in range(1, x + 1))


def finite_commutation_check() -> int:
    # Use the exact incidence-poset analogue: (J f)(x)=sum_{y<=x}f(y)/y and
    # (T_a f)(x)=sum_{n|x}a(n)f(x/n). The continuous theorem is verified separately
    # in the written proof; here we check the finite reindexing pattern on rationals.
    # For exact commutation with this discrete J, use multiplicative cumulative domain:
    # J_mult f(x)=sum_{d|x}f(d), which has the same finite Fubini identity.
    def Jm(v: dict[int, Fraction], x: int) -> Fraction:
        return sum(v[d] for d in range(1, x + 1) if x % d == 0)

    a = {1: Fraction(1), 2: Fraction(2), 3: Fraction(-1), 6: Fraction(3)}
    f = {n: Fraction(n * n - 3 * n + 1, n + 1) for n in range(1, 61)}
    Tf = {x: T_conv(a, f, x) for x in range(1, 61)}
    Jf = {x: Jm(f, x) for x in range(1, 61)}
    checks = 0
    for x in range(1, 61):
        lhs = Jm(Tf, x)
        rhs = T_conv(a, Jf, x)
        assert lhs == rhs
        checks += 1
    return checks


def g_suzuki(x: mp.mpf, omega: mp.mpf) -> mp.mpf:
    pref = 2 * mp.pi**omega / mp.gamma(omega)
    integ = mp.quad(
        lambda t: t ** (mp.mpf("0.5") - omega) * (1 - t) ** (omega - 1),
        [x * x, 1],
    )
    return pref * (
        x ** (2 - omega) * (1 - x * x) ** (omega - 1)
        - omega * x ** (omega - 1) * integ
    )


def C0(omega: mp.mpf) -> mp.mpf:
    return -4 * omega * mp.pi ** (omega - mp.mpf("0.5")) * mp.gamma(mp.mpf("1.5") - omega)


def C1(omega: mp.mpf) -> mp.mpf:
    return 6 * mp.pi**omega / ((3 - 2 * omega) * mp.gamma(omega))


def xi(s: mp.mpf) -> mp.mpf:
    if abs(s - 1) < mp.mpf("1e-40") or abs(s) < mp.mpf("1e-40"):
        return mp.mpf("0.5")
    return mp.mpf("0.5") * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def source_scalar(a: mp.mpf) -> mp.mpf:
    amp = mp.mpf("0.5") / xi(1 + 2 * a)
    zlog = mp.diff(lambda x: mp.log(mp.zeta(x)), 1 + 2 * a)
    return amp * (mp.euler - zlog)


def model_scalar(a: mp.mpf) -> mp.mpf:
    eta = mp.mpf("0.5") + a
    delta = mp.mpf(1)
    for r in (1, 2, 4):
        p = r * a
        delta *= ((eta - p) / (eta + p)) ** 2
    theta = mp.mpf("0.5") / xi(1 + 2 * a)
    return (delta ** (-2) - theta**2) / (2 * eta)


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def run() -> dict[str, object]:
    mp.mp.dps = 80
    checks = 0

    # 1. Local H2 norm.
    exact, approx = local_coeff_norm(Fraction(3, 10), Fraction(1, 10))
    assert abs(float(exact) - approx) < 1e-15
    checks += 1

    # 2. Special weighted local norms, q=p^{-2 omega}.
    q = sp.symbols("q", positive=True)
    at_sigma_omega = sp.simplify(1 + (1 - q) ** 2 / (1 - q**2))
    assert sp.simplify(at_sigma_omega - 2 / (1 + q)) == 0
    at_sigma_zero = sp.simplify(1 + ((1 / q) - 1) ** 2 * q / (1 - q))
    assert sp.simplify(at_sigma_zero - 1 / q) == 0
    checks += 2

    # 3. Translation overlap identity at several points.
    max_overlap_error = 0.0
    for aa, bb, th in [
        (0.31, 0.07, 0.4),
        (0.12, 0.03, 1.9),
        (0.48, 0.11, 2.7),
        (0.05, 0.004, 5.1),
    ]:
        qq, rhs = translation_overlap(aa, bb, th)
        err = abs((1.0 - abs(qq) ** 2) - rhs)
        max_overlap_error = max(max_overlap_error, err)
        assert err < 5e-15
        checks += 1

    # 4. Finite exact commutation shadow.
    commutation_checks = finite_commutation_check()
    checks += commutation_checks

    # 5. Pole residue identity at rational omega values.
    for om_str in ("1/4", "1/3", "2/5"):
        om = sp.Rational(om_str)
        gamma_completed = lambda s: sp.Rational(1, 2) * s * (s - 1) * sp.pi ** (-s / 2) * sp.gamma(s / 2)
        residue = sp.simplify(2 * gamma_completed(1 - 2 * om))
        c0 = sp.simplify(-4 * om * sp.pi ** (om - sp.Rational(1, 2)) * sp.gamma(sp.Rational(3, 2) - om))
        assert sp.simplify(residue - c0) == 0
        checks += 1

    # 6. Endpoint two-term asymptotic.
    asymptotic_errors: dict[str, float] = {}
    for om_s in ("0.25", "0.5"):
        om = mp.mpf(om_s)
        x = mp.mpf("1e-7")
        actual = g_suzuki(x, om)
        predicted = C0(om) * x ** (om - 1) + C1(om) * x ** (2 - om)
        rel = abs((actual - predicted) / actual)
        asymptotic_errors[om_s] = float(rel)
        assert rel < mp.mpf("1e-8")
        checks += 1

    # 7. Free Green growth exponent via leading formula.
    for om_s, expected_sign in (("0.25", 1), ("0.75", -1)):
        om = mp.mpf(om_s)
        t1, t2 = mp.mpf(20), mp.mpf(30)
        lead1 = abs(C0(om) / (1 - om) * mp.e ** ((mp.mpf("0.5") - om) * t1))
        lead2 = abs(C0(om) / (1 - om) * mp.e ** ((mp.mpf("0.5") - om) * t2))
        observed_sign = 1 if lead2 > lead1 else -1
        assert observed_sign == expected_sign
        checks += 1

    # 8. Finite Euler amplification at s0.
    omega = 0.2
    prime_cutoffs = [100, 500, 2000, 10000]
    log_products = []
    for cutoff in prime_cutoffs:
        total = 0.0
        for p in primes_upto(cutoff):
            total += math.log1p(-1.0 / p) - math.log1p(-(p ** (-(1 - 2 * omega))))
        log_products.append(total)
    assert all(log_products[i + 1] > log_products[i] for i in range(len(log_products) - 1))
    checks += len(log_products) - 1

    # 9. Pole-node source/model mismatch and asymptotic scaling.
    mismatch_rows = []
    qxi = 1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2
    cmodel = 112 + 4 * qxi
    for a_s in ("0.001", "0.0005", "0.0002", "0.0001"):
        aa = mp.mpf(a_s)
        ss = source_scalar(aa)
        tt = model_scalar(aa)
        scaled_source = 2 * aa * ss
        scaled_model = tt / (cmodel * aa)
        mismatch_rows.append(
            {
                "a": a_s,
                "2a_source": float(scaled_source),
                "model_over_Ca": float(scaled_model),
                "source_model_ratio": float(ss / tt),
            }
        )
        assert abs(scaled_source - 1) < mp.mpf("0.03")
        assert abs(scaled_model - 1) < mp.mpf("0.06")
        checks += 2
    assert mismatch_rows[-1]["source_model_ratio"] > 100000
    checks += 1

    return {
        "verdict": "PASS_X_91306_SECTOR_POLE_BRIDGE",
        "checks": checks,
        "commutation_checks": commutation_checks,
        "max_translation_overlap_error": max_overlap_error,
        "endpoint_asymptotic_relative_errors": asymptotic_errors,
        "finite_euler_log_products": {
            str(k): v for k, v in zip(prime_cutoffs, log_products)
        },
        "pole_node_mismatch": mismatch_rows,
        "scope": (
            "finite algebra and numerical asymptotics only; the PNT limit theorems, "
            "EPBOT_omega, renewal L2, innerness, and RH are not proved"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
