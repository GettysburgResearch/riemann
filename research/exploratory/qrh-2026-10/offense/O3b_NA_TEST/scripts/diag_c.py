#!/usr/bin/env python3
"""O3b diagnostic: which rows c drive the alignment of the cumulative (Kubota-dominated) A^{(Y)} with B?
EMPIRICAL, floating point, finite.  Usage: python3 diag_c.py Q SMAX out.json
Computes A^{(Y)}_m = sum_{1<N s<=SMAX} c(s) gamma_1(s) conj chi_s(-m)  and a random-column control,
then r_c = |<A, chi_c>_{Omega xi}| / (||A|| ||chi_c||) for every row c (N c <= 2.5 Z), binned by N(c)."""
import os, sys, json, math, time
os.environ.setdefault('OMP_NUM_THREADS', '1'); os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import na_model as M
Q = int(sys.argv[1]); SMAX = int(sys.argv[2]); OUT = sys.argv[3]
Z = int(round(Q ** 1.15)); CMAX = int(2.5 * Z); XMAX = max(CMAX, SMAX)
t0 = time.time(); rng = np.random.default_rng(99 + Q)
primes = M.make_primes(XMAX); sf = sorted(M.sf_elements(primes, XMAX), key=lambda t: t[1])
x, y, nm = M.ball(Q); nM = len(x)
Om = np.clip(1 - nm / Q, 0, None) ** 3; xi = M.xi_vec(x, y)
E = np.empty((len(primes), nM), dtype=np.int8)
for i, P in enumerate(primes): E[i] = P.tab[P.resid(x, y)]
def chi_row(fac):
    if not fac: return np.ones(nM, complex)
    s = np.zeros(nM, np.int64); zm = np.zeros(nM, bool)
    for i in fac:
        r = E[i]; zm |= (r < 0); s += r
    v = M.ZETA[s % 6]; v[zm] = 0
    return v
A = np.zeros(nM, complex); Ar = np.zeros(nM, complex); Gd = 0.0
for el, N, fac in sf:
    if N <= 1 or N > SMAX: continue
    km1 = M.chi_exp_el(primes, fac, (-1, 0))
    u = np.conj(chi_row(fac)) * np.conj(M.ZETA[km1])
    cs = M.ZETA[M.chi_exp_el(primes, fac, (2, -2))] * np.conj(M.xi_el(el))
    A += cs * M.gamma_sf(primes, fac, 1) * u; Ar += np.exp(2j * np.pi * rng.random()) * u; Gd += float((Om * abs(u) ** 2).sum())
nA = math.sqrt((Om * abs(A) ** 2).sum()); nAr = math.sqrt((Om * abs(Ar) ** 2).sum())
rows = []
for el, N, fac in sf:
    if N > CMAX: continue
    v = chi_row(fac); nv = math.sqrt((Om * abs(v) ** 2).sum())
    rows.append((N, abs((Om * xi * A * v).sum()) / (nA * nv), abs((Om * xi * Ar * v).sum()) / (nAr * nv),
                 abs((Om * abs(xi) * A * v).sum()) / (nA * nv)))
rows = np.array(rows)
G = nA ** 2; exc = max(G - Gd, 1e-300)
one = np.ones(nM); n1 = math.sqrt(Om.sum())
p1 = abs((Om * xi * A).sum()); p1r = abs((Om * xi * Ar).sum())
r1_exc = p1 / (math.sqrt(exc) * n1)
print(f'G/G_diag - 1 = {G/Gd-1:.3f};  c=1 row: |<A,1>| / (sqrt(G-G_diag) ||1||) = {r1_exc:.4f};  noise floor (randcol) {p1r/(math.sqrt(exc)*n1):.4f}')
bins = [1, 2, 8, 32, 128, 512, 2048, 8192, 32768, 10 ** 9]
res = []
print(f'Q={Q} Z={Z} nM={nM} SMAX={SMAX}; 1/sqrt(nM)={1/math.sqrt(nM):.4f}')
print('N(c) bin        #c   rms r_c(A)  max r_c(A)  rms r_c(A_randcol)  rms r_c(A, no xi)')
for lo, hi in zip(bins[:-1], bins[1:]):
    sel = (rows[:, 0] >= lo) & (rows[:, 0] < hi)
    if sel.sum() == 0: continue
    r = rows[sel]
    rec = dict(lo=lo, hi=hi, n=int(sel.sum()), rms=float(np.sqrt((r[:, 1] ** 2).mean())), mx=float(r[:, 1].max()),
               rms_rand=float(np.sqrt((r[:, 2] ** 2).mean())), rms_noxi=float(np.sqrt((r[:, 3] ** 2).mean())))
    res.append(rec)
    print(f"[{lo:6d},{hi:9d}) {rec['n']:6d}  {rec['rms']:.4f}     {rec['mx']:.4f}      {rec['rms_rand']:.4f}            {rec['rms_noxi']:.4f}")
top = rows[np.argsort(-rows[:, 1])[:12]]
print('top rows (N c, r_c):', [(int(a), round(b, 3)) for a, b, *_ in top])
json.dump(dict(Q=Q, Z=Z, nM=nM, SMAX=SMAX, G_over_Gdiag=G/Gd, r1_exc=r1_exc, r1_noise=p1r/(math.sqrt(exc)*n1), bins=res, top=[[float(t) for t in r] for r in top], secs=time.time() - t0), open(OUT, 'w'), indent=1)
print(f'done {time.time()-t0:.1f}s')
