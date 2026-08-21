#!/usr/bin/env python3
"""Light exact replay for the reciprocal Loewner/Hankel packets."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> dict[str, object]:
    t, s1, s2, w1, w2 = sp.symbols("t s1 s2 w1 w2", nonzero=True)
    p = w1 / (t + s1) + w2 / (t + s2)
    lhs = sp.factor(p * sp.diff(p, t, 2) - 2 * sp.diff(p, t) ** 2)
    rhs = sp.factor(
        2 * w1 * w2 * (s1 - s2) ** 2 / ((t + s1) ** 3 * (t + s2) ** 3)
    )
    assert sp.factor(lhs - rhs) == 0

    lhs3 = sp.factor(2 * sp.diff(p, t) * sp.diff(p, t, 3) - 3 * sp.diff(p, t, 2) ** 2)
    rhs3 = sp.factor(
        12 * w1 * w2 * (s1 - s2) ** 2 / ((t + s1) ** 4 * (t + s2) ** 4)
    )
    assert sp.factor(lhs3 - rhs3) == 0

    # Beta-Hankel determinant at alpha=1/2 from PR #461.
    alpha = sp.Rational(1, 2)
    beta_determinants = {}
    for n in range(1, 7):
        c = lambda k: sp.rf(alpha, k) / sp.factorial(k)
        mat = sp.Matrix([[c(i + j + 1) for j in range(n)] for i in range(n)])
        det = sp.factor(mat.det())
        expected = sp.Rational(1, 2) ** (n * (2 * n - 1))
        assert sp.simplify(det - expected) == 0
        beta_determinants[str(n)] = str(det)

    result = {
        "verdict": "PASS_REVIEWER_B_LOEWNER_HANKEL_LIGHT_REPLAY",
        "checks": {
            "pairwise_reciprocal_curvature": True,
            "pairwise_schwarzian_curvature": True,
            "beta_hankel_determinants_alpha_half": beta_determinants,
        },
        "scope": "two-pole symbolic identities and fixed finite beta-Hankel orders only; no growing-order zero-frame theorem",
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
