#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, sys
from fractions import Fraction
from pathlib import Path


def F(x: object) -> Fraction:
    if isinstance(x, bool):
        raise TypeError("boolean is not a number")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, str):
        return Fraction(x)
    raise TypeError(type(x))


def fourier_tail(q: int, *, P: int = 8, J: int = 10, K: int = 4096) -> Fraction:
    if not (0 <= q and 2 * J > q + 1):
        raise ValueError("invalid tail parameters")
    # Safe upper bound: use pi > 3 because q-2J is negative.
    return (
        Fraction(2, P)
        * 2 ** (J * (J + 3))
        * Fraction(6, P) ** (q - 2 * J)
        * Fraction(K) ** (q + 1 - 2 * J)
        / Fraction(2 * J - q - 1)
    )


def main(path: str) -> int:
    data = json.loads(Path(path).read_text())
    if data["schema"] != "riemann.x17801-five-notch-fourier-enclosure.v1":
        raise ValueError("schema")
    if data["classification"] != "DIRECTED_ENGINEERING_PROTOTYPE":
        raise ValueError("classification")
    if data["translation"] != {"numerator": "8578244975439", "denominator": "549755813888"}:
        raise ValueError("translation")
    if len(data["design_zero_ordinates"]) != 5:
        raise ValueError("notch count")
    runs = sorted(data["runs"], key=lambda x: x["grid_power"])
    if [r["grid_power"] for r in runs] != [18, 20]:
        raise ValueError("grid ladder")
    intervals = []
    for r in runs:
        if r["prime_power_terms"] != 64542:
            raise ValueError("term count")
        lo, c, hi = map(F, (r["prime_lower"], r["prime_center"], r["prime_upper"]))
        if not lo <= c <= hi:
            raise ValueError("interval order")
        intervals.append((lo, c, hi))
    if not (intervals[0][0] <= intervals[1][0] <= intervals[1][2] <= intervals[0][2]):
        raise ValueError("precision nesting")
    old = F(data["old_linear_midpoint"])
    if intervals[0][0] <= old <= intervals[0][2]:
        raise ValueError("old midpoint unexpectedly retained")
    model = F(data["ordinary_zero_plus_trivial_model"])
    if not intervals[1][0] <= model <= intervals[1][2]:
        raise ValueError("planning model no longer overlaps")
    t0 = fourier_tail(0)
    t4 = fourier_tail(4)
    if not t0 < F(data["value_tail_upper"]):
        raise ValueError("value tail")
    if not t4 < F(data["fourth_derivative_tail_upper"]):
        raise ValueError("fourth derivative tail")
    fine_radius = (intervals[1][2] - intervals[1][0]) / 2
    fine_center = (intervals[1][2] + intervals[1][0]) / 2
    separation_radii = (old - fine_center) / fine_radius
    result = {
        "schema": "riemann.x17801-five-notch-fourier-verification.v1",
        "verdict": "OLD_LINEAR_INTERPOLATION_SIGNAL_REFUTED",
        "rh_verdict": "NO_RH_BOUND_VIOLATION_CERTIFIED",
        "fine_interval": {
            "lower": str(intervals[1][0]),
            "upper": str(intervals[1][2]),
        },
        "old_midpoint_separation_radii_lower": str(separation_radii),
        "safe_value_tail": str(t0),
        "safe_fourth_derivative_tail": str(t4),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["exact_proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
