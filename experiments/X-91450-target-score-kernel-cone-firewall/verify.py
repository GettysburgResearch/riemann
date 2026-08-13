#!/usr/bin/env python3
from __future__ import annotations

import json
import sympy as sp


def run() -> dict[str, object]:
    checks = 0
    x, n = sp.symbols("x n", positive=True)
    WT = 4 * sp.sqrt(x) / n - 3 / sp.sqrt(n)
    WS = 5 * sp.sqrt(x) / n - 3 / sp.sqrt(n)
    assert sp.simplify(4 * WS - 5 * WT - 3 / sp.sqrt(n)) == 0
    checks += 1

    A = 1 - 1 / sp.sqrt(2) - 1 / sp.sqrt(3) - 1 / sp.sqrt(5)
    B = 1 - sp.Rational(1, 2) - sp.Rational(1, 3) - sp.Rational(1, 5)
    assert B == -sp.Rational(1, 30)
    T = 4 * sp.sqrt(5) * B - 3 * A
    S = 5 * sp.sqrt(5) * B - 3 * A
    assert sp.simplify(4 * S - 5 * T - 3 * A) == 0
    assert sp.N(A, 60) < 0
    assert sp.N(T, 60) > 0
    assert sp.N(S, 60) > 0
    assert sp.N(S / T, 60) < sp.Rational(5, 4)
    checks += 6

    L, R = sp.symbols("L R", nonnegative=True)
    TT = L + 2 * R
    SS = 2 * L + R
    Linv = sp.simplify((2 * SS - TT) / 3)
    Rinv = sp.simplify((2 * TT - SS) / 3)
    assert Linv == L and Rinv == R
    assert sp.simplify(2 * SS - TT - 3 * L) == 0
    assert sp.simplify(2 * TT - SS - 3 * R) == 0
    checks += 4

    r = sp.symbols("r", positive=True)
    H = sp.symbols("H", nonnegative=True)
    J = sp.symbols("J", nonnegative=True)
    for a in (1, 2):
        parent = a * H - J
        child = a * r * H - J
        slack = a * (1 - r) * H
        assert sp.expand(parent - child - slack) == 0
        checks += 1

    return {
        "verdict": "PASS_TARGET_SCORE_KERNEL_CONE_FIREWALL",
        "checks": checks,
        "x5": {
            "A": str(A),
            "B": str(B),
            "target": str(T),
            "score": str(S),
            "score_over_target": str(sp.N(S / T, 30)),
            "four_score_minus_five_target": str(sp.simplify(4 * S - 5 * T)),
        },
        "common_positive_kernel_constraint": "4*S-5*T=3*sum_n nu(n)/sqrt(n)>=0",
        "physical_two_ray_cone": "T/2 <= S <= 2*T",
        "scope": "exact algebra and an exact radical witness; physical row/capacity splice and RH are not proved",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
