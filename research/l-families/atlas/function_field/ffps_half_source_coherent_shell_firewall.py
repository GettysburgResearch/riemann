#!/usr/bin/env python3
"""Bounded exponent replay for the coherent half-source shell firewall."""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
HALF_SOURCE_PATH = HERE / "ffps_boolean_half_source_diagonal_gain.py"
SPEC = importlib.util.spec_from_file_location("half_source_gain", HALF_SOURCE_PATH)
assert SPEC and SPEC.loader
half_source_gain = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(half_source_gain)

OWNER_SCALE_EXPONENT = Fraction(1)
CORE_SCALE_EXPONENT = Fraction(2)
FINAL_HORIZON_EXPONENT = Fraction(10)


def disjoint_ordered_fraction(owner_count: int, core_count: int) -> Fraction:
    if owner_count < 2 or core_count < 2:
        raise ValueError("both label sets need at least two elements")
    return Fraction(owner_count - 1, owner_count) * Fraction(core_count - 1, core_count)


def scale_ledger() -> dict[str, Fraction]:
    half_product = OWNER_SCALE_EXPONENT + 2 * CORE_SCALE_EXPONENT
    atom_count = OWNER_SCALE_EXPONENT + CORE_SCALE_EXPONENT
    coefficient = OWNER_SCALE_EXPONENT / 2 + CORE_SCALE_EXPONENT
    diagonal = atom_count - 2 * coefficient
    coherent_square = 2 * (atom_count - coefficient)
    gap = coherent_square - diagonal
    return {
        "cutoff": FINAL_HORIZON_EXPONENT / 6,
        "half_product": half_product,
        "two_half_product": 2 * half_product,
        "atom_count": atom_count,
        "coefficient_decay": coefficient,
        "source_diagonal": diagonal,
        "coherent_square": coherent_square,
        "coherent_to_diagonal_gap": gap,
    }


def run() -> dict[str, object]:
    ledger = scale_ledger()
    epsilon = Fraction(1, 100)
    ratio = (1 + epsilon) ** 6
    if ratio >= 8:
        raise AssertionError("fixture must fit in the ratio-eight window")
    rough_singleton = half_source_gain.recombined_half_source((103,), 39)
    if rough_singleton != -1:
        raise AssertionError("rough singleton half-source sign changed")
    return {
        "scale_fixture": {
            "final_horizon": "Y=Z^10",
            "owner_primes": "p in [Z,(1+epsilon)Z]",
            "half_core_primes": "a in [Z^2,(1+epsilon)Z^2]",
            "vaughan_cutoff": "U=floor(Z^(5/3))",
            "half_products": "p*a^2 asymp Z^5=sqrt(Y)",
            "two_half_products": "asymp Z^10=Y",
            "epsilon": str(epsilon),
            "two_half_product_ratio_bound": str(ratio),
            "inside_ratio_eight": ratio < 8,
            "rough_half_source_coefficient": str(rough_singleton),
        },
        "asymptotic_ledger_in_Z": {key: str(value) for key, value in ledger.items()},
        "asymptotic_ledger_in_Y": {
            key: str(value / FINAL_HORIZON_EXPONENT) for key, value in ledger.items()
        },
        "logarithmic_scales": {
            "atom_count": "N_Z asymp Z^3/(log Z)^2",
            "source_diagonal": "D_Z asymp Z^(-2)/(log Z)^2",
            "coherent_positive_square": "C_Z asymp Z/(log Z)^4",
            "ratio": "C_Z/D_Z asymp Z^3/(log Z)^2 asymp N_Z",
        },
        "wick_disjointness_panels": [
            {
                "owner_count": owner_count,
                "core_count": core_count,
                "surviving_ordered_fraction": str(
                    disjoint_ordered_fraction(owner_count, core_count)
                ),
            }
            for owner_count, core_count in ((2, 3), (5, 11), (101, 1009))
        ],
        "scope": {
            "refutes": (
                "uniform diagonal-to-positive-local-observation bounds with "
                "Y^o(1) loss based only on injectivity, ratio-eight support, "
                "and Wick disjointness"
            ),
            "does_not_refute": (
                "the signed native differential/reflection kernel after full "
                "source recombination"
            ),
        },
        "resource_caps": {
            "prime_intervals_enumerated": 0,
            "source_atoms_enumerated": 0,
            "maximum_integer_panel_count": 1009,
            "curves_enumerated": 0,
            "point_counts": 0,
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
