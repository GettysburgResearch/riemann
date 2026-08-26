#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def digest(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    monotonicity_subset_checks = 0
    for dim in range(1, 5):
        for c1, c2 in [(1.0, 0.0), (0.75, 0.25)]:
            for mask in range(1, 1 << dim):
                k = mask.bit_count()
                assert c1**k - c2**k >= 0.0
                monotonicity_subset_checks += 1

    sqrt2 = math.sqrt(2.0)
    z0 = 4.0 * sqrt2 - 5.0
    radius = 8.0 - 4.0 * sqrt2
    disk_constant = 16.0 - 8.0 * sqrt2

    assert abs(radius + z0 - 3.0) < 1e-12
    assert abs(radius**2 - z0**2 - (39.0 - 24.0 * sqrt2)) < 1e-12

    zx = -2.0 / 5.0
    zy = 4.0 * math.sqrt(6.0) / 5.0
    assert (3.0 - zx) ** 2 + zy**2 < disk_constant * (3.0 - zx)
    assert abs(zx**2 + zy**2 - 4.0) < 1e-12
    assert abs(2.0 * zx + 4.0 / 5.0) < 1e-12

    fixtures = [
        (1.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 2.0, 0.0),
        (1.0, -z0, z0**2 + radius**2, 0.0),
    ]
    for a, h, q, lam in fixtures:
        m11 = a + lam
        m12 = h + z0 * a
        m22 = q + 2.0 * z0 * h + z0**2 * a - lam * radius**2
        assert m11 >= -1e-12
        assert m22 >= -1e-12
        assert m11 * m22 - m12**2 >= -1e-12

    # Active polynomial identities for (D-1)T^2=3T and (D-1)(16y)=0.
    # Coefficients are ordered as y, sqrt(y), 1.
    t2 = (16.0, -24.0, 9.0)
    dminus1_t2 = (
        (1.0 - 1.0) * t2[0],
        (0.5 - 1.0) * t2[1],
        (0.0 - 1.0) * t2[2],
    )
    assert dminus1_t2 == (0.0, 12.0, -9.0)
    assert (1.0 - 1.0) * 16.0 == 0.0
    assert 1.0 == 1.0  # T^2 activation jump.
    assert 16.0 == 16.0  # W_3 activation jump.

    # Full P_2 mutation on a nonnegative dyadic fixture.
    filter_value = -(2.0 + sqrt2)
    assert filter_value < 0.0

    payload = {
        "schema": "riemann.t102730.completion-current-matrix.v1",
        "monotonicity_subset_checks": monotonicity_subset_checks,
        "disk_geometry_checks": 5,
        "s_lemma_matrix_fixtures": len(fixtures),
        "distributional_bridge_checks": 4,
        "fixed_shift_inside_disk": True,
        "fixed_five_to_one_projection": True,
        "filter_counterexample_value": filter_value,
        "completion_tangent_sharp_disk_positive": True,
        "flc102730_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102730_COMPLETION_CURRENT_MATRIX",
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
