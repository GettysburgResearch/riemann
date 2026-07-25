#!/usr/bin/env python3
"""Rigorous python-flint/Arb producer for direct completed-xi modulus witnesses.

Unlike xi'/xi producers, this program never divides by xi and does not reject a
point merely because the completed-xi rectangle contains zero.  It evaluates
one exact dyadic ordinate and a finite set of exact dyadic horizontal offsets,
checks the completed functional equation by a second evaluation at 1-s, and
exports exact rational rectangles consumed by verify_modulus_certificate.py.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
from pathlib import Path
from typing import Any, Sequence

from flint import acb, acb_series, arb, ctx

SCHEMA = "riemann.xi-modulus-witness.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"


class ProducerError(RuntimeError):
    pass


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ProducerError(f"{name} must not be bool")
    try:
        return int(value)
    except (TypeError, ValueError) as exc:
        raise ProducerError(f"{name} must be an integer") from exc


def parse_binary(value: Any, name: str) -> tuple[int, int]:
    if not isinstance(value, dict):
        raise ProducerError(f"{name} must be an object")
    return parse_int(value.get("mantissa"), f"{name}.mantissa"), parse_int(
        value.get("exponent"), f"{name}.exponent"
    )


def exact_arb(value: Any, name: str) -> arb:
    mantissa, exponent = parse_binary(value, name)
    return arb((mantissa, exponent))


def fraction_from_binary(mantissa: int, exponent: int) -> tuple[int, int]:
    if exponent >= 0:
        return mantissa << exponent, 1
    numerator = mantissa
    denominator = 1 << (-exponent)
    while numerator and numerator % 2 == 0:
        numerator //= 2
        denominator //= 2
    return numerator, denominator


def binary_fraction_json(mantissa: int, exponent: int) -> dict[str, int]:
    numerator, denominator = fraction_from_binary(mantissa, exponent)
    return {"numerator": numerator, "denominator": denominator}


def exact_rational_json(value: arb) -> dict[str, int]:
    mantissa, exponent = value.man_exp()
    return binary_fraction_json(int(mantissa), int(exponent))


def arb_interval_rational_json(value: arb) -> dict[str, object]:
    return {
        "lower": exact_rational_json(value.lower()),
        "upper": exact_rational_json(value.upper()),
    }


def acb_rectangle_rational_json(value: acb) -> dict[str, object]:
    return {
        "real": arb_interval_rational_json(value.real),
        "imag": arb_interval_rational_json(value.imag),
    }


def canonical_digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def constant(series: acb_series) -> acb:
    coefficients = series.coeffs()
    return coefficients[0] if coefficients else acb(0)


def completed_xi(s: acb, series_cap: int) -> acb:
    """Evaluate the standard completed xi product as one rigorous acb rectangle."""
    ctx.cap = series_cap
    x = acb_series([s, 1], prec=series_cap)
    zeta = x.zeta()
    gamma = (x / 2).gamma()
    log_pi = arb.pi().log()
    xi = (x * (x - 1) / 2) * (-(x / 2) * log_pi).exp() * gamma * zeta
    return constant(xi)


def point_payload(identifier: str, raw_x: Any, t: arb, series_cap: int) -> dict[str, object]:
    if not identifier:
        raise ProducerError("point ID must be nonempty")
    x_pair = parse_binary(raw_x, f"point {identifier}.x")
    x = exact_arb(raw_x, f"point {identifier}.x")
    if not (x >= 0):
        raise ProducerError("horizontal offsets must be nonnegative")

    s = acb(arb(1) / 2 + x, t)
    direct = completed_xi(s, series_cap)
    reflected = completed_xi(1 - s, series_cap)
    if not direct.overlaps(reflected):
        raise ProducerError(f"functional-equation xi rectangles do not overlap at {identifier}")

    canonical = {
        "id": identifier,
        "x": binary_fraction_json(*x_pair),
        "xi_rectangle": acb_rectangle_rational_json(direct),
    }
    return {
        **canonical,
        "point_sha256": canonical_digest(canonical),
        "functional_equation_reflected_rectangle": acb_rectangle_rational_json(reflected),
        "functional_equation_residual_contains_zero": bool((direct - reflected).contains(0)),
        "relative_accuracy_bits": {
            "xi_direct": int(direct.rel_accuracy_bits()),
            "xi_reflected": int(reflected.rel_accuracy_bits()),
        },
    }


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ProducerError("config root must be an object")
    return value


def build_certificate(config: dict[str, Any]) -> dict[str, object]:
    precision_bits = parse_int(config.get("precision_bits", 192), "precision_bits")
    series_cap = parse_int(config.get("series_cap", 2), "series_cap")
    if precision_bits < 64 or series_cap < 2:
        raise ProducerError("precision_bits>=64 and series_cap>=2 are required")
    ctx.prec = precision_bits
    ctx.cap = series_cap

    raw_t = config.get("ordinate")
    t_pair = parse_binary(raw_t, "ordinate")
    t = exact_arb(raw_t, "ordinate")
    raw_points = config.get("points")
    rows = config.get("rows")
    if not isinstance(raw_points, list) or not raw_points:
        raise ProducerError("points must be a nonempty array")
    if not isinstance(rows, list) or not rows:
        raise ProducerError("rows must be a nonempty array")

    seen: set[str] = set()
    points = []
    for index, raw in enumerate(raw_points):
        if not isinstance(raw, dict):
            raise ProducerError(f"points[{index}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in seen:
            raise ProducerError(f"invalid or duplicate point ID at points[{index}]")
        seen.add(identifier)
        points.append(point_payload(identifier, raw.get("x"), t, series_cap))

    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "classification": "RIEMANN_XI_DIRECTED",
        "normalization_id": NORMALIZATION,
        "ordinate": binary_fraction_json(*t_pair),
        "points": points,
        "rows": rows,
        "producer": {
            "backend": "python-flint/Arb",
            "python_flint_version": importlib.metadata.version("python-flint"),
            "python_version": platform.python_version(),
            "platform": platform.platform(),
            "precision_bits": precision_bits,
            "series_cap": series_cap,
            "formula": "0.5*s*(s-1)*pi^(-s/2)*Gamma(s/2)*zeta(s)",
            "division_by_xi": False,
            "functional_equation_gate": "direct xi(s) overlaps direct xi(1-s)",
        },
    }
    certificate["certificate_sha256"] = canonical_digest(certificate)
    return certificate


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    certificate = build_certificate(load_json(args.config))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "schema": certificate["schema"],
                "point_count": len(certificate["points"]),
                "row_count": len(certificate["rows"]),
                "certificate_sha256": certificate["certificate_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
