#!/usr/bin/env python3
"""C3 — pole-free / pole-subtracted terminal Hankel support ladder.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY only.

Focus: profiles with approximately vanishing Laplace moment v^- (pole channel
killed algebraically), then watch the Rayleigh quotient of the remaining
terminal Hankel along an expanding support ladder.

The hope is not to "find a counterexample" here, but to leave a short table
showing whether the remainder looks bounded, drifting, or phase-unstable at
toy scale — fuel for someone else's lemma about translation-boundedness.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from jsonutil import dumps as json_dumps  # noqa: E402

OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def primes_upto(n: int):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p :: p] = False
    return list(np.nonzero(sieve)[0])


def prime_powers_window(a, R, n_cap: float | None = None):
    """Enumerate terminal-window prime powers, optionally truncating n<=n_cap.

    Truncation is a reconnaissance convenience only; it is not the complete
    terminal sum required by L-15610.
    """
    lo, hi = np.exp(2 * a - 2 * R), np.exp(2 * a)
    if n_cap is not None:
        hi = min(hi, n_cap)
    if hi < 2:
        return [], True
    truncated = hi + 1e-12 < np.exp(2 * a)
    primes = primes_upto(int(hi) + 5)
    out = []
    for p in primes:
        pk, k = p, 1
        while pk <= hi + 1e-12:
            if pk >= lo - 1e-12:
                out.append((pk, float(np.log(p) / np.sqrt(pk))))
            if pk > hi / p:
                break
            pk *= p
            k += 1
    return out, truncated


def make_polefree_basis(R, m=6, grid=500):
    x = np.linspace(0.0, R, grid)
    dx = x[1] - x[0]
    # raw bumps
    raw = []
    centers = np.linspace(0.15 * R, 0.85 * R, m + 1)
    width = 0.28 * R
    for c in centers:
        y = np.zeros_like(x)
        left, right = c - width / 2, c + width / 2
        mask = (x > max(left, 0)) & (x < min(right, R))
        t = (x[mask] - left) / (right - left)
        y[mask] = np.sin(np.pi * np.clip(t, 0, 1)) ** 3
        raw.append(y)
    # build differences that approximately kill int e^{-r/2} phi
    w = np.exp(-0.5 * x)
    masses = np.array([np.sum(w * y) * dx for y in raw])
    phis = []
    for i in range(m):
        # phi = raw[i] - (m_i/m_last) raw[last]
        if abs(masses[-1]) < 1e-15:
            phis.append(raw[i].copy())
        else:
            phis.append(raw[i] - (masses[i] / masses[-1]) * raw[-1])
    vminus = np.array([np.sum(w * phi) * dx for phi in phis])
    G = np.zeros((m, m))
    for i in range(m):
        for j in range(i, m):
            G[i, j] = G[j, i] = np.sum(phis[i] * phis[j]) * dx
    return x, dx, phis, vminus, G


def hankel(x, dx, phis, u):
    m = len(phis)
    C = np.zeros((m, m))
    for i in range(m):
        for j in range(i, m):
            yi = np.interp(u - x, x, phis[i], left=0.0, right=0.0)
            val = np.sum(yi * phis[j]) * dx
            C[i, j] = C[j, i] = val
    return C


def rayleigh_stats(H, G):
    # solve gen. eigen H v = lam G v
    # use whitening
    evals, evecs = np.linalg.eigh(G)
    evals = np.clip(evals, 1e-18, None)
    W = evecs @ np.diag(1 / np.sqrt(evals)) @ evecs.T
    Hw = W.T @ H @ W
    ew = np.linalg.eigvalsh(0.5 * (Hw + Hw.T))
    return {
        "min": float(ew[0]),
        "max": float(ew[-1]),
        "absmax": float(np.max(np.abs(ew))),
        "eigs": [float(v) for v in ew],
    }


def main():
    print("=== C3 pole-free terminal Hankel ladder (provisional) ===")
    rows = []
    # Smoke taught: complete windows explode as exp(2a). For larger R we keep
    # a>2R but truncate the prime sum at n_cap so the hour-budget stays honest.
    n_cap = 8e4
    for R in (2.0, 2.5, 3.0, 3.5, 4.0, 5.0):
        x, dx, phis, vminus, G = make_polefree_basis(R, m=6, grid=500)
        for da in (0.5, 1.0, 1.5, 2.0, 2.5):
            a = 2 * R + da
            pps, truncated = prime_powers_window(a, R, n_cap=n_cap)
            H = np.zeros((len(phis), len(phis)))
            for n, c in pps:
                u = 2 * a - np.log(n)
                H += 2 * c * hankel(x, dx, phis, u)
            # residual pole subtraction (should be nearly zero already)
            vv = np.outer(vminus, vminus)
            H_centered = H - 2 * np.exp(a) * vv
            stats = rayleigh_stats(H_centered, G)
            row = {
                "R": R,
                "a": a,
                "da": da,
                "n_pps": len(pps),
                "truncated_at_n_cap": bool(truncated),
                "n_cap": n_cap,
                "vminus_norm": float(np.linalg.norm(vminus)),
                "rayleigh": stats,
                "frobenius": float(np.linalg.norm(H_centered)),
            }
            rows.append(row)
            print(
                f"R={R} a={a:.2f}: pps={len(pps)} trunc={truncated} |v-|={row['vminus_norm']:.2e} "
                f"min={stats['min']:.3e} max={stats['max']:.3e} absmax={stats['absmax']:.3e}"
            )

    # crude drift diagnostics by R
    by_R = {}
    for r in rows:
        by_R.setdefault(r["R"], []).append(r)
    drift = {}
    for R, lst in by_R.items():
        absmax = [x["rayleigh"]["absmax"] for x in lst]
        drift[str(R)] = {
            "absmax_series": absmax,
            "absmax_first": absmax[0],
            "absmax_last": absmax[-1],
            "ratio_last_over_first": absmax[-1] / absmax[0] if absmax[0] else None,
            "tentative_reading": (
                "looks growing"
                if absmax[-1] > 2 * absmax[0]
                else "looks shrinking"
                if absmax[-1] < 0.5 * absmax[0]
                else "looks roughly stable (toy scale only)"
            ),
        }

    payload = {
        "schema": "riemann.x8455.comp3.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": (
            "Pole-free basis is approximate (float cancellation of Laplace masses). "
            "No archimedean block, no second polar term, no directed primes. "
            "Drift labels are informal."
        ),
        "ladder": rows,
        "drift_by_R": drift,
        "suggested_questions_for_other_agents": [
            "If |v^-| is driven below 1e-12 exactly (rational profiles), does absmax stabilize in a?",
            "Is the observed sign oscillation explained by the first un-notched zero phase e^{i gamma (2a)}?",
            "Can one prove a uniform bound for pole-free packets from a single zero-sum majorant?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    digest = hashlib.sha256(text.encode()).hexdigest()
    payload["content_sha256"] = digest
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp3.json").write_text(text)
    (OUT / "comp3.txt").write_text(
        "C3 provisional summary\n"
        + "\n".join(
            f"R={r['R']} a={r['a']:.2f}: absmax={r['rayleigh']['absmax']:.6e} min={r['rayleigh']['min']:.6e}"
            for r in rows
        )
        + "\n"
        + "\n".join(f"R={R}: {v['tentative_reading']} ratio={v['ratio_last_over_first']}" for R, v in drift.items())
        + f"\nsha256={digest}\n"
    )
    print(f"wrote {OUT/'comp3.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
