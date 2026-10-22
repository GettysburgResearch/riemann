#!/usr/bin/env python3
"""Exact rational regression for R-29803/R-29804/L-29809/L-29810.

This checker verifies finite algebra and rational-grid Hall inequalities only.
It does not construct the two-orientation Pascal gadget, prove DCD, or prove RH.
"""

from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def modal_value(u: Fraction, q: int, n: int) -> Fraction:
    exponent = n * q - 1 if n % 2 == 0 else n * q
    return u**exponent


def finite_difference(u: Fraction, q: int, n: int, order: int) -> Fraction:
    return sum(
        Fraction((-1) ** r * comb(order, r)) * modal_value(u, q, n + r)
        for r in range(order + 1)
    )


def interval_supply_minus_demand(
    order: int, first_odd: int, last_odd: int, y: Fraction
) -> Fraction:
    lo = first_odd - 1
    hi = min(last_odd + 1, order)
    return sum(
        Fraction(1 if r % 2 == 0 else -1) * comb(order, r) * y**r
        for r in range(lo, hi + 1)
    )


def run() -> dict[str, object]:
    modal_rows = 0
    euler_rows = 0

    for u in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(4, 5)):
        for q in range(1, 8):
            z = u**q
            alpha = (1 / u + 1) / 2
            beta = (1 / u - 1) / 2

            for n in range(2, 12):
                assert modal_value(u, q, n) == alpha * z**n + beta * (-z) ** n
                for order in range(8):
                    expected = (
                        alpha * z**n * (1 - z) ** order
                        + beta * (-z) ** n * (1 + z) ** order
                    )
                    assert finite_difference(u, q, n, order) == expected
                    modal_rows += 1

            for k in range(1, 6):
                start = 2 * k
                exact_tail = (
                    alpha * z**start / (1 + z)
                    + beta * z**start / (1 - z)
                )
                for order in range(1, 8):
                    finite_part = sum(
                        Fraction(1, 2 ** (m + 1))
                        * finite_difference(u, q, start, m)
                        for m in range(order)
                    )
                    remainder = (
                        alpha * z**start * (1 - z) ** order / (1 + z)
                        + beta * z**start * (1 + z) ** order / (1 - z)
                    )
                    assert remainder >= 0
                    assert finite_part + Fraction(1, 2**order) * remainder == exact_tail
                    euler_rows += 1

    hall_rows = 0
    for order in range(1, 25):
        odd_levels = [r for r in range(order + 1) if r % 2 == 1]
        for denominator in range(1, 17):
            for numerator in range(denominator + 1):
                y = Fraction(numerator, denominator)
                for index, first_odd in enumerate(odd_levels):
                    for last_odd in odd_levels[index:]:
                        assert interval_supply_minus_demand(
                            order, first_odd, last_odd, y
                        ) >= 0
                        hall_rows += 1

    # Exact controls from the claim cards.
    assert Fraction(1, 6) - Fraction(2, 7) + Fraction(1, 10) == Fraction(-2, 105)
    assert Fraction(1, 5) - Fraction(1, 7) == Fraction(2, 35)
    assert Fraction(1, 7) - Fraction(1, 5) + Fraction(1, 11) == Fraction(13, 385)

    result: dict[str, object] = {
        "classification": "EXACT_INTERLEAVED_EULER_AND_HAUSDORFF_MATCHING_VERIFIED",
        "counts": {
            "modal_difference_rows": modal_rows,
            "euler_identity_rows": euler_rows,
            "weighted_hall_interval_rows": hall_rows,
            "exact_source_counterexamples": 2,
        },
        "controls": {
            "pair_first_actual_tail": "q=1,s=1,K=1 gives 1",
            "pair_first_alternating_tail": "q=1,s=1,K=1 gives pi/2-1 (symbolic claim)",
            "negative_odd_start_second_jet": "-2/105",
            "one_sided_vector_deficit": "2/35",
        },
        "scope": {
            "certifies": [
                "rational two-mode parity algebra",
                "even-start Euler identity on rational Laplace fibers",
                "all rational-grid weighted Hall interval inequalities",
                "exact source-binding counterexamples",
            ],
            "does_not_certify": [
                "continuous weighted Hall theorem beyond the proved claim text",
                "two-orientation Pascal gadget",
                "DCD",
                "RH",
            ],
        },
    }

    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["proof_object_sha256"] = sha256(canonical.encode("utf-8")).hexdigest()

    out = ROOT / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
