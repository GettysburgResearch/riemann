#!/usr/bin/env python3
"""Exact scalar certificate for a proposed extension of the cubic-theta method.

This checks rational exponent identities and inequalities. The recorded
independent written-adapter review is metadata, not proved by this checker;
the imported analytic inputs have not been independently rebuilt here.
Run with the prepared SymPy environment; explicit predicates also survive -O.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as s


def require(condition: object, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    delta, v = s.symbols("delta v", real=True)
    kappa = s.Rational(749915, 1000000)
    boundary = s.Rational(87495703, 100000000)
    ell = s.Rational(12512891, 75000000)
    b = s.Rational(1542571, 12500000)
    alpha = s.Rational(5, 6)
    c = 1 / (6 * kappa)
    x = s.Rational(1, 2) - v
    lx, ly = (1 - b - ell) / 2, (1 + b - ell) / 2
    h = (1 + b + 3 * ell) / 2
    C0 = -s.Rational(1, 4) + b / 6 + 5 * ell / 4

    root_lo = s.Rational(30347981810, 1000000000)
    root_hi = s.Rational(30347981811, 1000000000)
    require(root_lo**2 < 921 < root_hi**2, "sqrt(921) rational isolation")
    imported_upper = (1507 - 2 * root_lo) / 1653
    imported_lower = (1507 - 2 * root_hi) / 1653
    require(imported_upper < (1 + kappa) / 2, "known boundary permits chosen kappa")
    require(boundary < imported_lower, "candidate strictly improves imported boundary")
    require(boundary == s.Rational(11, 12) - ell / 4, "direct/signal match")
    require(s.Rational(13, 18) <= kappa < s.Rational(3, 4), "proposed new moment range")
    gates = {
        "ell_positive": ell,
        "b_positive": b,
        "lx_gt_ell": lx - ell,
        "ly_gt_ell": ly - ell,
        "positive_gram_margin": ly - ell - 11 * b / 6,
        "one_minus_three_ell": 1 - 3 * ell,
        "ell_below_one_fifth": s.Rational(1, 5) - ell,
        "prime_supply_above_seven_over_37": ell / h - s.Rational(7, 37),
        "five_ell_gt_h": 5 * ell - h,
        "boundary_domain": boundary - s.Rational(437, 500),
        "analytic_lx_gt_b_plus_ell": lx - b - ell,
        "ly_below_one": 1 - ly,
        "positive_low_exponent": lx / 2 + b / 12,
        "floor_saving": -C0 - (s.Rational(1, 2) + 3 * ell / 2) / 50,
        "intermediate_floor_saving": -((225 * ell + 50 - 75 * b) / 50 + 78 * ell - 49 * b - 73) / 300,
        "intermediate_top_saving": -((225 * ell + 50 - 75 * b) * s.Rational(5, 6) + 78 * ell - 49 * b - 73) / 300,
        "small_row_saving": ly / 2 - 13 * h / 75 - s.Rational(2, 100),
        "small_row_transport": ly / 2 - 13 * h / 75 - s.Rational(2, 100) - (s.Rational(7, 8) - boundary),
        "principal_y_saving": ly / 20,
        "principal_h_saving": h / 600,
    }
    require(all(value > 0 for value in gates.values()), "unchanged geometric gate")
    require(lx / 2 + b / 12 == boundary - (4 + b) / 6, "low/signal exponent identity")
    require(s.Rational(2, 9) < c < s.Rational(3, 13), "generalized crossing coefficient range")

    # Full positive-capacity crossing geometry, with unchanged inverse gates.
    cg, xg, tg = s.symbols("cg xg tg", real=True)
    Ag, Dg = 2 - 4 * cg * xg, 3 - xg - 4 * cg * xg
    rg = (Ag * tg + (2 * cg - 1) * xg) / Dg
    mg = tg - rg
    r1 = rg.subs(tg, 1)
    require(s.cancel(rg.subs(tg, s.Rational(3, 2)) - 1) == 0, "crossing r(3/2)=1")
    require(s.cancel(mg.subs(tg, s.Rational(3, 2)) - s.Rational(1, 2)) == 0,
            "crossing m(3/2)=1/2")
    require(s.cancel(s.diff(r1, xg) - (2 * cg - 1) / Dg**2) == 0,
            "r(1) decreases in x")
    require(s.cancel(r1.subs(xg, s.Rational(1, 2)) - s.Rational(23, 37)
                     - (18 * cg - 4) / (37 * (5 - 4 * cg))) == 0,
            "crossing inverse threshold retains strict margin")
    require(s.cancel(mg.subs(tg, 1) - s.Rational(1, 3)
                     - xg * (1 - 2 * cg) / (3 * Dg)) == 0,
            "crossing plain length at least 1/3")
    crossing_gates = {
        "D_lower": s.Rational(5, 2) - 2 * c,
        "r_min_minus_23_over_37": (18 * c - 4) / (37 * (5 - 4 * c)),
        "inverse_second_width_margin": s.Rational(9, 37),
        "plain_capacity_below_inverse_supply": s.Rational(7, 37) - c / 3,
        "plain_count_decreases_in_m": 2 - 2 * c,
        "positive_crossing_weights": 2 - 2 * c,
    }
    require(all(value > 0 for value in crossing_gates.values()), "generalized crossing geometry")

    # Generalized uncapped inverse/plain crossing, then short/long balance.
    A_count = 2 - 4 * c * x
    D_count = 3 - x - 4 * c * x
    P_count = A_count * (1 - x)
    J = (alpha - delta) * D_count + delta * P_count
    require(s.expand(D_count - P_count - (1 + x - 4 * c * x**2)) == 0,
            "P below D identity")
    R = 1 - delta + (alpha - delta) * delta * P_count / (2 * J)
    E = (
        -s.Rational(1, 4) + b / 6 + 5 * ell / 4
        + (s.Rational(1, 2) + ell) * delta + ell * x * delta
        - h * (1 - R)
    )
    Q = s.Poly(s.cancel(2 * J * (-E)), delta)
    require(Q.degree() == 2, "quadratic certificate degree")
    A, D, G = [s.expand(Q.nth(i)) for i in (2, 1, 0)]
    disc = s.Poly(s.expand(4 * A * G - D**2), v)
    require(all(coef > 0 for coef in s.Poly(A, v).all_coeffs()), "A coefficient positivity")
    require(all(coef > 0 for coef in disc.all_coeffs()), "discriminant coefficient positivity")
    require(s.expand(4 * A * Q.as_expr() - (2 * A * delta + D)**2 - disc.as_expr()) == 0,
            "complete-square identity")

    # On 0<=delta<=alpha, 0<=x<=1/2: P<=D<=3 and P>=1-c>0,
    # so alpha*(1-c)<=J<=5/2. On 0<=v<=1/2, A<=A(1/2).
    # Positive coefficients give disc>=disc(0), and the square is nonnegative.
    gap = s.factor(disc.nth(0) / (20 * A.subs(v, s.Rational(1, 2))))
    require(gap > s.Rational(1, 1000000000), "uniform endpoint margin exceeds 1e-9")

    # Conditional self-consistent limiting optimization, not a zero-free theorem.
    dc = s.symbols("dc", real=True)
    k_of_dc = (5 + 18 * dc) / (9 + 18 * dc)
    c_of_dc = 1 / (6 * k_of_dc)
    critical_D = s.Rational(5, 2) - 2 * c_of_dc
    critical_P = 1 - c_of_dc
    critical_J = (alpha - dc) * critical_D + dc * critical_P
    critical_R = 1 - dc + (alpha - dc) * dc * critical_P / (2 * critical_J)
    numerator = s.fraction(s.factor(critical_R - s.Rational(2, 3)))[0]
    require(s.Poly(numerator, dc) == s.Poly(-1188 * dc**3 + 2160 * dc**2 - 171 * dc - 190, dc),
            "limiting cubic elimination")

    result = {
        "status": "PASS_EXACT_KAPPA_SCALAR_CERTIFICATE",
        "scope": "exact scalar certificate with separately reviewed source-qualified written adapter",
        "imported_bound_independently_rebuilt": False,
        "fourth_moment_extension_verified": True,
        "fourth_moment_extension_verification_scope": "written proof adapter independently reviewed; imported analysis not rebuilt",
        "new_zero_free_theorem_claimed": False,
        "rh_proved": False,
        "parameters": {"kappa": str(kappa), "B": str(boundary), "ell": str(ell), "b": str(b)},
        "geometry_gates": {key: str(value) for key, value in gates.items()},
        "crossing_gates": {key: str(value) for key, value in crossing_gates.items()},
        "A_coefficients_ascending": [str(s.Poly(A, v).nth(i)) for i in range(s.degree(A, v) + 1)],
        "disc_coefficients_ascending": [str(disc.nth(i)) for i in range(disc.degree() + 1)],
        "uniform_minus_E_lower_bound": str(gap),
        "limiting_cubic": "1188*d^3-2160*d^2+171*d+190=0",
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(text, encoding="utf-8")
    elif len(sys.argv) > 2:
        raise SystemExit("usage: python3 check_kappa_candidate.py [OUTPUT_JSON]")
    print(text, end="")


if __name__ == "__main__":
    main()
