#!/usr/bin/env python3
"""Memory-conscious empirical search for exact finite rational filters.

The filter ledger is exact, but FFT inversion, interpolation, mpmath zeros and
prime accumulation in this script are ordinary reconnaissance arithmetic.  Use
``filter_core.py`` for the independent exact-rational small-support checker and
``rh_bound.py`` for the fail-closed rational RH envelope.
"""
from __future__ import annotations

import argparse
import json
import math
import time
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

import numpy as np

from filter_core import FilterSpec, qtext, standard_spec


def prime_power_arrays(limit: int) -> tuple[np.ndarray, np.ndarray, dict[str, object]]:
    sieve = np.ones(limit + 1, dtype=np.bool_)
    sieve[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    primes = np.nonzero(sieve)[0]

    ns: list[int] = []
    ps: list[int] = []
    exponents: list[int] = []
    for raw_p in primes:
        p = int(raw_p)
        value = p
        k = 1
        while value <= limit:
            ns.append(value)
            ps.append(p)
            exponents.append(k)
            if value > limit // p:
                break
            value *= p
            k += 1

    n_array = np.asarray(ns, dtype=np.int64)
    p_array = np.asarray(ps, dtype=np.int64)
    k_array = np.asarray(exponents, dtype=np.int16)
    order = np.argsort(n_array, kind="stable")
    n_array = n_array[order]
    p_array = p_array[order]
    k_array = k_array[order]
    weights = np.log(p_array.astype(np.float64)) / np.sqrt(n_array.astype(np.float64))

    digest = sha256()
    for n, p, k in zip(n_array, p_array, k_array):
        digest.update(f"{int(n)},{int(p)},{int(k)}\n".encode("ascii"))
    histogram = Counter(int(k) for k in k_array)
    manifest = {
        "format": "sorted ASCII records n,p,k with newline",
        "sha256": digest.hexdigest(),
        "cutoff": limit,
        "ordinary_prime_count": int(len(primes)),
        "prime_power_count": int(len(n_array)),
        "first_records": [
            [int(n), int(p), int(k)]
            for n, p, k in zip(n_array[:8], p_array[:8], k_array[:8])
        ],
        "last_records": [
            [int(n), int(p), int(k)]
            for n, p, k in zip(n_array[-8:], p_array[-8:], k_array[-8:])
        ],
        "exponent_histogram": {str(k): v for k, v in sorted(histogram.items())},
        "duplicate_n_count": int(len(n_array) - len(np.unique(n_array))),
        "regeneration": "prime_power_arrays in search.py; no bulk manifest committed",
    }
    return n_array, weights, manifest


def build_density(spec: FilterSpec, fft_size: int) -> tuple[np.ndarray, float, float]:
    widths = np.asarray([float(w) for w in spec.widths], dtype=np.float64)
    length = float(sum(spec.widths, Fraction(0)))
    density_support = 2.0 * length
    period = 2.0 ** math.ceil(math.log2(max(4.0, density_support + 1.0)))
    step = period / fft_size
    freq = np.fft.fftfreq(fft_size, d=step) * (2.0 * np.pi)
    amplitude = np.ones(fft_size, dtype=np.float64)
    for width in widths:
        amplitude *= np.sinc((freq * width / 2.0) / np.pi)
    transform = np.exp(-1j * freq * length) * amplitude * amplitude
    samples = np.fft.ifft((fft_size / period) * transform).real
    return samples, step, density_support


def interpolate(samples: np.ndarray, step: float, points: np.ndarray) -> np.ndarray:
    position = points / step
    left = np.floor(position).astype(np.int64)
    fraction = position - left
    left = np.clip(left, 0, len(samples) - 2)
    return samples[left] * (1.0 - fraction) + samples[left + 1] * fraction


def make_window(spec: FilterSpec, samples: np.ndarray, step: float, density_support: float):
    base_shift = float(spec.base_shift)
    delta = float(spec.highpass_delta)
    order = spec.highpass_order
    h = math.log(4.0)

    def fstar(points: np.ndarray) -> np.ndarray:
        y = points - base_shift
        out = np.zeros_like(points, dtype=np.float64)
        mask = (y >= 0.0) & (y <= density_support)
        if np.any(mask):
            out[mask] = interpolate(samples, step, y[mask])
        return out

    coefficients = [((-1.0) ** j) * math.comb(order, j) / (2.0**order) for j in range(order + 1)]

    def window(points: np.ndarray) -> np.ndarray:
        out = np.zeros_like(points, dtype=np.float64)
        for j, coefficient in enumerate(coefficients):
            shifted = points - j * delta
            out += coefficient * (fstar(shifted) - 2.0 * fstar(shifted - h))
        return out

    return window


def spectral_model(spec: FilterSpec, zero_count: int):
    if zero_count <= 0:
        return None
    try:
        import mpmath as mp
    except ImportError as exc:  # pragma: no cover - environment-dependent
        raise SystemExit("mpmath is required when --zero-count is positive") from exc
    mp.mp.dps = 60
    zeros = np.asarray([float(mp.im(mp.zetazero(j))) for j in range(1, zero_count + 1)])
    widths = [float(w) for w in spec.widths]
    length = float(spec.profile_length)
    h = math.log(4.0)
    delta = float(spec.highpass_delta)
    coefficients = []
    for t in zeros:
        amplitude = 1.0
        for width in widths:
            a = width * t / 2.0
            amplitude *= (1.0 if a == 0.0 else math.sin(a) / a) ** 2
        fhat = np.exp(-1j * t * (float(spec.base_shift) + length)) * amplitude
        pole = 1.0 - 2.0 * np.exp(-1j * h * t)
        highpass = ((1.0 - np.exp(-1j * delta * t)) / 2.0) ** spec.highpass_order
        coefficients.append(fhat * pole * highpass)
    coeff = np.asarray(coefficients, dtype=np.complex128)
    return {
        "zeros": zeros,
        "coefficients": coeff,
        "listed_absolute_sum": float(2.0 * np.sum(np.abs(coeff))),
        "listed_variance": float(2.0 * np.sum(np.abs(coeff) ** 2)),
    }


def contiguous_runs(mask: np.ndarray) -> list[tuple[int, int]]:
    if len(mask) == 0:
        return []
    changes = np.diff(np.concatenate(([False], mask, [False])).astype(np.int8))
    starts = np.nonzero(changes == 1)[0]
    ends = np.nonzero(changes == -1)[0] - 1
    return list(zip(starts.tolist(), ends.tolist()))


def scan_one(
    spec: FilterSpec,
    ns: np.ndarray,
    weights: np.ndarray,
    *,
    cutoff: int,
    fft_size: int,
    grid_points: int,
    zero_count: int,
    scan_floor: float,
) -> dict[str, object]:
    samples, step, density_support = build_density(spec, fft_size)
    window = make_window(spec, samples, step, density_support)
    logs = np.log(ns.astype(np.float64))
    support_hi = float(spec.support_max_interval(80)[1])
    support_lo = float(spec.support_min)
    x_min = max(support_hi, scan_floor)
    x_max = math.log(cutoff) + support_lo
    if x_min >= x_max:
        raise ValueError("cutoff leaves no complete-support scan interval")
    grid = np.linspace(x_min, x_max, grid_points)
    values = np.empty(grid_points, dtype=np.float64)
    counts = np.empty(grid_points, dtype=np.int64)
    for index, x in enumerate(grid):
        lo = int(np.searchsorted(logs, x - support_hi, side="left"))
        hi = int(np.searchsorted(logs, x - support_lo, side="right"))
        u = x - logs[lo:hi]
        values[index] = float(np.dot(weights[lo:hi], window(u)))
        counts[index] = hi - lo

    min_index = int(np.argmin(values))
    max_index = int(np.argmax(values))
    abs_index = int(np.argmax(np.abs(values)))
    spectral = spectral_model(spec, zero_count)
    spectral_summary: dict[str, object] | None = None
    exceedance_intervals: list[dict[str, object]] = []
    max_prediction_error = None
    if spectral is not None:
        zeros = spectral["zeros"]
        coeff = spectral["coefficients"]
        prediction = -2.0 * np.real(np.exp(1j * np.outer(grid, zeros)) @ coeff)
        max_prediction_error = float(np.max(np.abs(values - prediction)))
        moat = float(spectral["listed_absolute_sum"])
        for sign, mask in ((1, values > moat), (-1, values < -moat)):
            for left, right in contiguous_runs(mask):
                exceedance_intervals.append(
                    {
                        "sign": sign,
                        "x_grid_interval": [float(grid[left]), float(grid[right])],
                        "sample_count": right - left + 1,
                        "sampled_inf_abs_Q": float(np.min(np.abs(values[left : right + 1]))),
                        "listed_zero_moat": moat,
                    }
                )
        spectral_summary = {
            "classification": "EMPIRICAL_MPMATH_MIDPOINT_ZEROS",
            "zero_count": zero_count,
            "listed_absolute_sum": moat,
            "listed_variance": float(spectral["listed_variance"]),
            "listed_rms": math.sqrt(float(spectral["listed_variance"])),
            "max_direct_minus_listed_prediction_abs": max_prediction_error,
            "truncated_moat_exceedance_intervals": exceedance_intervals,
            "warning": "The listed-zero moat omits every higher zero and is not RH-valid.",
        }

    # Independently of any moat, retain a narrow, same-sign sampled interval
    # around the largest absolute observation.
    sign = 1 if values[abs_index] >= 0 else -1
    target = 0.95 * abs(values[abs_index])
    mask = (sign * values) >= target
    selected = next((run for run in contiguous_runs(mask) if run[0] <= abs_index <= run[1]), (abs_index, abs_index))
    left, right = selected

    return {
        "classification": "EMPIRICAL_NON_DIRECTED",
        "filter": {
            "widths": [qtext(w) for w in spec.widths],
            "dyadic_box_count": sum(1 for w in spec.widths if w.denominator & (w.denominator - 1) == 0 and w.numerator == 1),
            "total_box_count_before_square": len(spec.widths),
            "profile_support_cost": qtext(spec.profile_length),
            "convolution_square_support_cost": qtext(2 * spec.profile_length),
            "base_shift": qtext(spec.base_shift),
            "highpass_order": spec.highpass_order,
            "highpass_delta": qtext(spec.highpass_delta),
            "support_max": support_hi,
        },
        "fft": {
            "fft_size": fft_size,
            "step": step,
            "period": step * fft_size,
            "density_support": density_support,
            "density_integral": float(np.trapezoid(samples, dx=step)),
            "density_minimum": float(samples.min()),
            "density_maximum": float(samples.max()),
        },
        "scan": {
            "cutoff": cutoff,
            "grid_points": grid_points,
            "x_min": x_min,
            "x_max": x_max,
            "minimum": {"x": float(grid[min_index]), "value": float(values[min_index])},
            "maximum": {"x": float(grid[max_index]), "value": float(values[max_index])},
            "empirical_mean_square": float(np.mean(values * values)),
            "empirical_rms": float(np.sqrt(np.mean(values * values))),
            "prime_terms_min": int(counts.min()),
            "prime_terms_max": int(counts.max()),
            "strongest_sign_separated_grid_interval": {
                "sign": sign,
                "x_grid_interval": [float(grid[left]), float(grid[right])],
                "sampled_inf_abs_Q": float(np.min(np.abs(values[left : right + 1]))),
                "threshold_definition": "0.95 * largest sampled |Q|",
            },
        },
        "spectral": spectral_summary,
        "proof_boundary": (
            "Exact rational filter definition and complete deterministic integer manifest, "
            "but FFT/interpolation/prime accumulation and mpmath zero midpoints are ordinary "
            "floating reconnaissance. Every interval here is a sampled grid interval."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoff", type=int, default=1_000_000)
    parser.add_argument("--fft-size", type=int, default=1 << 18)
    parser.add_argument("--grid-points", type=int, default=2_000)
    parser.add_argument("--dyadic-level", type=int, default=8)
    parser.add_argument("--notches", default="0,1,2")
    parser.add_argument("--highpass-order", type=int, default=0)
    parser.add_argument("--highpass-delta-power", type=int, default=6)
    parser.add_argument("--zero-count", type=int, default=50)
    parser.add_argument(
        "--scan-floor",
        type=float,
        default=14.0,
        help="discard the compact trivial-zero transient below this x",
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.cutoff < 100 or args.fft_size < 1024 or args.grid_points < 10:
        raise SystemExit("invalid search parameters")
    notch_counts = sorted({int(item) for item in args.notches.split(",")})

    started = time.time()
    ns, weights, manifest = prime_power_arrays(args.cutoff)
    ladders = []
    for notch_count in notch_counts:
        spec = standard_spec(
            dyadic_level=args.dyadic_level,
            notch_count=notch_count,
            highpass_order=args.highpass_order,
            highpass_delta=Fraction(1, 1 << args.highpass_delta_power),
        )
        ladders.append(
            scan_one(
                spec,
                ns,
                weights,
                cutoff=args.cutoff,
                fft_size=args.fft_size,
                grid_points=args.grid_points,
                zero_count=args.zero_count,
                scan_floor=args.scan_floor,
            )
        )
    output = {
        "classification": "EMPIRICAL_NON_DIRECTED",
        "manifest": manifest,
        "ladders": ladders,
        "runtime_seconds": time.time() - started,
        "environment": {"numpy": np.__version__},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
