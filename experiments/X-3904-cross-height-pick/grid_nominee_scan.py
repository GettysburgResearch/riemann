#!/usr/bin/env python3
"""Replay the frozen 16-point cross-height Pick nominee with Arb."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any, Sequence

from arb_value_producer import build_certificate
from verify_complex_pick_candidate import verify_certificate

X_EXPONENTS = (17, 15, 13, 11, 10, 9, 7, 5)
T_NUMERATORS = (
    20225875608346342631827,
    20225875608346476849555,
)
T_EXPONENT = -32


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain an object")
    return value


def build_config(nominee: dict[str, Any], precision_bits: int) -> dict[str, object]:
    if nominee.get("schema") != "riemann.xi-cross-height-pick-nominee.v1":
        raise ValueError("bad nominee schema")
    point_ids = nominee.get("point_ids")
    real = nominee.get("real_numerators")
    imag = nominee.get("imag_numerators")
    bits = nominee.get("scale_bits")
    if (
        not isinstance(point_ids, list)
        or not isinstance(real, list)
        or not isinstance(imag, list)
        or len(point_ids) != 16
        or len(real) != 16
        or len(imag) != 16
        or isinstance(bits, bool)
        or not isinstance(bits, int)
    ):
        raise ValueError("malformed nominee")
    points: list[dict[str, object]] = []
    expected_ids: list[str] = []
    for row, t_num in enumerate(T_NUMERATORS):
        t_label = "p24" if row == 0 else "p25"
        for exponent in X_EXPONENTS:
            identifier = f"t_{t_label}_x{exponent}"
            expected_ids.append(identifier)
            points.append({
                "id": identifier,
                "x": {"mantissa": "1", "exponent": -exponent},
                "t": {"mantissa": str(t_num), "exponent": T_EXPONENT},
            })
    if point_ids != expected_ids:
        raise ValueError("nominee point order does not match the pre-registered grid")
    vector = {
        "scale_bits": bits,
        "real_numerators": real,
        "imag_numerators": imag,
    }
    channel = {
        "id": "cross-height-grid-nominee",
        "kind": "complex-pick-rayleigh",
        "points": point_ids,
        "vector": vector,
        "source_nomination": {
            "artifact_sha256": nominee["source_artifact_sha256"],
            "source_midpoint_eigenvalue": nominee["source_midpoint_eigenvalue"],
            "vector_canonical_sha256": nominee["canonical_sha256"],
            "frozen_before_replay": True,
        },
    }
    return {
        "precision_bits": precision_bits,
        "series_cap": 3,
        "points": points,
        "channels": [channel],
        "declared_channel_ids": ["cross-height-grid-nominee"],
    }


def fraction_decimal(raw: dict[str, Any]) -> str:
    from fractions import Fraction
    value = Fraction(int(raw["numerator"]), int(raw["denominator"]))
    return format(float(value), ".17g")


def summarize(verification: dict[str, Any], precision_bits: int) -> dict[str, object]:
    channel = verification["channels"][0]
    normalized = channel["normalized_interval"]
    return {
        "schema": "riemann.xi-cross-height-grid-nominee-result.v1",
        "status": verification["status"],
        "precision_bits": precision_bits,
        "point_count": verification["point_count"],
        "channel_id": channel["id"],
        "channel_status": channel["status"],
        "normalized_interval": normalized,
        "normalized_lower_decimal": fraction_decimal(normalized["lower"]),
        "normalized_upper_decimal": fraction_decimal(normalized["upper"]),
        "vector_sha256": channel["vector_sha256"],
        "source_nomination": channel["source_nomination"],
        "counterexample_candidate": None,
        "promotion_boundary": (
            "A negative directed interval is a rigorous nomination only. It must be "
            "independently reproduced and the D-3201/L-3202 normalization reviewed."
        ),
    }


def write(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nominee", type=Path, required=True)
    parser.add_argument("--precision-bits", type=int, default=160)
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--verification", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.precision_bits < 128:
        raise ValueError("precision_bits must be at least 128")
    config = build_config(load(args.nominee), args.precision_bits)
    certificate = build_certificate(config)
    verification = verify_certificate(certificate)
    summary = summarize(verification, args.precision_bits)
    write(args.certificate, certificate)
    write(args.verification, verification)
    write(args.summary, summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
