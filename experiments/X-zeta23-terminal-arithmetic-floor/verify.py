#!/usr/bin/env python3
"""Finite regression for the terminal-Gaussian arithmetic-floor normal form.

This script checks the exact Gaussian cardinal transform, its real-axis square,
the closed autocorrelation kernel, the completed-Chebyshev Stieltjes normal
form, the vanishing archimedean-scale mass, and the support/moment resource
barrier. It is a finite numerical/algebraic regression, not a proof of the
cofinal one-sided Chebyshev-discrepancy inequality and not a proof of RH.
"""
from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path

import numpy as np


def transform(w: complex, sigma: float, x: float, y: float) -> complex:
    a = sigma * sigma * y * y
    denominator = math.exp(2.0 * a) - 1.0
    return (
        cmath.exp(-0.5 * sigma * sigma * (w - (x - 1j * y)) ** 2)
        - cmath.exp(-0.5 * sigma * sigma * (w - (x + 1j * y)) ** 2)
    ) / denominator


def real_square(t: np.ndarray, sigma: float, x: float, y: float) -> np.ndarray:
    a = sigma * sigma * y * y
    denominator = math.exp(2.0 * a) - 1.0
    r = t - x
    return (
        4.0
        * np.exp(a - sigma * sigma * r * r)
        * np.sin(sigma * sigma * y * r) ** 2
        / denominator**2
    )


def prefactor(sigma: float, y: float) -> float:
    a = sigma * sigma * y * y
    denominator = math.exp(2.0 * a) - 1.0
    return math.exp(a) / (math.sqrt(math.pi) * sigma * denominator**2)


def shell(v: np.ndarray | float, sigma: float, y: float) -> np.ndarray:
    value = np.asarray(v, dtype=float)
    shift = 2.0 * sigma * sigma * y
    return (
        np.exp(-(value**2) / (4.0 * sigma * sigma))
        - 0.5 * np.exp(-((value - shift) ** 2) / (4.0 * sigma * sigma))
        - 0.5 * np.exp(-((value + shift) ** 2) / (4.0 * sigma * sigma))
    )


def shell_derivative(v: np.ndarray | float, sigma: float, y: float) -> np.ndarray:
    value = np.asarray(v, dtype=float)
    shift = 2.0 * sigma * sigma * y
    g0 = np.exp(-(value**2) / (4.0 * sigma * sigma))
    gp = np.exp(-((value - shift) ** 2) / (4.0 * sigma * sigma))
    gm = np.exp(-((value + shift) ** 2) / (4.0 * sigma * sigma))
    return (
        -value * g0 / (2.0 * sigma * sigma)
        + (value - shift) * gp / (4.0 * sigma * sigma)
        + (value + shift) * gm / (4.0 * sigma * sigma)
    )


def autocorrelation(v: np.ndarray | float, sigma: float, x: float, y: float) -> np.ndarray:
    value = np.asarray(v, dtype=float)
    return prefactor(sigma, y) * np.exp(-1j * x * value) * shell(value, sigma, y)


def symmetric_kernel(v: np.ndarray | float, sigma: float, x: float, y: float) -> np.ndarray:
    value = np.asarray(v, dtype=float)
    return 2.0 * prefactor(sigma, y) * shell(value, sigma, y) * np.cos(x * value)


def completed_weight_derivative(v: np.ndarray, sigma: float, x: float, y: float) -> np.ndarray:
    h = shell(v, sigma, y)
    hp = shell_derivative(v, sigma, y)
    return 2.0 * prefactor(sigma, y) * np.exp(-v / 2.0) * (
        (hp - 0.5 * h) * np.cos(x * v) - x * h * np.sin(x * v)
    )


def spectral_mass(sigma: float, y: float) -> float:
    a = sigma * sigma * y * y
    denominator = math.exp(2.0 * a) - 1.0
    return 2.0 * math.sqrt(math.pi) * (math.exp(a) - 1.0) / (
        sigma * denominator**2
    )


def von_mangoldt(cutoff: int) -> np.ndarray:
    values = np.zeros(cutoff + 1, dtype=float)
    is_prime = np.ones(cutoff + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, int(cutoff**0.5) + 1):
        if is_prime[p]:
            is_prime[p * p : cutoff + 1 : p] = False
    for p0 in np.nonzero(is_prime)[0]:
        p = int(p0)
        q = p
        logp = math.log(p)
        while q <= cutoff:
            values[q] = logp
            if q > cutoff // p:
                break
            q *= p
    return values


def run() -> dict[str, object]:
    sigma = 1.5
    x = 3.7
    y = 0.23
    t_max = 13.0
    grid_points = 240_001

    z = x + 1j * y
    z_reflected = x - 1j * y
    target_values = [transform(z, sigma, x, y), transform(z_reflected, sigma, x, y)]

    spectral_grid = np.linspace(x - 8.0, x + 8.0, grid_points)
    square_values = real_square(spectral_grid, sigma, x, y)
    mass_numeric = float(np.trapezoid(square_values, spectral_grid))
    mass_exact = spectral_mass(sigma, y)

    correlation_samples: dict[str, object] = {}
    correlation_errors: list[float] = []
    for shift in (0.0, 0.3, 2.0, 4.0):
        numeric = np.trapezoid(
            square_values * np.exp(-1j * spectral_grid * shift), spectral_grid
        ) / (2.0 * math.pi)
        exact = complex(autocorrelation(shift, sigma, x, y))
        error = abs(numeric - exact)
        correlation_errors.append(float(error))
        correlation_samples[str(shift)] = {
            "numeric": [float(numeric.real), float(numeric.imag)],
            "exact": [float(exact.real), float(exact.imag)],
            "absolute_error": float(error),
        }

    prime_cutoff = int(math.exp(t_max))
    mangoldt = von_mangoldt(prime_cutoff)
    psi = np.cumsum(mangoldt)
    t_grid = np.linspace(0.0, t_max, grid_points)
    integer_points = np.floor(np.exp(t_grid)).astype(int)
    theta = psi[integer_points] - np.exp(t_grid) + 1.0

    discrepancy_integral = float(
        np.trapezoid(
            theta * completed_weight_derivative(t_grid, sigma, x, y), t_grid
        )
    )
    low_pole_remainder = float(
        np.trapezoid(
            np.exp(-t_grid / 2.0) * symmetric_kernel(t_grid, sigma, x, y),
            t_grid,
        )
    )
    pole_integral = float(
        np.trapezoid(
            (np.exp(t_grid / 2.0) + np.exp(-t_grid / 2.0))
            * symmetric_kernel(t_grid, sigma, x, y),
            t_grid,
        )
    )
    support = np.nonzero(mangoldt)[0]
    support = support[support >= 2]
    prime_sum = float(
        np.sum(
            mangoldt[support]
            / np.sqrt(support)
            * symmetric_kernel(np.log(support), sigma, x, y)
        )
    )
    direct_value = pole_integral - prime_sum
    normal_form_value = low_pole_remainder + discrepancy_integral
    normal_form_error = abs(direct_value - normal_form_value)

    decay = []
    for sigma_value in (2.0, 3.0, 4.0, 5.0):
        decay.append(
            {
                "sigma": sigma_value,
                "a": sigma_value * sigma_value * y * y,
                "spectral_mass": spectral_mass(sigma_value, y),
                "autocorrelation_prefactor": prefactor(sigma_value, y),
            }
        )

    moment_barrier = []
    for depth in (0.01, 0.10, 0.25, 0.49):
        moment_barrier.append(
            {
                "off_line_depth": depth,
                "largest_exponent_from_r_lambda_below_2": 2.0 * depth,
                "strictly_below_compression_dimension_exponent": 2.0 * depth < 1.0,
            }
        )

    gates = {
        "target_values": max(abs(target_values[0] - 1.0), abs(target_values[1] + 1.0))
        < 1e-12,
        "spectral_mass_formula": abs(mass_numeric - mass_exact) < 1e-10,
        "autocorrelation_formula": max(correlation_errors) < 1e-10,
        "completed_chebyshev_normal_form": normal_form_error < 3e-4,
        "mass_decay": all(
            decay[index + 1]["spectral_mass"] < decay[index]["spectral_mass"]
            for index in range(len(decay) - 1)
        ),
        "moment_support_barrier": all(
            item["strictly_below_compression_dimension_exponent"]
            for item in moment_barrier
        ),
    }

    return {
        "status": (
            "PASS_TERMINAL_GAUSSIAN_ARITHMETIC_FLOOR_NORMAL_FORM"
            if all(gates.values())
            else "FAIL"
        ),
        "parameters": {
            "sigma": sigma,
            "x": x,
            "y": y,
            "t_max": t_max,
            "prime_cutoff": prime_cutoff,
            "grid_points": grid_points,
        },
        "gates": gates,
        "target_values": [
            [float(target_values[0].real), float(target_values[0].imag)],
            [float(target_values[1].real), float(target_values[1].imag)],
        ],
        "spectral_mass": {
            "numeric": mass_numeric,
            "exact": mass_exact,
            "absolute_error": abs(mass_numeric - mass_exact),
        },
        "autocorrelation_samples": correlation_samples,
        "normal_form": {
            "pole_integral": pole_integral,
            "prime_sum": prime_sum,
            "low_pole_remainder": low_pole_remainder,
            "completed_chebyshev_discrepancy_integral": discrepancy_integral,
            "direct_pole_minus_prime": direct_value,
            "normal_form_value": normal_form_value,
            "absolute_error": normal_form_error,
        },
        "decay": decay,
        "moment_support_barrier": moment_barrier,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = run()
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text + "\n", encoding="utf-8")
    if payload["status"] == "FAIL":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
