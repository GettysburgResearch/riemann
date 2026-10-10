#!/usr/bin/env python3
"""Exact finite bookkeeping for the two spectral mean proofs.

This checks rational crossover/exponent calculations only. It does not
verify the imported large sieve, theta estimate, or analytic continuation.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def text_fraction(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def row_record(r: F, t: F, target: F) -> dict[str, str]:
    # H^r X^t = H^2 F/X determines the two crossover exponents.
    x_h = (2 - r) / (1 + t)
    x_f = 1 / (1 + t)
    threshold = (1 + t) / (2 * (2 - r))
    h_at_target = 1 - target * x_h
    f_at_target = F(1, 2) - target * x_f
    require(r + t * x_h == 2 - x_h, "H crossover mismatch")
    require(t * x_f == 1 - x_f, "F crossover mismatch")
    require(r / 2 + ((1 + t) / 2 - target) * x_h == h_at_target,
            "lower Mellin H exponent mismatch")
    require(((1 + t) / 2 - target) * x_f == f_at_target,
            "lower Mellin F exponent mismatch")
    require(h_at_target <= F(1, 2), "target row exponent fails")
    require(f_at_target <= (1 - target) / 2, "target auxiliary exponent fails")
    require(r / 2 <= F(1, 2), "lower-endpoint norm exceeds row envelope")
    return {
        "row_power": text_fraction(r),
        "column_power": text_fraction(t),
        "crossover_H": text_fraction(x_h),
        "crossover_F": text_fraction(x_f),
        "threshold": text_fraction(threshold),
        "H_norm_at_threshold": text_fraction(h_at_target),
        "F_norm_at_threshold": text_fraction(f_at_target),
    }


def build_result() -> dict:
    old_target = F(5, 8)
    new_target = F(4, 7)
    old = [row_record(F(1, 6), F(1), old_target),
           row_record(F(2, 3), F(2, 3), old_target)]
    new = [row_record(F(1, 6), F(1), new_target),
           row_record(F(5, 6), F(1, 3), new_target),
           row_record(F(1, 3), F(5, 6), new_target)]
    require(max(F(x["threshold"]) for x in old) == old_target,
            "old threshold not reconstructed")
    require(max(F(x["threshold"]) for x in new) == new_target,
            "new threshold not reconstructed")
    require(new_target < old_target, "no strict domain improvement")

    candidate_a = F(9, 16)
    require(candidate_a > max(F(6, 11), F(11, 20)),
            "negative control does not clear other thresholds")
    require(1 - F(7, 8) * candidate_a == F(65, 128) > F(1, 2),
            "incorrectly deleting the middle term was not detected")

    critical_x = F(7, 8)
    require(F(5, 6) + critical_x / 3 == 2 - critical_x == F(9, 8),
            "critical block does not balance")
    require(F(1, 6) + critical_x < F(9, 8),
            "sixth-power copy term dominates critical block")
    require(F(1, 3) + F(5, 6) * critical_x < F(9, 8),
            "other mixed term dominates critical block")

    old_scalar = (1 + old_target) / 2
    new_scalar = (1 + new_target) / 2
    tau = (3 * new_target - 1) / 2
    s = tau - new_target
    require(old_scalar == F(13, 16), "old scalar normalization mismatch")
    require(new_scalar == F(11, 14), "new scalar normalization mismatch")
    require(old_scalar - new_scalar == F(3, 112), "scalar saving mismatch")
    require(tau == F(5, 14) and s == F(-3, 14), "limiting contour mismatch")
    require(2 * new_target - tau == new_scalar, "balanced scalar mismatch")
    require(1 - new_target <= new_target, "physical comparison ranges leave a gap")

    return {
        "status": "pass",
        "arithmetic": "exact fractions; explicit exceptions, independent of Python optimization",
        "scope": "finite crossover identities and exponent comparisons only",
        "old_all_row_threshold": text_fraction(old_target),
        "new_all_row_threshold": text_fraction(new_target),
        "old_rows": old,
        "new_rows": new,
        "negative_control": {
            "omitted_middle_mixed_term": "rejected",
            "test_a": text_fraction(candidate_a),
            "actual_H_norm_exponent": "65/128",
        },
        "reflected_scalar": {
            "old": text_fraction(old_scalar),
            "new": text_fraction(new_scalar),
            "difference": "3/112",
            "limiting_tau": text_fraction(tau),
            "limiting_s": text_fraction(s),
            "endpoint_claimed": False,
            "physical_envelope_improved": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(build_result(), sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
