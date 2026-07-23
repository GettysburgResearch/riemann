#!/usr/bin/env python3
"""Regenerate a complete-prime D-0801 leading vector and freeze it dyadically.

STATUS: discovery arithmetic, not interval-certified. The output vector itself
is exact dyadic data and is suitable as input to a directed fixed-vector producer.
"""
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path
import numpy as np
from scipy.linalg import toeplitz
from exact_vector import SCHEMA, canonical_sha256


def simple_primes(limit: int) -> np.ndarray:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    return np.flatnonzero(sieve).astype(np.int64)


def segment_primes(low: int, high: int, base: np.ndarray) -> np.ndarray:
    mark = np.ones(high - low, dtype=bool)
    root = math.isqrt(high - 1)
    for raw in base:
        p = int(raw)
        if p > root:
            break
        start = max(p * p, ((low + p - 1) // p) * p)
        if start < high:
            mark[start - low : high - low : p] = False
    return np.flatnonzero(mark).astype(np.int64) + low


def higher_prime_powers(cutoff: int, base: np.ndarray):
    qs, ps = [], []
    for raw in base:
        p = int(raw)
        q = p * p
        while q <= cutoff:
            qs.append(q)
            ps.append(p)
            if q > cutoff // p:
                break
            q *= p
    return np.asarray(qs, dtype=np.int64), np.asarray(ps, dtype=np.int64)


def accumulate(coeff, q, p, *, cutoff, carrier):
    if len(q) == 0:
        return
    cells = len(coeff)
    log_cutoff = np.log(np.longdouble(cutoff))
    two_pi = np.longdouble(2) * np.longdouble(np.pi)
    q_ld = q.astype(np.longdouble)
    log_q = np.log(q_ld)
    scaled = (cells * log_q / log_cutoff).astype(np.float64)
    lag = np.floor(scaled).astype(np.int64)
    fraction = scaled - lag
    amplitude = (
        np.log(p.astype(np.longdouble))
        / (np.longdouble(np.pi) * np.sqrt(q_ld))
    ).astype(np.float64)
    phase = np.remainder(carrier * log_q, two_pi).astype(np.float64)
    z = amplitude * (np.cos(phase) - 1j * np.sin(phase))
    for target, weight in ((lag, 1 - fraction), (lag + 1, fraction)):
        mask = target < cells
        indices = target[mask]
        coeff.real += np.bincount(
            indices, weights=weight[mask] * z.real[mask], minlength=cells
        )
        coeff.imag += np.bincount(
            indices, weights=weight[mask] * z.imag[mask], minlength=cells
        )


def regenerate(cutoff: int, carrier_text: str, cells: int, bits: int, segment_size: int):
    carrier = np.longdouble(carrier_text)
    base = simple_primes(math.isqrt(cutoff))
    coefficients = np.zeros(cells, dtype=np.complex128)
    prime_count = 0
    for low in range(2, cutoff + 1, segment_size):
        high = min(cutoff + 1, low + segment_size)
        primes = segment_primes(low, high, base)
        accumulate(coefficients, primes, primes, cutoff=cutoff, carrier=carrier)
        prime_count += len(primes)
    q, p = higher_prime_powers(cutoff, base)
    accumulate(coefficients, q, p, cutoff=cutoff, carrier=carrier)

    row = np.empty(cells, dtype=np.complex128)
    row[0] = coefficients[0].real
    row[1:] = 0.5 * coefficients[1:]
    matrix = toeplitz(np.conj(row), row)
    matrix = (matrix + matrix.conj().T) / 2
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    largest = float(eigenvalues[-1])
    vector = eigenvectors[:, -1]

    pivot = int(np.argmax(np.abs(vector)))
    vector *= np.exp(-1j * np.angle(vector[pivot]))
    if vector[pivot].real < 0:
        vector = -vector

    scale = 1 << bits
    real = [int(round(float(z.real) * scale)) for z in vector]
    imag = [int(round(float(z.imag) * scale)) for z in vector]
    dyadic = np.array([complex(a / scale, b / scale) for a, b in zip(real, imag)])
    alpha = float(
        np.log(carrier / (np.longdouble(2) * np.longdouble(np.pi)))
        / (np.longdouble(2) * np.longdouble(np.pi))
    )
    norm = float(np.vdot(dyadic, dyadic).real)
    rayleigh = float(np.vdot(dyadic, matrix @ dyadic).real)
    margin = (alpha * norm - rayleigh) / norm
    residual = float(np.max(np.abs(matrix @ dyadic - (rayleigh / norm) * dyadic)))
    canonical = {
        "imag_numerators": imag,
        "real_numerators": real,
        "scale_bits": bits,
    }
    return {
        "schema": SCHEMA,
        "status": "EMPIRICAL_VECTOR_EXACT_DYADIC_DATA",
        "cells": cells,
        "parameters": {
            "cutoff": cutoff,
            "carrier": carrier_text,
            "phase_backend": (
                "numpy.longdouble log/product/remainder; float64 trigonometry, "
                "accumulation, eigensolve"
            ),
            "segment_size": segment_size,
        },
        "counts": {
            "primes": int(prime_count),
            "higher_prime_powers": int(len(q)),
            "total_prime_powers": int(prime_count + len(q)),
        },
        "vector": canonical,
        "vector_sha256": canonical_sha256(canonical),
        "discovery": {
            "largest_prime_eigenvalue": largest,
            "archimedean_leading_scalar": alpha,
            "rounded_vector_leading_margin": margin,
            "rounded_vector_residual_inf_norm": residual,
            "rounded_vector_norm_squared": norm,
            "canonical_pivot_index": pivot,
        },
        "warning": (
            "The coefficients are exact dyadics; their nomination and the reported "
            "values are ordinary numerical discovery output."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cutoff", type=int, default=100_000_000)
    parser.add_argument("--carrier", default="4709203636353.65")
    parser.add_argument("--cells", type=int, default=1024)
    parser.add_argument("--bits", type=int, default=96)
    parser.add_argument("--segment-size", type=int, default=20_000_000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = regenerate(
        args.cutoff, args.carrier, args.cells, args.bits, args.segment_size
    )
    text = json.dumps(data, sort_keys=True, separators=(",", ":")) + "\n"
    args.output.write_text(text, encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "sha256": hashlib.sha256(text.encode()).hexdigest(),
                "vector_sha256": data["vector_sha256"],
                "margin": data["discovery"]["rounded_vector_leading_margin"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
