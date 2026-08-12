#!/usr/bin/env python3
"""Finite checks for the radial spectral-type lock packet.

This script verifies exact finite identities and a toy spectral-type firewall.
It does not prove the continuous-product gamma refinement, RLSL, or RH.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np


def prime_radial_error() -> float:
    mp.mp.dps = 80
    sigma = mp.mpf("1.7")
    a = mp.mpf("0.43")
    carrier = mp.mpf("0.91")
    direct = mp.mpc(0)
    radial = mp.mpc(0)

    for p in (2, 3, 5, 7, 11):
        for k in (1, 2, 3):
            u = mp.mpf(k) * mp.log(p)
            coeff = mp.power(p, -k * sigma) * (1 - mp.power(p, -2 * a * k)) / k
            phase = 1 - mp.e ** (-1j * carrier * u)
            direct += coeff * phase
            radial += mp.quad(
                lambda r: 2
                * mp.log(p)
                * mp.power(p, -k * (sigma + 2 * r))
                * phase,
                [0, a],
            )

    return float(abs(direct - radial))


def eta_radial_error() -> float:
    mp.mp.dps = 80
    sigma = mp.mpf("1.3")
    omega = mp.mpf("0.27")
    delta = mp.mpf("0.61")
    cutoff = 300

    def i_eta(z: mp.mpc) -> mp.mpc:
        return mp.fsum(
            [
                (mp.power(2 * m - 1, -z) - mp.power(2 * m, -z)) / z
                for m in range(1, cutoff + 1)
            ]
        )

    lhs = i_eta(sigma - omega + 1j * delta) - i_eta(
        sigma + omega + 1j * delta
    )
    rhs = mp.mpc(0)
    for m in range(1, cutoff + 1):
        lo = mp.log(2 * m - 1)
        hi = mp.log(2 * m)
        rhs += mp.quad(
            lambda y: mp.e ** (-(sigma - omega + 1j * delta) * y)
            - mp.e ** (-(sigma + omega + 1j * delta) * y),
            [lo, hi],
        )

    return float(abs(lhs - rhs))


def build_results() -> dict:
    n_grid = 127
    grid = (np.arange(n_grid) + 0.5) / n_grid
    atom_depth = math.sqrt(2.0) / 4.0
    min_gap = float(np.min(np.abs(grid - atom_depth)))

    halfwidths = [0.1, 0.05, 0.02, 0.01, 0.005, 0.002]
    bounds = [math.sqrt(min(1.0, 2.0 * h)) for h in halfwidths]

    result = {
        "status": "PASS_RADIAL_SPECTRAL_TYPE_LOCK",
        "prime_radial_identity_error": prime_radial_error(),
        "eta_radial_identity_error": eta_radial_error(),
        "finite_grid_atom_depth": atom_depth,
        "finite_grid_min_spectral_gap": min_gap,
        "shrinking_interval_halfwidths": halfwidths,
        "module_local_atom_norm_bounds": bounds,
        "global_total_counterexample": {
            "source_total": 1.0,
            "critical_total": 0.7,
            "hyperbolic_atom_total": 0.3,
            "global_equality": True,
            "interval_locality": False,
        },
    }

    assert result["prime_radial_identity_error"] < 1e-60
    assert result["eta_radial_identity_error"] < 1e-60
    assert result["finite_grid_min_spectral_gap"] > 0
    assert all(
        b1 > b2
        for b1, b2 in zip(
            result["module_local_atom_norm_bounds"],
            result["module_local_atom_norm_bounds"][1:],
        )
    )
    assert (
        result["global_total_counterexample"]["source_total"]
        == result["global_total_counterexample"]["critical_total"]
        + result["global_total_counterexample"]["hyperbolic_atom_total"]
    )
    assert not result["global_total_counterexample"]["interval_locality"]

    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    result = build_results()
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n"

    if args.json:
        args.json.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
