#!/usr/bin/env python3
"""Directed python-flint producer for PR71 support-scale completed-xi values.

Unlike the microscopic horizontal table, these nodes satisfy u=alpha*A with
alpha>=1/8 and A about 398.5, so Re(s)=1/2+sqrt(u)>7.5.  The producer still uses
the standard completed-xi product and performs a functional-equation overlap
check, but it does not divide by xi or use a numerical zero locator.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import acb, acb_series, arb, ctx

SCHEMA = "riemann.x9305-support-scale-primitives.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
T = Fraction(20225875608341108140435, 2**32)
SLAB_LOWER = Fraction(75347258181331, 16)
SLAB_UPPER = Fraction(37673629090985, 8)
SUPPORT_GAP = min((T - SLAB_LOWER) ** 2, (SLAB_UPPER - T) ** 2)
ALPHAS = (
    Fraction(1, 8),
    Fraction(3, 16),
    Fraction(1, 4),
    Fraction(3, 8),
    Fraction(1, 2),
    Fraction(3, 4),
    Fraction(1, 1),
    Fraction(3, 2),
    Fraction(2, 1),
    Fraction(3, 1),
    Fraction(4, 1),
    Fraction(6, 1),
    Fraction(8, 1),
    Fraction(12, 1),
    Fraction(16, 1),
)


class ProducerError(RuntimeError):
    pass


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def exact_arb(value: Fraction) -> arb:
    result = arb(value.numerator) / arb(value.denominator)
    if not result.is_exact():
        raise ProducerError(f"rational {value} did not survive as an exact arb")
    return result


def fraction_from_binary(mantissa: int, exponent: int) -> Fraction:
    return (
        Fraction(mantissa << exponent, 1)
        if exponent >= 0
        else Fraction(mantissa, 1 << (-exponent))
    )


def exact_rational_json(value: arb) -> dict[str, int]:
    mantissa, exponent = value.man_exp()
    return fraction_json(fraction_from_binary(int(mantissa), int(exponent)))


def arb_interval_json(value: arb) -> dict[str, object]:
    return {
        "lower": exact_rational_json(value.lower()),
        "upper": exact_rational_json(value.upper()),
    }


def acb_rectangle_json(value: acb) -> dict[str, object]:
    return {
        "real": arb_interval_json(value.real),
        "imag": arb_interval_json(value.imag),
    }


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def constant(series: acb_series) -> acb:
    coefficients = series.coeffs()
    return coefficients[0] if coefficients else acb(0)


def completed_xi(s: acb, series_cap: int) -> acb:
    ctx.cap = series_cap
    variable = acb_series([s, 1], prec=series_cap)
    zeta = variable.zeta()
    gamma = (variable / 2).gamma()
    log_pi = arb.pi().log()
    xi = (
        (variable * (variable - 1) / 2)
        * (-(variable / 2) * log_pi).exp()
        * gamma
        * zeta
    )
    return constant(xi)


def point_payload(
    index: int,
    alpha: Fraction,
    target: arb,
    series_cap: int,
) -> dict[str, Any]:
    u_fraction = alpha * SUPPORT_GAP
    u = exact_arb(u_fraction)
    x = u.sqrt()
    if not (x > 0):
        raise ProducerError("support-scale square root is not strictly positive")
    s = acb(arb(1) / 2 + x, target)
    direct = completed_xi(s, series_cap)
    reflected = completed_xi(1 - s, series_cap)
    if not direct.overlaps(reflected):
        raise ProducerError(
            f"functional-equation rectangles do not overlap at alpha={alpha}"
        )
    if direct.rel_accuracy_bits() < 20:
        raise ProducerError(
            f"insufficient completed-xi accuracy at alpha={alpha}: "
            f"{direct.rel_accuracy_bits()} bits"
        )

    identifier = f"a-{index:02d}"
    canonical = {
        "id": identifier,
        "alpha": fraction_json(alpha),
        "u": fraction_json(u_fraction),
        "x_interval": arb_interval_json(x),
        "xi_rectangle": acb_rectangle_json(direct),
    }
    return {
        **canonical,
        "point_sha256": canonical_sha(canonical),
        "functional_equation_reflected_rectangle": acb_rectangle_json(reflected),
        "functional_equation_residual_contains_zero": bool(
            (direct - reflected).contains(0)
        ),
        "relative_accuracy_bits": {
            "xi_direct": int(direct.rel_accuracy_bits()),
            "xi_reflected": int(reflected.rel_accuracy_bits()),
        },
    }


def build(precision_bits: int, series_cap: int) -> dict[str, Any]:
    if precision_bits < 96 or series_cap < 2:
        raise ProducerError("precision_bits>=96 and series_cap>=2 are required")
    ctx.prec = precision_bits
    ctx.cap = series_cap
    target = exact_arb(T)
    points = [
        point_payload(index, alpha, target, series_cap)
        for index, alpha in enumerate(ALPHAS)
    ]
    certificate: dict[str, Any] = {
        "schema": SCHEMA,
        "classification": "RIEMANN_XI_DIRECTED",
        "normalization_id": NORMALIZATION,
        "ordinate": fraction_json(T),
        "slab": {
            "lower": fraction_json(SLAB_LOWER),
            "upper": fraction_json(SLAB_UPPER),
        },
        "support_gap": fraction_json(SUPPORT_GAP),
        "points": points,
        "producer": {
            "backend": "python-flint/Arb",
            "python_flint_version": importlib.metadata.version("python-flint"),
            "python_version": platform.python_version(),
            "platform": platform.platform(),
            "precision_bits": precision_bits,
            "series_cap": series_cap,
            "formula": "0.5*s*(s-1)*pi^(-s/2)*Gamma(s/2)*zeta(s)",
            "division_by_xi": False,
            "node_rule": "u=alpha*A, x=sqrt(u), A=min((T-a)^2,(b-T)^2)",
            "functional_equation_gate": "direct xi(s) overlaps direct xi(1-s)",
        },
    }
    certificate["certificate_sha256"] = canonical_sha(certificate)
    return certificate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=192)
    parser.add_argument("--series-cap", type=int, default=2)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    certificate = build(args.precision, args.series_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "schema": certificate["schema"],
                "precision_bits": args.precision,
                "point_count": len(certificate["points"]),
                "minimum_direct_accuracy_bits": min(
                    point["relative_accuracy_bits"]["xi_direct"]
                    for point in certificate["points"]
                ),
                "certificate_sha256": certificate["certificate_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
