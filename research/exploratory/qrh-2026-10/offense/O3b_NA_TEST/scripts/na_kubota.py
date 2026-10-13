#!/usr/bin/env python3
"""O3b, operational definition OP-K (Kubota residue).  EMPIRICAL, floating point, finite.
A^{exc} is the Kubota-residue (Patterson-bias) part of A in the column variable s: the component of
  sum_s c(s) gamma_1(s) conj chi_s(-m) N(s)^{-w}
coming from the pole at w = 2/3 ([S30] Prop 15.2's P_a^{1/6} term; O3 README Sec. 2.3).  Hence
  <A^{exc}, B> = Y'^{-1/3} * C_W * rho_B,   rho_B = Res_{w=2/3} sum_s y_s N(s)^{-w},
  y_s = c(s) gamma_1(s) z_s,   z_s = sum_m Omega xi(m) conj chi_s(-m) B_m.
We compute y_s for ALL squarefree primary s (2 not dividing s) with N(s) <= SMAX and test whether the
cumulative sums T_B(Y) = sum_{N s <= Y} y_s grow like Y^{2/3} (pole: alignment of A^{exc} with B) or like
Y^{1/2} (no pole), normalised by the random-walk scale.  Same for the self-bias of A (Gram form):
  G(Y) = sum_m Omega |sum_{N s <= Y} c gamma_1 conj chi_s(-m)|^2  vs its random expectation.
Usage: python3 na_kubota.py Q SMAX out.json"""
import os, sys, json, math, time
os.environ.setdefault('OMP_NUM_THREADS', '1'); os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import na_model as M
Q = int(sys.argv[1]); SMAX = int(sys.argv[2]); OUT = sys.argv[3]
Z = int(round(Q ** 1.15)); CMAX = int(2.5 * Z); XMAX = max(CMAX, SMAX)
t0 = time.time(); rng = np.random.default_rng(777 + Q)
primes = M.make_primes(XMAX); sf = [t for t in M.sf_elements(primes, XMAX)]
sf.sort(key=lambda t: t[1])
x, y, nm = M.ball(Q); nM = len(x)
Om = np.clip(1 - nm / Q, 0, None) ** 3; xi = M.xi_vec(x, y)
E = np.empty((len(primes), nM), dtype=np.int8)
for i, P in enumerate(primes): E[i] = P.tab[P.resid(x, y)]
print(f'Q={Q} Z={Z} nM={nM} primes={len(primes)} sf={len(sf)} t={time.time()-t0:.1f}', flush=True)
def chi_row(fac):
    if not fac: return np.ones(nM, complex)
    s = np.zeros(nM, np.int64); zm = np.zeros(nM, bool)
    for i in fac:
        r = E[i]; zm |= (r < 0); s += r
    v = M.ZETA[s % 6]; v[zm] = 0
    return v
B2L = (2, -2)
# ---- B variants
Bv = np.zeros((nM, 4), complex)   # 0: theta = mu conj g2^2 ; 1: mu -> 1 ; 2: mu -> random +-1 ; 3: theta -> random phase
cl = [t for t in sf if t[1] <= CMAX]
CH = 400
for st in range(0, len(cl), CH):
    ch = cl[st:st + CH]
    Ech = np.empty((nM, len(ch)), complex); co = np.empty((len(ch), 4), complex)
    for k, (el, N, fac) in enumerate(ch):
        Ech[:, k] = chi_row(fac)
        g2 = M.gamma_sf(primes, fac, 2); mu = (-1) ** len(fac)
        Xi = M.xi_el(el) * M.ZETA[M.chi_exp_el(primes, fac, B2L)]
        base = np.conj(g2) ** 2 * np.conj(Xi) * math.exp(-(N / Z) ** 2) / math.sqrt(N)
        co[k] = (mu * base, base, rng.choice([-1, 1]) * base, abs(base) * np.exp(2j * np.pi * rng.random()))
    Bv += Ech @ co
Bm = np.abs(Bv[:, 0]) * np.exp(2j * np.pi * rng.random(nM))   # 4: |B| with random m-phases
Bv = np.column_stack([Bv, Bm])
nB = np.sqrt((Om[:, None] * abs(Bv) ** 2).sum(0))
print(f'B built t={time.time()-t0:.1f}', flush=True)
W = (Om * xi)[:, None] * Bv; Wa = (Om * abs(xi))[:, None] * Bv
# ---- sweep s
sl = [t for t in sf if 1 < t[1] <= SMAX]
checkpoints = sorted(set(int(SMAX * 2 ** (-k / 2)) for k in range(0, 17)))
T = np.zeros(5, complex); Ta = np.zeros(5, complex); Tr = np.zeros(5, complex)
RW = np.zeros(5); RWa = np.zeros(5)
Avec = np.zeros(nM, complex); Arand = np.zeros(nM, complex); diagE = 0.0
recs = []; ci = 0
for st in range(0, len(sl), CH):
    ch = sl[st:st + CH]
    U = np.empty((nM, len(ch)), complex); cg = np.empty(len(ch), complex)
    for k, (el, N, fac) in enumerate(ch):
        km1 = M.chi_exp_el(primes, fac, (-1, 0))
        U[:, k] = np.conj(chi_row(fac)) * np.conj(M.ZETA[km1])           # conj chi_s(-m)
        cs = M.ZETA[M.chi_exp_el(primes, fac, B2L)] * np.conj(M.xi_el(el))
        cg[k] = cs * M.gamma_sf(primes, fac, 1)
    zs = U.T @ W; za = U.T @ Wa                       # (len(ch), 5)
    ys = cg[:, None] * zs; ya = cg[:, None] * za
    # random-phase column coefficients (no Kubota pole by construction)
    ph = np.exp(2j * np.pi * rng.random(len(ch)))
    yr = ph[:, None] * zs
    nrm = (Om[:, None] * abs(U) ** 2).sum(0)           # ||chi_s||^2
    # process in order to hit checkpoints exactly
    Ns = np.array([t[1] for t in ch])
    for k in range(len(ch)):
        T += ys[k]; Ta += ya[k]; Tr += yr[k]
        RW += abs(zs[k]) ** 2; RWa += abs(za[k]) ** 2
        Avec += cg[k] * U[:, k]; Arand += ph[k] * U[:, k]; diagE += nrm[k]
        while ci < len(checkpoints) and (k + 1 == len(ch) and st + CH >= len(sl) or Ns[k] <= checkpoints[ci] < (Ns[k + 1] if k + 1 < len(ch) else (sl[st + CH][1] if st + CH < len(sl) else 10 ** 18))):
            G = float((Om * abs(Avec) ** 2).sum()); Gr = float((Om * abs(Arand) ** 2).sum())
            recs.append(dict(Y=checkpoints[ci], ns=st + k + 1,
                T=[abs(t) for t in T], T_noxi=[abs(t) for t in Ta], T_randcol=[abs(t) for t in Tr],
                RW=[float(math.sqrt(r)) for r in RW], RW_noxi=[float(math.sqrt(r)) for r in RWa],
                gram=G, gram_randcol=Gr, gram_diag=diagE))
            ci += 1
    if st // CH % 5 == 0: print(f'  s up to N={ch[-1][1]} t={time.time()-t0:.1f}', flush=True)
out = dict(Q=Q, Z=Z, nM=nM, SMAX=SMAX, normB=[float(v) for v in nB],
           variants=['theta=mu*conj(g2)^2', 'mu->1', 'mu->random +-1', 'theta->random phase', '|B| random m-phase'],
           recs=recs, secs=time.time() - t0)
json.dump(out, open(OUT, 'w'), indent=1)
print('Y      ns   G/Gdiag  Grand/Gdiag | T/RW (theta, mu1, pm1, cph, mph) | T_randcol/RW(theta) | noxi T/RW (theta, mu1)')
for r in recs:
    print(f"{r['Y']:6d} {r['ns']:5d} {r['gram']/r['gram_diag']:.3f} {r['gram_randcol']/r['gram_diag']:.3f} | "
          + ' '.join(f"{a/b:.2f}" for a, b in zip(r['T'], r['RW'])) + f" | {r['T_randcol'][0]/r['RW'][0]:.2f} | "
          + f"{r['T_noxi'][0]/r['RW_noxi'][0]:.2f} {r['T_noxi'][1]/r['RW_noxi'][1]:.2f}")
print(f'done {time.time()-t0:.1f}s')
