#!/usr/bin/env python3
"""Produce a rigorous scalar-deflation control from total critical-strip zero counts."""
from __future__ import annotations

import argparse
import json
import platform
from fractions import Fraction
from pathlib import Path

import flint
from flint import acb, acb_series, arb, ctx


def frac(value: arb) -> Fraction:
    mantissa, exponent = value.man_exp()
    mantissa = int(mantissa)
    exponent = int(exponent)
    return Fraction(mantissa << exponent, 1) if exponent >= 0 else Fraction(mantissa, 1 << (-exponent))


def interval(value: arb) -> tuple[Fraction, Fraction]:
    return frac(value.lower()), frac(value.upper())


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def interval_json(value: arb) -> dict[str, dict[str, str]]:
    lower, upper = interval(value)
    return {"lower": fraction_json(lower), "upper": fraction_json(upper)}


def complex_json(value: acb) -> dict[str, object]:
    return {"real": interval_json(value.real), "imag": interval_json(value.imag)}


def constant(series: acb_series) -> acb:
    coefficients = series.coeffs()
    return coefficients[0] if coefficients else acb(0)


def assemblies(s: acb) -> tuple[acb, acb, acb, acb]:
    x = acb_series([s, 1], prec=3)
    zeta = x.zeta()
    gamma = (x / 2).gamma()
    log_pi = arb.pi().log()
    xi = (x * (x - 1) / 2) * (-(x / 2) * log_pi).exp() * gamma * zeta
    return (
        constant(xi.derivative() / xi),
        constant(
            1 / x
            + 1 / (x - 1)
            - log_pi / 2
            + gamma.derivative() / gamma
            + zeta.derivative() / zeta
        ),
        constant(zeta),
        constant(xi),
    )


def exact_count(t: Fraction) -> tuple[int, tuple[Fraction, Fraction]]:
    value = (arb(t.numerator) / t.denominator).zeta_nzeros()
    lower, upper = interval(value)
    if lower != upper or lower.denominator != 1:
        raise RuntimeError("zero count is not an exact integer")
    return lower.numerator, (lower, upper)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 192
    ctx.cap = 3

    lower_t = Fraction(1413, 100)
    upper_t = Fraction(707, 50)
    sample_t = (lower_t + upper_t) / 2
    sample_x = Fraction(1, 20)
    lower_count, lower_ball = exact_count(lower_t)
    upper_count, upper_ball = exact_count(upper_t)
    count_difference = upper_count - lower_count
    if count_difference <= 0:
        raise RuntimeError("empty slab count")

    lower_zeta = acb(arb(1) / 2, arb(lower_t.numerator) / lower_t.denominator).zeta()
    upper_zeta = acb(arb(1) / 2, arb(upper_t.numerator) / upper_t.denominator).zeta()
    if not (lower_zeta.abs_lower() > 0 and upper_zeta.abs_lower() > 0):
        raise RuntimeError("endpoint zeta ball touches zero")

    s = acb(
        arb(1) / 2 + arb(sample_x.numerator) / sample_x.denominator,
        arb(sample_t.numerator) / sample_t.denominator,
    )
    via_xi, via_parts, zeta, xi = assemblies(s)
    xi_lower, xi_upper = interval(via_xi.real)
    parts_lower, parts_upper = interval(via_parts.real)
    f_lower, f_upper = max(xi_lower, parts_lower), min(xi_upper, parts_upper)
    if f_lower > f_upper:
        raise RuntimeError("disjoint F assemblies")

    distance = max(abs(sample_t - lower_t), abs(sample_t - upper_t))
    subtraction = count_difference * sample_x / (sample_x * sample_x + distance * distance)
    residual_lower, residual_upper = f_lower - subtraction, f_upper - subtraction

    output = {
        "schema": "riemann.zero-deflation.actual-slab-control.v1",
        "classification": "RIGOROUS_NUMERICAL_CONTROL_PENDING_PARENT_ANALYTIC_REVIEW",
        "producer": {
            "python_flint_version": flint.__version__,
            "python_version": platform.python_version(),
            "precision_bits": 192,
            "count_primitive": "arb.zeta_nzeros at exact rational endpoints",
            "f_assemblies": [
                "completed xi derivative divided by xi",
                "corrected completion plus zeta prime over zeta",
            ],
        },
        "slab": {
            "lower": fraction_json(lower_t),
            "upper": fraction_json(upper_t),
            "N_lower": lower_count,
            "N_upper": upper_count,
            "count_difference": count_difference,
            "N_lower_ball": {
                "lower": fraction_json(lower_ball[0]),
                "upper": fraction_json(lower_ball[1]),
            },
            "N_upper_ball": {
                "lower": fraction_json(upper_ball[0]),
                "upper": fraction_json(upper_ball[1]),
            },
            "endpoint_zeta_abs_lower": [
                fraction_json(frac(lower_zeta.abs_lower())),
                fraction_json(frac(upper_zeta.abs_lower())),
            ],
        },
        "sample": {"x": fraction_json(sample_x), "t": fraction_json(sample_t)},
        "f_via_xi": complex_json(via_xi),
        "f_via_parts": complex_json(via_parts),
        "f_real_intersection": {
            "lower": fraction_json(f_lower),
            "upper": fraction_json(f_upper),
        },
        "zeta_abs_lower": fraction_json(frac(zeta.abs_lower())),
        "xi_abs_lower": fraction_json(frac(xi.abs_lower())),
        "subtracted_poisson_lower": fraction_json(subtraction),
        "residual_interval": {
            "lower": fraction_json(residual_lower),
            "upper": fraction_json(residual_upper),
        },
        "status": "CERTIFIED_POSITIVE_SLAB_COUNT_CONTROL",
        "proof_boundary": (
            "The total nontrivial-zero count difference and special-function balls are "
            "directed python-flint/Arb outputs. L-8405 converts the count to line mass "
            "only under the RH assumption. Project-level use still needs parent analytic "
            "review and independent numerical reproduction."
        ),
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "count": count_difference,
                "residual_lower": str(residual_lower),
                "residual_upper": str(residual_upper),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
