"""LP duality re-run (Theorem A) + five-parent identity + T-90005 certified minimum."""
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
from rev_final import Model, children

def run_lp(X, n):
    M = Model(X, n)
    E = M.E_table()
    Sig = M.sigma_backward(E)
    V = list(range(n, X+1)); F = list(range(2*n, X+1))
    iV = {m: i for i, m in enumerate(V)}
    nF = len(F); nV = len(V)
    # vars: y(m) m in F, then t.  max t  s.t. S + Q^T y - y 1_F >= t 1_W
    # As A_ub x <= b_ub:  y(m')1_F - (Q^T y)(m') + t 1_W <= S(m')
    A = lil_matrix((nV, nF+1))
    for j, m in enumerate(F):
        A[iV[m], j] += 1.0
        for c in children(m):
            if c >= n:
                A[iV[c], j] -= c/(2*m)
    for p in M.wp:
        A[iV[p], nF] = 1.0
    b = np.array([M.S[m] for m in V])
    cobj = np.zeros(nF+1); cobj[nF] = -1.0
    res = linprog(cobj, A_ub=A.tocsr(), b_ub=b,
                  bounds=[(None, None)]*(nF+1), method='highs')
    t_star = -res.fun
    duals = -res.ineqlin.marginals  # h >= 0
    pstar_i = int(np.argmin(Sig)); pstar = M.wp[pstar_i]
    # compare dual vector with pixel H_pstar on V
    Hp = np.array([E[m, pstar_i] for m in V])
    diff = np.max(np.abs(duals - Hp))
    wsupp = [p for p in M.wp if duals[iV[p]] > 1e-9]
    print(f"(X,n)=({X},{n}): t*={t_star:.15f} minSig={Sig.min():.15f} "
          f"|t*-minSig|={abs(t_star-Sig.min()):.2e} ||dual-H_p*||_inf={diff:.2e} "
          f"window support={wsupp} p*={pstar}")
    return M, E, Sig

for X, n in [(3000, 100), (3000, 149), (2000, 20)]:
    run_lp(X, n)

# five-parent bottom-pixel identity + certified minimum at (1960,196)
X, n = 1960, 196
M = Model(X, n)
E = M.E_table()
Sig = M.sigma_backward(E)
g, sink, leak = M.forward_g()
rhs = n*M.R[n] + 0.5*g[2*n] + g[2*n+1]*n/(2*(2*n+1)) \
      + sum(g[m]*n/(2*m) for m in (3*n, 3*n-1, 3*n-2) if m <= X)
print(f"five-parent identity at (1960,196): Sigma(n)={Sig[0]:.15f} rhs={rhs:.15f} diff={abs(Sig[0]-rhs):.2e}")
i391 = 391 - M.Wlo
print(f"sqrt(X)*Sigma(391) = {np.sqrt(X)*Sig[i391]:.6f}  (T-90005 certified 4.826247)")
print(f"argmin p = {M.wp[int(np.argmin(Sig))]}, sqrt(X)*min = {np.sqrt(X)*Sig.min():.6f}")

# also verify five-parent at (2000,20) and (3000,25)
for X, n in [(2000, 20), (3000, 25)]:
    M = Model(X, n); E = M.E_table(); Sig = M.sigma_backward(E)
    g, sink, leak = M.forward_g()
    rhs = n*M.R[n] + 0.5*g[2*n] + g[2*n+1]*n/(2*(2*n+1)) \
          + sum(g[m]*n/(2*m) for m in (3*n, 3*n-1, 3*n-2) if m <= X)
    print(f"five-parent at ({X},{n}): diff={abs(Sig[0]-rhs):.2e}")
