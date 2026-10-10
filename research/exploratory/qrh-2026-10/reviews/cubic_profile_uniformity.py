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
ok = True
for X in (mp.mpf(10) ** 8, mp.mpf(10) ** 16, mp.mpf(10) ** 32, mp.mpf(10) ** 64):
    e = 1 / mp.log(X)
    m0 = nu_weighted(0, e)
    masses.append((X, m0, m0 - 2 * mp.log(mp.log(X))))
diffs = [d for (_, _, d) in masses]
ok = max(diffs) - min(diffs) < mp.mpf('0.05')
check("M3", "MP nu-mass int |Gamma(1/2+w)/Gamma(1/2)| |dw/w| on Re w = 1/log X equals 2 log log X + O(1)",
      ok, "; ".join("X=1e%d: mass %.4f, minus 2loglogX %.4f" % (int(mp.log10(Xv)), float(mv), float(dv))
                    for (Xv, mv, dv) in masses))

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

# spectral grid on u in [-1, 1) (g vanishes for |u| >= ln 2)
NS = 2 ** 15
US = np.linspace(-1.0, 1.0, NS, endpoint=False)
DU = US[1] - US[0]
KS = 2 * np.pi * np.fft.fftfreq(NS, d=DU)
G_S = g_of_u(US)


def sup_derivs_spectral(alpha, jmax, gvals=G_S):
    """sup_u |d_u^k [e^{-alpha u} g(u)]|, k = 0..jmax, alpha complex (spectral differentiation)."""
    f = np.exp(-alpha * US) * gvals
    F = np.fft.fft(f)
    return [float(np.max(np.abs(np.fft.ifft((1j * KS) ** k * F)))) for k in range(jmax + 1)]


# independent method: exact sympy derivatives of S, binomial formula on a fine grid
xs = sp.symbols('xs')
S_expr = 1 / (1 + sp.exp(1 / xs - 1 / (1 - xs)))
S_der = [sp.lambdify(xs, sp.diff(S_expr, xs, k), 'numpy') for k in range(0, 6)]
UF = np.linspace(-LN2 * (1 - 1e-9), LN2 * (1 - 1e-9), 200001)


def g_der_exact(k):
    xv = 1.0 - np.abs(UF) / LN2
    with np.errstate(over='ignore', invalid='ignore', divide='ignore'):
        val = S_der[k](xv)
    val = np.nan_to_num(val, nan=0.0, posinf=0.0, neginf=0.0)
    # d/du of S(1 - |u|/ln2) = (-sign(u)/ln2)^k S^(k)
    return val * (-np.sign(UF) / LN2) ** k


G_EX = [g_der_exact(k) for k in range(0, 6)]


def sup_derivs_exact(alpha, jmax):
    ex = np.exp(-alpha * UF)
    out = []
    for k in range(jmax + 1):
        s = sum(math.comb(k, i) * (-alpha) ** i * G_EX[k - i] for i in range(k + 1))
        out.append(float(np.max(np.abs(ex * s))))
    return out


JMAX = 4
TGRID = [0, 1, 2, 3, 5, 7, 10, 14, 20, 28, 40, 50, 60]
P_SPEC, P_EX = {}, {}
maxrel = 0.0
for tv in TGRID:
    al = 0.5 + EPS0 + 1j * tv
    sd = sup_derivs_spectral(al, JMAX)
    se = sup_derivs_exact(al, JMAX)
    maxrel = max(maxrel, max(abs(p - q) / q for p, q in zip(sd, se)))
    P_SPEC[tv] = np.cumsum(sd)
    P_EX[tv] = np.cumsum(se)
check("E1", "FLOAT p_j(W_w), j<=4, |Im w|<=60: spectral FFT vs exact-derivative grid agree", maxrel < 1e-5,
      "max relative difference of the sup|d^k| values = %.1e" % maxrel)

print("      table p_j(W_w) (eps0 = 1/log 1e8 = %.4f):" % EPS0)
print("      t    " + "  ".join("p_%d" % j + " " * 8 for j in range(JMAX + 1)))
for tv in TGRID:
    print("      %-4d " % tv + "  ".join("%11.4e" % P_SPEC[tv][j] for j in range(JMAX + 1)))


def fit_slope(tvals, vals):
    xv = np.log1p(np.array(tvals, dtype=float))
    yv = np.log(np.array(vals, dtype=float))
    A = np.vstack([xv, np.ones_like(xv)]).T
    sl, ic = np.linalg.lstsq(A, yv, rcond=None)[0]
    return sl


def local_slope(P, t1, t2, j):
    return math.log(P[t2][j] / P[t1][j]) / math.log((1 + t2) / (1 + t1))


FIT = [20, 28, 40, 50, 60]
slopes = [fit_slope(FIT, [P_SPEC[tv][j] for tv in FIT]) for j in range(JMAX + 1)]
ratios = [(min(P_SPEC[tv][j] / (1 + tv) ** j for tv in TGRID), max(P_SPEC[tv][j] / (1 + tv) ** j for tv in TGRID))
          for j in range(JMAX + 1)]
check("E2", "EMPIRICAL fitted exponent of p_j(W_w) in (1+|t|) over t in [20,60] is j (|slope - j| < 0.15)",
      all(abs(slopes[j] - j) < 0.15 for j in range(JMAX + 1)),
      "slopes " + ", ".join("j=%d: %.3f" % (j, s) for j, s in enumerate(slopes)))
check("E3", "EMPIRICAL p_j(W_w)/(1+|t|)^j bounded above and below on t in [0,60] (max/min < 12)",
      all(hi / lo < 12 for lo, hi in ratios),
      "; ".join("j=%d: [%.3g, %.3g]" % (j, lo, hi) for j, (lo, hi) in enumerate(ratios)))
check("E4", "EMPIRICAL FAILING CONTROL: exponent hypothesis j+1 rejected (|slope-(j+1)| > 0.5 for every j)",
      all(abs(slopes[j] - (j + 1)) > 0.5 for j in range(JMAX + 1)),
      "the fit discriminates exponents; slope - (j+1): " + ", ".join("%.2f" % (slopes[j] - j - 1) for j in range(JMAX + 1)))

# polynomial-growth detector: local slopes on [20,40] and [40,60] must agree
pol_gap = [abs(local_slope(P_SPEC, 40, 60, j) - local_slope(P_SPEC, 20, 40, j)) for j in range(JMAX + 1)]
P_BAD = {}
for tv in TGRID:
    al = 0.5 + EPS0 - tv / 10.0 + 1j * tv      # off the vertical line: |y^{-a}| up to 2^{t/10}
    P_BAD[tv] = np.cumsum(sup_derivs_spectral(al, JMAX))
bad_gap = [abs(local_slope(P_BAD, 40, 60, j) - local_slope(P_BAD, 20, 40, j)) for j in range(JMAX + 1)]
check("E5", "EMPIRICAL polynomial-growth detector accepts W_w (local-slope drift < 0.3)",
      max(pol_gap) < 0.3, "drift per j: " + ", ".join("%.3f" % d for d in pol_gap))
check("E6", "EMPIRICAL FAILING CONTROL: detector rejects y^{-1/2-eps0+t/10-it} phi (exponential growth)",
      min(bad_gap) > 0.5, "drift per j: " + ", ".join("%.3f" % d for d in bad_gap)
      + "; p_0 at t=60: %.3e" % P_BAD[60][0])

# separation norms ||W_w||_{J,sep} via zero-padded FFT (no use of the shift identity)
PAD = 32
NP_ = NS * PAD
UP = (np.arange(NP_) - NP_ // 2) * DU
GP = g_of_u(UP)
TAU = 2 * np.pi * np.fft.fftfreq(NP_, d=DU)
DTAU = 2 * np.pi / (NP_ * DU)
JS = [0, 1, 2, 3]
SEP = {}
for tv in [0, 5, 10, 20, 30, 40, 50, 60]:
    al = 0.5 + EPS0 + 1j * tv
    f = np.exp(-al * UP) * GP
    # hat w(tau) = int f(u) e^{-i tau u} du; phase from the grid offset does not affect |.|
    Fh = np.abs(np.fft.fft(f)) * DU
    SEP[tv] = [float(np.sum(Fh * (1 + np.abs(TAU)) ** J) * DTAU) for J in JS]
sep_sl = [fit_slope([20, 30, 40, 50, 60], [SEP[tv][J] for tv in [20, 30, 40, 50, 60]]) for J in JS]
# shift identity consequence ||W_w||_{J,sep} <= (1+|t|)^J ||W_{eps0}||_{J,sep}
peetre = all(SEP[tv][J] <= (1 + tv) ** J * SEP[0][J] * (1 + 1e-6) for tv in SEP for J in JS)
check("E7", "EMPIRICAL ||W_w||_{J,sep} grows with exponent J (|slope-J| < 0.2) and obeys <= (1+|t|)^J ||W_eps0||_{J,sep}",
      all(abs(sep_sl[J] - J) < 0.2 for J in JS) and peetre,
      "slopes " + ", ".join("J=%d: %.3f" % (J, s) for J, s in zip(JS, sep_sl))
      + "; Lemma 4.5 would allow J+3")

# Mellin decay of phi itself (the dyadic-partition alternative): |M phi(1/2+it)| super-polynomial
f = np.exp(0.5 * UP) * GP
Fh = np.abs(np.fft.fft(f)) * DU
tvals = [10, 25, 50, 100, 200, 400]
mvals = []
for tv in tvals:
    idx = int(round(tv / DTAU))
    mvals.append(float(Fh[idx]))
loc = [math.log(mvals[i + 1] / mvals[i]) / math.log(tvals[i + 1] / tvals[i]) for i in range(len(tvals) - 1)]
check("E8", "EMPIRICAL |M phi(1/2+it)| decays faster than any fixed power (local log-log slope keeps falling)",
      all(loc[i + 1] < loc[i] for i in range(len(loc) - 1)) and loc[-1] < -8,
      "values " + ", ".join("t=%d:%.1e" % (tv, mv) for tv, mv in zip(tvals, mvals))
      + "; local slopes " + ", ".join("%.1f" % s for s in loc))

# Variant B: V_lam(u) = e^{-u/2} g(u) erfc(sqrt(2 pi e^{lam+u})): seminorms bounded uniformly in lam
from scipy.special import erfc as sp_erfc
lams = np.linspace(-30, 8, 153)
PV = []
for lam in lams:
    with np.errstate(over='ignore', under='ignore'):
        Vu = np.exp(-0.5 * US) * G_S * sp_erfc(np.sqrt(2 * np.pi * np.exp(lam + US)))
    F = np.fft.fft(Vu)
    sd = [float(np.max(np.abs(np.fft.ifft((1j * KS) ** k * F)))) for k in range(JMAX + 1)]
    PV.append(np.cumsum(sd))
PV = np.array(PV)
mx = PV.max(axis=0)
at_edges = np.maximum(PV[0], PV[-1])
argmx = [float(lams[i]) for i in PV.argmax(axis=0)]
# lam -> -oo limit is y^{-1/2} phi(y): compare
F0 = np.fft.fft(np.exp(-0.5 * US) * G_S)
lim0 = np.cumsum([float(np.max(np.abs(np.fft.ifft((1j * KS) ** k * F0)))) for k in range(JMAX + 1)])
check("E9", "EMPIRICAL variant B: sup_lam p_j(V_lam), j<=4, lam in [-30,8], finite; lam -> -oo limit is y^{-1/2}phi",
      np.all(np.isfinite(mx)) and np.max(np.abs(PV[0] - lim0) / lim0) < 1e-3 and PV[-1][-1] < 1e-6 * mx[-1],
      "sup p_j: " + ", ".join("%.3g" % v for v in mx) + "; attained at lam = "
      + ", ".join("%.1f" % v for v in argmx) + "; p_4 at lam=8: %.1e" % PV[-1][-1])

print("SUMMARY %d/%d PASS (%.1f s)" % (sum(o for _, o in RESULTS), len(RESULTS), time.time() - T0))
