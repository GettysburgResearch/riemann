#!/usr/bin/env python3
"""Exact rational verifier for the positive seed-excess band [1/40,1/32]."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import runpy


BASE = Path(__file__).resolve().parents[1] / "X-24501-outer-parabolic-seed" / "verify.py"
module = runpy.run_path(str(BASE), run_name="x24501_exact_interval_module")
Interval = module["Interval"]
sqrt_interval = module["sqrt_interval"]
log_interval = module["log_interval"]

CELL_MIN = 32
CELL_MAX = 40
MARGIN = Fraction(1, 10)
LIPSCHITZ = 253
FINITE_X_THRESHOLD = 101_201


def boundary_lower(cell: int) -> Fraction:
    harmonic = Interval.exact(0)
    logarithmic = Interval.exact(0)
    for k in range(1, cell + 1):
        inverse_sqrt = Interval.exact(1) / sqrt_interval(k)
        harmonic += inverse_sqrt
        logarithmic += log_interval(k) * inverse_sqrt
    boundary = (
        sqrt_interval(cell)
        * (logarithmic - (harmonic + 1) * log_interval(cell) + 4 * harmonic)
        - 4 * cell
    )
    return boundary.lo


def proof_object(cell_min: int = CELL_MIN, margin: Fraction = MARGIN) -> dict[str, object]:
    rows = []
    for cell in range(cell_min, CELL_MAX + 1):
        lower = boundary_lower(cell)
        rows.append(
            {
                "cell": cell,
                "lower_gt_margin": lower > margin,
                "lower_decimal": f"{float(lower):.15g}",
            }
        )
    return {
        "arithmetic": "EXACT_RATIONAL",
        "source_verifier": "../X-24501-outer-parabolic-seed/verify.py",
        "cells": rows,
        "margin": "1/10",
        "lipschitz_bound": LIPSCHITZ,
        "finite_X_threshold": FINITE_X_THRESHOLD,
        "lipschitz_integer_check": 40**3 < LIPSCHITZ**2,
        "remainder_threshold_check": 40 * LIPSCHITZ * 20 < 2 * FINITE_X_THRESHOLD,
        "all_cells_pass": all(bool(row["lower_gt_margin"]) for row in rows),
    }


def verify() -> dict[str, object]:
    result = proof_object()
    if not result["all_cells_pass"]:
        raise AssertionError("one reciprocal boundary failed the 1/10 margin")
    if not result["lipschitz_integer_check"]:
        raise AssertionError("253 does not dominate 40^(3/2)")
    if not result["remainder_threshold_check"]:
        raise AssertionError("finite-X threshold does not dominate the Taylor remainder")

    # Adversarial mutations.
    if proof_object(cell_min=30)["all_cells_pass"]:
        raise AssertionError("mutation failed: cell 30 does not satisfy the 1/10 margin")
    if proof_object(margin=Fraction(1, 5))["all_cells_pass"]:
        raise AssertionError("mutation failed: 1/5 is too strong at cell 32")

    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = sha256(canonical).hexdigest()
    result["verdict"] = "PASS_EXACT_POSITIVE_SEED_EXCESS_BAND"
    return result


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
