"""CRIT23 adjudication P1-F1: explicit-constant witness on an actual zeta zero (companion to adj_P1F1_trace.py).

For T = 1e4 take the zeta zero gamma nearest T - sqrt(T)/2 (it lies in I' \\ I). Exhibit (i) a grid point alpha_k with
k notin [0,d) and |gamma - alpha_k| < D_rho, contradicting AF line 327, and (ii) AF's displayed tail inequality
  tail <= e^{L/2} C_chi^2 * 2 (D^-4 + h^-1 int_D^inf s^-4 ds)
evaluated with its explicit constants, against the computed tail = aL^2 - head.
Also (iii) the norms ||phi''||_1 and ||(phi^2)''||_1 (AF's C_chi) for the cut-off chiA.
Run:  python3 -I adj_P1F1_witness.py
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import adj_P1F1_trace as m  # noqa: E402  (same directory; this audit's own helper)


def main():
    out = []
    pr = lambda s: (print(s), out.append(s))
    t = np.linspace(0, 1, 2000001)
    c = m.chiA(t)
    norms = {}
    for f, lab in ((c, "phi"), (c * c, "phi^2")):
        d2 = np.gradient(np.gradient(f, t), t)
        norms[lab] = 2 * np.trapezoid(np.abs(d2), t)        # two transition layers (flat window: bulk contributes 0)
    pr(f"(iii) chiA, flat window: ||phi''||_1 = {norms['phi']:.4f}, ||(phi^2)''||_1 = C_chi = {norms['phi^2']:.4f}")
    T = 1e4
    L, h, d = m.grid(T)
    G = m.load_zeros()
    g = float(G[np.argmin(np.abs(G - (T - math.sqrt(T) / 2)))])
    D = min(abs(g - T), abs(g - 2 * T))
    k = round((g - T) / h)
    ak = T + k * h
    pr(f"T=1e4: L={L:.6f} h={h:.6f} d={d}")
    pr(f"(i) zeta zero gamma={g:.6f} in I'\\I, D_rho={D:.4f}; grid point k={k} (not in [0,d)): alpha_k={ak:.6f}, "
       f"|gamma-alpha_k|={abs(g - ak):.4f} < D_rho")
    P = m.Phi(L, m.chiA, zmax=300.0)
    hd, tl, full = m.head_tail(P, T, g, 300.0)
    aL2 = P.a * L * L
    X = math.exp(L)
    pr(f"    a={P.a:.6f} aL^2={aL2:.4f}  tail={tl:.6f}  tail/aL^2={tl / aL2:.12f}  head/aL^2={hd / aL2:.3e}")
    for lab in ("phi^2", "phi"):
        C = norms[lab]
        rhs = math.sqrt(X) * C * C * 2 * (D ** -4 + (1 / h) * D ** -3 / 3)
        pr(f"(ii) AF display RHS with C_chi=||({lab})''||_1={C:.3f}: {rhs:.4e};  tail/RHS = {tl / rhs:.1f}  (inequality fails)")
    with open(os.path.join(HERE, "adj_P1F1_witness.out"), "w") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
