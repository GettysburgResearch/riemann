#!/usr/bin/env python3
"""Deterministic floating reconnaissance for the actual P61 Target-Lorenz gate.

This file is deliberately not proof-producing. It uses NumPy float64 and only
reports candidate minima to guide the exact analytic campaign.
"""
from __future__ import annotations

from pathlib import Path
import bisect
import hashlib
import json
import math

import numpy as np

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
P_VALUES = [67, 71, 73, 79, 83, 89, 97, 101, 127, 151, 251, 509, 1009, 2003, 5003]
Y_VALUES = np.linspace(1.0, 66.999, 133)
MAX_N = int(max(P_VALUES) * max(Y_VALUES)) + 2


def divisors_mu() -> tuple[list[int], np.ndarray]:
    vals = [(1, 1)]
    for q in PRIMES:
        vals += [(d * q, -mu) for d, mu in list(vals)]
    vals.sort()
    return [d for d, _ in vals], np.array([mu for _, mu in vals], dtype=np.int8)


D, MU = divisors_mu()
ARR = np.arange(1, MAX_N + 1, dtype=np.float64)
INV = np.zeros(MAX_N + 1)
LINV = np.zeros(MAX_N + 1)
INV[1:] = 1.0 / np.sqrt(ARR)
LINV[1:] = np.log(ARR) / np.sqrt(ARR)
H = np.cumsum(INV)
L = np.cumsum(LINV)


def q_vec(Y: np.ndarray, j: int) -> np.ndarray:
    Y = np.asarray(Y, dtype=np.float64)
    N = np.floor(Y).astype(np.int64)
    out = np.zeros_like(Y)
    mask = N >= j
    if not np.any(mask):
        return out
    Ym = Y[mask]
    Nm = N[mask]
    logY = np.log(Ym)
    first = (j + 1) / (j - 1) / math.sqrt(j)
    C = np.full_like(Ym, first)
    D0 = np.full_like(Ym, first * math.log(j))
    second = -((j + 1) * (j - 2)) / (j * (j - 1)) / math.sqrt(j + 1)
    m2 = Nm >= j + 1
    C[m2] += second
    D0[m2] += second * math.log(j + 1)
    m3 = Nm >= j + 2
    if np.any(m3):
        c = 2.0 / (j * (j - 1))
        C[m3] += c * (H[Nm[m3]] - H[j + 1])
        D0[m3] += c * (L[Nm[m3]] - L[j + 1])
    out[mask] = C * logY - D0
    return out


def s4(Y: np.ndarray) -> np.ndarray:
    out = np.zeros_like(Y, dtype=np.float64)
    mask = Y >= 1.0
    out[mask] = 4.0 * np.sqrt(Y[mask]) - 3.0
    return out


def one_point(p: float, y: float) -> tuple[dict, dict]:
    x = p * y
    r = p**-0.5
    count = bisect.bisect_right(D, x)
    d = np.array(D[:count], dtype=np.float64)
    mu = MU[:count]
    target = (s4(x / d) - r * s4(y / d)) / np.sqrt(d)
    even = np.flatnonzero(mu == 1)
    odd = np.flatnonzero(mu == -1)
    E_T = float(target[even].sum())
    O_T = float(target[odd].sum())
    cumulative = np.cumsum(target[even])
    k = int(np.searchsorted(cumulative, O_T, side="left"))
    used = even[: k + 1]
    weights = np.ones(k + 1)
    before = cumulative[k - 1] if k else 0.0
    weights[-1] = (O_T - before) / target[even[k]]
    cutoff = int(D[int(even[k])])

    best_lorenz = {"margin": float("inf")}
    best_det = {"margin": float("inf")}
    for j in range(2, 67):
        row = (q_vec(x / d, j) - r * q_vec(y / d, j)) / np.sqrt(d)
        O_R = float(row[odd].sum())
        E_R = float(row[even].sum())
        lorenz = float(np.dot(weights, row[used]) - O_R)
        determinant = float(O_T * E_R - E_T * O_R)
        if lorenz < best_lorenz["margin"]:
            best_lorenz = {
                "margin": lorenz,
                "p": p,
                "y": y,
                "row": j,
                "cutoff": cutoff,
                "quotient": x / j,
            }
        if determinant < best_det["margin"]:
            best_det = {
                "margin": determinant,
                "p": p,
                "y": y,
                "row": j,
                "cutoff": cutoff,
                "quotient": x / j,
            }
    return best_lorenz, best_det


def main() -> None:
    best_lorenz = {"margin": float("inf")}
    best_lorenz_after_five = {"margin": float("inf")}
    best_det = {"margin": float("inf")}
    points = 0
    row_tests = 0
    for p in P_VALUES:
        for y0 in Y_VALUES:
            y = float(y0)
            lorenz, det = one_point(float(p), y)
            points += 1
            row_tests += 65
            if lorenz["margin"] < best_lorenz["margin"]:
                best_lorenz = lorenz
            if lorenz["quotient"] >= 5 and lorenz["margin"] < best_lorenz_after_five["margin"]:
                best_lorenz_after_five = lorenz
            if det["margin"] < best_det["margin"]:
                best_det = det
    assert best_lorenz["margin"] > 0
    assert best_det["margin"] > 0
    payload = {
        "arithmetic_class": "FLOATING_RECONNAISSANCE",
        "classification": "PASS_FLOATING_TARGET_LORENZ_RECONNAISSANCE",
        "p_values": P_VALUES,
        "y_points_per_p": len(Y_VALUES),
        "parameter_points": points,
        "row_tests": row_tests,
        "minimum_lorenz_margin": best_lorenz,
        "minimum_lorenz_margin_after_exact_quotient_five_region": best_lorenz_after_five,
        "minimum_full_target_determinant": best_det,
        "proof_status": "not a directed or exact certificate",
        "rh_established_by_replay": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["record_sha256"] = hashlib.sha256(canonical).hexdigest()
    out = Path(__file__).resolve().parent / "results" / "reconnaissance.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["classification"])
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
