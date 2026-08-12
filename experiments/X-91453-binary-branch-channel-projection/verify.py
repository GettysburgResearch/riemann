#!/usr/bin/env python3
from __future__ import annotations

import json
import sympy as sp


def run() -> dict[str, object]:
    checks = 0
    r, X, Y, z = sp.symbols("r X Y z", positive=True)
    L = 2 * X - Y
    R = X - Y
    A = 1 - r**2
    B = 1 - r

    alpha_s = 2 * (r + 2) / (r + 3)
    alpha_h = 2 * (r + 1) / (r + 2)
    beta_h = (4 * r + 1) / (2 * r + 1)

    target_s = A * L + 2 * B * R
    score_s = A * (2 * L + R)
    target_h = r**2 * L + 2 * r * R
    score_h = 2 * r**2 * L + r * R

    assert sp.simplify(target_s - (1 - r) * (r + 3) * (alpha_s * X - Y)) == 0
    assert sp.simplify(score_s - 3 * A * (sp.Rational(5, 3) * X - Y)) == 0
    assert sp.simplify(target_h - r * (r + 2) * (alpha_h * X - Y)) == 0
    assert sp.simplify(score_h - r * (2 * r + 1) * (beta_h * X - Y)) == 0
    checks += 4

    assert sp.factor(alpha_s - sp.Rational(4, 3)) == 2 * r / (3 * (r + 3))
    assert sp.factor(sp.Rational(3, 2) - alpha_s) == (1 - r) / (2 * (r + 3))
    assert sp.factor(alpha_h - 1) == r / (r + 2)
    assert sp.factor(beta_h - alpha_h) == r / ((r + 2) * (2 * r + 1))
    assert sp.factor(sp.Rational(6, 5) - beta_h) == (1 - 2 * r) / (5 * (2 * r + 1))
    checks += 5

    q_s = ((2 * r + 4) * z - (r + 3)) / ((r + 1) * (5 * z - 3))
    q_h = ((2 * r + 2) * z - (r + 2)) / ((4 * r + 1) * z - (2 * r + 1))
    assert sp.factor(sp.diff(q_s, z)) == (3 - r) / ((r + 1) * (5 * z - 3) ** 2)
    assert sp.factor(sp.diff(q_h, z)) == 3 * r / ((4 * r + 1) * z - (2 * r + 1)) ** 2
    checks += 2

    # Verify exact target and score recombination in channel coordinates.
    parent_target = 4 * X - 3 * Y
    parent_score = 5 * X - 3 * Y
    d = r * (1 - r)
    assert sp.simplify(target_s + target_h - parent_target) == 0
    assert sp.simplify(score_s + score_h - parent_score - d * R) == 0
    checks += 2

    corridors: list[dict[str, str]] = []
    for p in (67, 71, 73, 101, 1009):
        rv = sp.sqrt(sp.Rational(1, p))
        vals = {
            "p": str(p),
            "alpha_s": str(sp.N(alpha_s.subs(r, rv), 30)),
            "alpha_h": str(sp.N(alpha_h.subs(r, rv), 30)),
            "beta_h": str(sp.N(beta_h.subs(r, rv), 30)),
        }
        assert sp.N(alpha_s.subs(r, rv), 50) > sp.Rational(4, 3)
        assert sp.N(alpha_s.subs(r, rv), 50) < sp.Rational(3, 2)
        assert sp.N(alpha_h.subs(r, rv), 50) > 1
        assert sp.N(beta_h.subs(r, rv), 50) > sp.N(alpha_h.subs(r, rv), 50)
        assert sp.N(beta_h.subs(r, rv), 50) < sp.Rational(6, 5)
        corridors.append(vals)
        checks += 5

    return {
        "verdict": "PASS_BINARY_BRANCH_CHANNEL_PROJECTION",
        "checks": checks,
        "parameter_samples": corridors,
        "survival_target_parameter": "2(r+2)/(r+3)",
        "survival_score_parameter": "5/3",
        "hazard_target_parameter": "2(r+1)/(r+2)",
        "hazard_score_parameter": "(4r+1)/(2r+1)",
        "scope": "exact finite algebra only; directed Hall inputs imported; all-generation type stability and RH are not proved",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
