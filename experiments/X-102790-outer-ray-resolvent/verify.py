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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    # 5s(s-1/2)-s-3/2 = (s-1)(5s+3/2).
    polynomial_checks = 0
    for s in [Fraction(-3, 2), Fraction(-1, 3), Fraction(1, 4), Fraction(2), Fraction(7, 3)]:
        lhs = 5 * s * (s - Fraction(1, 2)) - s - Fraction(3, 2)
        rhs = (s - 1) * (5 * s + Fraction(3, 2))
        assert lhs == rhs
        polynomial_checks += 1

    # Stable inverse mass constant: (2/5)/(3/10)=4/3.
    resolvent_constant = Fraction(2, 5) / Fraction(3, 10)
    assert resolvent_constant == Fraction(4, 3)

    # Outer-ray and barycentric coordinates agree.
    interpolation_checks = 0
    for A, B, C in [
        (Fraction(1), Fraction(2), Fraction(3)),
        (Fraction(-4), Fraction(0), Fraction(1)),
        (Fraction(7, 5), Fraction(-3, 4), Fraction(11, 6)),
    ]:
        pm = C - B + A / 4
        p0 = C
        pp = C + B + A / 4
        p8 = C - 16 * B + 64 * A
        lorentz = 4 * A - B
        assert (p8 - p0) / 16 == lorentz
        assert Fraction(17, 2) * pm + Fraction(15, 2) * pp - 16 * p0 == lorentz
        interpolation_checks += 1

    # High-frequency converse fixture.
    N = 100
    samples = 20000
    y_neg = 0.0
    l_neg = 0.0
    length = 2 * math.pi
    for j in range(samples):
        u = length * (j + 0.5) / samples
        y = math.sin(N * u)
        ell = 2.5 * (N * math.cos(N * u) + 0.3 * math.sin(N * u))
        y_neg += max(-y, 0.0) * length / samples
        l_neg += max(-ell, 0.0) * length / samples
    assert y_neg < 3.0
    assert l_neg > 100 * y_neg

    payload = {
        "schema": "riemann.t102790.outer-ray-resolvent.v1",
        "polynomial_factor_checks": polynomial_checks,
        "interpolation_checks": interpolation_checks,
        "resolvent_negative_mass_constant": "4/3",
        "high_frequency_fixture_N": N,
        "high_frequency_negative_mass_ratio": l_neg / y_neg,
        "outer_to_critical_direction_positive": True,
        "critical_to_outer_converse_source_free": False,
        "oer102780_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102790_OUTER_RAY_RESOLVENT",
    }
    payload["proof_object_sha256"] = digest(payload)

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
