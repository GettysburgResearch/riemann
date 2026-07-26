#!/usr/bin/env python3
"""Directed direct completed-xi producer for X-9703 configured slab nodes.

At the configured support-scaled nodes, Re(s)>1.  The producer evaluates the
standard completed-xi product directly and never divides by xi or locates a
zero.
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

CONFIG_SCHEMA = "riemann.x9703-certified-slab-configs.v1"
OUTPUT_SCHEMA = "riemann.x9703-count-only-primitives.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"


class ProducerError(RuntimeError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ProducerError(f"{name} must be an integer")
    return value


def rational(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise ProducerError(f"{name} must be an object")
    numerator = integer(value.get("numerator"), f"{name}.numerator")
    denominator = integer(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise ProducerError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def exact_arb(value: Fraction) -> arb:
    result = arb(value.numerator) / arb(value.denominator)
    if not result.is_exact():
        raise ProducerError(f"rational {value} was not represented exactly")
    return result


def binary_fraction(value: arb) -> Fraction:
    mantissa, exponent = value.man_exp()
    mantissa = int(mantissa)
    exponent = int(exponent)
    return (
        Fraction(mantissa << exponent, 1)
        if exponent >= 0
        else Fraction(mantissa, 1 << (-exponent))
    )


def arb_interval(value: arb) -> dict[str, object]:
    return {"lower": fj(binary_fraction(value.lower())), "upper": fj(binary_fraction(value.upper()))}


def acb_rectangle(value: acb) -> dict[str, object]:
    return {"real": arb_interval(value.real), "imag": arb_interval(value.imag)}


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


def load_config(path: Path, slab_id: str) -> tuple[dict[str, Any], list[Fraction]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema") != CONFIG_SCHEMA:
        raise ProducerError("configuration schema mismatch")
    raw_slabs = data.get("slabs")
    raw_alphas = data.get("alphas")
    if not isinstance(raw_slabs, list) or not isinstance(raw_alphas, list):
        raise ProducerError("configuration needs slabs and alphas arrays")
    matches = [row for row in raw_slabs if isinstance(row, dict) and row.get("id") == slab_id]
    if len(matches) != 1:
        raise ProducerError(f"slab id {slab_id!r} is missing or duplicated")
    alphas = sorted(
        {rational(raw, f"alphas[{index}]") for index, raw in enumerate(raw_alphas)}
    )
    if len(alphas) < 3 or any(alpha <= 0 for alpha in alphas):
        raise ProducerError("at least three positive distinct alpha values are required")
    return matches[0], alphas


def build(
    slab: dict[str, Any],
    alphas: list[Fraction],
    precision: int,
    series_cap: int,
) -> dict[str, Any]:
    if precision < 96 or series_cap < 2:
        raise ProducerError("precision>=96 and series_cap>=2 are required")
    lower = rational(slab.get("lower"), "slab.lower")
    upper = rational(slab.get("upper"), "slab.upper")
    target = rational(slab.get("target"), "slab.target")
    declared_count = integer(slab.get("total_count"), "slab.total_count")
    if not lower < target < upper or declared_count < 0:
        raise ProducerError("invalid slab geometry or count")
    support_gap = min((target - lower) ** 2, (upper - target) ** 2)

    ctx.prec = precision
    ctx.cap = series_cap
    target_arb = exact_arb(target)
    points: list[dict[str, Any]] = []
    for index, alpha in enumerate(alphas):
        u_fraction = alpha * support_gap
        u = exact_arb(u_fraction)
        x = u.sqrt()
        if not (x > 0):
            raise ProducerError("support-scaled square root is not positive")
        s = acb(arb(1) / 2 + x, target_arb)
        if not (s.real > 1):
            raise ProducerError("configured node is not in the absolutely convergent half-plane")
        xi = completed_xi(s, series_cap)
        if xi.rel_accuracy_bits() < 20:
            raise ProducerError(
                f"insufficient completed-xi accuracy at alpha={alpha}: "
                f"{xi.rel_accuracy_bits()} bits"
            )
        identifier = f"a-{index:02d}"
        canonical = {
            "id": identifier,
            "u": fj(u_fraction),
            "xi_rectangle": acb_rectangle(xi),
        }
        points.append(
            {
                **canonical,
                "alpha": fj(alpha),
                "x_interval": arb_interval(x),
                "point_sha256": canonical_sha(canonical),
                "relative_accuracy_bits": int(xi.rel_accuracy_bits()),
            }
        )

    output: dict[str, Any] = {
        "schema": OUTPUT_SCHEMA,
        "classification": "RIEMANN_XI_DIRECTED",
        "normalization_id": NORMALIZATION,
        "slab_id": slab.get("id"),
        "slab": {"lower": fj(lower), "upper": fj(upper)},
        "target": fj(target),
        "declared_total_count": declared_count,
        "support_gap": fj(support_gap),
        "points": points,
        "producer": {
            "backend": "python-flint/Arb",
            "python_flint_version": importlib.metadata.version("python-flint"),
            "python_version": platform.python_version(),
            "platform": platform.platform(),
            "precision_bits": precision,
            "series_cap": series_cap,
            "formula": "0.5*s*(s-1)*pi^(-s/2)*Gamma(s/2)*zeta(s)",
            "division_by_xi": False,
            "zero_location": False,
            "node_rule": "u=alpha*min((T-a)^2,(b-T)^2)",
        },
    }
    output["certificate_sha256"] = canonical_sha(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    parser.add_argument("--slab-id", required=True)
    parser.add_argument("--precision", type=int, default=192)
    parser.add_argument("--series-cap", type=int, default=2)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    slab, alphas = load_config(args.config, args.slab_id)
    result = build(slab, alphas, args.precision, args.series_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "slab_id": args.slab_id,
                "precision_bits": args.precision,
                "point_count": len(result["points"]),
                "minimum_accuracy_bits": min(
                    point["relative_accuracy_bits"] for point in result["points"]
                ),
                "certificate_sha256": result["certificate_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
