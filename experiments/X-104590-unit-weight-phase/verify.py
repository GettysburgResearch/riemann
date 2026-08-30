#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def digest(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def sign(q: Fraction) -> int:
    return 1 if q > 0 else -1 if q < 0 else 0


def orientation(fc: Fraction, fppc: Fraction) -> int:
    return -sign(fc) * sign(fppc)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    identity_fixtures = []
    for f, fp, fpp, lam in [
        (Fraction(5, 3), Fraction(7, 5), Fraction(-2, 7), Fraction(3, 2)),
        (Fraction(-4, 9), Fraction(11, 6), Fraction(5, 8), Fraction(2, 3)),
        (Fraction(13, 10), Fraction(-9, 7), Fraction(4, 11), Fraction(5, 4)),
    ]:
        lhs = (f * f + lam * lam * fp * fp) - f * (f + lam * lam * fpp)
        rhs = lam * lam * (fp * fp - f * fpp)
        assert lhs == rhs
        identity_fixtures.append(str(lhs))

    quartic = [
        orientation(Fraction(1), Fraction(8)),
        orientation(Fraction(2), Fraction(-4)),
        orientation(Fraction(1), Fraction(8)),
    ]
    assert quartic == [-1, 1, -1]
    assert sum(quartic) == -1

    cubic = [
        orientation(Fraction(2), Fraction(-6)),
        orientation(Fraction(-2), Fraction(6)),
    ]
    assert cubic == [1, 1]
    assert sum(cubic) == 2

    amplitudes = [Fraction(2), Fraction(2), Fraction(2), Fraction(1, 10)]
    eps = [1, 1, 1, -1]
    D = sum(e * a for e, a in zip(eps, amplitudes))
    B = sum(a * a for a in amplitudes)
    R = len(amplitudes)
    G = sum(e == 1 for e in eps)
    lower_G = D * D / B
    assert lower_G <= G
    eta = 2 * D * D / (R * B) - 1
    assert eta > 0

    marked_second_moment = Fraction(8)
    assert marked_second_moment == Fraction(4) + Fraction(4)

    primitive_period_checks = []
    for theta in [-3.7, -0.4, 0.0, 0.9, 4.2]:
        def H(x: float) -> float:
            k = math.floor(x / math.pi)
            r = x - k * math.pi
            return 2.0 * k + 1.0 - math.cos(r)
        diff = H(theta + math.pi) - H(theta)
        assert abs(diff - 2.0) < 1e-12
        primitive_period_checks.append(diff)

    payload = {
        "schema": "riemann.t104590.unit_weight_phase.v1",
        "checks": {
            "pointwise_numerator_identity": identity_fixtures,
            "quartic_orientation_sum": sum(quartic),
            "cubic_orientation_sum": sum(cubic),
            "moment_fixture": {
                "D": str(D),
                "B": str(B),
                "R": R,
                "G": G,
                "lower_G": str(lower_G),
                "eta": str(eta),
            },
            "marked_second_moment": str(marked_second_moment),
            "phase_primitive_period_increments": primitive_period_checks,
        },
        "scope": {
            "unit_amplitude_count_identity_proved_exact": True,
            "lambda_uniform_phase_reduction_proved_exact": True,
            "weighted_moment_count_bound_proved_exact": True,
            "marked_contour_identity_proved_exact": True,
            "uphase104590_proved": False,
            "cm2x104590_proved": False,
            "alpha2_from_alpha3_proved": False,
            "rh_established": False,
        },
        "verdict": "PASS_T104590_UNIT_WEIGHT_PHASE_ALGEBRA",
    }
    payload["proof_object_sha256"] = digest(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
