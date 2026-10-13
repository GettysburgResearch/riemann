#!/usr/bin/env python3
"""O3b main run.  EMPIRICAL, floating point, finite.  Usage: python3 na_run.py Q out.json [ntrial]
For one ball size Q and Z = round(Q^1.15), loops over P_a in {1,4,16,64,256,1024}, Y' = sqrt(P_a Q).
Writes per-(Q,Y') diagnostics: Gram excess, exceptional-eigenspace dimension and mass, R_full,
R_exc, R_rest, the diagonal (c = s) and off-diagonal parts, the no-xi control, and baselines."""
import os, sys, json, math, time
os.environ.setdefault('OMP_NUM_THREADS', '1'); os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import na_model as M

Q = int(sys.argv[1]); OUT = sys.argv[2]; NT = int(sys.argv[3]) if len(sys.argv) > 3 else 24
PAS = [1, 4, 16, 64, 256, 1024]
Z = int(round(Q ** 1.15))
CMAX = int(2.5 * Z)
YS = [int(round(math.sqrt(P * Q))) for P in PAS]
XMAX = max(CMAX, 2 * max(YS))
t0 = time.time()
rng = np.random.default_rng(12345 + Q)
primes = M.make_primes(XMAX)
sf = M.sf_elements(primes, XMAX)
sf = [t for t in sf if t[1] > 0]
print(f'Q={Q} Z={Z} primes={len(primes)} sf={len(sf)} t={time.time()-t0:.1f}', flush=True)
x, y, nm = M.ball(Q)
nM = len(x)
Om = np.clip(1 - nm / Q, 0, None) ** 3
xi = M.xi_vec(x, y)
w_xi = Om * xi                 # pairing weight
w_abs = Om * np.abs(xi)        # no-xi control: weight Omega * 1_{(m,6)=1}
# per-prime exponent rows over the ball (int8, -1 = zero)
E = np.empty((len(primes), nM), dtype=np.int8)
for i, P in enumerate(primes):
    E[i] = P.tab[P.resid(x, y)]
print(f'ball {nM}, exp table built t={time.time()-t0:.1f}', flush=True)
B2L = (2, -2)    # b_* = 2 lambda
def chi_row(fac):
    if not fac: return np.ones(nM, complex)
    s = np.zeros(nM, np.int64); z = np.zeros(nM, bool)
    for i in fac:
        r = E[i]; z |= (r < 0); s += r
    v = M.ZETA[s % 6]; v[z] = 0
    return v
# ------------- B coefficients
info = {}
bc = []; cidx = []
for j, (el, N, fac) in enumerate(sf):
    if N > CMAX: continue
    mu = (-1) ** len(fac)
    g2 = M.gamma_sf(primes, fac, 2)
    theta = mu * np.conj(g2) ** 2
    kb = M.chi_exp_el(primes, fac, B2L)
    Xi = M.xi_el(el) * M.ZETA[kb]
    v = math.exp(-(N / Z) ** 2) / math.sqrt(N)
    bc.append((theta * np.conj(Xi) * v, np.conj(g2) ** 2 * np.conj(Xi) * v, g2 * np.conj(Xi) * v))
    cidx.append(j)
bc = np.array(bc)          # columns: b'(theta), b' with mu removed (for +-1 control), b'(untwisted gamma_2)
cpos = {j: k for k, j in enumerate(cidx)}
mus = np.array([(-1) ** len(sf[j][2]) for j in cidx])
print(f'#c={len(cidx)} t={time.time()-t0:.1f}', flush=True)
# ------------- A vectors per Y'
Avecs = []; recs = []; cols_by = []; topv = []
for P_a, Yp in zip(PAS, YS):
    cols = [j for j, (el, N, fac) in enumerate(sf) if Yp <= N <= 2 * Yp]
    U = np.empty((nM, len(cols)), complex); ap = np.empty(len(cols), complex)
    for k, j in enumerate(cols):
        el, N, fac = sf[j]
        U[:, k] = np.conj(chi_row(fac))
        r = N / Yp
        W1 = math.sin(math.pi * (r - 1)) ** 2
        kb = M.chi_exp_el(primes, fac, B2L); km1 = M.chi_exp_el(primes, fac, (-1, 0))
        cs = M.ZETA[kb] * np.conj(M.xi_el(el))
        ap[k] = W1 * r ** -0.5 * cs * M.gamma_sf(primes, fac, 1) * np.conj(M.ZETA[km1]) / Yp
    A = U @ ap
    G = (U.conj().T * Om) @ U          # Gram, s-side
    lam, V = np.linalg.eigh(G)
    dbar = np.real(np.diag(G)).mean()
    neff = Om.sum() ** 2 / (Om ** 2).sum()
    gam = len(cols) / neff
    edge = dbar * (1 + math.sqrt(gam)) ** 2
    nexc = int((lam > 1.2 * edge).sum())
    def proj(r):
        if r == 0: return np.zeros_like(ap)
        Vt = V[:, -r:]
        return Vt @ (Vt.conj().T @ ap)
    a_exc = proj(nexc)
    A_exc = U @ a_exc; A_rest = A - A_exc
    nA2 = float((Om * abs(A) ** 2).sum())
    diag_rand = float((abs(ap) ** 2 * np.real(np.diag(G))).sum())    # E||A||^2 if gamma_1 phases randomised
    # diagonal kernels K(s,s) = sum_m w |chi_s(m)|^2
    Kxi = (w_xi[:, None] * abs(U) ** 2).sum(0); Kab = (w_abs[:, None] * abs(U) ** 2).sum(0)
    bidx = np.array([cpos.get(j, -1) for j in cols])
    rec = dict(P_a=P_a, Yp=Yp, ns=len(cols), nM=nM, Z=Z, nc=len(cidx), gram_A=nA2, gram_rand=diag_rand,
               excess=nA2 / diag_rand - 1, Q_over_Y=float(Om.sum()) / Yp, nexc=nexc, edge=edge,
               lam_top=[float(t) for t in lam[-6:][::-1]], dbar=dbar,
               frac_exc=float((Om * abs(A_exc) ** 2).sum()) / nA2,
               frac_top1=float((Om * abs(U @ proj(1)) ** 2).sum()) / nA2,
               frac_top4=float((Om * abs(U @ proj(min(4, len(cols)))) ** 2).sum()) / nA2)
    for name, av in (('full', ap), ('exc', a_exc), ('rest', ap - a_exc)):
        ok = bidx >= 0
        # diagonal c = s contributions (squarefree: t = 1 only), with xi and without
        rec['diag_xi_' + name] = complex((av[ok] * bc[bidx[ok], 0] * Kxi[ok]).sum())
        rec['diag_noxi_' + name] = complex((av[ok] * bc[bidx[ok], 0] * Kab[ok]).sum())
    Avecs += [A, A_exc, A_rest]
    cols_by.append(cols)
    rec['R_top'] = {}
    topv.append([U @ proj(min(r, len(cols))) for r in (1, 4, 16)])
    recs.append(rec)
    print(f"  P_a={P_a} Y'={Yp} ns={len(cols)} excess={rec['excess']:.3f} nexc={nexc} frac_exc={rec['frac_exc']:.3f} t={time.time()-t0:.1f}", flush=True)
    del U, G
Av = np.array(Avecs)                       # (3*len(PAS), nM)
LX = (Av * w_xi).T; LA = (Av * w_abs).T     # (nM, nv)
# ------------- one pass over c: B (three coefficient variants), y_c = <A_v, chi_c> with xi and without, ||chi_c||^2
nv = Av.shape[0]
Yx = np.zeros((len(cidx), nv), complex); Ya = np.zeros((len(cidx), nv), complex)
cn2 = np.zeros(len(cidx)); Bs = np.zeros((nM, 3), complex)
CH = 400
for st in range(0, len(cidx), CH):
    js = cidx[st:st + CH]
    Ech = np.empty((nM, len(js)), complex)
    for k, j in enumerate(js): Ech[:, k] = chi_row(sf[j][2])
    Bs += Ech @ bc[st:st + CH]
    Yx[st:st + CH] = Ech.T @ LX
    Ya[st:st + CH] = Ech.T @ LA
    cn2[st:st + CH] = Om @ (abs(Ech) ** 2)
print(f'B pass done t={time.time()-t0:.1f}', flush=True)
nB2 = [float((Om * abs(Bs[:, i]) ** 2).sum()) for i in range(3)]
B = Bs[:, 0]
expB2 = float((abs(bc[:, 0]) ** 2 * cn2).sum())
for ip, rec in enumerate(recs):
    for kk, name in enumerate(('full', 'exc', 'rest')):
        v = 3 * ip + kk
        nA = math.sqrt(float((Om * abs(Av[v]) ** 2).sum()))
        if nA == 0: rec['R_' + name] = None; continue
        pair = complex((w_xi * Av[v] * B).sum())
        pair2 = complex((Yx[:, v] * bc[:, 0]).sum())
        rec['pair_' + name] = pair; rec['pair_check_' + name] = abs(pair - pair2) / max(abs(pair), 1e-300)
        nB = math.sqrt(nB2[0])
        rec['R_' + name] = abs(pair) / (nA * nB)
        rec['Rdiag_' + name] = abs(rec['diag_xi_' + name]) / (nA * nB)
        rec['Roff_' + name] = abs(pair - rec['diag_xi_' + name]) / (nA * nB)
        pna = complex((Ya[:, v] * bc[:, 0]).sum())
        rec['R_noxi_' + name] = abs(pna) / (nA * nB)
        rec['Rdiag_noxi_' + name] = abs(rec['diag_noxi_' + name]) / (nA * nB)
        rec['Roff_noxi_' + name] = abs(pna - rec['diag_noxi_' + name]) / (nA * nB)
        # variants of B: untwisted gamma_2 (no conj alpha)
        rec['R_Bu_' + name] = abs(complex((Yx[:, v] * bc[:, 2]).sum())) / (nA * math.sqrt(nB2[2]))
        # mu -> 1 control (removes the Moebius factor of theta(c) = mu conj(gamma_2)^2): with xi and without
        rec['R_mu1_' + name] = abs(complex((Yx[:, v] * bc[:, 1]).sum())) / (nA * math.sqrt(nB2[1]))
        rec['R_mu1_noxi_' + name] = abs(complex((Ya[:, v] * bc[:, 1]).sum())) / (nA * math.sqrt(nB2[1]))

        # baseline (i): |B_m| with random phases
        r1 = []
        for t in range(NT):
            Br = abs(B) * np.exp(2j * np.pi * rng.random(nM))
            r1.append(abs(complex((w_xi * Av[v] * Br).sum())) / (nA * nB))
        # baseline (ii): theta(c) -> random unimodular (keeps chi_c(m) structure); norm by expectation
        r2 = []; r3 = []; r3a = []
        for t in range(NT):
            ph = np.exp(2j * np.pi * rng.random(len(cidx)))
            r2.append(abs(complex((Yx[:, v] * abs(bc[:, 0]) * ph).sum())) / (nA * math.sqrt(expB2)))
            eps = rng.choice([-1.0, 1.0], len(cidx))           # mu -> random signs
            r3.append(abs(complex((Yx[:, v] * bc[:, 1] * eps).sum())) / (nA * math.sqrt(expB2)))
            r3a.append(abs(complex((Ya[:, v] * bc[:, 1] * eps).sum())) / (nA * math.sqrt(expB2)))
        rec['base_mphase_' + name] = [float(np.mean(r1)), float(np.percentile(r1, 90))]
        rec['base_cphase_' + name] = [float(np.mean(r2)), float(np.percentile(r2, 90))]
        rec['ctrl_mu_pm1_' + name] = [float(np.mean(r3)), float(np.percentile(r3, 90))]
        rec['ctrl_mu_pm1_noxi_' + name] = [float(np.mean(r3a)), float(np.percentile(r3a, 90))]
for ip, rec in enumerate(recs):
    for r, Av_ in zip((1, 4, 16), topv[ip]):
        nA = math.sqrt(float((Om * abs(Av_) ** 2).sum()))
        rec['R_top'][str(r)] = dict(R=abs(complex((w_xi * Av_ * B).sum())) / (nA * math.sqrt(nB2[0])),
            R_noxi=abs(complex((w_abs * Av_ * B).sum())) / (nA * math.sqrt(nB2[0])),
            frac=float(nA ** 2 / rec['gram_A']))
out = dict(Q=Q, Z=Z, nM=nM, nc=len(cidx), normB2=nB2, expB2=expB2, sumOmega=float(Om.sum()),
           recs=recs, secs=time.time() - t0)
def enc(o):
    if isinstance(o, complex): return [o.real, o.imag]
    if isinstance(o, (np.floating,)): return float(o)
    if isinstance(o, (np.integer,)): return int(o)
    raise TypeError(type(o))
json.dump(out, open(OUT, 'w'), indent=1, default=enc)
for rec in recs:
    print(f"P_a={rec['P_a']:5d} Y'={rec['Yp']:5d} exc={rec['excess']:.3f} nexc={rec['nexc']} fexc={rec['frac_exc']:.3f} "
          f"R_full={rec['R_full']:.4f} R_exc={rec.get('R_exc') or 0:.4f} R_rest={rec.get('R_rest') or 0:.4f} "
          f"base_m={rec['base_mphase_full'][0]:.4f} base_c={rec['base_cphase_full'][0]:.4f} "
          f"Rdiag={rec['Rdiag_full']:.2e} R_noxi={rec['R_noxi_full']:.4f} Rdiag_noxi={rec['Rdiag_noxi_full']:.4f} "
          f"Rmu1={rec['R_mu1_full']:.4f} Rmu1_noxi={rec['R_mu1_noxi_full']:.4f} pm1={rec['ctrl_mu_pm1_full'][0]:.4f} pm1_noxi={rec['ctrl_mu_pm1_noxi_full'][0]:.4f} top1={rec['R_top']['1']['R']:.4f}")
print(f'done {time.time()-t0:.1f}s')
