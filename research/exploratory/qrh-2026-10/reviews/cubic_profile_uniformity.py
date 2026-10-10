#!/usr/bin/env python3
"""cubic_profile_uniformity.py -- checks for reviews/CUBIC_PROFILE_UNIFORMITY.md (risk item 1 of
proposed/CUBIC_FOURTH_MOMENT/SKETCH.md: uniformity of Statement C in the complex profiles W_w).

Source read as untrusted data: pr908 31c706bb paper.tex, sha256 42a5ee0f...deac6a3 (external,
unreviewed).  Nothing here proves Statement C, Lemma 18.1 or any moment bound.

Labels.  EXACT = sympy / fractions identities.  MP = mpmath at the stated working precision
(ordinary high precision: NOT directed, NOT certified).  EMPIRICAL = double-precision numerics on a
finite range, with fitted exponents; a sanity check only.

Objects (SKETCH Sec. 2.4-2.5).
  phi(y) = rho(log2 y) - rho(log2 y - 1), rho a smooth step (0 for v <= -1, 1 for v >= 0), so that
  sum_j phi(y/2^j) = 1 exactly and supp phi = [1/2, 2].  In u = log y, g(u) := phi(e^u) = S(1-|u|/ln2),
  S(x) = 1/(1+exp(1/x - 1/(1-x))) on (0,1).
  W_w(y) = y^{-1/2-w} phi(y),  w = eps0 + i t,  eps0 = 1/log X.
  p_j(W) = sum_{k<=j} sup_u |d_u^k W(e^u)|            (paper.tex l. 1102-1108)
  ||W||_{J,sep} = int |W^(tau)| (1+|tau|)^J dtau       (l. 1112-1117)
  Phi_1(x) = (2 pi i)^{-1} int_(2) (2 pi x)^{-w} Gamma(1/2+w)/Gamma(1/2) dw/w   (SKETCH 2.2)
  V_lam(y) = y^{-1/2} phi(y) Phi_1(e^lam y)            (variant B, Sobolev in the scale)

Parts.
  A  EXACT: derivative formula, Gamma-weight integrals, sharp-cutoff and polynomial-kernel controls,
     homogeneity, X-exponent of the losses, Phi_1 = erfc(sqrt(2 pi x)) log-derivative identities.
  M  MP: Phi_1 Mellin integral vs erfc; explicit Stirling bound; nu-mass ~ 2 log log X; weighted
     w-integrals finite and below the explicit bound.
  E  EMPIRICAL: p_j(W_w) by two independent methods, fitted exponents (expect j), separation norms
     (expect J), Mellin decay of phi, variant-B seminorms bounded in lam; FAILING CONTROLS: a
     non-polynomial profile family and the wrong exponent j+1 are rejected.
"""
import math
import time

import numpy as np
import sympy as sp
import mpmath as mp

T0 = time.time()
RESULTS = []


def check(tag, label, ok, msg):
    RESULTS.append((tag, bool(ok)))
    print("%s %s %s : %s" % ("PASS" if ok else "FAIL", tag, label, msg), flush=True)


LN2 = math.log(2.0)
X_REF = 1e8
EPS0 = 1.0 / math.log(X_REF)

# ----------------------------------------------------------------------------------------------
# A. EXACT
# ----------------------------------------------------------------------------------------------
u, a, t, H = sp.symbols('u a t H', real=True)
gfun = sp.Function('g')
ok = True
for k in range(0, 7):
    lhs = sp.diff(sp.exp(-a * u) * gfun(u), u, k)
    rhs = sp.exp(-a * u) * sum(sp.binomial(k, i) * (-a) ** i * sp.diff(gfun(u), u, k - i)
                              for i in range(k + 1))
    ok &= sp.simplify(lhs - rhs) == 0
check("A1", "EXACT d_u^k[e^{-au} g] = e^{-au} sum_i C(k,i)(-a)^i g^(k-i), k <= 6", ok,
      "so p_j(W_w) <= 2^{1/2+eps0} p_j(phi) sum_k (1+|a|)^k, a = 1/2+w")

# A2 Gamma-weight tail integrals: int_0^oo t^H e^{-pi t/2} dt = Gamma(H+1) (2/pi)^{H+1}
tt = sp.symbols('tt', positive=True)
ok = True
for Hv in range(0, 41, 4):
    val = sp.integrate(tt ** Hv * sp.exp(-sp.pi * tt / 2), (tt, 0, sp.oo))
    ok &= sp.simplify(val - sp.gamma(Hv + 1) * (2 / sp.pi) ** (Hv + 1)) == 0
Hs = sp.symbols('Hs', positive=True)
gen = sp.integrate(tt ** Hs * sp.exp(-sp.pi * tt / 2), (tt, 0, sp.oo), conds='none')
ok &= sp.simplify(gen - sp.gamma(Hs + 1) * (2 / sp.pi) ** (Hs + 1)) == 0
check("A2", "EXACT int_0^oo t^H e^{-pi t/2} dt = Gamma(H+1)(2/pi)^{H+1} (H = 0..40 step 4 and symbolic H>0)",
      ok, "finite for every H: the Gamma weight beats every polynomial")

e0 = sp.symbols('e0', positive=True)
near = sp.integrate(1 / sp.sqrt(e0 ** 2 + tt ** 2), (tt, 0, 1)) * 2
diffA3 = sp.simplify((near - 2 * sp.asinh(1 / e0)).rewrite(sp.log))
check("A3", "EXACT int_{-1}^{1} dt/sqrt(eps0^2+t^2) = 2 asinh(1/eps0)",
      diffA3 == 0,
      "= 2 log(2 log X) + o(1) at eps0 = 1/log X  (sympy: %s)" % sp.simplify(near))

# A4 control: sharp cutoff kernel 1/w (Perron) -> int_1^T (1+t)^H / t dt diverges even at H = 0
T = sp.symbols('T', positive=True)
div0 = sp.limit(sp.integrate(1 / tt, (tt, 1, T)), T, sp.oo)
div2 = sp.limit(sp.integrate((1 + tt) ** 2 / tt, (tt, 1, T)), T, sp.oo)
check("A4", "EXACT CONTROL sharp cutoff (Mellin kernel 1/w, no Gamma factor): w-integral diverges",
      div0 == sp.oo and div2 == sp.oo, "H=0: %s, H=2: %s  (the route needs a smooth AFE weight)" % (div0, div2))

# A5 control: polynomially decaying kernel (1+t)^{-B}: int_1^oo (1+t)^{H-B} dt < oo iff B > H+1
ok = True
rows = []
for (Hv, Bv) in [(4, 6), (4, 5), (4, 4), (8, 10), (8, 9), (16, 18), (16, 17)]:
    v = sp.integrate((1 + tt) ** (Hv - Bv), (tt, 1, sp.oo))
    fin = v.is_finite
    rows.append("H=%d,B=%d:%s" % (Hv, Bv, "finite" if fin else "diverges"))
    ok &= (bool(fin) == (Bv > Hv + 1))
check("A5", "EXACT CONTROL kernel decay (1+|t|)^{-B} absorbs growth (1+|t|)^H iff B > H+1", ok,
      "; ".join(rows) + "  (a C^B-only partition would need B > 4J*+1)")

# A5b exact threshold for the Gamma weight: growth e^{c|t|} is absorbed by e^{-pi|t|/2} iff c < pi/2
cc = sp.symbols('cc', positive=True)
ok = True
rows = []
for cv in (sp.Rational(1, 10), sp.Rational(3, 2), sp.pi / 2 - sp.Rational(1, 1000), sp.pi / 2, sp.Rational(8, 5)):
    v = sp.integrate(sp.exp((cv - sp.pi / 2) * tt), (tt, 1, sp.oo))
    fin = bool(v.is_finite)
    ok &= (fin == bool(cv < sp.pi / 2))
    rows.append("c=%s:%s" % (cv, "finite" if fin else "diverges"))
check("A5b", "EXACT growth e^{c|t|} is integrable against e^{-pi|t|/2} iff c < pi/2 (true critical rate)", ok,
      "; ".join(rows) + "  (route (a) tolerates any sub-exponential and some exponential growth)")

# A6 homogeneity of bidegree (2,2)
c1, c2, s1, s2 = sp.symbols('c1 c2 s1 s2')
lhs = (c1 * s1 * c2 * s2) * sp.conjugate(c1 * s1 * c2 * s2)
rhs = (c1 * sp.conjugate(c1)) * (c2 * sp.conjugate(c2)) * (s1 * s2) * sp.conjugate(s1 * s2)
check("A6", "EXACT |S(c1 W1) S(c2 W2)|^2 = |c1|^2 |c2|^2 |S(W1) S(W2)|^2 (S linear in W)",
      sp.simplify(sp.expand(lhs - rhs)) == 0,
      "uniformity on {p_J <= 1} => bound C p_J(W1)^2 p_J(W2)^2 Z^{M+eps}")

# A7 X-exponent of the losses: L = log X; losses (L+1)^4 * asinh(L)^4 * 5^3 * C  -> exponent o(1)
L = sp.symbols('L', positive=True)
loss = 4 * sp.log(L + 1) + 4 * sp.log(sp.asinh(L)) + 3 * sp.log(5)
lim = sp.limit(loss / L, L, sp.oo)
check("A7", "EXACT log(losses)/log X -> 0 (dyadic (log X)^4, nu-mass (log log X)^4, S-part 5^3)",
      lim == 0, "limit = %s; X-exponent stays 1+eps" % lim)

# A8 exact upper constant: 1+|a| <= (5/2)(1+|t|) for a = 1/2+eps0+it, 0 <= eps0 <= 1
from fractions import Fraction as Fr
ok = all(Fr(1) + Fr(1, 2) + e + tv <= Fr(5, 2) * (1 + tv)
         for e in (Fr(0), Fr(1, 2), Fr(1)) for tv in (Fr(0), Fr(1, 3), Fr(1), Fr(7), Fr(1000)))
check("A8", "EXACT 1+|1/2+eps0+it| <= 3/2+eps0+|t| <= (5/2)(1+|t|) for eps0 <= 1 (grid, fractions)", ok,
      "p_j(W_w) <= 2^{3/2} (j+1) (5/2)^j p_j(phi) (1+|t|)^j")

# A9 Phi_1 = erfc(sqrt(2 pi x)): D = x d/dx gives D erfc(sqrt z) = -sqrt(z/pi) e^{-z}; D^k bounded
z = sp.symbols('z', positive=True)
f0 = sp.erfc(sp.sqrt(z))
D1 = sp.simplify(z * sp.diff(f0, z))
ok = sp.simplify(D1 + sp.sqrt(z / sp.pi) * sp.exp(-z)) == 0
Dk = f0
sups = []
for k in range(1, 6):
    Dk = sp.simplify(z * sp.diff(Dk, z))
    # Dk = P_k(sqrt z) e^{-z}: bounded on (0, oo) since limits at 0 and oo are finite
    l0 = sp.limit(Dk, z, 0, '+')
    li = sp.limit(Dk, z, sp.oo)
    ok &= (l0 == 0 and li == 0)
    fnum = sp.lambdify(z, Dk, 'mpmath')
    sups.append(max(abs(float(fnum(mp.mpf(zz)))) for zz in np.linspace(1e-6, 40, 4001)))
check("A9", "EXACT D^k erfc(sqrt z) -> 0 at z->0+ and z->oo (k=1..5), D erfc(sqrt z) = -sqrt(z/pi)e^{-z}",
      ok, "so sup_lam p_k(V_lam) < oo; grid sups of |D^k|: %s" % ", ".join("%.3f" % s for s in sups))

# ----------------------------------------------------------------------------------------------
# M. mpmath (high precision, not certified)
# ----------------------------------------------------------------------------------------------
mp.mp.dps = 30


def Phi1_mellin(x, c=1):
    f = lambda tv: (mp.mpf(2) * mp.pi * x) ** (-(c + 1j * tv)) * mp.gamma(0.5 + c + 1j * tv) \
        / mp.gamma(0.5) / (c + 1j * tv)
    return mp.quad(f, [-80, -20, -5, 0, 5, 20, 80]) / (2 * mp.pi)


errs = []
for x in (mp.mpf('0.003'), mp.mpf('0.05'), mp.mpf('0.3'), mp.mpf(1), mp.mpf(2.5)):
    v = Phi1_mellin(x)
    errs.append(abs(v - mp.erfc(mp.sqrt(2 * mp.pi * x))))
check("M1", "MP Phi_1(x) (Mellin integral on Re w = 1) = erfc(sqrt(2 pi x)), x in {.003,.05,.3,1,2.5}",
      max(errs) < mp.mpf('1e-20'), "max |diff| = %s (Phi_1 real; y^k Phi^(k) << (1+y)^{-A})" % mp.nstr(max(errs), 3))

# M2 explicit Stirling bound |Gamma(1/2+e+it)| <= sqrt(2pi) e^{1/3} (1+|t|)^e e^{-pi|t|/2}
worst = mp.mpf(0)
for e in (mp.mpf(0), EPS0, mp.mpf('0.25'), mp.mpf('0.5')):
    for tv in list(np.linspace(0, 5, 51)) + list(np.linspace(5, 400, 80)):
        tv = mp.mpf(tv)
        lhs = abs(mp.gamma(mp.mpf(0.5) + e + 1j * tv))
        rhs = mp.sqrt(2 * mp.pi) * mp.e ** (mp.mpf(1) / 3) * (1 + tv) ** e * mp.e ** (-mp.pi * tv / 2)
        worst = max(worst, lhs / rhs)
check("M2", "MP |Gamma(1/2+eps0+it)| <= sqrt(2pi) e^{1/3} (1+|t|)^{eps0} e^{-pi|t|/2}, eps0 in [0,1/2], |t|<=400",
      worst <= 1, "max ratio %s (proof: Stirling remainder |mu(s)| <= 1/(6|s|) for Re s > 0)" % mp.nstr(worst, 5))


def nu_weighted(H_, e):
    f = lambda tv: (1 + abs(tv)) ** H_ * abs(mp.gamma(mp.mpf(0.5) + e + 1j * tv)) / mp.sqrt(mp.pi) \
        / mp.sqrt(e ** 2 + tv ** 2)
    pts = [-120, -40, -10, -1, -e, 0, e, 1, 10, 40, 120]
    return mp.quad(f, pts)


masses = []
for ex in (8, 16, 32, 64, 128, 256):
    X = mp.mpf(10) ** ex
    e = 1 / mp.log(X)
    m0 = nu_weighted(0, e)
    masses.append((ex, m0, m0 - 2 * mp.log(mp.log(X))))
diffs = [d for (_, _, d) in masses]
incs = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]
ok = all(-mp.mpf('0.1') < d < 1 for d in diffs) and all(incs[i + 1] < incs[i] for i in range(len(incs) - 1))
check("M3", "MP nu-mass int |Gamma(1/2+w)/Gamma(1/2)| |dw/w| on Re w = 1/log X is 2 log log X + O(1)",
      ok, "; ".join("X=1e%d: mass %.4f (minus 2loglogX: %.4f)" % (ex, float(mv), float(dv))
                    for (ex, mv, dv) in masses)
      + "; increments shrink (O(eps0 log(1/eps0)) correction)")

rows = []
ok = True
e = mp.mpf(EPS0)
for Hv in (0, 4, 8, 16, 32):
    I = nu_weighted(Hv, e)
    bound = mp.sqrt(2) * mp.e ** (mp.mpf(1) / 3) * mp.mpf(2) ** (Hv + 2) * (
        mp.asinh(1 / e) + mp.gamma(Hv + 1) * (2 / mp.pi) ** (Hv + 1))
    ok &= mp.isfinite(I) and I <= bound
    rows.append("H=%d: I=%s <= %s" % (Hv, mp.nstr(I, 5), mp.nstr(bound, 5)))
check("M4", "MP int (1+|t|)^H dnu(w) finite and <= sqrt2 e^{1/3} 2^{H+2}[asinh(1/eps0) + Gamma(H+1)(2/pi)^{H+1}]",
      ok, "; ".join(rows))

# ----------------------------------------------------------------------------------------------
# E. EMPIRICAL (double precision)
# ----------------------------------------------------------------------------------------------


def S_step(x):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    out[x >= 1] = 1.0
    m = (x > 0) & (x < 1)
    xm = x[m]
    arg = np.clip(1.0 / xm - 1.0 / (1.0 - xm), -700, 700)
    out[m] = 1.0 / (1.0 + np.exp(arg))
    return out


def g_of_u(uu):
    return S_step(1.0 - np.abs(uu) / LN2)


def phi(y):
    y = np.asarray(y, dtype=float)
    v = np.log2(y)
    rho = lambda s: S_step(s + 1.0)
    return rho(v) - rho(v - 1.0)


rng = np.random.default_rng(20261010)
ys = np.exp(rng.uniform(-30, 30, 2000))
tot = sum(phi(ys / 2.0 ** j) for j in range(-60, 61))
supp_ok = np.all(phi(np.array([0.49, 0.4999, 2.0001, 2.2, 10.0])) == 0)
check("E0", "FLOAT partition of unity sum_j phi(y/2^j) = 1, supp phi in [1/2,2], phi(1) = 1, phi = g(log y)",
      np.max(np.abs(tot - 1)) < 1e-12 and supp_ok and abs(phi(np.array([1.0]))[0] - 1) < 1e-15
      and np.max(np.abs(phi(ys[(ys > 0.5) & (ys < 2)]) - g_of_u(np.log(ys[(ys > 0.5) & (ys < 2)])))) < 1e-12,
      "max |sum - 1| = %.1e" % np.max(np.abs(tot - 1)))

# spectral grid on u in [-1, 1) (g vanishes for |u| >= ln 2).  Spectral differentiation amplifies
# round-off by |k|^j, so Fourier modes below 1e-15 * max are zeroed first (noise floor filter).
NS = 2 ** 15
US = np.linspace(-1.0, 1.0, NS, endpoint=False)
DU = US[1] - US[0]
KS = 2 * np.pi * np.fft.fftfreq(NS, d=DU)
G_S = g_of_u(US)


def sup_derivs_spectral(f, jmax):
    """sup_u |d_u^k f(u)|, k = 0..jmax, by filtered spectral differentiation on the periodic grid."""
    F = np.fft.fft(f)
    F = np.where(np.abs(F) > 1e-15 * np.max(np.abs(F)), F, 0)
    return [float(np.max(np.abs(np.fft.ifft((1j * KS) ** k * F)))) for k in range(jmax + 1)]


# independent method: exact sympy derivatives of S, the A1 binomial formula, fine grid
xs = sp.symbols('xs')
S_expr = 1 / (1 + sp.exp(1 / xs - 1 / (1 - xs)))
S_der = [sp.lambdify(xs, sp.diff(S_expr, xs, k), 'numpy') for k in range(0, 6)]
UF = np.linspace(-LN2 * (1 - 1e-9), LN2 * (1 - 1e-9), 200001)


def g_der_exact(k):
    xv = 1.0 - np.abs(UF) / LN2
    with np.errstate(over='ignore', invalid='ignore', divide='ignore'):
        val = S_der[k](xv)
    val = np.nan_to_num(val, nan=0.0, posinf=0.0, neginf=0.0)   # overflow only where S^(k) ~ 0
    return val * (-np.sign(UF) / LN2) ** k                       # d^k/du^k of S(1 - |u|/ln2)


G_EX = [g_der_exact(k) for k in range(0, 6)]
SUP_G = [float(np.max(np.abs(G_EX[k]))) for k in range(6)]
P_PHI = np.cumsum(SUP_G)                                         # p_j(phi), j = 0..5

# third method for the t-independent inputs sup|g^(k)|: mpmath numerical differentiation
mp.mp.dps = 40
Sm = lambda x: 1 / (1 + mp.e ** (1 / x - 1 / (1 - x)))
mpsup = []
for k in range(1, 5):
    best = mp.mpf(0)
    for xv in np.linspace(0.02, 0.98, 1201):
        best = max(best, abs(mp.diff(Sm, mp.mpf(xv), k)))
    mpsup.append(float(best) / LN2 ** k)
relg = max(abs(a_ - b_) / b_ for a_, b_ in zip(mpsup, SUP_G[1:5]))
check("E1a", "MP/FLOAT sup|g^(k)|, k=1..4: exact-derivative grid vs mpmath.diff (1201 points)", relg < 1e-3,
      "sup|g^(k)| = " + ", ".join("%.4g" % v for v in SUP_G[:6]) + "; max rel diff %.1e" % relg)


def sup_derivs_exact(alpha, jmax):
    ex = np.exp(-alpha * UF)
    out = []
    for k in range(jmax + 1):
        s_ = sum(math.comb(k, i) * (-alpha) ** i * G_EX[k - i] for i in range(k + 1))
        out.append(float(np.max(np.abs(ex * s_))))
    return out


JMAX = 4
TGRID = [0, 1, 2, 3, 5, 7, 10, 14, 20, 28, 40, 50, 60, 80, 100, 140, 200]
P_SPEC, P_EX = {}, {}
maxrel = 0.0
for tv in TGRID:
    al = 0.5 + EPS0 + 1j * tv
    sd = sup_derivs_spectral(np.exp(-al * US) * G_S, JMAX)
    se = sup_derivs_exact(al, JMAX)
    maxrel = max(maxrel, max(abs(p - q) / q for p, q in zip(sd, se)))
    P_SPEC[tv] = np.cumsum(sd)
    P_EX[tv] = np.cumsum(se)
check("E1", "FLOAT p_j(W_w), j<=4, |Im w|<=200: filtered spectral FFT vs exact-derivative grid agree",
      maxrel < 1e-4, "max relative difference of the sup|d^k| values = %.1e" % maxrel)

print("      table p_j(W_w) (eps0 = 1/log 1e8 = %.4f; exact-derivative method):" % EPS0)
print("      t    " + "  ".join("p_%d" % j + " " * 8 for j in range(JMAX + 1)))
for tv in TGRID:
    print("      %-4d " % tv + "  ".join("%11.4e" % P_EX[tv][j] for j in range(JMAX + 1)))

# E2 explicit two-sided bracket: (1/2)(1+t)^j <= p_j(W_w) for t >= 50, and
#    p_j(W_w) <= 2^{1/2+eps0} (j+1) p_j(phi) (1 + |1/2+eps0+it|)^j  (A1 + A8)
ok = True
worst_up, worst_lo = 0.0, 1e9
for tv in TGRID:
    for j in range(JMAX + 1):
        up = 2 ** (0.5 + EPS0) * (j + 1) * P_PHI[j] * (1 + abs(0.5 + EPS0 + 1j * tv)) ** j
        worst_up = max(worst_up, P_EX[tv][j] / up)
        ok &= P_EX[tv][j] <= up
        if tv >= 50:
            worst_lo = min(worst_lo, P_EX[tv][j] / (1 + tv) ** j)
            ok &= P_EX[tv][j] >= 0.5 * (1 + tv) ** j
check("E2", "FLOAT bracket (1/2)(1+|t|)^j <= p_j(W_w) (t>=50) and p_j(W_w) <= 2^{1/2+eps0}(j+1)p_j(phi)(1+|a|)^j (all t)",
      ok, "max p_j/upper = %.3f; min p_j/(1+t)^j for t>=50 = %.3f" % (worst_up, worst_lo))


def local_slopes(P, ts, j):
    xs_, ss_ = [], []
    for t1, t2 in zip(ts[:-1], ts[1:]):
        ss_.append(math.log(P[t2][j] / P[t1][j]) / math.log((1 + t2) / (1 + t1)))
        xs_.append(1.0 / (1 + math.sqrt(t1 * t2)))
    return np.array(xs_), np.array(ss_)


def extrapolated_exponent(P, ts, j):
    """local log-log slopes s(t) fitted as s = gamma - c/(1+t); returns gamma (the t -> oo exponent)."""
    xv, sv = local_slopes(P, ts, j)
    A = np.vstack([np.ones_like(xv), xv]).T
    gamma_, c_ = np.linalg.lstsq(A, sv, rcond=None)[0]
    return gamma_, sv


FIT = [20, 28, 40, 50, 60, 80, 100, 140, 200]
FIT50 = [20, 28, 40, 50]
gam = [extrapolated_exponent(P_EX, FIT, j) for j in range(JMAX + 1)]
gam50 = [extrapolated_exponent(P_EX, FIT50, j) for j in range(JMAX + 1)]
check("E3", "EMPIRICAL fitted growth exponent of p_j(W_w) is j (local slopes extrapolated, t in [20,200]; |gamma-j|<0.1)",
      all(abs(gam[j][0] - j) < 0.1 for j in range(JMAX + 1)),
      "gamma: " + ", ".join("j=%d: %.3f" % (j, g_[0]) for j, g_ in enumerate(gam))
      + " | t<=50 only: " + ", ".join("%.3f" % g_[0] for g_ in gam50)
      + " | raw local slope at t~170: " + ", ".join("%.3f" % g_[1][-1] for g_ in gam))
# E3 (tolerance 0.1, linear 1/t model) FAILED in the run recorded in the review (j = 4: 4.112).
# E3b/E3c were added AFTER that run: the raw top-pair slope, and a model with a 1/t^2 term.


def extrapolated_exponent2(P, ts, j):
    xv, sv = local_slopes(P, ts, j)
    A = np.vstack([np.ones_like(xv), xv, xv ** 2]).T
    return np.linalg.lstsq(A, sv, rcond=None)[0][0]


gam2 = [extrapolated_exponent2(P_EX, FIT, j) for j in range(JMAX + 1)]
check("E3b", "EMPIRICAL (added after E3 failed) raw local slope of p_j(W_w) on [140,200] is j (|s-j| < 0.05)",
      all(abs(gam[j][1][-1] - j) < 0.05 for j in range(JMAX + 1)),
      "s = " + ", ".join("%.3f" % g_[1][-1] for g_ in gam))
check("E3c", "EMPIRICAL (added after E3 failed) quadratic-in-1/t extrapolation of the local slopes is j (|gamma-j| < 0.1)",
      all(abs(gam2[j] - j) < 0.1 for j in range(JMAX + 1)),
      "gamma = " + ", ".join("%.3f" % v for v in gam2))
check("E4", "EMPIRICAL FAILING CONTROL: exponent hypothesis j+1 rejected (|gamma-(j+1)| > 0.5 for every j)",
      all(abs(gam[j][0] - (j + 1)) > 0.5 for j in range(JMAX + 1)),
      "gamma - (j+1): " + ", ".join("%.2f" % (gam[j][0] - j - 1) for j in range(JMAX + 1)))

# polynomial-growth detector: the extrapolated exponent from [20,60] and from [60,200] must agree
gA = [extrapolated_exponent(P_EX, [20, 28, 40, 50, 60], j)[0] for j in range(JMAX + 1)]
gB = [extrapolated_exponent(P_EX, [60, 80, 100, 140, 200], j)[0] for j in range(JMAX + 1)]
P_BAD = {}
for tv in TGRID:
    al = 0.5 + EPS0 - tv / 10.0 + 1j * tv      # off the vertical line: |y^{-a}| up to 2^{t/10}
    P_BAD[tv] = np.cumsum(sup_derivs_spectral(np.exp(-al * US) * G_S, JMAX))
bA = [extrapolated_exponent(P_BAD, [20, 28, 40, 50, 60], j)[0] for j in range(JMAX + 1)]
bB = [extrapolated_exponent(P_BAD, [60, 80, 100, 140, 200], j)[0] for j in range(JMAX + 1)]
check("E5", "EMPIRICAL polynomial-growth detector accepts W_w (exponent on [20,60] vs [60,200] differ < 0.3)",
      max(abs(x_ - y_) for x_, y_ in zip(gA, gB)) < 0.3,
      "[20,60]: " + ", ".join("%.2f" % v for v in gA) + "; [60,200]: " + ", ".join("%.2f" % v for v in gB))
check("E6", "EMPIRICAL FAILING CONTROL: detector rejects y^{-1/2-eps0+t/10-it} phi (exponential growth)",
      min(abs(x_ - y_) for x_, y_ in zip(bA, bB)) > 1.0,
      "[20,60]: " + ", ".join("%.1f" % v for v in bA) + "; [60,200]: " + ", ".join("%.1f" % v for v in bB)
      + "; p_0 at t=200: %.2e" % P_BAD[200][0])

# separation norms ||W_w||_{J,sep} via zero-padded FFT (direct; the shift identity is not used)
PAD = 32
NP_ = NS * PAD
UP = (np.arange(NP_) - NP_ // 2) * DU
GP = g_of_u(UP)
TAU = 2 * np.pi * np.fft.fftfreq(NP_, d=DU)
DTAU = 2 * np.pi / (NP_ * DU)
JS = [0, 1, 2, 3]
SEP = {}
STS = [0, 10, 20, 28, 40, 50, 60, 80, 100, 140, 200]
for tv in STS:
    al = 0.5 + EPS0 + 1j * tv
    Fh = np.abs(np.fft.fft(np.exp(-al * UP) * GP)) * DU   # |hat w(tau)|; grid phase irrelevant
    SEP[tv] = [float(np.sum(Fh * (1 + np.abs(TAU)) ** J) * DTAU) for J in JS]
sep_g = [extrapolated_exponent(SEP, [20, 28, 40, 50, 60, 80, 100, 140, 200], J)[0] for J in JS]
peetre = all(SEP[tv][J] <= (1 + tv) ** J * SEP[0][J] * (1 + 1e-6) for tv in SEP for J in JS)
check("E7", "EMPIRICAL ||W_w||_{J,sep} has growth exponent J (|gamma-J| < 0.1) and is <= (1+|t|)^J ||W_eps0||_{J,sep}",
      all(abs(sep_g[J] - J) < 0.1 for J in JS) and peetre,
      "gamma: " + ", ".join("J=%d: %.3f" % (J, g_) for J, g_ in zip(JS, sep_g))
      + "; ||W_eps0||_{J,sep} = " + ", ".join("%.3g" % v for v in SEP[0]) + " (Lemma 4.5 allows J+3)")

# Mellin decay of phi itself (the dyadic-partition alternative): |M phi(1/2+it)| super-polynomial.
# |M phi| oscillates, so use the envelope E(t) = max_{s >= t} |M phi(1/2+is)|.
Fh = np.abs(np.fft.fft(np.exp(0.5 * UP) * GP)) * DU
pos = TAU >= 0
taus, mvals_all = TAU[pos], Fh[pos]
order_ = np.argsort(taus)
taus, mvals_all = taus[order_], mvals_all[order_]
env = np.maximum.accumulate(mvals_all[::-1])[::-1]
tvals = [10, 25, 50, 100, 200, 400, 800]
envv = [float(env[np.searchsorted(taus, tv)]) for tv in tvals]
loc = [math.log(envv[i + 1] / envv[i]) / math.log(tvals[i + 1] / tvals[i]) for i in range(len(tvals) - 1)]
check("E8", "EMPIRICAL envelope of |M phi(1/2+it)| decays faster than any fixed power (local slopes fall, last < -8)",
      all(loc[i + 1] < loc[i] + 0.5 for i in range(len(loc) - 1)) and loc[-1] < -8,
      "envelope " + ", ".join("t=%d:%.1e" % (tv, mv) for tv, mv in zip(tvals, envv))
      + "; local slopes " + ", ".join("%.1f" % s_ for s_ in loc))

# Variant B: V_lam(u) = e^{-u/2} g(u) erfc(sqrt(2 pi e^{lam+u})): seminorms bounded uniformly in lam.
from scipy.special import erfc as sp_erfc
lams = np.linspace(-30, 8, 153)
PV = []
for lam in lams:
    with np.errstate(over='ignore', under='ignore'):
        Vu = np.exp(-0.5 * US) * G_S * sp_erfc(np.sqrt(2 * np.pi * np.exp(lam + US)))
    PV.append(np.cumsum(sup_derivs_spectral(Vu, JMAX)))
PV = np.array(PV)
mx = PV.max(axis=0)
lim0 = np.cumsum(sup_derivs_spectral(np.exp(-0.5 * US) * G_S, JMAX))   # lam -> -oo limit
bound = [2 ** 0.5 * P_PHI[j] * sum(2.5 ** k for k in range(j + 1)) for j in range(JMAX + 1)]
check("E9", "EMPIRICAL variant B: p_j(V_lam) <= 2^{1/2} p_j(phi) sum_{k<=j}(5/2)^k for all lam in [-30,8] (j<=4)",
      np.all(PV <= np.array(bound)[None, :]) and np.max(np.abs(PV[0] - lim0) / lim0) < 1e-4
      and PV[-1][-1] < 1e-6 * mx[-1],
      "sup_lam p_j: " + ", ".join("%.4g" % v for v in mx) + "; bound: " + ", ".join("%.4g" % v for v in bound)
      + "; lam=-30 equals the lam->-oo limit y^{-1/2}phi to %.1e; lam=8: p_4 = %.1e"
      % (np.max(np.abs(PV[0] - lim0) / lim0), PV[-1][-1]))

print("SUMMARY %d/%d PASS (%.1f s)" % (sum(o for _, o in RESULTS), len(RESULTS), time.time() - T0))
