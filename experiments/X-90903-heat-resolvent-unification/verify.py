#!/usr/bin/env python3
"""Checks the confluent resolvent/first-Hermite Gamma-moment identity."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp


def resolvent(k: int, y: mp.mpf, z: mp.mpc) -> mp.mpc:
    p = k + 1
    return mp.factorial(k) * (
        (1 - z * z) ** (-p)
        - mp.mpf("0.5") * (1 - z * z - 2 * y * z) ** (-p)
        - mp.mpf("0.5") * (1 - z * z + 2 * y * z) ** (-p)
    )


def confluent(k: int, z: mp.mpc) -> mp.mpc:
    return -2 * mp.factorial(k + 2) * z * z / (1 - z * z) ** (k + 3)


def gamma_integral(k: int, z: mp.mpc) -> mp.mpc:
    return -2 * mp.quad(lambda q: q ** (k + 2) * mp.e ** (-q) * z * z * mp.e ** (q * z * z), [0, mp.inf])


def main():
    mp.mp.dps = 60
    points = [mp.mpc("0.2", "0.1"), mp.mpc("0.35", "0.2"), mp.mpc("0.1", "0.5")]
    ys = [mp.mpf("0.1"), mp.mpf("0.05"), mp.mpf("0.025"), mp.mpf("0.0125")]
    max_gamma_error = mp.mpf("0")
    convergence = []
    for k in [0, 1, 3, 7]:
        for z in points:
            target = confluent(k, z)
            integ = gamma_integral(k, z)
            max_gamma_error = max(max_gamma_error, abs(target - integ))
            row = []
            for y in ys:
                row.append(float(abs(resolvent(k, y, z) / (y * y) - target)))
            convergence.append({"k": k, "z": [float(z.real), float(z.imag)], "errors": row})

    # Convergence errors should shrink approximately quadratically in y.
    convergence_ok = all(item["errors"][-1] < item["errors"][0] / 20 for item in convergence)
    gates = {
        "gamma_moment_identity": max_gamma_error < mp.mpf("1e-45"),
        "confluent_convergence": convergence_ok,
    }
    if not all(gates.values()):
        raise AssertionError(gates)

    return {
        "status": "PASS_X_90903_HEAT_RESOLVENT_UNIFICATION",
        "gates": gates,
        "max_gamma_moment_error": float(max_gamma_error),
        "convergence": convergence,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = main()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text)
    else:
        print(text, end="")
