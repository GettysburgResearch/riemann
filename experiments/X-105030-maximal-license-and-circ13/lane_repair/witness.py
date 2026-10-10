#!/usr/bin/env python3
"""(a) largest x <= 10007 with |m_j - G_j| > 1e-9  (sliver-touch horizon);
    binding-constraint identification.
(b) Task 2: canonical NW-corner witness realizing greedy c* at x=88 and x=10006.999999:
    anti-monotone edge list, debt mass, row/score debt vs nested bonus.
(c) LP vertex structure at x=88 (which edges carry flow at the max-min optimum)."""
import numpy as np
from math import sqrt, log
from fast import sieve_mu_np, gamma_arrays, greedy_fast
from core import sieve_mu, fibre, profiles
from lp_check import lp_margin

mu = sieve_mu_np(10008)
ga = gamma_arrays(10008)

print("== (a) done earlier: sliver-touch horizon = 46; binding census {'m3': 33, 'm_sc': 9972} ==")

def nw_witness(x, mu, ga):
    """NW-corner coupling of odds (ascending) to greedy capacities c* (evens ascending).
    Returns decomposition stats + explicit anti-monotone edges."""
    n = int(np.floor(x))
    ks = np.nonzero(mu[1:n+1])[0] + 1
    sg = mu[ks]
    Y = x/ks; sqY = np.sqrt(Y); den = 4*sqY - 3
    T = den/np.sqrt(ks); s = (5*sqY-3)/den
    M = np.floor(Y).astype(np.int64); lgY = np.log(Y)
    rho = {}
    for j in (2,3):
        Pg, Lg = ga[j]
        rho[j] = (lgY*Pg[M] - Lg[M])/den
    evm = sg > 0
    Ek = ks[evm]; Ok = ks[~evm]
    Te = T[evm]; To = T[~evm]
    D = To.sum()
    # greedy fill
    cum = np.cumsum(Te); idx = int(np.searchsorted(cum, D))
    c = Te.copy()
    if idx < len(c):
        c[idx] = D - (cum[idx-1] if idx > 0 else 0.0); c[idx+1:] = 0.0
    # NW-corner: walk odds and evens in ascending k order
    rho2 = {k: rho[2][i] for i, k in enumerate(ks)}
    rho3 = {k: rho[3][i] for i, k in enumerate(ks)}
    sv = {k: s[i] for i, k in enumerate(ks)}
    oi = ei = 0
    do = To[0]; ce = c[0]
    tol = 1e-12*max(1.0, D)
    nested_mass = anti_mass = 0.0
    bonus2 = bonus3 = debt2 = debt3 = sc_credit = sc_debt = 0.0
    anti_edges = []
    while oi < len(Ok):
        f = min(do, ce)
        if f > tol:
            o, e = int(Ok[oi]), int(Ek[ei])
            d2 = rho2[e]-rho2[o]; d3 = rho3[e]-rho3[o]; ds = sv[e]-sv[o]
            if e <= o:
                nested_mass += f; bonus2 += f*d2; bonus3 += f*d3; sc_credit += -f*ds
            else:
                anti_mass += f; debt2 += -f*d2; debt3 += -f*d3; sc_debt += f*ds
                anti_edges.append((o, e, f))
        do -= f; ce -= f
        if do <= tol:
            oi += 1
            if oi < len(Ok): do = To[oi]
            continue
        if ce <= tol:
            if ei < len(c)-1:
                ei += 1; ce = c[ei]
            else:
                break  # roundoff exhaustion
    return dict(D=D, nested=nested_mass, anti=anti_mass, edges=anti_edges,
                bonus2=bonus2, debt2=debt2, bonus3=bonus3, debt3=debt3,
                B2=bonus2-debt2, B3=bonus3-debt3,
                sc_credit=sc_credit, sc_debt=sc_debt, score=-(sc_credit-sc_debt))

print("\n== (b) canonical NW witness ==")
for x in (88.0, 10006.999999):
    w = nw_witness(x, mu, ga)
    g = greedy_fast(x, mu, ga)
    print(f"x={x}: demand D={w['D']:.4f}; nested mass={w['nested']:.4f}; "
          f"ANTI-MONOTONE mass={w['anti']:.6f} ({100*w['anti']/w['D']:.2f}% of demand)")
    print(f"   row2: bonus={w['bonus2']:.6f} debt={w['debt2']:.6f} net={w['B2']:.6f} (greedy m2={g['m2']:.6f})")
    print(f"   row3: bonus={w['bonus3']:.6f} debt={w['debt3']:.6f} net={w['B3']:.6f} (greedy m3={g['m3']:.6f})")
    print(f"   score: credit={w['sc_credit']:.6f} debt={w['sc_debt']:.6f} "
          f"edge term={w['score']:.6f} (= -m_sc + sliver: greedy m_sc={g['m_sc']:.6f})")
    agg = {}
    for o, e, f in w['edges']:
        agg[(o, e)] = agg.get((o, e), 0.0) + f
    top = sorted(agg.items(), key=lambda t: -t[1])[:14]
    print(f"   anti-monotone edges (top by mass): " +
          ", ".join(f"{o}->{e}:{f:.4f}" for (o, e), f in top))
    spans = sorted(set((o, e) for (o, e) in agg))
    print(f"   #anti edges={len(agg)}; max span e/o = {max(e/o for o,e in agg):.3f}")

print("\n== (c) LP vertex structure at x=88 ==")
muc, _ = sieve_mu(1200)
res = lp_margin(88.0, muc)
ks, E, O, T = fibre(88.0, muc)
t = res.x[:-1].reshape(len(O), len(E))
nz = [(O[oi], E[ei], t[oi, ei]) for oi in range(len(O)) for ei in range(len(E)) if t[oi, ei] > 1e-9]
anti = [(o, e, f) for o, e, f in nz if e > o]
nested = [(o, e, f) for o, e, f in nz if e <= o]
print(f"m* = {-res.fun:.9f}; active edges: {len(nz)} of {len(O)*len(E)}; "
      f"nested={len(nested)} anti={len(anti)}")
print("anti-monotone edges at LP optimum:", [(o, e, round(f, 4)) for o, e, f in sorted(anti, key=lambda z: -z[2])[:12]])
am = sum(f for _, _, f in anti)
print(f"anti mass at LP optimum = {am:.6f}")
