#!/usr/bin/env python3
from __future__ import annotations

import json
import sympy as sp


def run() -> dict[str, object]:
    r, z = sp.symbols("r z", positive=True)
    A = 1 - r**2
    d = r * (1 - r)

    T0 = 4 * z - 3
    S0 = 5 * z - 3

    Ts = (1 - r) * (2 * (r + 2) * z - (r + 3))
    Th = r * ((2 * r + 2) * z - (r + 2))

    Ss_actual = A * (5 * z - 3)
    Sh_actual = r * ((4 * r + 1) * z - (2 * r + 1))

    Ss_native = A * (5 * z - 3)
    Sh_native = r**2 * (5 * z - 3)

    checks = 0

    assert sp.simplify(Ts + Th - T0) == 0
    assert sp.simplify(Ss_native + Sh_native - S0) == 0
    assert sp.simplify(A + r**2 - 1) == 0
    assert sp.simplify(Sh_actual - Sh_native - d * (z - 1)) == 0
    assert sp.simplify(Ss_actual - Ss_native) == 0
    checks += 5

    qs = sp.factor(Ts / Ss_native)
    qh = sp.factor(Th / Sh_native)

    qs_expected = (
        (2 * (r + 2) * z - (r + 3)) / ((1 + r) * (5 * z - 3))
    )
    qh_expected = (
        ((2 * r + 2) * z - (r + 2)) / (r * (5 * z - 3))
    )

    assert sp.simplify(qs - qs_expected) == 0
    assert sp.simplify(qh - qh_expected) == 0
    assert sp.simplify(
        sp.diff(qs, z) - (3 - r) / ((1 + r) * (5 * z - 3) ** 2)
    ) == 0
    assert sp.simplify(
        sp.diff(qh, z) - (4 - r) / (r * (5 * z - 3) ** 2)
    ) == 0
    assert sp.simplify(qs.subs(z, 1) - sp.Rational(1, 2)) == 0
    assert sp.simplify(qh.subs(z, 1) - sp.Rational(1, 2)) == 0
    checks += 6

    # Exact half-corridor factorizations.  Use algebraic equality rather than
    # structural expression equality so the replay is insensitive to SymPy's
    # chosen factor ordering.
    assert sp.simplify(
        2 * Ts - Ss_native - (1 - r) * (3 - r) * (z - 1)
    ) == 0
    assert sp.simplify(
        2 * Th - Sh_native - r * (4 - r) * (z - 1)
    ) == 0
    checks += 2

    # The fixed-67 score slopes match the physical row coefficients exactly.
    slope_s = sp.diff(Ss_native, z)
    slope_h = sp.diff(Sh_native, z)
    assert sp.simplify(slope_s - 5 * A) == 0
    assert sp.simplify(slope_h - 5 * r**2) == 0
    checks += 2

    # Verify target factorizations through the Hall parameters.
    alpha_s = 2 * (r + 2) / (r + 3)
    alpha_h = 2 * (r + 1) / (r + 2)
    assert sp.simplify(
        Ts - (1 - r) * (r + 3) * (alpha_s * z - 1)
    ) == 0
    assert sp.simplify(
        Th - r * (r + 2) * (alpha_h * z - 1)
    ) == 0
    checks += 2

    result = {
        "classification": "PASS_BINARY_NATIVE_ROW_SCORE_BUDGET",
        "checks": checks,
        "row_coefficients": {
            "survival": "1-r^2",
            "hazard": "r^2",
            "sum": "1",
        },
        "native_scores": {
            "survival": "(1-r^2)(5z-3)",
            "hazard": "r^2(5z-3)",
            "sum": "5z-3",
        },
        "discarded_favorable_score": "r(1-r)(z-1)",
        "target_per_native_score_derivatives": {
            "survival": "(3-r)/((1+r)(5z-3)^2)",
            "hazard": "(4-r)/(r(5z-3)^2)",
        },
        "scope": (
            "Exact symbolic one-prime target/score/row normalization only. "
            "Hall existence, directed component-row monotonicity, native "
            "J_Lambda boundary, finite collar assembly, and RH are not "
            "certified by this replay."
        ),
    }
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
