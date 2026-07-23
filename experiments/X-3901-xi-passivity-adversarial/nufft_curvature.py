#!/usr/bin/env python3
"""Moment-corrected NUFFT nomination scan for no-remainder Hardy curvature.

STATUS: ordinary floating discovery arithmetic. The raw moment Taylor bounds do
not enclose the final curvature near a small Hardy sum. Retained signs require
direct exact-point escalation.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from decimal import Decimal, getcontext
import json
import math
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np

TWO_PI_LD = np.longdouble(2) * np.longdouble(np.pi)


def theta_data(t_text: str, dps: int = 50) -> tuple[np.longdouble, ...]:
    with mp.workdps(dps):
        t = mp.mpf(t_text)
        z = mp.mpf("0.25") + mp.j * t / 2
        theta = mp.siegeltheta(t)
        psi = mp.digamma(z)
        psi1 = mp.polygamma(1, z)
        theta1 = mp.re(psi) / 2 - mp.log(mp.pi) / 2
        theta2 = -mp.im(psi1) / 4
        completion2 = (
            2 * (mp.mpf("0.25") - t * t) / (t * t + mp.mpf("0.25")) ** 2
            - mp.re(psi1) / 4
        )
        return tuple(
            np.longdouble(mp.nstr(value, 40))
            for value in (theta, theta1, theta2, completion2)
        )


def direct_no_remainder(t_text: str) -> dict[str, float | int | str]:
    t = np.longdouble(t_text)
    theta, theta1, theta2, completion2 = theta_data(t_text)
    n_max = int(np.floor(np.sqrt(t / TWO_PI_LD)))
    n = np.arange(1, n_max + 1, dtype=np.int64)
    log_n = np.log(n.astype(np.longdouble))
    weight = 1 / np.sqrt(n.astype(np.float64))
    phase = np.remainder(theta - t * log_n, TWO_PI_LD).astype(np.float64)
    frequency = (theta1 - log_n).astype(np.float64)
    cosine = np.cos(phase)
    sine = np.sin(phase)
    z0 = 2 * np.sum(weight * cosine, dtype=np.float64)
    z1 = -2 * np.sum(weight * sine * frequency, dtype=np.float64)
    z2 = 2 * np.sum(
        weight * (-cosine * frequency * frequency - sine * float(theta2)),
        dtype=np.float64,
    )
    curvature = -(float(completion2) + z2 / z0 - (z1 / z0) ** 2)
    return {
        "t": t_text,
        "riemann_siegel_terms": n_max,
        "hardy_Z_no_remainder": float(z0),
        "curvature_no_remainder": float(curvature),
    }


def scan(
    *, center_text: str, spacing_text: str, points: int, order: int
) -> dict[str, Any]:
    if points < 4 or points & (points - 1):
        raise ValueError("points must be a power of two >= 4")
    if order < 1:
        raise ValueError("order must be positive")
    center_dec = Decimal(center_text)
    spacing_dec = Decimal(spacing_text)
    if spacing_dec <= 0:
        raise ValueError("spacing must be positive")

    center = np.longdouble(center_text)
    spacing = np.longdouble(spacing_text)
    half = points // 2
    low = center - spacing * half
    high = center + spacing * (half - 1)
    n_low = int(np.floor(np.sqrt(low / TWO_PI_LD)))
    n_high = int(np.floor(np.sqrt(high / TWO_PI_LD)))
    if n_low != n_high:
        raise ValueError("Riemann--Siegel truncation index changes across the grid")
    n_max = n_low

    n = np.arange(1, n_max + 1, dtype=np.int64)
    log_n_ld = np.log(n.astype(np.longdouble))
    log_n = log_n_ld.astype(np.float64)
    amplitude = 1 / np.sqrt(n.astype(np.float64))
    theta0, theta1, theta2, completion2 = theta_data(center_text)

    base_phase = np.remainder(-center * log_n_ld, TWO_PI_LD).astype(np.float64)
    base = amplitude * (np.cos(base_phase) + np.j * np.sin(base_phase))

    frequency = (np.longdouble(points) * spacing * log_n_ld / TWO_PI_LD).astype(
        np.float64
    )
    bins = np.rint(frequency).astype(np.int64)
    residual = frequency - bins
    bins %= points

    signed = np.arange(points, dtype=np.int64)
    signed[signed > half] -= points
    expansion = -2j * np.pi * signed / points
    outputs = [np.zeros(points, dtype=np.complex128) for _ in range(3)]
    log_powers = (np.ones(n_max), log_n, log_n * log_n)
    residual_power = np.ones(n_max)
    factorial = 1

    for r in range(order + 1):
        if r:
            residual_power *= residual
            factorial *= r
        moment = residual_power / factorial
        output_factor = expansion**r
        for p in range(3):
            weights = base * log_powers[p] * moment
            bucket = np.bincount(
                bins, weights=weights.real, minlength=points
            ) + 1j * np.bincount(bins, weights=weights.imag, minlength=points)
            outputs[p] += output_factor * np.fft.fft(bucket)

    offsets = signed.astype(np.float64) * float(spacing)
    theta0_mod = float(np.remainder(theta0, TWO_PI_LD))
    theta1_array = float(theta1) + float(theta2) * offsets
    theta_phase = np.remainder(
        theta0_mod
        + float(theta1) * offsets
        + 0.5 * float(theta2) * offsets * offsets,
        2 * np.pi,
    )
    exponential = np.cos(theta_phase) + 1j * np.sin(theta_phase)
    s0, s1, s2 = outputs
    z0 = 2 * np.real(exponential * s0)
    z1 = 2 * np.real(exponential * (1j * theta1_array * s0 - 1j * s1))
    z2 = 2 * np.real(
        exponential
        * (
            (-theta1_array * theta1_array + 1j * float(theta2)) * s0
            + 2 * theta1_array * s1
            - s2
        )
    )
    curvature = -(float(completion2) + z2 / z0 - (z1 / z0) ** 2)

    eta = np.pi / 2
    raw_bounds = []
    for p in range(3):
        total_weight = np.sum(amplitude * log_powers[p])
        raw_bounds.append(
            float(
                total_weight
                * math.exp(eta)
                * eta ** (order + 1)
                / math.factorial(order + 1)
            )
        )

    minimum_index = int(np.nanargmin(curvature))
    minimum_offset_index = int(signed[minimum_index])
    minimum_t = center_dec + spacing_dec * minimum_offset_index
    negative_indices = np.flatnonzero(curvature < 0)

    return {
        "schema": "riemann.xi-nufft-curvature-scan.v1",
        "status": "EMPIRICAL_NOT_CERTIFIED",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "center": center_text,
            "spacing": spacing_text,
            "points": points,
            "signed_offset_index_min": -half,
            "signed_offset_index_max": half - 1,
            "taylor_order": order,
            "riemann_siegel_terms": n_max,
            "phase_rule": (
                "exact decimal center parsed to longdouble; high-precision theta "
                "reduced modulo 2*pi before binary64 output phases"
            ),
        },
        "raw_moment_taylor_bounds": {
            "S0": raw_bounds[0],
            "S1": raw_bounds[1],
            "S2": raw_bounds[2],
            "warning": "These do not enclose division by a small Hardy sum.",
        },
        "summary": {
            "negative_count": int(len(negative_indices)),
            "minimum_curvature": float(curvature[minimum_index]),
            "minimum_t": format(minimum_t, "f"),
            "minimum_signed_offset_index": minimum_offset_index,
            "minimum_hardy_Z": float(z0[minimum_index]),
        },
        "counterexample_candidate": None,
        "warning": (
            "This is a nomination scan. Every retained point requires direct "
            "exact-input replay and directed xi/zeta balls."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--center", required=True)
    parser.add_argument("--spacing", default="0.01")
    parser.add_argument("--points", type=int, default=65536)
    parser.add_argument("--order", type=int, default=18)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--direct", help="evaluate one exact decimal ordinate instead")
    args = parser.parse_args()
    if args.direct is not None:
        result: dict[str, Any] = direct_no_remainder(args.direct)
    else:
        getcontext().prec = 80
        result = scan(
            center_text=args.center,
            spacing_text=args.spacing,
            points=args.points,
            order=args.order,
        )
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
