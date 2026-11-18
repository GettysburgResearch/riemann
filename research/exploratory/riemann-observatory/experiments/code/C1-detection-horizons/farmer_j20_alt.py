#!/usr/bin/env python3
"""C1: test the hypothesis that Farmer's X_20 moved the cos zeros 9pi/2 and 11pi/2 (14.14, 17.28) rather than
11pi/2 and 13pi/2 (17.28, 20.42): Farmer's row '# first zeros of X_j are real' = 4 for j=20 is consistent only with
the former. Computes (i) heat-flow prediction 1/(2 tau_c); (ii) Arb root isolation of J^{d,0} near the threshold."""
import sys, math, json, time
import numpy as np, mpmath as mp, flint
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import common
src = open(__file__.rsplit('/', 1)[0] + '/exp_dbn_jensen.py').read()
ns = {'__file__': __file__}
exec(src.split('# ---------------- Part A')[0], ns)          # imports, collapse()
partB = src.split('# ---------------- Part B: Farmer')[1].split('# sanity check')[0]
exec('import mpmath as _mp\n' + partB.split('\n', 1)[1], ns)
collapse_w_full, cos_tails = ns['collapse_w_full'], ns['cos_tails']

def tau_for(j, moved, Mz=400):
    c = (np.arange(Mz) + 0.5) * math.pi
    keep = np.setdiff1d(np.arange(Mz), moved)
    w = np.log(c[keep])
    wpair = complex(math.log(abs(complex(j, 1))), math.atan2(1, j))
    return collapse_w_full(w, w.copy(), wpair, tail2=cos_tails(Mz))

def taylor_general(j, moved_vals, K, dps=500):
    mp.mp.dps = dps
    a, b = [mp.mpf(v) for v in moved_vals]
    A = (a**2 + b**2) - 2 * (j**2 - 1); B = (j**2 + 1)**2 - a**2 * b**2
    C1 = (A * a**2 + B) / (a**2 - b**2); C2 = (A * b**2 + B) / (b**2 - a**2)
    def gcoef(n, r):
        s = mp.mpf(0); l = n + 1; term = (-1)**l * r**(2 * l) / mp.factorial(2 * l)
        while True:
            s += term
            if l > r and abs(term) < mp.mpf(10)**(-dps + 5) * abs(s): break
            l += 1; term = term * (-1) * r**2 / ((2 * l) * (2 * l - 1))
        return s / r**(2 * n + 2)
    return [((-1)**n / mp.factorial(2 * n) + C1 * gcoef(n, a) + C2 * gcoef(n, b)) * mp.factorial(2 * n) for n in range(K // 2 + 1)]

def certify(alpha, d, S=450):
    mp.mp.dps = 500
    co = [int(mp.nint(mp.binomial(d, 2 * n) * alpha[n] * mp.mpf(10)**S)) for n in range(d // 2 + 1)]
    roots = flint.fmpz_poly(co).complex_roots()
    nonreal = [r for r, m in roots if not r.imag.contains(0)]
    neg = [r for r, m in roots if r.imag.contains(0) and r.real < 0]
    return len(nonreal), len(neg)

out = {}
c = (np.arange(10) + 0.5) * math.pi
for label, moved in {"A: moved 11pi/2,13pi/2 (17.28,20.42) [closest to 20]": [5, 6], "B: moved 9pi/2,11pi/2 (14.14,17.28)": [4, 5]}.items():
    t1 = time.time()
    tau = tau_for(20, moved)
    alpha = taylor_general(20, [c[moved[0]], c[moved[1]]], 900)
    pred = 1 / (2 * tau)
    cert = {}
    for d in sorted(set([int(pred) - 3, int(pred) - 1, int(pred) + 1, int(pred) + 3, 749, 750, 760])):
        nr, ng = certify(alpha, d)
        cert[d] = {"certified_nonreal_roots_of_R": nr, "negative_real_roots_of_R": ng, "J_real_rooted": nr == 0 and ng == 0}
    out[label] = {"tau_c": tau, "pred_first_nonreal_d": pred, "certify": cert, "sec": round(time.time() - t1, 1)}
    print(label, out[label], flush=True)
p = common.save_json("farmer_j20_alt.json", {"env": common.env(), "result": out})
print("saved", p, common.sha256(p))
