#!/usr/bin/env python3
"""Merge complete X-0801 shards and compute the Hermitian Toeplitz leading screen."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any, Iterable

import numpy as np

from stream import SCHEMA

RESULT_SCHEMA = "riemann.carrier-piecewise-result.v1"


def _load(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema") != SCHEMA:
        raise ValueError(f"{path}: unsupported shard schema")
    return data


def hermitian_toeplitz(coefficients: np.ndarray) -> np.ndarray:
    cells = len(coefficients)
    first = np.empty(cells, dtype=np.complex128)
    first[0] = coefficients[0].real
    if cells > 1:
        first[1:] = 0.5 * coefficients[1:]
    matrix = np.empty((cells, cells), dtype=np.complex128)
    for lag in range(cells):
        indices = np.arange(cells - lag)
        matrix[indices, indices + lag] = first[lag]
        if lag:
            matrix[indices + lag, indices] = np.conj(first[lag])
    return matrix


def merge_shards(shards: Iterable[dict[str, Any]]) -> dict[str, Any]:
    items = list(shards)
    if not items:
        raise ValueError("at least one shard is required")
    reference = items[0]["parameters"]
    keys = ("cutoff", "carrier", "cells", "segment_size", "total_segments")
    for item in items:
        if any(item["parameters"].get(key) != reference.get(key) for key in keys):
            raise ValueError("all shards must have identical parameters")
    ordered = sorted(items, key=lambda item: item["segment_range"]["start"])
    cursor = 0
    for item in ordered:
        start = item["segment_range"]["start"]
        end = item["segment_range"]["end"]
        if start != cursor:
            raise ValueError(f"segment gap or overlap at {cursor}: next shard starts {start}")
        if end < start:
            raise ValueError("invalid decreasing segment range")
        cursor = end
    if cursor != reference["total_segments"]:
        raise ValueError("shards do not cover the complete prime stream")
    power_shards = sum(bool(item["include_higher_prime_powers"]) for item in items)
    if power_shards != 1:
        raise ValueError("exactly one shard must include higher prime powers")

    cells = int(reference["cells"])
    coefficients = np.zeros(cells, dtype=np.complex128)
    prime_count = 0
    higher_count = 0
    for item in items:
        real = np.asarray(item["coefficients"]["real"], dtype=np.float64)
        imag = np.asarray(item["coefficients"]["imag"], dtype=np.float64)
        if len(real) != cells or len(imag) != cells:
            raise ValueError("coefficient vector has the wrong length")
        coefficients += real + 1j * imag
        prime_count += int(item["prime_count"])
        higher_count += int(item["higher_prime_power_count"])

    matrix = hermitian_toeplitz(coefficients)
    eigenvalues = np.linalg.eigvalsh(matrix)
    carrier = np.longdouble(reference["carrier"])
    alpha = float(
        np.log(carrier / (np.longdouble(2) * np.longdouble(np.pi)))
        / (np.longdouble(2) * np.longdouble(np.pi))
    )
    largest = float(eigenvalues[-1])
    leading_margin = alpha - largest
    return {
        "schema": RESULT_SCHEMA,
        "experiment_id": "X-0801",
        "status": "EMPIRICAL_NOT_CERTIFIED",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "parameters": reference,
        "prime_count": prime_count,
        "higher_prime_power_count": higher_count,
        "total_prime_power_terms": prime_count + higher_count,
        "archimedean_leading_scalar": alpha,
        "largest_prime_toeplitz_eigenvalue": largest,
        "leading_margin": leading_margin,
        "top_ten_leading_margins": [float(alpha - x) for x in eigenvalues[-1:-11:-1]],
        "certified_negative": False,
        "counterexample_candidate": None,
        "warning": (
            "A negative leading margin would still require exact archimedean and pole "
            "blocks, directed phase balls, an explicit-formula normalization audit, and "
            "an exact frozen-vector checker. This ordinary-floating result is not a proof."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("shards", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = merge_shards(_load(path) for path in args.shards)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
