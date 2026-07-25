#!/usr/bin/env python3
"""
X-0005d -- Joint multi-line fit: removing the blending floor.

Agent: claude-01
Completes the M-0003 loop begun in X-0005b and continued in X-0005c.

WHERE WE WERE

X-0005c reduced the screen's sensitivity floor to delta ~ 0.1 overall, and
showed that the residual scatter is not leakage but LINE BLENDING: reading each
peak independently fails when two ordinates are closer than the window
resolution (48.005 and 49.774, separated by 1.77 against a resolution of 2.37,
accounted for all of the scatter).

THE FIX

Blending is only a resolution limit when the line positions are unknown.  They
are not: X-0001/X-0004 supply certified ordinates.  So instead of reading peaks
off a periodogram, fit the model

    f(u)  =  c  +  sum_j [ a_j cos(gamma_j u) + b_j sin(gamma_j u) ]

by ordinary least squares over each window, with the gamma_j FIXED at the known
ordinates, and take the line amplitude to be A_j = sqrt(a_j^2 + b_j^2).  Least
squares handles the non-orthogonality of the sinusoids over a finite window
exactly, so neighbouring lines no longer contaminate each other.

The observable is unchanged: for rho = 1/2 + delta + i gamma_j the amplitude
grows like e^{delta u}, so A_late/A_early = e^{delta D} between two windows of
equal length separated by D.

STATUS: EMPIRICAL.  Floating point; certifies nothing.  A lead from this must
still be converted into a rectangle for L-0002 / T-0001.

Usage: python3 joint_fit.py [X]
"""
from __future__ import annotations

import cmath
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from run import psi_samples  # noqa: E402
from validate import ORDINATES  # noqa: E402


def load_ordinates(n):
    """The certified ordinates produced by X-0004, falling back to the short
    hard-coded list.  Widening the modelled band is the main lever on model
    mismatch (O-0002)."""
    path = os.path.join(HERE, "..", "X-0004-lehmer-pairs", "results",
                        "lehmer-T2000.json")
    try:
        with open(path) as fh:
            zs = json.load(fh)["zeros"]
        vals = [float(z.split(" ")[0].lstrip("[")) for z in zs]
        return vals[:n]
    except Exception:
        return ORDINATES[:n]


def design_solve(us, f, gammas, extra_terms=True):
    """Least-squares fit of

        c + d e^{-u/2} + sum_j (a_j cos(g_j u) + b_j sin(g_j u))

    to f on the grid us.  The e^{-u/2} column absorbs the NON-ZERO terms of the
    explicit formula: psi(x) = x - sum_rho x^rho/rho - log(2 pi)
    - (1/2) log(1 - x^-2), whose contribution to f(u) = (psi(e^u)-e^u)e^{-u/2}
    is -(log 2 pi) e^{-u/2} plus a term smaller still.  Leaving it out is one of
    the two sources of model mismatch identified in O-0002.

    Returns the list of amplitudes sqrt(a_j^2+b_j^2)."""
    m = len(gammas)
    k = 2 * m + 1 + (1 if extra_terms else 0)
    # normal equations  (A^T A) x = A^T f, built streaming to avoid a big matrix
    ATA = [[0.0] * k for _ in range(k)]
    ATf = [0.0] * k
    for u, fv in zip(us, f):
        row = [1.0]
        if extra_terms:
            row.append(math.exp(-u / 2))
        for g in gammas:
            row.append(math.cos(g * u))
            row.append(math.sin(g * u))
        for i in range(k):
            ri = row[i]
            if ri == 0.0:
                continue
            ATfi = ri * fv
            ATf[i] += ATfi
            Ai = ATA[i]
            for j in range(i, k):
                Ai[j] += ri * row[j]
    for i in range(k):
        for j in range(i):
            ATA[i][j] = ATA[j][i]

    # Gaussian elimination with partial pivoting
    M = [ATA[i][:] + [ATf[i]] for i in range(k)]
    for col in range(k):
        piv = max(range(col, k), key=lambda r: abs(M[r][col]))
        if abs(M[piv][col]) < 1e-14:
            raise ValueError("singular design matrix")
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        for r in range(col + 1, k):
            fac = M[r][col] / pv
            if fac:
                for c in range(col, k + 1):
                    M[r][c] -= fac * M[col][c]
    x = [0.0] * k
    for r in range(k - 1, -1, -1):
        s = M[r][k] - sum(M[r][c] * x[c] for c in range(r + 1, k))
        x[r] = s / M[r][r]
    off = 2 if extra_terms else 1
    return [math.hypot(x[off + 2 * j], x[off + 1 + 2 * j]) for j in range(m)]


def grid(a, b, n):
    return [a + (b - a) * i / (n - 1) for i in range(n)]


def synthetic_f(us, zeros):
    out = []
    for u in us:
        tot = 0.0
        for beta, g in zeros:
            rho = complex(beta, g)
            tot += 2.0 * (cmath.exp((rho - 0.5) * u) / rho).real
        out.append(-tot)
    return out


def main():
    X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 4 * 10**7
    ulo, uhi = math.log(1000.0), math.log(X)
    W = (uhi - ulo) / 2
    u1, u2 = ulo, ulo + W
    D = W
    n = 3000
    nlines = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    G = load_ordinates(nlines)
    report = G[:12]

    print(f"X = {X:.3g}   window W = {W:.3f}   separation D = {D:.3f}   "
          f"{len(G)} modelled lines")
    out = {"experiment": "X-0005d", "agent": "claude-01", "status": "EMPIRICAL",
           "X": X, "W": W, "D": D, "n_modelled_lines": len(G),
           "design": "joint least-squares fit at known certified ordinates",
           "synthetic": []}

    eu, lu = grid(u1, u1 + W, n), grid(u2, u2 + W, n)

    base = [(0.5, g) for g in G]
    Ae = design_solve(eu, synthetic_f(eu, base), G)
    Al = design_solve(lu, synthetic_f(lu, base), G)
    ratios = [Al[i] / Ae[i] for i in range(len(report))]
    scatter = max(abs(r - 1.0) for r in ratios)
    print(f"on-line baseline ratios: {min(ratios):.6f} .. {max(ratios):.6f}"
          f"   => scatter {scatter:.2e}")
    print("   (periodogram designs gave 0.1494 and 0.1682)")
    out["baseline_scatter"] = scatter
    out["baseline_scatter_prior_designs"] = [0.1494, 0.1682]

    ti = 3
    for delta in [0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 0.0005]:
        zs = [(0.5 + delta if i == ti else 0.5, g) for i, g in enumerate(G)]
        Ae2 = design_solve(eu, synthetic_f(eu, zs), G)
        Al2 = design_solve(lu, synthetic_f(lu, zs), G)
        r = Al2[ti] / Ae2[ti]
        det = abs(r - 1.0) > 3 * scatter
        out["synthetic"].append({"delta": delta, "ratio": r,
                                 "predicted": math.exp(D * delta),
                                 "detected_at_3x_scatter": bool(det)})
        print(f"  delta={delta:<7} ratio={r:9.6f} (predicted {math.exp(D*delta):9.6f})"
              f"  detected={det}")
    floor = min((r["delta"] for r in out["synthetic"]
                 if r["detected_at_3x_scatter"]), default=None)
    out["sensitivity_floor_delta"] = floor
    print(f"=> sensitivity floor: delta >= {floor}   "
          f"(periodogram designs: 0.2, then 0.1)")

    print("\nreal sieve data:")
    allu = sorted(set(eu) | set(lu))
    psis = psi_samples(X, allu)
    pmap = dict(zip(allu, psis))
    fe = [(pmap[u] - math.exp(u)) / math.exp(u / 2) for u in eu]
    fl = [(pmap[u] - math.exp(u)) / math.exp(u / 2) for u in lu]
    Re_, Rl = design_solve(eu, fe, G), design_solve(lu, fl, G)
    rows = []
    for i, g in enumerate(report):
        r = Rl[i] / Re_[i]
        rows.append({"gamma": g, "ratio": r, "implied_delta": math.log(r) / D})
        print(f"  gamma={g:9.4f}  ratio={r:8.5f}  implied delta={math.log(r)/D:+.5f}")
    out["real_data"] = rows
    out["max_abs_implied_delta"] = max(abs(x["implied_delta"]) for x in rows)
    print(f"  max |implied delta| = {out['max_abs_implied_delta']:.5f}")
    out["interpretation"] = (
        "The implied displacements are now dominated by the finite-X error of "
        "the explicit formula (the neglected non-zero terms and the zeros above "
        "the modelled band), not by blending.  They are NOT bounds -- there is "
        "no error analysis behind them -- but the sensitivity floor from the "
        "planted-zero test IS a measurement of what this screen can see."
    )

    path = os.path.join(HERE, "results", f"joint-fit-X{X}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\nwrote", path)


if __name__ == "__main__":
    main()
