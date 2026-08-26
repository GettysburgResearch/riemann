#!/usr/bin/env python3
"""Exact exponent replay for the growing closed-place supply tax."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

PANELS = (
    (0.5, 0.20, 0.20),
    (0.5, 0.274064461784, 0.40),
    (0.5, 0.30, 0.48),
    (1.0, 0.40, 0.30),
    (1.0, 0.548128923568, 0.45),
    (1.0, 0.60, 0.55),
)


def upper_tail_rate(density: float, alpha: float, beta: float) -> float:
    if not 0 < density <= 1:
        raise ValueError("density must lie in (0,1]")
    if not 0 < alpha < density:
        raise ValueError("alpha must lie in (0,density)")
    if not 0 < beta < alpha / density:
        raise ValueError("beta must lie below alpha/density")
    mean_exponent = density * beta
    return alpha * math.log(alpha / mean_exponent) - alpha + mean_exponent


def leverage_exponent(alpha: float) -> float:
    if alpha <= 0:
        raise ValueError("alpha must be positive")
    return alpha * math.log(5 / 4)


def panel(density: float, alpha: float, beta: float) -> dict[str, object]:
    rate = upper_tail_rate(density, alpha, beta)
    return {
        "eligible_density": density,
        "rank_exponent_alpha": alpha,
        "short_place_cutoff_exponent_beta": beta,
        "expected_short_factor_exponent": density * beta,
        "upper_tail_rate": f"{rate:.12f}",
        "formal_leverage_exponent": f"{leverage_exponent(alpha):.12f}",
        "critical_place_degree_exponent": f"{alpha / density:.12f}",
    }


def run() -> dict[str, object]:
    return {
        "truncated_factor_mgf": {
            "bound": "E[s^Omega_E(F;D)] <= C_q*D^(delta*(s-1))",
            "range": "s>=1, D<n, F monic squarefree of degree n",
        },
        "large_deviation": {
            "rank": "r=floor(alpha*log n)",
            "cutoff": "D=floor(n^beta), beta<alpha/delta",
            "probability": "Pr(Omega_E(F;D)>=r)<=n^(-J+o(1))",
            "rate": "J=alpha*log(alpha/(delta*beta))-alpha+delta*beta",
        },
        "supply_tax": {
            "typical_rth_place_degree": (
                "log(d_(r))/log(n) >= alpha/delta-o_Pr(1)"
            ),
            "leverage_gain": "n^(-alpha*log(5/4)+o(1))",
            "degree_to_leverage_exponent_ratio": {
                "delta_1": f"{1 / math.log(5 / 4):.12f}",
                "delta_1_over_2": f"{2 / math.log(5 / 4):.12f}",
            },
            "allowable_conductor_power": {
                "delta_1": f"{math.log(5 / 4):.12f}",
                "delta_1_over_2": f"{0.5 * math.log(5 / 4):.12f}",
                "criterion": "a D^theta loss requires theta<delta*log(5/4)",
            },
        },
        "panels": [panel(*values) for values in PANELS],
        "resource_caps": {
            "exponent_panels": len(PANELS),
            "polynomials_enumerated": 0,
            "closed_places_enumerated": 0,
            "curves_enumerated": 0,
            "point_counts": 0,
            "floating_point_evaluations": 40,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
