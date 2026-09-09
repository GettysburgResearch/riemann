"""Extend the monic-sieve normal form (T-108513 converse) to m = 16, 17:
exact factorization of disc_z M_m(a,1) — the converse holds at level m
iff the monic factors are exactly the torsion minimal polynomials with
threshold <= m and the remaining factor has non-unit leading
coefficient. Writes matrix/disc_slice_m18.json.
rh_established = false.
"""
import sys, json, time
sys.path.insert(0, '.')
import sympy as sp

a, z = sp.symbols('a z')

def q_seq(n):
    q = [sp.Integer(2), a]
    for j in range(2, n + 1):
        q.append(sp.expand(a * q[-1] - q[-2]))
    return q

def defect_numerator_b1(m):
    dim = m + 1
    q = q_seq(m * (dim + 1) + 1)
    ps = []
    for j in range(1, dim + 1):
        s = sp.Integer(0)
        i = 0
        while 2 * i < m:
            s += q[(m - 2 * i) * j]
            i += 1
        if m % 2 == 0:
            s += 1
        ps.append(sp.expand(s))
    e = [sp.Integer(1)]
    for k in range(1, dim + 1):
        s = sp.Integer(0)
        for i in range(1, k + 1):
            s += (-1) ** (i - 1) * e[k - i] * ps[i - 1]
        e.append(sp.expand(s / k))
    h = [sp.Integer(1), a]
    for k in range(2, m + 5):
        h.append(sp.expand(a * h[-1] - h[-2]))
    hm = [sp.expand(v ** m) for v in h]
    def c(r):
        s = sp.Integer(0)
        for u in range(r + 1):
            if r - u <= dim:
                s += (-1) ** (r - u) * e[r - u] * hm[u]
        return sp.expand(s)
    N = [c(r) for r in range(m)]
    for r in range(m, m + 3):
        assert c(r) == 0
    return N

def spectrum_b1(N, m):
    eps = 1 if m % 2 == 0 else 0
    nu = (m - 1 - eps) // 2
    if eps:
        quo = [sp.Integer(0)] * (len(N) - 1)
        rem = list(N)
        for i in range(len(N) - 2, -1, -1):
            quo[i] = rem[i + 1]
            rem[i] = sp.expand(rem[i] - quo[i])
            rem[i + 1] = sp.Integer(0)
        assert sp.expand(rem[0]) == 0
        N = quo
    mus = [sp.Integer(0)] * (nu + 1)
    work = list(N)
    for j in range(nu, -1, -1):
        mu = work[nu + j]
        mus[j] = mu
        for i in range(j + 1):
            work[nu + 2 * i - j] = sp.expand(work[nu + 2 * i - j]
                                             - mu * sp.binomial(j, i))
    assert all(sp.expand(v) == 0 for v in work)
    assert mus[nu] == 1
    return mus, nu

out = {}
for m in (18,):
    t0 = time.time()
    N = defect_numerator_b1(m)
    mus, nu = spectrum_b1(N, m)
    M = sum(mus[j] * z ** j for j in range(nu + 1))
    d = sp.discriminant(sp.Poly(M, z), z)
    fl = sp.factor_list(sp.expand(d))
    rows = []
    for (f, mult) in fl[1]:
        p = sp.Poly(f, a)
        rows.append([str(f.as_expr())[:70], int(mult), int(p.degree()),
                     str(p.LC())])
    out[str(m)] = rows
    print(f"m={m} ({time.time()-t0:.0f}s):", flush=True)
    for r in rows:
        print(f"   deg={r[2]:3d} mult={r[1]} lc={r[3][:30]}  {r[0][:50]}",
              flush=True)
    json.dump(out, open('matrix/disc_slice_m18.json', 'w'), indent=1)
