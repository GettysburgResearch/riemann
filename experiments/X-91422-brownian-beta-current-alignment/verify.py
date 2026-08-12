#!/usr/bin/env python3
from __future__ import annotations
import json
import sympy as sp


def run():
    checks = 0

    tau1, tau2, t, ds, dd = sp.symbols("tau1 tau2 t ds dd", real=True)
    lhs = (tau1+tau2)*ds + (tau1-tau2)*dd
    beta = (tau1-tau2)*(dd-t*ds) + (
        tau1+tau2+(tau1-tau2)*t
    )*ds
    assert sp.expand(lhs-beta) == 0
    checks += 1

    c = tau1+tau2+(tau1-tau2)*t
    cpos = (1+t)*tau1+(1-t)*tau2
    assert sp.expand(c-cpos) == 0
    checks += 1

    z1, z2, x = sp.symbols("z1 z2 x", real=True)
    S = z1+z2
    Delta = z1-z2
    F = lambda y: sp.exp(y)-2*sp.exp(2*y)
    A = sp.integrate(F(x+Delta/2)*F(x-Delta/2), (x, -S/2, S/2))
    dplus = sp.simplify(sp.diff(A, z1)+sp.diff(A, z2))
    endpoint = sp.simplify(F(z1)*F(z2)+F(-z2)*F(-z1))
    assert sp.simplify(dplus-endpoint) == 0
    checks += 1

    AS, AD, th = sp.symbols("AS AD th")
    dminus = 2*AD
    dbeta = AD-th*AS
    assert sp.expand(dminus-(2*dbeta+th*(2*AS))) == 0
    checks += 1

    minimum = None
    for a in (sp.Rational(1,10), sp.Rational(1,2), sp.Rational(3,2), sp.Rational(5)):
        for b in (sp.Rational(1,8), sp.Rational(2), sp.Rational(7)):
            for q in (sp.Rational(-9,10), sp.Rational(0), sp.Rational(9,10)):
                value = (1+q)*a+(1-q)*b
                assert value >= 0
                fv = float(value)
                minimum = fv if minimum is None else min(minimum, fv)
                checks += 1

    return {
        "verdict": "PASS_X_91422_BROWNIAN_BETA_CURRENT_ALIGNMENT",
        "checks": checks,
        "minimum_positive_boundary_weight": minimum,
        "scope": "exact algebra only; the tilted Green domination and RH are not proved",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
