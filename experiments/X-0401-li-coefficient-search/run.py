#!/usr/bin/env python3
"""Exploratory Keiper-Li scan via Cauchy coefficients of d/dz log xi(1/(1-z)).

Discovery only: binary64 mpmath.fp evaluations + numpy FFT.
"""
from __future__ import annotations

import argparse
import cmath
import json
import math
import time
from pathlib import Path

import mpmath as mp
import numpy as np


def g_of_z(z: complex, zeta_s: complex | None = None) -> tuple[complex, bool]:
    """Return d/dz log xi(1/(1-z)) in the standard xi normalization."""
    s = 1.0 / (1.0 - z)
    # Logarithmic derivative of xi(s). The circle used below stays away from s=1.
    fp = mp.fp
    if zeta_s is None:
        zeta_s = fp.zeta(s)
    fallback = False
    try:
        zeta_prime_s = fp.zeta(s, derivative=1)
    except Exception:
        fallback = True
        with mp.workdps(40):
            smp = mp.mpc(s)
            zeta_s = mp.zeta(smp)
            zeta_prime_s = mp.zeta(smp, derivative=1)
    dlogxi = (
        1.0 / s
        + 1.0 / (s - 1.0)
        - 0.5 * math.log(math.pi)
        + 0.5 * fp.digamma(s / 2.0)
        + zeta_prime_s / zeta_s
    )
    return complex(s * s * dlogxi), fallback


def scan(n_max: int, oversample: float, alpha: float) -> dict:
    target = math.ceil(oversample * n_max)
    M = 1 << (target - 1).bit_length()
    r = math.exp(-alpha / n_max)

    samples = np.empty(M, dtype=np.complex128)
    max_abs = 0.0
    min_abs_zeta = math.inf
    fallback_count = 0
    t0 = time.time()
    for j in range(M):
        theta = 2.0 * math.pi * j / M
        z = r * complex(math.cos(theta), math.sin(theta))
        s = 1.0 / (1.0 - z)
        zs = complex(mp.fp.zeta(s))
        min_abs_zeta = min(min_abs_zeta, abs(zs))
        # Reuse zeta would require duplicating g; keep auditability simple for now.
        value, fallback = g_of_z(z, zs)
        fallback_count += int(fallback)
        samples[j] = value
        max_abs = max(max_abs, abs(value))

    sample_seconds = time.time() - t0
    t1 = time.time()
    coeff_raw = np.fft.fft(samples) / M
    fft_seconds = time.time() - t1

    k = np.arange(n_max, dtype=np.float64)
    scale = np.exp((alpha / n_max) * k)  # r^{-k}
    coeffs = coeff_raw[:n_max] * scale
    lambdas = coeffs.real
    imag = np.abs(coeffs.imag)

    n_idx = np.arange(1, n_max + 1)
    min_i = int(np.argmin(lambdas))
    neg_idx = np.flatnonzero(lambdas < 0)
    # Conservative binary64 diagnostic, not a proof bound.
    eps = np.finfo(np.float64).eps
    rough_roundoff = eps * math.sqrt(M) * max_abs * math.exp(alpha)

    checkpoints = sorted(set([1,2,3,4,5,10,20,50,100,200,500,1000,2000,5000,10000,n_max]))
    checkpoints = [n for n in checkpoints if n <= n_max]
    block_minima = {}
    for start in [1, 10, 100, 1000, 10000, 50000]:
        if start <= n_max:
            j = start - 1 + int(np.argmin(lambdas[start-1:]))
            block_minima[str(start)] = {"n": j + 1, "value": float(lambdas[j])}

    return {
        "method": "binary64-cauchy-fft-discovery",
        "n_max": n_max,
        "M": M,
        "oversample": oversample,
        "alpha": alpha,
        "radius": r,
        "sample_seconds": sample_seconds,
        "fft_seconds": fft_seconds,
        "max_abs_integrand": max_abs,
        "min_abs_zeta_on_samples": min_abs_zeta,
        "high_precision_fallback_count": fallback_count,
        "rough_roundoff_absolute": rough_roundoff,
        "max_abs_imag_coefficient": float(imag.max()),
        "minimum": {"n": min_i + 1, "value": float(lambdas[min_i])},
        "block_minima_from_n": block_minima,
        "negative_count": int(len(neg_idx)),
        "first_negative_indices": [int(i + 1) for i in neg_idx[:20]],
        "checkpoints": {str(n): float(lambdas[n-1]) for n in checkpoints},
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-max", type=int, default=10000)
    ap.add_argument("--oversample", type=float, default=8.0)
    ap.add_argument("--alpha", type=float, default=4.0)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    result = scan(args.n_max, args.oversample, args.alpha)
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.write_text(text + "\n")

if __name__ == "__main__":
    main()
