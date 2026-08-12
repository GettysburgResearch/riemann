#!/usr/bin/env python3
"""Regression for gamma-ladder, compensated Wick-Green, and plastic-aligned Cauchy source."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 70


def xi_gamma_logder(s):
    return 1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2 + mp.digamma(s / 2) / 2


def r_alpha(alpha, t):
    return 1 / (alpha - 1j * t) - 1 / (alpha + 1j * t)


def ladder_error(sigma, t):
    direct = xi_gamma_logder(sigma + 1j * t) - xi_gamma_logder(sigma - 1j * t)
    ladder = mp.nsum(lambda m: r_alpha(sigma + 2 * m, t), [1, mp.inf])
    approx = ladder - r_alpha(sigma - 1, t)
    return abs(direct - approx), direct, approx


def compensated_identity():
    """Exact rational two-label instance of L-91412."""
    us = [F(1, 100), F(1, 20), F(1, 5), F(3, 5)]
    ws = [F(7, 11), F(5, 13), F(3, 17), F(2, 19)]
    h = F(1, 2)

    C = [
        np.array([F(2, 3), F(-1, 4)], dtype=object),
        np.array([F(-3, 5), F(4, 7)], dtype=object),
    ]
    A = [
        np.array([F(1, 2), F(2, 5)], dtype=object),
        np.array([F(-2, 9), F(1, 3)], dtype=object),
    ]
    B = [
        np.array([F(-1, 7), F(3, 8)], dtype=object),
        np.array([F(5, 11), F(-2, 5)], dtype=object),
    ]
    A2 = [
        np.array([F(1, 13), F(-1, 9)], dtype=object),
        np.array([F(2, 15), F(1, 10)], dtype=object),
    ]
    B2 = [
        np.array([F(-1, 12), F(1, 14)], dtype=object),
        np.array([F(1, 16), F(-1, 18)], dtype=object),
    ]

    def dot(x, y):
        return sum((xx * yy for xx, yy in zip(x, y)), F(0))

    U = [[C[i] + u * A[i] + u * u * A2[i] for u in us] for i in range(2)]
    V = [[C[i] + u * B[i] + u * u * B2[i] for u in us] for i in range(2)]
    chi = [u <= h for u in us]
    zero = np.array([F(0), F(0)], dtype=object)
    Ut = [
        [U[i][q] - (C[i] if chi[q] else zero) for q in range(len(us))]
        for i in range(2)
    ]
    Vt = [
        [V[i][q] - (C[i] if chi[q] else zero) for q in range(len(us))]
        for i in range(2)
    ]

    J = []
    for i in range(2):
        z = np.array([F(0), F(0)], dtype=object)
        for q, w in enumerate(ws):
            if chi[q]:
                z = z + w * (Ut[i][q] + Vt[i][q])
        J.append(z)

    K = np.empty((2, 2), dtype=object)
    rhs = np.empty((2, 2), dtype=object)
    for i in range(2):
        for j in range(2):
            value = F(0)
            gram_d = gram_u = gram_v = F(0)
            for q, w in enumerate(ws):
                value -= w * (
                    dot(U[i][q], V[j][q])
                    + dot(V[i][q], U[j][q])
                    - (2 * dot(C[i], C[j]) if chi[q] else 0)
                )
                d_i = Ut[i][q] - Vt[i][q]
                d_j = Ut[j][q] - Vt[j][q]
                gram_d += w * dot(d_i, d_j)
                gram_u += w * dot(Ut[i][q], Ut[j][q])
                gram_v += w * dot(Vt[i][q], Vt[j][q])
            connection = (
                dot(C[i] - J[i], C[j] - J[j])
                - dot(C[i], C[j])
                - dot(J[i], J[j])
            )
            K[i, j] = value
            rhs[i, j] = gram_d - gram_u - gram_v + connection
            assert K[i, j] == rhs[i, j]

    return {
        "kernel": [[str(K[i, j]) for j in range(2)] for i in range(2)],
        "connection_vectors": [[str(x) for x in v] for v in J],
    }


def residual_dimless(s):
    return (
        -mp.mpf(1) / 4 * (1 + s) * mp.e ** (-s)
        + mp.mpf(17) / 32 * (1 + 2 * s) * mp.e ** (-2 * s)
        - mp.mpf(1) / 16 * (1 + 4 * s) * mp.e ** (-4 * s)
    )


def h_switch(s):
    return (
        mp.mpf(17) / 32 * (1 + 2 * s) / (1 + s) * mp.e ** (-s)
        - mp.mpf(1) / 16 * (1 + 4 * s) / (1 + s) * mp.e ** (-3 * s)
    )


def base_density_factor(u):
    return 1 / (1 - mp.e ** (-2 * u)) - (1 + mp.e**u)


def gamma_arch_n(c, x):
    def p(z):
        return mp.re(xi_gamma_logder(mp.mpf("0.5") + z + 1j * x))

    return mp.mpf("0.5") * (c * p(c) - c * c * mp.diff(p, c))


def gamma_arch_e(c, x):
    return c ** (-4) * (gamma_arch_n(2 * c, x) - gamma_arch_n(c, x))


def gamma_arch_recurrence(a, x):
    return gamma_arch_e(a, x) - gamma_arch_e(2 * a, x)


def aligned_integral(a, x):
    def integrand(u):
        return (
            2
            * a ** (-4)
            * (1 - mp.cos(x * u))
            * mp.e ** (-u / 2)
            * base_density_factor(u)
            * (a * residual_dimless(a * u))
        )

    plastic_log = mp.log(mp.findroot(lambda y: y**3 - y - 1, mp.mpf("1.3")))
    return mp.quad(integrand, [0, plastic_log, mp.mpf("0.5"), 1, mp.inf])


def xi_logder(s):
    return xi_gamma_logder(s) + mp.diff(lambda z: mp.log(mp.zeta(z)), s)


def full_n(c, x):
    def p(z):
        return mp.re(xi_logder(mp.mpf("0.5") + z + 1j * x))

    return mp.mpf("0.5") * (c * p(c) - c * c * mp.diff(p, c))


def full_e(c, x):
    return c ** (-4) * (full_n(2 * c, x) - full_n(c, x))


def full_recurrence(a, x):
    return full_e(a, x) - full_e(2 * a, x)


def rank_one_control(alpha=mp.mpf("3.5")):
    grid = np.array([0.0, 0.17, 0.41, 0.93, 1.37])
    matrix = np.exp(-float(alpha) * (grid[:, None] + grid[None, :]))
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    norm_formula = 1 / (2 * alpha)
    norm_quadrature = (
        mp.quad(lambda t: 1 / (t * t + alpha * alpha), [-mp.inf, mp.inf])
        / (2 * mp.pi)
    )
    return [float(x) for x in singular_values], float(abs(norm_formula - norm_quadrature))


def build():
    sigma = mp.mpf("4.5")
    carrier = mp.mpf("0.83")
    ladder_err, direct, ladder_value = ladder_error(sigma, carrier)

    tau_star = mp.findroot(lambda s: h_switch(s) - mp.mpf(1) / 4, (1, 1.4))
    plastic = mp.findroot(lambda y: y**3 - y - 1, mp.mpf("1.3"))
    plastic_log = mp.log(plastic)
    aligned_scale = tau_star / plastic_log

    samples = [
        mp.mpf("1e-5"),
        plastic_log / 4,
        plastic_log * mp.mpf("0.99"),
        plastic_log * mp.mpf("1.01"),
        1,
        2,
        4,
    ]
    sign_products = [
        base_density_factor(u)
        * (aligned_scale * residual_dimless(aligned_scale * u))
        for u in samples
    ]

    carriers = [mp.mpf("0.2"), mp.mpf("1.1"), mp.mpf("4.7")]
    increment_errors = []
    increments = []
    for x in carriers:
        lhs = gamma_arch_recurrence(aligned_scale, x) - gamma_arch_recurrence(
            aligned_scale, 0
        )
        rhs = aligned_integral(aligned_scale, x)
        increment_errors.append(float(abs(lhs - rhs)))
        increments.append(float(lhs))

    full_anchor = full_recurrence(aligned_scale, 0)
    singular_values, norm_error = rank_one_control()
    compensated = compensated_identity()

    gates = {
        "ladder": ladder_err < mp.mpf("1e-55"),
        "rank_one": singular_values[1] < 1e-14 and norm_error < 1e-50,
        "compensated_green": True,
        "single_switch": all(p >= -mp.mpf("1e-55") for p in sign_products),
        "aligned_increment": max(increment_errors) < 1e-45 and min(increments) > 0,
        "positive_full_anchor": full_anchor > 0,
    }
    assert all(gates.values())

    return {
        "status": "PASS_LADDER_COMPENSATED_GREEN_ALIGNMENT",
        "gates": gates,
        "sigma": float(sigma),
        "carrier": float(carrier),
        "gamma_ladder_truncation_error": float(ladder_err),
        "arch_derivative_imag": float(mp.im(direct)),
        "ladder_approx_imag": float(mp.im(ladder_value)),
        "rank_one_singular_values": singular_values,
        "hardy_kernel_norm_error": norm_error,
        "compensated_identity": compensated,
        "residual_switch": float(tau_star),
        "plastic_constant": float(plastic),
        "plastic_log": float(plastic_log),
        "aligned_scale": float(aligned_scale),
        "sign_products": [float(p) for p in sign_products],
        "aligned_increment_errors": increment_errors,
        "aligned_increments": increments,
        "full_recurrence_anchor": float(full_anchor),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = json.dumps(build(), sort_keys=True, separators=(",", ":")) + "\n"
    if args.json:
        args.json.write_text(payload)
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
