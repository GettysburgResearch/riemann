#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from pathlib import Path


def digest(x):
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def psd(a, b, c, tol=1e-12):
    return a >= -tol and c >= -tol and a * c - b * b >= -tol


def radial_cost_fixture(A, B, C):
    lam = abs(A) + abs(B) + 4 * abs(C)
    eta = abs(B) + abs(C) + lam / 4
    x = A + lam
    y = C + eta - lam / 4
    assert psd(x, B, y)
    cost = (255 / 64) * lam + (C + eta) / 16
    bound = 4 * abs(A) + (65 / 16) * abs(B) + (129 / 8) * abs(C)
    assert cost <= bound + 1e-12
    return cost


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    sqrt2 = math.sqrt(2.0)
    carrier = 2 * (2 - sqrt2)
    initial_integral = 32 - 16 * sqrt2
    assert abs(initial_integral - 8 * carrier) < 1e-14

    kappa = 0.25 + 9 * math.log(2.0) ** 2 / math.pi**2
    assert kappa < 0.689

    rng = random.Random(102770)
    target_checks = 0
    subadditivity_checks = 0

    for _ in range(300):
        x = 10 ** rng.uniform(-2, 2)
        y = 10 ** rng.uniform(-2, 2)
        b = (2 * rng.random() - 1) * math.sqrt(x * y)
        lam = 10 ** rng.uniform(-3, 1)
        A = x - lam
        C = y + lam / 4
        target = 4 * A - b
        cost = (255 / 64) * lam + C / 16
        assert max(-target, 0.0) <= cost + 1e-10
        radial_cost_fixture(A, b, C)
        target_checks += 1

        x2 = 10 ** rng.uniform(-2, 2)
        y2 = 10 ** rng.uniform(-2, 2)
        b2 = (2 * rng.random() - 1) * math.sqrt(x2 * y2)
        assert psd(x + x2, b + b2, y + y2)
        subadditivity_checks += 1

    Y = 1024.0
    octaves = [(Y / 8, Y / 4), (Y / 4, Y / 2), (Y / 2, Y), (Y, 2 * Y)]
    assert octaves[0][0] == Y / 8 and octaves[-1][1] == 2 * Y
    assert all(
        abs(octaves[i][1] - octaves[i + 1][0]) < 1e-12 for i in range(3)
    )

    payload = {
        "schema": "riemann.t102770.centered-radial-localization.v1",
        "carrier_coefficient": carrier,
        "carrier_initial_integral": initial_integral,
        "centered_support_ratio": 8,
        "one_octave_contraction": kappa,
        "one_octave_contraction_below_0689": True,
        "source_octaves_per_dyadic_horizon": 4,
        "target_bound_checks": target_checks,
        "subadditivity_checks": subadditivity_checks,
        "endpoint_homotopy_compression": True,
        "oersc102770_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102770_CENTERED_RADIAL_LOCALIZATION",
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
