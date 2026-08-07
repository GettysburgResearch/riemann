#!/usr/bin/env python3
"""Reconnaissance for the universal dyadic-convolution terminal prime window.

This script is intentionally non-directed.  It constructs the convolution-square
window by Fourier inversion, enumerates every prime power through a finite cutoff,
and compares the pole-subtracted prime statistic with a finite critical-zero sum.
"""
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import mpmath as mp
import numpy as np


def dyadic_M(z: mp.mpc | mp.mpf, terms: int = 140) -> mp.mpc:
    out = mp.mpc(1)
    for j in range(1, terms + 1):
        r = mp.mpf(2) ** (-j)
        out *= -mp.expm1(-r * z) / (r * z)
    return out


def build_window(fft_size: int, period: float = 4.0) -> tuple[np.ndarray, float]:
    """Return samples of g=f*f on one period; g is supported in [0,2]."""
    freq = np.fft.fftfreq(fft_size, d=period / fft_size) * (2.0 * np.pi)
    amplitude = np.ones(fft_size, dtype=np.float64)
    for j in range(1, 64):
        r = 2.0 ** (-j)
        amplitude *= np.sinc((freq * r / 2.0) / np.pi)
    transform = np.exp(-1j * freq) * amplitude * amplitude
    samples = np.fft.ifft((fft_size / period) * transform).real
    return samples, period / fft_size


def prime_power_events(limit: int) -> tuple[np.ndarray, np.ndarray, int]:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    primes = np.nonzero(sieve)[0]

    ns: list[int] = []
    weights: list[float] = []
    for raw_p in primes:
        p = int(raw_p)
        logp = math.log(p)
        value = p
        while value <= limit:
            ns.append(value)
            weights.append(logp / math.sqrt(value))
            if value > limit // p:
                break
            value *= p

    order = np.argsort(ns)
    return (
        np.asarray(ns, dtype=np.int64)[order],
        np.asarray(weights, dtype=np.float64)[order],
        int(len(primes)),
    )


def interpolate(samples: np.ndarray, step: float, points: np.ndarray) -> np.ndarray:
    position = points / step
    left = np.floor(position).astype(np.int64)
    fraction = position - left
    left = np.clip(left, 0, len(samples) - 2)
    return samples[left] * (1.0 - fraction) + samples[left + 1] * fraction


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoff", type=int, default=10_000_000)
    parser.add_argument("--fft-size", type=int, default=1 << 17)
    parser.add_argument("--grid-points", type=int, default=10_000)
    parser.add_argument("--zero-count", type=int, default=50)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if args.cutoff < 100 or args.fft_size < 1024 or args.grid_points < 10:
        raise SystemExit("invalid reconnaissance parameters")

    started = time.time()
    window, step = build_window(args.fft_size)
    ns, weights, prime_count = prime_power_events(args.cutoff)
    logs = np.log(ns.astype(np.float64))

    mp.mp.dps = 60
    c_star = float(mp.e ** (-1) * dyadic_M(mp.mpf("0.5")) ** 2)

    def statistic(x: float) -> tuple[float, int]:
        lo = int(np.searchsorted(logs, x - 4.0, side="left"))
        hi = int(np.searchsorted(logs, x - 2.0, side="right"))
        u = x - logs[lo:hi]
        values = interpolate(window, step, u - 2.0)
        return float(np.dot(weights[lo:hi], values) - c_star * math.exp(x / 2.0)), hi - lo

    zeros = [float(mp.im(mp.zetazero(j))) for j in range(1, args.zero_count + 1)]

    def dyadic_amplitude(t: float) -> float:
        value = 1.0
        for j in range(1, 64):
            argument = t * (2.0 ** (-j)) / 2.0
            value *= 1.0 if argument == 0.0 else math.sin(argument) / argument
        return value

    zero_weights = np.asarray([dyadic_amplitude(t) ** 2 for t in zeros])
    zero_array = np.asarray(zeros)

    def zero_prediction(x: float) -> float:
        return float(-2.0 * np.sum(zero_weights * np.cos(zero_array * (x - 3.0))))

    def F_laplace(z: mp.mpf | mp.mpc) -> mp.mpc:
        return mp.e ** (-2 * z) * dyadic_M(z) ** 2

    def trivial_prediction(x: float, count: int = 20) -> float:
        total = mp.mpf(0)
        for m in range(1, count + 1):
            lam = mp.mpf(2 * m) + mp.mpf("0.5")
            total -= mp.e ** (-mp.mpf(x) * lam) * F_laplace(-lam)
        return float(mp.re(total))

    x_max = math.log(args.cutoff) + 2.0
    grid = np.linspace(6.0, x_max, args.grid_points)
    values = np.empty_like(grid)
    term_counts = np.empty(args.grid_points, dtype=np.int64)
    for index, x in enumerate(grid):
        values[index], term_counts[index] = statistic(float(x))

    minimum_index = int(np.argmin(values))
    maximum_index = int(np.argmax(values))

    checkpoints = [6.0, 8.0, 10.0, 12.0, 14.0, 16.0]
    checkpoints.extend([float(grid[minimum_index]), float(grid[maximum_index])])
    checkpoints = sorted(set(x for x in checkpoints if x <= x_max))

    comparisons = []
    for x in checkpoints:
        prime_value, count = statistic(x)
        zero_value = zero_prediction(x)
        trivial_value = trivial_prediction(x)
        comparisons.append(
            {
                "x": x,
                "a": x / 2.0,
                "prime_power_terms": count,
                "prime_statistic": prime_value,
                "zero_prediction_first_n": zero_value,
                "trivial_zero_prediction": trivial_value,
                "difference": prime_value - zero_value - trivial_value,
            }
        )

    output = {
        "classification": "EMPIRICAL_NON_DIRECTED",
        "cutoff": args.cutoff,
        "ordinary_primes": prime_count,
        "prime_power_terms": int(len(ns)),
        "fft_size": args.fft_size,
        "grid_points": args.grid_points,
        "zero_count": args.zero_count,
        "c_star": c_star,
        "window_integral": float(np.trapezoid(window, dx=step)),
        "window_minimum": float(window.min()),
        "window_maximum": float(window.max()),
        "scan": {
            "x_min": 6.0,
            "x_max": x_max,
            "minimum": {"x": float(grid[minimum_index]), "value": float(values[minimum_index])},
            "maximum": {"x": float(grid[maximum_index]), "value": float(values[maximum_index])},
        },
        "comparisons": comparisons,
        "runtime_seconds": time.time() - started,
        "proof_boundary": (
            "IEEE-754/FFT/mpmath reconnaissance; not directed and not an independent "
            "explicit-formula or prime-manifest certificate"
        ),
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
