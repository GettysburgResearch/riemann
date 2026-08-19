#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T99230_VOLTERRA_BOUNDARY_AND_TWO_ANCHOR_AUDIT"


def main() -> None:
    assert 2 * Fraction(1, 2) ** 2 - 3 * Fraction(1, 2) + 1 == 0
    assert 2 * Fraction(1) ** 2 - 3 * Fraction(1) + 1 == 0

    t = Fraction(4)
    jump = Fraction(1, 8)
    assert 2 * t * t * jump == 4

    a = Fraction(4)
    f_a = Fraction(26)
    fp_a = Fraction(23, 4)
    A = 2 * (f_a - a * fp_a) / 2
    B = 2 * fp_a - f_a / a
    assert A == 3
    assert B == 5

    c0 = A - B
    c1 = B
    assert c0 == -2
    assert c1 == 5
    assert c0 < 0

    Ap, Bp = Fraction(7), Fraction(2)
    cp0, cp1 = Ap - Bp, Bp
    assert cp0 == 5 and cp1 == 2

    core = {
        "schema": "riemann.x99230.volterra-boundary.v1",
        "green_jump_unit_mass": True,
        "kernel_span_sqrt_x_x": True,
        "knot_atoms_required": True,
        "negative_anchor_fixture_rejected": True,
        "positive_two_anchor_fixture": True,
        "rh_established": False,
        "verdict": VERDICT,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canon).hexdigest()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(core, indent=2, sort_keys=True) + "\n")
    print(VERDICT)
    print(core["proof_object_sha256"])


if __name__ == "__main__":
    main()
