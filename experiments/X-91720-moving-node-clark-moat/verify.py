#!/usr/bin/env python3
"""Finite replay for the optimized moving-node Clark moat."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 70


def charge(eta, x, y):
    return mp.log(((eta + x) ** 2 + y**2) / ((eta - x) ** 2 + y**2))


def box_moat(eta, delta, upper, height):
    return 4 * eta * delta / ((eta + upper) ** 2 + height**2)


def optimal_node(upper, height):
    return mp.sqrt(upper**2 + height**2)


def optimal_moat(delta, upper, height):
    return 2 * delta / (mp.sqrt(upper**2 + height**2) + upper)


def build():
    delta = mp.mpf("0.03")
    upper = mp.mpf("0.06")
    heights = [mp.mpf("1"), mp.mpf("5"), mp.mpf("20"), mp.mpf("100")]

    optimization_errors = []
    moat_records = []
    for Y in heights:
        eta = optimal_node(upper, Y)
        direct = box_moat(eta, delta, upper, Y)
        closed = optimal_moat(delta, upper, Y)
        optimization_errors.append(abs(direct - closed))
        fixed = box_moat(mp.mpf("1"), delta, upper, Y)
        moat_records.append(
            {
                "height": float(Y),
                "optimal_node": float(eta),
                "optimal_moat": float(closed),
                "fixed_node_moat": float(fixed),
                "gain": float(closed / fixed),
            }
        )

    synthetic = [
        (mp.mpf("0.031"), mp.mpf("2.1")),
        (mp.mpf("0.045"), mp.mpf("7.7")),
        (mp.mpf("0.059"), mp.mpf("19.5")),
    ]
    Y = mp.mpf("20")
    eta = optimal_node(upper, Y)
    lower_slacks = [
        charge(eta, x, y) - optimal_moat(delta, upper, Y)
        for x, y in synthetic
    ]
    total = sum(charge(eta, x, y) for x, y in synthetic)
    count_upper = total / optimal_moat(delta, upper, Y)

    asymptotic_records = []
    for Y in [mp.mpf("10"), mp.mpf("100"), mp.mpf("1000")]:
        scaled = Y * optimal_moat(delta, upper, Y)
        asymptotic_records.append(float(scaled))

    gates = {
        "closed_optimum": max(optimization_errors) < mp.mpf("1e-60"),
        "synthetic_moat": min(lower_slacks) > 0,
        "count_bound": count_upper >= len(synthetic),
        "one_over_y_rate": abs(asymptotic_records[-1] - float(2 * delta)) < 1e-4,
    }
    assert all(gates.values())

    return {
        "status": "PASS_MOVING_NODE_CLARK_MOAT",
        "gates": gates,
        "delta": float(delta),
        "upper_depth": float(upper),
        "optimization_errors": [float(x) for x in optimization_errors],
        "moat_records": moat_records,
        "synthetic_lower_slacks": [float(x) for x in lower_slacks],
        "synthetic_count_upper_bound": float(count_upper),
        "height_times_optimal_moat": asymptotic_records,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = json.dumps(build(), sort_keys=True, separators=(",", ":")) + "\n"
    if args.json:
        args.json.write_text(payload)
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
