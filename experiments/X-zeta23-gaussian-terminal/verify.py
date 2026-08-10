#!/usr/bin/env python3
"""Finite replay for Gaussian terminal-pair isolation.

Classification:
    EXACT FORMULA / FLOATING REGRESSION

The script checks the closed Gaussian kernel identities, target interpolation,
reflection symmetry, norm formula, finite-packet Gram decorrelation, the threat
inequality, and a deterministic terminal-packet leakage example.  It does not
check the Riemann-von Mangoldt theorem, the infinite zero-tail argument, the
Weil explicit formula, or RH.
"""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

SQRT_2PI = math.sqrt(2.0 * math.pi)
TOL = 2.0e-11


def kernel(sigma: float, z: complex, w: complex) -> complex:
    return (
        SQRT_2PI
        * sigma
        * cmath.exp(-0.5 * sigma * sigma * (z - w.conjugate()) ** 2)
    )


def normalized_correlation(sigma: float, z: complex, w: complex) -> float:
    den = math.sqrt(kernel(sigma, z, z).real * kernel(sigma, w, w).real)
    return abs(kernel(sigma, z, w)) / den


def interpolant(sigma: float, z: complex, w: complex) -> complex:
    reflected = z.conjugate()
    a = kernel(sigma, z, z)
    c = kernel(sigma, z, reflected)
    return (kernel(sigma, w, z) - kernel(sigma, w, reflected)) / (a - c)


def target_norm(sigma: float, z: complex) -> float:
    a = kernel(sigma, z, z).real
    c = kernel(sigma, z, z.conjugate()).real
    return 2.0 / (a - c)


def threat_phi(z: complex, w: complex) -> float:
    x, y = z.real, z.imag
    xp, d = w.real, w.imag
    return (d - y) * (d + 3.0 * y) - (xp - x) ** 2


def assert_close(actual: complex | float, expected: complex | float, tol: float = TOL) -> None:
    if abs(actual - expected) > tol * max(1.0, abs(expected)):
        raise AssertionError(f"{actual!r} != {expected!r}")


def check_kernel_formula() -> int:
    checks = 0
    points = [
        2.0 + 0.00j,
        2.3 + 0.11j,
        4.1 + 0.27j,
        -1.2 + 0.39j,
        8.0 + 0.49j,
    ]
    for sigma in (0.5, 1.0, 2.0, 4.0):
        for z in points:
            for w in points:
                lhs = normalized_correlation(sigma, z, w)
                rhs = math.exp(-0.5 * sigma * sigma * abs(z - w) ** 2)
                assert_close(lhs, rhs)
                assert_close(kernel(sigma, z, w), kernel(sigma, w, z).conjugate())
                checks += 2
    return checks


def check_target_interpolant() -> int:
    checks = 0
    z = 14.0 + 0.18j
    previous_norm = float("inf")
    for sigma in (1.0, 2.0, 4.0, 8.0, 12.0):
        fz = interpolant(sigma, z, z)
        fr = interpolant(sigma, z, z.conjugate())
        assert_close(fz, 1.0)
        assert_close(fr, -1.0)
        norm = target_norm(sigma, z)
        if not (norm > 0.0 and norm < previous_norm):
            raise AssertionError("target norm did not decrease")
        previous_norm = norm
        checks += 3

        for w in (13.4 + 0.31j, 14.5 + 0.24j, 14.2 + 0.0j):
            assert_close(
                interpolant(sigma, z, w.conjugate()),
                -interpolant(sigma, z, w).conjugate(),
            )
            checks += 1
    return checks


def check_finite_packet_decorrelation() -> int:
    checks = 0
    packet = [
        5.0 + 0.08j,
        5.7 + 0.19j,
        7.2 + 0.31j,
        9.1 + 0.00j,
    ]
    previous = float("inf")
    for sigma in (0.5, 1.0, 2.0, 4.0, 8.0):
        maximum = 0.0
        for i, z in enumerate(packet):
            for j, w in enumerate(packet):
                if i == j:
                    continue
                maximum = max(maximum, normalized_correlation(sigma, z, w))
        if maximum >= previous:
            raise AssertionError("finite-packet off-diagonal correlation did not decrease")
        previous = maximum
        checks += 1
    if previous >= 1.0e-4:
        raise AssertionError("finite packet did not decorrelate strongly")
    return checks


def check_threat_inequality() -> int:
    checks = 0
    # Synthetic threat edges: the horizontal increment is 90% of the exact
    # parabolic threshold.  Their squared increments telescope below twice the
    # total depth increase, exactly as in the theorem.
    y_values = [0.08, 0.13, 0.19, 0.26, 0.34, 0.41, 0.46]
    x_values = [0.0]
    square_sum = 0.0
    for y, d in zip(y_values, y_values[1:]):
        threshold = (d - y) * (d + 3.0 * y)
        dx = 0.9 * math.sqrt(threshold)
        x_values.append(x_values[-1] + dx)
        square_sum += dx * dx
        if dx * dx > threshold + TOL:
            raise AssertionError("synthetic edge is not a threat")
        if dx * dx >= 2.0 * (d - y):
            raise AssertionError("strict depth-energy inequality failed")
        checks += 2

    if square_sum >= 2.0 * (y_values[-1] - y_values[0]):
        raise AssertionError("telescoping threat budget failed")

    for n, x in enumerate(x_values[1:], start=1):
        if abs(x - x_values[0]) >= math.sqrt(n):
            raise AssertionError("Cauchy square-root confinement failed")
        checks += 1
    return checks


def check_terminal_packet_leakage() -> tuple[int, list[dict[str, float]]]:
    z = 14.0 + 0.18j
    nuisance = [
        13.4 + 0.31j,
        14.5 + 0.24j,
        14.1 + 0.12j,
        15.2 + 0.45j,
        14.2 + 0.00j,
    ]
    for w in nuisance:
        if threat_phi(z, w) >= 0.0:
            raise AssertionError("control packet is not terminal")

    rows: list[dict[str, float]] = []
    previous_leak = float("inf")
    previous_norm = float("inf")
    checks = 0
    for sigma in (2.0, 4.0, 6.0, 8.0, 10.0, 12.0):
        leak = sum(abs(interpolant(sigma, z, w)) ** 2 for w in nuisance)
        norm = target_norm(sigma, z)
        if not (leak < previous_leak and norm < previous_norm):
            raise AssertionError("terminal leakage or target norm did not decrease")
        previous_leak = leak
        previous_norm = norm
        rows.append({"sigma": sigma, "nuisance_square_sum": leak, "target_norm": norm})
        checks += 2

    if previous_leak >= 1.0e-3:
        raise AssertionError("terminal packet leakage did not become small")
    return checks, rows


def main() -> None:
    counts = {
        "kernel_and_correlation": check_kernel_formula(),
        "target_and_reflection": check_target_interpolant(),
        "finite_packet_decorrelation": check_finite_packet_decorrelation(),
        "threat_budget": check_threat_inequality(),
    }
    leak_checks, rows = check_terminal_packet_leakage()
    counts["terminal_packet"] = leak_checks

    payload = {
        "classification": "PASS_GAUSSIAN_TERMINAL_PAIR_ALGEBRA",
        "arithmetic_class": "EXACT_CLOSED_FORM_PLUS_FLOATING_REGRESSION",
        "checks": counts,
        "terminal_packet": rows,
        "not_certified": [
            "Riemann-von Mangoldt theorem",
            "infinite zero-tail interchange",
            "Weil explicit formula continuity",
            "arithmetic lower floor",
            "Riemann Hypothesis",
        ],
    }
    out = Path(__file__).with_name("verification.json")
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
