#!/usr/bin/env python3
"""Bounded replay for the closed-place entropy--conductor phase diagram."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

LOG_BLOCK_GAIN = math.log(5 / 4)


def is_prime_power(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value and value % divisor:
        divisor += 1
    if divisor * divisor > value:
        return True
    while value % divisor == 0:
        value //= divisor
    return value == 1


def eligible_density(q: int) -> float:
    """Return the logarithmic density of quartically orientable places."""
    if q <= 1 or q % 2 == 0 or not is_prime_power(q):
        raise ValueError("q must be an odd prime power")
    return 1.0 if q % 4 == 1 else 0.5


def effective_rank_gain(density: float, conductor_power: float) -> float:
    """Exponent per block after a degree^theta conductor loss."""
    if density not in (0.5, 1.0):
        raise ValueError("density must be 1/2 or 1")
    if conductor_power < 0:
        raise ValueError("conductor power must be nonnegative")
    return LOG_BLOCK_GAIN - conductor_power / density


def richness_rate(density: float, alpha: float) -> float:
    """Ambient poor-core exponent at rank alpha*log(n)."""
    if density not in (0.5, 1.0):
        raise ValueError("density must be 1/2 or 1")
    if not 0 < alpha < density:
        raise ValueError("alpha must lie strictly between zero and density")
    return density - alpha + alpha * math.log(alpha / density)


def uniform_balanced_fraction(density: float, conductor_power: float) -> float:
    """Solve 1-x+x log x = log(5/4)*x-theta/delta on (0,1)."""
    typical_gain = effective_rank_gain(density, conductor_power)
    if typical_gain <= 0:
        raise ValueError("conductor power must lie below the critical threshold")
    scaled_power = conductor_power / density
    lo = 1e-15
    hi = 1 - 1e-15
    for _ in range(160):
        mid = (lo + hi) / 2
        value = (
            1
            - mid
            + mid * math.log(mid)
            - LOG_BLOCK_GAIN * mid
            + scaled_power
        )
        if value > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def optimized_power_panel(density: float, conductor_power: float) -> dict[str, object]:
    typical_gain = effective_rank_gain(density, conductor_power)
    threshold = density * LOG_BLOCK_GAIN
    if typical_gain <= 0:
        return {
            "density": density,
            "conductor_power": conductor_power,
            "critical_conductor_power": f"{threshold:.12f}",
            "status": "no growing-rank net gain",
            "typical_effective_gain_per_rank": f"{typical_gain:.12f}",
            "optimal_alpha": None,
            "optimal_net_exponent": "0.000000000000",
        }
    fraction = uniform_balanced_fraction(density, conductor_power)
    alpha = density * fraction
    uniform_trace_exponent = alpha * LOG_BLOCK_GAIN - conductor_power
    exponent = uniform_trace_exponent
    return {
        "density": density,
        "conductor_power": conductor_power,
        "critical_conductor_power": f"{threshold:.12f}",
        "status": "conditional uniform rich-core net gain",
        "typical_effective_gain_per_rank": f"{typical_gain:.12f}",
        "optimal_fraction_alpha_over_delta": f"{fraction:.12f}",
        "optimal_alpha": f"{alpha:.12f}",
        "optimal_net_exponent": f"{exponent:.12f}",
        "uniform_trace_exponent_at_optimum": f"{uniform_trace_exponent:.12f}",
        "richness_rate_at_optimum": f"{richness_rate(density, alpha):.12f}",
    }


def sublog_panel(
    density: float, conductor_power: float, kappa: float
) -> dict[str, object]:
    if kappa <= 0:
        raise ValueError("kappa must be positive")
    gain = effective_rank_gain(density, conductor_power)
    return {
        "density": density,
        "conductor_power": conductor_power,
        "rank_schedule": f"r={kappa:g}*log(log(n))",
        "typical_rth_place_degree": f"(log(n))^({kappa / density:.12f}+o_Pr(1))",
        "formal_leverage": f"(log(n))^(-{kappa * LOG_BLOCK_GAIN:.12f}+o(1))",
        "typical_net_exponent_after_degree_power_loss": f"{kappa * gain:.12f}",
        "status": (
            "typical-scale net gain, not an averaged bound"
            if gain > 0
            else "no typical-scale net gain"
        ),
    }


def run() -> dict[str, object]:
    power_panels = []
    for density, losses in (
        (0.5, (0.0, 0.025, 0.05, 0.10, 0.12)),
        (1.0, (0.0, 0.05, 0.10, 0.20, 0.24)),
    ):
        power_panels.extend(
            optimized_power_panel(density, loss) for loss in losses
        )
    return {
        "order_statistic": {
            "sublogarithmic_rank": (
                "r->infinity and r=o(log n): "
                "log(d_(r))/r -> 1/delta in probability"
            ),
            "logarithmic_rank": (
                "r=alpha*log(n), 0<alpha<delta: "
                "log(d_(r))/log(n) -> alpha/delta in probability"
            ),
            "tail_scope": (
                "the variance proof gives convergence in probability, "
                "not the polynomial tail needed for an averaged trace exponent"
            ),
            "variance_input": "Var Omega_E(F;D)=delta*log(D)+O_q(1)+o(1)",
        },
        "ambient_abundance": {
            "sublog_rank": "Pr(omega_E(F)<r)<=n^(-delta+o(1))",
            "power_rank": (
                "r=alpha*log(n): Pr(omega_E(F)<r)"
                "<=n^(-c_delta(alpha)+o(1))"
            ),
            "rate": "c_delta(alpha)=delta-alpha+alpha*log(alpha/delta)",
        },
        "universal_threshold": {
            "criterion": "theta<delta*log(5/4)",
            "delta_1_over_2": f"{0.5 * LOG_BLOCK_GAIN:.12f}",
            "delta_1": f"{LOG_BLOCK_GAIN:.12f}",
            "meaning": (
                "both the typical and uniform rich-core ledgers have positive "
                "exponent exactly below this threshold; their optimized "
                "positive-theta exponents differ"
            ),
        },
        "optimized_power_rank_panels": power_panels,
        "sublog_panels": [
            sublog_panel(0.5, 0.0, 1.0),
            sublog_panel(0.5, 0.10, 1.0),
            sublog_panel(1.0, 0.0, 1.0),
            sublog_panel(1.0, 0.20, 1.0),
        ],
        "firewalls": [
            "the order-statistic theorem is for ambient squarefree cores",
            "FFPS-RICH-CARLESON is still needed for the frozen weighted source",
            "the conductor comparison is conditional on a degree^theta trace loss",
            (
                "the alpha*(log(5/4)-theta/delta) power-rank expression is "
                "typical only, not an averaged exponent"
            ),
            (
                "the optimized power panels use the deterministic d_(r)<=n "
                "bound on every rich core"
            ),
            "a relative virtual complex may cancel branches before this loss is paid",
            "none of the phase panels proves CYSEL, individualization, RH, or GRH",
        ],
        "resource_caps": {
            "polynomials_enumerated": 0,
            "closed_places_enumerated": 0,
            "curves_enumerated": 0,
            "power_rank_panels": len(power_panels),
            "bisection_steps_per_live_panel": 160,
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
