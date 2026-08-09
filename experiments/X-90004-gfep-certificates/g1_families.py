"""PRONG G1: (a) exhaustive binding-family classification; (b) margin regression vs
signed Mobius remainder; (c) renewal profile of harmonic pixels."""
import sys, math
import numpy as np
sys.path.insert(0, "/home/user/riemann/experiments/X-90002-stress-test-artifacts")
sys.path.insert(0, "/home/user/riemann/experiments/X-90004-gfep-certificates")
from gfep import mobius_sieve, critical_r
from smallX_band2 import full_G
from g1_scan import sigma_from_G, mob_coeffs
from g1_flow import pixel_H

MU_STEP = 0.5 * math.log(2) + (1/6) * math.log(3) + (1/3) * math.log(1.5)

def classify(X):
    mu = mobius_sieve(X); r = critical_r(X, mu); G = full_G(X, r)
    fam = {"bottom": 0, "top": 0, "interior_odd": 0, "interior_even": 0}
    worst_by_fam = {}
    rows = []
    for n in range(8, X // 10 + 1):
        p, sig = sigma_from_G(X, n, r, G)
        j = int(np.argmin(sig)); ps = int(p[j]); th = ps / n
        if ps == n: f = "bottom"
        elif ps == 2 * n - 1: f = "top"
        elif ps % 2 == 1: f = "interior_odd"
        else: f = "interior_even"
        fam[f] += 1
        v = float(sig[j]) * math.sqrt(n)
        rows.append((n, ps, th, v, f))
        if f not in worst_by_fam or v < worst_by_fam[f][0]:
            worst_by_fam[f] = (v, n, ps)
    print(f"X={X}: binding-family counts over n=8..{X//10}: {fam}")
    print(f"   worst per family: {worst_by_fam}")
    ths = [t for (_, _, t, _, f) in rows if f.startswith("interior")]
    if ths:
        print(f"   interior theta*: min={min(ths):.4f} max={max(ths):.4f} "
              f"mean={np.mean(ths):.4f}  (4/3={4/3:.4f})")
    return rows, mu, r, G

def regress(rows, X, mu):
    """sq ~ a(L+2) + b*Bform_K  for K = X/n and K = X/(2n)."""
    import numpy.linalg as la
    y = np.array([v for (_, _, _, v, _) in rows])
    L = np.array([math.log(X / n) for (n, _, _, _, _) in rows])
    for Kdiv in (1, 2):
        B = []
        for (n, _, _, _, _) in rows:
            K = max(1, X // (Kdiv * n))
            MK, AK, mK = mob_coeffs(K, mu)
            B.append((4 + math.log(X / n)) * MK - AK)
        B = np.array(B)
        A1 = np.column_stack([L + 2])
        A2 = np.column_stack([L + 2, B])
        for A, tag in ((A1, "a(L+2)"), (A2, f"a(L+2)+b*Bform[K=X/{Kdiv}n]")):
            coef, res_, *_ = la.lstsq(A, y, rcond=None)
            pred = A @ coef
            r2 = 1 - np.sum((y - pred) ** 2) / np.sum((y - y.mean()) ** 2)
            print(f"   fit {tag}: coef={np.round(coef,4)} R2={r2:.4f}")

def renewal_profile(X, n):
    """kappa_hat(p) = mean_{m in [X/2,X]} H_p(m)*p*MU_STEP; predict 1 on (4/3,2), 2/3 on (1,4/3)."""
    print(f"renewal profile X={X} n={n}: theta  kappa_hat  (pred: 2/3 below 4/3, 1 above)")
    ps = sorted(set([n, n + 1, n + 2] +
                    [int(n * t) for t in (1.1, 1.2, 1.25, 1.30, 1.32)] +
                    [int(n * 4 / 3), int(n * 4 / 3) + 1] +
                    [int(n * t) for t in (1.4, 1.5, 1.6, 1.75, 1.9)] + [2 * n - 2, 2 * n - 1]))
    for p in ps:
        if not (n <= p < 2 * n): continue
        H = pixel_H(X, n, p)
        seg = H[X // 2: X + 1]
        k = float(np.mean(seg)) * p * MU_STEP
        cv = float(np.std(seg) / np.mean(seg)) if np.mean(seg) > 0 else float("nan")
        print(f"   theta={p/n:.4f} p={p} ({'odd' if p%2 else 'even'}): kappa={k:.4f} cv={cv:.3f}")

if __name__ == "__main__":
    for X in (3000, 10**4):
        rows, mu, r, G = classify(X)
        regress(rows, X, mu)
    renewal_profile(10**4, 60)
