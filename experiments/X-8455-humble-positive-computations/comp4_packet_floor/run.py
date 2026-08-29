#!/usr/bin/env python3
"""C4 — synthetic three-block / capacity-style margin table.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY (exact rational synthetics + float probes).

Does not assemble a production localized-Weil packet. Instead it varies tiny
synthetic blocks
    H = [[B_R, X*, Y*],
         [X , B_V, Z*],
         [Y , Z , C ]]
and records which Schur margins move together. The aim is to leave an
interesting dependence table for agents working on Issues #156/#169/#178.
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from linalg_q import inertia_ldl  # noqa: E402

OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def schur_three_block(BR, BV, C, X, Y, Z, h, beta, e):
    """Replay the triangular elimination margins from PR #169's sketch.

    Returns diagnostic floats; not a proof object.
    """
    # X_tilde = X - h^{-1} Z* C^{-1} Y   (here C is scalar/matrix; use solve)
    CinvY = np.linalg.solve(C, Y)
    X_tilde = X - (1 / h) * (Z.conj().T @ CinvY)
    KR = (1 / h) * (Y.conj().T @ CinvY) + (1 / beta) * (X_tilde.conj().T @ X_tilde)
    # residual radical block BR + e G_R - KR ; take G_R = I
    GR = np.eye(BR.shape[0])
    residual = BR + e * GR - KR
    # visible block check BV - h^{-1} Z* C^{-1} Z - beta G_V
    GV = np.eye(BV.shape[0])
    vis = BV - (1 / h) * (Z.conj().T @ np.linalg.solve(C, Z)) - beta * GV
    return {
        "residual_eigs": [float(v) for v in np.linalg.eigvalsh(0.5 * (residual + residual.T))],
        "visible_eigs": [float(v) for v in np.linalg.eigvalsh(0.5 * (vis + vis.T))],
        "KR_eigs": [float(v) for v in np.linalg.eigvalsh(0.5 * (KR + KR.T))],
        "residual_min": float(np.min(np.linalg.eigvalsh(0.5 * (residual + residual.T)))),
        "visible_min": float(np.min(np.linalg.eigvalsh(0.5 * (vis + vis.T)))),
    }


def synthetic_family():
    rows = []
    rng = np.random.default_rng(8455)
    for e in (0.0, 0.02, 0.05, 0.1, 0.2, 0.4):
        for beta in (0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0):
            for h in (0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0):
                # dimensions: radical 2, visible 2, complement 2
                BR = np.diag([0.3, 0.1])  # mild positive
                BV = np.diag([1.0, 0.7])
                C = np.diag([2.0, 3.0])  # complement floor
                X = 0.1 * rng.standard_normal((2, 2))
                Y = 0.1 * rng.standard_normal((2, 2))
                Z = 0.2 * rng.standard_normal((2, 2))
                # optional terminal-like skew in visible cross
                Z = Z + np.array([[0.0, 0.4], [-0.4, 0.0]])
                diag = schur_three_block(BR, BV, C, X, Y, Z, h=h, beta=beta, e=e)
                rows.append(
                    {
                        "e": e,
                        "beta": beta,
                        "h": h,
                        **diag,
                        "all_nonneg_residual": diag["residual_min"] >= -1e-10,
                        "all_nonneg_visible": diag["visible_min"] >= -1e-10,
                    }
                )
    return rows


def capacity_toy():
    """Toy D vs C comparison: count vs packet rank on diagonal spectra."""
    rows = []
    for n in (8, 16, 32):
        # fake symbol eigenvalues: bathtub then plunge
        xs = np.linspace(-3, 3, n)
        spec = xs**2 - 0.5  # negative in a middle well
        for t in (-0.2, 0.0, 0.2, 0.5):
            D = int(np.sum(spec < t))  # count below threshold
            # repaired packet capacity C: allow rank = #modes with |spec-near-radical|
            near = np.sum(np.abs(spec) < 0.35)
            C = int(near)
            rows.append(
                {
                    "n": n,
                    "t": t,
                    "count_D": D,
                    "packet_cap_C": C,
                    "D_le_C": D <= C,
                    "gap_C_minus_D": C - D,
                }
            )
    return rows


def exact_inertia_examples():
    """Exact rational inertia samples for a 3x3 Loewner-like family."""
    rows = []
    for q in (F(1), F(2), F(1, 2), F(-1, 3)):
        M = [
            [F(2), q, F(1)],
            [q, F(2, 3), q],
            [F(1), q, F(2)],
        ]
        rows.append({"q": str(q), "inertia": list(inertia_ldl(M))})
    return rows


def main():
    print("=== C4 synthetic packet-floor table (provisional) ===")
    family = synthetic_family()
    for r in family[::3]:
        print(
            f"e={r['e']} beta={r['beta']} h={r['h']}: "
            f"res_min={r['residual_min']:.3e} vis_min={r['visible_min']:.3e}"
        )
    cap = capacity_toy()
    exact = exact_inertia_examples()

    # dependence summary: correlation between residual_min and visible_min
    res = np.array([r["residual_min"] for r in family])
    vis = np.array([r["visible_min"] for r in family])
    if np.std(res) > 0 and np.std(vis) > 0:
        corr = float(np.corrcoef(res, vis)[0, 1])
    else:
        corr = None

    payload = {
        "schema": "riemann.x8455.comp4.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": (
            "Synthetic blocks only. Random cross-terms are not Weil data. "
            "Capacity toy uses a fake bathtub spectrum. Useful as a margin map, not a theorem."
        ),
        "three_block_family": family,
        "residual_visible_corr": corr,
        "capacity_toy": cap,
        "exact_inertia_examples": exact,
        "pass_counts": {
            "residual_nonneg": sum(1 for r in family if r["all_nonneg_residual"]),
            "visible_nonneg": sum(1 for r in family if r["all_nonneg_visible"]),
            "both": sum(1 for r in family if r["all_nonneg_residual"] and r["all_nonneg_visible"]),
            "total": len(family),
        },
        "suggested_questions_for_other_agents": [
            "In production packets, does increasing h (complement floor) ever hurt residual_min more than it helps visible_min?",
            "Is there an exact identity linking residual_min + visible_min to a single Schur complement of H?",
            "Can the fake D<=C bathtub be replaced by Suzuki-symbol counts on one CCM matrix?",
        ],
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    digest = hashlib.sha256(text.encode()).hexdigest()
    payload["content_sha256"] = digest
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp4.json").write_text(text)
    (OUT / "comp4.txt").write_text(
        "C4 provisional summary\n"
        f"residual/visible corr~{corr}\n"
        f"pass both={payload['pass_counts']['both']}/{payload['pass_counts']['total']}\n"
        + "\n".join(f"q={r['q']} inertia={r['inertia']}" for r in exact)
        + f"\nsha256={digest}\n"
    )
    print(f"wrote {OUT/'comp4.json'} corr={corr}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
