#!/usr/bin/env python3
"""Finite diagnostics for L-90901/R-90901/L-90902.

This script checks only finite-dimensional algebra and kernel quadrature.  It does
not evaluate the zeta explicit-formula distribution and proves neither RH nor any
prime-side positivity theorem.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


def kappa(a: float, x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return a / math.pi * (
        1.0 / (a * a + (x - y) ** 2)
        - 1.0 / (a * a + (x + y) ** 2)
    )


def elementary_symmetric(vals: np.ndarray) -> np.ndarray:
    out = np.zeros(len(vals) + 1, dtype=np.float64)
    out[0] = 1.0
    for value in vals:
        out[1:] = out[1:] + value * out[:-1].copy()
    return out


def chebyshev_t(d: int, x: float) -> float:
    if abs(x) <= 1.0:
        return math.cos(d * math.acos(x))
    if x > 1.0:
        return math.cosh(d * math.acosh(x))
    return ((-1) ** d) * math.cosh(d * math.acosh(-x))


def main() -> dict:
    rng = np.random.default_rng(20260811)

    # 1. Kernel semigroup on a large quadrature box.
    n_quad = 500
    nodes, weights = leggauss(n_quad)
    radius = 70.0
    s = radius * (nodes + 1.0) / 2.0
    w = radius * weights / 2.0
    x = np.array([0.35, 0.9, 1.7, 2.8])
    a, b = 0.7, 1.1
    ka = kappa(a, x[:, None], s[None, :])
    kb = kappa(b, s[:, None], x[None, :])
    composed = (ka * w[None, :]) @ kb
    direct = kappa(a + b, x[:, None], x[None, :])
    semigroup_error = float(np.max(np.abs(composed - direct)))

    # 2. Finite cyclic determinant identity and Fredholm coefficient formula.
    m, n = 8, 6
    B = rng.normal(size=(m, n)) + 1j * rng.normal(size=(m, n))
    q = rng.normal(size=m)
    Aq = B.conj().T @ np.diag(q) @ B
    L = B @ B.conj().T
    t = 0.031
    det_left = np.linalg.det(np.eye(n) + t * Aq)
    det_right = np.linalg.det(np.eye(m) + t * np.diag(q) @ L)
    cyclic_error = float(abs(det_left - det_right))

    eig = np.linalg.eigvalsh((Aq + Aq.conj().T) / 2.0)
    exterior = elementary_symmetric(eig)
    subset_coefficients = [1.0]
    from itertools import combinations

    for k in range(1, n + 1):
        total = 0.0 + 0.0j
        for idx in combinations(range(m), k):
            block = L[np.ix_(idx, idx)]
            total += np.linalg.det(block) * np.prod(q[list(idx)])
        subset_coefficients.append(float(total.real))
    exterior_error = float(np.max(np.abs(exterior - subset_coefficients)))

    # Principal minors of L are nonnegative.
    min_lenard_minor = math.inf
    for k in range(1, min(5, m) + 1):
        for idx in combinations(range(m), k):
            val = float(np.linalg.det(L[np.ix_(idx, idx)]).real)
            min_lenard_minor = min(min_lenard_minor, val)

    # 3. Exterior firewall A=I_K+(-eps).
    K = 13
    eps = 0.031
    vals = np.array([1.0] * K + [-eps])
    e = elementary_symmetric(vals)
    first_negative = next(i for i, value in enumerate(e[1:], start=1) if value < 0)
    predicted_first_negative = math.floor((K + 1) / (1.0 + eps)) + 1
    exterior_firewall_ok = (
        np.all(e[1:K + 1] > 0)
        and e[K + 1] < 0
        and first_negative == predicted_first_negative
    )

    # 4. Bounded heat firewall.
    heat_B = 5.0
    eps_heat = 0.95 * math.log(2.0 - math.exp(-heat_B)) / heat_B
    grid = np.linspace(0.0, heat_B, 1001)
    theta = np.exp(-grid) - 1.0 + np.exp(eps_heat * grid) - 1.0
    heat_firewall_max = float(np.max(theta))

    # 5. Quantitative Chebyshev-Hankel selector.
    positives = np.array([0.2, 0.5, 1.0, 1.7, 2.0])
    eta = 0.08
    Rplus = float(np.max(positives))
    Mplus = float(np.sum(positives))
    d_bound = math.acosh(math.sqrt(Mplus / eta)) / math.acosh(1.0 + 2.0 * eta / Rplus)
    d = math.floor(d_bound) + 1
    denom = chebyshev_t(d, -1.0 - 2.0 * eta / Rplus)
    p_pos = np.array([chebyshev_t(d, 2.0 * z / Rplus - 1.0) / denom for z in positives])
    p_neg = chebyshev_t(d, -1.0 - 2.0 * eta / Rplus) / denom
    quadratic = float(np.sum(positives * p_pos**2) - eta * p_neg**2)
    theoretical_upper = -eta + Mplus / (chebyshev_t(d, 1.0 + 2.0 * eta / Rplus) ** 2)

    # 6. Explicit heat time.
    r = Mplus / eta
    beta_star = 2.0 / eta * math.log(1.0 + r)
    heat_value = float(np.sum(np.exp(-beta_star * positives) - 1.0) + math.exp(beta_star * eta) - 1.0)
    heat_lower = r * (r + 2.0 - 2.0 * math.log(1.0 + r))

    gates = {
        "kernel_semigroup": semigroup_error < 2e-7,
        "cyclic_determinant": cyclic_error < 1e-7,
        "exterior_subset_formula": exterior_error < 2e-6,
        "lenard_principal_minors": min_lenard_minor > -1e-7,
        "exterior_firewall": bool(exterior_firewall_ok),
        "bounded_heat_firewall": heat_firewall_max < 1e-12,
        "chebyshev_hankel_detection": quadratic < 0 and theoretical_upper < 0,
        "explicit_heat_detection": heat_value > 0 and heat_lower > 0,
    }
    if not all(gates.values()):
        raise AssertionError(gates)

    return {
        "status": "PASS_X_90901_FERMIONIC_LENARD_HIERARCHY",
        "gates": gates,
        "kernel_semigroup_max_error": semigroup_error,
        "cyclic_determinant_error": cyclic_error,
        "exterior_subset_max_error": exterior_error,
        "minimum_lenard_principal_minor": min_lenard_minor,
        "exterior_firewall_first_negative": first_negative,
        "exterior_firewall_predicted": predicted_first_negative,
        "bounded_heat_firewall_max": heat_firewall_max,
        "chebyshev_degree_bound": d_bound,
        "chebyshev_degree_used": d,
        "chebyshev_quadratic": quadratic,
        "chebyshev_theoretical_upper": theoretical_upper,
        "heat_beta_star": beta_star,
        "heat_value": heat_value,
        "heat_lower_bound": heat_lower,
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
