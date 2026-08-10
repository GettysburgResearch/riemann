#!/usr/bin/env python3
"""Regression for the Xi-cardinal Gram-capture theorem.

A planted-zero toy entire function F(z)=P(z)*sqrt(pi)*exp(-z^2/4) has a
Schwartz inverse Fourier source. Its exact target-pair cardinal difference is
used as a packet-independent competitor in the weighted strip RKHS. The
script verifies the RKHS capture inequality, nested-constraint monotonicity,
the target Schur rank-one bound, and convergence of compact exponential
windows to the strip kernel.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.hermite import hermval
from numpy.polynomial.legendre import leggauss


def gaussian_transform(z: complex | np.ndarray) -> complex | np.ndarray:
    return np.sqrt(np.pi) * np.exp(-np.asarray(z) ** 2 / 4.0)


def planted_cardinal_source(points: np.ndarray) -> tuple[np.poly1d, np.ndarray]:
    """Return polynomial Q and ascending coefficients for H(z)=Q(z)G(z)."""
    polynomial = np.poly1d(np.poly(points))
    derivative = np.polyder(polynomial)

    def cardinal_polynomial(root: complex) -> np.poly1d:
        quotient, remainder = np.polydiv(polynomial, np.poly1d([1.0, -root]))
        if np.max(np.abs(remainder.coeffs)) > 2e-10:
            raise AssertionError(remainder)
        denominator = np.polyval(derivative, root) * gaussian_transform(root)
        return np.poly1d(quotient.coeffs / denominator)

    q_poly = cardinal_polynomial(points[0]) - cardinal_polynomial(points[1])
    return q_poly, q_poly.coeffs[::-1]


def source_values(u: np.ndarray, ascending: np.ndarray) -> np.ndarray:
    """Inverse Fourier source of Q(z)*sqrt(pi)*exp(-z^2/4)."""
    values = np.zeros(u.shape, dtype=np.complex128)
    base = np.exp(-(u**2))
    for order, coefficient in enumerate(ascending):
        selector = np.zeros(order + 1)
        selector[-1] = 1.0
        hermite = hermval(u, selector)
        derivative = ((-1) ** order) * hermite * base
        values += coefficient * (1j**order) * derivative
    return values


def strip_kernel(z: complex, w: complex, a: float) -> complex:
    delta = z - np.conjugate(w)
    return 4.0 * a / (4.0 * a * a + delta * delta)


def compact_kernel(z: complex, w: complex, a: float, radius: float) -> complex:
    """Integral over [-R,R] of exp(-2a|u|) exp(i(z-conj(w))u)."""
    delta = z - np.conjugate(w)
    left = 2.0 * a - 1j * delta
    right = 2.0 * a + 1j * delta
    return (1.0 - np.exp(-left * radius)) / left + (
        1.0 - np.exp(-right * radius)
    ) / right


def gram(points: np.ndarray, kernel) -> np.ndarray:
    matrix = np.array(
        [[kernel(z, w) for w in points] for z in points], dtype=np.complex128
    )
    return (matrix + matrix.conjugate().T) / 2.0


def capture_cost(matrix: np.ndarray, target: np.ndarray) -> float:
    return float(np.vdot(target, np.linalg.solve(matrix, target)).real)


def target_schur(matrix: np.ndarray) -> np.ndarray:
    if matrix.shape[0] == 2:
        return matrix
    a_block = matrix[:2, :2]
    cross = matrix[:2, 2:]
    nuisance = matrix[2:, 2:]
    return a_block - cross @ np.linalg.solve(nuisance, cross.conjugate().T)


def weighted_source_norm(
    ascending: np.ndarray, a: float, radius: float = 10.0, order: int = 1000
) -> float:
    nodes, weights = leggauss(order)
    u = radius * nodes
    integrand = (
        np.abs(source_values(u, ascending)) ** 2 * np.exp(2.0 * a * np.abs(u))
    )
    return float(radius * np.sum(weights * integrand))


def run() -> dict[str, object]:
    omega = 0.35 + 0.22j
    points = np.array(
        [
            omega,
            np.conjugate(omega),
            -1.10 + 0.0j,
            0.90 + 0.0j,
            1.40 + 0.08j,
            1.40 - 0.08j,
        ],
        dtype=np.complex128,
    )
    target = np.zeros(len(points), dtype=np.complex128)
    target[0] = 1.0
    target[1] = -1.0
    target_pair = target[:2]
    a = 0.55

    q_poly, ascending = planted_cardinal_source(points)
    transform_values = np.polyval(q_poly, points) * gaussian_transform(points)
    cardinal_error = float(np.max(np.abs(transform_values - target)))

    source_norm = weighted_source_norm(ascending, a)

    nested_costs: list[float] = []
    final_gram = None
    for count in range(2, len(points) + 1):
        current_points = points[:count]
        current_target = target[:count]
        current = gram(current_points, lambda z, w: strip_kernel(z, w, a))
        nested_costs.append(capture_cost(current, current_target))
        final_gram = current
    assert final_gram is not None

    schur = target_schur(final_gram)
    schur_cost = capture_cost(schur, target_pair)
    rank_one_residual = schur - np.outer(target_pair, np.conjugate(target_pair)) / source_norm
    rank_one_min = float(np.min(np.linalg.eigvalsh(rank_one_residual)))

    radii = [2.0, 4.0, 6.0, 8.0, 10.0]
    compact_costs: list[float] = []
    compact_errors: list[float] = []
    strip = final_gram
    for radius in radii:
        compact = gram(
            points, lambda z, w, radius=radius: compact_kernel(z, w, a, radius)
        )
        compact_costs.append(capture_cost(compact, target))
        compact_errors.append(float(np.linalg.norm(compact - strip, ord="fro")))

    local_weil_value = float(
        (
            transform_values[0] * np.conjugate(transform_values[1])
            + transform_values[1] * np.conjugate(transform_values[0])
        ).real
    )

    gates = {
        "cardinal_values": cardinal_error < 2e-10,
        "positive_strip_gram": float(np.min(np.linalg.eigvalsh(final_gram))) > 1e-4,
        "packet_independent_bound": max(nested_costs) < source_norm,
        "constraint_monotonicity": all(
            nested_costs[index + 1] + 1e-9 >= nested_costs[index]
            for index in range(len(nested_costs) - 1)
        ),
        "schur_identity": abs(schur_cost - nested_costs[-1]) < 2e-8,
        "rank_one_schur_bound": rank_one_min > 1e-5,
        "compact_kernel_convergence": all(
            compact_errors[index + 1] < compact_errors[index]
            for index in range(len(compact_errors) - 1)
        ),
        "compact_cost_convergence": abs(compact_costs[-1] - nested_costs[-1]) < 2.0,
        "negative_pair_value": abs(local_weil_value + 2.0) < 2e-10,
    }

    return {
        "status": "PASS_XI_CARDINAL_GRAM_CAPTURE" if all(gates.values()) else "FAIL",
        "gates": {key: bool(value) for key, value in gates.items()},
        "a": a,
        "target_pair": [[float(z.real), float(z.imag)] for z in points[:2]],
        "nuisance_count": len(points) - 2,
        "cardinal_error": cardinal_error,
        "weighted_source_norm": source_norm,
        "nested_strip_capture_costs": nested_costs,
        "final_strip_min_eigenvalue": float(np.min(np.linalg.eigvalsh(final_gram))),
        "target_schur_capture_cost": schur_cost,
        "rank_one_schur_residual_min_eigenvalue": rank_one_min,
        "compact_radii": radii,
        "compact_capture_costs": compact_costs,
        "compact_kernel_frobenius_errors": compact_errors,
        "local_weil_value": local_weil_value,
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
    if payload["status"] != "PASS_XI_CARDINAL_GRAM_CAPTURE":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
