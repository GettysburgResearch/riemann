#!/usr/bin/env python3
"""Light exact replay for PRs #445--#446.

Checks the three-node determinant factorization, reciprocal-concavity assembly,
and the one-orbit reserve algebra.  The external verified-zero-height theorem is
not rerun.
"""
from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path

import sympy as sp


def dd2(values, nodes):
    return sum(
        values[i] / sp.prod(nodes[i] - nodes[j] for j in range(3) if j != i)
        for i in range(3)
    )


def main() -> dict[str, object]:
    x1, x2, x3 = sp.symbols("x1 x2 x3", nonzero=True)
    p1, p2, p3 = sp.symbols("p1 p2 p3", nonzero=True)
    xs = [x1, x2, x3]
    ps = [p1, p2, p3]
    ts = [x**2 for x in xs]

    H = sp.Matrix(
        [
            [(xs[i] * ps[i] + xs[j] * ps[j]) / (xs[i] + xs[j]) for j in range(3)]
            for i in range(3)
        ]
    )
    delta = sp.prod(ts[j] - ts[i] for i in range(3) for j in range(i + 1, 3))
    denominator = sp.prod((xs[i] + xs[j]) ** 2 for i in range(3) for j in range(i + 1, 3))
    rhs = (
        p1
        * p2
        * p3
        * delta**2
        / denominator
        * dd2([1 / p for p in ps], ts)
        * dd2([ts[i] * ps[i] for i in range(3)], ts)
    )
    assert sp.factor(H.det() - rhs) == 0

    # Reciprocal-concavity closure lower-bound identity.
    f, g, fp, gp = sp.symbols("f g fp gp", positive=True)
    lower_cross = 2 * g * fp**2 / f + 2 * f * gp**2 / g - 4 * fp * gp
    square_form = 2 * (g * fp - f * gp) ** 2 / (f * g)
    assert sp.factor(lower_cross - square_form) == 0

    # One off-line orbit paired with one critical reserve orbit.
    t, c, B, m, r = sp.symbols("t c B m r", positive=True)
    U = t + c
    d = c - r
    s = d / U
    kappa = B**2 / d**2
    q = 4 * m * U / (U**2 + B**2)
    R = 2 / (t + r)

    def E(expr):
        return sp.simplify(expr * sp.diff(expr, t, 2) - 2 * sp.diff(expr, t) ** 2)

    Eq = sp.factor(E(q))
    ER = sp.factor(E(R))
    assert sp.factor(Eq + 32 * m**2 * B**2 / (U**2 + B**2) ** 3) == 0
    assert ER == 0

    cross = sp.factor(q * sp.diff(R, t, 2) + R * sp.diff(q, t, 2) - 4 * sp.diff(q, t) * sp.diff(R, t))
    Q = 1 - kappa + 3 * kappa * s * (2 - s) + kappa**2 * s**2 * (3 - 2 * s)
    cross_expected = 16 * m * s**2 * Q / (U**4 * (1 + kappa * s**2) ** 3 * (1 - s) ** 3)
    assert sp.factor(cross - cross_expected) == 0

    getcontext().prec = 60
    Hstar = Decimal("3000175332800")
    budget = Decimal(18) * (Hstar.ln() + Decimal(1)) / Hstar
    assert budget < Decimal("1.8e-10")

    result = {
        "verdict": "PASS_REVIEWER_B_XI_PICK_ORDER3_LIGHT_REPLAY",
        "checks": {
            "three_node_determinant_factorization": True,
            "reciprocal_concavity_sum_closure": True,
            "off_line_orbit_curvature": str(Eq),
            "critical_orbit_curvature": str(ER),
            "cross_curvature_factorization": True,
            "global_declared_budget_upper_bound": str(budget),
        },
        "scope": "exact finite algebra and printed budget only; external zero verification and infinite Hadamard passage not rerun",
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
