#!/usr/bin/env python3
"""Finite controls for the growing-resolution first-Hermite positivity wedge."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def simpson(fn, a: float, b: float, n: int) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    total = fn(a) + fn(b)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * fn(a + i * h)
    return total * h / 3


def rf(x: float) -> float:
    if not math.isfinite(x):
        raise ValueError(x)
    return round(x, 15)


def continuum_prime_envelope(q: float) -> float:
    upper = q + 14 * math.sqrt(q) + 20
    integral = simpson(
        lambda t: t
        * (1 + t * t / (2 * q))
        * math.exp(t / 2 - t * t / (4 * q)),
        0.0,
        upper,
        120000,
    )
    return integral / (2 * math.sqrt(math.pi) * q ** 1.5)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    # Exact completion-of-square identity.
    square_errors = []
    for q in (1.0, 2.0, 5.0, 10.0, 25.0):
        for t in (0.0, 0.3 * q, q, 1.7 * q, 3 * q):
            left = t / 2 - t * t / (4 * q)
            right = q / 4 - (t - q) ** 2 / (4 * q)
            square_errors.append(abs(left - right))

    # The absolute prime envelope has the predicted q*exp(q/4) scale.
    prime_rows = []
    max_ratio = 0.0
    for q in (1.0, 2.0, 4.0, 8.0, 12.0, 20.0, 32.0):
        envelope = continuum_prime_envelope(q)
        ratio = envelope / (q * math.exp(q / 4))
        max_ratio = max(max_ratio, ratio)
        prime_rows.append(
            {
                "q": q,
                "continuum_envelope": rf(envelope),
                "ratio_to_q_exp_q_over_4": rf(ratio),
            }
        )

    # Wedge ratio q^(5/2)e^(q/4)/log x with log log x = ell.
    epsilon = 0.5
    wedge_rows = []
    previous_log_ratio = float("inf")
    wedge_decreases = True
    for ell in (20.0, 40.0, 80.0, 160.0, 320.0):
        q = (4 - epsilon) * ell
        log_ratio = 2.5 * math.log(q) + q / 4 - ell
        wedge_decreases = wedge_decreases and log_ratio < previous_log_ratio
        previous_log_ratio = log_ratio
        wedge_rows.append(
            {
                "log_log_x": ell,
                "q": q,
                "log_of_q_5_over_2_exp_q_over_4_over_log_x": rf(log_ratio),
            }
        )

    # Above the constant 4 the same phase-blind ratio grows.
    supercritical_rows = []
    epsilon_plus = 0.5
    previous = -float("inf")
    grows = True
    for ell in (20.0, 40.0, 80.0, 160.0):
        q = (4 + epsilon_plus) * ell
        log_ratio = 2.5 * math.log(q) + q / 4 - ell
        grows = grows and log_ratio > previous
        previous = log_ratio
        supercritical_rows.append(
            {"log_log_x": ell, "q": q, "log_ratio": rf(log_ratio)}
        )

    # Target exponent threshold: q*y^2 versus log log height.
    depth_rows = []
    ell = 100.0
    for y in (0.49, 0.4, 0.25, 0.1):
        q_needed = ell / (y * y)
        depth_rows.append(
            {
                "depth": y,
                "q_for_q_y_squared_equals_log_log_height": rf(q_needed),
                "ratio_to_4_log_log_height": rf(q_needed / (4 * ell)),
            }
        )

    gates = {
        "completion_of_square": max(square_errors) < 1e-12,
        "prime_envelope_q_exp_q_over_4_scale": max_ratio < 8.0,
        "subcritical_wedge_ratio_tends_down": wedge_decreases
        and previous_log_ratio < -20,
        "constant_four_phase_blind_wall": grows,
        "depth_threshold_at_least_four": all(
            r["ratio_to_4_log_log_height"] > 1 for r in depth_rows
        ),
    }
    if not all(gates.values()):
        raise SystemExit(gates)

    out = {
        "status": "PASS_GROWING_RESOLUTION_HEAT_WEDGE",
        "gates": gates,
        "max_completion_square_error": rf(max(square_errors)),
        "prime_envelope_rows": prime_rows,
        "maximum_prime_scale_ratio": rf(max_ratio),
        "subcritical_wedge": {"epsilon": epsilon, "rows": wedge_rows},
        "supercritical_phase_blind_control": {
            "epsilon": epsilon_plus,
            "rows": supercritical_rows,
        },
        "depth_resolution_rows": depth_rows,
    }
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
