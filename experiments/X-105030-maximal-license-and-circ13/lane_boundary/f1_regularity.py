#!/usr/bin/env python3
"""L-105032 verification: F_1(s) bounded as s -> 1/2+ (moving-boundary pole
cancellation), vs the fixed-cut blow-up of R-105024. Sieve to 10^7."""
import numpy as np
N = 10**7
P = []
smallest = np.zeros(N+1, dtype=np.int64)
mu_arr = np.ones(N+1, dtype=np.int8)
is_comp = np.zeros(N+1, dtype=bool)
for i in range(2, N+1):
    if not is_comp[i]:
        P.append(i); smallest[i] = i; mu_arr[i] = -1
    for p in P:
        if p*i > N or p > smallest[i]: break
        is_comp[p*i] = True; smallest[p*i] = p
        mu_arr[p*i] = 0 if i % p == 0 else -mu_arr[i]
P = np.array(P)
mu_f = mu_arr.astype(np.float64)
A_prefix = np.concatenate([[0.0], np.cumsum(mu_f[1:]/np.arange(1, N+1))])
B_prefix = np.concatenate([[0.0], np.cumsum(mu_f[1:]/np.sqrt(np.arange(1, N+1)))])
Ap, Bp = A_prefix[P-1], B_prefix[P-1]
kappa1 = float(np.sum(Ap/P))
assert abs(kappa1 - 0.7372232414) < 1e-9, kappa1
vals, cs = [], []
for s in [0.6, 0.55, 0.52, 0.51, 0.505]:
    z = s + 0.5
    D1 = -np.sum(P**(-z)*Ap); S2 = np.sum(P**(-2.0*s)*Ap)
    iii = 3.0/s*np.sum(P**(-2.0*s-0.5)*Bp)
    K = (s+1.5)/(s*(s-0.5))
    F1 = K*D1 + 4.0/(s-0.5)*S2 + iii
    c = (s+1.5)/s*D1 + 4.0*S2
    vals.append(F1); cs.append(c)
    print(f"s={s}: F1={F1:.6f} c={c:+.6f}")
# assertions: boundedness + pole-coefficient decay + expected values
exp_vals = [2.470837, 2.894101, 3.176587, 3.275089, 3.325066]
for v, e in zip(vals, exp_vals): assert abs(v-e) < 1e-4, (v, e)
assert all(abs(cs[i]) > abs(cs[i+1]) for i in range(len(cs)-1))
assert max(vals) < 4.0  # bounded well below the fixed-cut blow-up scale
print("ALL F1 REGULARITY CHECKS PASSED  (kappa1 = %.10f)" % kappa1)
