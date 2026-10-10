import numpy as np
from sympy import mobius

def build_C(T):
    """C = (B_T^T)^{-1} via the proved row formula (fast, exact structure)."""
    idx = np.arange(2, T + 1)
    m = len(idx)
    mu = np.array([int(mobius(k)) for k in range(1, T + 1)])
    C = np.zeros((m, m))
    for jj, j in enumerate(idx):
        # c_j(n) = sum_{e|n, e>=2} A(j,e) mu(n/e);  A: j -> (j+1)/(j-1); j+1 -> that -2(j+1)/j; >=j+2 -> +1 more
        a_j   = (j + 1) / (j - 1)
        a_j1  = a_j - 2 * (j + 1) / j
        a_tail = a_j1 + 1.0          # = 2/(j(j-1))
        for nn in range(jj, m):
            n = idx[nn]
            s = 0.0
            e = j
            # divisors e of n with e >= j
            for e in range(j, n + 1):
                if n % e == 0:
                    if e == j: a = a_j
                    elif e == j + 1: a = a_j1
                    else: a = a_tail
                    s += a * mu[n // e - 1]
            C[jj, nn] = s
    return C, idx

def stats(T):
    C, idx = build_C(T)
    m = len(idx)
    n = idx.astype(float)
    out = {}
    # symmetry defect of raw C and of scaled congruences D C D'
    def defect(M):
        return np.linalg.norm(M - M.T) / np.linalg.norm(M)
    out['defect_raw'] = defect(C)
    scalings = {'n^{3/4} both': (n**0.75, n**0.75),
                'n^{3/4},n^{-3/4}': (n**0.75, n**-0.75),
                'n^{-3/4} both': (n**-0.75, n**-0.75)}
    for name, (dl, dr) in scalings.items():
        M = dl[:, None] * C * dr[None, :]
        out['defect ' + name] = defect(M)
        Sym = 0.5 * (M + M.T)
        ev = np.linalg.eigvalsh(Sym)
        out['symEV ' + name] = (ev[0], ev[1], ev[2], ev[-1], int((ev < 0).sum()))
    # eigenvalues of C itself (triangular -> diagonal)
    out['eig_diag_check'] = np.allclose(np.sort(np.diag(C)), np.sort((n + 1) / (n - 1)))
    # singular values of raw C
    sv = np.linalg.svd(C, compute_uv=False)
    out['sv_max'] = sv[0]; out['sv_min'] = sv[-1]
    out['sv_small5'] = sv[-5:]
    out['sv_big5'] = sv[:5]
    # best diagonal similarity symmetrizer (impossible in principle; optimize log-scale greedily)
    # defect for D C D^{-1}, D=n^a, sweep a
    best = (1e9, None)
    for a in np.linspace(-3, 3, 61):
        M = (n**a)[:, None] * C * (n**-a)[None, :]
        d = defect(M)
        if d < best[0]: best = (d, a)
    out['best_similarity_defect(a)'] = best
    # symmetric part of raw C: PD?
    Sym = 0.5 * (C + C.T)
    ev = np.linalg.eigvalsh(Sym)
    out['symC ev min/max, #neg'] = (ev[0], ev[-1], int((ev < 0).sum()))
    # condition number of C
    out['cond_C'] = sv[0] / sv[-1]
    return out, sv, C

for T in [200, 500, 1000, 2000]:
    out, sv, C = stats(T)
    print("==== T =", T)
    for k, v in out.items():
        print("  ", k, "=", v)
    np.save(f"sv_{T}.npy", sv)
