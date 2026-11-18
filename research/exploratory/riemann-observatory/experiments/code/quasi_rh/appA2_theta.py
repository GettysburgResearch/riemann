# appA2_theta.py -- independent numerical checks of the imported theta-function facts used in App. A.2
# of "The Quasi-Riemann Hypothesis" (paper2.tex l.3083-3165, l.3339-3369), and of the
# coefficient identity (eq:intro-theta-coefficients) l.363-366 used in (eq:ray-mellin).
# Own code (appA_zw.py); nothing from the OpenAI repository.  Run: python3 -I appA2_theta.py
#
# theta is built from DR (5.6)-(5.8) as RENDERED (overlines present), tau1, tau2 from DR (5.13)-(5.14),
# and the cusp table entries d_10, d_19 of DR App. A; action of SL2(C) on H^3 from DR (5.1).
import sys, os, math, cmath, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.special import kv
import appA_zw as Z
from appA_zw import mul, add, sub, neg, conj, norm, ONE, ZERO, LAM, UNITS, ZETA6, W

random.seed(7)
FAIL = []; COUNT = {}
def check(tag, ok, info=None):
    COUNT[tag] = COUNT.get(tag, 0) + 1
    if not ok:
        FAIL.append((tag, info))
        if len([f for f in FAIL if f[0] == tag]) <= 3: print("FAIL", tag, info)
t0 = time.time()

def cub3(c, x):
    """cubic symbol (x/c)_3 as exponent of omega, c primary coprime to 3 (2 | c allowed), None if not coprime."""
    k = 0
    for p, e in Z.fac(c)[1].items():
        if p == (-2, 0):
            ks = [j for j in range(3) if Z.cong(x, Z.pw((0, 1), j), (2, 0))]
            if not ks: return None
            k += e * ks[0]
        else:
            s = Z.PR(p).sym6(x)
            if s is None: return None
            k += e * ((2 * s) % 6 // 2)
    return k % 3
_g = {}
def gDR(r, c):
    """DR's unnormalised g(r, c) = sum_{x mod c} (x/c)_3 breve-e(r x / c), c primary squarefree."""
    if norm(c) == 1: return 1.0 + 0j
    key = (Z.red(r, c), c)
    if key in _g: return _g[key]
    s = 0
    for x in Z.residues(c):
        k = cub3(c, x)
        if k is None: continue
        s += W ** k * Z.eb_xn(mul(r, x), c)
    _g[key] = s
    return s

def decompose(x):
    """x in O nonzero -> (u, m, c, d) with x = u * lambda^m * c * d^3, c squarefree primary, d primary,
    or None if some exponent is == 2 mod 3."""
    unit, f = Z.fac(x)
    m = f.get(LAM, 0)
    c = ONE; d = ONE
    for p, e in f.items():
        if p == LAM: continue
        if e % 3 == 2: return None
        if e % 3 == 1: c = mul(c, p)
        d = mul(d, Z.pw(p, e // 3))
    rest = mul(Z.pw(LAM, m), mul(c, Z.pw(d, 3)))
    u = Z.exdiv(x, rest)
    assert Z.is_unit(u)
    return u, m, c, d

OM = (0, 1); OM2 = (-1, -1)
def tau(mu_x):
    """tau(mu) for mu = mu_x / lambda^3, mu_x in O nonzero (DR (5.7))."""
    dec = decompose(mu_x)
    if dec is None: return 0
    u, k, c, d = dec
    m = k - 3                      # mu = u lambda^m c d^3
    ratio = abs(Z.cv(d)) / abs(Z.cv(c))
    L2 = mul(LAM, LAM)
    if m % 3 == 0:                 # m = 3n - 3, n >= 0
        n = (m + 3) // 3
        if u not in [(1, 0), (-1, 0)]: return 0
        return np.conj(gDR(ONE, c)) * ratio * 3 ** (n / 2 + 2.5)
    if m % 3 == 2:                 # m = 3n - 4, n >= 1
        n = (m + 4) // 3
        if u in [(1, 0), (-1, 0)]:
            return np.conj(gDR(L2, c)) * ratio * 3 ** (n / 2 + 2)
        if u in [OM, neg(OM)]:
            return cmath.exp(-2j * math.pi / 9) * np.conj(gDR(mul(OM, L2), c)) * ratio * 3 ** (n / 2 + 2)
        return cmath.exp(2j * math.pi / 9) * np.conj(gDR(mul(OM2, L2), c)) * ratio * 3 ** (n / 2 + 2)
    return 0

def tau12(mu_x, which):
    """tau_1 / tau_2 of mu = mu_x / lambda^4 (DR (5.13), (5.14))."""
    dec = decompose(mu_x)
    if dec is None: return 0
    u, k, c, d = dec
    if k != 0: return 0
    ratio = abs(Z.cv(d)) / abs(Z.cv(c)); L2 = mul(LAM, LAM)
    e9 = cmath.exp(2j * math.pi / 9); w = complex(W)
    if which == 1:
        if u == ONE: return 9 * w * np.conj(gDR(L2, c)) * ratio
        if u == OM: return 9 / e9 * w ** 2 * np.conj(gDR(mul(OM, L2), c)) * ratio
        if u == OM2: return 9 * e9 * np.conj(gDR(mul(OM2, L2), c)) * ratio
        return 0
    else:
        if u == (-1, 0): return 9 * w ** 2 * np.conj(gDR(L2, c)) * ratio
        if u == neg(OM): return 9 / e9 * np.conj(gDR(mul(OM, L2), c)) * ratio
        if u == neg(OM2): return 9 * w * e9 * np.conj(gDR(mul(OM2, L2), c)) * ratio
        return 0

def lattice(radius):
    pts = []
    B = int(radius * 1.2) + 2
    for a in range(-B, B + 1):
        for b in range(-B, B + 1):
            if (a, b) != (0, 0) and abs(Z.cv((a, b))) <= radius: pts.append((a, b))
    return pts

R = 10.0
LAM3 = Z.cv(Z.pw(LAM, 3)); LAM4 = Z.cv(Z.pw(LAM, 4))
pts = lattice(R * abs(LAM3))
MU = []; TAU = []
for x in pts:
    t = tau(x)
    if t != 0: MU.append(Z.cv(x) / LAM3); TAU.append(t)
MU = np.array(MU); TAU = np.array(TAU)
print("theta: %d nonzero coefficients with |mu| <= %.1f, build %.1fs" % (len(MU), R, time.time() - t0))
check("T.tau_even", True)
SIG = 3 ** 2.5 / 2
def theta(z, v):
    return SIG * v ** (2 / 3) + np.sum(TAU * v * kv(1 / 3, 4 * math.pi * np.abs(MU) * v) * np.exp(4j * math.pi * (MU * z).real))
def act(g, z, v):
    a, b, c, d = [Z.cv(t) if isinstance(t, tuple) else t for t in g]
    den = abs(c * z + d) ** 2 + abs(c) ** 2 * v ** 2
    return (((a * z + b) * np.conj(c * z + d) + a * np.conj(c) * v ** 2) / den, v / den)

# tau even, and the coefficient identity (eq:intro-theta-coefficients):
# coefficient of conj(theta) at lambda^{-3} n b^3 = conj(tau(-lambda^{-3} n b^3)) = 3^{5/2}|b| conj(chi_n(lambda)^2) gamma_2(n)
for x in random.sample(pts, 300):
    check("T.tau_even", abs(tau(x) - tau(neg(x))) < 1e-9, x)
sqf = [n for n in (p for p in ((a, b) for a in range(-20, 21) for b in range(-20, 21)))
       if Z.is_primary(n) and 1 <= norm(n) <= 300 and math.gcd(norm(n), 6) == 1 and Z.is_squarefree(n)] + [ONE]
bs = [b for b in ((a, b) for a in range(-8, 9) for b in range(-8, 9)) if Z.is_primary(b) and norm(b) <= 49 and math.gcd(norm(b), 6) == 1] + [ONE]
for n in random.sample(sqf, 60):
    g2 = Z.gauss(n, 2) if norm(n) > 1 else 1.0
    lam_sym = 0 if norm(n) == 1 else (2 * Z.chi_fast(n, LAM)) % 6
    shared = [p for p in Z.fac(n)[1]] if norm(n) > 1 else []
    for b in random.sample(bs, 6) + shared:
        x = mul(n, Z.pw(b, 3))
        lhs = np.conj(tau(neg(x)))
        rhs = 3 ** 2.5 * abs(Z.cv(b)) * np.conj(ZETA6 ** lam_sym) * g2
        check("T.coeff_identity (no coprimality n,b)", abs(lhs - rhs) < 1e-8 * max(1, abs(rhs)), (n, b, lhs, rhs))
print("coefficient identity done %.1fs" % (time.time() - t0))

# invariances
for _ in range(6):
    z = complex(random.uniform(-1, 1), random.uniform(-1, 1)); v = random.uniform(0.6, 1.2)
    th = theta(z, v)
    for t in [(1, 0), (0, 3), (3, -3)]:
        check("T.period Z+3O", abs(theta(z + Z.cv(t), v) - th) < 1e-9 * abs(th), t)
    check("T.not period omega", abs(theta(z + W, v) - th) > 1e-3 * abs(th))
for _ in range(6):
    z = complex(random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2)); v = random.uniform(0.8, 1.1)
    zz, vv = act((ZERO, (-1, 0), ONE, ZERO), z, v)
    check("T.E invariance", abs(theta(zz, vv) - theta(z, v)) < 1e-9 * abs(theta(z, v)), (z, v, vv))

# automorphy on Gamma_1(3) with multiplier (c/a)_3 (DR (5.4)); compare with the conjugate (c/d)_3
def gamma1_3(c, d):
    THREE_C = mul((3, 0), c)
    a = Z.inv_mod(d, THREE_C)
    b = Z.exdiv(sub(mul(a, d), ONE), c)
    return a, b, c, d
gams = []
for c in [(3, 0), (0, 3), (3, 3), (-3, 0), (3, 6), (6, 3), (6, 0)]:
    for d in [(1, 3), (-2, 0), (4, 3), (1, -3), (-2, -3), (4, 0), (7, 3), (1, 6)]:
        if not Z.is_unit(Z.egcd(c, d)[0]) or not Z.is_primary(d): continue
        gams.append(gamma1_3(c, d))
random.shuffle(gams)
nauto = 0
DEV = []
for (a, b, c, d) in gams[:24]:
    assert sub(mul(a, d), mul(b, c)) == ONE and Z.is_primary(a) and Z.is_primary(d)
    ca = Z.cubic_sym_recip(c, a); cd = Z.cubic_sym_recip(c, d)
    zc = -Z.cv(d) / Z.cv(c)
    for dz in (0.03 + 0.02j, -0.025 + 0.01j):
        z = zc + dz; v = 1 / abs(Z.cv(c))   # puts both points at height ~ 1/|c|
        zz, vv = act((a, b, c, d), z, v)
        if min(v, vv) < 0.17: continue
        ratio = theta(zz, vv) / theta(z, v)
        DEV.append((abs(ratio - W ** ca), abs(ratio - W ** cd) if ca != cd else None, min(v, vv)))
        okA = abs(ratio - W ** ca) < 1e-6; okD = abs(ratio - W ** cd) < 1e-6
        check("T.automorphy multiplier (c/a)_3", okA, ((a, b, c, d), ratio, ca, cd, v, vv))
        if ca != cd:
            check("T.conjugate multiplier (c/d)_3 rejected", not okD, (a, b, c, d))
        nauto += 1
print("automorphy tests: %d  %.1fs" % (nauto, time.time() - t0))
print("  max |ratio - (c/a)_3| = %.2e ; min |ratio - (c/d)_3| over nontrivial symbols = %.3f ; nontrivial cases %d ; min height %.3f"
      % (max(d[0] for d in DEV), min(d[1] for d in DEV if d[1] is not None), sum(1 for d in DEV if d[1] is not None), min(d[2] for d in DEV)))

# H -> gamma_sigma: theta(H w) = theta(gamma_sigma w) for the paper's H (cases 2 and 3)
gp = (ONE, ZERO, OM, ONE); gm = (ONE, ZERO, OM2, ONE)
Hs = [((ONE, ZERO, LAM, ONE), gm, "case2 u0=lambda -> gamma_-"), ((ONE, ZERO, neg(LAM), ONE), gp, "case2 u0=-lambda -> gamma_+")]
for u0 in [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]:
    tgt = {0: (ONE, ZERO, ZERO, ONE), 1: gm, 2: gp}[u0[1] % 3]
    Hs.append(((u0, (-1, 0), ONE, ZERO), tgt, "case3 u0=%s" % (u0,)))
for Hm, gs, name in Hs:
    for _ in range(3):
        # choose w so that both H w and gamma_sigma w are high
        c_ = Z.cv(Hm[2]); d_ = Z.cv(Hm[3])
        z = (-d_ / c_ if abs(c_) > 0 else 0) + complex(random.uniform(-0.05, 0.05), random.uniform(-0.05, 0.05))
        v = 0.9
        z1, v1 = act(Hm, z, v); z2, v2 = act(gs, z, v)
        if min(v1, v2) < 0.25: continue
        t1 = theta(z1, v1); t2 = theta(z2, v2)
        check("T.theta(Hw)=theta(gamma_sigma w)", abs(t1 - t2) < 1e-8 * max(1, abs(t1)), (name, t1, t2, v1, v2))
print("H reduction done %.1fs" % (time.time() - t0))

# cusp expansions (eq:cusp-fourier-coefficients): theta(gamma_+ w) = sum omega tau2(omega mu) e(mu) vK e(mu z), etc.
pts4 = lattice(4.5 * abs(LAM4))
MU4 = np.array([Z.cv(x) / LAM4 for x in pts4])
def tplus(x):   # x = lambda^4 mu ; t_+(mu) = omega tau2(omega mu) e(mu)
    return complex(W) * tau12(mul(OM, x), 2) * np.exp(4j * math.pi * (Z.cv(x) / LAM4).real)
def tminus(x):
    return complex(W) ** 2 * tau12(mul(OM2, x), 1) * np.exp(4j * math.pi * (Z.cv(x) / LAM4).real)
TP = np.array([tplus(x) for x in pts4]); TM = np.array([tminus(x) for x in pts4])
print("cusp coefficient tables: %d indices, %.1fs" % (len(pts4), time.time() - t0))
def F(T, z, v):
    return np.sum(T * v * kv(1 / 3, 4 * math.pi * np.abs(MU4) * v) * np.exp(4j * math.pi * (MU4 * z).real))
for gs, T, name in ((gp, TP, "+"), (gm, TM, "-")):
    for _ in range(5):
        cz = -1 / Z.cv(gs[2])
        z = cz + complex(random.uniform(-0.15, 0.15), random.uniform(-0.15, 0.15)); v = random.uniform(0.75, 0.95)
        zz, vv = act(gs, z, v)
        lhs = theta(zz, vv); rhs = F(T, z, v)
        check("T.cusp expansion gamma_%s (no constant term)" % name, abs(lhs - rhs) < 1e-7 * max(1, abs(lhs)), (z, v, vv, lhs, rhs))
print("cusp expansions done %.1fs" % (time.time() - t0))

# coefficient support and bound (eq:theta-support), (eq:theta-coefficient-bound): |d(ell)| <= 27 * 3^{m/6} |b|
def mval_b(x):
    dec = decompose(x)
    return dec
worst = 0.0
for x in pts:
    t = tau(x)
    if t == 0: continue
    u, k, c, d = decompose(x); m = k - 3
    check("T.support m >= -4 (d_0)", m >= -4)
    ratio_ = abs(t) / (27 * 3 ** (m / 6) * abs(Z.cv(d)))
    worst = max(worst, ratio_)
    check("T.|d_0| <= 27*3^(m/6)|b|", ratio_ <= 1 + 1e-12, (x, ratio_))
for T_, name in ((TP, "+"), (TM, "-")):
    for x, t in zip(pts4, T_):
        if abs(t) < 1e-12: continue
        u, k, c, d = decompose(x); m = k - 4
        check("T.support m = -4 (d_%s)" % name, m == -4)
        check("T.|d_pm| <= 9|b| <= 27*3^(-4/6)|b|", abs(t) <= 9 * abs(Z.cv(d)) * (1 + 1e-12) and 9 <= 27 * 3 ** (-4 / 6))
print("max |d_0(ell)| / (27 3^{m/6} |b|) = %.6f (equality case m = 3k-3)" % worst)

# end-to-end (eq:theta-factorized-shifts): Theta_Psi(z,v) = sum_h c_F(h) conj theta(z + z_h, v)
# with Psi = chi_p^j (Psi_0 trivial), S = {lambda, 2}, L = 18, one prime p of norm 7, j in {1, 0, 4}.
L = (18, 0); RES_L = Z.residues(L)
def phi(x):
    if not Z.is_primary(x) or Z.divides((2, 0), x): return 0
    if norm(x) == 1: return 1.0
    return ZETA6 ** ((2 * Z.chi_fast(x, LAM)) % 6)
PH = {h0: sum(phi(x) * Z.e_xn(neg(mul(h0, x)), L) for x in RES_L if not Z.is_zero(x)) / norm(L) for h0 in RES_L}
p = Z.primary_assoc(Z.split_prime(7)); Np = norm(p)
def chij(x, j):
    k = Z.PR(p).sym6(x)
    if k is None: return 0
    return ZETA6 ** ((j * k) % 6)
def Cpj(j, h):
    return sum(chij(y, j) * Z.e_xn(neg(mul(h, y)), p) for y in Z.residues(p)) / Np
MUc = np.array([Z.cv(x) / LAM3 for x in pts]); TAUc = np.array([tau(x) for x in pts])
def theta_c(z, v):
    return SIG * v ** (2 / 3) + np.sum(TAUc * v * kv(1 / 3, 4 * math.pi * np.abs(MUc) * v) * np.exp(4j * math.pi * (MUc * z).real))
for j in (1, 0, 4):
    # definition series: coefficient conj(tau(-ell)) phi(lambda^3 ell) chi_p^j(lambda^3 ell) at ell = x/lambda^3
    coefs = np.array([np.conj(tau(neg(x))) * phi(x) * chij(x, j) if tau(neg(x)) != 0 else 0 for x in pts])
    shifts = []
    for h0 in RES_L:
        if abs(PH[h0]) < 1e-14: continue
        for hp in Z.residues(p):
            cf = PH[h0] * Cpj(j, hp)
            if abs(cf) < 1e-14: continue
            zh = Z.cv(mul(LAM, LAM)) * (Z.cv(h0) / 18 + Z.cv(hp) / Z.cv(p))
            shifts.append((cf, zh))
    for _ in range(3):
        z = complex(random.uniform(-1, 1), random.uniform(-1, 1)); v = random.uniform(0.45, 0.7)
        lhs = np.sum(coefs * v * kv(1 / 3, 4 * math.pi * np.abs(MUc) * v) * np.exp(4j * math.pi * (MUc * z).real))
        rhs = sum(cf * np.conj(theta_c(z + zh, v)) for cf, zh in shifts)
        check("T.factorized shifts Theta_Psi = sum c_F conj theta(z+z_h)", abs(lhs - rhs) < 1e-8 * max(1, abs(lhs)), (j, z, v, lhs, rhs))
    print("  j=%d: %d translates; Theta_Psi at a sample point = %s" % (j, len(shifts), lhs))

print()
print("SUMMARY (check: number of cases)")
for k in sorted(COUNT): print("  %-50s %6d" % (k, COUNT[k]))
print("TOTAL cases:", sum(COUNT.values()), " FAILURES:", len(FAIL))
for f in FAIL[:20]: print("  ", f)
print("time %.1fs" % (time.time() - t0))
