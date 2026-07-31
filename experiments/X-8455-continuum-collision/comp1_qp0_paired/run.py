#!/usr/bin/env python3
"""D1 — Qp=0, paired even/odd soft modes, collision-vector alignment.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY (absorbing PR #182 review corrections)
"""

from __future__ import annotations

import hashlib
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp
from mpmath import mp, nstr

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import Fwin, Phi  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 40
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)

# C41-ish α_def seeds
ALPHA_DEF = {
    4: 0.9734385944092645,
    6: 0.9750627888059245,
    8: 0.9754669242082166,
    10: 0.9756154785668478,
    12: 0.9756828425684942,
}


def pack(alpha, N):
    nodes = list(range(-N, N + 1))
    pvals = [((-1) ** j) * Fwin(alpha, j, Phi) for j in nodes]
    p = np.array([float(v) for v in pvals], dtype=float)
    # Loewner via rationalized poly (same pipeline as before; discovery only)
    pf = [F(nstr(v, 26, strip_zeros=False)) for v in pvals]
    s = sp.symbols("s")
    P = 0
    for i, lam in enumerate(nodes):
        term = 1
        for mu in nodes:
            if mu != lam:
                term *= mu - s
        P += sp.Rational(pf[i]) * term
    P = sp.Poly(sp.expand(P), s)
    Pd = sp.diff(P.as_expr(), P.gen)
    Pdd = sp.diff(Pd, P.gen)
    b, a = {}, {}
    for lam in nodes:
        Pi = complex(P.as_expr().subs(P.gen, lam))
        Pdi = complex(Pd.subs(P.gen, lam))
        Pddi = complex(Pdd.subs(P.gen, lam))
        b[lam] = -Pdi / Pi
        a[lam] = (Pdi * Pdi - Pi * Pddi) / (Pi * Pi)
    Q = np.zeros((len(nodes), len(nodes)))
    for i, li in enumerate(nodes):
        for j, lj in enumerate(nodes):
            Q[i, j] = float(np.real(a[li] if i == j else (b[li] - b[lj]) / (li - lj)))
    Qs = 0.5 * (Q + Q.T)
    return nodes, p, Qs, P


def align(u, v):
    u = u / (np.linalg.norm(u) + 1e-30)
    v = v / (np.linalg.norm(v) + 1e-30)
    return float(abs(np.dot(u, v)))


def main():
    print("=== D1 Qp=0 + paired collision geometry ===", flush=True)
    rows = []
    for N, adef in ALPHA_DEF.items():
        for tag, alpha in (
            ("pass", adef + 0.002),
            ("near", adef),
            ("fail", adef - 0.002),
        ):
            nodes, p, Q, Ppoly = pack(alpha, N)
            # Qp residual
            Qp = Q @ p
            qp_rel = float(np.linalg.norm(Qp) / (np.linalg.norm(p) + 1e-30))

            ew, ev = np.linalg.eigh(Q)
            # modes: sort by |eig|
            order = np.argsort(np.abs(ew))
            # structural kernel ~ smallest |eig|, should align with p
            k0 = int(order[0])
            align_p = align(ev[:, k0], p)

            # classify even/odd of eigenvectors
            idx = {nodes[i]: i for i in range(len(nodes))}

            def parity_mass(vec):
                even = sum((vec[idx[j]] - (vec[idx[-j]] if j else vec[idx[0]])) ** 2 for j in nodes if j > 0)
                # simpler: even part / odd part norms
                e = 0.0
                o = 0.0
                for j in nodes:
                    if j == 0:
                        e += vec[idx[0]] ** 2
                    elif j > 0:
                        ve = 0.5 * (vec[idx[j]] + vec[idx[-j]])
                        vo = 0.5 * (vec[idx[j]] - vec[idx[-j]])
                        e += 2 * ve * ve
                        o += 2 * vo * vo
                return float(e), float(o)

            # soft candidates: smallest eigs excluding kernel
            soft_info = []
            for k in order[:6]:
                e_m, o_m = parity_mass(ev[:, k])
                soft_info.append(
                    {
                        "eig": float(ew[k]),
                        "mass_even": e_m,
                        "mass_odd": o_m,
                        "align_p": align(ev[:, k], p),
                    }
                )

            # estimate r from double-root attempt: use |r|~2.18 seed via poly roots
            # find real roots of P near ±2.18
            roots = [complex(z) for z in sp.roots(Ppoly) ] if False else []
            # use numpy companion on float coeffs of P
            coeffs = [float(c) for c in Ppoly.all_coeffs()]
            try:
                rts = np.roots(coeffs)
            except Exception:  # noqa: BLE001
                rts = np.array([])
            real_rts = sorted([float(z.real) for z in rts if abs(z.imag) < 1e-6], key=abs)
            # pick positive real root closest to 2.18
            r_hat = None
            if real_rts:
                pos = [x for x in real_rts if x > 0]
                if pos:
                    r_hat = float(min(pos, key=lambda x: abs(x - 2.18)))

            align_even_x = align_odd_x = None
            if r_hat is not None and abs(r_hat) > 1e-9:
                x_even = np.array([p[idx[j]] / (j * j - r_hat * r_hat) if abs(j * j - r_hat * r_hat) > 1e-14 else 0.0 for j in nodes])
                x_odd = np.array([j * p[idx[j]] / (j * j - r_hat * r_hat) if abs(j * j - r_hat * r_hat) > 1e-14 else 0.0 for j in nodes])
                # compare to soft evecs: first even non-kernel and first odd
                even_soft = odd_soft = None
                for k in order:
                    if abs(ew[k]) < 1e-10 and align(ev[:, k], p) > 0.9:
                        continue  # skip kernel p
                    e_m, o_m = parity_mass(ev[:, k])
                    if even_soft is None and e_m > 0.8:
                        even_soft = ev[:, k]
                    if odd_soft is None and o_m > 0.8:
                        odd_soft = ev[:, k]
                    if even_soft is not None and odd_soft is not None:
                        break
                if even_soft is not None:
                    align_even_x = align(even_soft, x_even)
                if odd_soft is not None:
                    align_odd_x = align(odd_soft, x_odd)

            row = {
                "N": N,
                "tag": tag,
                "alpha": float(alpha),
                "qp_rel": qp_rel,
                "align_kernel_with_p": align_p,
                "kernel_eig": float(ew[k0]),
                "n_neg": int(np.sum(ew < -1e-12)),
                "soft_modes": soft_info,
                "r_hat_from_poly": r_hat,
                "align_x_even": align_even_x,
                "align_x_odd": align_odd_x,
            }
            rows.append(row)
            print(
                f"N={N} {tag} a={alpha:.6f} qp_rel={qp_rel:.3e} align_p={align_p:.6f} "
                f"n_neg={row['n_neg']} r_hat={r_hat} "
                f"align_xe={align_even_x} align_xo={align_odd_x}",
                flush=True,
            )

    payload = {
        "schema": "riemann.x8455.d1.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Float Loewner; review claims Qp=0 and paired kernels are exact.",
        "rows": rows,
        "review_corrections_absorbed": [
            "Structural ~0 mode should be Qp=0 (target kernel).",
            "First deficit-four is paired even/odd collision.",
            "Collision vectors x_even=p/(j^2-r^2), x_odd=j p/(j^2-r^2).",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "d1.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "d1.txt").write_text(
        "\n".join(
            f"N={r['N']} {r['tag']} qp_rel={r['qp_rel']:.3e} align_p={r['align_kernel_with_p']:.6f} "
            f"n_neg={r['n_neg']} xe={r['align_x_even']} xo={r['align_x_odd']}"
            for r in rows
        )
        + "\n"
    )
    print("wrote", OUT / "d1.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
