#!/usr/bin/env python3
"""Rigorous python-flint/Arb producer for xi'/xi passivity certificates.

All input coordinates are exact dyadic numbers. At each point this producer
constructs ``F = xi'/xi`` in two rigorous ways from one ``acb_series``:

1. differentiate the completed xi product and divide by xi;
2. assemble the corrected completion terms plus zeta'/zeta.

The exact checker intersects the two rectangles, verifies the direct
functional-equation control, reconstructs every witness coefficient, and
decides every strict sign. This producer never labels a counterexample by
itself.
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

SCHEMA = "riemann.xi-passivity-balls.v1"


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


def binary_fraction_json(mantissa: int, exponent: int) -> dict[str, str]:
    if exponent >= 0:
        numerator = mantissa << exponent
        denominator = 1
    else:
        numerator = mantissa
        denominator = 1 << (-exponent)
        while numerator and numerator % 2 == 0:
            numerator //= 2
            denominator //= 2
    return {"numerator": str(numerator), "denominator": str(denominator)}


def exact_binary_json(value: arb) -> dict[str, str | int]:
    mantissa, exponent = value.man_exp()
    return {"mantissa": str(int(mantissa)), "exponent": int(exponent)}


def arb_interval_json(value: arb) -> dict[str, object]:
    return {
        "lower": exact_binary_json(value.lower()),
        "upper": exact_binary_json(value.upper()),
    }


def acb_rectangle_json(value: acb) -> dict[str, object]:
    return {"real": arb_interval_json(value.real), "imag": arb_interval_json(value.imag)}


def canonical_digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def constant(series: acb_series) -> acb:
    coefficients = series.coeffs()
    return coefficients[0] if coefficients else acb(0)


def evaluate_assemblies(s: acb, series_cap: int) -> dict[str, acb | arb]:
    """Return two rigorous F assemblies and denominator lower bounds."""
    ctx.cap = series_cap
    x = acb_series([s, 1], prec=series_cap)
    zeta = x.zeta()
    gamma = (x / 2).gamma()
    log_pi = arb.pi().log()

    xi = (x * (x - 1) / 2) * (-(x / 2) * log_pi).exp() * gamma * zeta
    xi0 = constant(xi)
    if not (xi0.abs_lower() > 0):
        raise ProducerError("completed xi denominator ball contains zero")
    via_xi = constant(xi.derivative() / xi)

    zeta0 = constant(zeta)
    if not (zeta0.abs_lower() > 0):
        raise ProducerError("zeta denominator ball contains zero")
    via_parts = constant(
        1 / x
        + 1 / (x - 1)
        - log_pi / 2
        + gamma.derivative() / gamma
        + zeta.derivative() / zeta
    )
    if not via_xi.overlaps(via_parts):
        raise ProducerError("completed-xi and termwise F rectangles do not overlap")
    return {
        "f_via_xi": via_xi,
        "f_via_parts": via_parts,
        "zeta": zeta0,
        "xi": xi0,
        "zeta_abs_lower": zeta0.abs_lower(),
        "xi_abs_lower": xi0.abs_lower(),
    }


def point_payload(raw: dict[str, Any], series_cap: int) -> dict[str, object]:
    identifier = raw.get("id")
    if not isinstance(identifier, str) or not identifier:
        raise ProducerError("point ID must be a nonempty string")
    x_pair = parse_binary(raw.get("x"), f"point {identifier}.x")
    t_pair = parse_binary(raw.get("t"), f"point {identifier}.t")
    x = exact_arb(raw.get("x"), f"point {identifier}.x")
    t = exact_arb(raw.get("t"), f"point {identifier}.t")
    if not (x > 0):
        raise ProducerError("every point must have x>0")

    s = acb(arb(1) / 2 + x, t)
    direct = evaluate_assemblies(s, series_cap)
    payload: dict[str, object] = {
        "id": identifier,
        "x": binary_fraction_json(*x_pair),
        "t": binary_fraction_json(*t_pair),
        "f_via_xi": acb_rectangle_json(direct["f_via_xi"]),
        "f_via_parts": acb_rectangle_json(direct["f_via_parts"]),
        "zeta_abs_lower": exact_binary_json(direct["zeta_abs_lower"]),
        "xi_abs_lower_diagnostic": exact_binary_json(direct["xi_abs_lower"]),
        "relative_accuracy_bits": {
            "f_via_xi": int(direct["f_via_xi"].rel_accuracy_bits()),
            "f_via_parts": int(direct["f_via_parts"].rel_accuracy_bits()),
            "zeta": int(direct["zeta"].rel_accuracy_bits()),
        },
    }

    reflected_s = 1 - s
    reflected = evaluate_assemblies(reflected_s, series_cap)
    payload["reflected"] = {
        "x": binary_fraction_json(-x_pair[0], x_pair[1]),
        "t": binary_fraction_json(-t_pair[0], t_pair[1]),
        "f_via_xi": acb_rectangle_json(reflected["f_via_xi"]),
        "f_via_parts": acb_rectangle_json(reflected["f_via_parts"]),
        "zeta_abs_lower": exact_binary_json(reflected["zeta_abs_lower"]),
        "xi_abs_lower_diagnostic": exact_binary_json(reflected["xi_abs_lower"]),
    }
    residual = direct["f_via_xi"] + reflected["f_via_xi"]
    if not residual.contains(0):
        raise ProducerError("functional-equation residual does not contain zero")
    return payload


def build_certificate(config: dict[str, Any]) -> dict[str, object]:
    precision_bits = parse_int(config.get("precision_bits", 192), "precision_bits")
    series_cap = parse_int(config.get("series_cap", 3), "series_cap")
    if precision_bits < 64 or series_cap < 2:
        raise ProducerError("precision_bits>=64 and series_cap>=2 are required")
    ctx.prec = precision_bits
    ctx.cap = series_cap

    raw_points = config.get("points")
    channels = config.get("channels")
    declared = config.get("declared_channel_ids")
    if not isinstance(raw_points, list) or not isinstance(channels, list):
        raise ProducerError("config points and channels must be arrays")
    if not isinstance(declared, list):
        raise ProducerError("declared_channel_ids must be an array")

    points = [point_payload(raw, series_cap) for raw in raw_points]
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "producer": {
            "backend": "python-flint/Arb",
            "python_flint_version": importlib.metadata.version("python-flint"),
            "python_version": platform.python_version(),
            "platform": platform.platform(),
            "precision_bits": precision_bits,
            "series_cap": series_cap,
            "assembly_gate": (
                "intersection of completed-xi differentiation and corrected termwise "
                "completion plus zeta'/zeta"
            ),
            "functional_equation_gate": "direct F(s)+F(1-s) rectangle contains zero",
        },
        "points": points,
        "channels": channels,
        "declared_channel_ids": declared,
        "classification": (
            "Primitive directed-ball production only. The exact checker reconstructs "
            "all contractions and sign classifications."
        ),
    }
    certificate["certificate_sha256"] = canonical_digest(certificate)
    return certificate


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ProducerError("config root must be an object")
    return value


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
                "channel_count": len(certificate["channels"]),
                "certificate_sha256": certificate["certificate_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
