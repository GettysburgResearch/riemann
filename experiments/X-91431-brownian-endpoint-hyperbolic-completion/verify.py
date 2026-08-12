#!/usr/bin/env python3
from __future__ import annotations

import json
import sympy as sp


def run() -> dict[str, object]:
    checks = 0

    B = sp.Matrix([[0, sp.Rational(1, 2)], [sp.Rational(1, 2), 0]])
    M = sp.diag(B, B)
    eigenvalues = sorted([sp.simplify(v) for v in M.eigenvals().keys()], key=lambda x: float(x))
    assert M.eigenvals()[sp.Rational(-1, 2)] == 2
    assert M.eigenvals()[sp.Rational(1, 2)] == 2
    checks += 2

    ar, ai, br, bi, cr, ci, dr, di = sp.symbols(
        "ar ai br bi cr ci dr di", real=True
    )
    H = ar * br + ai * bi + cr * dr + ci * di
    diag = sp.Rational(1, 2) * (
        ar**2 + ai**2 + br**2 + bi**2 + cr**2 + ci**2 + dr**2 + di**2
    )
    squares = sp.Rational(1, 2) * (
        (ar + br) ** 2 + (ai + bi) ** 2 + (cr + dr) ** 2 + (ci + di) ** 2
    )
    assert sp.expand(H + diag - squares) == 0
    checks += 1

    subs = {br: -ar, bi: -ai, dr: -cr, di: -ci}
    assert sp.expand((H + diag).subs(subs)) == 0
    checks += 1

    xi, dz = sp.symbols("xi dz", real=True, nonzero=True)
    endpoint_exp = 2 * sp.cos(xi * dz)
    assert sp.simplify(endpoint_exp.subs(xi, sp.pi / dz) + 2) == 0
    checks += 1

    eta, W, u, v = sp.symbols("eta W u v", positive=True, real=True)
    plus_square = (sp.sqrt(eta * W) * v + u / sp.sqrt(eta * W)) ** 2
    minus_square = (sp.sqrt(eta * W) * v - u / sp.sqrt(eta * W)) ** 2
    assert sp.simplify(eta * W * v**2 + u**2 / (eta * W) + 2 * u * v - plus_square) == 0
    assert sp.simplify(eta * W * v**2 + u**2 / (eta * W) - 2 * u * v - minus_square) == 0
    checks += 2

    tau1, tau2, t = sp.symbols("tau1 tau2 t", nonnegative=True, real=True)
    c = (1 + t) * tau1 + (1 - t) * tau2
    for tv in (sp.Rational(-1), sp.Rational(-9, 10), 0, sp.Rational(9, 10), 1):
        cv = sp.expand(c.subs(t, tv))
        assert all(coef >= 0 for coef in (cv.coeff(tau1), cv.coeff(tau2)))
        checks += 1

    return {
        "verdict": "PASS_BROWNIAN_ENDPOINT_HYPERBOLIC_COMPLETION",
        "checks": checks,
        "endpoint_matrix_eigenvalues": [str(v) for v in eigenvalues],
        "signature": [2, 2],
        "sharp_diagonal_coefficient": "1/2 before the outer factor, 1/4 in L-91422.9",
        "negative_exponential_witness": "2*cos(xi*(z2-z1))=-2 at xi=pi/(z2-z1)",
        "scope": "exact finite algebra only; theta reserve domination and RH are not proved",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
