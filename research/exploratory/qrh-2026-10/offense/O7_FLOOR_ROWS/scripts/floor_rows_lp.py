#!/usr/bin/env python3
"""O7 floor rows: exact-rational LP for the Sep 30 architecture with (i) a floor-row saving theta_F,
(ii) a near-critical saving theta_NC in every DH bin, (iii) Gram loss either the manuscript's b/12
(Prop 15.2 branches max(0, b/6, 2b - ly)) or 'zero' = the P_a^{1/6} branch b/6 removed while the
P_a^2/Y' branch 2b - ly is kept (the O3 convention, offense/O3_SEP30_X_OCT5/scripts/o3_barriers.py).

PROPOSED / EXPLORATORY.  Copied and modified from ../../scripts/{barrier_lp.py, floor_lp.py}
(originals untouched).  Model = stated output exponents of [OAI] Part II lemmas (ARCH hypothesis of
FLOOR_BIN_BARRIER.md Sec. 4); nothing here is a theorem about L-functions.

Variables v = (lx, ly, ell, s); every constraint is  coeffs . v <= rhs.
Low side (threshold_calculus.low_threshold at dd = 0, which is the worst dd for these branches):
    s >= 1 - lx/2 - h/6 + (-ly + gram + E)/2,   h = 1 - lx + ell,  M = lx + ly,
    E in {M, (2M+1+3ell)/4, 2M+ell-1} (paper)  or  {M, 2M+ell-1} plus M >= 2 ell (optimal).
High side, bin (a, R) at the top dyad d = h, x = 1/2, beta* -> s:
    a(1 - ly) + h(R + delta/2 - 1/6) - ell/2 + delta*ell/2 - s <= 0.
Small rows (Sec. 20.3): h(17/50 - 1/6) - ly/2 <= 0.
Certificates: rational dual multipliers, verified exactly; a-posteriori fine-grid check of every
bin delta in (delta0, 5/6] with beta* = max(s, a).
"""
from fractions import Fraction as Fr
import sys
import numpy as np
from scipy.optimize import linprog

Z0 = Fr(17, 50)


def low_rows(gram='b12', energy='paper'):
    rows = []
    # s >= 5/6 - lx/3 - ly/2 - ell/6 + gram/2 + E/2   (since 1 - lx/2 - (1-lx+ell)/6 = 5/6 - lx/3 - ell/6)
    if energy == 'paper':
        Es = [([Fr(1), Fr(1), Fr(0)], Fr(0)),                    # E = M
              ([Fr(1, 2), Fr(1, 2), Fr(3, 4)], Fr(1, 4)),         # E = (2M+1+3ell)/4
              ([Fr(2), Fr(2), Fr(1)], Fr(-1))]                    # E = 2M + ell - 1
    else:
        Es = [([Fr(1), Fr(1), Fr(0)], Fr(0)), ([Fr(2), Fr(2), Fr(1)], Fr(-1))]
    if gram == 'b12':
        Gs = [([Fr(0), Fr(0), Fr(0)], Fr(0)),                     # 0
              ([Fr(-1, 6), Fr(1, 6), Fr(0)], Fr(0)),              # b/6, b = ly - lx
              ([Fr(-2), Fr(1), Fr(0)], Fr(0))]                    # 2b - ly = ly - 2 lx
    else:   # 'zero': the P_a^{1/6} term (b/6) removed; the P_a^2/Y' term (2b - ly) is kept, as in O3
        Gs = [([Fr(0), Fr(0), Fr(0)], Fr(0)),
              ([Fr(-2), Fr(1), Fr(0)], Fr(0))]
    for (ec, e0) in Es:
        for (gc, g0) in Gs:
            # s >= 5/6 + c . (lx, ly, ell)
            c = [Fr(-1, 3) + (ec[0] + gc[0])/2, Fr(-1, 2) + (ec[1] + gc[1])/2, Fr(-1, 6) + (ec[2] + gc[2])/2]
            const = Fr(5, 6) + (e0 + g0)/2
            rows.append(([c[0], c[1], c[2], Fr(-1)], -const))
    if energy == 'optimal':
        rows.append(([Fr(-1), Fr(-1), Fr(2), Fr(0)], Fr(0)))    # M >= 2 ell
    return rows


def bin_row(a, R, x=Fr(1, 2)):
    delta = 2*a - 1
    c_h = R + delta/2 - Fr(1, 6)
    return ([-c_h, -a, c_h - Fr(1, 2) + x*delta, Fr(-1)], -(a + c_h))


def validity_rows(require_lx_le_ly=True):
    rows = [([Fr(-1), Fr(0), Fr(1), Fr(0)], Fr(0)),               # ell <= lx
            ([Fr(0), Fr(-1), Fr(1), Fr(0)], Fr(0)),               # ell <= ly
            ([Fr(0), Fr(0), Fr(-1), Fr(0)], Fr(0))]               # ell >= 0
    if require_lx_le_ly:
        rows.append(([Fr(1), Fr(-1), Fr(0), Fr(0)], Fr(0)))
    # small rows: h(z0 - 1/6) - ly/2 <= 0, h = 1 - lx + ell
    k = Z0 - Fr(1, 6)
    rows.append(([-k, Fr(-1, 2), k, Fr(0)], -k))
    return rows


DGRID = [Fr(k, 300) for k in range(1, 201)]   # delta in (0, 2/3]


def rows_for(a0, thF, gram, energy, dh=True, thNC=Fr(0), lxly=True):
    rows = low_rows(gram, energy) + validity_rows(lxly) + [bin_row(a0, 1 - thF)]
    if dh:
        d0 = 2*a0 - 1
        for dl in DGRID:
            if dl <= d0:
                continue
            R = max(1 - dl - thNC, (1 - dl)/2)
            rows.append(bin_row((1 + dl)/2, R))
    return rows


def solve(rows):
    A = np.array([[float(c) for c in r[0]] for r in rows]); b = np.array([float(r[1]) for r in rows])
    return linprog([0, 0, 0, 1], A_ub=A, b_ub=b, bounds=[(None, None)]*4, method='highs')


def certify(rows, res):
    y = -res.ineqlin.marginals
    yr = [Fr(v).limit_denominator(10**7) for v in y]
    comb = [sum(yr[i]*rows[i][0][j] for i in range(len(rows))) for j in range(4)]
    bound = -sum(yr[i]*rows[i][1] for i in range(len(rows)))
    ok = all(v >= 0 for v in yr) and comb[:3] == [0, 0, 0] and comb[3] == -1
    return ok, bound


def posterior(x, a0, thNC, dh):
    if not dh:
        return True
    lx, ly, ell, s = x
    h = 1 - lx + ell
    worst = -1.0
    for k in range(1, 834):
        dl = k/1000
        if dl <= float(2*a0 - 1):
            continue
        a = (1 + dl)/2
        R = max(1 - dl - float(thNC), (1 - dl)/2)
        G = a*(1 - ly) + h*(R + dl/2 - 1/6) - ell/2 + 0.5*dl*ell
        worst = max(worst, G - max(s, a))
    return worst <= 1e-9


def value(a0, thF, gram, energy, dh=True, thNC=Fr(0), lxly=True):
    rows = rows_for(a0, thF, gram, energy, dh, thNC, lxly)
    res = solve(rows)
    ok, bound = certify(rows, res)
    ok = ok and posterior(res.x, a0, thNC, dh)
    return res.fun, ok, bound, res.x[:3]


def fmt(v, ok, b):
    s = f"{v:.6f}"
    if ok and b.denominator < 10**5:
        s += f" (={b})"
    elif not ok:
        s += " (cert?)"
    return s


if __name__ == '__main__':
    TH = [Fr(0), Fr(1, 200), Fr(1, 100), Fr(1, 50), Fr(1, 20), Fr(1, 10), Fr(1, 6), Fr(1, 4), Fr(1, 3)]
    for gram in ('b12', 'zero'):
        for energy in ('paper', 'optimal'):
            print(f"=== gram = {gram}, energy = {energy} ===")
            for a0 in (Fr(51, 100), Fr(1, 2)):
                v, ok, b, g = value(a0, Fr(0), gram, energy, dh=False)
                print(f" a0={float(a0):.3f}  low+floor only (any counting, theta=0): {fmt(v, ok, b)} geom {np.round(g, 4)}")
                for th in TH:
                    v1, ok1, b1, g1 = value(a0, th, gram, energy, dh=True)
                    v2, ok2, b2, g2 = value(a0, th, gram, energy, dh=True, thNC=th)
                    print(f"  theta={float(th):.4f}  floor-only(+DH) {fmt(v1, ok1, b1):26s}"
                          f" floor+NC(+DH) {fmt(v2, ok2, b2):26s} geom {np.round(g2, 4)}")
