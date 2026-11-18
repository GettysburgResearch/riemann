# appA1_identities.py -- numerical/exact checks of every identity in App. A.1 of
# "The Quasi-Riemann Hypothesis" (paper2.tex l.2689-2872; statement Lemma 4.1 l.823-856).
# Own code only (appA_zw.py); nothing from the OpenAI repository.  Run: python3 -I appA1_identities.py
import sys, os, math, cmath, itertools, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import appA_zw as Z
from appA_zw import mul, add, sub, neg, conj, norm, ONE, ZERO, LAM, UNITS, ZETA6, W

TOL = 1e-9
FAIL = []
COUNT = {}
def check(tag, ok, info=None):
    COUNT[tag] = COUNT.get(tag, 0) + 1
    if not ok:
        FAIL.append((tag, info))
        if len([f for f in FAIL if f[0] == tag]) <= 3: print("FAIL", tag, info)
def close(a, b, tol=TOL): return abs(a - b) < tol

t0 = time.time()
PMAX = 400       # primes with N(p) <= PMAX (split and inert)
primes = Z.primary_primes(PMAX)
print("primes tested:", len(primes), "max norm", max(norm(p) for p in primes),
      "inert:", [p for p in primes if p[1] == 0])

def chival(p, x, j):
    s = Z.PR(p).sym6(x)
    if s is None: return 0
    return ZETA6 ** ((j * s) % 6)
def J(p, i, k):
    return sum(chival(p, x, i) * chival(p, sub(ONE, x), k) for x in Z.residues(p))
def g(p, j):
    return sum(chival(p, x, j) * Z.e_xn(x, p) for x in Z.residues(p))
def chi4(n):  # chi_n(4) complex
    k = Z.chi_fast(n, (4, 0)); return ZETA6 ** k
def chim1(n):
    k = Z.chi_fast(n, (-1, 0)); return ZETA6 ** k

# ---------------- prime-modulus identities (proof of (eq:gj), l.2691-2772) ----------------
for p in primes:
    N = norm(p); R = Z.residues(p); P = Z.PR(p)
    sp = math.sqrt(N)
    gam = {j: g(p, j) / sp for j in range(-6, 12)}
    # (1) count identity  #{x: 4x(1-x)=y} = 1 + chi^3(1-y)
    cnt = {}
    for x in R:
        y = Z.red(mul((4, 0), mul(x, sub(ONE, x))), p); cnt[y] = cnt.get(y, 0) + 1
    for y in R:
        v3 = chival(p, sub(ONE, y), 3)
        check("A1.count", abs(cnt.get(y, 0) - (1 + complex(v3).real)) < 1e-9, (p, y))
    # (2) chi(4) J(chi,chi) = J(chi, chi^3)
    check("A1.chi4J", close(chival(p, (4, 0), 1) * J(p, 1, 1), J(p, 1, 3)), p)
    # (3) Gauss-Jacobi for all nontrivial pairs with nontrivial product
    for i in range(1, 6):
        for k in range(1, 6):
            if (i + k) % 6 == 0: continue
            check("A1.GJ_all_pairs", close(g(p, i) * g(p, k), J(p, i, k) * g(p, i + k), 1e-7), (p, i, k))
    check("A1.GJ_134", close(gam[1] * gam[3] / gam[4], J(p, 1, 3) / sp), p)
    check("A1.GJ_112", close(gam[1] ** 2 / gam[2], J(p, 1, 1) / sp), p)
    # (4) gamma_j gamma_{-j} = chi(-1)^j, |gamma_j| = 1
    for j in range(1, 6):
        check("A1.inverse_char", close(gam[j] * gam[-j], chival(p, (-1, 0), j)), (p, j))
        check("A1.unimodular", close(abs(gam[j]), 1.0), (p, j))
    check("A1.gamma2gamma4", close(gam[2] * gam[4], 1.0), p)
    # (5) gamma1 gamma2 = conj(chi(4)) gamma3 gamma2^3
    check("A1.step_g1g2", close(gam[1] * gam[2], chival(p, (4, 0), 1).conjugate() * gam[3] * gam[2] ** 3), p)
    # (6) J(chi^2,chi^2) exactly in Z[omega]
    Jx = [0, 0, 0]   # coefficients of 1, omega, omega^2
    jsum = 0; prod = ONE
    for x in R:
        s1 = P.sym6(x); s2 = P.sym6(sub(ONE, x))
        if s1 is None or s2 is None: continue
        e = (2 * s1 + 2 * s2) % 6 // 2      # chi^2 = zeta6^{2s} = omega^{s}; exponent of omega
        Jx[e] += 1; jsum += e
        prod = Z.red(mul(prod, mul(x, sub(ONE, x))), p)
    Jel = (Jx[0] - Jx[2], Jx[1] - Jx[2])   # a + b w + c w^2 = (a-c) + (b-c) w
    check("A1.prod_x(1-x)=1", Z.cong(prod, ONE, p), p)
    check("A1.sum_jx=0mod3", jsum % 3 == 0, p)
    check("A1.J22_div_p", Z.divides(p, Jel), (p, Jel))
    check("A1.J22=-1mod3", Z.cong(Jel, (-1, 0), (3, 0)), (p, Jel))
    check("A1.J22=-p", Jel == neg(p), (p, Jel))
    check("A1.J22_vs_complex", close(Z.cv(Jel), J(p, 2, 2)), p)
    # (7) gamma2^3 = -alpha(p)
    check("A1.gamma2^3=-alpha", close(gam[2] ** 3, -Z.alpha(p)), p)
    # (8) (gj) prime case, (g)
    G = chival(p, (4, 0), 1).conjugate() * gam[3]
    check("A1.gj_prime", close(gam[1] * gam[2], -Z.alpha(p) * G), p)
    check("A1.g_prime", close(gam[1] * gam[-1], chival(p, (-1, 0), 1)), p)
    # (9) Gauss sum with e(-y/p): (1/sqrtN) sum chi(y)^j e(-y/p) = chi(-1)^j gamma_j
    for j in range(1, 6):
        s = sum(chival(p, x, j) * Z.e_xn(neg(x), p) for x in R) / sp
        check("A1.gauss_minus", close(s, chival(p, (-1, 0), j) * gam[j]), (p, j))
    # (10) the vanishing power sums used in the binomial step (exponents (q-1)/3 + l, 0<=l<=(q-1)/3)
    if N <= 200:
        e0 = (N - 1) // 3
        for l in range(0, e0 + 1):
            tot = ZERO
            for x in R: tot = add(tot, P.powmod(x, e0 + l))
            check("A1.powersum_vanish", Z.divides(p, tot), (p, l))
print("prime identities done %.1fs" % (time.time() - t0))

# ---------------- quadratic Gauss sums (eq:quadratic-gaussian), l.2782-2844 ----------------
def Gq_direct(c):
    s = sum(Z.e_xn(mul(x, x), c) for x in Z.residues(c))
    return s / math.sqrt(norm(c))
def Gq_poisson(c):
    s = 0
    for y in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        s += Z.e_xn(neg(mul(c, mul(y, y))), (4, 0))
    return s / 2
def Gq_closed(c):
    a, b = c; I = 1j
    return (1 + I ** ((-b) % 4) + I ** (a % 4) + I ** ((b - a) % 4)) / 2
odd = [(a, b) for a in range(-25, 26) for b in range(-25, 26)
       if not (a % 2 == 0 and b % 2 == 0) and 0 < norm((a, b)) <= 700]
for c in odd:
    d = Gq_direct(c)
    check("A1.Gquad_poisson", close(d, Gq_poisson(c)), c)
    check("A1.Gquad_closed", close(d, Gq_closed(c)), c)
print("Gamma_quad: %d moduli c (2 not | c, N(c) <= 700) checked" % len(odd))
# class mod 4 and square invariance
units4 = sorted({Z.red(c, (4, 0)) for c in odd})
check("A1.units_mod4_count", len(units4) == 12, units4)
for c in units4:
    vals = {round(Gq_closed(add(c, mul((4, 0), (s, t)))).real, 9) + 1j * round(Gq_closed(add(c, mul((4, 0), (s, t)))).imag, 9)
            for s in range(-3, 4) for t in range(-3, 4)}
    check("A1.Gquad_mod4", len(vals) == 1, (c, vals))
    for s in units4:
        check("A1.Gquad_square_inv", close(Gq_closed(mul(c, mul(s, s))), Gq_closed(c)), (c, s))
table = {(1, 0): 1, (-1, 0): 1, LAM: 1j, neg(LAM): -1j}
for c, v in table.items():
    check("A1.Gquad_table", close(Gq_closed(c), v), (c, Gq_closed(c)))
# square class of c: c = s^2 * (-1)^e * lambda^f mod 4
def sqclass(c):
    for e in (0, 1):
        for f in (0, 1):
            rep = mul(((-1) ** e, 0), Z.pw(LAM, f))
            for s in units4:
                if Z.cong(c, mul(rep, mul(s, s)), (4, 0)): return e, f
    raise ValueError(c)
def Rcls(c1, c2):
    return Gq_closed(mul(c1, c2)) / (Gq_closed(c1) * Gq_closed(c2))
for c1 in units4:
    for c2 in units4:
        (e, f), (gg, h) = sqclass(c1), sqclass(c2)
        r = Rcls(c1, c2)
        check("A1.R_formula", close(r, (-1) ** (e * h + f * gg + f * h)), (c1, c2, r))
        check("A1.R_symmetric", close(r, Rcls(c2, c1)), (c1, c2))
        for c3 in units4:
            check("A1.R_bichar", close(Rcls(mul(c1, c3), c2), Rcls(c1, c2) * Rcls(c3, c2)), (c1, c2, c3))
print("square classes / R table done %.1fs" % (time.time() - t0))

# Gamma_quad(p) = gamma_3(p) for primes; = gamma_3(n) for squarefree n
for p in primes:
    check("A1.Gquad=gamma3_prime", close(Gq_direct(p), g(p, 3) / math.sqrt(norm(p))), p)

# ---------------- composite squarefree moduli ----------------
NMAX = 2000
small = [p for p in primes if norm(p) <= 200]
comp = []
for r in (2, 3):
    for combo in itertools.combinations(small, r):
        n = ONE
        for q in combo: n = mul(n, q)
        if norm(n) <= NMAX: comp.append((n, combo))
random.seed(1)
print("composite squarefree n:", len(comp))
for n, combo in comp:
    gm = {j: Z.gauss(n, j) for j in (-1, 1, 2, 3)}
    mu = (-1) ** len(combo); al = Z.alpha(n)
    check("A1.gamma2^3=mu*alpha", close(gm[2] ** 3, mu * al), n)
    Gn = chi4(n).conjugate() * gm[3]
    check("A1.gj", close(gm[1] * gm[2], mu * al * Gn), n)
    check("A1.g", close(gm[1] * gm[-1], chim1(n)), n)
    check("A1.convert1", close(al.conjugate() * gm[2] * gm[1], mu * Gn), n)
    check("A1.convert2", close(mu * gm[-1], chim1(n) / Gn * al.conjugate() * gm[2]), n)
    check("A1.Gquad=gamma3_sqfree", close(Gq_direct(n), gm[3]), n)
    # twisted multiplicativity gamma_j(ab) = gamma_j(a) gamma_j(b) (chi_a(b) chi_b(a))^j
    a = combo[0]; b = ONE
    for q in combo[1:]: b = mul(b, q)
    ka = Z.chi_fast(a, b); kb = Z.chi_fast(b, a)
    for j in (1, 2, 3):
        ga = Z.gauss(a, j); gb = Z.gauss(b, j)
        gab = gm[j] if j in gm else Z.gauss(n, j)
        check("A1.twisted_mult", close(gab, ga * gb * ZETA6 ** ((j * (ka + kb)) % 6)), (n, j))
    # (crt-a) with xi = 1 and xi = conj chi_.(4)
    for xi in (lambda m: 1.0, lambda m: chi4(m).conjugate()):
        aX = lambda m: Z.alpha(m).conjugate() * Z.gauss(m, 2) * xi(m)
        check("A1.crt-a", close(aX(n), aX(a) * aX(b) * ZETA6 ** ((4 * kb) % 6)), n)
print("composite identities done %.1fs" % (time.time() - t0))

# ---------------- reciprocity ----------------
prim = [x for x in ((a, b) for a in range(-30, 31) for b in range(-30, 31))
        if Z.is_primary(x) and norm(x) > 1 and norm(x) <= 600 and math.gcd(norm(x), 6) == 1]
print("primary elements coprime to 6 with N<=600:", len(prim))
def cub(k): return None if k is None else (2 * k) % 6 // 2      # chi^2 = omega^{k}: exponent mod 3
def quad(k): return None if k is None else (3 * k) % 6 // 3     # chi^3 = (-1)^{k}
nrec = 0
for a in prim[:260]:
    for b in prim[:260]:
        if a == b: continue
        ga, _, _ = Z.egcd(a, b)
        if not Z.is_unit(ga): continue
        kab = Z.chi_fast(b, a); kba = Z.chi_fast(a, b)   # chi_b(a), chi_a(b)
        R = Rcls(a, b)
        check("A1.sextic_recip", close(ZETA6 ** kab, R * ZETA6 ** kba), (a, b))
        check("A1.cubic_recip", cub(kab) == cub(kba), (a, b))
        # R = (a/b)_2 (b/a)_2 and Gq twisted multiplicativity
        q2 = (-1) ** (quad(kab) + quad(kba))
        check("A1.R=(a/b)2(b/a)2", close(R, q2), (a, b))
        check("A1.Gquad_twisted", close(Gq_closed(mul(a, b)), q2 * Gq_closed(a) * Gq_closed(b)), (a, b))
        nrec += 1
print("reciprocity pairs:", nrec, "%.1fs" % (time.time() - t0))
# supplementary laws DR (1.5) and periodicity of (lambda/n)_3 mod 9
per9 = {}
for d in prim:
    a2, a3 = Z.cubic_supp(d)
    check("A1.supp_omega", cub(Z.chi_fast(d, (0, 1))) == a2 % 3, d)
    check("A1.supp_lambda", cub(Z.chi_fast(d, LAM)) == (-a3) % 3, d)
    key = Z.red(d, (9, 0)); v = cub(Z.chi_fast(d, LAM))
    check("A1.lambda_sym_period9", per9.setdefault(key, v) == v, d)
    # chi_d(-1) = (-1/d)_2 depends on d mod 4; chi_d(4) = (-2/d)_3 = (d/-2)_3 depends on d mod 2
    dm2 = Z.red(d, (2, 0))
    cube_root_mod2 = [k for k in range(3) if Z.cong(d, Z.pw((0, 1), k), (2, 0))]
    # chi_d(4) is the SEXTIC symbol (4/d)_6; compare with the CUBIC symbols (-2/d)_3 and (d/-2)_3
    k4 = Z.chi_fast(d, (4, 0))
    check("A1.chi4=(d/-2)_3", len(cube_root_mod2) == 1 and close(ZETA6 ** k4, W ** cube_root_mod2[0]), d)
    check("A1.chi4=(-2/d)_3", close(ZETA6 ** k4, W ** cub(Z.chi_fast(d, (-2, 0)))), d)
    # R(c,c) = chi_c(-1)
    check("A1.R(c,c)=chi_c(-1)", close(Rcls(d, d), ZETA6 ** Z.chi_fast(d, (-1, 0))), d)

# ---------------- G on the ray class group mod 12 (primary reps <-> (O/4)^x) ----------------
def cls_rep(c4):
    """a primary element congruent to c4 mod 4 (and 1 mod 3)."""
    for s in range(-6, 7):
        for t in range(-6, 7):
            x = add(c4, mul((4, 0), (s, t)))
            if Z.is_primary(x) and math.gcd(norm(x), 6) == 1: return x
def Gcls(c):
    k = [k for k in range(3) if Z.cong(c, Z.pw((0, 1), k), (2, 0))][0]   # (c/-2)_3 = omega^k
    return (W ** k).conjugate() * Gq_closed(c)
reps = {c4: cls_rep(c4) for c4 in units4}
for c4, x in reps.items():
    check("A1.class_rep", Z.cong(x, c4, (4, 0)) and Z.is_primary(x), (c4, x))
for c4a, xa in reps.items():
    # G(a^{-1}) = chi_a(-1) conj G(a)
    ainv4 = [c for c in units4 if Z.cong(mul(c, c4a), ONE, (4, 0))][0]
    xainv = reps[ainv4]
    check("A1.G_inverse", close(Gcls(xainv), ZETA6 ** Z.chi_fast(xa, (-1, 0)) * Gcls(xa).conjugate()), c4a)
    for c4b, xb in reps.items():
        check("A1.G_mult_classes", close(Gcls(mul(xa, xb)), Gcls(xa) * Gcls(xb) * Rcls(xa, xb)), (c4a, c4b))
        bainv = Z.red(mul(c4b, ainv4), (4, 0)); xq = reps[bainv]
        lhs = ZETA6 ** Z.chi_fast(xa, (-1, 0)) * Gcls(xa).conjugate() * Gcls(xb) * Rcls(xa, xb)
        check("A1.quotient", close(lhs, Gcls(xq)), (c4a, c4b))
# G(n) (squarefree, defined via gamma_3) agrees with the class function
for n, combo in comp[:150]:
    check("A1.G_is_class_fn", close(chi4(n).conjugate() * Z.gauss(n, 3), Gcls(n)), n)
for p in primes:
    check("A1.G_is_class_fn_prime", close(chi4(p).conjugate() * g(p, 3) / math.sqrt(norm(p)), Gcls(p)), p)
print("ray-class identities done %.1fs" % (time.time() - t0))

# ---------------- the Gaussian Fourier transform used in the Poisson proof (l.2793-2797) ----------------
# f(z) = e(z^2/c) exp(-pi eta |z|^2).  Claimed: hat f(y) = |c|/(2 sqrt r) exp(-pi eta N(c)|y|^2/(4r)) e(-c y^2/(4r)),
# r = 1 + 3 N(c) eta^2 / 16, with the measure normalised to give O covolume 1 (so Poisson reads
# sum_O f = sum_O hat f), pairing <z,y> = Tr(z y / lambda).  We check by exact Gaussian algebra
# and by direct numerical quadrature.
import numpy as np
def quadform_e(cz):
    """matrix Q with e(z^2 * cz) = exp(2 pi i x^T Q x), x = (Re z, Im z), cz complex."""
    # e(w) = exp(4 pi i Im w / sqrt3); Im(cz (x1 + i x2)^2) = Im(cz)(x1^2 - x2^2) + 2 Re(cz) x1 x2
    k = 2 / SQ3_
    return k * np.array([[cz.imag, cz.real], [cz.real, -cz.imag]])
SQ3_ = math.sqrt(3.0)
def fhat_exact(c, eta, y):
    cz = 1 / Z.cv(c)
    Q = quadform_e(cz)
    A = eta * np.eye(2) - 2j * Q                    # f = exp(-pi x^T A x)
    # pairing: e(-z y) = exp(-2 pi i (2/sqrt3) Im(z y)); Im(zy) = x1 Im y + x2 Re y
    yc = Z.cv(y) if isinstance(y, tuple) else y
    xi = (2 / SQ3_) * np.array([yc.imag, yc.real])  # e(-zy) = exp(-2 pi i xi.x)
    Ainv = np.linalg.inv(A)
    detA = np.linalg.det(A)
    # Fourier transform with Lebesgue measure: det(A)^{-1/2} exp(-pi xi^T A^{-1} xi); principal sqrt is right
    # because A = eta I - 2iQ has positive definite real part (continuity in eta from the real case)
    val = np.exp(-math.pi * xi @ Ainv @ xi) / np.sqrt(detA)
    return val * 2 / SQ3_                            # measure giving O covolume 1
def fhat_claim(c, eta, y):
    Nc = norm(c); r = 1 + 3 * Nc * eta ** 2 / 16
    yc = Z.cv(y) if isinstance(y, tuple) else y
    ee = cmath.exp(4j * math.pi * ((-Z.cv(c) * yc ** 2 / (4 * r)).imag) / SQ3_)
    return abs(Z.cv(c)) / (2 * math.sqrt(r)) * math.exp(-math.pi * eta * Nc * abs(yc) ** 2 / (4 * r)) * ee
for c in [(1, 3), (5, 0), (2, -3), (7, 3), (-1, 0), (3, 1), (1, 2)]:
    for eta in (0.05, 0.3, 1.0, 2.5):
        for y in [(0, 0), (1, 0), (0, 1), (2, -1), (3, 5)]:
            a = fhat_exact(c, eta, y); b = fhat_claim(c, eta, y)
            check("A1.gauss_FT_formula", abs(a - b) < 1e-9 * max(1, abs(a)), (c, eta, y, a, b))
# one brute-force quadrature cross-check of fhat_exact (c = 1+3w, eta = 1)
from scipy import integrate
c = (1, 3); eta = 1.0; y = (1, 0)
cz = 1 / Z.cv(c); yc = Z.cv(y)
def integrand(x1, x2, part):
    z = complex(x1, x2)
    v = cmath.exp(4j * math.pi * (z * z * cz).imag / SQ3_) * math.exp(-math.pi * eta * abs(z) ** 2) \
        * cmath.exp(-4j * math.pi * (z * yc).imag / SQ3_)
    return v.real if part == 0 else v.imag
re_ = integrate.dblquad(lambda x2, x1: integrand(x1, x2, 0), -6, 6, -6, 6, epsabs=1e-11)[0]
im_ = integrate.dblquad(lambda x2, x1: integrand(x1, x2, 1), -6, 6, -6, 6, epsabs=1e-11)[0]
quad = complex(re_, im_) * 2 / SQ3_
check("A1.gauss_FT_quadrature", abs(quad - fhat_exact(c, eta, y)) < 1e-7, (quad, fhat_exact(c, eta, y)))
print("Gaussian FT: quadrature", quad, "closed form", fhat_claim(c, eta, y))

print()
print("SUMMARY (check: number of cases)")
for k in sorted(COUNT): print("  %-28s %6d" % (k, COUNT[k]))
print("TOTAL cases:", sum(COUNT.values()), " FAILURES:", len(FAIL))
for f in FAIL[:20]: print("  ", f)
print("time %.1fs" % (time.time() - t0))
