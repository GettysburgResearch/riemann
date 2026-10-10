#!/usr/bin/env python3
"""Kubota-pole residues of Gauss-sum Dirichlet series over Q(omega): numerical estimates of
theta coefficients tau_n(m)/tau_n(1) for n = 3 (validation: Patterson's cubic theta) and n = 6
(the sextic theta of hypothesis (S6), SEXTIC_THETA_S6.md).

Labels: EMPIRICAL, FLOAT (double precision, not directed, not certified).  Finite numerics; no
theorem is proved here.

Setup (conventions of a2/eis.py = the Oct 5 manuscript):
  * c runs over squarefree primary (c = 1 mod 3) elements of Z[omega] prime to 6 (one generator
    per ideal: the representative set V' = {c = 1 mod 3}; see Broeker-Hoffstein Sec. 2.2 for why
    the representative set matters), plus the p-power parts that the index m forces.
  * g_n(m, c) = sum_{x mod c} (x/c)_n e(mx/c), (x/c)_6 = chi_c(x), (x/c)_3 = chi_c(x)^2;
    G_n = g_n / sqrt(N c).
  * D_n(s, m) = sum_c G_n(m, c) N(c)^{-s} has its Kubota pole at s = 1/2 + 1/n with residue
    proportional to tau_n(m, V') N(m)^{-1/(2n)} (CFH (2.4); BH Sec. 2.2).
  * Smoothed sums F_m(Y) = sum_c G_n(m, c) w(N c / Y), w(t) = exp(-t), exp(-t^2) or the Riesz
    weight (1-t)_+^3 (full length; most reliable at this size), are fitted to
    A_m Y^{1/2+1/n} + B_m Y^{1/2-1/n} + C_m (the next Mellin poles; the left-contour remainder is
    assumed small, which the fit residuals test).  A_m is divided by the weight's Mellin factor
    at 1/2 + 1/n, so A_m estimates the residue.  Estimate: r(m) = (A_m / A_1) N(m)^{1/(2n)}.
    Agreement between weights is the noise diagnostic (cubic: ~0.04; sextic: ~0.5-1.3).
Twisted multiplicativity: g(m, c1 c2) = (c1/c2)(c2/c1) g(m, c1) g(m, c2); g(m, c) = conj((m/c)) g(1, c)
for (m, c) = 1; for m = pi^j (j = 1, 2, 4), the only extra p-part is c = pi^{j+1} c' with
g(pi^j, pi^{j+1}) = N(pi)^j g_{s(j+1)}(1, pi) (s = 6/n; a Ramanujan sum -1 when 6 | s(j+1)).

Usage: python3 s6_theta_bias.py XMAX MMAX OUT.json [path/to/s6_gauss binary]
  e.g. gcc -O2 -o $SCRATCH/s6_gauss s6_gauss.c -lm;  python3 s6_theta_bias.py 300000 100 out.json $SCRATCH/s6_gauss
  (X = 3e5: 79 s single process, 63 s of it in the C kernel.)
"""
import cmath, json, math, os, subprocess, sys, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import eis
from eis import mul, norm, conj, primary

XMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
MMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 150
OUT = sys.argv[3] if len(sys.argv) > 3 else None
BIN = sys.argv[4] if len(sys.argv) > 4 else os.environ.get('S6_GAUSS_BIN', './s6_gauss')
t0 = time.time()
ZETA = [cmath.exp(1j * math.pi * k / 3) for k in range(6)]

# ------------------------------------------------------------------ primes of Z[omega] prime to 6
def sieve(N):
    s = bytearray([1]) * (N + 1); s[0] = s[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(N + 1) if s[i]]

primes = []          # (kind, p, a, b): kind 0 split (N = p), kind 1 inert (pi = -q, N = q^2)
for p in sieve(XMAX):
    if p < 5: continue
    if p % 3 == 1:
        b = 1
        while True:
            d = 4 * p - 3 * b * b
            if d < 0: raise RuntimeError(p)
            s = math.isqrt(d)
            if s * s == d:
                a = (b + s) // 2; break
            b += 1
        x = primary((a, b)); y = primary(conj((a, b)))
        primes += [(0, p, x[0], x[1]), (0, p, y[0], y[1])]
    elif p * p <= XMAX:
        primes.append((1, p, -p, 0))
primes.sort(key=lambda t: (t[1] if t[0] == 0 else t[1] ** 2, t[2], t[3]))
inp = ''.join(f'{k} {p} {a} {b}\n' for (k, p, a, b) in primes)
res = subprocess.run([BIN], input=inp, capture_output=True, text=True, check=True)
rows = [l.split() for l in res.stdout.strip().split('\n')]
assert len(rows) == len(primes)
P = []               # dicts: elem, N, G[1..5]
for (k, p, a, b), r in zip(primes, rows):
    assert int(r[0]) == a and int(r[1]) == b
    G = [None] + [complex(float(r[1 + 2 * j]), float(r[2 + 2 * j])) for j in range(1, 6)]
    P.append({'kind': k, 'p': p, 'elem': (a, b), 'N': p if k == 0 else p * p, 'G': G})
NP = len(P)
t_gauss = time.time() - t0

# ------------------------------------------------------------------ validation against eis.gamma
val = 0.0; nval = 0
for Q in P:
    if Q['N'] > 250: break
    for j in (1, 2, 3):
        val = max(val, abs(Q['G'][j] - eis.gamma(j, [Q['elem']]))); nval += 1
modmax = max(abs(abs(Q['G'][j]) - 1) for Q in P for j in range(1, 6))

# ------------------------------------------------------------------ residue symbols (x/pi)_6
for Q in P:
    if Q['kind'] == 0:
        p, (a, b) = Q['p'], Q['elem']
        r = (-a) * pow(b % p, p - 2, p) % p
        Q['r'] = r
        z, zk, d = (1 + r) % p, 1, {}
        for k in range(6): d[zk] = k; zk = zk * z % p
        Q['dl'] = d
    else:
        q = Q['p']; zk = (1, 0); d = {}
        for k in range(6):
            d[zk] = k; zk = ((zk[0] - zk[1]) % q, (zk[0]) % q)   # times (1 + omega)
        Q['dl'] = d

def zpow_q(x, e, q):
    ru, rv = 1, 0; bu, bv = x[0] % q, x[1] % q
    while e:
        if e & 1: ru, rv = (ru * bu - rv * bv) % q, (ru * bv + rv * bu - rv * bv) % q
        bu, bv = (bu * bu - bv * bv) % q, (2 * bu * bv - bv * bv) % q
        e >>= 1
    return (ru, rv)

def sym(x, Q):
    """(x/pi)_6 as k (value zeta^k), or None if pi | x."""
    if Q['kind'] == 0:
        p = Q['p']; t = (x[0] + x[1] * Q['r']) % p
        if t == 0: return None
        return Q['dl'][pow(t, (p - 1) // 6, p)]
    q = Q['p']
    if x[0] % q == 0 and x[1] % q == 0: return None
    return Q['dl'][zpow_q(x, (q * q - 1) // 6, q)]

# quick check of sym against eis.sym_prime
for Q in P[:40]:
    for x in [(2, 0), (-1, 0), (0, 1), (5, 7), (11, -3)]:
        assert sym(x, Q) == eis.sym_prime(x, Q['elem']), (x, Q['elem'])

# ------------------------------------------------------------------ enumerate squarefree c
print(f'[{time.time()-t0:.1f}s] {NP} primes, Gauss sums done ({t_gauss:.1f}s); validation dev {val:.2e}', flush=True)
CF = []; CN = []; CG6 = []; CG3 = []; CE = []
symcache = {}
def psym(i, j):          # (P_i / P_j)_6
    key = (i, j)
    v = symcache.get(key)
    if v is None:
        v = sym(P[i]['elem'], P[j]); symcache[key] = v
    return v
stack = [((), 1, 0, 1 + 0j, 1 + 0j, (1, 0))]
while stack:
    fac, Nc, start, g6, g3, el = stack.pop()
    CF.append(fac); CN.append(Nc); CG6.append(g6); CG3.append(g3); CE.append(el)
    for i in range(start, NP):
        Ni = P[i]['N']
        if Nc * Ni > XMAX: break
        e = 0
        for f in fac: e += psym(f, i) + psym(i, f)
        stack.append((fac + (i,), Nc * Ni, i + 1, g6 * P[i]['G'][1] * ZETA[e % 6],
                      g3 * P[i]['G'][2] * ZETA[(2 * e) % 6], mul(el, P[i]['elem'])))
NC = len(CF)
CN = np.array(CN, dtype=np.float64); CG6 = np.array(CG6); CG3 = np.array(CG3)
maxf = max(len(f) for f in CF)
FAC = -np.ones((NC, maxf), dtype=np.int64)
for t, f in enumerate(CF): FAC[t, :len(f)] = f
print(f'[{time.time()-t0:.1f}s] {NC} squarefree c (max {maxf} prime factors)', flush=True)

# ------------------------------------------------------------------ smoothing and fit
WEIGHTS = {'exp1': (lambda t: np.exp(-t), 30.0), 'exp2': (lambda t: np.exp(-t * t), 5.6),
           'riesz3': (lambda t: np.where(t < 1, (1 - np.minimum(t, 1)) ** 3, 0.0), 1.0)}
# Mellin factors of the weights at s = b (main-term constant = Res * W(b)):
MELLIN = {'exp1': lambda b: math.gamma(b), 'exp2': lambda b: 0.5 * math.gamma(b / 2),
          'riesz3': lambda b: 6 * math.gamma(b) / math.gamma(b + 4)}
def fit(coef_norms, coefs, n):
    """returns, per weight, (A, B, C, relative rms residual)."""
    b1, b2 = 0.5 + 1.0 / n, 0.5 - 1.0 / n
    out = {}
    for wn, (w, cut) in WEIGHTS.items():
        Ytop = XMAX / cut
        Ys = np.geomspace(Ytop / 30, Ytop, 40)
        F = np.array([np.sum(coefs * w(coef_norms / Y)) for Y in Ys])
        M = np.stack([Ys ** b1, Ys ** b2, np.ones_like(Ys)], axis=1).astype(complex)
        sol, *_ = np.linalg.lstsq(M, F, rcond=None)
        resid = F - M @ sol
        out[wn] = (sol[0] / MELLIN[wn](b1), sol[1], sol[2], float(np.sqrt(np.mean(np.abs(resid) ** 2)) / np.sqrt(np.mean(np.abs(F) ** 2))))
    return out

def coeffs_for(m_idx, j, n):
    """norms and coefficients G_n(pi^j, c) over admissible c, for m = P[m_idx]^j (m_idx None: m = 1)."""
    s = 6 // n
    base = CG6 if n == 6 else CG3
    if m_idx is None: return CN, base
    Q = P[m_idx]
    # per-prime symbols (pi/f) and (f/pi); sentinel 99 where f = pi
    a1 = np.zeros(NP + 1, dtype=np.int64); a2 = np.zeros(NP + 1, dtype=np.int64)
    for i in range(NP):
        if i == m_idx: a1[i] = a2[i] = 99; continue
        a1[i] = sym(Q['elem'], P[i]); a2[i] = sym(P[i]['elem'], Q)
    e1 = a1[FAC].sum(axis=1); e2 = a2[FAC].sum(axis=1)     # padding index -1 -> a[NP] = 0
    ok = e1 < 99
    coprime = ok
    c1 = base * np.conj(np.array(ZETA)[(s * j * e1) % 6])
    t = s * (j + 1)
    Gpp = (Q['N'] ** (j / 2)) * Q['G'][t % 6] if t % 6 else -(Q['N'] ** ((j - 1) / 2))
    c2 = Gpp * c1 * np.array(ZETA)[(t * (e1 + e2)) % 6]
    n2 = CN * Q['N'] ** (j + 1)
    sel2 = coprime & (n2 <= XMAX)
    return (np.concatenate([CN[coprime], n2[sel2]]), np.concatenate([c1[coprime], c2[sel2]]))

out = {'params': {'XMAX': XMAX, 'MMAX': MMAX, 'n_primes': NP, 'n_c': NC},
       'validation': {'max_dev_vs_eis_gamma': val, 'n_checks': nval, 'max_abs_dev_unit_modulus': modmax}}
alpha = lambda e: complex(e[0] - e[1] / 2, e[1] * math.sqrt(3) / 2) / math.sqrt(norm(e))
for n in (3, 6):
    base = fit(*coeffs_for(None, 0, n), n)
    out[f'n{n}_m1'] = {w: [str(v[0]), str(v[1]), str(v[2]), v[3]] for w, v in base.items()}
    rows = []
    for i, Q in enumerate(P):
        if Q['N'] > MMAX: break
        js = (1,) if n == 3 else (1, 2, 4)
        for j in js:
            if Q['N'] ** (j + 1) > XMAX / 3: continue
            f = fit(*coeffs_for(i, j, n), n)
            row = {'pi': Q['elem'], 'N': Q['N'], 'j': j}
            for w in WEIGHTS:
                r = f[w][0] / base[w][0] * Q['N'] ** (j / (2 * n))
                row[w] = {'r': [r.real, r.imag], 'abs_r': abs(r), 'rel_resid': f[w][3]}
            row['G'] = {k: [Q['G'][k].real, Q['G'][k].imag] for k in range(1, 6)}
            row['alpha'] = [alpha(Q['elem']).real, alpha(Q['elem']).imag]
            row['chi_m1'] = sym((-1, 0), Q); row['chi_4'] = sym((4, 0), Q)
            row['chi_2'] = sym((2, 0), Q); row['chi_3'] = sym((3, 0), Q)
            rows.append(row)
            print(f"n={n} pi={Q['elem']} N={Q['N']} j={j} " + ' '.join(
                f"{w}: |r|={row[w]['abs_r']:.4f} arg/(2pi/12)={math.atan2(row[w]['r'][1], row[w]['r'][0])/(math.pi/6):+.3f} res={row[w]['rel_resid']:.1e}" for w in WEIGHTS), flush=True)
    out[f'n{n}_rows'] = rows
out['seconds'] = time.time() - t0
if OUT:
    with open(OUT, 'w') as fh: json.dump(out, fh, indent=1)
print(f'done in {time.time()-t0:.1f}s')
