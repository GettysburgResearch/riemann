#!/usr/bin/env python3
"""(1) higher rows j=4..8: greedy margins at sample fibres (same c*).
(2) 61-smooth frozen-support variant: greedy feasibility at sample fibres + TB_smooth scan."""
import numpy as np
from fast import sieve_mu_np, gamma_arrays

N = 1_000_000
mu = sieve_mu_np(N)

# smooth flag: divide out primes <= 61; smooth iff residue becomes 1
primes61 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
tmp = np.arange(N+1)
tmp[0] = 1
for p in primes61:
    for _ in range(30):
        mask = (tmp % p == 0) & (tmp > 1)
        if not mask.any(): break
        tmp[mask] //= p
smooth = tmp == 1
smooth[0] = False

def greedy_gen(x, mu, ga, js, support=None):
    n = int(np.floor(x))
    ks = np.nonzero(mu[1:n+1])[0] + 1
    if support is not None:
        ks = ks[support[ks]]
    sg = mu[ks].astype(np.float64)
    Y = x/ks; sqY = np.sqrt(Y); den = 4*sqY - 3
    T = den/np.sqrt(ks); s = (5*sqY-3)/den
    M = np.floor(Y).astype(np.int64); lgY = np.log(Y)
    ev = sg > 0; od = ~ev
    Te, Ts = T[ev], T[od]
    D = Ts.sum(); TB = Te.sum() - D
    out = dict(TB=TB, feasible=TB >= 0)
    if TB < 0: return out
    cum = np.cumsum(Te); idx = int(np.searchsorted(cum, D))
    c = Te.copy()
    if idx < len(c):
        c[idx] = D - (cum[idx-1] if idx > 0 else 0.0); c[idx+1:] = 0.0
    for j in js:
        Pg, Lg = ga[j]
        rho = (lgY*Pg[M] - Lg[M])/den
        mrow = float((c*rho[ev]).sum() - (Ts*rho[od]).sum())
        out[f"m{j}"] = mrow
        out["feasible"] &= mrow >= 0
    msc = float((Ts*s[od]).sum() - (c*s[ev]).sum())
    out["m_sc"] = msc; out["feasible"] &= msc >= 0
    return out

js = (2,3,4,5,6,8)
ga = gamma_arrays(N, js=js)
print("== (1) higher rows, full support ==")
for x in (88.0, 1009.0-1e-6, 10007.0-1e-6, 100003.0, 999999.0):
    r = greedy_gen(x, mu, ga, js)
    print(f"x={x:>10.1f}: TB={r['TB']:.4f} " +
          " ".join(f"m{j}={r[f'm{j}']:+.4f}" for j in js) +
          f" m_sc={r['m_sc']:.4f} feas={r['feasible']}")

print("\n== (2) 61-smooth frozen support ==")
for x in (88.0, 1009.0-1e-6, 10007.0-1e-6, 100003.0, 999999.0):
    r = greedy_gen(x, mu, ga, (2,3), support=smooth)
    print(f"x={x:>10.1f}: TB={r['TB']:.4f} m2={r['m2']:+.4f} m3={r['m3']:+.4f} "
          f"m_sc={r['m_sc']:.4f} feas={r['feasible']}")

# smooth TB scan over all x (prefix arrays)
n = np.arange(N+1, dtype=np.float64); n[0] = 1.0
muf = mu.astype(np.float64)
sm = smooth & (mu != 0)
As = np.cumsum(np.where(sm, muf/n, 0.0)); Bs = np.cumsum(np.where(sm, muf/np.sqrt(n), 0.0))
x = np.arange(2, N+1); xd = x.astype(np.float64)
TBs = 4*np.sqrt(xd)*As[x] - 3*Bs[x]
i = int(np.argmin(TBs))
print(f"smooth TB: min over [2,1e6] = {TBs[i]:.6f} at x={x[i]}; negatives = {(TBs<0).sum()}")
# smooth-variant full-fibre sweep to 10007
ga2 = gamma_arrays(10008, js=(2,3))
bad = []
mins = {k: (1e18, None) for k in ("m2","m3","m_sc","TB")}
for xi in range(2, 10008):
    r = greedy_gen(float(xi), mu, ga2, (2,3), support=smooth)
    if not r["feasible"]: bad.append(xi)
    for k in mins:
        if k in r and r[k] < mins[k][0]: mins[k] = (r[k], xi)
print(f"smooth-variant sweep [2,10007]: infeasible fibres = {len(bad)} {bad[:5]}")
for k in mins: print(f"   min {k} = {mins[k][0]:.6f} at x={mins[k][1]}")
