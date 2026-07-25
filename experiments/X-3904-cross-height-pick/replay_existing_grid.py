#!/usr/bin/env python3
"""Replay a frozen complex Pick vector from an existing rigorous Arb grid artifact."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from verify_complex_pick_candidate import verify_certificate

EXPECTED_PRIMITIVE_SHA = "10025d3c3b50b24f0b39c9981664131644fc58ad0a59fd8606f1d96d9b3e02c2"


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain an object")
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_replay(primitive_path: Path, nominee: dict[str, Any]) -> dict[str, Any]:
    digest = sha256(primitive_path)
    if digest != EXPECTED_PRIMITIVE_SHA:
        raise ValueError(f"primitive artifact digest mismatch: {digest}")
    if nominee.get("source_artifact_sha256") != digest:
        raise ValueError("nominee is not bound to the supplied primitive artifact")
    primitive = load(primitive_path)
    if primitive.get("schema") != "riemann.xi-passivity-value-balls.v1":
        raise ValueError("unexpected primitive certificate schema")
    by_id = {str(point["id"]): point for point in primitive["points"]}
    point_ids = nominee.get("point_ids")
    if not isinstance(point_ids, list) or len(point_ids) < 2:
        raise ValueError("nominee point_ids missing")
    try:
        points = [by_id[str(identifier)] for identifier in point_ids]
    except KeyError as exc:
        raise ValueError("nominee references a missing primitive point") from exc
    vector = {
        "scale_bits": nominee["scale_bits"],
        "real_numerators": nominee["real_numerators"],
        "imag_numerators": nominee["imag_numerators"],
    }
    channel = {
        "id": "cross-height-grid-nominee",
        "kind": "complex-pick-rayleigh",
        "points": point_ids,
        "vector": vector,
        "source_nomination": {
            "artifact_sha256": digest,
            "source_midpoint_eigenvalue": nominee["source_midpoint_eigenvalue"],
            "vector_canonical_sha256": nominee["canonical_sha256"],
            "frozen_before_replay": True,
        },
    }
    return {
        "schema": primitive["schema"],
        "producer": primitive.get("producer"),
        "points": points,
        "channels": [channel],
        "declared_channel_ids": [channel["id"]],
        "classification": "Exact replay from an existing rigorous primitive Arb artifact.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primitive", type=Path, required=True)
    parser.add_argument("--nominee", type=Path, required=True)
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--verification", type=Path, required=True)
    args = parser.parse_args()
    certificate = build_replay(args.primitive, load(args.nominee))
    verification = verify_certificate(certificate)
    args.certificate.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    args.verification.write_text(
        json.dumps(verification, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(verification, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
