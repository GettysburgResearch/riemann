#!/usr/bin/env python3
"""Finite controls for the macroscopic first-Hermite positivity theorem.

The replay checks the elementary inequalities used in the proof. It does not
certify the global digamma bound, Guinand--Weil, the all-prime sign, or RH.
"""
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


def paired_log(x: float, u: float) -> float:
    return math.log(2 + abs(x + u)) + math.log(2 + abs(x - u))


def annulus_mass() -> float:
    return simpson(lambda v: v * v * math.exp(-v * v), 1.0, 2.0, 20000)


def log_integral(q: float, x: float) -> float:
    # Scale u=v/sqrt(q), truncate at v=10 where the tail is negligible.
    return q ** -1.5 * simpson(
        lambda v: v * v
        * math.exp(-v * v)
        * (
            math.log(2 + abs(x + v / math.sqrt(q)))
            + math.log(2 + abs(x - v / math.sqrt(q)))
        ),
        0.0,
        10.0,
        80000,
    )


def integer_prime_envelope(q: float, limit: int = 150000) -> float:
    total = 0.0
    for n in range(2, limit + 1):
        t = math.log(n)
        total += (
            t
            / math.sqrt(n)
            * (1 + t * t / (2 * q))
            * math.exp(-t * t / (4 * q))
            / (2 * math.sqrt(math.pi) * q ** 1.5)
        )
    return total


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    # Paired logarithm inequality over a hostile grid.
    min_slack = float("inf")
    worst = None
    for x_i in range(-300, 301):
        x = x_i / 13
        for u_i in range(1, 401):
            u = u_i / 17
            slack = paired_log(x, u) - math.log(2 + u)
            if slack < min_slack:
                min_slack = slack
                worst = (x, u)

    mass = annulus_mass()
    small_q_rows = []
    for q in (0.2, 0.1, 0.05, 0.025, 0.0125):
        minimum_sample = min(
            log_integral(q, x) for x in (-30.0, -3.0, 0.0, 4.0, 35.0)
        )
        lower = 0.5 * mass * q ** -1.5 * math.log(1 / q)
        small_q_rows.append(
            {
                "q": q,
                "minimum_sampled_log_integral": rf(minimum_sample),
                "annulus_lower_bound": rf(lower),
                "ratio": rf(minimum_sample / lower),
            }
        )

    prime_rows = []
    previous = float("inf")
    decreasing = True
    for q in (0.05, 0.03, 0.02, 0.01, 0.005, 0.004):
        value = integer_prime_envelope(q)
        decreasing = decreasing and value < previous
        previous = value
        prime_rows.append({"q": q, "all_integer_envelope": rf(value)})

    # Fixed-q logarithmic growth of the positive gamma surrogate.
    q_fixed = 1.3
    center_rows = []
    previous_value = -float("inf")
    eventually_increasing = True
    for x in (10.0, 30.0, 100.0, 300.0, 1000.0):
        value = log_integral(q_fixed, x)
        eventually_increasing = eventually_increasing and value > previous_value
        previous_value = value
        center_rows.append({"x": x, "log_integral": rf(value)})

    # Pole bound: sup_x (x^2+1/4)e^{-q x^2} is O(1/q).
    pole_rows = []
    for q in (0.05, 0.1, 0.5, 1.0, 2.0):
        samples = [(j / 500) ** 2 + 0.25 for j in range(0, 10000)]
        values = [
            samples[j] * math.exp(-q * (j / 500) ** 2)
            for j in range(len(samples))
        ]
        sup_numeric = max(values)
        coarse_bound = 1 / (math.e * q) + 0.25
        pole_rows.append(
            {
                "q": q,
                "numeric_sup_without_exp_q_over_4": rf(sup_numeric),
                "coarse_bound": rf(coarse_bound),
                "bound_holds": sup_numeric <= coarse_bound + 1e-12,
            }
        )

    gates = {
        "paired_log_lower_bound": min_slack >= -1e-14,
        "small_q_annulus_bound": all(r["ratio"] >= 1 for r in small_q_rows),
        "prime_envelope_superdecay": decreasing and previous < 1e-8,
        "fixed_q_center_growth": eventually_increasing,
        "pole_O_inverse_q_bound": all(r["bound_holds"] for r in pole_rows),
    }
    if not all(gates.values()):
        raise SystemExit(gates)

    out = {
        "status": "PASS_MACROSCOPIC_FIRST_HERMITE_POSITIVITY",
        "gates": gates,
        "paired_log": {
            "minimum_slack": rf(min_slack),
            "worst_grid_point": [rf(worst[0]), rf(worst[1])] if worst else None,
        },
        "annulus_mass_1_2": rf(mass),
        "small_q_rows": small_q_rows,
        "prime_envelope_rows": prime_rows,
        "fixed_q_center_rows": center_rows,
        "pole_bound_rows": pole_rows,
    }
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
