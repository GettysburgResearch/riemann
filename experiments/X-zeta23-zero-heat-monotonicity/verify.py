#!/usr/bin/env python3
"""Finite regression for the first-Hermite Gaussian zero-heat criterion.

This script verifies closed-form identities and synthetic controls only. It does
not prove the infinite zero-set terminal theorem, the Guinand--Weil formula, the
prime-side sign, or the Riemann Hypothesis.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path
from typing import Callable


def simpson_complex(fn: Callable[[float], complex], a: float, b: float, n: int) -> complex:
    if n <= 0:
        raise ValueError("n must be positive")
    if n % 2:
        n += 1
    step = (b - a) / n
    total = fn(a) + fn(b)
    for index in range(1, n):
        total += (4 if index % 2 else 2) * fn(a + index * step)
    return total * step / 3


def round_float(value: float, digits: int = 15) -> float:
    if not math.isfinite(value):
        raise ValueError(f"non-finite value: {value}")
    return round(value, digits)


def complex_pair(value: complex) -> list[float]:
    return [round_float(value.real), round_float(value.imag)]


def spectral_square(q: float, x: float, z: complex) -> complex:
    delta = z - x
    return delta * delta * cmath.exp(-q * delta * delta)


def physical_autocorrelation(q: float, x: float, u: float) -> complex:
    return (
        cmath.exp(-1j * x * u)
        * (1 - u * u / (2 * q))
        * math.exp(-u * u / (4 * q))
        / (4 * math.sqrt(math.pi) * q ** 1.5)
    )


def normalized_three_gaussian_kernel(q: float, y: float, z: complex) -> complex:
    numerator = cmath.sinh(q * y * z)
    denominator = math.sinh(q * y * y)
    return -2 * cmath.exp(q * (z * z - y * y)) * (numerator / denominator) ** 2


def pair_contribution(q: float, x: float, t: float, y: float, multiplicity: int = 1) -> complex:
    return multiplicity * (
        spectral_square(q, x, t + 1j * y)
        + spectral_square(q, x, t - 1j * y)
    )


def zero_heat_moment(points: list[tuple[complex, int]], q: float, x: float) -> complex:
    return sum(mult * spectral_square(q, x, z) for z, mult in points)


def von_mangoldt_sieve(limit: int) -> list[float]:
    values = [0.0] * (limit + 1)
    is_prime = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        is_prime[0] = 0
    if limit >= 1:
        is_prime[1] = 0
    for p in range(2, limit + 1):
        if not is_prime[p]:
            continue
        logp = math.log(p)
        power = p
        while power <= limit:
            values[power] = logp
            if power > limit // p:
                break
            power *= p
        if p <= int(math.isqrt(limit)):
            start = p * p
            is_prime[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return values


def prime_weight_envelope(q: float, n: int) -> float:
    t = math.log(n)
    return (
        math.log(n)
        / math.sqrt(n)
        * (1 + t * t / (2 * q))
        * math.exp(-t * t / (4 * q))
        / (2 * math.sqrt(math.pi) * q ** 1.5)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    # 1. Fourier inversion of the first-Hermite autocorrelation.
    q_fourier = 1.7
    x_fourier = 2.3
    fourier_samples: dict[str, dict[str, object]] = {}
    max_fourier_error = 0.0
    for tau in (-1.1, 0.2, 2.3, 3.7):
        numeric = simpson_complex(
            lambda u: physical_autocorrelation(q_fourier, x_fourier, u)
            * cmath.exp(1j * tau * u),
            -18.0,
            18.0,
            60000,
        )
        exact = spectral_square(q_fourier, x_fourier, tau)
        error = abs(numeric - exact)
        max_fourier_error = max(max_fourier_error, error)
        fourier_samples[str(tau)] = {
            "numeric": complex_pair(numeric),
            "exact": complex_pair(exact),
            "absolute_error": round_float(error),
        }

    # 2. Confluent limit of the PR #375 three-Gaussian residue kernel.
    q_confluent = 1.3
    z_confluent = 0.44 + 0.17j
    confluent_target = -2 * z_confluent * z_confluent * cmath.exp(
        q_confluent * z_confluent * z_confluent
    )
    confluent_rows = []
    previous_error = float("inf")
    confluent_decreases = True
    for y in (0.2, 0.1, 0.05, 0.025, 0.0125):
        value = y * y * normalized_three_gaussian_kernel(q_confluent, y, z_confluent)
        error = abs(value - confluent_target)
        confluent_decreases = confluent_decreases and error < previous_error
        previous_error = error
        confluent_rows.append(
            {
                "y": y,
                "value": complex_pair(value),
                "absolute_error": round_float(error),
            }
        )

    # 3. Exact target-pair value and derivative identity.
    q_target = 2.4
    y_target = 0.23
    target_numeric = pair_contribution(q_target, 0.0, 0.0, y_target)
    target_exact = -2 * y_target * y_target * math.exp(q_target * y_target * y_target)
    derivative_step = 1e-5
    z_deriv = 0.41 + 0.19j
    finite_difference = -(
        cmath.exp(-(q_target + derivative_step) * z_deriv * z_deriv)
        - cmath.exp(-(q_target - derivative_step) * z_deriv * z_deriv)
    ) / (2 * derivative_step)
    derivative_exact = z_deriv * z_deriv * cmath.exp(-q_target * z_deriv * z_deriv)

    # 4. Threat-budget identities for an increasing-depth chain.
    depths = [0.08, 0.13, 0.19, 0.27, 0.36, 0.45]
    increments = []
    square_budget = 0.0
    for left, right in zip(depths, depths[1:]):
        r = math.sqrt(0.72 * (right * right - left * left))
        square_budget += r * r
        increments.append(
            {
                "from_depth": left,
                "to_depth": right,
                "ordinate_increment": round_float(r),
                "edge_slack": round_float(right * right - r * r - left * left),
            }
        )
    telescoping_cap = depths[-1] ** 2 - depths[0] ** 2

    # 5. Synthetic terminal packet: normalized moment converges to -multiplicity.
    x0 = 0.7
    y0 = 0.23
    target_mult = 1
    synthetic_points: list[tuple[complex, int]] = [
        (x0 + 1j * y0, target_mult),
        (x0 - 1j * y0, target_mult),
    ]
    for real_zero in (-4.0, -2.0, 0.0, 1.4, 3.2):
        synthetic_points.append((complex(real_zero, 0.0), 1))
    nuisance_pairs = [(-1.5, 0.31, 1), (1.9, 0.28, 2), (4.0, 0.45, 1), (0.74, 0.12, 1)]
    terminal_slacks = []
    for t, depth, mult in nuisance_pairs:
        slack = depth * depth - (t - x0) ** 2 - y0 * y0
        if not slack < 0:
            raise AssertionError("synthetic nuisance is not terminal")
        terminal_slacks.append(round_float(slack))
        synthetic_points.extend([(t + 1j * depth, mult), (t - 1j * depth, mult)])

    asymptotic_rows = []
    final_normalized = None
    for q in (5.0, 10.0, 20.0, 40.0, 80.0, 120.0):
        moment = zero_heat_moment(synthetic_points, q, x0)
        normalized = moment / (2 * y0 * y0 * math.exp(q * y0 * y0))
        final_normalized = normalized.real
        asymptotic_rows.append(
            {
                "q": q,
                "moment": complex_pair(moment),
                "normalized": complex_pair(normalized),
            }
        )

    # 6. Finite prime-tail envelope control.
    q_tail = 1.8
    cutoff = 2000
    limit = 120000
    mangoldt = von_mangoldt_sieve(limit)
    actual_tail = 0.0
    integer_envelope = 0.0
    for n in range(cutoff + 1, limit + 1):
        t = math.log(n)
        kernel_abs = (
            abs(1 - t * t / (2 * q_tail))
            * math.exp(-t * t / (4 * q_tail))
            / (2 * math.sqrt(math.pi) * q_tail ** 1.5)
        )
        actual_tail += mangoldt[n] / math.sqrt(n) * kernel_abs
        integer_envelope += prime_weight_envelope(q_tail, n)
    if actual_tail > integer_envelope * (1 + 1e-13):
        raise AssertionError("all-integer tail envelope failed")

    gates = {
        "first_hermite_fourier_inversion": max_fourier_error < 1e-11,
        "confluent_kernel_limit": confluent_decreases and previous_error < 2e-4,
        "target_pair_value": abs(target_numeric - target_exact) < 1e-13,
        "heat_derivative_identity": abs(finite_difference - derivative_exact) < 2e-10,
        "threat_square_budget": square_budget < telescoping_cap + 1e-14,
        "terminal_packet_asymptotic": final_normalized is not None
        and abs(final_normalized + target_mult) < 1e-3,
        "prime_tail_envelope": actual_tail <= integer_envelope,
    }
    if not all(gates.values()):
        raise SystemExit(f"verification failure: {gates}")

    output = {
        "status": "PASS_FIRST_HERMITE_ZERO_HEAT_MONOTONICITY",
        "gates": gates,
        "parameters": {
            "fourier_q": q_fourier,
            "fourier_x": x_fourier,
            "confluent_q": q_confluent,
            "target_q": q_target,
            "target_depth": y_target,
            "tail_q": q_tail,
            "tail_cutoff": cutoff,
            "tail_limit": limit,
        },
        "fourier_inversion": {
            "max_error": round_float(max_fourier_error),
            "samples": fourier_samples,
        },
        "confluent_limit": {
            "target": complex_pair(confluent_target),
            "errors_strictly_decrease": confluent_decreases,
            "rows": confluent_rows,
        },
        "target_pair": {
            "numeric": complex_pair(target_numeric),
            "exact": round_float(target_exact),
            "absolute_error": round_float(abs(target_numeric - target_exact)),
        },
        "heat_derivative": {
            "numeric": complex_pair(finite_difference),
            "exact": complex_pair(derivative_exact),
            "absolute_error": round_float(abs(finite_difference - derivative_exact)),
        },
        "threat_chain": {
            "rows": increments,
            "sum_squared_ordinate_increments": round_float(square_budget),
            "telescoping_depth_square_cap": round_float(telescoping_cap),
        },
        "synthetic_terminal_packet": {
            "terminal_slacks": terminal_slacks,
            "target_multiplicity": target_mult,
            "rows": asymptotic_rows,
        },
        "finite_tail_control": {
            "actual_von_mangoldt_tail_to_limit": round_float(actual_tail),
            "all_integer_envelope_to_limit": round_float(integer_envelope),
        },
    }

    rendered = json.dumps(output, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
