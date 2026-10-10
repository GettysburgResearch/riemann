#!/usr/bin/env python3
"""Lane A2 hostile numeric re-verification of the HHFE/HCNC chain objects.
All formulas implemented directly from branch sources:
  L-102009 (f4016db5), L-102010 (f4016db5, constant 3), T-102001,
  L-100310/311/312 (4f69b765 = PR #685), L-103100/101/102 (89f9954).
"""
import numpy as np, math, json
from math import sqrt, log

OUT = {}
SQ2 = sqrt(2.0)
H = log(2.0)

# ---------- arithmetic tables ----------
def sieve_spf(N):
    spf = np.zeros(N+1, dtype=np.int64)
    for i in range(2, N+1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i  # careful: set spf for multiples where unset
    return spf

def build_tables(N):
    spf = np.zeros(N+1, dtype=np.int64)
    for p in range(2, N+1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    mu = np.zeros(N+1, dtype=np.float64); mu[1] = 1
    eta = np.zeros(N+1); eta[1] = 1
    # eta(p^k) = C(2k,k)/4^k
    etapk = [math.comb(2*k, k)/4**k for k in range(0, 64)]
    for n in range(2, N+1):
        p = spf[n]; m = n; k = 0
        while m % p == 0: m //= p; k += 1
        rest = n // p**k
        mu[n] = (-mu[rest] if k == 1 else 0.0)
        eta[n] = eta[rest]*etapk[k]
    return mu, eta

def dconv(f, g, N):
    """Dirichlet convolution up to N (f,g arrays indexed 0..N)."""
    out = np.zeros(N+1)
    for d in range(1, N+1):
        if f[d] == 0: continue
        gd = g[1:(N//d)+1]
        out[d::d] += f[d]*gd
    return out

NMAX = 120000
mu, eta = build_tables(NMAX)
one = np.ones(NMAX+1); one[0] = 0

# ---------- check 1: eta*eta = 1 ----------
binom_ok = all(abs(sum(math.comb(2*i,i)*math.comb(2*(k-i),k-i) for i in range(k+1))/4**k - 1.0) < 1e-12 for k in range(0, 40))
ee = dconv(eta, eta, 20000)
OUT['eta_star_eta_eq_1'] = {'binomial_identity_k_le_39': bool(binom_ok),
                            'max_dev_n_le_20000': float(np.max(np.abs(ee[1:] - 1.0)))}

# ---------- check 2/3: Vaughan identities ----------
def vaughan_checks(U, N):
    muU = mu.copy(); muU[U+1:] = 0.0
    bU = mu.copy(); bU[:U+1] = 0.0
    aU = -dconv(muU, one, N); aU[1] += 1.0   # eps - muU*1
    # a_U = b_U * 1
    dev_a = np.max(np.abs(aU[:N+1] - dconv(bU, one, N)))
    g1 = dconv(dconv(aU, aU, N), mu, N)      # a*a*mu
    g2 = dconv(dconv(bU, bU, N), one, N)     # b*b*1
    hU = dconv(bU, eta, N)
    g3 = dconv(hU, hU, N)
    dev_g12 = np.max(np.abs(g1 - g2)); dev_g13 = np.max(np.abs(g1 - g3))
    # mu = 2 muU - muU*muU*1 + a*a*mu
    rhs = 2*muU[:N+1] - dconv(dconv(muU, muU, N), one, N) + g1
    dev_mu = np.max(np.abs(mu[:N+1] - rhs))
    return dict(dev_aU_eq_bU_conv_1=float(dev_a), dev_aamu_eq_bb1=float(dev_g12),
                dev_aamu_eq_hh=float(dev_g13), dev_vaughan_mu_identity=float(dev_mu))
OUT['vaughan_identities'] = {f'U={U},N={N}': vaughan_checks(U, N) for U, N in [(5, 3000), (12, 8000), (21, 8000)]}

# ---------- kernels ----------
def A_minus(y):
    return 1.0 if 1 < y < 2 else (-SQ2 if 2 < y < 4 else 0.0)
def A_plus(y):
    if 1 < y <= 2: return 4*sqrt(y) - 3
    if 2 < y < 4: return SQ2*(3 - 2*sqrt(y))
    return 0.0
def A_spline(y):
    if 1 <= y <= 2: return 2*(sqrt(y)-1)
    if 2 <= y <= 4: return 2*SQ2 - sqrt(2*y)
    return 0.0

def K1(x):
    """K1(x) = int A_-(y) A_+(x/y) dy/y, closed form piecewise."""
    if x <= 1 or x >= 16: return 0.0
    lo, hi = max(1.0, x/4), min(4.0, x)
    brks = sorted({lo, hi, 2.0, x/2, x/4} & set())  # placeholder
    pts = sorted({lo, hi} | {t for t in (2.0, x/2, x/4) if lo < t < hi})
    tot = 0.0
    for y1, y2 in zip(pts[:-1], pts[1:]):
        ym = sqrt(y1*y2)
        c = A_minus(ym)
        if c == 0.0: continue
        z = x/ym
        if 1 < z <= 2: al, be = -3.0, 4.0
        elif 2 < z < 4: al, be = 3*SQ2, -2*SQ2
        else: continue
        # int_{y1}^{y2} c*(al + be*sqrt(x/y)) dy/y
        tot += c*(al*log(y2/y1) + be*sqrt(x)*(-2.0)*(1/sqrt(y2) - 1/sqrt(y1)))
    return tot

# Mellin check of K1 against both closed forms
import mpmath as mp
mp.mp.dps = 30
def K1_mellin_num(s):
    return mp.quad(lambda u: mp.e**(u)*0 + K1(float(mp.e**u))*mp.e**(-s*u), [0, mp.log(16)])
def Ahat(s): return (1 - 2**(-s))*(1 - SQ2*2**(-s))/(s*(s - 0.5))
def K1hat_formula(s): return (s - 0.5)*(s + 1.5)*Ahat(s)**2
def K0hat(s): return (1 - SQ2*2**(-s))*(1 - 2**(-s))**2*(s + 1.5)/(s**2*(s - 0.5))
def K1hat_685(s): return (1 - SQ2*2**(-s))*K0hat(s)
mell = {}
for s in [mp.mpf(2), mp.mpf('0.8'), mp.mpc(1, 3), mp.mpf('1.5')]:
    num = complex(K1_mellin_num(s))
    f1 = complex(K1hat_formula(complex(s))); f2 = complex(K1hat_685(complex(s)))
    mell[str(s)] = {'num': abs(num), 'dev_vs_L102009': abs(num - f1), 'dev_vs_L100310': abs(num - f2)}
half = complex(K1_mellin_num(mp.mpf('0.5') + mp.mpf('1e-25')))
mell['K1hat(1/2)'] = abs(half)
OUT['K1_mellin'] = {k: {kk: float(vv) for kk, vv in v.items()} if isinstance(v, dict) else float(v) for k, v in mell.items()}

# ---------- fields, energies, B ----------
def h_field_prefix(hU, wmax):
    """returns arrays n, c(n)=h(n)/sqrt(n) for n<=wmax."""
    n = np.arange(1, wmax+1)
    return n, hU[1:wmax+1]/np.sqrt(n)

def field_energy(hU, U, Ncut, Ymax):
    """int_U^{Ymax} |sum_{U<n<=Ncut} h(n)/sqrt(n) A_-(Y/n)|^2 dY/Y, exact piecewise-const."""
    ns = np.arange(U+1, Ncut+1)
    c = hU[U+1:Ncut+1]/np.sqrt(ns)
    brk = np.unique(np.concatenate([ns, 2.0*ns, 4.0*ns, [U, Ymax]]).astype(float))
    brk = brk[(brk >= U) & (brk <= Ymax)]
    brk.sort()
    # prefix sums over n of c
    csum = np.zeros(Ncut+2); csum[U+1:Ncut+1] = c; csum = np.cumsum(csum)
    def S(a, b):  # sum of c(n) for a < n < b  (n integer strictly inside)
        ia, ib = math.floor(a), math.ceil(b)-1
        ia = min(max(ia, U), Ncut); ib = min(max(ib, U), Ncut)
        if ib <= ia: return 0.0
        return csum[ib] - csum[ia]
    E = 0.0
    for y1, y2 in zip(brk[:-1], brk[1:]):
        ym = sqrt(y1*y2)
        val = S(ym/2, ym) - SQ2*S(ym/4, ym/2)
        E += val*val*log(y2/y1)
    return E

def field_value(hU, U, Ncut, Y):
    ns = np.arange(U+1, Ncut+1)
    c = hU[U+1:Ncut+1]/np.sqrt(ns)
    m = (ns > Y/4) & (ns < Y)
    sgn = np.where(ns > Y/2, 1.0, -SQ2)
    return float(np.sum(c[m]*sgn[m]))

def B_direct(g, X):
    lo, hi = int(X/16)+1, int(X)
    ns = np.arange(lo, hi+1)
    vals = np.array([K1(X/n) for n in ns])
    return float(np.sum(g[lo:hi+1]/np.sqrt(ns)*vals))

def B_twofield(bU, aU, U, X, npts=None):
    """int_U^{X/U} F_-(Y) F_+(X/Y) dY/Y via breakpoint-exact Gauss quadrature."""
    ds = np.nonzero(bU)[0]; es = np.nonzero(aU)[0]
    brks = set([U, X/U])
    for d in ds:
        for t in (d, 2*d, 4*d):
            if U < t < X/U: brks.add(float(t))
    for e in es:
        for t in (X/e, X/(2*e), X/(4*e)):
            if U < t < X/U: brks.add(float(t))
    brks = sorted(brks)
    # Gauss-Legendre 8 pt per interval (F_- const, F_+ smooth sqrt on each)
    xg, wg = np.polynomial.legendre.leggauss(8)
    tot = 0.0
    cd = bU[ds]/np.sqrt(ds); ce = aU[es]/np.sqrt(es)
    for y1, y2 in zip(brks[:-1], brks[1:]):
        if y2 - y1 < 1e-12: continue
        u1, u2 = log(y1), log(y2)
        uu = 0.5*(u2-u1)*xg + 0.5*(u1+u2); ww = 0.5*(u2-u1)*wg
        for u, w in zip(uu, ww):
            Y = math.exp(u)
            Fm = sum(cd[i]*A_minus(Y/ds[i]) for i in range(len(ds)) if ds[i] > Y/4 and ds[i] < Y)
            Z = X/Y
            Fp = sum(ce[i]*A_plus(Z/es[i]) for i in range(len(es)) if es[i] > Z/4 and es[i] < Z)
            tot += w*Fm*Fp
    return tot

# small-scale two-field identity check
res_twofield = {}
for X, U in [(600.0, 8), (2000.0, 12)]:
    N = int(X)
    muU = mu.copy(); muU[U+1:] = 0.0
    bU = mu.copy(); bU[:U+1] = 0.0
    aU = -dconv(muU, one, N); aU[1] += 1.0
    g = dconv(dconv(bU, bU, N), one, N)
    lhs = B_direct(g, X)
    # restrict bU,aU supports to relevant ranges d<=X/U, e<=X/U
    bUr = bU.copy(); bUr[int(X/U)+1:] = 0
    aUr = aU.copy(); aUr[int(X/U)+1:] = 0
    rhs = B_twofield(bUr[:N+1], aUr[:N+1], U, X)
    res_twofield[f'X={X},U={U}'] = {'B_direct': lhs, 'B_int_F-F+': rhs,
                                    'rel_dev': abs(lhs-rhs)/max(1e-30, abs(lhs))}
OUT['twofield_identity_L102009_13'] = res_twofield

# ---------- |B| <= 3 H tables ----------
rows = []
for X in [1e3, 3e3, 1e4, 3e4, 1e5]:
    U = int(X**(1/3.0))
    N = int(X)
    bU = mu.copy(); bU[:U+1] = 0.0
    hU = dconv(bU, eta, min(NMAX, 4*int(X/U)+8))
    g = dconv(dconv(bU, bU, N), one, N)
    B = B_direct(g, X)
    Ntr = int(X/U)
    H_tr = field_energy(hU, U, Ntr, 4.0*Ntr)          # truncated (L-103100 object, N_X=floor(X/U))
    H_un = field_energy(hU, U, min(len(hU)-1, int(4*X/U)), 4.0*X/U)  # untruncated on [U,4X/U]
    rows.append({'X': X, 'U': U, 'B': B, 'H_trunc': H_tr, 'H_untrunc': H_un,
                 'ratio_trunc': abs(B)/H_tr, 'ratio_untrunc': abs(B)/H_un})
OUT['B_le_3H_table'] = rows

# ---------- Plancherel L-103102.1 ----------
def plancherel_check(U, N):
    bU = mu.copy(); bU[:U+1] = 0.0
    hU = dconv(bU, eta, N)
    lhs = field_energy(hU, U, N, 4.0*N)
    ns = np.arange(U+1, N+1); c = hU[U+1:N+1]/np.sqrt(ns); ln = np.log(ns)
    def integrand(g):
        P = np.abs(np.sum(c*np.exp(-1j*g*ln)))**2 if not np.isscalar(g) else None
        return P
    mp.mp.dps = 20
    cmp_ = [mp.mpf(str(x)) for x in []]
    def f(g):
        g = float(g)
        if g == 0.0:
            Ah2 = (log(2)**2)*( (1-SQ2)**2 )  # limit |Ahat_-(i g)|^2 at 0: |(1-1)(...)|... compute via series
        z = np.exp(-1j*g*H)
        Am = (1-z)*(1-SQ2*z)/(1j*g) if g != 0 else (0)
        if g == 0:
            Am = complex(-H*(1-SQ2) - 0)  # derivative limit: d/ds[(1-2^{-s})(1-sqrt2 2^{-s})]/1 at 0 ... handled by avoiding g=0
        P = np.sum(c*np.exp(-1j*g*ln))
        return float(abs(Am)**2*abs(P)**2)
    # numeric integral over [eps, G] + exact trig tail
    G = 30000.0
    quadv = mp.quad(lambda g: f(g), [1e-6, 1.0, 10.0, 100.0, 1000.0, G])
    # tail: (1/2pi)*2*int_G^inf ; integrand = trig-poly/g^2
    w0, w1, w2 = 6+2*SQ2, 6+4*SQ2, 2*SQ2
    tail = mp.mpf(0)
    def cositail(w, G):
        # int_G^inf cos(w g)/g^2 dg
        w = abs(w)
        if w == 0: return mp.mpf(1)/G
        return mp.cos(w*G)/G - w*(mp.pi/2 - mp.si(w*G))
    for i in range(len(ns)):
        for j in range(len(ns)):
            b = ln[i]-ln[j]; coef = c[i]*c[j]
            t = w0*cositail(b, G) - 0.5*w1*(cositail(b+H, G)+cositail(b-H, G)) \
                + 0.5*w2*(cositail(b+2*H, G)+cositail(b-2*H, G))
            tail += coef*t
    rhs = float((quadv + tail)/mp.pi)  # (1/2pi)*2*int_0^inf
    return {'lhs_exact_energy': lhs, 'rhs_fourier': rhs, 'rel_dev': abs(lhs-rhs)/abs(lhs)}
OUT['plancherel_L103102_1'] = plancherel_check(5, 60)

# ---------- H = D + O, R(v) ----------
def gram_check(U, N):
    bU = mu.copy(); bU[:U+1] = 0.0
    hU = dconv(bU, eta, N)
    lhs = field_energy(hU, U, N, 4.0*N)
    ns = np.arange(U+1, N+1); c = hU[U+1:N+1]/np.sqrt(ns)
    def R(v):
        v = abs(v)
        if v <= H: return 3*H - (3+SQ2)*v
        if v <= 2*H: return -SQ2*(2*H - v)
        return 0.0
    D = 3*H*float(np.sum(c*c))
    O = 0.0
    for i in range(len(ns)):
        for j in range(len(ns)):
            if i == j: continue
            r = ns[i]/ns[j]
            if 0.25 < r < 4:
                O += c[i]*c[j]*R(log(r))
    gram = D + O
    return {'H_direct': lhs, 'D': D, 'O': O, 'D_plus_O': gram, 'rel_dev': abs(lhs-gram)/abs(lhs)}
OUT['gram_H_eq_D_plus_O'] = {f'U={u},N={n}': gram_check(u, n) for u, n in [(5, 80), (10, 300)]}

# R(v) vs direct overlap integral
def psi(u): return 1.0 if 0 < u < H else (-SQ2 if H < u < 2*H else 0.0)
devR = 0.0
for v in np.linspace(-1.6, 1.6, 41):
    direct = mp.quad(lambda u: psi(float(u))*psi(float(u)+float(v)), [0-abs(v), H, 2*H])
    v_ = abs(v)
    Rv = 3*H-(3+SQ2)*v_ if v_ <= H else (-SQ2*(2*H-v_) if v_ <= 2*H else 0.0)
    devR = max(devR, abs(float(direct)-Rv))
OUT['R_formula_max_dev'] = devR

# ---------- Type-I decay L-100310.4 ----------
typei = []
for Y in [10, 30, 100, 300, 1000, 3000, 10000]:
    ms = np.arange(max(1, int(Y/16)), int(Y)+2)
    S = float(np.sum([K1(Y/m)/sqrt(m) for m in ms]))
    typei.append({'Y': Y, 'S': S, 'S_times_Y^1.5': S*Y**1.5})
OUT['typeI_decay_L100310_4'] = typei

# ---------- W1 = T_U + B_U (L-100311.3) ----------
res_vd = {}
for X, U in [(800.0, 6), (5000.0, 17)]:
    N = int(X)
    W1 = B_direct(mu[:N+1], X)  # sum mu(n)/sqrt(n) K1(X/n)
    muU = mu.copy(); muU[U+1:] = 0.0
    bU = mu.copy(); bU[:U+1] = 0.0
    g = dconv(dconv(bU, bU, N), one, N)
    B = B_direct(g, X)
    # T_U = - sum_{a,b<=U} mu(a)mu(b)/sqrt(ab) sum_m K1(X/(abm))/sqrt(m)
    T = 0.0
    for a in range(1, U+1):
        if mu[a] == 0: continue
        for b in range(1, U+1):
            if mu[b] == 0: continue
            ab = a*b; Y = X/ab
            ms = np.arange(max(1, int(Y/16)), int(Y)+2)
            T -= mu[a]*mu[b]/sqrt(ab)*float(np.sum([K1(Y/m)/sqrt(m) for m in ms]))
    res_vd[f'X={X},U={U}'] = {'W1': W1, 'T_U': T, 'B_U': B, 'dev_W1_minus_T_minus_B': W1 - T - B}
OUT['vaughan_decomposition_L100311_3'] = res_vd

with open('/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad/GRAND/laneA2/results.json', 'w') as fh:
    json.dump(OUT, fh, indent=1, default=float)
print(json.dumps(OUT, indent=1, default=float))
