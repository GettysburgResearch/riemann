#!/usr/bin/env python3
"""Finite regression for the logarithmic annular Green continuation."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 70

ETA = mp.mpf("1")
ANNULI = (
    ((mp.mpf("0.08"), mp.mpf("14.1"), 1), (mp.mpf("0.15"), mp.mpf("21.3"), 2)),
    ((mp.mpf("0.03"), mp.mpf("30.2"), 1),),
    ((mp.mpf("0.20"), mp.mpf("9.7"), 1),),
)


def one_log_mass(x: mp.mpf, y: mp.mpf) -> mp.mpf:
    return mp.log(((ETA + x) ** 2 + y**2) / ((ETA - x) ** 2 + y**2))


def one_laplace_mass(x: mp.mpf, y: mp.mpf) -> mp.mpf:
    return mp.quadosc(
        lambda t: 4
        * mp.e ** (-ETA * t)
        * mp.sinh(x * t)
        * mp.cos(y * t)
        / t,
        [0, mp.inf],
        omega=y,
    )


def annulus_mass(rows) -> mp.mpf:
    return mp.fsum(mult * one_log_mass(x, y) for x, y, mult in rows)


def h_from_log(value: mp.mpf) -> mp.mpf:
    return (mp.e**value - 1) / (2 * ETA)


def build() -> dict[str, object]:
    annular_logs = [annulus_mass(rows) for rows in ANNULI]
    cumulative = mp.mpf("0")
    weighted_h_error = mp.mpf("0")
    additive_error = mp.mpf("0")
    lower_bound_slack = mp.inf
    laplace_error = mp.mpf("0")
    records = []

    for rows, increment in zip(ANNULI, annular_logs):
        before = cumulative
        after = cumulative + increment
        additive_error = max(additive_error, abs(after - before - increment))

        h_before = h_from_log(before)
        h_ann = h_from_log(increment)
        h_after = h_from_log(after)
        weighted_h_error = max(
            weighted_h_error,
            abs(h_after - h_before - mp.e**before * h_ann),
        )

        rational_lower = mp.fsum(
            mult * 2 * x / ((ETA + x) ** 2 + y**2)
            for x, y, mult in rows
        )
        lower_bound_slack = min(lower_bound_slack, h_ann - rational_lower)

        for x, y, mult in rows:
            laplace = one_laplace_mass(x, y)
            direct = one_log_mass(x, y)
            laplace_error = max(laplace_error, abs(laplace - direct))

        records.append(
            {
                "log_increment": float(increment),
                "h_increment": float(h_ann),
                "rational_lower_bound": float(rational_lower),
                "cumulative_log": float(after),
                "cumulative_h": float(h_after),
            }
        )
        cumulative = after

    gates = {
        "additive_log_telescope": additive_error < mp.mpf("1e-60"),
        "weighted_h_telescope": weighted_h_error < mp.mpf("1e-60"),
        "quantitative_moat": lower_bound_slack > 0,
        "green_laplace": laplace_error < mp.mpf("1e-55"),
    }
    assert all(gates.values())

    return {
        "status": "PASS_LOG_ANNULAR_GREEN",
        "gates": gates,
        "eta": float(ETA),
        "records": records,
        "final_log_mass": float(cumulative),
        "final_hyperbolic_mass": float(h_from_log(cumulative)),
        "additive_telescope_error": float(additive_error),
        "weighted_h_telescope_error": float(weighted_h_error),
        "minimum_quantitative_moat_slack": float(lower_bound_slack),
        "maximum_green_laplace_error": float(laplace_error),
    }


def main() -> None:
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
