#!/usr/bin/env python3
"""Exact finite separators for the fractional-heat correction line."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def det2(a, b, c, d):
    return a * d - b * c


def main() -> dict[str, object]:
    # PR #619, L-98901: phase-zero Tao diagonal fails for the phase-locked port.
    diagonal = Fraction(8, 9)
    off_diagonal = Fraction(4, 3)
    separator = det2(diagonal, off_diagonal, off_diagonal, diagonal)
    assert separator == Fraction(-80, 81)

    theta = Fraction(1, 384)
    claimed_rate = 96 * theta
    true_uniform_energy_type = Fraction(1, 2)
    assert claimed_rate == Fraction(1, 4)
    assert claimed_rate < true_uniform_energy_type

    result = {
        "verdict": "PASS_REVIEWER_B_FRACTIONAL_HEAT_FIREWALL_LIGHT_REPLAY",
        "checks": {
            "tao_phase_separator_determinant": str(separator),
            "claimed_rate_at_theta_1_over_384": str(claimed_rate),
            "uniform_center_energy_type": str(true_uniform_energy_type),
        },
        "scope": "finite exact separators only; no Selberg--Delange or vertical-limit campaign rerun",
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
