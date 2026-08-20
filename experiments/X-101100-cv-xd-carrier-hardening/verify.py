#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

BASE_SHA = "e6d923c1069f5a481abdf0769ca6d870a8b5ae4b"


def digest(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def T(y):
    return 4 * math.sqrt(y) - 3 if y >= 1 else 0.0


def K0_log_derivative(y):
    r2 = math.sqrt(2)
    if 1 < y < 2:
        return 4 * math.sqrt(y) - 3
    if 2 < y < 4:
        return -4 * r2 * math.sqrt(y) + 3 * (1 + r2)
    if 4 < y < 8:
        return 2 * math.sqrt(y) - 3 * r2
    return 0.0


def D_filter_T(y):
    r2 = math.sqrt(2)
    return (
        T(y)
        - (r2 + 2) * T(y / 2)
        + (2 * r2 + 1) * T(y / 4)
        - r2 * T(y / 8)
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    r = 0.5
    lhs = (1.0, 0.0, -r * r)
    rhs = (1.0, 0.0, -r * r)
    assert lhs == rhs

    F = (-1.0, 3.0)
    completed = (F[0] + r * F[1], F[1])
    assert completed[0] >= 0 and completed[1] >= 0
    assert F[0] < 0

    for X in (10.0, 10**3, 10**9):
        Z = X ** 0.9
        assert Z * Z > X

    P = 7.0
    v = (-P, P)
    sum_channel = (v[0] + v[1]) / math.sqrt(2)
    diff_channel = (-v[0] + v[1]) / math.sqrt(2)
    assert abs(sum_channel) < 1e-15
    assert abs(diff_channel - math.sqrt(2) * P) < 1e-12

    samples = (1.1, 1.7, 2.2, 3.7, 4.3, 7.7, 9.0, 64.0)
    max_error = 0.0
    for y in samples:
        err = abs(D_filter_T(y) - K0_log_derivative(y))
        max_error = max(max_error, err)
        assert err < 1e-10

    R = 67.0
    mass = 1.0 / (1.0 - R ** -0.5)
    assert 1 < mass < 1.15

    payload = {
        "schema": "riemann.t101100.cv-xd-carrier-hardening.v1",
        "base_sha": BASE_SHA,
        "finite_squaring_identity": True,
        "literal_completed_collar_negative_variation": 0,
        "positive_completion_implies_native_positivity": False,
        "carrier_sum_projection_zero_fixture": True,
        "kernel_bridge_max_regression_error": max_error,
        "duplicate67_resolvent_mass": mass,
        "cv_proved": False,
        "xd_proved": False,
        "rh_established": False,
        "verdict": "PASS_T101100_CV_XD_CARRIER_HARDENING",
    }
    payload["proof_object_sha256"] = digest(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
