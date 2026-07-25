#!/usr/bin/env python3
"""Reconnaissance for circulant upper certificates of the c=10^11 Toeplitz target.

This script is discovery arithmetic only.  It merges the committed complete
X-0801 coefficient shards, reconstructs the Hermitian Toeplitz prime matrix,
and solves finite linear programs for Hermitian circulant extensions whose
leading principal K x K block is exactly that midpoint Toeplitz matrix.

If C is such an extension, Cauchy interlacing gives

    lambda_max(S_K) <= lambda_max(C).

The circulant eigenvalues are the finite DFT of its first row.  The LP chooses
all entries that do not occur in the leading K x K block so as to minimize the
largest DFT value.  Floating results are nominations only; a proof-grade follow-
up must freeze the completion to dyadics and enclose every DFT value and every
coefficient-source error.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
from scipy.linalg import toeplitz
from scipy.optimize import linprog

ALPHA = 4.351719952088318
EXPECTED_PRIMES = 4_118_054_813
EXPECTED_HIGHER = 28_156
EXPECTED_TOTAL = 4_118_082_969
K = 1024


def load_coefficients(root: Path) -> tuple[np.ndarray, dict[str, int]]:
    paths = sorted(root.glob("shard-*.json"))
    if len(paths) != 50:
        raise ValueError(f"expected 50 discovery shards, found {len(paths)}")

    coeff = np.zeros(K, dtype=np.complex128)
    ranges: list[tuple[int, int]] = []
    prime_count = higher_count = total_count = higher_streams = 0
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("schema") != "riemann.carrier-piecewise-shard.v1":
            raise ValueError(f"{path}: wrong schema")
        params = data.get("parameters", {})
        if (
            params.get("cutoff") != 100_000_000_000
            or params.get("cells") != K
            or params.get("segment_size") != 20_000_000
            or params.get("total_segments") != 5000
            or params.get("carrier") != "4709203636353.65"
        ):
            raise ValueError(f"{path}: parameter mismatch")
        segment_range = data.get("segment_range", {})
        start = int(segment_range.get("start"))
        end = int(segment_range.get("end"))
        ranges.append((start, end))
        real = np.asarray(data["coefficients"]["real"], dtype=np.float64)
        imag = np.asarray(data["coefficients"]["imag"], dtype=np.float64)
        if real.shape != (K,) or imag.shape != (K,):
            raise ValueError(f"{path}: wrong coefficient shape")
        coeff += real + 1j * imag
        primes = int(data["prime_count"])
        higher = int(data["higher_prime_power_count"])
        prime_count += primes
        higher_count += higher
        total_count += primes + higher
        higher_streams += bool(data.get("include_higher_prime_powers"))

    ranges.sort()
    cursor = 0
    for start, end in ranges:
        if start != cursor:
            raise ValueError(f"coverage gap or overlap at {cursor}")
        cursor = end
    if cursor != 5000 or higher_streams != 1:
        raise ValueError("coverage or higher-power stream mismatch")
    if (prime_count, higher_count, total_count) != (
        EXPECTED_PRIMES,
        EXPECTED_HIGHER,
        EXPECTED_TOTAL,
    ):
        raise ValueError("global term counts mismatch")
    return coeff, {
        "prime_count": prime_count,
        "higher_prime_power_count": higher_count,
        "total_terms": total_count,
        "shards": len(paths),
    }


def toeplitz_matrix(coeff: np.ndarray) -> np.ndarray:
    row = np.empty(K, dtype=np.complex128)
    row[0] = coeff[0].real
    row[1:] = 0.5 * coeff[1:]
    matrix = toeplitz(np.conj(row), row)
    return 0.5 * (matrix + matrix.conj().T)


def fixed_circulant_row(coeff: np.ndarray, size: int) -> np.ndarray:
    if size < 2 * K:
        raise ValueError("circulant size must be at least 2K")
    row = np.zeros(size, dtype=np.complex128)
    row[0] = coeff[0].real
    row[1:K] = 0.5 * coeff[1:]
    row[size - K + 1 :] = np.conj(row[1:K][::-1])
    return row


def optimize_completion(coeff: np.ndarray, size: int) -> dict[str, Any]:
    row = fixed_circulant_row(coeff, size)
    fixed_eigenvalues = np.fft.fft(row).real

    # One real variable for a self-conjugate Nyquist lag, two real variables
    # for every other free conjugate pair.  The final variable is t.
    columns: list[np.ndarray] = []
    labels: list[tuple[str, int]] = []
    k = np.arange(size, dtype=np.float64)
    for d in range(K, size // 2 + 1):
        angle = 2.0 * np.pi * k * d / size
        if 2 * d == size:
            columns.append(np.cos(angle))
            labels.append(("real", d))
        else:
            columns.append(2.0 * np.cos(angle))
            labels.append(("real", d))
            columns.append(2.0 * np.sin(angle))
            labels.append(("imag", d))

    if columns:
        design = np.column_stack(columns)
    else:
        design = np.empty((size, 0), dtype=np.float64)
    a_ub = np.column_stack([design, -np.ones(size, dtype=np.float64)])
    b_ub = -fixed_eigenvalues
    objective = np.zeros(design.shape[1] + 1, dtype=np.float64)
    objective[-1] = 1.0
    result = linprog(
        objective,
        A_ub=a_ub,
        b_ub=b_ub,
        bounds=[(None, None)] * (design.shape[1] + 1),
        method="highs",
        options={"dual_feasibility_tolerance": 1e-9, "primal_feasibility_tolerance": 1e-9},
    )
    if not result.success:
        raise RuntimeError(f"size {size}: LP failed: {result.message}")

    free = result.x[:-1]
    for value, (kind, d) in zip(free, labels):
        if kind == "real":
            row[d] += value
            if 2 * d != size:
                row[size - d] += value
        else:
            row[d] += 1j * value
            row[size - d] -= 1j * value
    eigenvalues = np.fft.fft(row).real
    residual = float(np.max(eigenvalues - result.x[-1]))
    hermitian_residual = float(np.max(np.abs(row[1:] - np.conj(row[:0:-1]))))
    principal = np.empty(K, dtype=np.complex128)
    principal[0] = row[0]
    principal[1:] = row[1:K]
    expected = np.empty(K, dtype=np.complex128)
    expected[0] = coeff[0].real
    expected[1:] = 0.5 * coeff[1:]
    principal_residual = float(np.max(np.abs(principal - expected)))

    # Store only the free completion; the fixed first K lags are already in the
    # committed source shards.  Decimal values are discovery data, not a proof.
    free_values = []
    for value, (kind, d) in zip(free, labels):
        free_values.append({"lag": d, "component": kind, "value": float(value)})

    return {
        "size": size,
        "free_real_variables": len(columns),
        "lp_objective": float(result.fun),
        "maximum_circulant_eigenvalue": float(np.max(eigenvalues)),
        "minimum_circulant_eigenvalue": float(np.min(eigenvalues)),
        "alpha_minus_circulant_max": float(ALPHA - np.max(eigenvalues)),
        "constraint_residual": residual,
        "hermitian_residual": hermitian_residual,
        "principal_block_residual": principal_residual,
        "iterations": int(result.nit),
        "free_completion": free_values,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--shard-root",
        type=Path,
        default=Path(
            "experiments/X-2805-directed-prime-producer/results/target-c1e11/"
            "discovery/shards"
        ),
    )
    parser.add_argument("--sizes", default="2048,2560,3072,4096")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    coeff, counts = load_coefficients(args.shard_root)
    s_matrix = toeplitz_matrix(coeff)
    h_matrix = ALPHA * np.eye(K) - s_matrix
    h_eigenvalues = np.linalg.eigvalsh(h_matrix)
    sizes = [int(value) for value in args.sizes.split(",") if value.strip()]
    completions = [optimize_completion(coeff, size) for size in sizes]
    result = {
        "schema": "riemann.d0801-circulant-completion-reconnaissance.v1",
        "status": "EMPIRICAL_NOT_CERTIFIED",
        "counts": counts,
        "cells": K,
        "alpha_midpoint": ALPHA,
        "toeplitz": {
            "minimum_h_eigenvalue": float(h_eigenvalues[0]),
            "second_h_eigenvalue": float(h_eigenvalues[1]),
            "maximum_prime_eigenvalue": float(np.linalg.eigvalsh(s_matrix)[-1]),
            "hermitian_residual": float(np.max(np.abs(h_matrix - h_matrix.conj().T))),
        },
        "completions": completions,
        "interpretation": (
            "A positive alpha-minus-circulant-max is a discovery nomination for a "
            "whole-matrix certificate. Proof requires a dyadic completion, directed "
            "DFT enclosures, and an operator-norm source-error moat."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "toeplitz_min": result["toeplitz"]["minimum_h_eigenvalue"],
        "completion_gaps": [
            [entry["size"], entry["alpha_minus_circulant_max"]]
            for entry in completions
        ],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
