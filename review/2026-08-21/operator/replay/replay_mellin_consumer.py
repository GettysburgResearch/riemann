#!/usr/bin/env python3
"""Light exact replay for the analytic Mellin--Landau consumer.

This script deliberately checks only finite algebraic identities.  It does not
attempt any zeta-zero computation or arithmetic producer estimate.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> dict[str, object]:
    a = sp.symbols("a")

    # PR #652, L-99602: P2=0 gives b=2a-1.  Substitute into 3P3.
    substituted_three_p3 = sp.expand(5 * (2 * a - 1) - a - 1 - 3 * a**2)
    expected = sp.expand(-3 * (a - 1) * (a - 2))
    assert sp.expand(substituted_three_p3 - expected) == 0

    # PR #653 / L-99603: no positive-half-plane zero can be introduced by
    # 1-67^{-(s+1/2)} because its second term has modulus <1 there.
    # The executable fixture checks representative exact real parts; the
    # general statement is the one-line modulus argument recorded in REPORT.md.
    real_parts = [sp.Rational(1, 100), sp.Rational(1, 2), sp.Rational(7, 3)]
    multiplier_moduli = [sp.Pow(67, -(sigma + sp.Rational(1, 2))) for sigma in real_parts]
    assert all(sp.simplify(value < 1) is sp.true for value in multiplier_moduli)

    # PR #653 logarithmic box smoothing multiplier: zeros of sinh(sH) lie on
    # Re(s)=0.  On positive real samples it is strictly positive.
    positive_samples = [sp.Rational(1, 10), sp.Rational(1, 1), sp.Rational(5, 2)]
    H = sp.Rational(7, 5)
    box_values = [sp.sinh(s * H) / (s * H) for s in positive_samples]
    assert all(value > 0 for value in box_values)

    result = {
        "verdict": "PASS_REVIEWER_B_MELLIN_CONSUMER_LIGHT_REPLAY",
        "checks": {
            "two_row_common_zero_elimination": str(expected),
            "factor_67_multiplier_positive_half_plane_modulus": True,
            "log_box_positive_real_samples": [str(v) for v in box_values],
        },
        "scope": "finite symbolic algebra only; no arithmetic producer and no zeta-zero campaign",
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
