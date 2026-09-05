#!/usr/bin/env python3
"""Direct LP over t(o,e) >= 0 on ALL pairs; maximize m with
B_2>=m, B_3>=m, -score>=m, demand equality, capacity.
Cross-check against greedy reduction margins: expect m* = min(m2,m3,m_sc)."""
import sys
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix, csr_matrix
from core import sieve_mu, fibre, profiles, greedy_margins

def lp_margin(x, mu):
    ks, E, O, T = fibre(x, mu)
    rho, s = profiles(x, ks)
    nO, nE = len(O), len(E)
    nv = nO*nE + 1   # t(o,e) dense pairs + margin m
    # demand equality rows (nO), capacity rows (nE), 3 aggregate rows
    Aeq = lil_matrix((nO, nv)); Aub = lil_matrix((nE+3, nv))
    beq = np.array([T[o] for o in O]); bub = np.zeros(nE+3)
    bub[:nE] = [T[e] for e in E]
    for oi, o in enumerate(O):
        for ei, e in enumerate(E):
            jv = oi*nE + ei
            Aeq[oi, jv] = 1.0
    # fill capacity + aggregates
    for oi, o in enumerate(O):
        for ei, e in enumerate(E):
            jv = oi*nE + ei
            Aub[ei, jv] = 1.0
            Aub[nE+0, jv] = -(rho[2][e]-rho[2][o])   # -B2 <= -m  -> -B2 + m <= 0
            Aub[nE+1, jv] = -(rho[3][e]-rho[3][o])
            Aub[nE+2, jv] = (s[e]-s[o])              # score + m <= 0
    Aub[nE+0, nv-1] = 1.0
    Aub[nE+1, nv-1] = 1.0
    Aub[nE+2, nv-1] = 1.0
    c = np.zeros(nv); c[nv-1] = -1.0  # maximize m
    res = linprog(c, A_eq=csr_matrix(Aeq), b_eq=beq, A_ub=csr_matrix(Aub), b_ub=bub,
                  bounds=[(0, None)]*(nv-1) + [(None, None)], method='highs')
    return res

if __name__ == "__main__":
    mu, _ = sieve_mu(1200)
    eps = 1e-6
    tests = [88.0, 89.0-eps, 101.0-eps, 149.0-eps, 211.0-eps, 401.0-eps]
    if len(sys.argv) > 1 and sys.argv[1] == "big":
        tests = [1009.0-eps]
    for x in tests:
        g = greedy_margins(x, mu)
        pred = min(g['m2'], g['m3'], g['m_sc'])
        res = lp_margin(x, mu)
        mstar = -res.fun if res.status == 0 else None
        print(f"x={x:<12.6f} LP status={res.status} m*={mstar!s:>14} "
              f"greedy pred={pred:.9f} m2={g['m2']:.6f} m3={g['m3']:.6f} m_sc={g['m_sc']:.6f} TB={g['TB']:.6f}")
        if mstar is not None:
            print(f"   |m* - pred| = {abs(mstar-pred):.3e}")
