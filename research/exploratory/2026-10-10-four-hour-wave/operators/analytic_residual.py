#!/usr/bin/env python3
"""Use an analytic high-precision U artifact and sampled continuum residual R.

This experiment is not directed or certified.  In particular, floating-point
Gaussian quadrature of the gamma logarithmic cusp may bias residual estimates.
"""

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import qr
from scipy.special import roots_legendre

from explore_effective import B, C2, kernel, primitive


def run(path, order):
    data = json.loads(path.read_text())
    coeff = np.array(data["z_coefficients_decimal"], dtype=float)
    removed = data["complement_dimension"] - 3
    trial_modes = data["trial_mode_count"]
    nodes, weights = roots_legendre(order)
    t = (nodes + 1) / 2
    weights /= 2
    low_modes = np.arange(1, removed + 1)
    high_modes = np.arange(removed + 1, removed + trial_modes + 1)
    def sins(m):
        return np.sin(math.pi * t[:, None] * m)
    def dsins(m):
        return math.pi * m * np.cos(math.pi * t[:, None] * m)
    zbase = np.column_stack((sins(low_modes), np.exp(t / 2), np.exp(-t / 2),
                            np.cosh(B * t), sins(high_modes)))
    zpbase = np.column_stack((dsins(low_modes), .5 * np.exp(t / 2), -.5 * np.exp(-t / 2),
                             B * np.sinh(B * t), dsins(high_modes)))
    bdy0 = np.concatenate((np.zeros(removed), [1, 1, 1], np.zeros(trial_modes)))
    bdy1 = np.concatenate((np.zeros(removed), [math.exp(.5), math.exp(-.5), math.cosh(B)],
                           np.zeros(trial_modes)))
    z = zbase @ coeff
    zp = zpbase @ coeff
    z0 = bdy0 @ coeff
    z1 = bdy1 @ coeff
    kmat = kernel(t[:, None] - t) * weights[None, :]
    f = -kernel(t)[:, None] * z0 + kernel(t - 1)[:, None] * z1 - kmat @ zp
    del kmat
    intk = (primitive(t[:, None] - t) + primitive(t)[None, :]) * weights[None, :]
    f += C2 * (intk @ z)
    del intk
    constraints = np.column_stack((np.ones(order), np.cos(math.pi * t[:, None] * low_modes),
                                   np.sinh(B * t)))
    weighted_f = np.sqrt(weights)[:, None] * f
    projection, _ = qr(np.sqrt(weights)[:, None] * constraints, mode="economic")
    residual = weighted_f - projection @ (projection.T @ weighted_f)
    r = residual.T @ residual
    u = np.array(data["u_matrix_decimal"], dtype=float)
    lower = (u + u.T) / 2 - (15 / 8) * r
    return {
        "status": "EMPIRICAL_ANALYTIC_U_SAMPLED_R_NOT_CERTIFIED",
        "analytic_source_artifact": str(path),
        "quadrature_order": order,
        "trial_modes": trial_modes,
        "u_minimum_eigenvalue": float(np.linalg.eigvalsh(u)[0]),
        "lower_eigenvalues": np.linalg.eigvalsh(lower).tolist(),
        "residual_operator_norm": float(np.linalg.norm(r, 2)),
        "residual_matrix": r.tolist(),
        "z_l2_matrix_norm": float(np.linalg.norm(np.sqrt(weights)[:, None] * z, 2)),
        "z_maximum_absolute_value": float(np.max(np.abs(z))),
        "limitations": ["ordinary arithmetic", "unenclosed quadrature", "analytic source values not directed"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path)
    parser.add_argument("--order", type=int, default=2000)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.artifact, args.order)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "residual_matrix"}, indent=2))
