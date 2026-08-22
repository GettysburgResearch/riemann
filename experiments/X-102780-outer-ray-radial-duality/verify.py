#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def digest(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def pvalue(A: Fraction, B: Fraction, C: Fraction, t: Fraction) -> Fraction:
    return C + 2 * B * t + A * t * t


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    # Change-of-variables identity for exact feasible fixtures.
    primal_transform_checks = 0
    fixtures = [
        (Fraction(1), Fraction(1, 3), Fraction(2), Fraction(1), Fraction(1)),
        (Fraction(-2), Fraction(1), Fraction(5), Fraction(3), Fraction(2)),
        (Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
    ]
    for A, B, C, lam, eta in fixtures:
        x = A + lam
        y = C + eta - lam / 4
        assert x >= 0 and y >= 0 and x * y >= B * B
        old = Fraction(255, 64) * lam + Fraction(1, 16) * (C + eta)
        new = 4 * (x - A) + y / 16
        assert old == new
        primal_transform_checks += 1

    # Weak duality for exact rational primal/dual fixtures.
    dual_checks = 0
    duals = [
        (Fraction(4), Fraction(-1, 2), Fraction(1, 16)),
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(2), Fraction(1, 8), Fraction(1, 64)),
    ]
    for A, B, C, lam, eta in fixtures:
        primal = Fraction(255, 64) * lam + Fraction(1, 16) * (C + eta)
        for u, v, w in duals:
            assert 0 <= w <= Fraction(1, 16)
            assert 0 <= u <= Fraction(255, 64) + w / 4
            assert v * v <= u * w
            dual = -u * A - 2 * v * B + (Fraction(1, 16) - w) * C
            assert dual <= primal
            dual_checks += 1

    # The distinguished dual point is rank one and is exactly t=-8.
    u, v, w = Fraction(4), Fraction(-1, 2), Fraction(1, 16)
    assert u * w == v * v
    assert Fraction(2, 1) / Fraction(-1, 4) == -8

    # Outer-ray identity and three-ray interpolation on the basis 1,t,t^2.
    interpolation_checks = 0
    for A, B, C in [
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(7, 5), Fraction(-3, 4), Fraction(11, 6)),
    ]:
        pm = pvalue(A, B, C, Fraction(-1, 2))
        p0 = pvalue(A, B, C, Fraction(0))
        pp = pvalue(A, B, C, Fraction(1, 2))
        p8 = pvalue(A, B, C, Fraction(-8))
        assert p8 == 136 * pm + 120 * pp - 255 * p0
        assert (p8 - p0) / 16 == 4 * A - B
        interpolation_checks += 1

    # Sharp source-blind countermodel.
    A, B, C = Fraction(-4), Fraction(0), Fraction(1)
    assert pvalue(A, B, C, Fraction(0)) == 1
    assert pvalue(A, B, C, Fraction(1, 2)) == 0
    assert pvalue(A, B, C, Fraction(-1, 2)) == 0
    assert pvalue(A, B, C, Fraction(-8)) == -255
    target = 4 * A - B
    assert target == -16
    radial_cost = Fraction(255, 64) * 4 + Fraction(1, 16)
    assert radial_cost == 16 == -target

    payload = {
        "schema": "riemann.t102780.outer-ray-radial-duality.v1",
        "primal_transform_checks": primal_transform_checks,
        "weak_duality_checks": dual_checks,
        "interpolation_checks": interpolation_checks,
        "outer_ray": -8,
        "lagrange_coefficients": [136, 120, -255],
        "sharp_countermodel_target": -16,
        "radial_cost_sharp": True,
        "oer102780_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102780_OUTER_RAY_RADIAL_DUALITY",
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
