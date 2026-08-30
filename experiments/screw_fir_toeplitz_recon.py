#!/usr/bin/env python3
"""Binary64 reconnaissance for L-9504 zeta-screw FIR/Toeplitz witnesses.

The default case uses the exact resonance h=log(2)/3 and n=53.  Every prime
threshold is assigned by the integer predicate q**3 <= 2**k, so even the
reconnaissance code does not compare rounded exponentials with integers.

This program is NOT a proof producer.  Its eigenvectors and zeta zeros are
search data only.  Exact nominations must be frozen and replayed by
``screw_toeplitz_mpfr.c`` and the independent standard-library checker.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import time
from pathlib import Path
from typing import Any

import numpy as np

EULER_GAMMA = 0.577215664901532860606512090082402431
CATALAN = 0.915965594177219015054603514932384111
B_CONSTANT = (
    -EULER_GAMMA
    - math.pi / 2.0
    - 3.0 * math.log(2.0)
    - math.log(math.pi)
) / 2.0
C_CONSTANT = math.pi * math.pi + 8.0 * CATALAN


def integer_nth_root(value: int, degree: int) -> int:
    if value < 0 or degree <= 0:
        raise ValueError("invalid integer-root input")
    if value < 2:
        return value
    lo, hi = 0, 1 << ((value.bit_length() + degree - 1) // degree)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**degree <= value:
            lo = mid
        else:
            hi = mid
    return lo


def sieve_flags(limit: int) -> bytearray:
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if flags[p]:
            start = p * p
            flags[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    return flags


def smooth_a(t: float) -> float:
    if t <= 0.0:
        raise ValueError("smooth_a requires t>0")
    total = 0.0
    index = 1
    ratio_cap = math.exp(-2.0 * t)
    while True:
        denominator = 4 * index + 1
        term = math.exp(-denominator * t / 2.0) / denominator**2
        total += term
        next_denominator = denominator + 4
        next_term = (
            math.exp(-next_denominator * t / 2.0) / next_denominator**2
        )
        if 4.0 * next_term / (1.0 - ratio_cap) < 1.0e-17:
            break
        index += 1
    return (
        4.0 * (math.exp(t / 2.0) - 2.0)
        + B_CONSTANT * t
        + C_CONSTANT / 4.0
        - 4.0 * total
    )


def exact_resonance_table(
    step_prime: int,
    denominator: int,
    matrix_size: int,
) -> tuple[float, int, int, int, str, list[float]]:
    if step_prime < 2 or denominator < 1 or matrix_size < 1:
        raise ValueError("invalid resonance parameters")
    cutoff = integer_nth_root(step_prime**matrix_size, denominator)
    flags = sieve_flags(cutoff)
    threshold_powers = [step_prime**k for k in range(matrix_size + 1)]
    bucket_0 = [0.0] * (matrix_size + 1)
    bucket_1 = [0.0] * (matrix_size + 1)
    digest = hashlib.sha256()
    prime_count = 0
    prime_power_count = 0

    for prime in range(2, cutoff + 1):
        if not flags[prime]:
            continue
        prime_count += 1
        log_prime = math.log(prime)
        q = prime
        exponent = 1
        while q <= cutoff:
            powered = q**denominator
            lo, hi = 1, matrix_size
            while lo < hi:
                mid = (lo + hi) // 2
                if powered <= threshold_powers[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            bucket = lo
            if not powered <= threshold_powers[bucket]:
                raise AssertionError("threshold assignment failed")

            weight = log_prime / math.sqrt(q)
            bucket_0[bucket] += weight
            bucket_1[bucket] += weight * exponent * log_prime

            digest.update(q.to_bytes(8, "big"))
            digest.update(prime.to_bytes(8, "big"))
            digest.update(exponent.to_bytes(4, "big"))
            prime_power_count += 1

            if q > cutoff // prime:
                break
            q *= prime
            exponent += 1

    h = math.log(step_prime) / denominator
    prefix_0 = 0.0
    prefix_1 = 0.0
    psi = [0.0]
    for k in range(1, matrix_size + 1):
        prefix_0 += bucket_0[k]
        prefix_1 += bucket_1[k]
        t = k * h
        psi.append(smooth_a(t) - t * prefix_0 + prefix_1)

    return (
        h,
        cutoff,
        prime_count,
        prime_power_count,
        digest.hexdigest(),
        psi,
    )


def increment_toeplitz(psi: list[float], matrix_size: int) -> np.ndarray:
    indices = np.arange(matrix_size)
    lag = np.abs(indices[:, None] - indices[None, :])
    values = np.asarray(psi)
    matrix = values[lag + 1] + values[np.abs(lag - 1)] - 2.0 * values[lag]
    return (matrix + matrix.T) / 2.0


def exact_filter_data(numerators: list[int]) -> tuple[list[int], list[int]]:
    n = len(numerators)
    differences = [numerators[0]]
    differences.extend(
        numerators[index] - numerators[index - 1] for index in range(1, n)
    )
    differences.append(-numerators[-1])
    if sum(differences) != 0:
        raise AssertionError("difference vector is not zero-sum")
    correlations = [
        sum(
            differences[index] * differences[index + lag]
            for index in range(n + 1 - lag)
        )
        for lag in range(1, n + 1)
    ]
    return differences, correlations


def binomial_values(
    psi: list[float],
    step_prime: int,
    denominator: int,
) -> list[dict[str, float | int]]:
    result: list[dict[str, float | int]] = []
    for order in range(1, len(psi)):
        norm = math.comb(2 * order, order)
        value = 0.0
        jump = 0.0
        for lag in range(1, order + 1):
            value += (
                2.0
                * (-1.0) ** (lag + 1)
                * math.comb(2 * order, order - lag)
                * psi[lag]
                / norm
            )
        for power in range(1, order // denominator + 1):
            lag = denominator * power
            jump += (
                2.0
                * denominator
                * math.log(step_prime)
                * ((-1) ** lag)
                * power
                * math.comb(2 * order, order - lag)
                * step_prime ** (-power / 2.0)
                / norm
            )
        result.append(
            {
                "order": order,
                "normalized_value": value,
                "derivative_jump": jump,
            }
        )
    return result


def zero_attribution(
    h: float,
    matrix: np.ndarray,
    vector: np.ndarray,
    zero_count: int,
) -> dict[str, Any] | None:
    if zero_count <= 0:
        return None
    import mpmath as mp

    mp.mp.dps = 25
    zeros = [float(mp.im(mp.zetazero(index))) for index in range(1, zero_count + 1)]
    dimension = len(vector)
    contributions: list[tuple[float, int, float, np.ndarray]] = []
    residual = matrix.copy()
    checkpoints: list[dict[str, float | int]] = []
    checkpoint_set = {
        value
        for value in (10, 25, 50, 100, 200, 400, zero_count)
        if value <= zero_count
    }
    for index, gamma in enumerate(zeros, 1):
        phase = gamma * h
        u = (
            (1.0 - np.exp(1j * phase))
            * np.exp(1j * phase * np.arange(dimension))
            / gamma
        )
        pair_matrix = 2.0 * np.real(np.outer(u, np.conj(u)))
        contribution = 2.0 * abs(np.vdot(u, vector)) ** 2
        contributions.append((float(contribution), index, gamma, pair_matrix))
        residual -= pair_matrix
        if index in checkpoint_set:
            checkpoints.append(
                {
                    "positive_zero_pairs": index,
                    "reoptimized_min_eigenvalue": float(
                        np.linalg.eigvalsh((residual + residual.T) / 2.0)[0]
                    ),
                    "original_vector_residual": float(vector @ residual @ vector),
                }
            )

    contributions.sort(key=lambda item: item[0], reverse=True)
    top = [
        {
            "positive_zero_index": index,
            "ordinate": gamma,
            "original_vector_pair_contribution": contribution,
        }
        for contribution, index, gamma, _ in contributions[: min(20, zero_count)]
    ]
    return {
        "classification": "APPROXIMATE_MPMATH_ZERO_ATTRIBUTION_ONLY",
        "zero_count": zero_count,
        "checkpoints": checkpoints,
        "top_original_vector_contributors": top,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--step-prime", type=int, default=2)
    parser.add_argument("--denominator", type=int, default=3)
    parser.add_argument("--matrix-size", type=int, default=53)
    parser.add_argument("--freeze-bits", type=int, default=24)
    parser.add_argument("--zero-count", type=int, default=0)
    parser.add_argument("--json-out", type=Path)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    started = time.perf_counter()
    (
        h,
        cutoff,
        prime_count,
        prime_power_count,
        manifest_sha256,
        psi,
    ) = exact_resonance_table(
        args.step_prime,
        args.denominator,
        args.matrix_size,
    )
    matrix = increment_toeplitz(psi, args.matrix_size)
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    vector = eigenvectors[:, 0]
    if float(vector.sum()) < 0.0:
        vector = -vector
    scale = 1 << args.freeze_bits
    numerators = np.rint(vector * scale).astype(np.int64).tolist()
    frozen = np.asarray(numerators, dtype=float) / scale
    differences, correlations = exact_filter_data(numerators)

    result = {
        "classification": "EMPIRICAL_RECONNAISSANCE_ONLY",
        "arithmetic": "binary64 plus exact integer thresholds/autocorrelations",
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "parameters": {
            "step_prime": args.step_prime,
            "denominator": args.denominator,
            "h": h,
            "matrix_size": args.matrix_size,
            "prime_cutoff": cutoff,
            "threshold_rule": (
                f"q^{args.denominator} <= {args.step_prime}^k"
            ),
        },
        "manifest": {
            "prime_count": prime_count,
            "prime_power_count": prime_power_count,
            "sha256": manifest_sha256,
        },
        "toeplitz": {
            "binary64_min_eigenvalue": float(eigenvalues[0]),
            "binary64_max_eigenvalue": float(eigenvalues[-1]),
            "freeze_bits": args.freeze_bits,
            "b_numerators": numerators,
            "difference_numerators": differences,
            "autocorrelation_lags_1_to_n": correlations,
            "frozen_vector_norm2": float(frozen @ frozen),
            "frozen_vector_rayleigh": float(frozen @ matrix @ frozen),
        },
        "binomial_filters": binomial_values(
            psi, args.step_prime, args.denominator
        ),
        "zero_attribution": zero_attribution(
            h, matrix, vector, args.zero_count
        ),
        "timing_seconds": time.perf_counter() - started,
    }
    encoded = json.dumps(result, indent=2, sort_keys=True)
    print(encoded)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(encoded + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
