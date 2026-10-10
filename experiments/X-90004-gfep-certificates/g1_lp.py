"""PRONG G1 step 2/4: solve the actual flow LP, extract optimal dual potentials.
Primal (P_n):  max t  s.t.  S(m') + (Q^T y)(m') - y(m')1_{m'>=2n} >= t (m' in W), >= 0 (m'>=2n),
y in R^{[2n,X]} free.  Predicted: t* = min_p Sigma(p); optimal dual = harmonic pixel H_{p*}."""
import sys, math
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
sys.path.insert(0, "/home/user/riemann/experiments/X-90002-stress-test-artifacts")
from gfep import mobius_sieve, critical_r
from g1_flow import children, sigma_all, pixel_H

def solve_lp(X, n):
    mu = mobius_sieve(X); r = critical_r(X, mu)
    S = np.zeros(X + 2); mm = np.arange(2, X + 1); S[2:X + 1] = mm * r[2:X + 1]
    up = min(2 * n, X + 1)
    rows = list(range(n, X + 1))          # constraint rows m' in [n,X]
    ridx = {m: i for i, m in enumerate(rows)}
    ys = list(range(2 * n, X + 1))        # y variables
    yidx = {m: j for j, m in enumerate(ys)}
    nv = len(ys) + 1                       # + t
    A = lil_matrix((len(rows), nv))
    b = np.zeros(len(rows))
    # row m': -S - Q^T y + y*1_{>=2n} + t*1_W <= 0
    for m in ys:
        j = yidx[m]
        A[ridx[m], j] += 1.0
        for c in children(m):
            if c >= n:
                A[ridx[c], j] -= c / (2.0 * m)
    for m in rows:
        b[ridx[m]] = S[m]
        if m < up:
            A[ridx[m], nv - 1] = 1.0
    c_obj = np.zeros(nv); c_obj[-1] = -1.0   # maximize t
    res = linprog(c_obj, A_ub=A.tocsr(), b_ub=b,
                  bounds=[(None, None)] * nv, method="highs")
    assert res.status == 0, res.message
    t_star = -res.fun
    lam = -res.ineqlin.marginals             # dual vars >= 0 for our >= form
    sig = sigma_all(X, n, S)
    j0 = int(np.argmin(sig)); p_star = n + j0
    # compare dual vector with harmonic pixel H_{p*}
    H = pixel_H(X, n, p_star)
    dual = np.array([lam[ridx[m]] for m in rows])
    Hvec = H[n:X + 1]
    # window part of dual: support
    wdual = dual[:up - n]
    supp = [n + i for i, v in enumerate(wdual) if v > 1e-9]
    err = float(np.max(np.abs(dual - Hvec)))
    print(f"X={X} n={n}: LP t*={t_star:.10e}  min_p Sigma={sig[j0]:.10e}  "
          f"match={abs(t_star - sig[j0]):.1e}")
    print(f"   argmin pixel p*={p_star} (=2n-1? {p_star == 2*n-1}; theta*={p_star/n:.4f}); "
          f"dual window support={supp}")
    print(f"   ||dual - H_p*||_inf = {err:.2e}  (harmonic-pixel collapse)")
    return t_star, p_star, dual, Hvec

if __name__ == "__main__":
    for (X, n) in [(3000, 100), (3000, 149), (3000, 271)]:
        solve_lp(X, n)
