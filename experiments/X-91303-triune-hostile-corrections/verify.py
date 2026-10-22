#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sympy as sp


def run() -> dict[str, object]:
    checks = 0
    w = sp.symbols("w", positive=True)
    t = sp.symbols("t", positive=True)

    kappa_raw = 35 + (1 - 2**(-2*w)) * (-15 * 2**w + 2 * 2**(2*w))
    kappa_t = 2*t**2 - 15*t + 15/t + 33
    assert sp.simplify(kappa_raw.subs(2**w, t) - kappa_t) == 0
    checks += 1

    deriv = sp.diff(kappa_t, t)
    assert sp.simplify(deriv - (4*t - 15 - 15/t**2)) == 0
    checks += 1

    endpoint = sp.simplify(kappa_t.subs(t, sp.sqrt(2)))
    assert endpoint == 37 - sp.Rational(15, 2)*sp.sqrt(2)
    assert sp.N(endpoint - sp.Rational(103,4), 50) > 0
    checks += 2

    b = 1 - t**-2
    assert sp.simplify(35 + b*(-15*t + 2*t**2) - kappa_t) == 0
    checks += 1

    # Use D=A*v so logarithmic branch algebra is explicit.
    A, v, C = sp.symbols("A v C", positive=True)
    zp = (sp.log(A) + sp.log(1+v))/2 + C
    zm = (sp.log(A) + sp.log(1-v))/2 + C
    Delta = sp.simplify(zp-zm)
    S = sp.simplify(zp+zm)
    expected_delta = (sp.log(1+v)-sp.log(1-v))/2
    expected_S = sp.log(A) + (sp.log(1+v)+sp.log(1-v))/2 + 2*C
    assert sp.simplify(Delta-expected_delta) == 0
    assert sp.simplify(S-expected_S) == 0
    checks += 2

    assert sp.simplify(sp.exp(2*Delta) - (1+v)/(1-v)) == 0
    assert sp.simplify(sp.exp(2*S-4*C) - A**2*(1-v**2)) == 0
    checks += 2

    a = sp.symbols("a", positive=True)
    up = sp.exp(a*Delta)
    um = sp.exp(-a*Delta)
    ratio = sp.simplify((up-um)/(up+um))
    exp_ratio = sp.simplify((sp.exp(2*a*Delta)-1)/(sp.exp(2*a*Delta)+1))
    assert sp.simplify(ratio-exp_ratio) == 0
    checks += 1

    uplus = ((1+v)/(1-v))**(a/2)
    uminus = ((1+v)/(1-v))**(-a/2)
    for u in (uplus, uminus):
        ode = -sp.diff((1-v**2)*sp.diff(u,v),v) + a**2/(1-v**2)*u
        assert sp.simplify(ode) == 0
        checks += 1

    return {
        "verdict": "PASS_X_91303_TRIUNE_HOSTILE_CORRECTIONS",
        "checks": checks,
        "kappa_endpoint": str(endpoint),
        "strict_lower_bound": "103/4",
        "scope": "finite algebra only; no zeta evaluation and no proof of AOT_a or RH",
    }


def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument("--json", type=Path)
    args=p.parse_args()
    out=run()
    text=json.dumps(out, sort_keys=True, indent=2)+"\n"
    if args.json:
        args.json.write_text(text)
    print(text, end="")


if __name__=="__main__":
    main()
