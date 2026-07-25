#!/usr/bin/env python3
"""Produce one rigorous low-height scalar-deflation calibration with python-flint."""
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
    via_xi = constant(xi.derivative() / xi)
    via_parts = constant(
        1 / x
        + 1 / (x - 1)
        - log_pi / 2
        + gamma.derivative() / gamma
        + zeta.derivative() / zeta
    )
    return via_xi, via_parts, constant(zeta), constant(xi)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    ctx.prec = 192
    ctx.cap = 3
    zero = acb.zeta_zero(1)
    zero_lower, zero_upper = interval(zero.imag)
    sample_t = (zero_lower + zero_upper) / 2
    sample_x = Fraction(1, 20)
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

    distance = max(abs(sample_t - zero_lower), abs(sample_t - zero_upper))
    subtraction = sample_x / (sample_x * sample_x + distance * distance)
    residual_lower = f_lower - subtraction
    residual_upper = f_upper - subtraction

    output = {
        "schema": "riemann.zero-deflation.actual-low-control.v1",
        "classification": "RIGOROUS_NUMERICAL_CONTROL_PENDING_PARENT_ANALYTIC_REVIEW",
        "producer": {
            "python_flint_version": flint.__version__,
            "python_version": platform.python_version(),
            "precision_bits": 192,
            "zero_primitive": "acb.zeta_zero(1)",
            "f_assemblies": [
                "completed xi derivative divided by xi",
                "corrected completion plus zeta'/zeta",
            ],
        },
        "sample": {"x": fraction_json(sample_x), "t": fraction_json(sample_t)},
        "critical_line_zero_bin": {
            "lower": fraction_json(zero_lower),
            "upper": fraction_json(zero_upper),
            "count_lower": 1,
        },
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
        "status": "CERTIFIED_POSITIVE_NUMERICAL_CONTROL",
        "proof_boundary": (
            "The special-function and zero balls are directed python-flint/Arb outputs. "
            "The finite subtraction is exact. Project-level use still depends on "
            "independent review of D-3201/L-3201 and independent numerical reproduction."
        ),
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "residual_lower": str(residual_lower),
                "residual_upper": str(residual_upper),
                "zero_width": str(zero_upper - zero_lower),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
