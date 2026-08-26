#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

L = math.log(2.0)


def a(u: float) -> float:
    if not (0.0 < u < 2.0 * L):
        return 0.0
    if u < L:
        return 2.0 * (math.exp(u / 2.0) - 1.0)
    return 2.0 * math.sqrt(2.0) * (
        1.0 - math.exp((u - 2.0 * L) / 2.0)
    )


def b(u: float) -> float:
    if not (0.0 < u < 2.0 * L):
        return 0.0
    return 1.0 if u < L else -math.sqrt(2.0)


def psi(u: float) -> float:
    return b(u) / a(u)


def main() -> None:
    # Endpoint and continuity checks.
    assert abs(a(1e-12)) < 1e-9
    assert abs(a(2.0 * L - 1e-12)) < 1e-9
    assert abs(a(L - 1e-12) - a(L + 1e-12)) < 1e-8

    ode_checks = 0
    for j in range(1, 1000):
        u = 2.0 * L * j / 1000.0
        if abs(u - L) < 1e-9:
            continue
        h = 1e-7
        derivative = (a(u + h) - a(u - h)) / (2.0 * h)
        assert abs(derivative - 0.5 * a(u) - b(u)) < 2e-5
        ode_checks += 1

    psi_checks = 0
    previous = None
    for j in range(1, 2000):
        u = 2.0 * L * j / 2000.0
        if abs(u - L) < 1e-9:
            continue
        value = psi(u)
        if previous is not None:
            assert value < previous + 1e-9
        previous = value
        psi_checks += 1

    wronskian_checks = 0
    tp2_checks = 0
    for i in range(1, 25):
        x = 0.07 * i
        for j in range(i + 1, 28):
            y = 0.07 * j
            for k in range(1, 80):
                u = 0.035 * k
                w = b(u - x) * a(u - y) - a(u - x) * b(u - y)
                assert w <= 2e-12
                wronskian_checks += 1
            for r in range(1, 22):
                u1 = 0.06 * r
                u2 = u1 + 0.23
                determinant = (
                    a(u1 - x) * a(u2 - y)
                    - a(u1 - y) * a(u2 - x)
                )
                assert determinant >= -2e-12
                tp2_checks += 1

    # Source-blind sign reversal fixture.
    x, y = 0.1, 0.4
    flip = None
    for k in range(1, 100):
        u = 0.03 * k
        w = b(u - x) * a(u - y) - a(u - x) * b(u - y)
        if w < -1e-4:
            flip = -w
            break
    assert flip is not None and flip > 0.0

    payload = {
        "schema": "riemann.t103010.tp2-order-current.v1",
        "ode_checks": ode_checks,
        "psi_monotonicity_checks": psi_checks,
        "wronskian_sign_checks": wronskian_checks,
        "tp2_minor_checks": tp2_checks,
        "source_blind_flip_fixture": flip,
        "tp2_kernel_proved_by_replay": False,
        "dori103010_proved": False,
        "rh_established": False,
        "verdict": "PASS_T103010_TP2_ORDER_CURRENT",
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["proof_object_sha256"] = hashlib.sha256(raw.encode()).hexdigest()

    output = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    target = Path(__file__).parent / "results" / "verification.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(output, encoding="utf-8")

    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
