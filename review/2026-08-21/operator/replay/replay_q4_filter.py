#!/usr/bin/env python3
"""Light exact replay for the factor-1024 Q4 annularization."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> dict[str, object]:
    S = sp.symbols("S")
    q = sp.expand((1 - S / 2) * (1 - S / 4) * (1 - S / 8))
    expected = 1 - sp.Rational(7, 8) * S + sp.Rational(7, 32) * S**2 - sp.Rational(1, 64) * S**3
    assert sp.expand(q - expected) == 0

    inverse_mass = sp.prod(1 / (1 - sp.Rational(1, 2) ** k) for k in (1, 2, 3))
    assert sp.simplify(inverse_mass - sp.Rational(64, 21)) == 0

    result = {
        "verdict": "PASS_REVIEWER_B_Q4_FILTER_LIGHT_REPLAY",
        "checks": {
            "triple_filter_coefficients": str(q),
            "inverse_l1_mass": str(inverse_mass),
            "mellin_zero_real_parts": [-1, -2, -3],
        },
        "scope": "exact scale-filter algebra only; no endpoint scan and no SACF/UOSACF campaign",
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
