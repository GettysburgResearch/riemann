#!/usr/bin/env python3
"""Finite regression for the Fredholm–Pontryagin final-strike packet.

The script checks finite-dimensional/operator algebra only. It does not prove
any zeta-function positivity theorem or RH.
"""
from __future__ import annotations

import argparse
import cmath
import itertools
import json
import math
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np

STATUS = "PASS_FREDHOLM_PONTRYAGIN_FINAL_STRIKE"


def elementary_symmetric(values: Sequence[float]) -> list[float]:
    coeff = [1.0]
    for value in values:
        coeff.append(0.0)
        for k in range(len(coeff) - 1, 0, -1):
            coeff[k] += float(value) * coeff[k - 1]
    return coeff


def determinant_from_coefficients(coeff: Sequence[float], t: float) -> float:
    return sum(c * (t**k) for k, c in enumerate(coeff))


def shifted_hankel(values: np.ndarray, degree: int) -> np.ndarray:
    moments = {k: float(np.sum(values**k)) for k in range(1, 2 * degree + 2)}
    return np.array(
        [[moments[i + j + 1] for j in range(degree + 1)] for i in range(degree + 1)],
        dtype=float,
    )


def exp_tail(radius: float, start: int) -> float:
    log_term = start * math.log(radius) - math.lgamma(start + 1) if radius else -math.inf
    term = math.exp(log_term) if log_term > -745 else 0.0
    total = term
    k = start
    while term > max(1e-18, abs(total) * 1e-16):
        k += 1
        term *= radius / k
        total += term
        if k > start + 100000:
            raise RuntimeError("tail failed to converge")
    return total


def gaussian_overlap_numeric(sigma: float, y: float, radius: float = 20.0, points: int = 400001) -> float:
    grid = np.linspace(-radius, radius + y, points)
    values = np.exp(-sigma * grid**2) * np.exp(-sigma * (grid - y) ** 2)
    return float(np.trapezoid(values, grid))


def phi(omega: complex, z: complex, a: float = 0.5, length: float = math.log(4.0)) -> complex:
    x = cmath.exp(-length * z)
    return (a - omega * x) / (1.0 - a * omega * x)


def phase_bank_metrics(
    z: complex, powers: Iterable[int], modes: int = 8, eta: float = 0.173
) -> dict[str, object]:
    roots = [cmath.exp(1j * (eta + 2.0 * math.pi * j / modes)) for j in range(modes)]
    critical_t = 0.437
    critical_errors: list[float] = []
    reflected_lower_bounds: list[float] = []
    right_values: list[float] = []
    for k in powers:
        critical = [phi(1.0 + 0j, 1j * critical_t) * phi(w, 1j * critical_t) ** k for w in roots]
        critical_errors.append(abs(sum(abs(v) ** 2 for v in critical) / modes - 1.0))
        right = [phi(1.0 + 0j, z) * phi(w, z) ** k for w in roots]
        reflected = [
            phi(1.0 + 0j, -z.conjugate()) * phi(w, -z.conjugate()) ** k for w in roots
        ]
        right_values.append(sum(abs(v) ** 2 for v in right) / modes)
        reflected_lower_bounds.append(math.sqrt(sum(abs(v) ** 2 for v in reflected) / modes))
    return {
        "critical_mean_square_errors": critical_errors,
        "right_half_plane_mean_squares": right_values,
        "reflected_bank_multiplier_lower_bounds": reflected_lower_bounds,
        "growth_ratio_last_first": reflected_lower_bounds[-1] / reflected_lower_bounds[0],
    }


def trace_word_sum(components: Sequence[np.ndarray], power: int) -> complex:
    total = 0.0 + 0.0j
    for word in itertools.product(range(len(components)), repeat=power):
        product = np.eye(components[0].shape[0], dtype=complex)
        for index in word:
            product = product @ components[index]
        total += np.trace(product)
    return total


def wedge_products(values: Sequence[float], degree: int) -> list[float]:
    return [math.prod(combo) for combo in itertools.combinations(values, degree)]


def von_mangoldt_sieve(limit: int) -> np.ndarray:
    values = np.zeros(limit + 1, dtype=float)
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, limit + 1):
        if is_prime[p]:
            if p * p <= limit:
                is_prime[p * p : limit + 1 : p] = False
            power = p
            logp = math.log(p)
            while power <= limit:
                values[power] = logp
                if power > limit // p:
                    break
                power *= p
    return values


def main() -> dict[str, object]:
    gates: dict[str, bool] = {}

    positive = np.array([1.7, 0.8, 0.35, 0.12], dtype=float)
    mixed = np.array([2.0, 0.7, -0.25], dtype=float)

    positive_e = elementary_symmetric(positive)
    mixed_e = elementary_symmetric(mixed)
    gates["positive_exterior_coefficients"] = min(positive_e[1:]) > 0.0
    first_negative_degree = next(k for k, value in enumerate(mixed_e[1:], start=1) if value < 0)
    gates["mixed_exterior_detects_negative_spectrum"] = first_negative_degree == 3

    positive_hankel_mins = [
        float(np.linalg.eigvalsh(shifted_hankel(positive, degree))[0]) for degree in range(3)
    ]
    mixed_hankel_mins = [
        float(np.linalg.eigvalsh(shifted_hankel(mixed, degree))[0]) for degree in range(3)
    ]
    gates["positive_shifted_hankel_psd"] = min(positive_hankel_mins) > -1e-11
    gates["mixed_shifted_hankel_detects"] = min(mixed_hankel_mins) < -1e-4

    negative_size = 0.25
    root = 1.0 / negative_size
    root_residual = determinant_from_coefficients(mixed_e, root)
    gates["positive_axis_fredholm_root"] = abs(root_residual) < 1e-12

    trace_radius = float(np.sum(np.abs(mixed)) / negative_size)
    start = max(2, math.ceil(2.0 * math.e * trace_radius))
    tail = exp_tail(trace_radius, start)
    gates["finite_degree_tail_bound"] = tail < 1.0 and first_negative_degree < start

    positives = [1.0 + 0.1 * j for j in range(7)]
    one_negative = positives + [-0.3]
    exterior_counts: dict[str, dict[str, int]] = {}
    for degree in range(1, 9):
        products = wedge_products(one_negative, degree)
        observed = sum(value < 0 for value in products)
        expected = math.comb(7, degree - 1)
        exterior_counts[str(degree)] = {"observed": observed, "expected": expected}
    gates["exterior_signature_amplification"] = all(
        row["observed"] == row["expected"] for row in exterior_counts.values()
    )

    overlap_rows: list[dict[str, float]] = []
    max_overlap_relative_error = 0.0
    overlap_sigma = 0.73
    for y in [0.0, 0.5, 1.5, 3.0, 6.0]:
        numeric = gaussian_overlap_numeric(overlap_sigma, y)
        exact = math.sqrt(math.pi / (2.0 * overlap_sigma)) * math.exp(-overlap_sigma * y * y / 2.0)
        relative = abs(numeric - exact) / exact
        max_overlap_relative_error = max(max_overlap_relative_error, relative)
        overlap_rows.append({"y": y, "numeric": numeric, "exact": exact, "relative_error": relative})
    gates["gaussian_overlap_law"] = max_overlap_relative_error < 2e-7

    phase_metrics = phase_bank_metrics(0.16 + 0.29j, [1, 2, 4, 8, 12, 16])
    gates["phase_bank_boundary_unitarity"] = max(
        phase_metrics["critical_mean_square_errors"]
    ) < 1e-12
    lower_bounds = phase_metrics["reflected_bank_multiplier_lower_bounds"]
    gates["phase_bank_strip_norm_growth"] = (
        all(b > a for a, b in zip(lower_bounds, lower_bounds[1:]))
        and phase_metrics["growth_ratio_last_first"] > 20.0
    )

    components = [
        np.array([[0.8, 0.1j], [-0.1j, 0.35]], dtype=complex),
        np.array([[0.12, -0.04], [-0.04, -0.03]], dtype=complex),
        np.array([[-0.02, 0.03j], [-0.03j, 0.05]], dtype=complex),
    ]
    total_matrix = sum(components)
    word_errors: list[float] = []
    for power in range(1, 6):
        direct = np.trace(np.linalg.matrix_power(total_matrix, power))
        expanded = trace_word_sum(components, power)
        word_errors.append(float(abs(direct - expanded)))
    gates["noncommutative_prime_word_expansion"] = max(word_errors) < 5e-12

    base = np.diag([1.2, 0.5, -0.18])
    perturbations = [
        (0.08 / (j * j))
        * np.array(
            [[math.cos(j), math.sin(j), 0.0], [math.sin(j), -math.cos(j), 0.0], [0.0, 0.0, 0.2]],
            dtype=float,
        )
        for j in range(1, 81)
    ]
    full = base + sum(perturbations)
    cutoff_rows: list[dict[str, float | int]] = []
    stability_ok = True
    degree = 3
    full_e = elementary_symmetric(np.linalg.eigvalsh(full))[degree]
    full_norm = float(np.sum(np.abs(np.linalg.eigvalsh(full))))
    for cutoff in [2, 5, 10, 20, 40, 80]:
        truncated = base + sum(perturbations[:cutoff])
        delta = full - truncated
        delta_trace_norm = float(np.sum(np.linalg.svd(delta, compute_uv=False)))
        truncated_norm = float(np.sum(np.abs(np.linalg.eigvalsh(truncated))))
        truncated_e = elementary_symmetric(np.linalg.eigvalsh(truncated))[degree]
        bound = degree * max(full_norm, truncated_norm) ** (degree - 1) * delta_trace_norm
        error = abs(full_e - truncated_e)
        stability_ok = stability_ok and error <= bound + 1e-12
        cutoff_rows.append(
            {"cutoff": cutoff, "coefficient": truncated_e, "error": error, "trace_norm_bound": bound}
        )
    gates["exterior_coefficient_trace_norm_stability"] = stability_ok

    limit = 200000
    mangoldt = von_mangoldt_sieve(limit)
    prime_sigma = 0.18
    n = np.arange(2, limit + 1, dtype=float)
    logn = np.log(n)
    weighted = mangoldt[2:] * n ** (-0.5) * np.exp(-0.5 * prime_sigma * logn**2)
    tail_rows: list[dict[str, float | int]] = []
    previous = math.inf
    tail_monotone = True
    for cutoff in [100, 500, 2000, 10000, 50000, 100000]:
        value = float(np.sum(weighted[cutoff - 1 :]))
        tail_monotone = tail_monotone and value < previous
        previous = value
        tail_rows.append({"cutoff": cutoff, "finite_tail_to_200000": value})
    gates["prime_weighted_tail_decreases"] = tail_monotone

    if not all(gates.values()):
        failed = [name for name, ok in gates.items() if not ok]
        raise AssertionError(f"failed gates: {failed}")

    return {
        "status": STATUS,
        "gates": gates,
        "fredholm_control": {
            "positive_eigenvalues": positive.tolist(),
            "positive_exterior_coefficients": positive_e,
            "mixed_eigenvalues": mixed.tolist(),
            "mixed_exterior_coefficients": mixed_e,
            "first_negative_exterior_degree": first_negative_degree,
            "positive_axis_root": root,
            "root_residual": root_residual,
            "trace_radius": trace_radius,
            "finite_degree_bound_exclusive": start,
            "exponential_tail_at_bound": tail,
        },
        "hankel_control": {
            "positive_min_eigenvalues": positive_hankel_mins,
            "mixed_min_eigenvalues": mixed_hankel_mins,
        },
        "exterior_amplification": exterior_counts,
        "overlap_control": {
            "sigma": overlap_sigma,
            "rows": overlap_rows,
            "max_relative_error": max_overlap_relative_error,
        },
        "phase_bank_firewall": phase_metrics,
        "word_expansion_errors": word_errors,
        "cutoff_stability": cutoff_rows,
        "prime_tail_control": {"sigma": prime_sigma, "rows": tail_rows, "finite_limit": limit},
        "scope": "finite algebra and diagnostics only; RH is not proved",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()
    result = main()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    print(STATUS)
