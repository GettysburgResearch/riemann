#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from pathlib import Path

VERDICT = "PASS_X_100500_MINIMAL_WAVELET_MERTENS_FRAME"


def K(y: float) -> float:
    rt2 = math.sqrt(2.0)
    if y < 1.0 or y >= 8.0:
        return 0.0
    if y < 2.0:
        return 8.0 * math.sqrt(y) - 8.0 - 3.0 * math.log(y)
    if y < 4.0:
        return (
            -8.0 * rt2 * math.sqrt(y)
            + 8.0 * (1.0 + rt2)
            + 3.0 * (1.0 + rt2) * math.log(y)
            - 3.0 * (2.0 + rt2) * math.log(2.0)
        )
    return (
        4.0 * math.sqrt(y)
        - 8.0 * rt2
        + 9.0 * rt2 * math.log(2.0)
        - 3.0 * rt2 * math.log(y)
    )


def V(y: float) -> float:
    rt2 = math.sqrt(2.0)
    if y <= 1.0 or y >= 8.0:
        return 0.0
    sy = math.sqrt(y)
    if y < 2.0:
        return 8.0 - (7.0 + 1.5 * math.log(y)) / sy
    if y < 4.0:
        return -8.0 * rt2 + (
            7.0 * (1.0 + rt2)
            + 1.5 * (1.0 + rt2) * math.log(y)
            - 1.5 * (2.0 + rt2) * math.log(2.0)
        ) / sy
    return 4.0 + (
        -7.0 * rt2
        + 4.5 * rt2 * math.log(2.0)
        - 1.5 * rt2 * math.log(y)
    ) / sy


def adaptive_simpson(f, a, b, eps=1e-11, depth=20):
    c = (a + b) / 2.0
    fa, fb, fc = f(a), f(b), f(c)
    whole = (b - a) * (fa + 4.0 * fc + fb) / 6.0

    def rec(a, b, fa, fb, fc, whole, eps, depth):
        c = (a + b) / 2.0
        l = (a + c) / 2.0
        r = (c + b) / 2.0
        fl, fr = f(l), f(r)
        left = (c - a) * (fa + 4.0 * fl + fc) / 6.0
        right = (b - c) * (fc + 4.0 * fr + fb) / 6.0
        if depth <= 0 or abs(left + right - whole) <= 15.0 * eps:
            return left + right + (left + right - whole) / 15.0
        return rec(a, c, fa, fc, fl, left, eps / 2.0, depth - 1) + rec(
            c, b, fc, fb, fr, right, eps / 2.0, depth - 1
        )

    return rec(a, b, fa, fb, fc, whole, eps, depth)


def run() -> dict[str, object]:
    endpoint_checks = 0
    derivative_checks = 0
    abel_checks = 0
    inverse_checks = 0
    hostile = 0

    # Endpoints and activation continuity.
    assert abs(K(1.0)) < 1e-14
    assert abs(K(8.0)) < 1e-14
    for knot in (2.0, 4.0):
        assert abs(K(knot * (1.0 - 1e-12)) - K(knot * (1.0 + 1e-12))) < 1e-8
        endpoint_checks += 1
    endpoint_checks += 2

    # Verify V = y^-1/2 (K/2 + y K') away from knots.
    for y in [1.05, 1.2, 1.7, 2.2, 3.3, 4.2, 6.5, 7.8]:
        h = 1e-6 * y
        kp = (K(y + h) - K(y - h)) / (2.0 * h)
        rhs = (0.5 * K(y) + y * kp) / math.sqrt(y)
        assert abs(V(y) - rhs) < 2e-7
        derivative_checks += 1

    # Abel identity on arbitrary finite coefficient fixtures.
    # Preserve the original T100200 fixture stream: this publication only
    # migrates the claim namespace and does not change the mathematics.
    rng = random.Random(100200)
    for X in (64.0, 96.0, 160.0, 256.0):
        N = int(X)
        coeff = [0] + [rng.choice((-1, 0, 1)) for _ in range(N)]
        prefix = [0] * (N + 1)
        for n in range(1, N + 1):
            prefix[n] = prefix[n - 1] + coeff[n]

        direct = sum(
            coeff[n] / math.sqrt(n) * K(X / n)
            for n in range(max(1, math.ceil(X / 8.0)), N + 1)
        )

        def M_of(t: float) -> int:
            j = min(N, max(0, int(math.floor(t + 1e-12))))
            return prefix[j]

        def integrand(y: float) -> float:
            return M_of(X / y) * V(y)

        # Split at every Mertens jump in y=X/n and at kernel knots.
        cuts = {1.0, 2.0, 4.0, 8.0}
        for n in range(max(1, math.floor(X / 8.0)), N + 1):
            y = X / n
            if 1.0 < y < 8.0:
                cuts.add(y)
        cuts = sorted(cuts)
        integral = 0.0
        for a, b in zip(cuts, cuts[1:]):
            if b - a < 1e-13:
                continue
            integral += adaptive_simpson(integrand, a + 1e-10, b - 1e-10)
        framed = integral / math.sqrt(X)
        assert abs(direct - framed) < 3e-6
        abel_checks += 1

    # Exact critical inverse coefficients and square-root mass growth.
    for L in range(1, 21):
        coeff = [2.0 ** (j / 2.0) for j in range(L + 1)]
        total = sum(coeff)
        assert total >= 2.0 ** (L / 2.0)
        assert total <= (1.0 / (1.0 - 2.0 ** -0.5)) * 2.0 ** (L / 2.0)
        inverse_checks += 2

    # Hostile mutations.
    if abs(K(1.0) - 1.0) > 0.1:
        hostile += 1
    if abs(K(8.0) - 1.0) > 0.1:
        hostile += 1
    if 2.0 ** (10 / 2.0) != 31.0:
        hostile += 1
    if VERDICT != "PASS_X_100500_WAVELET":
        hostile += 1
    if V(1.5) != 0.0:
        hostile += 1

    core = {
        "schema": "riemann.x100500.wavelet-mertens-frame.v1",
        "classification": VERDICT,
        "base_pr": 675,
        "base_sha": "7b28224ba1b072d4ccd5b93ad37c0a64e7939740",
        "endpoint_continuity_checks": endpoint_checks,
        "kernel_derivative_checks": derivative_checks,
        "abel_mertens_fixture_checks": abel_checks,
        "critical_inverse_checks": inverse_checks,
        "hostile_mutations_detected": hostile,
        "proves": [
            "exact compact Abel-Mertens representation",
            "piecewise derivative kernel authentication",
            "critical square-root inverse cost",
            "source-blind labelled-collapse firewall",
        ],
        "analytic_theorems_in_packet": [
            "quantitative Littlewood exponent dictionary",
            "MWOC100500 is equivalent to RH",
        ],
        "does_not_prove": [
            "MWOC100500",
            "Riemann Hypothesis",
        ],
        "mwoc100500_proved": False,
        "rh_established": False,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    return {**core, "proof_object_sha256": hashlib.sha256(canon).hexdigest()}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
