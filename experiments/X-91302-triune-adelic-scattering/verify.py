#!/usr/bin/env python3
"""Exact/symbolic replay for T-91302. It does not evaluate zeta."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


def period_packet(coeff: list[int], degree: int) -> list[int]:
    q = 2**degree
    return [
        sum(coeff[j] for j in range(degree + 1) if r % (2**j) == 0)
        for r in range(q)
    ]


def finite_dft_nested(coeff: list[int], degree: int, k: int) -> int:
    # Exact formula for the unnormalised DFT of a divisibility packet.
    return sum(
        (2**ell) * coeff[degree - ell]
        for ell in range(degree + 1)
        if k % (2**ell) == 0
    )


def pick_control() -> Fraction:
    # PR #398 bare symmetric control at y=1/4, u=1/8.
    y = Fraction(1, 4)
    u = Fraction(1, 8)

    def f(q: Fraction) -> Fraction:
        return (
            (q + Fraction(1, 2)) ** 2 - y**2
        ) / (
            (q + Fraction(1, 2) + u) ** 2 - y**2
        )

    q = Fraction(1)
    r = Fraction(2)
    a11 = (1 - f(q) ** 2) / (1 + u + 2 * q)
    a22 = (1 - f(r) ** 2) / (1 + u + 2 * r)
    a12 = (1 - f(q) * f(r)) / (1 + u + q + r)
    return a11 * a22 - a12**2


def run() -> dict[str, object]:
    checks = 0

    # 1. Local Laurent factor.
    x = sp.symbols("x", nonzero=True)
    qstar = (1 - x) * (1 - 2*x) * (2 - x) * (1 - 4*x)
    rhs = 16 * (1 - x) * (1 - x/2) * (1 - 1/(2*x)) * (1 - 1/(4*x))
    assert sp.simplify(x**-2 * qstar - rhs) == 0
    checks += 1

    # 2. Exact period-16 DFT packet.
    coeff = [2, -15, 35, -30, 8]
    expected = [0, 2, -13, 2, 22, 2, -13, 2, -8, 2, -13, 2, 22, 2, -13, 2]
    packet = period_packet(coeff, 4)
    assert packet == expected
    checks += 16
    for k in range(16):
        assert finite_dft_nested(coeff, 4, k) == 4 * packet[k]
        checks += 1
    for power in range(4):
        assert sum((r**power) * packet[r] for r in range(16)) == 0
        checks += 1

    # 3. Cayley congruence.
    l, m = sp.symbols("l m")
    d_l = (1-l)/(1+l)
    d_m = (1-m)/(1+m)
    assert sp.simplify(
        1 - d_l*d_m - 2*(l+m)/((1+l)*(1+m))
    ) == 0
    checks += 1

    # 4. Disk conservative-colligation identity for an exact orthogonal U.
    z, w = sp.symbols("z w")
    A = sp.Rational(3, 5)
    B = sp.Rational(4, 5)
    C = sp.Rational(4, 5)
    D = -sp.Rational(3, 5)
    S_z = D + z*C*(1-z*A)**-1*B
    S_w = D + w*C*(1-w*A)**-1*B
    lhs = (1-S_z*S_w)/(1-z*w)
    rhs_coll = C*(1-z*A)**-1*(1-w*A)**-1*C
    assert sp.simplify(lhs-rhs_coll) == 0
    checks += 1

    # 5. Resolvent identity.
    zz, ww = sp.symbols("zz ww")
    H = sp.diag(2, 5)
    g = sp.Matrix([1, 2])
    I = sp.eye(2)
    m_z = (g.T * (H-zz*I).inv() * g)[0]
    m_w = (g.T * (H-ww*I).inv() * g)[0]
    lhs_res = sp.simplify((m_z-m_w)/(zz-ww))
    rhs_res = sp.simplify((g.T*(H-zz*I).inv()*(H-ww*I).inv()*g)[0])
    assert sp.simplify(lhs_res-rhs_res) == 0
    checks += 1

    # 6. Log-odds Sturm-Liouville cell.
    v, a = sp.symbols("v a", positive=True)
    t = sp.atanh(v)
    up = sp.exp(a*t)
    um = sp.exp(-a*t)
    for ufun in (up, um):
        ode = -sp.diff((1-v**2)*sp.diff(ufun, v), v) + a**2/(1-v**2)*ufun
        assert sp.simplify(ode) == 0
        checks += 1
    c = sp.cosh(a*t)
    s = sp.sinh(a*t)
    assert sp.simplify((1-v**2)*sp.diff(c, v)-a*s) == 0
    assert sp.simplify((1-v**2)*sp.diff(s, v)-a*c) == 0
    assert sp.simplify(s/c-sp.tanh(a*t)) == 0
    checks += 3

    # 7. Brownian two-copy algebra.
    z1, z2, r, ss, aa = sp.symbols("z1 z2 r ss aa")
    Ssum = z1 + z2
    Delta = z1 - z2
    raw1 = sp.exp(r*z1 + ss*z2) * sp.sinh(aa*Ssum)
    raw2 = sp.exp(r*z2 + ss*z1) * sp.sinh(aa*Ssum)
    sym = sp.simplify((raw1+raw2)/2)
    mean = (r+ss)*Ssum/2
    delta = (r-ss)*Delta/2
    target = (
        sp.exp(mean+delta) + sp.exp(mean-delta)
    ) * sp.sinh(aa*Ssum) / 2
    assert sp.simplify(sym-target) == 0
    checks += 1

    # 8. Exact hostile control.
    det = pick_control()
    assert det < 0
    checks += 1

    return {
        "verdict": "PASS_X_91302_TRIUNE_ADELIC_SCATTERING",
        "checks": checks,
        "period16": packet,
        "pick_control_determinant": str(det),
        "scope": (
            "finite algebra only; AOT_a, innerness, the renewal estimate, "
            "and RH are not proved"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
