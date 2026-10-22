#!/usr/bin/env python3
"""Finite regression for L-90905/T-90903.

No zeta zero table is used.  The script checks exact rational coefficient
identities and high-precision synthetic functional-equation controls.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Dict

import mpmath as mp

Laurent = Dict[int, Fraction]
Rows = Dict[int, Laurent]


def add_term(poly: Laurent, exponent: int, value: Fraction) -> None:
    poly[exponent] = poly.get(exponent, Fraction(0)) + value
    if poly[exponent] == 0:
        del poly[exponent]


def coefficient_rows(max_k: int) -> list[list[Fraction]]:
    rows: Rows = {
        0: {-3: Fraction(1, 2)},
        1: {-2: Fraction(-1, 2)},
        2: {-1: Fraction(-1, 2)},
    }
    out: list[list[Fraction]] = []
    for k in range(max_k + 1):
        out.append([sum(rows.get(j, {}).values(), Fraction(0)) for j in range(k + 3)])
        if k == max_k:
            break
        nxt: Rows = {}
        for j, poly in rows.items():
            # -(2r)^-1 d/dr [c_j(r)]
            for exponent, value in poly.items():
                add_term(nxt.setdefault(j, {}), exponent - 2, -Fraction(exponent, 2) * value)
                # -(2r)^-1 c_j(r) X^(j+1)
                add_term(nxt.setdefault(j + 1, {}), exponent - 1, -Fraction(1, 2) * value)
        rows = nxt
    return out


def partial_fraction_a(k: int, j: int) -> Fraction:
    """[w^(k+3-j)] (1-w)^2/(2-w)^(k+3)."""
    r = k + 3
    m = r - j
    total = Fraction(0)
    for ell in range(0, min(2, m) + 1):
        n = m - ell
        total += (
            Fraction((-1) ** ell * math.comb(2, ell), 1)
            * Fraction(math.comb(r + n - 1, n), 2 ** (r + n))
        )
    return total


def kappa(k: int, z: mp.mpc) -> mp.mpc:
    return -2 * mp.factorial(k + 2) * z * z / (1 - z * z) ** (k + 3)


def synthetic_roots() -> list[mp.mpc]:
    a_values = [mp.mpc("0.2", "0.3"), mp.mpc("0.2", "-0.3"), mp.mpc("0", "0.7")]
    roots: list[mp.mpc] = []
    for a in a_values:
        roots.extend([mp.mpf("0.5") + a, mp.mpf("0.5") - a])
    return roots


def xcal_from_roots(roots: list[mp.mpc], s: mp.mpc) -> mp.mpc:
    return -sum(1 / (s - rho) for rho in roots)


def xcal_derivative(roots: list[mp.mpc], s: mp.mpc, order: int) -> mp.mpc:
    return ((-1) ** (order + 1)) * mp.factorial(order) * sum(
        1 / (s - rho) ** (order + 1) for rho in roots
    )


def h_from_row(roots: list[mp.mpc], s: mp.mpc, row: list[Fraction]) -> mp.mpc:
    return sum(
        (mp.mpf(coeff.numerator) / coeff.denominator)
        * xcal_derivative(roots, s + 1, j)
        for j, coeff in enumerate(row)
    )


def three_point(roots: list[mp.mpc], s: mp.mpc, alpha: mp.mpf, y: mp.mpf) -> mp.mpc:
    r = mp.sqrt(alpha)
    q = mp.sqrt(alpha + y * y)
    return xcal_from_roots(roots, s + r) / r - (
        xcal_from_roots(roots, s + q - y) + xcal_from_roots(roots, s + q + y)
    ) / (2 * q)


def confluent_d0(roots: list[mp.mpc], s: mp.mpc, alpha: mp.mpf) -> mp.mpc:
    r = mp.sqrt(alpha)
    point = s + r
    return mp.mpf("0.5") * (
        xcal_derivative(roots, point, 0) / r**3
        - xcal_derivative(roots, point, 1) / r**2
        - xcal_derivative(roots, point, 2) / r
    )


def terminal_packet() -> list[mp.mpc]:
    roots: list[mp.mpc] = []

    def add_quartet(depth: str, ordinate: str) -> None:
        d = mp.mpf(depth)
        t = mp.mpf(ordinate)
        for sign_d in (-1, 1):
            for sign_t in (-1, 1):
                roots.append(mp.mpf("0.5") + sign_d * d + 1j * sign_t * t)

    add_quartet("0.31", "10")       # target
    add_quartet("0.40", "10.50")   # 0.4^2-0.5^2 < 0.31^2
    add_quartet("0.20", "10.10")   # 0.2^2-0.1^2 < 0.31^2
    for t in ("9.8", "11.5", "-8.7"):
        roots.append(mp.mpf("0.5") + 1j * mp.mpf(t))
    return roots


def main() -> dict:
    mp.mp.dps = 80
    max_k = 9
    rows = coefficient_rows(max_k)

    # Exact recurrence versus independent partial-fraction coefficients.
    exact_checks = 0
    for k, row in enumerate(rows):
        for n, coeff in enumerate(row):
            expected = (
                Fraction(4 * math.factorial(k + 2) * ((-1) ** (n + 1)), math.factorial(n))
                * partial_fraction_a(k, n + 1)
            )
            assert coeff == expected
            exact_checks += 1

    # Direct partial-fraction identity at generic complex points.
    max_partial_error = mp.mpf("0")
    test_z = [mp.mpc("0.23", "0.17"), mp.mpc("-0.31", "0.41"), mp.mpc("0.61", "-0.08")]
    for k in range(max_k + 1):
        for z in test_z:
            direct = z * z / (1 - z * z) ** (k + 3)
            expanded = mp.mpc(0)
            for j in range(1, k + 4):
                a = partial_fraction_a(k, j)
                amp = mp.mpf(a.numerator) / a.denominator
                expanded += amp * ((1 - z) ** (-j) + (1 + z) ** (-j))
            max_partial_error = max(max_partial_error, abs(direct - expanded))

    roots = synthetic_roots()
    s = mp.mpf("0.5") + 1j * mp.mpf("0.4")

    # Three-point confluent limit at general alpha.
    alpha = mp.mpf("1.3")
    target_d0 = confluent_d0(roots, s, alpha)
    confluence_errors = []
    for y_text in ("0.08", "0.04", "0.02", "0.01"):
        y = mp.mpf(y_text)
        value = three_point(roots, s, alpha, y) / (y * y)
        confluence_errors.append(float(abs(value - target_d0)))
    assert confluence_errors[-1] < confluence_errors[0] / 50

    # One-safe-line derivative formula versus the rational zero kernel.
    max_zero_kernel_error = mp.mpf("0")
    zero_kernel_values = []
    for k, row in enumerate(rows[:7]):
        h_value = h_from_row(roots, s, row)
        zero_value = sum(kappa(k, rho - s) for rho in roots)
        error = abs(-mp.re(h_value) - mp.re(zero_value))
        max_zero_kernel_error = max(max_zero_kernel_error, error)
        zero_kernel_values.append(float(mp.re(zero_value)))

    # One-line Euler polynomial: use a finite synthetic Dirichlet series.
    terms = [(2, mp.log(2)), (3, mp.log(3)), (4, mp.log(2)), (5, mp.log(5)), (8, mp.log(2)), (9, mp.log(3))]
    w = mp.mpf("1.5") + 1j * mp.mpf("0.73")
    max_euler_weight_error = mp.mpf("0")
    for row in rows[:7]:
        derivative_form = mp.mpc(0)
        polynomial_form = mp.mpc(0)
        for j, coeff in enumerate(row):
            amp = mp.mpf(coeff.numerator) / coeff.denominator
            derivative_form += amp * sum(weight * (-mp.log(n)) ** j * n ** (-w) for n, weight in terms)
        for n, weight in terms:
            t = mp.log(n)
            p = sum((mp.mpf(c.numerator) / c.denominator) * (-t) ** j for j, c in enumerate(row))
            polynomial_form += weight * n ** (-w) * p
        max_euler_weight_error = max(max_euler_weight_error, abs(derivative_form - polynomial_form))

    # Synthetic terminal pair: the hierarchy must eventually be negative.
    packet = terminal_packet()
    x = mp.mpf("10")
    sx = mp.mpf("0.5") + 1j * x
    terminal_values = []
    for k in (0, 2, 4, 8, 12, 20, 32):
        value = mp.re(sum(kappa(k, rho - sx) for rho in packet))
        # Scale out factorial and target denominator to avoid unreadable magnitudes.
        scaled = value * (1 - mp.mpf("0.31") ** 2) ** (k + 3) / (2 * mp.factorial(k + 2) * mp.mpf("0.31") ** 2)
        terminal_values.append([k, float(scaled)])
    assert terminal_values[-1][1] < -1.9

    gates = {
        "exact_coefficient_crosscheck": exact_checks == sum(k + 3 for k in range(max_k + 1)),
        "partial_fraction_identity": max_partial_error < mp.mpf("1e-65"),
        "three_point_confluence": confluence_errors[-1] < 1e-4,
        "zero_kernel_identity": max_zero_kernel_error < mp.mpf("1e-65"),
        "single_euler_polynomial": max_euler_weight_error < mp.mpf("1e-65"),
        "synthetic_terminal_isolation": terminal_values[-1][1] < -1.9,
    }
    if not all(gates.values()):
        raise AssertionError(gates)

    return {
        "status": "PASS_X_90904_SINGLE_SAFE_LINE",
        "gates": gates,
        "exact_coefficient_checks": exact_checks,
        "coefficient_rows_0_to_4": [[str(c) for c in row] for row in rows[:5]],
        "max_partial_fraction_error": float(max_partial_error),
        "confluence_errors": confluence_errors,
        "max_zero_kernel_error": float(max_zero_kernel_error),
        "zero_kernel_values_0_to_6": zero_kernel_values,
        "max_euler_weight_error": float(max_euler_weight_error),
        "terminal_scaled_values": terminal_values,
        "scope": "Finite exact/high-precision synthetic algebra only; no Riemann-data sign and no RH claim.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = main()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end=")
