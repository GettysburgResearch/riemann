#!/usr/bin/env python3
"""Level-2 audit checks for paper2.tex (The Quasi-Riemann Hypothesis, 11/12):
Appendix B (l.3481-3650) and Outline (l.206-659) consistency.

Our own code; nothing from the OpenAI repository is run or imported.
Run:  python3 -I appB_outline_checks.py   (about 1-2 minutes)

Part A  Appendix B (Lemma B.1, the R-form (eq:smooth-pointwise), Lemma B.2, Lemma B.3).
Part B  Outline identities (Steps 2-5), with self-implemented Z[omega] arithmetic.
Part C  Outline scale/exponent algebra (sympy).
"""
import math, cmath, random, itertools, sys
import numpy as np
import sympy as sp

rng = np.random.default_rng(20261117)
random.seed(20261117)
FAILS = []
def report(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAILS.append(name)

# ----------------------------------------------------------------------------
# smooth cutoffs
# ----------------------------------------------------------------------------
def _psi(x):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    m = x > 0
    out[m] = np.exp(-1.0 / x[m])
    return out
def step(x):            # smooth 0->1 on [0,1]
    a = _psi(x); b = _psi(1 - np.asarray(x, dtype=float))
    return a / (a + b)
def bump(x, a, b, a2, b2):
    """smooth, =1 on [a2,b2], supported in [a,b] (a<a2<b2<b)"""
    x = np.asarray(x, dtype=float)
    return step((x - a) / (a2 - a)) * step((b - x) / (b - b2))

# ============================================================================
# PART A : Appendix B
# ============================================================================
print("=== Part A: Appendix B ===")

# grid in logarithmic coordinates; period P, M points
P, M = 2.0, 1024
yg = -0.35 + P * np.arange(M) / M          # covers [-0.35, 1.65): x in [0.70, 5.2)
tg = 2 * np.pi * np.fft.fftfreq(M, d=P / M)   # angular frequencies

def mellin_coeffs_2d(Kfun):
    """C[k1,k2] with K(e^y1,e^y2) = sum C e^{i t1 y1 + i t2 y2} on the period window.
    Relation to the paper's b(t): b(t) dt ~ C[k] (spacing 2 pi/P); b = (2pi)^{-d} * FT."""
    Y1, Y2 = np.meshgrid(yg, yg, indexing="ij")
    vals = Kfun(np.exp(Y1), np.exp(Y2))
    C = np.fft.fft2(vals) / (M * M)
    # phase correction for grid offset y0=-1.2
    ph = np.exp(-1j * np.add.outer(tg, tg) * yg[0])
    return C * ph

def eval_from_coeffs_2d(C, x, y):
    ex = np.exp(1j * np.outer(np.log(x), tg))   # (n, M)
    ey = np.exp(1j * np.outer(np.log(y), tg))
    return np.einsum("nk,kl,nl->n", ex, C, ey)

# ---- A1: Lemma B.1 representation (eq:smooth-separation), d=2 -----------------
I_lo, I_hi = 1.0, 2.0
def Wa(x): return bump(x, 1.02, 1.98, 1.35, 1.65) * (1 + 0.3 * np.sin(3 * x))
def Wb(x): return bump(x, 1.05, 1.95, 1.4, 1.6) * np.cos(x)
def K0(x, y, a=0.7):
    return Wa(x) * Wb(y) * np.exp(-a / (x * y))
C0 = mellin_coeffs_2d(K0)
xs = rng.uniform(0.75, 4.5, 400); ys = rng.uniform(0.75, 4.5, 400)
err = np.max(np.abs(eval_from_coeffs_2d(C0, xs, ys) - K0(xs, ys)))
report("A1 Lemma B.1: Mellin separation reconstructs K at 400 random (x,y) incl. outside the box", err < 1e-10, "max err %.2e" % err)

# ---- A2: pointwise bound in the proof of B.1: (1+|t|^2)^{q/2}|b(t)| <= (2pi)^{-d}||(1-Lap)^{q/2}(K o exp)||_{L^1}
# periodic version: |C_k| (1+|t_k|^2)^{q/2} <= P^{-2} ||(1-Lap)^{q/2} f||_{L^1(window)}; Laplacian by 2nd-order FD
Y1, Y2 = np.meshgrid(yg, yg, indexing="ij")
f = K0(np.exp(Y1), np.exp(Y2)); hstep = P / M
def lap(g):
    return ((np.roll(g, 1, 0) - 2 * g + np.roll(g, -1, 0)) + (np.roll(g, 1, 1) - 2 * g + np.roll(g, -1, 1))) / hstep ** 2
T1, T2 = np.meshgrid(tg, tg, indexing="ij")
ok = True; msg = []
g = f.copy()
for q in (2, 4, 6):
    g = g - lap(g)                       # (1-Lap)^{q/2} f
    L1 = np.sum(np.abs(g)) * hstep ** 2 / P ** 2
    lhs = np.max(np.abs(C0) * (1 + T1 ** 2 + T2 ** 2) ** (q / 2))
    msg.append("q=%d: max|C|(1+|t|^2)^{q/2}=%.3e <= %.3e" % (q, lhs, L1))
    ok &= lhs <= L1 * 1.02
report("A2 Lemma B.1 pointwise bound via (1-Laplacian)^{q/2} (q=2,4,6)", ok, "; ".join(msg))

# ---- A3: (eq:smooth-pointwise): R-uniform decay for K_R = W(x) F(R x) (d=1) ----
def mellin_coeffs_1d(fun):
    vals = fun(np.exp(yg))
    C = np.fft.fft(vals) / M * np.exp(-1j * tg * yg[0])
    return C
A_dec = 2.0
def Fdec(u):   # (1+u)^A |(u d/du)^m F| bounded, and sharp: F(u)= u^{1/4}(1+u)^{-A-1/4} ~ u^{-A}
    return u ** 0.25 * (1 + u) ** (-A_dec - 0.25)
def Wd(x): return bump(x, 1.02, 1.98, 1.2, 1.7)
ratios = []
for R in np.logspace(-3, 4, 29):
    C = mellin_coeffs_1d(lambda x: Wd(x) * Fdec(R * x))
    ratios.append(np.max(np.abs(C) * (1 + np.abs(tg)) ** 2) * (1 + R) ** A_dec)
ratios = np.array(ratios)
Rs = np.logspace(-3, 4, 29)
report("A3 (eq:smooth-pointwise): sup_t |b_R(t)|(1+|t|)^2 (1+R)^A bounded above uniformly in R in [1e-3,1e4], A=2",
       np.all(np.isfinite(ratios)) and ratios[Rs > 100].max() <= 1.5 * ratios[(Rs > 1) & (Rs <= 100)].max(),
       "ratio range [%.3e, %.3e], at R=1e4: %.3e" % (ratios.min(), ratios.max(), ratios[-1]))
# negative control: claiming A+1 decay should FAIL (ratios blow up like R)
ratios_bad = []
for R in np.logspace(1, 4, 7):
    C = mellin_coeffs_1d(lambda x: Wd(x) * Fdec(R * x))
    ratios_bad.append(np.max(np.abs(C)) * (1 + R) ** (A_dec + 1))
report("A3-ctl negative control: (1+R)^{A+1} weighting is unbounded (as it must be)",
       ratios_bad[-1] / ratios_bad[0] > 100, "growth factor %.1e" % (ratios_bad[-1] / ratios_bad[0]))

# ---- A4: Lemma B.2 structural identity and the Cauchy-Schwarz chain ----------
# I=[1,2] (kernel support), I_* = [0.7, 2.6]; V=1 on I, supported in int I_*
def V(x): return bump(x, 0.75, 2.5, 0.98, 2.02)
Rrows, Ncols = 6, 40
w = rng.uniform(0.2, 2.0, Rrows)
c = w * np.exp(2j * np.pi * rng.uniform(size=Rrows)) * rng.uniform(0.3, 1.0, Rrows)   # |c_r| <= w_r
a1 = rng.normal(size=(Rrows, Ncols)) + 1j * rng.normal(size=(Rrows, Ncols))
a2 = rng.normal(size=(Rrows, Ncols)) + 1j * rng.normal(size=(Rrows, Ncols))
x1 = rng.uniform(0.8, 2.4, (Rrows, Ncols)); x2 = rng.uniform(0.8, 2.4, (Rrows, Ncols))   # row-dependent points
avals = rng.uniform(0.0, 3.0, Rrows)
Kr = [ (lambda aa: (lambda x, y: K0(x, y, aa)))(aa) for aa in avals ]
LHS = 0
for r in range(Rrows):
    X1, X2 = np.meshgrid(x1[r], x2[r], indexing="ij")
    LHS += c[r] * np.sum(np.outer(a1[r], np.conj(a2[r])) * Kr[r](X1, X2))
Cs = [mellin_coeffs_2d(K) for K in Kr]
# S_{j,r}(U_s) for U_s(x) = V(x) x^{is}
S1 = np.array([[np.sum(a1[r] * V(x1[r]) * np.exp(1j * s * np.log(x1[r]))) for s in tg] for r in range(Rrows)])
S2 = np.array([[np.sum(a2[r] * V(x2[r]) * np.exp(1j * s * np.log(x2[r]))) for s in tg] for r in range(Rrows)])
# K_r(x,y) = sum C[k1,k2] x^{i s1} y^{i s2} = sum C[k1,k2] U_{s1}(x) conj(U_{-s2}(y)) on supp
neg = (-np.arange(M)) % M
REP = 0
for r in range(Rrows):
    REP += c[r] * np.einsum("k,kl,l->", S1[r], Cs[r], np.conj(S2[r][neg]))
err = abs(REP - LHS) / max(1, abs(LHS))
report("A4 Lemma B.2: Mellin/test-function representation of the coupled row-dependent sum", err < 1e-9,
       "LHS=%.6g%+.6gi  rel err %.1e" % (LHS.real, LHS.imag, err))
Bmaj = np.max(np.abs(np.array(Cs)), axis=0)
n1 = np.sqrt(np.sum(w[:, None] * np.abs(S1) ** 2, axis=0))
n2 = np.sqrt(np.sum(w[:, None] * np.abs(S2[:, neg]) ** 2, axis=0))
CSbound = np.einsum("k,kl,l->", n1, Bmaj, n2)
report("A4b Lemma B.2: |LHS| <= sum_{s,t} sup_r|b_r| sqrt(sum w|S1(U_s)|^2) sqrt(sum w|S2(U_t)|^2)",
       abs(LHS) <= CSbound * (1 + 1e-12), "|LHS|=%.4g  bound=%.4g" % (abs(LHS), CSbound))

# ---- A5: ||U_t||_{C^m(I_*)} << (1+|t|)^m  (analytic derivative formula) ------
from math import comb
def Vderivs(x, mmax, h=1e-3):
    # derivatives of V by high-order finite differences on a fine grid (sufficient for a ratio check)
    out = [V(x)]
    f = V
    for k in range(1, mmax + 1):
        f = (lambda g: (lambda z: (g(z + h) - g(z - h)) / (2 * h)))(f)
        out.append(f(x))
    return out
xx = np.linspace(0.7, 2.6, 2001)
ok = True; msg = []
for mm in (1, 2, 3):
    Vd = Vderivs(xx, mm)
    rat = []
    for t in (0, 5, 20, 80, 320):
        # d^j/dx^j [V x^{it}] = sum_k C(j,k) V^{(j-k)} (it)_k x^{it-k}
        best = 0
        for j in range(mm + 1):
            tot = 0
            for k in range(j + 1):
                fall = np.prod([1j * t - i for i in range(k)]) if k else 1
                tot = tot + comb(j, k) * Vd[j - k] * fall * xx ** (1j * t - k)
            best = max(best, np.max(np.abs(tot)))
        rat.append(best / (1 + t) ** mm)
    msg.append("m=%d:%s" % (mm, ",".join("%.2g" % v for v in rat)))
    ok &= rat[-1] <= 1.5 * rat[-2] and np.all(np.isfinite(rat))
report("A5 Lemma B.2: ||V x^{it}||_{C^m} / (1+|t|)^m stays bounded", ok, "; ".join(msg))

# ---- A6: the integral in (eq:kernel-bilinear-integral) is finite iff q > 2m+2 --
from scipy.integrate import quad
def bil_integral(m, q, Rmax):
    # 4 * int_{s,t>=0} ; s = r u, t = r(1-u), ds dt = r dr du ; u by Gauss-Legendre (exact, polynomial)
    xg, wg = np.polynomial.legendre.leggauss(40); ug = (xg + 1) / 2; wu = wg / 2
    def inner(r):
        return np.sum(wu * (1 + r * ug) ** m * (1 + r * (1 - ug)) ** m) * r / (1 + r) ** q
    val = 0.0; a0 = 0.0
    for b0 in np.concatenate(([1.0], np.logspace(0.5, np.log10(Rmax), 40))):
        val += quad(inner, a0, b0, limit=200)[0]; a0 = b0
    return 4 * val
ok = True; msg = []
for mm in (0, 1, 2, 3):
    q = 2 * mm + 4
    v1, v2 = bil_integral(mm, q, 1e4), bil_integral(mm, q, 1e8)
    w1, w2 = bil_integral(mm, 2 * mm + 2, 1e4), bil_integral(mm, 2 * mm + 2, 1e8)
    msg.append("m=%d: q=2m+4 %.5g->%.5g ; q=2m+2 %.4g->%.4g" % (mm, v1, v2, w1, w2))
    ok &= (v2 - v1) / v2 < 1e-3 and (w2 - w1) / w1 > 0.3
exact0 = 4 / 6.0
report("A6 Lemma B.2: q=2m+4 integral finite (exact 2/3 for m=0); q=2m+2 diverges like log", ok and abs(bil_integral(0, 4, 1e8) - exact0) < 1e-6,
       " | ".join(msg))

# ---- A7: Lemma B.3 (eq:integral-mean-square), randomized, plus equality case ---
ok = True; worst = 0
tt = np.linspace(-30, 30, 3001); dt = tt[1] - tt[0]
for trial in range(200):
    nI, nR = rng.integers(1, 4), rng.integers(1, 6)
    b = np.array([rng.uniform(0.1, 2) / (1 + np.abs(tt - rng.uniform(-5, 5))) ** 2 for _ in range(nI)])
    cc = b[:, None, :] * rng.uniform(0, 1, (nI, nR, len(tt))) * np.exp(2j * np.pi * rng.uniform(size=(nI, nR, len(tt))))
    F = rng.normal(size=(nI, nR, len(tt))) + 1j * rng.normal(size=(nI, nR, len(tt)))
    wr = rng.uniform(0, 2, nR)
    Mtot = np.sum(b) * dt
    lhs = np.sum(wr * np.abs(np.sum(cc * F, axis=(0, 2)) * dt) ** 2)
    rhs = Mtot * np.sum(b[:, None, :] * wr[None, :, None] * np.abs(F) ** 2) * dt
    worst = max(worst, lhs / rhs)
    ok &= lhs <= rhs * (1 + 1e-12)
# equality: c=b, F independent of (iota,t)
b = np.array([1 / (1 + tt ** 2), 2 / (1 + (tt - 1) ** 2)]); Fc = 1.7 - 0.4j
lhs = abs(np.sum(b) * dt * Fc) ** 2; rhs = np.sum(b) * dt * np.sum(b) * dt * abs(Fc) ** 2
report("A7 Lemma B.3: inequality on 200 random instances; equality when c=b and F constant",
       ok and abs(lhs - rhs) / rhs < 1e-12, "max lhs/rhs=%.3f; equality case ratio=%.15f" % (worst, lhs / rhs))

# ============================================================================
# PART B : Outline identities with Z[omega] arithmetic
# ============================================================================
print("=== Part B: outline identities (Z[omega]) ===")
SQ3 = math.sqrt(3.0)
OMC = complex(-0.5, SQ3 / 2)
def zmul(x, y):
    a, b = x; c2, d = y
    return (a * c2 - b * d, a * d + b * c2 - b * d)
def zconj(x): return (x[0] - x[1], -x[1])
def znorm(x): return x[0] * x[0] - x[0] * x[1] + x[1] * x[1]
def zc(x): return x[0] + x[1] * OMC
def zsub(x, y): return (x[0] - y[0], x[1] - y[1])
def zmod(x, m):
    n = znorm(m); z = zmul(x, zconj(m))
    q = (round(z[0] / n), round(z[1] / n))
    best = None
    for da in (-1, 0, 1):
        for db in (-1, 0, 1):
            r = zsub(x, zmul((q[0] + da, q[1] + db), m))
            if best is None or znorm(r) < znorm(best): best = r
    return best
def zdivides(y, x):
    n = znorm(y); z = zmul(x, zconj(y)); return z[0] % n == 0 and z[1] % n == 0
def zpow(x, e, m):
    r = (1, 0); x = zmod(x, m)
    while e:
        if e & 1: r = zmod(zmul(r, x), m)
        x = zmod(zmul(x, x), m); e >>= 1
    return r
UNITS = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]   # zeta6^k, zeta6 = 1+omega = e^{i pi/3}
def primary(x): return (x[0] - 1) % 3 == 0 and x[1] % 3 == 0
def to_primary(x):
    for u in UNITS:
        y = zmul(u, x)
        if primary(y): return y
    return None

# primary primes (excluding those above 2 and 3) up to norm bound
NB = 400
primes = []
for q in sp.primerange(5, NB + 1):
    if q % 3 == 1:
        found = None
        for a in range(-40, 41):
            for b in range(-40, 41):
                if znorm((a, b)) == q:
                    found = (a, b); break
            if found: break
        p1 = to_primary(found); p2 = to_primary(zconj(found))
        primes += [p1, p2]
    elif q % 3 == 2 and q * q <= NB:
        primes.append((-q, 0))
primes = sorted(set(primes), key=znorm)

SEXT_CACHE = {}
def sext_prime(u, p):
    """(u/p)_6 as exponent k (zeta6^k) or None if p|u."""
    key = (u, p)
    if key in SEXT_CACHE: return SEXT_CACHE[key]
    SEXT_CACHE[key] = _sext_prime(u, p)
    return SEXT_CACHE[key]
def _sext_prime(u, p):
    if zdivides(p, u): return None
    r = zpow(u, (znorm(p) - 1) // 6, p)
    for k, uu in enumerate(UNITS):
        if zdivides(p, zsub(r, uu)): return k
    raise ValueError("no sixth root found")
def chi(u, plist, power=1):
    """chi_n(u)^power as complex, n = prod plist (primary primes, squarefree or not)."""
    val = 1 + 0j
    for p in plist:
        k = sext_prime(u, p)
        if k is None: return 0j
        val *= cmath.exp(2j * math.pi * k * power / 6)
    return val
def e_add(z): return cmath.exp(4j * math.pi * z.imag / SQ3)
def resid_system(n):
    """complete residue system of O mod n: HNF basis (A,x),(0,B) of the lattice nO in (a,b)-coordinates."""
    v1 = n; v2 = zmul(n, (0, 1))
    g, u, w_ = sp.gcdex(v1[0], v2[0])[2], sp.gcdex(v1[0], v2[0])[0], sp.gcdex(v1[0], v2[0])[1]
    g = int(g); u = int(u); w_ = int(w_)
    r2 = (v2[0] // g * v1[0] - v1[0] // g * v2[0], v2[0] // g * v1[1] - v1[0] // g * v2[1])
    assert r2[0] == 0
    A = abs(g); B = abs(r2[1])
    assert A * B == znorm(n), (n, A, B)
    return [(a, b) for a in range(A) for b in range(B)]

def gauss(j, plist):
    """gamma_j(n) = N(n)^{-1/2} sum_{x mod n} chi_n(x)^j e(x/n)."""
    n = (1, 0)
    for p in plist: n = zmul(n, p)
    N = znorm(n); nc = zc(n)
    reps = resid_system(n)
    assert len(reps) == N
    tot = 0j
    for x in reps:
        cv = chi(x, plist, j)
        if cv != 0:
            tot += cv * e_add(zc(x) / nc)
    return tot / math.sqrt(N)

# ---- B1: classical Jacobi identity (outline l.318) ------------------------------
def jacobi_gauss_ok(m):
    s = sum(int(sp.jacobi_symbol(x, m)) * cmath.exp(2j * math.pi * x / m) for x in range(m))
    return abs((s / math.sqrt(m)) ** 2 - int(sp.jacobi_symbol(-1, m))) < 1e-8
ms = [m for m in range(1, 1200, 2) if sp.ntheory.factor_.core(m) == m]
bad = [m for m in ms if not jacobi_gauss_ok(m)]
report("B1 outline l.318: (-1/m) = (m^{-1/2} sum (x/m) e^{2 pi i x/m})^2, odd squarefree m<1200", not bad,
       "%d values, failures %s" % (len(ms), bad[:5]))

# ---- B2: six units represent (O/3)^x ; quadratic/cubic symbols = chi^3, chi^2 ----
cls = {zmod(u, (3, 0)) for u in UNITS}
report("B2a outline l.246-247: the six units are distinct mod 3 (hence all of (O/3)^x, order 6)", len(cls) == 6)
ok = True; cnt = 0
for p in primes[:40]:
    N = znorm(p)
    for _ in range(12):
        u = (random.randint(-50, 50), random.randint(-50, 50))
        if zdivides(p, u): continue
        k = sext_prime(u, p)
        r2 = zpow(u, (N - 1) // 2, p); r3 = zpow(u, (N - 1) // 3, p)
        k2 = [i for i, uu in enumerate(UNITS) if zdivides(p, zsub(r2, uu))][0]
        k3 = [i for i, uu in enumerate(UNITS) if zdivides(p, zsub(r3, uu))][0]
        ok &= (k2 == (3 * k) % 6) and (k3 == (2 * k) % 6); cnt += 1
report("B2b outline l.263: (u/p)_2 = chi_p(u)^3 and (u/p)_3 = chi_p(u)^2", ok, "%d cases" % cnt)
ok = True; cnt = 0
for p in primes[:25]:
    p6 = (1, 0)
    for _ in range(6): p6 = zmul(p6, p)
    for qn in primes[:25]:
        v = chi(p6, [qn]); ok &= abs(v - (0 if qn == p else 1)) < 1e-12; cnt += 1
report("B2c outline l.284 / l.699: chi_n(p^6) = 1_{p not | n}", ok, "%d (p,n) pairs" % cnt)

# ---- B3: outline l.322 identity mu(n) gamma_{-1}(n) = chi_n(-1) G(n)^{-1} conj(alpha) gamma_2,
#          G(n) = conj(chi_n(4)) gamma_3(n), for squarefree primary n (1 or 2 prime factors)
def alpha(plist):
    n = (1, 0)
    for p in plist: n = zmul(n, p)
    z = zc(n); return z / abs(z)
tests = [[p] for p in primes[:14]] + [[primes[i], primes[j]] for i in range(0, 8) for j in range(i + 1, 8) if znorm(primes[i]) * znorm(primes[j]) < 700]
worst = 0
for pl in tests:
    mu = (-1) ** len(pl)
    gm1 = gauss(-1, pl); g2 = gauss(2, pl); g3 = gauss(3, pl)
    G = np.conj(chi((4, 0), pl)) * g3
    lhs = mu * gm1
    rhs = chi((-1, 0), pl) / G * np.conj(alpha(pl)) * g2
    worst = max(worst, abs(lhs - rhs))
report("B3 outline l.322 (= eq:convert2 with eq:g): mu*gamma_{-1} = chi_n(-1) G^{-1} conj(alpha) gamma_2",
       worst < 1e-9, "%d n (primes and 2-prime products, split+inert), max err %.1e" % (len(tests), worst))

# ---- B4: cube completion (eq:intro-cube-completion), inversion (eq:intro-cube-inversion),
#          long-part regrouping (l.494-510), with the c_theta normalization of (eq:intro-completed-theta-sum)
# columns n squarefree primary from the prime list; coefficient a(n)=conj(alpha(n)) gamma_2(n) (genuine for
# primes; for products use the twisted multiplicativity gamma_2(ab)=gamma_2(a)gamma_2(b)chi_a(b)^2 chi_b(a)^2,
# itself spot-checked here against direct summation).
pr_small = [p for p in primes if znorm(p) <= 200]
g2p = {p: gauss(2, [p]) for p in pr_small}
# spot-check twisted multiplicativity
worst = 0
for i in range(5):
    for j in range(i + 1, 7):
        a_, b_ = pr_small[i], pr_small[j]
        if znorm(a_) * znorm(b_) > 800: continue
        d = gauss(2, [a_, b_]); f = g2p[a_] * g2p[b_] * chi(b_, [a_], 2) * chi(a_, [b_], 2)
        worst = max(worst, abs(d - f))
report("B4a gamma_2(ab)=gamma_2(a)gamma_2(b)chi_a(b)^2chi_b(a)^2 (helper for B4)", worst < 1e-9, "max err %.1e" % worst)

def sqfree_lists(maxN):
    out = [[]]
    def rec(start, cur, N):
        for i in range(start, len(pr_small)):
            p = pr_small[i]; NN = N * znorm(p)
            if NN > maxN: break
            out.append(cur + [p]); rec(i + 1, cur + [p], NN)
    rec(0, [], 1)
    return out
Xmax = 2600.0
cols = sqfree_lists(int(Xmax * 2.2))
def a_coef(pl):
    val = np.conj(alpha(pl)) if pl else 1.0
    g = 1.0 + 0j
    for p in pl: g *= g2p[p]
    for i in range(len(pl)):
        for j in range(i + 1, len(pl)):
            g *= chi(pl[j], [pl[i]], 2) * chi(pl[i], [pl[j]], 2)
    return val * g
acoef = [a_coef(pl) for pl in cols]
Ncol = [math.prod(znorm(p) for p in pl) for pl in cols]
def Uw(y): return float(bump(np.array([y]), 0.5, 2.0, 0.8, 1.6)[0] * (1 + 0.2 * y))
hrows = [(2, 1), (5, 3), (7, 0), (4, 9), (-1, 0), (11, 2)]
# cube indices b: primary, built from small primes (with repetition)
blist = [[]] + [[p] for p in pr_small if znorm(p) ** 3 <= 2 * Xmax] + [[p, q] for p in pr_small for q in pr_small
          if znorm(p) <= znorm(q) and (znorm(p) * znorm(q)) ** 3 <= 2 * Xmax]
blist = [b for b in blist if b == sorted(b, key=znorm)]
def bval(bl):
    n = (1, 0)
    for p in bl: n = zmul(n, p)
    return n
def Ph(h, Y):          # P_h(Y) = Y^{-1/2} sum_n a(n) chi_n(h) U(N(n)/Y)
    tot = 0j
    for pl, a, N in zip(cols, acoef, Ncol):
        u = Uw(N / Y)
        if u == 0: continue
        tot += a * chi(h, pl) * u
    return tot / math.sqrt(Y)
def w_h(h, bl):        # conj(alpha(b))^3 xi(b)^3 chi_b(h)^3, xi trivial
    bb = bval(bl); al = zc(bb) / abs(zc(bb))
    return np.conj(al) ** 3 * chi(h, bl, 3)
def Th_direct(h, X):
    # (eq:intro-completed-theta-sum) with c_theta(nb^3)=3^{5/2}|b| conj(chi_n(lambda)^2) gamma_2(n)
    lam = (1, 2)
    tot = 0j
    for bl in blist:
        bb = bval(bl); Nb = znorm(bb)
        for pl, a, N in zip(cols, acoef, Ncol):
            u = Uw(N * Nb ** 3 / X)
            if u == 0: continue
            nb3 = pl + bl * 3
            ctheta = 3 ** 2.5 * math.sqrt(Nb) * np.conj(chi(lam, pl, 2)) * (a / np.conj(alpha(pl)) if pl else 1.0)
            n_el = bval(pl); m_el = zmul(n_el, zmul(bb, zmul(bb, bb)))
            al = zc(m_el) / abs(zc(m_el))
            tot += ctheta * np.conj(al) * chi(lam, nb3, 2) * chi(h, nb3) * u
    return tot / (3 ** 2.5 * math.sqrt(X))
worst_c = 0; worst_i = 0; worst_l = 0; maxlong = 0
for h in hrows[:4]:
    X = Xmax
    T = Th_direct(h, X)
    Tc = sum(w_h(h, bl) / znorm(bval(bl)) * Ph(h, X / znorm(bval(bl)) ** 3) for bl in blist)
    worst_c = max(worst_c, abs(T - Tc))
    # inversion: P_h(X) = sum_d mu(d) w_h(d)/N(d) T_h(X/N(d)^3), d squarefree in blist
    sq = [bl for bl in blist if len(set(bl)) == len(bl)]
    Tfun = lambda Y: sum(w_h(h, bl) / znorm(bval(bl)) * Ph(h, Y / znorm(bval(bl)) ** 3) for bl in blist)
    Pinv = sum((-1) ** len(dl) * w_h(h, dl) / znorm(bval(dl)) * Tfun(X / znorm(bval(dl)) ** 3) for dl in sq)
    worst_i = max(worst_i, abs(Pinv - Ph(h, X)))
    # long part regrouping with several cutoffs Hc
    for Hc in (1.5, 7.5, 10.0):
        long1 = sum((-1) ** len(dl) * w_h(h, dl) / znorm(bval(dl)) * Tfun(X / znorm(bval(dl)) ** 3)
                    for dl in sq if znorm(bval(dl)) > Hc)
        long2 = 0j
        for bl in blist:
            bb = bval(bl); Nb = znorm(bb)
            if Nb <= Hc: continue
            # divisors d of b (squarefree, as sub-multisets), N(d) > Hc
            ds = set()
            for r in range(len(bl) + 1):
                for comb_ in itertools.combinations(range(len(bl)), r):
                    sub = tuple(sorted({tuple(bl[i]) for i in comb_}))
                    if len(sub) == r: ds.add(sub)
            s = sum((-1) ** len(dd) for dd in ds if math.prod(znorm(p) for p in dd) > Hc)
            al = zc(bb) / abs(zc(bb))
            beta0 = np.conj(al) ** 3 * s
            long2 += beta0 * chi(h, bl, 3) / Nb * Ph(h, X / Nb ** 3)

        worst_l = max(worst_l, abs(long1 - long2)); maxlong = max(maxlong, abs(long1))

report("B4b outline (eq:intro-completed-theta-sum)=(eq:intro-cube-completion): T_h = sum_b w_h(b)/N(b) P_h(X/N(b)^3)",
       worst_c < 1e-9, "4 rows h, X=%g, %d columns, %d cube indices, max err %.1e" % (Xmax, len(cols), len(blist), worst_c))
report("B4c outline (eq:intro-cube-inversion): P_h(X) = sum_d mu(d) w_h(d)/N(d) T_h(X/N(d)^3)", worst_i < 1e-9,
       "max err %.1e" % worst_i)
report("B4d outline l.494-510: long-part regrouping with beta_0(b)", worst_l < 1e-9, "H_c in {1.5,7.5,10}, max err %.1e, max |P_long| = %.3e (nontrivial)" % (worst_l, maxlong))

# ============================================================================
# PART C : outline scale / exponent algebra
# ============================================================================
print("=== Part C: outline scale algebra (sympy) ===")
D, th, Hs, X, L, Nb, E1 = sp.symbols("D vartheta H X L N_b Eprime", positive=True)
H = D ** (1 + th)
Y = H ** sp.Rational(1, 6)
t1 = sp.simplify(sp.log(D * H / Y, D)); t2 = sp.simplify(sp.log(D ** 2 / Y ** 2, D))
report("C1 (eq:intro-extraction)/(eq:prime-extract): exponents 11/6+5th/6 and 5/3-th/3",
       sp.simplify(t1 - (sp.Rational(11, 6) + 5 * th / 6)) == 0 and sp.simplify(t2 - (sp.Rational(5, 3) - th / 3)) == 0,
       "got %s, %s" % (sp.expand(t1), sp.expand(t2)))
# dominance for th in (0,1/10]: max exponent /2 = 11/12 + 5th/12
diff = sp.simplify(t1 - t2)
report("C2 first term dominates for all th>0 (so A_1 << D^{11/12+5th/12})", sp.simplify(diff - (sp.Rational(1, 6) + 7 * th / 6)) == 0,
       "difference = %s" % sp.expand(diff))
# Step 3: (H/D) * D^2 = D*H
report("C3 (eq:intro-poisson-comparison)+(eq:intro-dual-ms) give D H", sp.simplify((H / D) * D ** 2 - D * H) == 0)
# Step 5 transfer algebra
Lb = X / Nb ** 3
Yen = X * Lb / Hs
Hp = sp.simplify(Lb ** 2 / Yen)
report("C4 l.580: H' = L_b^2/Y = H L_b / X = H/N(b)^3", sp.simplify(Hp - Hs * Lb / X) == 0 and sp.simplify(Hp - Hs / Nb ** 3) == 0)
expr = sp.simplify((Hs / Lb ** 2) * (Yen * Lb + Yen * E1))
report("C5 l.591: (H/L_b^2)(Y L_b + Y E') = X + (X/L_b) E'", sp.simplify(expr - (X + X / Lb * E1)) == 0)
report("C6 l.604-607: H'/X' = H/X", sp.simplify(Hp / Lb - Hs / X) == 0)
# contraction: N(b)^3 > Hc^3 = X^2/H^2  =>  H' < H (H/X)^2  (checked as an implication on random samples)
ok = True
for _ in range(20000):
    x = 10 ** rng.uniform(0, 12); hh = 10 ** rng.uniform(0, 12)
    if hh * hh <= x: continue           # empty supremum case
    hc3 = min(x, x * x / hh / hh)
    nb3 = hc3 * 10 ** rng.uniform(1e-9, 6)
    if x / nb3 <= 1: continue           # L_b > 1 required
    ok &= (hh / nb3) < hh * (hh / x) ** 2 * (1 + 1e-12)
report("C7 l.628-630: N(b)^3 > H_c^3, L_b>1  =>  H' < H (H/X)^2", ok)
# short part cutoff: H^2 Hc^3/X <= X  <=>  Hc <= (X/H)^{2/3}; basic scales
Hc = sp.Min(X ** sp.Rational(1, 3), (X / Hs) ** sp.Rational(2, 3))
val = (D / D ** (1 - th)) ** sp.Rational(2, 3)
report("C8 l.483-487: at X=D, H=D^{1-th}: (X/H)^{2/3} = D^{2th/3} < D^{1/3} for th<1/2",
       sp.simplify(val - D ** (2 * th / 3)) == 0)
# Step 1/2: rows p^6 have norm <= Y^6 = H
report("C9 l.289/l.708: N(p^6) <= Y^6 = H", sp.simplify(Y ** 6 - H) == 0)

print()
print("FAILURES:", FAILS if FAILS else "none")
sys.exit(1 if FAILS else 0)
