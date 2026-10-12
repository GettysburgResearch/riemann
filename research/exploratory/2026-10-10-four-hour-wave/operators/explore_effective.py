#!/usr/bin/env python3
"""Ordinary floating-point source experiment; this is NOT a certificate.

Analytic full prime tail and analytic gamma kernel/primitive are used.  Gaussian
quadrature has no rigorous enclosure.  Outputs cannot certify continuum signs.
"""

import argparse
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.linalg import qr, solve_triangular
from scipy.special import roots_legendre


mp.mp.dps = 60
P2 = float(-mp.diff(mp.zeta, 2) / mp.zeta(2))
CB = float((1 - mp.euler - mp.log(2 * mp.pi)) / 3)
B = 1.5
C2 = 0.25
Q2 = math.log(2) / math.sqrt(2)
GAMMA_PRIMITIVE_0 = (7 - math.pi - 4 * math.log(2)) / 9


def gamma_kernel(x):
    x = np.asarray(x)
    out = np.empty_like(x)
    positive = x > 0
    y = x[positive]
    out[positive] = (
        np.exp(-y / 2) / 6
        + np.cosh(B * y) * np.log1p(np.exp(-y)) / 3
        + np.sinh(B * y) * np.log(-np.expm1(-y)) / 3
    )
    out[~positive] = 1 / 6 + math.log(2) / 3
    return out


def kernel(x):
    y = np.abs(np.asarray(x))
    return (
        0.5 * np.exp(y / 2)
        + CB * np.exp(-B * y)
        + gamma_kernel(y)
        - (P2 / B) * np.cosh(B * y)
        + (Q2 / B) * np.sinh(B * np.maximum(y - math.log(2), 0))
    )


def gamma_primitive(x):
    x = np.asarray(x)
    out = np.zeros_like(x)
    positive = x > 0
    y = x[positive]
    r = np.exp(-y / 2)
    t = np.exp(-y)
    atanh_r = 0.5 * (np.log1p(r) - np.log(-np.expm1(-y / 2)))
    atanh_t = 0.5 * (np.log1p(t) - np.log(-np.expm1(-y)))
    tail = -(4 / 9) * (atanh_r + np.arctan(r) - 2 * r) + (2 / 9) * (
        np.exp(-B * y) * atanh_t
        - 0.5 * np.exp(B * y) * (np.log(-np.expm1(-2 * y)) + t * t)
    )
    out[positive] = GAMMA_PRIMITIVE_0 - tail
    return out


def primitive(x):
    x = np.asarray(x)
    y = np.abs(x)
    out = (
        np.expm1(y / 2)
        - (CB / B) * np.expm1(-B * y)
        + gamma_primitive(y)
        - (P2 / B**2) * np.sinh(B * y)
        + (Q2 / B**2) * (np.cosh(B * np.maximum(y - math.log(2), 0)) - 1)
    )
    return np.sign(x) * out


def run(n, removed=15, trial_modes=0):
    nodes, weights = roots_legendre(n)
    t = (nodes + 1) / 2
    weights = weights / 2
    sw = np.sqrt(weights)
    modes = np.arange(1, removed + 1)
    sins = np.sin(math.pi * t[:, None] * modes)
    z = np.column_stack((sins, np.exp(t / 2), np.exp(-t / 2), np.cosh(B * t)))
    zp = np.column_stack((math.pi * modes * np.cos(math.pi * t[:, None] * modes),
                          0.5 * np.exp(t / 2), -0.5 * np.exp(-t / 2), B * np.sinh(B * t)))
    z0 = np.concatenate((np.zeros(removed), [1, 1, 1]))
    z1 = np.concatenate((np.zeros(removed), [math.exp(.5), math.exp(-.5), math.cosh(B)]))
    # Exact constraints are represented by these continuous basis functions;
    # their normalization below uses sampled quadrature, hence remains empirical.
    ez, triangular = qr(sw[:, None] * z, mode="economic")
    transform = solve_triangular(triangular, np.eye(removed + 3))
    z = z @ transform
    zp = zp @ transform
    z0 = z0 @ transform
    z1 = z1 @ transform
    wmat = kernel(t[:, None] - t)
    kmat = wmat * weights[None, :]
    trial_data = {}
    if trial_modes:
        high_modes = np.arange(removed + 1, removed + trial_modes + 1)
        high = np.sin(math.pi * t[:, None] * high_modes)
        highp = math.pi * high_modes * np.cos(math.pi * t[:, None] * high_modes)
        coefficients = z.T @ (weights[:, None] * high)
        vz = high - z @ coefficients
        vzp = highp - zp @ coefficients
        vz0 = -z0 @ coefficients
        vz1 = -z1 @ coefficients
        weighted_v, rv = qr(sw[:, None] * vz, mode="economic")
        trial_transform = solve_triangular(rv, np.eye(trial_modes))
        vz = vz @ trial_transform
        vzp = vzp @ trial_transform
        vz0 = vz0 @ trial_transform
        vz1 = vz1 @ trial_transform
        vkv = B * (vz.T @ (weights[:, None] * (kmat @ vz)))
        vke = B * (vz.T @ (weights[:, None] * (kmat @ z)))
        vkv = (vkv + vkv.T) / 2
        solution = np.linalg.solve(vkv, vke)
        z = z - vz @ solution
        zp = zp - vzp @ solution
        z0 = z0 - vz0 @ solution
        z1 = z1 - vz1 @ solution
        trial_data = {
            "trial_mode_count": trial_modes,
            "trial_basis_condition": float(np.linalg.cond(rv)),
            "trial_energy_minimum_eigenvalue": float(np.linalg.eigvalsh(vkv)[0]),
        }
    k = kmat @ z
    u = B * (z.T @ (weights[:, None] * k))
    intk = (primitive(t[:, None] - t) + primitive(t)[None, :]) * weights[None, :]
    f = -kernel(t)[:, None] * z0 + kernel(t - 1)[:, None] * z1 - kmat @ zp + C2 * (intk @ z)
    constraints = np.column_stack((np.ones(n), np.cos(math.pi * t[:, None] * modes), np.sinh(B * t)))
    projection, _ = qr(sw[:, None] * constraints, mode="economic")
    weighted_f = sw[:, None] * f
    residual = weighted_f - projection @ (projection.T @ weighted_f)
    r = residual.T @ residual
    lower = (u + u.T) / 2 - (15 / 8) * r
    ev_u = np.linalg.eigvalsh((u + u.T) / 2)
    ev_lower = np.linalg.eigvalsh(lower)
    return {
        "status": "EMPIRICAL_NOT_CERTIFIED",
        "quadrature_order": n,
        "removed_sine_modes": removed,
        "complement_dimension": removed + 3,
        "trial": "Galerkin corrections" if trial_modes else "v_i=0",
        **trial_data,
        "constraint_basis_condition": float(np.linalg.cond(triangular)),
        "u_eigenvalues": ev_u.tolist(),
        "lower_eigenvalues": ev_lower.tolist(),
        "residual_norm": float(np.linalg.norm(r, 2)),
        "kernel_source": "full analytic prime constant; exact finite cusp at log2; gamma closed form",
        "limitations": ["ordinary float arithmetic", "unenclosed Gaussian quadrature", "sampled basis normalization and projection"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=400)
    parser.add_argument("--trial-modes", type=int, default=0)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    result = run(args.order, trial_modes=args.trial_modes)
    payload = json.dumps(result, indent=2)
    if args.out:
        args.out.write_text(payload + "\n")
    print(payload)
