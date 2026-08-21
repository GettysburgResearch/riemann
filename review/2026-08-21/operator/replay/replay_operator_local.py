#!/usr/bin/env python3
"""Light exact replay for selected local operator identities."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


def main() -> dict[str, object]:
    # Brownian-theta / Pick Cayley anticommutator, checked on a generic 2x2 packet.
    c11, c12, c22, d1, d2 = sp.symbols("c11 c12 c22 d1 d2")
    C = sp.Matrix([[c11, c12], [c12, c22]])
    D = sp.diag(d1, d2)
    L = sp.diag((1 - d1) / (1 + d1), (1 - d2) / (1 + d2))
    I = sp.eye(2)
    lhs = C - D * C * D
    rhs = 2 * (I + L).inv() * (L * C + C * L) * (I + L).inv()
    assert all(sp.factor(x) == 0 for x in (lhs - rhs))

    # PR #408 exact prime-Julia absorption margin and Jacobi spectral gap.
    margin = Fraction(1, 1) - Fraction(85, 196) ** 2 - Fraction(1, 4)
    assert margin == Fraction(21587, 38416)
    jacobi_gap = Fraction(1, 1) * Fraction(9, 2) / 4
    assert jacobi_gap == Fraction(9, 8)

    result = {
        "verdict": "PASS_REVIEWER_B_OPERATOR_LOCAL_LIGHT_REPLAY",
        "checks": {
            "cayley_anticommutator": True,
            "prime_julia_absorption_margin": str(margin),
            "jacobi_one_cell_gap": str(jacobi_gap),
        },
        "scope": "selected exact local identities only; no source-to-output domination theorem",
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
