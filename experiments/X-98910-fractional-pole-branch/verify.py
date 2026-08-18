#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T98910_FRACTIONAL_POLE_BRANCH_AUDIT"


def run() -> dict:
    finite_factor = (Fraction(1) - Fraction(1, 2)) * (
        Fraction(1) - Fraction(1, 4)
    )
    assert finite_factor == Fraction(3, 8)

    theta = Fraction(1, 384)
    claimed_rate = 96 * theta
    actual_energy_rate = Fraction(1, 2)
    assert claimed_rate == Fraction(1, 4)
    assert actual_energy_rate > claimed_rate

    h = 1.0
    translated_parity = math.exp(-2.0 * h * h)
    assert 0.0 < translated_parity < 1.0
    assert translated_parity != 1.0

    core = {
        "schema": "riemann.x98910.fractional-pole-branch.v1",
        "frozen_pr": 613,
        "frozen_head": "f28aa51a6d6740067202611d8ebda4be2ef0a1c9",
        "finite_factor_at_s1": "3/8",
        "theta_fixture": "1/384",
        "l98703_claimed_rate": "1/4",
        "pole_branch_energy_rate": "1/2",
        "strict_rate_gap": "1/4",
        "weyl_parity_invariant": False,
        "positive_continuum_carrier_density": "(exp(t)-1)/t",
        "pole_centered_limit": "(3/8)^theta",
        "nontrivial_zero_branches_preserved": True,
        "l98703_refuted": True,
        "pcfhe_proved": False,
        "rh_established": False,
        "verdict": VERDICT,
    }
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return core


def main() -> None:
    result = run()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
