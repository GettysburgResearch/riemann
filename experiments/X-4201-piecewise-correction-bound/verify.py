#!/usr/bin/env python3
"""Exact rational checker for the O-4201 correction-scale gate.

The checker does not evaluate the prime matrix, an eigenvalue, log, pi,
hyperbolic functions, or an oscillatory integral. It reconstructs conservative
rational upper bounds implied by L-4202 and L-4203 from elementary parameter
inequalities. The PR #44 leading margin remains explicitly empirical.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.piecewise-correction-bound.v1"
EXPECTED_C = 10**11
EXPECTED_K = 1024
EXPECTED_T = Fraction(94184072727073, 20)  # exact decimal 4709203636353.65
EXPECTED_MARGIN = Fraction(5379325285446157, 20_000_000_000_000_000_000)


class CertificateError(ValueError):
    """Raised for malformed or unsupported correction certificates."""


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must be an integer, not bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), f"{name}.numerator")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def parse_decimal_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, str):
        raise CertificateError(f"{name} must be an exact decimal string")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"{name} is not an exact finite decimal") from exc


def harmonic(index: int) -> Fraction:
    if index < 0:
        raise CertificateError("harmonic index must be nonnegative")
    return sum((Fraction(1, term) for term in range(1, index + 1)), Fraction(0))


def exp_partial(base: Fraction, degree: int) -> Fraction:
    if degree < 0:
        raise CertificateError("exponential partial degree must be nonnegative")
    return sum(
        (base**term / math.factorial(term) for term in range(degree + 1)),
        Fraction(0),
    )


def verify_certificate(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    if data.get("kind") != "optimized-carrier-nonprime-operator-gate":
        raise CertificateError("unsupported certificate kind")

    c = parse_int(data.get("c"), "c")
    k_cells = parse_int(data.get("K"), "K")
    carrier = parse_decimal_fraction(data.get("T_decimal"), "T_decimal")
    reported_margin = parse_decimal_fraction(
        data.get("reported_leading_margin_decimal"),
        "reported_leading_margin_decimal",
    )

    if c != EXPECTED_C:
        raise CertificateError(f"this certificate supports c={EXPECTED_C} exactly")
    if k_cells != EXPECTED_K:
        raise CertificateError(f"this certificate supports K={EXPECTED_K} exactly")
    if carrier != EXPECTED_T:
        raise CertificateError("carrier decimal does not match the committed exact rational")
    if reported_margin != EXPECTED_MARGIN:
        raise CertificateError("reported leading margin string does not match PR #44 data")
    if data.get("margin_classification") != "EMPIRICAL_ORDINARY_FLOATING_ONLY":
        raise CertificateError("the leading margin must remain explicitly empirical")

    claimed = data.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError("claimed must be an object")

    # Elementary enclosure for L=11*log(10).
    log_lower = Fraction(22)
    log_upper = Fraction(638, 25)
    exponential_control = exp_partial(Fraction(58, 25), 6)
    expected_control = Fraction(110699859859, 10986328125)
    if exponential_control != expected_control or exponential_control <= 10:
        raise AssertionError("exact exponential partial control failed")

    b_upper = 2 * log_upper / k_cells
    if b_upper >= Fraction(1, 20):
        raise CertificateError("small-cell condition b<1/20 was not proved")

    # L-4202 with the safe substitutions L>22 and pi>3.
    harmonic_value = harmonic(k_cells - 2)
    inverse_b_upper = Fraction(k_cells, 1) / (2 * log_lower)
    arch_upper = (
        (Fraction(5) + 2 * harmonic_value) * inverse_b_upper
        + 2 * (k_cells - 1)
        + Fraction(1, 4)
    ) / (3 * carrier)

    # L-4203 with deliberately coarse elementary bounds:
    # sinh(L/2)<sqrt(c)/2<160000, cosh^2(pi*h/2)<4,
    # pi^2*h=pi*L/(2K)>3*22/(2K), sinh(pi*h)>pi*h>22/(2K).
    pole_upper = Fraction(2 * 160_000 * 4, 1) / (
        Fraction(3 * 22, 2 * k_cells)
        * Fraction(22, 2 * k_cells)
        * carrier**2
    )
    total_upper = arch_upper + pole_upper

    arch_threshold = parse_fraction(claimed.get("arch_upper_threshold"), "claimed.arch_upper_threshold")
    pole_threshold = parse_fraction(claimed.get("pole_upper_threshold"), "claimed.pole_upper_threshold")
    total_threshold = parse_fraction(claimed.get("total_upper_threshold"), "claimed.total_upper_threshold")
    margin_lower = parse_fraction(claimed.get("empirical_margin_lower"), "claimed.empirical_margin_lower")
    scale_factor = parse_int(claimed.get("minimum_scale_factor"), "claimed.minimum_scale_factor")

    if arch_upper >= arch_threshold:
        raise CertificateError("claimed archimedean threshold is not proved")
    if pole_upper >= pole_threshold:
        raise CertificateError("claimed pole threshold is not proved")
    if total_upper >= total_threshold:
        raise CertificateError("claimed total correction threshold is not proved")
    if reported_margin <= margin_lower:
        raise CertificateError("reported empirical margin does not exceed claimed lower scale")
    if margin_lower / total_threshold < scale_factor:
        raise CertificateError("claimed scale factor is not implied by safe thresholds")

    status = "RIGOROUS_CORRECTION_BOUND_EMPIRICAL_MARGIN_ONLY"
    if claimed.get("status") != status:
        raise CertificateError("claimed status mismatch")

    return {
        "schema": SCHEMA,
        "status": status,
        "parameters": {
            "c": str(c),
            "K": k_cells,
            "T": fraction_json(carrier),
        },
        "log_c_bounds": {
            "lower": fraction_json(log_lower),
            "upper": fraction_json(log_upper),
            "exp_58_over_25_partial_degree_6": fraction_json(exponential_control),
        },
        "b_upper": fraction_json(b_upper),
        "harmonic_index": k_cells - 2,
        "harmonic_value": fraction_json(harmonic_value),
        "archimedean_operator_upper": fraction_json(arch_upper),
        "pole_operator_upper": fraction_json(pole_upper),
        "combined_operator_upper": fraction_json(total_upper),
        "proved_thresholds": {
            "archimedean": fraction_json(arch_threshold),
            "pole": fraction_json(pole_threshold),
            "combined": fraction_json(total_threshold),
        },
        "reported_margin": {
            "classification": "EMPIRICAL_ORDINARY_FLOATING_ONLY",
            "exact_decimal_fraction": fraction_json(reported_margin),
            "proved_only_as_string_greater_than": fraction_json(margin_lower),
        },
        "minimum_scale_factor": scale_factor,
        "proof_boundary": (
            "the nonprime operator envelope is rigorous conditional on L-4202/L-4203; "
            "the PR #44 leading margin is not a directed enclosure"
        ),
    }


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot read certificate: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError("certificate root must be an object")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args(argv)
    try:
        result = verify_certificate(load_json(args.certificate))
    except CertificateError as exc:
        print(
            json.dumps(
                {"schema": SCHEMA, "status": "REJECTED", "reason": str(exc)},
                sort_keys=True,
            )
        )
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
