#!/usr/bin/env python3
"""Finite exact replay for L-91323/L-91324. Does not evaluate zeta."""

from fractions import Fraction
import argparse
import json
from pathlib import Path
import cmath
import math


def universal_coeff_check(alpha: Fraction, beta: Fraction) -> None:
    c2 = (1-beta)**2 / (1-alpha)**2
    delta2 = (beta-alpha)*(1-alpha*beta)/(1-alpha)**2

    # Laurent coefficients of
    # |1-beta z|^2 - c^2 |1-alpha z|^2
    # - delta^2 |1-z|^2 on |z|=1.
    const = (1+beta*beta) - c2*(1+alpha*alpha) - 2*delta2
    zcoef = -beta + c2*alpha + delta2
    assert const == 0
    assert zcoef == 0


def cascade_identity(vals):
    scalar = 1.0 + 0.0j
    detail_energy = 0.0
    for m, d in vals:
        detail_energy += abs(scalar*d)**2
        scalar *= m
    return abs(scalar)**2 + detail_energy


def local_prime(p: int, a: float, sigma: float, theta: float):
    alpha = p**(-(sigma+2*a))
    beta = p**(-sigma)
    c = (1-beta)/(1-alpha)
    delta2 = (beta-alpha)*(1-alpha*beta)/(1-alpha)**2
    z = cmath.exp(-1j*theta*math.log(p))
    m = c*(1-alpha*z)/(1-beta*z)
    d = math.sqrt(delta2)*(1-z)/(1-beta*z)
    return m, d


def run():
    checks = 0
    for alpha, beta in [
        (Fraction(1, 8), Fraction(1, 4)),
        (Fraction(1, 27), Fraction(1, 9)),
        (Fraction(2, 25), Fraction(1, 5)),
        (Fraction(3, 40), Fraction(1, 4)),
    ]:
        universal_coeff_check(alpha, beta)
        checks += 2

    max_err = 0.0
    for theta in [0.0, 0.1, 0.7, 1.3, 2.1]:
        vals = [local_prime(p, 0.25, 2.0, theta) for p in [2,3,5,7,11,13]]
        err = abs(cascade_identity(vals)-1.0)
        max_err = max(max_err, err)
        assert err < 2e-13
        checks += 1

    # Exact scalar scale cocycle with rational alpha/beta chain.
    # beta0=1/4, alpha0=beta1=1/8, alpha1=1/32.
    zvals = [complex(1,0), cmath.exp(0.4j), cmath.exp(1.2j)]
    for z in zvals:
        q0 = (1-Fraction(1,8)*z)/(1-Fraction(1,4)*z)
        q1 = (1-Fraction(1,32)*z)/(1-Fraction(1,8)*z)
        q2 = (1-Fraction(1,32)*z)/(1-Fraction(1,4)*z)
        assert abs(q0*q1-q2) < 2e-15
        checks += 1

    # Critical detail asymptotic ratio tends to one.
    ratios = []
    a = 0.2
    for p in [101, 1009, 10007, 100003]:
        alpha = p**(-0.5-a)
        beta = p**(-0.5+a)
        delta2 = (beta-alpha)*(1-alpha*beta)/(1-alpha)**2
        ratios.append(delta2 / p**(-0.5+a))
    assert abs(ratios[-1]-1.0) < 0.02
    checks += 1

    return {
        "verdict": "PASS_X_91304_EULER_JULIA_CASCADE",
        "checks": checks,
        "max_boundary_norm_error": max_err,
        "critical_asymptotic_ratios": ratios,
        "scope": "finite local/cascade algebra only; GEJWO_a and RH are not proved",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", type=Path)
    ns = ap.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if ns.json:
        ns.json.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
