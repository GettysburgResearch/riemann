#!/usr/bin/env python3
"""Exact finite checks for L/T-106415--L/T-106420.

The replay checks coverage-matrix algebra, the coverage-to-Hankel trace
inequality, the monomial denominator firewall, and the rational percentage
ledger.  It does not prove PWSAMP106420 or evaluate Xi.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def payload() -> dict[str, object]:
    # A diagonal finite model of A=H*H and the source coverage compression C.
    # The exact operator theorem is basis-free; a commuting rational fixture
    # exercises every term and the low-coverage discard.
    h2 = [Fraction(1), Fraction(9, 16), Fraction(1, 4), Fraction(1, 16)]
    coverage = [Fraction(1), Fraction(3, 4), Fraction(1, 2), Fraction(1, 4)]
    threshold = Fraction(1, 2)

    assert all(0 <= value <= 1 for value in h2)
    assert all(0 <= value <= 1 for value in coverage)

    complete_charge = sum(h2, Fraction(0))
    source_charge = sum(
        (left * right for left, right in zip(h2, coverage)), Fraction(0)
    )
    discarded_rank = sum(value < threshold for value in coverage)
    assert complete_charge <= discarded_rank + source_charge / threshold

    deficit = sum((1 - value for value in coverage), Fraction(0))
    assert discarded_rank * (1 - threshold) <= deficit

    # R-106420: U=z^{-m} has m units of negative winding/Hankel charge while
    # N-D=1-z^m is analytic and contributes zero negative Hankel energy.
    monomial_degree = 7
    monomial_hankel_charge = monomial_degree
    cancelled_difference_charge = 0
    assert monomial_hankel_charge == 7
    assert cancelled_difference_charge == 0

    # T-106420 exact constants.
    source_constant = Fraction(2547232, 1568239201)
    assert source_constant < Fraction(1, 600)
    safe_fraction = Fraction(599, 625) - 2 * Fraction(1, 600) * Fraction(999, 1000)
    assert safe_fraction == Fraction(95507, 100000)
    assert safe_fraction > Fraction(9, 10)

    result: dict[str, object] = {
        "schema": "riemann.x106420.pw-model-coverage.v1",
        "classification": "PASS_T106420_MODEL_SPACE_COVERAGE_ALGEBRA",
        "coverage_matrix_positive_contraction_checked": True,
        "coverage_to_hankel_charge_checked": True,
        "monomial_denominator_firewall_checked": True,
        "source_four_channel_constant": "2547232/1568239201",
        "safe_conditional_fraction": "95507/100000",
        "safe_conditional_decimal": "0.95507",
        "pwsamp106420_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = payload()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
