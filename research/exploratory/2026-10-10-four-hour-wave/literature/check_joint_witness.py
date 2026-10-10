#!/usr/bin/env python3
"""Exact whole-domain pricing for an OPEN inverse/plain mixed moment.

Every predicate uses an explicit exception and survives Python -O. The
certificate proves scalar implications; it does not prove the mixed moment
or independently rebuild the imported analytic framework.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb
import json
from pathlib import Path
import sys

import sympy as s


def require(condition: object, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def f(value: object) -> Fraction:
    numerator, denominator = s.Rational(value).as_numer_denom()
    return Fraction(int(numerator), int(denominator))


def bernstein_cell(coeff: dict[tuple[int, int], Fraction], dl: Fraction,
                   dw: Fraction, vl: Fraction, vw: Fraction) -> list[Fraction]:
    """Power-to-tensor-Bernstein conversion on one affine rectangle."""
    local: dict[tuple[int, int], Fraction] = {}
    for i in range(3):
        for j in range(4):
            local[i, j] = sum(
                (q * comb(a, i) * dl**(a-i) * dw**i
                 * comb(b, j) * vl**(b-j) * vw**j
                 for (a, b), q in coeff.items() if a >= i and b >= j),
                Fraction(0),
            )
    return [
        sum((local[a, b] * Fraction(comb(i, a), comb(2, a))
             * Fraction(comb(j, b), comb(3, b))
             for a in range(i+1) for b in range(j+1)), Fraction(0))
        for i in range(3) for j in range(4)
    ]


def main() -> None:
    delta, v = s.symbols("delta v", real=True)
    x = s.Rational(1, 2) - v
    alpha, c = s.Rational(5, 6), s.Rational(2, 9)
    boundary = s.Rational(218739, 250000)
    ell, b = s.Rational(31283, 187500), s.Rational(1542571, 12500000)
    lam, cut = s.Rational(49, 100), s.Rational(191, 500)
    lx, ly = (1-b-ell)/2, (1+b-ell)/2
    h, C0 = (1+b+3*ell)/2, -s.Rational(1, 4)+b/6+5*ell/4

    root_lo, root_hi = s.Rational(30347981810, 10**9), s.Rational(30347981811, 10**9)
    require(root_lo**2 < 921 < root_hi**2, "sqrt(921) isolation")
    imported_lower = (1507-2*root_hi)/1653
    require(boundary < imported_lower, "strict improvement over imported boundary")
    require(boundary == s.Rational(11, 12)-ell/4, "signal match")
    require(0 < cut < lam < alpha, "ordered certificate branches")
    gates = {
        "ell_positive": ell,
        "b_positive": b,
        "lx_gt_ell": lx-ell,
        "ly_gt_ell": ly-ell,
        "positive_gram_margin": ly-ell-11*b/6,
        "one_minus_three_ell": 1-3*ell,
        "ell_below_one_fifth": s.Rational(1, 5)-ell,
        "prime_supply_above_seven_over_37": ell/h-s.Rational(7, 37),
        "five_ell_gt_h": 5*ell-h,
        "boundary_domain": boundary-s.Rational(437, 500),
        "analytic_lx_gt_b_plus_ell": lx-b-ell,
        "ly_below_one": 1-ly,
        "positive_low_exponent": lx/2+b/12,
        "floor_saving": -C0-(s.Rational(1, 2)+3*ell/2)/50,
        "intermediate_floor_saving": -((225*ell+50-75*b)/50+78*ell-49*b-73)/300,
        "intermediate_top_saving": -((225*ell+50-75*b)*s.Rational(5, 6)+78*ell-49*b-73)/300,
        "small_row_saving": ly/2-13*h/75-s.Rational(2, 100),
        "small_row_transport": ly/2-13*h/75-s.Rational(2, 100)-(s.Rational(7, 8)-boundary),
        "principal_y_saving": ly/20,
        "principal_h_saving": h/600,
    }
    require(all(value > 0 for value in gates.values()), "retained analytic geometry gate")
    require(lx/2+b/12 == boundary-(4+b)/6, "changed signal exponent")

    A_count, D_count = 2-4*c*x, 3-x-4*c*x
    P_count = A_count*(1-x)
    J = (alpha-delta)*D_count+delta*P_count
    R = 1-delta+(alpha-delta)*delta*P_count/(2*J)
    E = C0+(s.Rational(1, 2)+ell)*delta+ell*x*delta-h*(1-R)
    Q = s.Poly(s.cancel(2*J*(-E)), delta, v)
    require(Q.degree(delta) == 2 and Q.degree(v) == 3, "tensor polynomial degrees")
    require(s.expand(D_count-P_count-(1+x-4*c*x**2)) == 0, "P<=D identity")
    # P>=1-c>0, D<=3 and P<=D throughout x in [0,1/2], hence
    # alpha*(1-c)<=J<=3*alpha=5/2 throughout delta in [0,alpha].
    require(s.Rational(1, 1)-c > 0, "J strictly positive")
    coeff = {powers: f(coef) for powers, coef in Q.terms()}
    minimum: Fraction | None = None
    minimum_cell: list[int] | None = None
    checked = 0
    for di in range(32):
        for vi in range(16):
            values = bernstein_cell(coeff, f(cut)*di/32, f(cut)/32,
                                    Fraction(vi, 32), Fraction(1, 32))
            require(all(value > 0 for value in values), f"nonpositive Bernstein cell {di},{vi}")
            checked += len(values)
            for index, value in enumerate(values):
                if minimum is None or value < minimum:
                    minimum, minimum_cell = value, [di, vi, index//4, index % 4]
    require(checked == 6144 and minimum is not None, "complete rectangle cover")
    require(minimum == Fraction(415930007, 63281250000000), "frozen Bernstein minimum")
    base_gap = minimum/5
    require(base_gap > Fraction(131, 100000000), "uniform base reserve")

    joint_slope = s.Rational(1, 2)+3*ell/2-3*h/2
    require(joint_slope == -s.Rational(1, 4)-3*(b+ell)/4 < 0, "joint first-branch slope")
    Ej1 = C0+h*lam/2+joint_slope*delta
    Ej2 = C0-b*delta/2
    require(Ej1.subs(delta, lam) == Ej2.subs(delta, lam), "joint branch continuity")
    require(s.diff(Ej2, delta) == -b/2 < 0, "joint second branch slope")
    joint_gap = -Ej1.subs(delta, cut)
    require(joint_gap > s.Rational(6033, 10**7), "joint uniform reserve")
    uniform_gap = min(base_gap, f(joint_gap))

    w = s.sqrt(921)
    dc, tc = (49-w)/48, (333+37*w)/1295
    rc, mc = (11+4*w)/185, (256+9*w)/1295
    zi, zp = (87-2*w)/185, 2*(87-2*w)/(7*185)
    require(s.simplify(rc+mc-tc) == 0, "critical total length")
    require(s.simplify(zi-(1-rc)/2) == 0, "critical inverse capacity")
    require(s.simplify(zp-(1-2*mc)*c) == 0, "critical plain capacity")
    require(s.simplify(R.subs({delta: dc, v: 0})-s.Rational(2, 3)) == 0, "critical row count")
    # Lower sqrt endpoint gives a strict lower bound on lambda_*.
    require(lam < 3*(49-root_hi)/48-s.Rational(2, 3), "priced slope below old critical slope")
    critical = {
        "delta": dc, "t": tc, "r": rc, "m": mc,
        "z_inverse": zi, "z_plain": zp,
        "lambda_critical": 3*dc-s.Rational(2, 3),
        "same_pair_moment_threshold": s.Rational(2, 3)+dc*tc,
        "marginal_moment_exponents": [1+dc*mc, 1+dc*rc/2],
    }
    critical_text = {
        key: ([str(s.simplify(item)) for item in value] if isinstance(value, list)
              else str(s.simplify(value))) for key, value in critical.items()
    }
    result = {
        "status": "PASS_EXACT_CONDITIONAL_JOINT_MOMENT_PRICING",
        "scope": "whole-domain scalar implication from open source-qualified mixed moment",
        "joint_moment_proved": False,
        "imported_bound_independently_rebuilt": False,
        "new_zero_free_theorem_claimed": False,
        "rh_proved": False,
        "parameters": {"kappa": "3/4", "c": str(c), "lambda": str(lam),
                       "B": str(boundary), "ell": str(ell), "b": str(b),
                       "delta_cut": str(cut)},
        "geometry_gates": {key: str(value) for key, value in gates.items()},
        "polynomial_power_coefficients": {f"{i},{j}": str(value) for (i, j), value in sorted(coeff.items())},
        "bernstein_cells": 512,
        "bernstein_coefficients_checked": checked,
        "minimum_bernstein_coefficient": str(minimum),
        "minimum_bernstein_cell_and_indices": minimum_cell,
        "base_minus_E_lower_bound": str(base_gap),
        "joint_minus_E_lower_bound": str(joint_gap),
        "uniform_minus_E_lower_bound": str(uniform_gap),
        "critical_configuration": critical_text,
    }
    receipt = json.dumps(result, indent=2, sort_keys=True)+"\n"
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(receipt, encoding="utf-8")
    elif len(sys.argv) > 2:
        raise SystemExit("usage: python check_joint_witness.py [OUTPUT_JSON]")
    print(receipt, end="")


if __name__ == "__main__":
    main()
