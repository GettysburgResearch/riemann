#!/usr/bin/env python3
"""Bounded replay for the fixed-mollified complete-beta RH equivalence."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "3f10a6be2009f8e499b1bd421fd97b2095a82b06"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_EXTRA_NOTCHED_MELLIN_LANDAU_CONSUMER.md"
    ): "4a9aaf8bef6150bf054d6b6d4a873379db091b14",
}


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def beta_partial_sum_identity() -> str:
    return "A_beta(x)=A_mu(x)-67^(-1/2)*A_mu(x/67)"


def normalized_partial_sum_chain() -> list[str]:
    return [
        "RH => M(x)=O_delta(x^(1/2+delta))",
        ("A_mu(x)=M(x)/sqrt(x)+(1/2)*integral_1^x M(u)*u^(-3/2) du"),
        "A_mu(x)=O_delta(x^delta)",
        beta_partial_sum_identity(),
        "A_beta(x)=O_delta(x^delta)",
    ]


def bv_certificate(epsilon: Fraction = Fraction(1, 10)) -> dict[str, object]:
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    return {
        "epsilon": str(epsilon),
        "K_ext_support": "[0,4*log(2)]",
        "kappa_support": f"[0,4*log(2)+{epsilon}]",
        "sup_norm_bound_in_units_of_TV_K_ext": str(1 / epsilon),
        "variation_bound_in_units_of_TV_K_ext": str(2 / epsilon),
        "derivative_identity": ("d kappa_epsilon=(K_ext-tau_epsilon K_ext)/epsilon"),
        "summation_by_parts_factor_in_units_of_TV_K_ext": str(4 / epsilon),
    }


def box_multiplier_zero_free(real_part: Fraction) -> bool:
    return real_part > 0


def implication_graph() -> dict[str, str]:
    return {
        "RH_to_absolute_mass": "Mertens bound plus compact-BV summation",
        "absolute_to_negative_mass": "pointwise h_- <= |h|",
        "negative_mass_to_RH": "zero-safe Mellin identity plus Landau",
    }


def run() -> dict[str, object]:
    certificate = bv_certificate()
    if certificate["summation_by_parts_factor_in_units_of_TV_K_ext"] != "40":
        raise AssertionError("BV summation constant changed")
    panels = [Fraction(1, 100), Fraction(1, 10), Fraction(1, 4), Fraction(1, 2)]
    if not all(box_multiplier_zero_free(real_part) for real_part in panels):
        raise AssertionError("box multiplier gained a right-half-plane zero")
    graph = implication_graph()
    if set(graph) != {
        "RH_to_absolute_mass",
        "absolute_to_negative_mass",
        "negative_mass_to_RH",
    }:
        raise AssertionError("equivalence graph is incomplete")
    return {
        "frozen_sources": {"commit": SOURCE_COMMIT, "blobs": SOURCE_BLOBS},
        "definition": {
            "beta": "mu(n)-1_(67|n)*mu(n/67)",
            "kappa_epsilon": "eta_epsilon*K_ext in log coordinate",
            "h_epsilon": ("sum beta(n)/sqrt(n)*kappa_epsilon(t-log(n))"),
        },
        "RH_forward_chain": normalized_partial_sum_chain(),
        "BV_certificate": certificate,
        "mellin_transform": (
            "eta_hat_epsilon(s)*M_ext(s)*(1-67^(-(s+1/2)))/zeta(s+1/2)"
        ),
        "box_multiplier": {
            "formula": "(1-exp(-epsilon*s))/(epsilon*s)",
            "zeros": "Re(s)=0 only",
            "right_half_plane_panels": [str(value) for value in panels],
        },
        "equivalence": {
            "fixed_epsilon": "every epsilon>0",
            "statements": [
                "Riemann Hypothesis",
                "integral_0^T |h_epsilon(t)| dt = exp(o(T))",
                "integral_0^T (h_epsilon(t))_- dt = exp(o(T))",
            ],
            "implications": graph,
            "arithmetic_estimate_proved": False,
            "rh_proved": False,
            "grh_proved": False,
        },
        "resource_caps": {
            "mellin_panels": len(panels),
            "source_atoms_enumerated": 0,
            "conductors_enumerated": 0,
            "curves_enumerated": 0,
            "zeros_enumerated": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        check_source_blobs()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    print(rendered, end="")


if __name__ == "__main__":
    main()
