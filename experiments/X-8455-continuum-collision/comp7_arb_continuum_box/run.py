#!/usr/bin/env python3
"""D7 — Arb/acb.integral residual + Jacobian at (α_∞, r_∞).

Agent: cursor-grok-8455
Status: DIRECTED DISCOVERY (Arb integrate); Φ truncated with crude tail note

Uses flint `acb.integral` for rigorous quadrature of the truncated Φ series.
Still not a finished uniqueness certificate (needs Φ-tail bound + interval Newton).
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from flint import arb, acb, ctx

OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)

ctx.prec = 192

REF_A = arb("0.975779528461603467680421342178")
REF_R = arb("2.179490220360796425562316317235")


def phi_trunc(t: acb, nmax: int = 20, analytic: bool = False) -> acb:
    t = t  # even in real t; use abs for real path
    # On the real integration path t∈[0,T], use abs via real nonnegative
    tt = t
    if t.imag.contains(0) and t.real.lower() >= 0:
        pass
    pi = arb.pi()
    tot = acb(0)
    # en = exp(2t)
    en = (2 * tt).exp()
    for n in range(1, nmax + 1):
        nn = arb(n)
        term = (
            4 * pi * pi * (nn**4) * (acb("4.5") * tt).exp()
            - 6 * pi * (nn**2) * (acb("2.5") * tt).exp()
        ) * (-pi * (nn * nn) * en).exp()
        tot += term
    return tot


def G_arb(alpha: arb, s: arb, nmax: int = 20) -> arb:
    T = arb(1) / (2 * alpha)
    a = alpha
    ss = s

    def f(x, analytic):
        # x is acb
        return phi_trunc(x, nmax=nmax, analytic=analytic) * (2 * arb.pi() * a * ss * x).cos()

    I = acb.integral(f, acb(0), acb(T))
    return (2 * I).real


def Gr_arb(alpha: arb, s: arb, nmax: int = 20) -> arb:
    T = arb(1) / (2 * alpha)
    a = alpha
    ss = s

    def f(x, analytic):
        return (
            phi_trunc(x, nmax=nmax, analytic=analytic)
            * (-2 * arb.pi() * a * x)
            * (2 * arb.pi() * a * ss * x).sin()
        )

    I = acb.integral(f, acb(0), acb(T))
    return (2 * I).real


def main():
    print("=== D7 Arb acb.integral continuum residuals ===", flush=True)
    rows = []
    for nmax in (8, 12, 20):
        g = G_arb(REF_A, REF_R, nmax=nmax)
        gr = Gr_arb(REF_A, REF_R, nmax=nmax)
        row = {
            "nmax": nmax,
            "G": str(g),
            "Gr": str(gr),
            "G_mid": str(g.mid()),
            "G_rad": str(g.rad()),
            "Gr_mid": str(gr.mid()),
            "Gr_rad": str(gr.rad()),
            "G_contains_0": bool(g.contains(0)),
            "Gr_contains_0": bool(gr.contains(0)),
        }
        rows.append(row)
        print(row, flush=True)

    # tiny box: evaluate at corners / mid with radius via union
    rad = arb("1e-10")
    a_box = arb(REF_A, rad)
    r_box = arb(REF_R, rad)
    # Evaluating G on fat balls for alpha/s directly may explode; sample corners
    corners = []
    for da in (-rad, rad):
        for dr in (-rad, rad):
            g = G_arb(REF_A + da, REF_R + dr, nmax=20)
            gr = Gr_arb(REF_A + da, REF_R + dr, nmax=20)
            corners.append({"da": str(da), "dr": str(dr), "G": str(g), "Gr": str(gr)})
            print("corner", corners[-1], flush=True)

    # Jacobian FD with Arb point evals
    h = arb("1e-12")
    dG_da = (G_arb(REF_A + h, REF_R) - G_arb(REF_A - h, REF_R)) / (2 * h)
    dGr_da = (Gr_arb(REF_A + h, REF_R) - Gr_arb(REF_A - h, REF_R)) / (2 * h)
    dG_dr = Gr_arb(REF_A, REF_R)
    dGr_dr = (Gr_arb(REF_A, REF_R + h) - Gr_arb(REF_A, REF_R - h)) / (2 * h)
    det = dG_da * dGr_dr - dG_dr * dGr_da
    jac = {
        "dG_da": str(dG_da),
        "dG_dr": str(dG_dr),
        "dGr_da": str(dGr_da),
        "dGr_dr": str(dGr_dr),
        "det": str(det),
        "det_excludes_0": (not det.contains(0)),
        "det_mid": str(det.mid()),
        "det_rad": str(det.rad()),
    }
    print("jac", jac, flush=True)

    payload = {
        "schema": "riemann.x8455.d7.v1",
        "status": "DIRECTED_PROVISIONAL",
        "disclaimer": (
            "Arb acb.integral of truncated Φ (nmax terms). "
            "No explicit n>nmax tail bound yet; not a uniqueness certificate."
        ),
        "precision_bits": int(ctx.prec),
        "reference": {"alpha": str(REF_A), "r": str(REF_R)},
        "point_by_nmax": rows,
        "corners_1e-10": corners,
        "jacobian": jac,
        "suggested_next": [
            "Add a rigorous Φ tail bound for n>nmax on [0,T].",
            "Interval Newton uniqueness in a box around (α_∞,r_∞).",
            "Directed finite R_N Newton for N=4…20.",
        ],
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "d7.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "d7.txt").write_text(json.dumps({"point": rows[-1], "jac": jac}, indent=2) + "\n")
    print("wrote", OUT / "d7.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
