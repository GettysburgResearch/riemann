#!/usr/bin/env python3
"""Exact rational controls for the repaired profile and energy-angle reductions."""
from __future__ import annotations

import json
from fractions import Fraction as F
from typing import Iterable

SCHEMA = "riemann.x16202-four-gate-reduction.v1"


class CertificateError(ValueError):
    pass


def qf(matrix: list[list[F]], vector: list[F]) -> F:
    return sum(vector[i] * matrix[i][j] * vector[j]
               for i in range(len(vector)) for j in range(len(vector)))


def mat_sub(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[a[i][j] - b[i][j] for j in range(len(a))] for i in range(len(a))]


def mat_mul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def diagonal(values: Iterable[F]) -> list[list[F]]:
    vals = list(values)
    return [[vals[i] if i == j else F(0) for j in range(len(vals))]
            for i in range(len(vals))]


def ldl_pivots(a: list[list[F]]) -> list[F]:
    """Exact LDL pivots for a symmetric matrix without pivoting."""
    n = len(a)
    l = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    d: list[F] = []
    for i in range(n):
        pivot = a[i][i] - sum(l[i][k] * l[i][k] * d[k] for k in range(i))
        d.append(pivot)
        if pivot == 0:
            if any(a[j][i] - sum(l[j][k] * l[i][k] * d[k] for k in range(i))
                   for j in range(i + 1, n)):
                raise CertificateError("zero LDL pivot with nonzero trailing column")
            continue
        for j in range(i + 1, n):
            l[j][i] = (
                a[j][i] - sum(l[j][k] * l[i][k] * d[k] for k in range(i))
            ) / pivot
    return d


def require_pd(a: list[list[F]], name: str) -> list[F]:
    pivots = ldl_pivots(a)
    if not all(p > 0 for p in pivots):
        raise CertificateError(f"{name} is not positive definite")
    return pivots


def repaired_packet_control() -> dict:
    q = [F(1), F(1), F(1), F(1)]
    ell = [F(0), F(1), F(2), F(3)]
    u = [
        [F(1), F(2)],
        [F(-2), F(-3)],
        [F(1), F(0)],
        [F(0), F(1)],
    ]
    cols = transpose(u)
    if any(sum(q[i] * col[i] for i in range(4)) for col in cols):
        raise CertificateError("point-value cancellation failed")
    if any(sum(ell[i] * col[i] for i in range(4)) for col in cols):
        raise CertificateError("integral cancellation failed")

    raw_corrections = [
        {"u_minus_half": str(ell[i] / 2), "u_plus_half": str(-q[i] / 2)}
        for i in range(4)
    ]
    if any(item["u_minus_half"] == "0" and item["u_plus_half"] == "0"
           for item in raw_corrections):
        raise CertificateError("synthetic raw mode accidentally admissible")

    defects = diagonal([F(1, 10_000), F(1, 100), F(1), F(100)])
    repaired_gram = mat_mul(mat_mul(transpose(u), defects), u)
    pivots = require_pd(repaired_gram, "repaired leakage Gram")
    return {
        "raw_modes_have_poisson_power_corrections": True,
        "radical_basis": [[str(x) for x in row] for row in u],
        "repaired_leakage_gram": [[str(x) for x in row] for row in repaired_gram],
        "repaired_ldl_pivots": [str(x) for x in pivots],
    }


def energy_angle_control() -> dict:
    s0 = diagonal([F(1), F(4)])
    b0 = [[F(10)]]
    x = [[F(1, 2)], [F(1)]]
    kappa = F(1, 2)

    x_b_inv_xt = [[x[i][0] * x[j][0] / b0[0][0] for j in range(2)]
                  for i in range(2)]
    schur_s = mat_sub([[kappa * kappa * v for v in row] for row in s0],
                      x_b_inv_xt)
    schur_pivots = require_pd(schur_s, "source Schur margin")

    x_t_s_inv_x = x[0][0] * x[0][0] / s0[0][0] + x[1][0] * x[1][0] / s0[1][1]
    background_margin = kappa * kappa * b0[0][0] - x_t_s_inv_x
    if background_margin <= 0:
        raise CertificateError("background Schur margin failed")

    block = [
        [F(1), F(0), F(1, 2)],
        [F(0), F(4), F(1)],
        [F(1, 2), F(1), F(10)],
    ]
    require_pd(block, "full block")
    mu_s = F(1)
    g_s = F(3)
    g_b = F(10)
    theorem_gap = min((F(1) - kappa) * g_s - kappa * mu_s,
                      (F(1) - kappa) * g_b - mu_s)
    if theorem_gap != 1:
        raise CertificateError("unexpected theorem gap")

    shifted_complement = [[F(3), F(1)], [F(1), F(9)]]
    lower_replay = mat_sub(shifted_complement, diagonal([theorem_gap, theorem_gap]))
    require_pd(lower_replay, "replayed complement lower bound")

    target_dual = x[0][0] * x[0][0] / b0[0][0]
    target_dual_bound = kappa * kappa * mu_s
    if target_dual > target_dual_bound:
        raise CertificateError("target/background dual estimate failed")

    return {
        "kappa": str(kappa),
        "source_schur_pivots": [str(v) for v in schur_pivots],
        "background_schur_margin": str(background_margin),
        "global_floor": "0",
        "target_floor_excess": str(mu_s),
        "complete_gap_lower_bound": str(theorem_gap),
        "target_background_dual": str(target_dual),
        "target_background_dual_bound": str(target_dual_bound),
    }


def scalarization_control() -> dict:
    d = [F(1, 100), F(1), F(4)]
    sqrt_d = [F(1, 10), F(1), F(2)]
    a = F(5)
    eps = F(1, 10)
    e = [
        [F(1, 20), F(1, 50), F(0)],
        [F(1, 50), F(-1, 25), F(1, 100)],
        [F(0), F(1, 100), F(0)],
    ]
    row_bounds = [sum(abs(v) for v in row) for row in e]
    if max(row_bounds) > eps:
        raise CertificateError("whitened remainder exceeds declared epsilon")
    identity_plus = [[F(int(i == j)) + e[i][j] for j in range(3)] for i in range(3)]
    require_pd(identity_plus, "I+E")
    a_matrix = [
        [a * sqrt_d[i] * identity_plus[i][j] * sqrt_d[j] for j in range(3)]
        for i in range(3)
    ]
    require_pd(a_matrix, "scalarized Weil matrix")

    p = [F(1), F(0), F(0)]
    mu = qf(a_matrix, p)
    mu_upper = (F(1) + eps) * a * d[0]
    if mu > mu_upper:
        raise CertificateError("target upper transfer failed")

    complement = [[a_matrix[i][j] for j in (1, 2)] for i in (1, 2)]
    predicted_gap = (F(1) - eps) * a * d[1] - mu
    replay = mat_sub(complement, diagonal([mu + predicted_gap, mu + predicted_gap]))
    require_pd(replay, "complete scalarization gap replay")
    return {
        "epsilon": str(eps),
        "whitened_row_bounds": [str(v) for v in row_bounds],
        "target_rayleigh": str(mu),
        "target_upper_bound": str(mu_upper),
        "complete_gap_lower_bound": str(predicted_gap),
    }


def verify() -> dict:
    return {
        "schema": SCHEMA,
        "classification": "EXACT_SYNTHETIC_REDUCTION_CONTROL",
        "repaired_packet": repaired_packet_control(),
        "energy_angle": energy_angle_control(),
        "complete_scalarization": scalarization_control(),
        "proof_boundary": (
            "The checker validates finite rational algebra only. It does not "
            "evaluate prolate functions, the Weil form, zeta zeros, or any "
            "production asymptotic gate."
        ),
    }


def main() -> int:
    print(json.dumps(verify(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
