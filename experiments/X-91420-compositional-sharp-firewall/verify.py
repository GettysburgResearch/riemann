#!/usr/bin/env python3
from __future__ import annotations
import json
import sympy as sp


def run():
    r, s, A, B = sp.symbols("r s A B", positive=True)
    w = sp.Matrix([[1, 2]])

    def M(x):
        return sp.Matrix([
            [1 + x - 2*x**2, -2*x*(1-x)],
            [x*(1-x), (1-x)**2],
        ])

    def N(x):
        return sp.Matrix([
            [1 + x - 2*x**2, 0],
            [x*(1-x), (1-x)*(1-2*x)],
        ])

    checks = 0
    assert sp.simplify(w*N(r)-w*M(r)) == sp.zeros(1, 2)
    checks += 1

    defect = (w*N(s)*N(r)-w*M(s)*M(r)).applyfunc(sp.factor)
    expected = sp.Matrix([[0, 12*r*s*(1-r)*(1-s)]])
    assert sp.simplify(defect-expected) == sp.zeros(1, 2)
    checks += 1

    MAB = sp.Matrix([[2*A-B, -2*(A-B)], [A-B, 2*B-A]])
    NAB = sp.Matrix([[2*A-B, 0], [A-B, 3*B-2*A]])
    assert sp.simplify(w*NAB-w*MAB) == sp.zeros(1, 2)
    checks += 1

    J4 = sp.Matrix([[2, -2, -1, 1], [1, -1, -1, 1]])
    D4 = sp.diag(A, A, B, B)
    assert sp.simplify(J4*D4-MAB*J4) == sp.zeros(2, 4)
    checks += 1

    samples = []
    for p in (67, 71, 73, 101):
        for q in (67, 71, 97):
            rp = sp.sqrt(sp.Rational(1, p))
            rq = sp.sqrt(sp.Rational(1, q))
            val = sp.N(12*rp*rq*(1-rp)*(1-rq), 30)
            assert val > 0
            samples.append(float(val))
            checks += 1

    return {
        "verdict": "PASS_X_91420_COMPOSITIONAL_SHARP_FIREWALL",
        "checks": checks,
        "two_factor_defect": ["0", "12*r*s*(1-r)*(1-s)"],
        "minimum_sample_defect": min(samples),
        "scope": "exact finite algebra only; FSRP_X and RH are not proved",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
