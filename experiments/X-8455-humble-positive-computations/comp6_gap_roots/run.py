#!/usr/bin/env python3
"""C6 — gap parity, root placement, and two geometric references.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

Near the windowed transition, ask:
  1) does #same-sign adjacent pairs track the Sturm deficit?
  2) do real roots of P sit near zeta zeros / (2 pi), or near the sinc lattice?
  3) do failing cases park nonreal roots at a reproducible imag height?

This is a geometry table, not a proof of L-16003's converse (already audited as false in general).
"""

from __future__ import annotations

import hashlib
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp
from mpmath import mp, mpf, pi, nstr

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import Xi, Fwin, Phi, gammas  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 50
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def to_frac(x, digits=28) -> F:
    return F(nstr(x, digits, strip_zeros=False))


def same_sign_pairs(p):
    c = 0
    for a, b in zip(p, p[1:]):
        if a == 0 or b == 0:
            continue
        if (a > 0 and b > 0) or (a < 0 and b < 0):
            c += 1
    return c


def build_P(nodes, vals, s, digits=28):
    pfrac = [to_frac(v, digits) for v in vals]
    P = sp.Integer(0)
    for i, lam in enumerate(nodes):
        term = sp.Integer(1)
        for j, mu in enumerate(nodes):
            if i != j:
                term *= mu - s
        P += sp.Rational(pfrac[i]) * term
    return sp.Poly(sp.expand(P), s), pfrac


def root_geometry(P, alpha, N, zeta_scaled):
    """Compare complex roots of P to zeta-scaled and sinc lattices (float discovery)."""
    # numerical roots via numpy companion on float coeffs
    co = [complex(c) for c in P.all_coeffs()]
    if abs(co[0]) < 1e-30:
        return {"error": "leading coeff tiny"}
    roots = np.roots(co)
    real_roots = []
    nonreal = []
    for r in roots:
        if abs(r.imag) < 1e-8:
            real_roots.append(float(r.real))
        elif r.imag > 0:
            nonreal.append((float(r.real), float(r.imag)))
    real_roots.sort()

    # nearest zeta-scaled reference: gamma/(2pi)
    zeta_ref = [float(g / (2 * pi)) for g in zeta_scaled]
    sinc_ref = [float(k) for k in range(-N, N + 1) if k != 0]  # node lattice itself
    # also "frequency lattice" w = k / alpha mapped into node units? 
    # CvS nodes are integers; Xi zeros at gamma map to node-ish coordinate gamma/(2pi)
    # sinc artifact roots often near integers when truncation dominates

    def nn_stats(vals, refs):
        if not vals or not refs:
            return None
        dists = []
        for v in vals:
            d = min(abs(v - r) for r in refs)
            dists.append(d)
        return {
            "mean_nn": float(np.mean(dists)),
            "max_nn": float(np.max(dists)),
            "median_nn": float(np.median(dists)),
        }

    # nonreal imag heights
    imag_heights = sorted([im for _, im in nonreal])
    return {
        "n_real_float": len(real_roots),
        "n_nonreal_pairs_float": len(nonreal),
        "real_roots": real_roots,
        "nonreal_upper": nonreal,
        "imag_heights": imag_heights,
        "nn_to_zeta_over_2pi": nn_stats(real_roots, zeta_ref + [-z for z in zeta_ref]),
        "nn_to_nonzero_integers": nn_stats(real_roots, sinc_ref),
        "mean_abs_real_root": float(np.mean(np.abs(real_roots))) if real_roots else None,
    }


def main():
    print("=== C6 gap/root geometry (provisional) ===", flush=True)
    s = sp.symbols("s")
    zeta_scaled = gammas(12)
    rows = []
    grid = [
        (1.05, 4), (1.00, 4), (0.98, 4), (0.96, 4), (0.94, 4), (0.90, 4),
        (1.05, 6), (1.00, 6), (0.98, 6), (0.96, 6), (0.94, 6), (0.90, 6),
    ]
    for alpha, N in grid:
        nodes = list(range(-N, N + 1))
        for kind, maker in (
            ("windowed", lambda j: ((-1) ** j) * Fwin(alpha, j, Phi)),
            ("sampled", lambda j: ((-1) ** j) * Xi(2 * pi * mpf(alpha) * j)),
        ):
            vals = [maker(j) for j in nodes]
            P, pfrac = build_P(nodes, vals, s)
            deg = int(P.degree())
            g = sp.gcd(P, P.diff())
            nre = int(sp.Poly(P.quo(g), s).count_roots())
            ssp = same_sign_pairs(pfrac)
            geom = root_geometry(P, alpha, N, zeta_scaled)
            # sign pattern string
            signs = "".join("+" if v > 0 else "-" if v < 0 else "0" for v in pfrac)
            row = {
                "alpha": alpha,
                "N": N,
                "kind": kind,
                "deg": deg,
                "n_real_sturm": nre,
                "deficit": deg - nre,
                "same_sign_pairs": ssp,
                "gap_lower_bound_L16003": ssp,  # #real >= ssp
                "bound_gap": nre - ssp,
                "sign_pattern": signs,
                "geometry": geom,
            }
            rows.append(row)
            print(
                f"{kind:8} a={alpha} N={N}: def={deg-nre} ssp={ssp} bound_gap={nre-ssp} "
                f"nn_zeta={geom.get('nn_to_zeta_over_2pi')} imag={geom.get('imag_heights')}",
                flush=True,
            )

    # cross summary: when does deficit==2*something related to unresolved low gaps?
    payload = {
        "schema": "riemann.x8455.comp6.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": (
            "Float np.roots geometry is discovery-only. Sturm counts use rationalized coeffs. "
            "L-16003 converse is already known false in general; this only tables nearby cases."
        ),
        "rows": rows,
        "suggested_questions_for_other_agents": [
            "In failing windowed rows, are imag heights clustering near a universal value?",
            "Is bound_gap=0 exactly on the passing windowed side and >0 exactly on the failing side?",
            "Do real roots prefer zeta/(2pi) on the passing side and integers on the failing/sampled side?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp6.json").write_text(text)
    lines = ["C6 provisional"]
    for r in rows:
        lines.append(
            f"{r['kind']} a={r['alpha']} N={r['N']} def={r['deficit']} ssp={r['same_sign_pairs']} "
            f"bound_gap={r['bound_gap']} nn_zeta={r['geometry'].get('nn_to_zeta_over_2pi')}"
        )
    (OUT / "comp6.txt").write_text("\n".join(lines) + "\n")
    print("wrote", OUT / "comp6.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
