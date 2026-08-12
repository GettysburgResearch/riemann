#!/usr/bin/env python3
from __future__ import annotations
import json
import mpmath as mp
import sympy as sp


def run():
    mp.mp.dps = 70
    x = sp.symbols("x", positive=True)
    R = (
        -sp.Rational(1,4)*(1+x)*sp.exp(-x)
        +sp.Rational(17,32)*(1+2*x)*sp.exp(-2*x)
        -sp.Rational(1,16)*(1+4*x)*sp.exp(-4*x)
    )
    checks = 0
    expected = x*sp.exp(-4*x)*(2*sp.exp(3*x)-17*sp.exp(2*x)+8)/8
    assert sp.simplify(sp.diff(R,x)-expected) == 0
    checks += 1
    assert sp.integrate(R,(x,0,sp.oo)) == 0
    checks += 1
    assert sp.simplify(R.subs(x,0)-sp.Rational(7,32)) == 0
    checks += 1

    def Rf(z):
        return (
            -mp.mpf(1)/4*(1+z)*mp.e**(-z)
            +mp.mpf(17)/32*(1+2*z)*mp.e**(-2*z)
            -mp.mpf(1)/16*(1+4*z)*mp.e**(-4*z)
        )

    tau = mp.findroot(Rf,(1,1.5))
    varpi = mp.findroot(lambda y:y**3-y-1,1.3)
    kappa = mp.log(varpi)
    astar = tau/kappa
    assert 1 < tau < 2 and astar > 1
    checks += 1

    def B(u):
        return 1/(1-mp.e**(-2*u))-(1+mp.e**u)

    max_bad = mp.mpf("0")
    for j in range(1,4001):
        u = mp.mpf(j)/400
        prod = Rf(astar*u)*B(u)
        max_bad = max(max_bad,-prod)
        assert prod >= -mp.mpf("1e-55")
        checks += 1

    assert mp.log(2) > kappa
    assert Rf(astar*mp.log(2)) < 0
    checks += 2

    return {
        "verdict": "PASS_X_91423_ROOT_LOCKED_QUASI_LEVY",
        "checks": checks,
        "tau_star": mp.nstr(tau,40),
        "kappa": mp.nstr(kappa,40),
        "a_star": mp.nstr(astar,40),
        "maximum_sign_violation": mp.nstr(max_bad,10),
        "scope": "exact symbolic identities and high-precision sign diagnostics; operator domination and RH are not proved",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
