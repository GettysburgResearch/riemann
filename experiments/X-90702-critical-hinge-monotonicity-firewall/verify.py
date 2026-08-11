#!/usr/bin/env python3
"""Exact directed replay for L-90702 and R-90701.

The checker:
* verifies the closed top-inverse cone formula on rational targets;
* pulls the T=894 fourth-stage monotonicity functional backwards through the
  exact rational elimination maps;
* encloses every reciprocal square root by integer-square-root rational bounds;
* certifies the negative residual difference and the positive fifth-stage
  coefficient.

It proves no cofinal CHS statement or RH.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
import random
from pathlib import Path

STATUS = "PASS_X_90702_CRITICAL_HINGE_MONOTONICITY_FIREWALL"


def beta(n: int, q: int) -> Fraction:
    if q > n:
        return Fraction(0)
    a, r = divmod(n, q)
    return Fraction(a * (q - 1 - r), n + 1)


def top_inverse(target: list[Fraction], endpoint: int) -> list[Fraction]:
    cut = endpoint // 2
    c = [Fraction(0) for _ in range(endpoint + 1)]
    for q in range(endpoint, cut, -1):
        rhs = target[q]
        for n in range(q + 1, endpoint + 1):
            rhs -= c[n] * beta(n, q)
        c[q] = rhs / beta(q, q)
    return c


def verify_cone_formula() -> int:
    rng = random.Random(90702)
    rows = 0
    for endpoint in range(4, 90):
        cut = endpoint // 2
        for _ in range(12):
            target = [Fraction(0) for _ in range(endpoint + 2)]
            for q in range(2, endpoint + 1):
                target[q] = Fraction(rng.randint(-50, 50), rng.randint(1, 31))
            c = top_inverse(target, endpoint)
            delta = [
                target[q] - target[q + 1] for q in range(endpoint + 1)
            ]
            for q in range(cut + 1, endpoint + 1):
                vtail = sum(
                    (m * delta[m] for m in range(q + 1, endpoint + 1)),
                    Fraction(0),
                )
                lhs = q * (q - 1) * c[q]
                rhs = q * (q + 1) * delta[q] + 2 * vtail
                if lhs != rhs:
                    raise AssertionError(("cone formula", endpoint, q, lhs, rhs))
                value_rhs = (
                    q * (q + 1) * target[q]
                    - (q + 1) * (q - 2) * target[q + 1]
                    + 2 * sum(target[m] for m in range(q + 2, endpoint + 1))
                )
                if lhs != value_rhs:
                    raise AssertionError(("value formula", endpoint, q))
                rows += 1
    return rows


def pullback_residual_functional(
    functional: dict[int, Fraction], endpoint: int
) -> dict[int, Fraction]:
    """Pull l(residual) back to l'(target) exactly."""
    cut = endpoint // 2
    out = {q: value for q, value in functional.items() if value}
    x: dict[int, Fraction] = {}
    for n in range(cut + 1, endpoint + 1):
        value = sum(
            (coef * beta(n, q) for q, coef in functional.items()),
            Fraction(0),
        )
        value -= sum(
            (coef * beta(n, q) for q, coef in x.items()), Fraction(0)
        )
        x[n] = value / beta(n, n)
    for n, value in x.items():
        if value:
            out[n] = -value
    return out


def coefficient_functional(endpoint: int, selected_q: int) -> dict[int, Fraction]:
    """Return the exact target functional producing c(selected_q)."""
    cut = endpoint // 2
    x: dict[int, Fraction] = {}
    for n in range(cut + 1, endpoint + 1):
        value = Fraction(1) if n == selected_q else Fraction(0)
        value -= sum(
            (coef * beta(n, q) for q, coef in x.items()), Fraction(0)
        )
        x[n] = value / beta(n, n)
    return {q: value for q, value in x.items() if value}


def invsqrt_bounds(n: int, digits: int = 60) -> tuple[Fraction, Fraction]:
    scale = 10**digits
    floor_value = math.isqrt((scale * scale) // n)
    if not (
        floor_value * floor_value * n <= scale * scale
        < (floor_value + 1) * (floor_value + 1) * n
    ):
        raise AssertionError(("sqrt enclosure", n))
    low = Fraction(floor_value, scale)
    high = low if floor_value * floor_value * n == scale * scale else Fraction(
        floor_value + 1, scale
    )
    return low, high


def evaluate_hinge_functional(
    coefficients: dict[int, Fraction], endpoint: int, digits: int = 60
) -> tuple[Fraction, Fraction]:
    low = Fraction(0)
    high = Fraction(0)
    for q, coefficient in coefficients.items():
        lo, hi = invsqrt_bounds(q, digits)
        if coefficient >= 0:
            low += coefficient * lo
            high += coefficient * hi
        else:
            low += coefficient * hi
            high += coefficient * lo

    total_coefficient = sum(coefficients.values(), Fraction(0))
    lo, hi = invsqrt_bounds(endpoint, digits)
    coefficient = -total_coefficient
    if coefficient >= 0:
        low += coefficient * lo
        high += coefficient * hi
    else:
        low += coefficient * hi
        high += coefficient * lo
    return low, high


def decimal_string(value: Fraction, digits: int = 30) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    integer = value.numerator // value.denominator
    remainder = value.numerator % value.denominator
    out = [sign + str(integer), "."]
    for _ in range(digits):
        remainder *= 10
        out.append(str(remainder // value.denominator))
        remainder %= value.denominator
    return "".join(out)


def main() -> dict[str, object]:
    gates: dict[str, bool] = {}
    cone_rows = verify_cone_formula()
    gates["exact_top_inverse_cone"] = cone_rows > 10000

    # h4(28)-h4(29), pulled backwards through E=111,223,447,894.
    residual_functional = {28: Fraction(1), 29: Fraction(-1)}
    for endpoint in [111, 223, 447, 894]:
        residual_functional = pullback_residual_functional(
            residual_functional, endpoint
        )
    residual_interval = evaluate_hinge_functional(residual_functional, 894)
    gates["fourth_residual_increases"] = residual_interval[1] < 0

    # c5(28): coefficient solve at E=55, then pull through prior residual maps.
    coefficient = coefficient_functional(55, 28)
    for endpoint in [111, 223, 447, 894]:
        coefficient = pullback_residual_functional(coefficient, endpoint)
    coefficient_interval = evaluate_hinge_functional(coefficient, 894)
    gates["fifth_stage_coefficient_positive"] = coefficient_interval[0] > 0

    # The margins are deliberately much larger than enclosure widths.
    gates["directed_margin"] = (
        residual_interval[1] < Fraction(-4, 10**6)
        and coefficient_interval[0] > Fraction(6, 1000)
    )

    if not all(gates.values()):
        raise AssertionError([name for name, ok in gates.items() if not ok])

    residual_serial = ";".join(
        f"{q}:{c.numerator}/{c.denominator}"
        for q, c in sorted(residual_functional.items())
    ).encode()
    coefficient_serial = ";".join(
        f"{q}:{c.numerator}/{c.denominator}"
        for q, c in sorted(coefficient.items())
    ).encode()

    result = {
        "status": STATUS,
        "gates": gates,
        "cone_formula_rows": cone_rows,
        "witness": {
            "T": 894,
            "endpoints": [894, 447, 223, 111, 55],
            "residual_difference": {
                "quantity": "h4(28)-h4(29)",
                "lower": decimal_string(residual_interval[0], 40),
                "upper": decimal_string(residual_interval[1], 40),
                "functional_terms": len(residual_functional),
                "functional_sha256": hashlib.sha256(residual_serial).hexdigest(),
            },
            "next_coefficient": {
                "quantity": "c5(28)",
                "lower": decimal_string(coefficient_interval[0], 40),
                "upper": decimal_string(coefficient_interval[1], 40),
                "functional_terms": len(coefficient),
                "functional_sha256": hashlib.sha256(coefficient_serial).hexdigest(),
            },
            "radical_denominator": "10^60",
        },
        "scope": (
            "exact finite cone and counterexample only; CHS, average-carry "
            "positivity and RH remain open"
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    return result


if __name__ == "__main__":
    result = main()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(STATUS)
