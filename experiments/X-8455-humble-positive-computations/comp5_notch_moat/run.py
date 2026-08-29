#!/usr/bin/env python3
"""C5 — explicit-formula notch-moat table (midpoint zeros, discovery only).

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY only.

Instead of sieving primes to 1e7, this script evaluates a cheap zero-sum proxy
    S_m(x) = -2 sum_{j>m} w_j cos(gamma_j (x - x0))
with successive midpoint notches removing the first m modes (or attenuating
them by a fake certified radius).

This is meant to reproduce the qualitative collapse seen in O-15402 as a small
table another model can digest, without claiming a directed RH moat.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
from mpmath import mp, zetazero

mp.dps = 40
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def get_gammas(M=120):
    return np.array([float(mp.im(zetazero(k))) for k in range(1, M + 1)])


def weights_for_notches(gammas, m, eps=1e-8, law="inv_square"):
    w = np.zeros_like(gammas)
    for j, g in enumerate(gammas):
        if law == "inv_square":
            base = 1.0 / (g * g)
        elif law == "inv_exp":
            base = np.exp(-0.15 * g)
        else:
            base = 1.0 / (g * g)
        if j < m:
            base *= (eps / (g - eps)) ** 2
        w[j] = base
    return w


def scan_envelope(gammas, w, x0=3.0, xmin=14.0, xmax=40.0, npts=4000):
    xs = np.linspace(xmin, xmax, npts)
    # S(x) = -2 sum w cos(g(x-x0))
    # vectorized
    phase = np.cos(np.outer(xs - x0, gammas))
    S = -2.0 * phase @ w
    return {
        "min": float(S.min()),
        "max": float(S.max()),
        "absmax": float(np.max(np.abs(S))),
        "rms": float(np.sqrt(np.mean(S * S))),
        "argmax_x": float(xs[int(np.argmax(S))]),
        "argmin_x": float(xs[int(np.argmin(S))]),
    }


def main():
    print("=== C5 notch moat proxy (provisional) ===")
    gammas = get_gammas(120)
    tables = {}
    for law in ("inv_square", "inv_exp"):
        rows = []
        for m in range(0, 21):
            w = weights_for_notches(gammas, m, law=law)
            env = scan_envelope(gammas, w)
            cost = float(np.sum(2 * np.pi / gammas[:m])) if m else 0.0
            # residual theoretical abs-sum of weights
            row = {
                "n_notches": m,
                "support_cost": cost,
                "weight_abs_sum": float(2 * np.sum(w)),
                **env,
            }
            rows.append(row)
            print(
                f"law={law} notches={m}: absmax={env['absmax']:.3e} rms={env['rms']:.3e} cost={cost:.3f}"
            )
        tables[law] = rows

    # interesting comparison: cost vs log(absmax)
    efficiency = []
    for row in tables["inv_square"]:
        if row["n_notches"] == 0:
            continue
        efficiency.append(
            {
                "n_notches": row["n_notches"],
                "support_cost": row["support_cost"],
                "log10_absmax": float(np.log10(row["absmax"] + 1e-30)),
                "cost_per_log10": row["support_cost"] / max(1e-12, -np.log10(row["absmax"] + 1e-30)),
            }
        )

    payload = {
        "schema": "riemann.x8455.comp5.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": (
            "Uses mpmath zetazero midpoints, not certified balls. Weight laws are toy models "
            "for |transform|^2 decay, not the true universal window M(i gamma). "
            "Do not quote absmax as an RH-valid moat."
        ),
        "gammas_first10": [float(g) for g in gammas[:10]],
        "tables": tables,
        "cost_efficiency_inv_square": efficiency,
        "suggested_questions_for_other_agents": [
            "Which decay law best matches O-15401's empirical |M(i gamma)|^2 sequence?",
            "Is there a lemma that abs-sum after m notches is <= C * product (eps_j/gamma_j)^2 * sum_{j>m} gamma_j^{-2}?",
            "Does the phase center x0=3 (from O-15401) remain optimal after notches?",
        ],
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    digest = hashlib.sha256(text.encode()).hexdigest()
    payload["content_sha256"] = digest
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp5.json").write_text(text)
    lines = ["C5 provisional summary"]
    for row in tables["inv_square"]:
        lines.append(
            f"notches={row['n_notches']}: absmax={row['absmax']:.6e} rms={row['rms']:.6e} cost={row['support_cost']:.4f}"
        )
    lines.append(f"sha256={digest}")
    (OUT / "comp5.txt").write_text("\n".join(lines) + "\n")
    print(f"wrote {OUT/'comp5.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
