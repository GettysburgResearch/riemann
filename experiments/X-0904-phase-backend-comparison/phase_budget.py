#!/usr/bin/env python3
"""Phase-survival budgets for D-0801 complete-prime Toeplitz matrices."""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path


def uniform_phase_budget(margin: float, correction_budget: float, absolute_weight: float) -> float:
    if not all(math.isfinite(x) for x in (margin, correction_budget, absolute_weight)):
        raise ValueError("all inputs must be finite")
    if margin <= correction_budget or correction_budget < 0 or absolute_weight <= 0:
        raise ValueError("require margin > correction_budget >= 0 and positive weight")
    return (margin - correction_budget) / absolute_weight


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = {
        "experiment_id": "X-0904",
        "status": "EMPIRICAL_NOT_CERTIFIED",
        "frozen_vector_c1e10": {
            "leading_margin": 0.0006076603725748697,
            "uniform_exact_correction_bound": 4.424813255620086e-10,
            "absolute_phase_weight_sum": 493.7546104558693,
        },
        "complete_c1e8_backend_comparison": {
            "cutoff": 100000000,
            "K": 1024,
            "carrier": "4709203636353.65",
            "prime_count": 5761455,
            "prime_power_count": 5762859,
            "long_double_kahan_margin": 0.006643092728329414,
            "binary128_phase_kahan_margin": 0.006641474117036417,
            "margin_shift": -1.618611292997007e-06,
            "toeplitz_operator_difference": 8.045041107820625e-06,
            "coefficient_l1_difference": 0.000177962465138,
            "maximum_coefficient_difference": 1.08501790986e-06,
        },
        "counterexample_candidate": None,
        "warning": (
            "Binary128 and Kahan arithmetic are independent higher-precision "
            "empirical checks, not directed balls."
        ),
    }
    frozen = data["frozen_vector_c1e10"]
    frozen["required_uniform_phase_radius"] = uniform_phase_budget(
        frozen["leading_margin"],
        frozen["uniform_exact_correction_bound"],
        frozen["absolute_phase_weight_sum"],
    )
    text = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
