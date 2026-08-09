"""PRONG G1 step 3-4: binding-pixel structure across scales + scaling-law fits.
Uses T-90003 last-far-state decomposition: G(m) n-independent above 2n."""
import sys, math
import numpy as np
sys.path.insert(0, "/home/user/riemann/experiments/X-90002-stress-test-artifacts")
sys.path.insert(0, "/home/user/riemann/experiments/X-90004-gfep-certificates")
from gfep import mobius_sieve, critical_r
from smallX_band2 import full_G

def sigma_from_G(X, n, r, G):
    """Full Sigma_{X,n}(.) via parent inventory (audited in T-90005)."""
    up = min(2 * n, X + 1)
    p = np.arange(n, up)
    sig = p * r[n:up]
    def add(mpar, w, pres=None):
        msk = (mpar >= 2 * n) & (mpar <= X)
        if pres is not None: msk &= pres
        sig[msk] += G[mpar[msk]] * w[msk]
    add(2 * p, np.full(len(p), 0.5))
    add(2 * p + 1, p / (2.0 * (2 * p + 1)))
    add(2 * p - 1, p / (2.0 * (2 * p - 1)))
    for j in (0, 1, 2):
        add(3 * p - j, p / (2.0 * (3 * p - j)))
    bA = (3 * p + 1) // 2
    add(bA, p / (2.0 * bA))
    bB = 3 * (p // 2) + 1
    add(bB, p / (2.0 * bB), pres=(p % 2 == 0))
    return p, sig

def mob_coeffs(K, mu):
    ks = np.arange(1, K + 1)
    MK = float(np.sum(mu[1:K + 1] / np.sqrt(ks)))
    AK = float(np.sum(mu[1:K + 1] * np.log(ks) / np.sqrt(ks)))
    mK = float(np.sum(mu[1:K + 1] / ks))
    return MK, AK, mK

def scan(X, nlist):
    mu = mobius_sieve(X); r = critical_r(X, mu); G = full_G(X, r)
    rows = []
    for n in nlist:
        p, sig = sigma_from_G(X, n, r, G)
        j = int(np.argmin(sig))
        L = math.log(X / n)
        K = X // n
        MK, AK, mK = mob_coeffs(K, mu)
        rows.append(dict(X=X, n=n, pstar=int(p[j]), theta=p[j] / n,
                         minsig=float(sig[j]), sq=float(sig[j]) * math.sqrt(n),
                         L=L, ratio=float(sig[j]) * math.sqrt(n) / (L + 2),
                         MK=MK, AK=AK, mK=mK,
                         Bform=(4 + L) * MK - AK))
    return rows

if __name__ == "__main__":
    out = []
    for X in (3000, 10**4, 10**5):
        top = X // 10
        ns = sorted(set(int(round(8 * 1.25**k)) for k in range(200) if 8 * 1.25**k <= top))
        out += scan(X, ns)
    print(f"{'X':>6} {'n':>6} {'p*':>6} {'theta*':>7} {'sq=minSig*sqrt(n)':>18} "
          f"{'sq/(L+2)':>9} {'M_K':>7} {'|Bform|':>8} {'sq/|Bform|':>10}")
    for d in out:
        print(f"{d['X']:>6} {d['n']:>6} {d['pstar']:>6} {d['theta']:>7.4f} "
              f"{d['sq']:>18.5f} {d['ratio']:>9.4f} {d['MK']:>7.3f} "
              f"{abs(d['Bform']):>8.3f} {d['sq']/abs(d['Bform']) if d['Bform'] else float('nan'):>10.4f}")
    np.save("scan_rows.npy", out, allow_pickle=True)
