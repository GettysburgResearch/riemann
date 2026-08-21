#!/usr/bin/env python3
"""Vectorized exact greedy margins via Q prefix sums:
Q_Y(j) = log(Y)*Pg_j(floor(Y)) - Lg_j(floor(Y)),
Pg_j(M) = sum_{m<=M} gamma_j(m)/sqrt(m), Lg_j(M) = sum gamma_j(m)log(m)/sqrt(m)."""
import numpy as np
from math import sqrt, log

def sieve_mu_np(N):
    mu = np.ones(N+1, dtype=np.int8); mu[0] = 0
    primes = []
    is_comp = np.zeros(N+1, dtype=bool)
    for i in range(2, N+1):
        if not is_comp[i]:
            primes.append(i); mu[i] = -1
        for p in primes:
            if i*p > N: break
            is_comp[i*p] = True
            if i % p == 0:
                mu[i*p] = 0; break
            else:
                mu[i*p] = -mu[i]
    return mu

def gamma_arrays(N, js=(2,3)):
    m = np.arange(N+1, dtype=np.float64); m[0] = 1.0
    invs = 1.0/np.sqrt(m); lg = np.log(m)
    out = {}
    for j in js:
        g = np.full(N+1, 2.0/(j*(j-1))); g[:j] = 0.0
        g[j] = (j+1)/(j-1); g[j+1] = -((j+1)*(j-2))/(j*(j-1))
        Pg = np.cumsum(g*invs); Lg = np.cumsum(g*invs*lg)
        out[j] = (Pg, Lg)
    return out

def greedy_fast(x, mu, ga, js=(2,3)):
    n = int(np.floor(x))
    ks = np.nonzero(mu[1:n+1])[0] + 1
    sg = mu[ks].astype(np.float64)
    Y = x/ks
    sqY = np.sqrt(Y)
    den = 4*sqY - 3
    T = den/np.sqrt(ks)
    s = (5*sqY - 3)/den
    M = np.floor(Y).astype(np.int64)
    lgY = np.log(Y)
    rho = {}
    for j in js:
        Pg, Lg = ga[j]
        Qv = lgY*Pg[M] - Lg[M]
        rho[j] = Qv/den
    ev = sg > 0; od = ~ev
    Te, Ts = T[ev], T[od]
    D = Ts.sum(); TB = Te.sum() - D
    if TB < 0:
        return dict(x=x, TB=TB, feasible=False, why="total balance", D=D)
    cum = np.cumsum(Te)
    idx = int(np.searchsorted(cum, D))
    c = Te.copy()
    if idx < len(c):
        c[idx] = D - (cum[idx-1] if idx > 0 else 0.0)
        c[idx+1:] = 0.0
    res = dict(x=x, TB=TB, D=D, nE=int(ev.sum()), nO=int(od.sum()),
               estar=int(ks[ev][idx]) if idx < len(c) else int(ks[ev][-1]))
    feas = True
    for j in js:
        K = (Ts*rho[j][od]).sum()
        mrow = (c*rho[j][ev]).sum() - K
        G = (Te*rho[j][ev]).sum() - K
        res[f"m{j}"] = mrow; res[f"G{j}"] = G
        feas &= (mrow >= 0)
    Ksc = (Ts*s[od]).sum()
    msc = Ksc - (c*s[ev]).sum()
    res["m_sc"] = msc; feas &= (msc >= 0)
    res["feasible"] = feas
    res["TB_S"] = float((sg*T*s).sum())   # sum mu S = full signed score mass
    return res

if __name__ == "__main__":
    import core
    mu = sieve_mu_np(1200)
    ga = gamma_arrays(1200)
    muc, _ = core.sieve_mu(1200)
    for x in (88.0, 100.999999, 400.999999, 1008.999999):
        a = greedy_fast(x, mu, ga)
        b = core.greedy_margins(x, muc)
        print(f"x={x:<12.6f} fast: m2={a['m2']:.9f} m3={a['m3']:.9f} m_sc={a['m_sc']:.9f} TB={a['TB']:.9f}")
        print(f"{'':13s} core: m2={b['m2']:.9f} m3={b['m3']:.9f} m_sc={b['m_sc']:.9f} TB={b['TB']:.9f}")
