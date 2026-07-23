#!/usr/bin/env python3
"""Rigorous one-jet producer for high-height xi'/xi value certificates.

Unlike the stronger low-height control producer, this path does not reevaluate
``F(1-s)`` at every search point.  It retains the two rigorous assemblies and
the zeta-denominator exclusion at each exact right-half-plane point.  The full
functional-equation gate is exercised separately by the low-control artifact.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
from pathlib import Path
from typing import Any, Sequence

from flint import acb, arb, ctx

from arb_producer import (
    ProducerError,
    acb_rectangle_json,
    binary_fraction_json,
    evaluate_assemblies,
    exact_arb,
    exact_binary_json,
    parse_binary,
    parse_int,
)

SCHEMA = "riemann.xi-passivity-value-balls.v1"


def canonical_digest(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


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
    return {
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


def build_certificate(config: dict[str, Any]) -> dict[str, object]:
    precision_bits = parse_int(config.get("precision_bits", 128), "precision_bits")
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
                "completed-xi differentiation and corrected termwise completion "
                "plus zeta'/zeta overlap at every point"
            ),
            "functional_equation_control": (
                "not repeated per high point; exercised by low-control certificate"
            ),
        },
        "points": [point_payload(raw, series_cap) for raw in raw_points],
        "channels": channels,
        "declared_channel_ids": declared,
        "classification": (
            "High-height primitive directed balls; exact checker reconstructs signs."
        ),
    }
    certificate["certificate_sha256"] = canonical_digest(certificate)
    return certificate


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    config = json.loads(args.config.read_text(encoding="utf-8"))
    if not isinstance(config, dict):
        raise ProducerError("config root must be an object")
    certificate = build_certificate(config)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
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
