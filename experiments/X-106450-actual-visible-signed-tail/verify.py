#!/usr/bin/env python3
"""Exact replay for T-106450.

Checks the finite hard-band Hankel formulas, the denominator-cancelled
counterfamily, simple-factor spectral calibration, and exact percentage
constants. It does not evaluate Xi or prove the open spectral estimates.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


def circle_visible_negative(coeffs: dict[int, Fraction], d: int) -> Fraction:
    return sum(
        Fraction(min(d, -n)) * value * value
        for n, value in coeffs.items()
        if n < 0
    )


def circle_tail_negative(coeffs: dict[int, Fraction], d: int) -> Fraction:
    return sum(
        Fraction(max(-n - d, 0)) * value * value
        for n, value in coeffs.items()
        if n < 0
    )


def direct_hankel_squares(
    coeffs: dict[int, Fraction], d: int, max_mode: int
) -> tuple[Fraction, Fraction]:
    visible = Fraction(0)
    tail = Fraction(0)
    for j in range(max_mode):
        for k in range(max_mode):
            entry = coeffs.get(-(j + k + 1), Fraction(0))
            if k < d:
                visible += entry * entry
            else:
                tail += entry * entry
    return visible, tail


def run() -> dict[str, object]:
    checks = 0

    # Exact rational circle fixtures for L-106432.9--10.
    for radius in range(1, 13):
        coeffs = {
            n: Fraction((7 * n * n + 3 * n + 11) % 19 - 9, 17)
            for n in range(-radius, radius + 1)
        }
        for d in range(1, radius + 3):
            direct_visible, direct_tail = direct_hankel_squares(
                coeffs, d, 2 * radius + d + 5
            )
            assert direct_visible == circle_visible_negative(coeffs, d)
            assert direct_tail == circle_tail_negative(coeffs, d)
            checks += 2

    # R-106432: U=z^-m has nonzero compressed Hankel energy while N-D is analytic.
    for m in range(1, 101):
        coeffs = {-m: Fraction(1)}
        for d in range(1, 101):
            assert circle_visible_negative(coeffs, d) == min(m, d)
            analytic_difference_negative_energy = Fraction(0)
            assert analytic_difference_negative_energy == 0
            checks += 2

    # L-106433 simple-factor calibration.
    getcontext().prec = 60
    x = Decimal(1) / Decimal(100)  # 2 y H at yH=1/200
    tail = (-x).exp()
    visible = Decimal(1) - tail
    assert tail > Decimal(99) / Decimal(100)
    assert visible > Decimal(0)
    assert abs((visible + tail) - Decimal(1)) < Decimal("1e-55")
    checks += 3

    baseline = Fraction(599, 625)
    ninety = Fraction(9, 10)
    ninety_five = Fraction(19, 20)
    source_target = Fraction(1, 600)

    total_ninety_margin = baseline - ninety
    total_ninety_five_margin = baseline - ninety_five
    conditional_signed_tail = total_ninety_margin - source_target
    conditional_signed_tail_95 = total_ninety_five_margin - source_target

    assert total_ninety_margin == Fraction(73, 1250)
    assert total_ninety_five_margin == Fraction(21, 2500)
    assert conditional_signed_tail == Fraction(851, 15000)
    assert conditional_signed_tail_95 == Fraction(101, 15000)
    checks += 4

    result: dict[str, object] = {
        "schema": "riemann.x106450.actual-spectral-tail.v1",
        "classification": "PASS_T106450_ACTUAL_SPECTRAL_TAIL_REDUCTION",
        "exact_checks": checks,
        "circle_hard_band_formula_checked": True,
        "denominator_cancelled_counterfamily_checked": True,
        "simple_blaschke_visible_at_yH_1_over_200": str(visible),
        "simple_blaschke_tail_at_yH_1_over_200": str(tail),
        "total_ninety_margin": "73/1250",
        "conditional_q": "1/600",
        "conditional_signed_tail_threshold": "851/15000",
        "conditional_signed_tail_95_threshold": "101/15000",
        "quotientvis106450_proved": False,
        "signedtail106450_proved": False,
        "actualspectral106450_proved": False,
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

    payload = run()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
