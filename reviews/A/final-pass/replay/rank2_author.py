#!/usr/bin/env python3
"""Exact symbolic verifier for the two-factor CTI105655 packet.

This script proves only the n=2 Cauchy translation trace inequality.  It does
not test or prove arbitrary packet rank, cofinal Xi passage, POINTID105630, or
RH.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

A, B, D, H, U, P, R = sp.symbols(
    "A B D H U P R", positive=True, real=True
)
I = sp.I
lam = [A, B + I * D]


def gram(multiplier: int) -> sp.Matrix:
    shift = multiplier * H
    return sp.Matrix(
        [
            [
                1
                / (
                    sp.conjugate(lam[i])
                    + lam[j]
                    + shift
                )
                for j in range(2)
            ]
            for i in range(2)
        ]
    )


def even_polynomial_to_u(poly: sp.Expr) -> sp.Expr:
    source = sp.Poly(sp.expand(poly), D)
    target = sp.Integer(0)
    for (degree,), coefficient in source.terms():
        if degree % 2:
            raise AssertionError(
                f"unexpected odd horizontal-separation degree {degree}"
            )
        target += coefficient * U ** (degree // 2)
    return sp.expand(target)


def coefficientwise_nonnegative(
    expression: sp.Expr,
) -> tuple[bool, int]:
    polynomial = sp.Poly(sp.expand(expression), P, R, U, H)
    coefficients = polynomial.coeffs()
    return all(c >= 0 for c in coefficients), len(polynomial.terms())


def main() -> None:
    g0, g1, g2, g4 = gram(0), gram(1), gram(2), gram(4)

    overlap = sp.trace(g0.inv() * g2 * g4.inv() * g2)
    current = sp.trace(g0.inv() * g1)
    difference = sp.factor(
        sp.together(sp.simplify(sp.re(overlap - current)))
    )

    numerator, denominator = sp.fraction(difference)
    numerator_u = even_polynomial_to_u(numerator)
    denominator_u = even_polynomial_to_u(denominator)

    numerator_symmetric = sp.symmetrize(
        numerator_u, [A, B], formal=True
    )
    denominator_symmetric = sp.symmetrize(
        denominator_u, [A, B], formal=True
    )

    if numerator_symmetric[1] != 0:
        raise AssertionError("numerator is not symmetric in the two depths")
    if denominator_symmetric[1] != 0:
        raise AssertionError("denominator is not symmetric in the two depths")

    elementary_num = numerator_symmetric[2]
    elementary_den = denominator_symmetric[2]

    numerator_pr = numerator_symmetric[0].subs(
        {elementary_num[0]: P, elementary_num[1]: R}
    )
    denominator_pr = denominator_symmetric[0].subs(
        {elementary_den[0]: P, elementary_den[1]: R}
    )

    denominator_poly = sp.Poly(
        sp.expand(denominator_pr), P, R, U, H
    )
    if all(c <= 0 for c in denominator_poly.coeffs()):
        numerator_pr = -numerator_pr
        denominator_pr = -denominator_pr

    numerator_ok, numerator_terms = coefficientwise_nonnegative(
        numerator_pr
    )
    denominator_ok, denominator_terms = coefficientwise_nonnegative(
        denominator_pr
    )

    if not numerator_ok:
        raise AssertionError(
            "cleared CTI numerator is not coefficientwise nonnegative"
        )
    if not denominator_ok:
        raise AssertionError(
            "cleared CTI denominator is not coefficientwise nonnegative"
        )
    if sp.Poly(numerator_pr, P, R, U, H).is_zero:
        raise AssertionError("CTI difference vanished identically")

    fixtures = [
        (sp.Rational(1), sp.Rational(2), sp.Rational(0), sp.Rational(1)),
        (sp.Rational(1), sp.Rational(3), sp.Rational(2), sp.Rational(1)),
        (sp.Rational(2), sp.Rational(5), sp.Rational(7), sp.Rational(3, 2)),
        (sp.Rational(1, 3), sp.Rational(5, 4), sp.Rational(4, 3), sp.Rational(2)),
    ]
    fixture_values = []
    for a, b, d, h in fixtures:
        value = sp.factor(
            difference.subs({A: a, B: b, D: d, H: h})
        )
        if value <= 0:
            raise AssertionError(
                f"strict fixture failed at {(a, b, d, h)}: {value}"
            )
        fixture_values.append(str(value))

    result = {
        "verdict": "PASS_X_105659_RANK_TWO_CAUCHY_TRACE",
        "arithmetic_class": "EXACT_SYMBOLIC_RATIONAL",
        "packet_rank": 2,
        "numerator_coefficientwise_nonnegative": True,
        "denominator_coefficientwise_nonnegative": True,
        "numerator_terms": numerator_terms,
        "denominator_terms": denominator_terms,
        "strict_fixture_values": fixture_values,
        "general_packet_cti_proved": False,
        "cofinal_xi_transfer_proved": False,
        "pointwise_physical_sign_proved": False,
        "rh_established": False,
    }

    output = Path(__file__).parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(result["verdict"])


if __name__ == "__main__":
    main()
