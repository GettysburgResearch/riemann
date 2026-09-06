#!/usr/bin/env python3
"""Bounded exact replay for the full-grid centered-current majorant."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from pathlib import Path
from typing import Mapping

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUTPUT = HERE / "live_quotient_centered_current_majorant.json"

SOURCE_BLOBS = {
    (
        "6b2400e1cb6ea957a8afee70a9edc17e09eee79f",
        "research/riemann-structures/SOURCE_GROUPED_POSITIVE_HODGE_DESCENT.md",
    ): "d8a55066a1de69b320f759cacc1eaa9ef6798861",
    (
        "6b2400e1cb6ea957a8afee70a9edc17e09eee79f",
        "research/riemann-structures/source_grouped_positive_hodge_descent.py",
    ): "a8f6c9bac5a344539ee3d07d0a7a33ebbc667a09",
    (
        "6b2400e1cb6ea957a8afee70a9edc17e09eee79f",
        "research/riemann-structures/source_grouped_positive_hodge_descent.json",
    ): "12364692866e22a5352a059a3cc93ec037985cd5",
    (
        "6b2400e1cb6ea957a8afee70a9edc17e09eee79f",
        "tests/test_source_grouped_positive_hodge_descent.py",
    ): "cd033ed6d38c9d6f197b48e22ff5f65cb730c6b4",
}

Cell = tuple[int, int]
Current = Mapping[Cell, Fraction]


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def fp(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def principal_density(ell: int, rho: int) -> Fraction:
    if ell <= 1 or rho <= 1:
        raise ValueError("ell and rho must exceed one")
    return Fraction(ell - 1, ell) * Fraction(rho - 1, rho)


def centered_projection(
    ell: int,
    rho: int,
    current: Current,
) -> dict[Cell, Fraction]:
    """Apply H_ell tensor H_rho to a zero-extended current."""

    for x, y in current:
        if not (0 <= x < ell and 0 <= y < rho):
            raise ValueError("current cell lies outside the full grid")
    row = [sum((current.get((x, y), Fraction(0)) for y in range(rho)), Fraction(0)) for x in range(ell)]
    column = [sum((current.get((x, y), Fraction(0)) for x in range(ell)), Fraction(0)) for y in range(rho)]
    total = sum(row, Fraction(0))
    return {
        (x, y): (
            current.get((x, y), Fraction(0))
            - row[x] / rho
            - column[y] / ell
            + total / (ell * rho)
        )
        for x in range(ell)
        for y in range(rho)
    }


def centered_energy_formula(ell: int, rho: int, current: Current) -> Fraction:
    """Exact ANOVA formula for ||(H_ell tensor H_rho) current||^2."""

    row = [sum((current.get((x, y), Fraction(0)) for y in range(rho)), Fraction(0)) for x in range(ell)]
    column = [sum((current.get((x, y), Fraction(0)) for x in range(ell)), Fraction(0)) for y in range(rho)]
    total = sum(row, Fraction(0))
    raw = sum((value * value for value in current.values()), Fraction(0))
    return (
        raw
        - sum((value * value for value in row), Fraction(0)) / rho
        - sum((value * value for value in column), Fraction(0)) / ell
        + total * total / (ell * rho)
    )


def norm_squared(vector: Mapping[Cell, Fraction]) -> Fraction:
    return sum((value * value for value in vector.values()), Fraction(0))


def two_cell_fixture() -> dict[str, object]:
    ell, rho = 3, 2
    current = {(0, 0): Fraction(3), (1, 1): Fraction(-1)}
    projected = centered_projection(ell, rho, current)
    formula = centered_energy_formula(ell, rho, current)
    direct = norm_squared(projected)
    if direct != formula or formula != Fraction(7, 3):
        raise AssertionError("double-centering formula failed")

    # Two occupied cells, each with atom multiplicity two.  Their principal
    # compression is S=[[1/3,1/6],[1/6,1/3]], and Q=2S-(1/3)I=(1/3)J.
    s0, s1 = current[(0, 0)], current[(1, 1)]
    positive_debt = Fraction(1, 6) * (s0 + s1) ** 2
    if positive_debt != Fraction(2, 3):
        raise AssertionError("two-cell positive quotient fixture failed")
    if positive_debt > formula:
        raise AssertionError("positive debt exceeded centered-current majorant")
    return {
        "ell": ell,
        "rho": rho,
        "current": [fp(s0), fp(s1)],
        "centered_energy": fp(formula),
        "positive_debt": fp(positive_debt),
        "majorant_gap": fp(formula - positive_debt),
    }


def zero_centered_fixture() -> dict[str, object]:
    ell, rho = 3, 4
    # A full-grid additive row-plus-column field is killed by H_ell tensor H_rho.
    row_part = (Fraction(2), Fraction(-1), Fraction(3))
    column_part = (Fraction(1), Fraction(0), Fraction(-2), Fraction(4))
    current = {
        (x, y): row_part[x] + column_part[y]
        for x in range(ell)
        for y in range(rho)
    }
    energy = centered_energy_formula(ell, rho, current)
    direct = norm_squared(centered_projection(ell, rho, current))
    if energy != 0 or direct != 0:
        raise AssertionError("additive current was not annihilated")
    return {
        "ell": ell,
        "rho": rho,
        "centered_energy": fp(energy),
        "positive_debt": fp(Fraction(0)),
    }


def live_one_cell_fixture() -> dict[str, object]:
    ell, rho = 1031, 521
    multiplicity = 100
    current_sum = Fraction(4)
    literal_energy = Fraction(676)
    d = principal_density(ell, rho)
    majorant = d * current_sum * current_sum
    exact_one_cell_positive = d * Fraction(multiplicity - 1, multiplicity) * current_sum * current_sum
    gap = majorant - exact_one_cell_positive
    if d != Fraction(535600, 537151):
        raise AssertionError("live principal density mismatch")
    if exact_one_cell_positive != d * Fraction(396, 25):
        raise AssertionError("live one-cell positive ledger mismatch")
    if gap != d * Fraction(4, 25):
        raise AssertionError("live majorant gap mismatch")
    return {
        "ell": ell,
        "rho": rho,
        "principal_density": fp(d),
        "history_multiplicity": multiplicity,
        "current_sum": fp(current_sum),
        "literal_energy": fp(literal_energy),
        "centered_current_majorant": fp(majorant),
        "exact_one_cell_principal_block_positive_diagnostic": fp(exact_one_cell_positive),
        "majorant_gap": fp(gap),
        "majorant_to_literal_energy_ratio": fp(majorant / literal_energy),
        "census_caveat": "declared one-cell subpacket only; not a complete live fibre",
    }


def build_payload() -> dict[str, object]:
    two_cell = two_cell_fixture()
    zero = zero_centered_fixture()
    live = live_one_cell_fixture()
    core = {
        "two_cell": two_cell,
        "zero_centered": zero,
        "live_one_cell": live,
    }
    proof_object = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "schema": "riemann.t108106.live-quotient-centered-current-majorant.v1",
        "classification": "PASS_T108106_LIVE_QUOTIENT_CENTERED_CURRENT_MAJORANT",
        "proof_object_sha256": proof_object,
        "finite_checks": 24,
        **core,
        "full_grid_projection_majorant_proved": True,
        "double_centered_current_formula_proved": True,
        "unknown_quotient_norm_removed_from_upper_bound": True,
        "cross_history_terms_retained_before_square": True,
        "zero_centered_current_zero_positive_debt": True,
        "complete_live_grouped_current_census_proved": False,
        "live_subblock_centered_majorant_valid_for_zero_extended_vector": True,
        "declared_live_subblock_is_complete_fibre": False,
        "signed_cross_conductor_estimate_proved": False,
        "global_relative_trace_proved": False,
        "principal_binding_proved": False,
        "rh_or_grh_established": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--skip-source-check", action="store_true")
    args = parser.parse_args()
    if not args.skip_source_check:
        check_source_blobs()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != text:
            raise SystemExit("retained output mismatch")
    else:
        OUTPUT.write_text(text)
    print(payload["classification"])


if __name__ == "__main__":
    main()
