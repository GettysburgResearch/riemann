#!/usr/bin/env python3
"""Finite regression for the Birman–Schwinger / infinitesimal Pick programme."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 70


def xi(s: mp.mpf) -> mp.mpf:
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def xi_logder(s: mp.mpf) -> mp.mpf:
    return (
        1 / s
        + 1 / (s - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
        + mp.diff(mp.zeta, s) / mp.zeta(s)
    )


def mp_to_float_matrix(M: mp.matrix) -> np.ndarray:
    return np.array(
        [[float(M[i, j]) for j in range(M.cols)] for i in range(M.rows)],
        dtype=float,
    )


def safe_packet(u: mp.mpf, qs: list[mp.mpf]) -> dict:
    n = len(qs)
    C = mp.matrix(n)
    S = mp.matrix(n)
    D = mp.zeros(n)
    L = mp.zeros(n)
    for i, q in enumerate(qs):
        D[i, i] = xi(1 + q) / xi(1 + u + q)
        L[i, i] = xi_logder(1 + u + q)
        for j, r in enumerate(qs):
            C[i, j] = 1 / (1 + u + q + r)
            S[i, j] = 1 / (1 + u + q + r) ** 2

    P = C - D * C * D
    p_eigs, _ = mp.eigsy(P)

    gamma = -mp.mpf("0.5") * (C**-1) * S
    N = -L * D + gamma * D - D * gamma
    R = -(N.T * C * D + D * C * N)
    r_eigs, _ = mp.eigsy(R)

    Cf = mp_to_float_matrix(C)
    Df = mp_to_float_matrix(D)
    vals, vecs = np.linalg.eigh(Cf)
    Ch = (vecs * np.sqrt(vals)) @ vecs.T
    Cmh = (vecs * (1 / np.sqrt(vals))) @ vecs.T
    B = Ch @ Df @ Cmh
    singular_values = np.linalg.svd(B, compute_uv=False)

    return {
        "pick_eigenvalues": [float(p_eigs[i]) for i in range(n)],
        "canonical_remainder_eigenvalues": [float(r_eigs[i]) for i in range(n)],
        "return_singular_values": [float(x) for x in singular_values],
    }


def centered_F(x: mp.mpf) -> mp.mpf:
    return xi_logder(mp.mpf("0.5") + x)


def caratheodory_matrix(xs: list[mp.mpf]) -> mp.matrix:
    n = len(xs)
    M = mp.matrix(n)
    fs = [centered_F(x) for x in xs]
    for i in range(n):
        for j in range(n):
            M[i, j] = (fs[i] + fs[j]) / (xs[i] + xs[j])
    return M


def orbit_F(x: F, a: F = F(2, 5), b: F = F(14, 1)) -> F:
    t = x * x
    A = a * a - b * b
    B = 2 * a * b
    U = t - A
    return 4 * x * U / (U * U + B * B)


def det3_fraction(xs: list[F]) -> tuple[F, list[list[F]]]:
    vals = [orbit_F(x) for x in xs]
    M = [[(vals[i] + vals[j]) / (xs[i] + xs[j]) for j in range(3)] for i in range(3)]
    d = (
        M[0][0] * M[1][1] * M[2][2]
        + M[0][1] * M[1][2] * M[2][0]
        + M[0][2] * M[1][0] * M[2][1]
        - M[0][2] * M[1][1] * M[2][0]
        - M[0][1] * M[1][0] * M[2][2]
        - M[0][0] * M[1][2] * M[2][1]
    )
    return d, M


def rational_connection_control() -> dict:
    r = F(9, 10)
    d1 = F(1, 3)
    d2 = F(1, 3**10)

    p11 = 1 - d1 * d1
    p22 = 1 - d2 * d2
    p12 = r * (1 - d1 * d2)
    det_p = p11 * p22 - p12 * p12

    q11 = 2 * d1 * d1
    q22 = 20 * d2 * d2
    q12 = 11 * r * d1 * d2
    det_q = q11 * q22 - q12 * q12
    assert det_p > 0
    assert det_q < 0
    return {
        "pick_determinant": str(det_p),
        "canonical_remainder_determinant": str(det_q),
        "pick_determinant_float": float(det_p),
        "canonical_remainder_determinant_float": float(det_q),
    }


def friedrichs_control() -> dict:
    tc = 1 / mp.log(2)
    t = mp.mpf("2")
    E = mp.e ** (1 / t)
    kappa = (2 - E) / (E - 1)
    equation_error = abs(t * mp.log((2 + kappa) / (1 + kappa)) - 1)
    return {
        "threshold": float(tc),
        "coupling": float(t),
        "bound_state_kappa": float(kappa),
        "equation_error": float(equation_error),
    }


def entropy_control() -> dict:
    eigs = [mp.mpf("0.2"), mp.mpf("0.5"), mp.mpf("0.8")]
    lhs = -sum(mp.log(1 - x) for x in eigs)
    rhs = mp.quad(lambda t: sum(x / (1 - t * x) for x in eigs), [0, 1])
    return {
        "logdet_entropy": float(lhs),
        "resolvent_integral": float(rhs),
        "error": float(abs(lhs - rhs)),
    }


def build() -> dict:
    packet = safe_packet(
        mp.mpf("0.2"),
        [mp.mpf("0.1"), mp.mpf("0.3"), mp.mpf("0.8")],
    )

    two_node_sets = [
        [mp.mpf("0.6"), mp.mpf("1.5")],
        [mp.mpf("0.51"), mp.mpf("8")],
        [mp.mpf("2"), mp.mpf("36")],
    ]
    two_node_eigs = []
    for xs in two_node_sets:
        ev, _ = mp.eigsy(caratheodory_matrix(xs))
        two_node_eigs.append([float(ev[i]) for i in range(2)])

    det3, matrix3 = det3_fraction([F(3, 5), F(8), F(36)])
    assert det3 < 0

    friedrichs = friedrichs_control()
    entropy = entropy_control()
    rational = rational_connection_control()

    gates = {
        "friedrichs": friedrichs["equation_error"] < 1e-60,
        "safe_pick_sample": min(packet["pick_eigenvalues"]) > 0,
        "safe_return_sample": max(packet["return_singular_values"]) <= 1 + 1e-11,
        "canonical_connection_firewall": min(packet["canonical_remainder_eigenvalues"]) < 0,
        "rational_connection_firewall": rational["canonical_remainder_determinant_float"] < 0,
        "two_node_xi": min(min(x) for x in two_node_eigs) > 0,
        "three_node_orbit_firewall": det3 < 0,
        "entropy": entropy["error"] < 1e-60,
    }
    assert all(gates.values())

    return {
        "status": "PASS_BIRMAN_SCHWINGER_SPECTRAL_FLOW",
        "gates": gates,
        "friedrichs": friedrichs,
        "safe_xi_packet": packet,
        "two_node_xi_eigenvalues": two_node_eigs,
        "off_line_orbit_three_node": {
            "nodes": ["3/5", "8", "36"],
            "matrix": [[str(v) for v in row] for row in matrix3],
            "determinant": str(det3),
            "determinant_float": float(det3),
        },
        "rational_connection_control": rational,
        "feedback_entropy": entropy,
    }


def main() -> None:
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
