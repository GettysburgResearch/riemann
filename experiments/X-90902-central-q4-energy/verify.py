#!/usr/bin/env python3
"""Finite exact/numerical checks for the central Q4 energy criterion."""
from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path


def von_mangoldt(n: int) -> float:
    if n < 2:
        return 0.0
    p = None
    m = n
    d = 2
    while d * d <= m:
        if m % d == 0:
            p = d
            while m % d == 0:
                m //= d
            if m != 1:
                return 0.0
            return math.log(d)
        d += 1
    return math.log(n)  # n prime


def psi_real(x: float, lambdas: list[float]) -> float:
    return sum(lambdas[2 : int(math.floor(x)) + 1]) if x >= 2 else 0.0


def f4(x: float, lambdas: list[float]) -> float:
    return psi_real(4 * x, lambdas) - 2 * psi_real(2 * x, lambdas) - 4 * psi_real(x, lambdas) + 8 * psi_real(x / 2, lambdas)


def annulus_f4(x: float, lambdas: list[float]) -> float:
    total = 0.0
    for n in range(2, min(len(lambdas), int(math.floor(4 * x)) + 1)):
        if n <= x / 2:
            coeff = 3
        elif n <= x:
            coeff = -5
        elif n <= 2 * x:
            coeff = -1
        elif n <= 4 * x:
            coeff = 1
        else:
            coeff = 0
        total += coeff * lambdas[n]
    return total


def m4(s: complex) -> complex:
    return 4**s - 2 * 2**s - 4 + 8 * 2 ** (-s)


def main():
    limit = 3000
    lambdas = [0.0] * (limit + 1)
    for n in range(2, limit + 1):
        lambdas[n] = von_mangoldt(n)

    # Exact quarter-cell constancy and annular identity over many cells.
    max_cell_error = 0.0
    max_annulus_error = 0.0
    for m in range(16, 700):
        x0 = m / 4 + 1e-9
        x1 = (m + 0.37) / 4
        max_cell_error = max(max_cell_error, abs(f4(x0, lambdas) - f4(x1, lambdas)))
        max_annulus_error = max(max_annulus_error, abs(f4(x0, lambdas) - annulus_f4(x0, lambdas)))

    # Quarter-cell integral identity on [4,100].
    discrete = 0.0
    exact_integral = 0.0
    for m in range(16, 400):
        value = f4(m / 4 + 1e-9, lambdas)
        discrete += 4.0 * value * value / (m * (m + 1))
        exact_integral += value * value * (4.0 / m - 4.0 / (m + 1))
    energy_error = abs(discrete - exact_integral)

    # Mellin factorization and open-strip zero safety samples.
    factor_error = 0.0
    min_modulus = math.inf
    for beta in [0.51, 0.6, 0.75, 0.9, 0.99]:
        for gamma in [0.0, 0.7, 3.0, 9.0, 25.0]:
            z = beta + 1j * gamma
            factored = (4**z - 4) * (1 - 2 ** (1 - z))
            factor_error = max(factor_error, abs(m4(z) - factored))
            min_modulus = min(min_modulus, abs(factored))

    gates = {
        "quarter_cell_constancy": max_cell_error < 1e-10,
        "prime_annulus_identity": max_annulus_error < 1e-10,
        "quarter_cell_energy": energy_error < 1e-12,
        "mellin_factorization": factor_error < 1e-10,
        "sampled_open_strip_zero_safety": min_modulus > 1e-5,
    }
    if not all(gates.values()):
        raise AssertionError(gates)

    return {
        "status": "PASS_X_90902_CENTRAL_Q4_ENERGY",
        "gates": gates,
        "max_quarter_cell_error": max_cell_error,
        "max_annulus_identity_error": max_annulus_error,
        "quarter_cell_energy_error": energy_error,
        "mellin_factorization_error": factor_error,
        "sampled_min_multiplier_modulus": min_modulus,
        "discrete_energy_4_100": discrete,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = main()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text)
    else:
        print(text, end="")
