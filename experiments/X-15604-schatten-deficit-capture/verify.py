#!/usr/bin/env python3
"""Exact Fraction-only regression for L-15615.

The example is designed so that the ordinary r=1 trace certificate fails
because of one hundred shallow deficit modes, while the r=2 Schatten
certificate passes and recovers the exact complement floor.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F


def fj(x: F) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def main() -> int:
    G = F(2)
    Gamma = F(3, 2)
    alpha = F(9, 10)
    t = F(1)
    packet_dimension = 2

    # D has two genuinely dangerous modes and one hundred harmless shallow modes.
    deficit = [F(11, 10), F(11, 10)] + [F(1, 100)] * 100
    operator = [G - value for value in deficit]  # A = G I - D exactly.

    assert max(operator[:packet_dimension]) < t < Gamma
    assert min(operator[packet_dimension:]) >= Gamma

    kappa = G - alpha

    trace_1 = sum(deficit, F(0))
    capture_1 = packet_dimension * kappa
    remainder_1 = trace_1 - capture_1
    assert remainder_1 > G - Gamma

    trace_2 = sum((value * value for value in deficit), F(0))
    capture_2 = packet_dimension * kappa * kappa
    remainder_2 = trace_2 - capture_2
    assert remainder_2 <= (G - Gamma) ** 2

    # The theorem gives ||Q D Q|| <= sqrt(1/100)=1/10 and hence
    # A|_(L^perp) >= 2-1/10=19/10, stronger than Gamma=3/2.
    norm_upper = F(1, 10)
    certified_floor = G - norm_upper
    assert certified_floor >= Gamma
    assert certified_floor <= min(operator[packet_dimension:])

    result = {
        "schema": "riemann.x15604-schatten-deficit-capture.v1",
        "G": fj(G),
        "Gamma": fj(Gamma),
        "alpha": fj(alpha),
        "t": fj(t),
        "packet_dimension": packet_dimension,
        "deficit_spectrum": [
            {"value": fj(F(11, 10)), "multiplicity": 2},
            {"value": fj(F(1, 100)), "multiplicity": 100},
        ],
        "r1": {
            "trace": fj(trace_1),
            "forced_capture": fj(capture_1),
            "uncaptured_upper": fj(remainder_1),
            "required_upper": fj(G - Gamma),
            "passes": False,
            "classification": "R1_TRACE_CERTIFICATE_FAILS_ON_SHALLOW_MASS",
        },
        "r2": {
            "trace": fj(trace_2),
            "forced_capture": fj(capture_2),
            "uncaptured_moment_upper": fj(remainder_2),
            "required_upper": fj((G - Gamma) ** 2),
            "norm_upper": fj(norm_upper),
            "certified_complement_floor": fj(certified_floor),
            "passes": True,
            "classification": "R2_SCHATTEN_CERTIFICATE_PASSES",
        },
        "actual_operator": {
            "low_eigenvalue": fj(operator[0]),
            "complement_eigenvalue": fj(operator[-1]),
            "count_below_t": sum(value < t for value in operator),
            "count_below_Gamma": sum(value < Gamma for value in operator),
        },
        "verdict": "PASS_EXACT_R2_CAPTURE_WHILE_R1_TRACE_FAILS",
    }

    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["proof_object_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
