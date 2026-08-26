#!/usr/bin/env python3
"""Exact replay for the selector Young-lattice propagation obstruction."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MIN_DEGREE = 5
MAX_DEGREE = 256
REPLAY_DEGREES = (5, 8, 10, 16, 32, 64, 128, 256)

SOURCE_COMMITS = {
    "6d9e66033c1a00066935cceed9ca66b76b67fd99": {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_DERANGEMENT_SELECTOR_FINITE_L1_OPTIMIZATION.md"
        ): "602742ff6bafa9a9cbb4f563129feaad74e0184d",
        (
            "research/l-families/atlas/function_field/"
            "ffps_derangement_selector_finite_l1_optimization.py"
        ): "bf46f94efecb76eca788d6597eac8a2995dba00f",
        (
            "research/l-families/atlas/function_field/"
            "ffps_derangement_selector_finite_l1_optimization.json"
        ): "4c3bb43266e10d0e99d259f093664992f38130c5",
        "tests/test_ffps_derangement_selector_finite_l1_optimization.py": (
            "125a3e4dccb66070eb791f083944094106cfb952"
        ),
    },
    "0909baac5": {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_DERANGEMENT_SELECTOR_TANH_CALIBRATION.md"
        ): "079657d1768a91f73c3188994571161bfce15dd5",
        (
            "research/l-families/atlas/function_field/"
            "ffps_derangement_selector_tanh_calibration.py"
        ): "0c60db0f6c0c4714f79807edeb517c4a1c166cb1",
        (
            "research/l-families/atlas/function_field/"
            "ffps_derangement_selector_tanh_calibration.json"
        ): "7f34e0aa461b327f75f7858ac46c296a7dfc55a0",
        "tests/test_ffps_derangement_selector_tanh_calibration.py": (
            "f29f3842f2439dd3f644f4b7886deaa3425ccb96"
        ),
    },
}


def check_source_blobs() -> None:
    """Authenticate the exact theorem packets used as input."""

    for commit, blobs in SOURCE_COMMITS.items():
        for path, expected in blobs.items():
            completed = subprocess.run(
                ["git", "rev-parse", f"{commit}:{path}"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=2,
            )
            if completed.stdout.strip() != expected:
                raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def validate_degree(degree: int) -> None:
    if (
        isinstance(degree, bool)
        or not isinstance(degree, int)
        or not MIN_DEGREE <= degree <= MAX_DEGREE
    ):
        raise ValueError(f"degree must lie in [{MIN_DEGREE},{MAX_DEGREE}]")


def validate_chain_index(degree: int, index: int) -> None:
    validate_degree(degree)
    maximum = (degree - 1) // 2
    if (
        isinstance(index, bool)
        or not isinstance(index, int)
        or not 1 <= index <= maximum
    ):
        raise ValueError(f"chain index must lie in [1,{maximum}]")


def cycle_dual_mass(degree: int) -> Fraction:
    validate_degree(degree)
    return Fraction(2 ** (degree - 1), degree)


def first_two_row_potential(degree: int) -> Fraction:
    """The hook-forced value x_(d-2,1)."""

    validate_degree(degree)
    return Fraction(2**degree, degree) - degree


def hook_predecessor_potential(degree: int, depth: int) -> Fraction:
    validate_degree(degree)
    if (
        isinstance(depth, bool)
        or not isinstance(depth, int)
        or not 0 <= depth <= degree - 2
    ):
        raise ValueError(f"hook depth must lie in [0,{degree - 2}]")
    partial = sum(math.comb(degree - 1, index) for index in range(depth + 1))
    return (-1) ** depth * (partial - (depth + 1) * cycle_dual_mass(degree))


def two_row_dimension(degree: int, index: int) -> int:
    validate_chain_index(degree, index)
    return math.comb(degree, index) - math.comb(degree, index - 1)


def signed_forced_lower_bound(degree: int, index: int) -> Fraction:
    """Lower bound on (-1)^(j-1) X_j."""

    validate_chain_index(degree, index)
    return Fraction(2**degree, degree) - math.comb(degree, index)


def forced_depth(degree: int) -> int:
    """Largest two-row index with a strictly positive forced bound."""

    validate_degree(degree)
    return max(
        index
        for index in range(1, (degree - 1) // 2 + 1)
        if signed_forced_lower_bound(degree, index) > 0
    )


def verify_degree(degree: int) -> dict[str, object]:
    validate_degree(degree)
    depth = forced_depth(degree)
    maximum = (degree - 1) // 2
    x_one = first_two_row_potential(degree)
    if hook_predecessor_potential(degree, 1) != x_one:
        raise AssertionError("hook recurrence does not reproduce X_1")

    running = x_one
    for index in range(1, maximum + 1):
        if index > 1:
            running -= two_row_dimension(degree, index)
        expected = signed_forced_lower_bound(degree, index)
        if running != expected:
            raise AssertionError("two-row dimension telescope failed")

    if not all(
        signed_forced_lower_bound(degree, index) > 0 for index in range(1, depth + 1)
    ):
        raise AssertionError("positive forced range is not contiguous")
    if depth < maximum and signed_forced_lower_bound(degree, depth + 1) > 0:
        raise AssertionError("reported forced depth is not maximal")

    return {
        "degree": degree,
        "cycle_dual_mass": str(cycle_dual_mass(degree)),
        "first_two_row_potential": str(x_one),
        "forced_depth": depth,
        "maximum_two_row_index": maximum,
        "last_positive_signed_lower_bound": str(
            signed_forced_lower_bound(degree, depth)
        ),
        "first_nonpositive_index": depth + 1 if depth < maximum else None,
        "first_nonpositive_signed_lower_bound": (
            str(signed_forced_lower_bound(degree, depth + 1))
            if depth < maximum
            else None
        ),
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    panels = [verify_degree(degree) for degree in REPLAY_DEGREES]
    for degree in range(MIN_DEGREE, MAX_DEGREE + 1):
        verify_degree(degree)
    return {
        "theorem": {
            "signed_bound": "(-1)^(j-1) X_j >= 2^d/d - binom(d,j)",
            "forced_depth": ("m_d=max{j<=floor((d-1)/2): binom(d,j)<2^d/d}"),
            "asymptotic_depth": ("d/2-(1/2+o(1))*sqrt(d*log(d))"),
            "status": "necessary condition for every contractive optimal lift",
        },
        "scope": {
            "constructive_lift_proved": False,
            "all_degree_optimum_proved": False,
            "linear_programming_used": False,
            "floating_point_used": False,
            "maximum_replay_degree": MAX_DEGREE,
        },
        "panels": panels,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="run exact checks")
    parser.add_argument("--write", action="store_true", help="refresh canonical JSON")
    args = parser.parse_args()
    payload = run(check_sources=True)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    output = HERE / "ffps_selector_young_lattice_propagation_obstruction.json"
    if args.write:
        output.write_text(rendered, encoding="utf-8")
    elif args.check:
        if output.read_text(encoding="utf-8") != rendered:
            raise RuntimeError("canonical JSON is stale; run with --write")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
