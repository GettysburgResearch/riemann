#!/usr/bin/env python3
"""Recover and preserve a canonical dyadic top eigenvector from X-0801 shards.

This is a discovery-artifact exporter, not an interval proof. It fail-closes on
coverage or parameter inconsistencies, canonicalizes the global complex phase,
rounds the resulting vector to an exact dyadic vector, and records both the
floating eigenpair and the rounded-vector midpoint diagnostics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable, Sequence

import numpy as np

SHARD_SCHEMA = "riemann.carrier-piecewise-shard.v1"
VECTOR_SCHEMA = "riemann.piecewise-carrier-vector.v1"


def load_shard(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema") != SHARD_SCHEMA:
        raise ValueError(f"{path}: unsupported shard schema")
    return data


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")


def merge_coefficients(shards: Iterable[dict[str, Any]]) -> tuple[dict[str, Any], np.ndarray, dict[str, int]]:
    items = list(shards)
    if not items:
        raise ValueError("at least one shard is required")
    reference = items[0]["parameters"]
    keys = ("cutoff", "carrier", "cells", "segment_size", "total_segments")
    for item in items:
        if any(item["parameters"].get(key) != reference.get(key) for key in keys):
            raise ValueError("all shards must have identical parameters")
    ordered = sorted(items, key=lambda item: int(item["segment_range"]["start"]))
    cursor = 0
    for item in ordered:
        start = int(item["segment_range"]["start"])
        end = int(item["segment_range"]["end"])
        if start != cursor:
            raise ValueError(f"segment gap or overlap at {cursor}: next shard starts {start}")
        if end < start:
            raise ValueError("invalid decreasing segment range")
        cursor = end
    if cursor != int(reference["total_segments"]):
        raise ValueError("shards do not cover the complete prime stream")
    if sum(bool(item["include_higher_prime_powers"]) for item in items) != 1:
        raise ValueError("exactly one shard must include higher prime powers")

    cells = int(reference["cells"])
    coefficients = np.zeros(cells, dtype=np.complex128)
    prime_count = higher_count = 0
    for item in items:
        real = np.asarray(item["coefficients"]["real"], dtype=np.float64)
        imag = np.asarray(item["coefficients"]["imag"], dtype=np.float64)
        if len(real) != cells or len(imag) != cells:
            raise ValueError("coefficient vector has the wrong length")
        coefficients += real + 1j * imag
        pcount = int(item["prime_count"])
        hcount = int(item["higher_prime_power_count"])
        if int(item.get("total_prime_power_terms", pcount + hcount)) != pcount + hcount:
            raise ValueError("term-count mismatch")
        prime_count += pcount
        higher_count += hcount
    return reference, coefficients, {
        "prime_count": prime_count,
        "higher_prime_power_count": higher_count,
        "total_prime_power_terms": prime_count + higher_count,
    }


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


def canonicalize_phase(vector: np.ndarray) -> tuple[np.ndarray, int]:
    pivot = int(np.argmax(np.abs(vector)))
    if vector[pivot] == 0:
        raise ValueError("zero eigenvector")
    rotated = vector * np.exp(-1j * np.angle(vector[pivot]))
    if rotated[pivot].real < 0:
        rotated = -rotated
    rotated[pivot] = complex(abs(rotated[pivot]), 0.0)
    return rotated, pivot


def round_nearest_even_binary64(value: float, scale_bits: int) -> int:
    if not math.isfinite(value):
        raise ValueError("non-finite vector component")
    numerator, denominator = value.as_integer_ratio()
    if scale_bits >= 0:
        scaled_num = numerator << scale_bits
        q, r = divmod(abs(scaled_num), denominator)
        twice = 2 * r
        if twice > denominator or (twice == denominator and q & 1):
            q += 1
        return q if scaled_num >= 0 else -q
    raise ValueError("scale_bits must be nonnegative")


def dyadic_vector(vector: np.ndarray, scale_bits: int) -> tuple[list[int], list[int]]:
    return (
        [round_nearest_even_binary64(float(z.real), scale_bits) for z in vector],
        [round_nearest_even_binary64(float(z.imag), scale_bits) for z in vector],
    )


def dyadic_to_complex(real_nums: list[int], imag_nums: list[int], scale_bits: int) -> np.ndarray:
    scale = float(2.0 ** (-scale_bits))
    return np.asarray(real_nums, dtype=np.float64) * scale + 1j * np.asarray(imag_nums, dtype=np.float64) * scale


def freeze(shards: Iterable[dict[str, Any]], scale_bits: int) -> dict[str, Any]:
    if not isinstance(scale_bits, int) or isinstance(scale_bits, bool) or not 1 <= scale_bits <= 1022:
        raise ValueError("scale_bits must be an integer in [1,1022]")
    parameters, coefficients, counts = merge_coefficients(shards)
    matrix = hermitian_toeplitz(coefficients)
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    vector, pivot = canonicalize_phase(eigenvectors[:, -1])
    eigenvalue = float(eigenvalues[-1])
    residual = matrix @ vector - eigenvalue * vector
    residual_inf = float(np.max(np.abs(residual)))

    real_nums, imag_nums = dyadic_vector(vector, scale_bits)
    rounded = dyadic_to_complex(real_nums, imag_nums, scale_bits)
    rounded_norm = float(np.vdot(rounded, rounded).real)
    rounded_rayleigh = float((np.vdot(rounded, matrix @ rounded) / np.vdot(rounded, rounded)).real)

    vector_object = {
        "schema": VECTOR_SCHEMA,
        "parameters": parameters,
        "normalization_fingerprint_sha256": "65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be",
        "phase_convention": {
            "pivot_index": pivot,
            "rule": "largest-magnitude component is real and nonnegative; first index wins ties",
        },
        "dyadic_vector": {
            "scale_bits": scale_bits,
            "real_numerators": real_nums,
            "imag_numerators": imag_nums,
        },
    }
    digest = hashlib.sha256(canonical_json(vector_object)).hexdigest()
    return {
        **vector_object,
        "canonical_sha256": digest,
        "coverage": counts,
        "discovery_diagnostics": {
            "largest_prime_toeplitz_eigenvalue": eigenvalue,
            "eigenpair_residual_inf_norm": residual_inf,
            "floating_vector_norm_squared": float(np.vdot(vector, vector).real),
            "rounded_vector_norm_squared_midpoint": rounded_norm,
            "rounded_vector_prime_rayleigh_midpoint": rounded_rayleigh,
            "rounding_displacement_l2": float(np.linalg.norm(rounded - vector)),
            "backend": "numpy.linalg.eigh on complex128 Hermitian Toeplitz matrix",
            "classification": "EMPIRICAL_VECTOR_ARTIFACT_NOT_INTERVAL_CERTIFIED",
        },
        "warning": (
            "The dyadic coordinates are exact, but their association with the complete prime operator "
            "is only empirical until a directed fixed-vector producer re-evaluates every term."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("shards", nargs="+", type=Path)
    parser.add_argument("--scale-bits", type=int, default=96)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    result = freeze((load_shard(path) for path in args.shards), args.scale_bits)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
