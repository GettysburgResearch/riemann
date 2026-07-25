#!/usr/bin/env python3
"""Build an X-7501 certificate from X-2813/X-6511 target artifacts."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

OUT_SCHEMA = "riemann.toeplitz-box-spectral-closure.v1"


def parse_ratio(text: str) -> Fraction:
    if "/" in text:
        numerator, denominator = text.split("/", 1)
        return Fraction(int(numerator), int(denominator))
    return Fraction(int(text), 1)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: root must be an object")
    return value


def vector_from_document(document: dict[str, Any]) -> list[dict[str, object]]:
    if document.get("schema") != "riemann.piecewise-carrier-vector.v1":
        raise ValueError("bad vector schema")
    raw = document.get("vector")
    if not isinstance(raw, dict):
        raise ValueError("vector missing")
    bits = int(raw["scale_bits"])
    denominator = 1 << bits
    real = raw["real_numerators"]
    imag = raw["imag_numerators"]
    if (
        not isinstance(real, list)
        or not isinstance(imag, list)
        or len(real) != len(imag)
    ):
        raise ValueError("bad vector arrays")
    return [
        {
            "real": fraction_json(Fraction(int(real_part), denominator)),
            "imag": fraction_json(Fraction(int(imag_part), denominator)),
        }
        for real_part, imag_part in zip(real, imag)
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--boxes", type=Path, required=True)
    parser.add_argument("--final", type=Path, required=True)
    parser.add_argument("--vector", type=Path, action="append", required=True)
    parser.add_argument("--weight", action="append")
    parser.add_argument("--delta")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    boxes = load(args.boxes)
    final = load(args.final)
    vector_documents = [load(path) for path in args.vector]
    if boxes.get("schema") != "riemann.toeplitz-coefficient-box.v1":
        raise ValueError("bad boxes schema")
    if final.get("schema") != "riemann.piecewise-carrier-final-interval.v1":
        raise ValueError("bad final schema")

    dimension = int(boxes["cells"])
    lags = boxes["lags"]
    if len(lags) != dimension:
        raise ValueError("lag count mismatch")
    vectors = [vector_from_document(document) for document in vector_documents]
    if any(len(vector) != dimension for vector in vectors):
        raise ValueError("vector dimension mismatch")

    weights = (
        [Fraction(1) for _ in vectors]
        if args.weight is None
        else [parse_ratio(value) for value in args.weight]
    )
    if len(weights) != len(vectors):
        raise ValueError("one weight is required per vector")
    if any(weight <= 0 for weight in weights):
        raise ValueError("weights must be positive")

    checks: list[dict[str, object]] = []
    for index, vector in enumerate(vectors):
        checks.append(
            {
                "id": f"vector-{index}",
                "kind": "fixed-vector",
                "vector": vector,
            }
        )
    checks.append(
        {
            "id": "portfolio",
            "kind": "gram-portfolio",
            "terms": [
                {
                    "weight": fraction_json(weight),
                    "vector": vector,
                }
                for weight, vector in zip(weights, vectors)
            ],
        }
    )
    if args.delta is not None:
        checks.append(
            {
                "id": "whole-matrix",
                "kind": "whole-matrix-positive",
                "delta": fraction_json(parse_ratio(args.delta)),
            }
        )

    output = {
        "schema": OUT_SCHEMA,
        "dimension": dimension,
        "alpha_interval": final["alpha_interval"],
        "correction_operator_radius": final["correction_radius_per_unit"],
        "lags": lags,
        "checks": checks,
        "source_binding": {
            "cutoff": final.get("cutoff"),
            "carrier_exact": final.get("carrier_exact"),
            "precision_bits": final.get("precision_bits"),
            "coverage": final.get("coverage"),
            "lag_vector_sha256": boxes.get("vector_sha256"),
            "input_vector_sha256": [
                document.get("vector_sha256") for document in vector_documents
            ],
        },
        "proof_boundary": (
            "Adapter only. verify_toeplitz_box.py reconstructs every exact "
            "contraction and decides the sign."
        ),
    }
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
