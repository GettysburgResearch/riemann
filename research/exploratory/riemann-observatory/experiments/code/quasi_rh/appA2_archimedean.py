# appA2_archimedean.py -- checks of the archimedean part of App. A.2 of "The Quasi-Riemann Hypothesis"
# (paper2.tex l.3284-3479): Bessel-Mellin formula, derivative and phase identities, cusp coordinates,
# the substitution v -> 1/(N(c) v), the full constant chain giving C = -(i/81)..., the gamma quotient,
# and the decay of V_*^sharp.  Own code; nothing from the OpenAI repository.  Run: python3 -I appA2_archimedean.py
import sys, os, math, cmath, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
from scipy.special import loggamma, kv
import appA_zw as Z
from appA_zw import mul, conj, norm, ONE, LAM

random.seed(3); mp.mp.dps = 30
FAIL = []; COUNT = {}
def check(tag, ok, info=None):
    COUNT[tag] = COUNT.get(tag, 0) + 1
    if not ok:
        FAIL.append((tag, info)); print("FAIL", tag, info)
t0 = time.time()

# (a) DLMF 10.43.19 in the form (eq:bessel-mellin)
for s in [mp.mpf('0.3'), mp.mpf('1.2'), mp.mpc('0.7', '2.0'), mp.mpc('2.5', '-1.3'), mp.mpf('-0.2')]:
    for ell in [mp.mpf('0.37'), mp.mpf('1.9')]:
        lhs = mp.quad(lambda v: v ** (2 * s) * mp.besselk(mp.mpf(1) / 3, 4 * mp.pi * ell * v), [0, 1, mp.inf])
        rhs = 2 ** (2 * s - 1) * mp.gamma(s + mp.mpf(1) / 3) * mp.gamma(s + mp.mpf(2) / 3) / (4 * mp.pi * ell) ** (2 * s + 1)
        tol = 1e-15 if mp.re(s) > 0 else 1e-8   # Re s < 0: integrable endpoint singularity limits quadrature accuracy
        check("AR.bessel_mellin (valid for Re s > -1/3)", abs(lhs - rhs) < tol * abs(rhs), (s, ell, lhs, rhs))
# (b) phase/scale identity for ell = lambda^{-3} n b^3
for _ in range(200):
    n = Z.primary_assoc((random.randint(-20, 20) * 3 + 1, random.randint(-20, 20) * 3)) if False else None
    while True:
        n = (3 * random.randint(-10, 10) + 1, 3 * random.randint(-10, 10)); b = (3 * random.randint(-5, 5) + 1, 3 * random.randint(-5, 5))
        if norm(n) > 0 and norm(b) > 0: break
    s = complex(random.uniform(-2, 3), random.uniform(-5, 5))
    ell = Z.cv(n) * Z.cv(b) ** 3 / Z.cv(Z.pw(LAM, 3))
    lhs = 1j * np.conj(ell / abs(ell)) * abs(ell) ** (-2 * s)
    an = Z.cv(n) / abs(Z.cv(n)); ab = Z.cv(b) / abs(Z.cv(b))
    rhs = 27 ** s * np.conj(an) * np.conj(ab) ** 3 * norm(n) ** (-s) * norm(b) ** (-3 * s)
    check("AR.phase i*conj(alpha(ell))|ell|^-2s", abs(lhs - rhs) < 1e-9 * abs(rhs), (n, b, s))
check("AR.alpha(lambda^-3) = i", abs(1 / Z.cv(Z.pw(LAM, 3)) / abs(1 / Z.cv(Z.pw(LAM, 3))) - 1j) < 1e-14)
# (c) derivatives of breve-e
eb = lambda ell, z: cmath.exp(2j * math.pi * (ell * z + np.conj(ell * z)))
h = 1e-6
for _ in range(50):
    ell = complex(random.uniform(-3, 3), random.uniform(-3, 3)); z = complex(random.uniform(-1, 1), random.uniform(-1, 1))
    dx = (eb(ell, z + h) - eb(ell, z - h)) / (2 * h); dy = (eb(ell, z + 1j * h) - eb(ell, z - 1j * h)) / (2 * h)
    dzb = (dx + 1j * dy) / 2; dz = (dx - 1j * dy) / 2
    check("AR.d/dzbar ebreve = 2 pi i conj(ell) ebreve", abs(dzb - 2j * math.pi * np.conj(ell) * eb(ell, z)) < 1e-6, (ell, z))
    check("AR.d/dz ebreve = 2 pi i ell ebreve", abs(dz - 2j * math.pi * ell * eb(ell, z)) < 1e-6, (ell, z))
# (d) cusp coordinates (eq:theta-cusp-coordinates) from DR (5.1) and the derivatives at z = 0
def act(g, z, v):
    a, b, c, d = g
    den = abs(c * z + d) ** 2 + abs(c) ** 2 * v ** 2
    return (((a * z + b) * np.conj(c * z + d) + a * np.conj(c) * v ** 2) / den, v / den)
for _ in range(100):
    while True:
        c = (random.randint(-9, 9), random.randint(-9, 9)); dp = (random.randint(-9, 9), random.randint(-9, 9))
        if norm(c) and Z.is_unit(Z.egcd(c, dp)[0]): break
    # find a with a dp == 1 mod c, b = (a dp - 1)/c
    a = Z.inv_mod(dp, c) if norm(c) > 1 else ONE
    b = Z.exdiv(Z.sub(mul(a, dp), ONE), c)
    A, B, C, D = [Z.cv(t) for t in (a, b, c, dp)]
    # g^{-1} = (D -B; -C A)
    gi = (D, -B, -C, A)
    z = complex(random.uniform(-1, 1), random.uniform(-1, 1)) * 0.3; v = random.uniform(0.2, 2)
    zp, vp = act(gi, z + A / C, v)
    zc = -D / C - np.conj(z) / (C ** 2 * (v ** 2 + abs(z) ** 2)); vc = v / (abs(C) ** 2 * (v ** 2 + abs(z) ** 2))
    check("AR.cusp coordinates", abs(zp - zc) < 1e-9 * (1 + abs(zc)) and abs(vp - vc) < 1e-9 * vc, (c, dp))
    # derivatives at z = 0 (Wirtinger, by central differences)
    f = lambda zz: act(gi, zz + A / C, v)
    for comp, name, target in ((lambda t: t[0], "dz'/dzbar = -1/(c^2 v^2)", -1 / (C ** 2 * v ** 2)),
                               (lambda t: np.conj(t[0]), "d conj(z')/dzbar = 0", 0),
                               (lambda t: t[1], "dv'/dzbar = 0", 0)):
        dx = (comp(f(h)) - comp(f(-h))) / (2 * h); dy = (comp(f(1j * h)) - comp(f(-1j * h))) / (2 * h)
        dzb = (dx + 1j * dy) / 2
        check("AR." + name, abs(dzb - target) < 1e-5 * (1 + abs(target)), (c, dp, dzb, target))
    # c^{-2} N(c)^{2-2s} = conj(alpha(c))^2 N(c)^{1-2s}
    s = complex(random.uniform(-1, 2), random.uniform(-3, 3)); Nc = abs(C) ** 2
    check("AR.c^-2 N^(2-2s) = conj(alpha)^2 N^(1-2s)", abs(C ** -2 * Nc ** (2 - 2 * s) - np.conj(C / abs(C)) ** 2 * Nc ** (1 - 2 * s)) < 1e-9 * abs(Nc ** (1 - 2 * s)))
# (e) normalising constants
for s in [0.3 + 1j, 1.7 - 2j, 2.2]:
    lhs = 2j * math.pi * 2 ** (2 * s - 1) / (4 * math.pi) ** (2 * s + 1)
    check("AR.2 pi i 2^(2s-1)/(4pi)^(2s+1) = i/(4 (2pi)^2s)", abs(lhs - 1j / (4 * (2 * math.pi) ** (2 * s))) < 1e-14 * abs(lhs))
# (f) the substitution v -> 1/(N(c) v):  int v^{2s-3} G(1/(N v)) dv = N^{2-2s} int u^{1-2s} G(u) du
Gt = lambda u: u ** 2 * mp.exp(-u - 1 / u)
for s in [mp.mpc('0.4', '1.1'), mp.mpc('-0.7', '0.3')]:
    for Nn in [mp.mpf(7), mp.mpf(91)]:
        lhs = mp.quad(lambda v: v ** (2 * s - 3) * Gt(1 / (Nn * v)), [0, 1 / Nn, 1, mp.inf])
        rhs = Nn ** (2 - 2 * s) * mp.quad(lambda u: u ** (1 - 2 * s) * Gt(u), [0, 1, mp.inf])
        check("AR.substitution v->1/(N v)", abs(lhs - rhs) < 1e-15 * abs(rhs), (s, Nn))
REL = []
# (g) full constant chain (eq:theta-mellin-inversion) -> (eq:reflection)
def K(s): return 3 ** mp.mpf(2.5) / 4 * (27 / (2 * mp.pi) ** 2) ** s * mp.gamma(s + mp.mpf(1) / 3) * mp.gamma(s + mp.mpf(2) / 3)
def Jv_pref(sp): return 1j * mp.gamma(sp + mp.mpf(1) / 3) * mp.gamma(sp + mp.mpf(2) / 3) / (4 * (2 * mp.pi) ** (2 * sp))
def gq(t): return mp.gamma(mp.mpf(7) / 6 + t) * mp.gamma(mp.mpf(5) / 6 + t) / (mp.gamma(mp.mpf(7) / 6 - t) * mp.gamma(mp.mpf(5) / 6 - t))
for _ in range(20):
    s = mp.mpc(random.uniform(-3, -0.1), random.uniform(-6, 6)); t = mp.mpf(1) / 2 - s
    X = mp.mpf(random.uniform(1, 1e4)); Nc = mp.mpf(random.randint(2, 500)); Nl = mp.mpf(random.uniform(0.01, 50))
    # integrand of T(X) per (h, ell), stripped of c_F conj(kappa) conj(alpha(c))^2 d(ell) alpha(ell) ebreve(...) hatV(s-1/2)
    lhs = X ** (s - mp.mpf(1) / 2) / K(s) * (-1) * Nc ** (1 - 2 * s) * Jv_pref(1 - s) * Nl ** (-(1 - s))
    rhs = (-1j / 81) * gq(t) * ((2 * mp.pi) ** 4 * X * Nl / (27 * Nc ** 2)) ** (-t) * Nl ** (-mp.mpf(1) / 2)
    check("AR.constant chain C=-(i/81), kernel argument (2pi)^4 N(ell) X/(27 N(c)^2)", abs(lhs - rhs) < 1e-13 * abs(rhs), (s, lhs, rhs))
    REL.append(float(abs(lhs - rhs) / abs(rhs)))
# (h) gamma quotient: Stirling growth |u|^{4 eta} on Re t = eta
for eta in (-0.25, 0.5, 2.0):
    u1, u2 = 1e3, 1e5
    l1 = float(mp.log(abs(gq(mp.mpc(eta, u1))))); l2 = float(mp.log(abs(gq(mp.mpc(eta, u2)))))
    slope = (l2 - l1) / (math.log(u2) - math.log(u1))
    check("AR.gamma quotient grows like |u|^(4 eta)", abs(slope - 4 * eta) < 1e-3, (eta, slope))
# first pole of the numerator at t = -5/6, reciprocal denominator entire
print("constant chain: max relative deviation %.1e (double-precision inputs)" % max(REL))
check("AR.first numerator pole at t=-5/6", mp.rgamma(mp.mpf(5) / 6 + mp.mpf(-5) / 6) == 0 and abs(gq(mp.mpf(-0.8))) < 1e6 and abs(gq(mp.mpf(-0.8333))) > 1e3)
# (j) V_*^sharp.  Test function V_*(y) = sqrt(y) exp(-2 log^2 y): its Mellin transform is explicit,
#     hatV(w) = int V(x) x^{w-1} dx = sqrt(pi/2) exp((w + 1/2)^2 / 8), entire with Gaussian decay on vertical lines.
#     (Not compactly supported; it is used only to test the contour/pole/decay statements about V^sharp.)
def Vhat(w): return math.sqrt(math.pi / 2) * np.exp((w + 0.5) ** 2 / 8)
def lgq(t):
    return loggamma(7 / 6 + t) + loggamma(5 / 6 + t) - loggamma(7 / 6 - t) - loggamma(5 / 6 - t)
U = np.linspace(-60, 60, 120001); du = U[1] - U[0]
def Vsharp(x, eta):
    t = eta + 1j * U
    integrand = Vhat(-t) * np.exp(lgq(t) - t * math.log((2 * math.pi) ** 4 * x / 27))
    return integrand.sum() * du / (2 * math.pi)
for eta in (-0.25, 0.0, 0.5, 2.0):
    tl = abs(Vhat(-(eta + 60j))) * math.exp(float(np.real(lgq(np.array([eta + 60j]))[0])))
    check("AR.V# truncation tail negligible", tl < 1e-80, (eta, tl))
def Vsharp_err(x, eta):
    t = eta + 1j * U
    integrand = Vhat(-t) * np.exp(lgq(t) - t * math.log((2 * math.pi) ** 4 * x / 27))
    return integrand.sum() * du / (2 * math.pi), np.abs(integrand).sum() * du / (2 * math.pi)
for x in [1e-8, 1e-6, 1e-4, 1e-2, 0.3, 1.0, 3.0, 30.0, 300.0]:
    vals = [Vsharp_err(x, eta) for eta in (-0.25, 0.0, 0.5, 2.0)]
    ref = vals[1][0]
    # floating-point error of each line integral is ~ 1e-15 * int |integrand|; allow 1e-11 * that
    ok = all(abs(v - ref) < 1e-11 * max(l1, vals[1][1]) for v, l1 in vals)
    check("AR.V# contour independence (Re t = -1/4, 0, 1/2, 2): no poles for Re t > -5/6", ok, (x, [(v, l1) for v, l1 in vals]))
# the bounds of (eq:ray-kernel): |V#(x)| <= C_{-1/4} x^{1/4} (x<=1), |V#(x)| <= C_A x^{-A} (x>=1), with
# C_eta = (1/2pi) int |hatV(-t) Gamma-quotient| ((2pi)^4/27)^{-eta} du on Re t = eta
def Cconst(eta):
    t = eta + 1j * U
    return (np.abs(Vhat(-t)) * np.exp(np.real(lgq(t)))).sum() * du / (2 * math.pi) * ((2 * math.pi) ** 4 / 27) ** (-eta)
for x in [1e-8, 1e-6, 1e-4, 1e-2, 0.3, 1.0]:
    check("AR.|V#(x)| <= C x^{1/4} (x <= 1)", abs(Vsharp(x, 0.0)) <= Cconst(-0.25) * x ** 0.25 * (1 + 1e-9), x)
for A in (1.0, 4.0):
    for x in [1.0, 10.0, 1e2, 1e3, 1e4]:
        check("AR.|V#(x)| <= C_A x^{-A} (x >= 1)", abs(Vsharp(x, 0.0)) <= Cconst(A) * x ** (-A) * (1 + 1e-9) + 1e-300, (A, x))
# residue at the first pole t = -5/6:  V#(x) = Res + O(x^{7/6}),  Res = hatV(5/6) Gamma(1/3)/(Gamma(2) Gamma(5/3)) ((2pi)^4 x/27)^{5/6}
res_c = Vhat(5 / 6) * math.gamma(1 / 3) / (math.gamma(2.0) * math.gamma(5 / 3)) * ((2 * math.pi) ** 4 / 27) ** (5 / 6)
for x in [1e-8, 1e-6, 1e-4]:
    v = Vsharp(x, 0.0)
    rel = abs(v - res_c * x ** (5 / 6)) / abs(res_c * x ** (5 / 6))
    print("  x=%7.0e  V#=%.6e  residue term=%.6e  rel.diff=%.2e  (expected O(x^(1/3)))" % (x, v.real, res_c * x ** (5 / 6), rel))
    check("AR.V#(x) = Res_{t=-5/6} + O(x^{7/6}) (so |V#| << x^{5/6} <= x^{1/4} for x<=1)", rel < 10 * x ** (1 / 3), (x, rel))
for x in [10.0, 1e2, 1e3, 1e4]:
    print("  x=%7.0e  |V#(x)|=%.3e" % (x, abs(Vsharp(x, 0.0))))

print()
print("SUMMARY (check: number of cases)")
for k in sorted(COUNT): print("  %-80s %5d" % (k, COUNT[k]))
print("TOTAL cases:", sum(COUNT.values()), " FAILURES:", len(FAIL))
print("time %.1fs" % (time.time() - t0))
