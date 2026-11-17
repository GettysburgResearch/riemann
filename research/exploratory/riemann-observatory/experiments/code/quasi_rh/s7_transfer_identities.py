# s7_transfer_identities.py -- Level-2 audit of Section 7 of "The Quasi-Riemann Hypothesis"
# (paper2.tex l.2217-2685, proof of the transfer proposition, Prop. 5.4).
# Written from scratch for this audit; no code from the OpenAI repository is used or run.
# Reuses only our own Z[omega] helpers in s4_zw.py (same directory).
#
# All tests are EXACT identities. They hold for any radial Schwartz Phi, so we use the Gaussian
#   Phi(t) = exp(-pi t),  hatPhi(t) = (2/sqrt3) exp(-4 pi t/3)
# (closed form verified by quadrature in s4_poisson_checks.py). Since hatPhi is not compactly
# supported, every Fourier sum is taken over ALL nonzero frequencies, truncated where
# hatPhi < 1e-16. The paper's frequency ranges (support of hatPhi) are therefore NOT exercised here;
# they are checked by hand in the report.
#
# Toy arithmetic: S = {primes above 2, 3, 5}; xi((n)) = psi(N n mod 5) with psi of order 4
# (a ray class character of conductor 5, trivial on units); G is the class function on the
# 12 primary classes mod 4 from App. A.1, read off from brute-force Gauss sums of primes.
#
#   T1  Lemma 7.1: A(W) = Z + [displayed (C,t,d,f,h,x1,x2) expression], l.2274-2325,
#       with w_{C,d}, ell, p_{hf^2}, K_h exactly as in l.2235-2250, l.2316-2321.
#   T2  Lemma 7.2: M = Z + RHS of (eq:arithmetic-poisson-identity), l.2358-2413, for several
#       (C,d,t,xi_1,Y,ell), including Y < 1.
#   T3  Lemma 7.3: Q_{xi1}(U) = calZ + [(r,f',k') regrouped form], l.2509-2583, i.e. the
#       weight identity w Y N(g)/(N(e) ell) = c_I Sigma N(r)/L^2, the Fourier parameter
#       c_I Sigma F N(k') N(r)^2/(H L x1 x2), X'_0 = L/(N(r)N(f')), and the preimage
#       regrouping sum mu(e)mu(w) = tau(r) 1_{f'|k'}.
#   T4  abstract per-prime preimage count (l.2550-2568).
#   T5  symbolic scale identities (l.2237-2239, l.2526-2531, l.2587-2621, l.2646-2651,
#       l.2658-2661) with sympy.
#   Negative controls for T1-T3 (deliberately wrong conventions) must fail at O(1).
#
# Run:  python3 -I s7_transfer_identities.py
import sys, os, math, cmath, itertools, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from s4_zw import *

random.seed(20261117)
T0 = time.time()

def Phi(t): return np.exp(-np.pi * t)
def hatPhi(t): return (2 / SQ3) * np.exp(-4 * np.pi * t / 3)
TCUT = 9.6          # hatPhi(t) < 1e-16 for t > TCUT

fails = 0; tests = 0
def report(name, lhs, rhs, tol=1e-9):
    global fails, tests
    tests += 1
    err = abs(lhs - rhs) / max(1e-300, abs(lhs))
    ok = err < tol
    if not ok: fails += 1
    print("%-58s lhs=%-30s rhs=%-30s relerr=%.1e %s" % (name, "%.12g%+.12gj" % (lhs.real, lhs.imag),
          "%.12g%+.12gj" % (rhs.real, rhs.imag), err, "OK" if ok else "FAIL"))
    return ok
def control(name, lhs, bad, scale):
    """relative error measured against `scale` = size of the nonzero-frequency part |lhs - Z|;
    the genuine identities hold to ~1e-14 on this scale, so a control 'fails' if err > 1e-8."""
    err = abs(lhs - bad) / scale
    print("  negative control %-46s err/|lhs-Z|=%.2e  (%s)" % (name, err, "fails as it should" if err > 1e-8 else "UNEXPECTED: did not fail"))
    return err > 1e-8

# ---------------------------------------------------------------- arithmetic set-up
P = [p for p in eisenstein_primes(130) if p.q != 25]     # primes prime to 30 (split and inert 11)
key = lambda ps: tuple(sorted(p.g for p in ps))
mu = lambda ps: (-1) ** len(ps)
def pset(ps): return set(p.g for p in ps)
def coprime(a, b): return not (pset(a) & pset(b))
def divisors(ps): return [list(c) for k in range(len(ps) + 1) for c in itertools.combinations(ps, k)]
def tau(ps): return 2 ** len(ps)
def phi_ratio(ps):
    r = 1.0
    for p in ps: r *= (1 - 1 / p.q)
    return r
def union(*lists):
    out = []; seen = set()
    for l in lists:
        for p in l:
            if p.g not in seen: out.append(p); seen.add(p.g)
    return out
def minus(a, b): return [p for p in a if p.g not in pset(b)]

psi = {1: 1, 2: 1j, 4: -1, 3: -1j}            # order-4 character mod 5
def xi(ps): return psi[nm(ps) % 5]
def xi1(ps): return psi[nm(ps) % 5] ** 3     # a second ray class character (conj of xi)

G_class = {}
for p in eisenstein_primes(600):
    t = mod4(p.g)
    if t not in G_class:
        G_class[t] = chi([p], (4, 0)).conjugate() * gamma([p], 3)
assert len(G_class) == 12
units4 = [(a, b) for a in range(4) for b in range(4) if norm((a, b)) % 2 == 1]
def inv4(t):
    for u in units4:
        if mod4(mul(u, t)) == (1, 0): return u
def Gquot(ps_num, ps_den):
    """G(num * den^{-1}) on the primary classes mod 4"""
    return G_class[mod4(mul(elt(ps_num), inv4(mod4(elt(ps_den)))))]
acache = {}
def a(ps):
    k = key(ps)
    if k not in acache:
        acache[k] = alpha(elt(ps)).conjugate() * gamma(ps, 2) if ps else 1.0 + 0j
    return acache[k]
def chi_el(ps, x, j=1):
    return chi(ps, x, j) if ps else 1.0 + 0j

def CHarr(ps, A, B, j=1):
    return chi_arr(ps, A, B, j) if ps else np.ones(A.shape, dtype=complex)
def coprime_mask(ps, A, B):
    m = np.ones(A.shape, dtype=bool)
    for p in ps: m &= (p.sym_arr(A, B) >= 0)
    return m

# ================================================================ T1: Lemma 7.1
print("=" * 30, "T1  Lemma 7.1 (first Poisson summation, in k)")
L1 = 50.0; NM1 = 100; H1 = 30.0
cols1 = squarefree_products(P, NM1)
F1 = 7.0
fs1 = [f for f in cols1 if F1 <= nm(f) < 2 * F1]
wval = {N: complex(random.gauss(0, 1), random.gauss(0, 1)) for N in range(1, NM1 + 1)}
def Wn(N): return wval.get(N, 0.0)          # W(N(n)/L) := Wn(N(n)), supported on N(n) <= NM1
print("columns", len(cols1), " twists f:", [nm(f) for f in fs1])

# direct A(W)
KA, KB = lattice_points(15 * H1 + 30); KN = KA * KA - KA * KB + KB * KB
CHk = {key(n): CHarr(n, KA, KB) for n in cols1}
A_direct = 0.0
for f in fs1:
    f4 = power(elt(f), 4)
    S = np.zeros(KA.shape, dtype=complex); S0 = 0j
    for n in cols1:
        c = a(n) * xi(n) * chi_el(n, f4) * Wn(nm(n))
        if c == 0: continue
        S += c * CHk[key(n)]
        if not n: S0 += c                    # k = 0: only n = 1 survives (chi_1 = 1)
    A_direct += np.sum(Phi(KN / H1) * np.abs(S) ** 2) + abs(S0) ** 2
A_direct /= (L1 * F1)
A_direct = complex(A_direct)

Z1 = 0.0
for f in fs1:
    for C in cols1:
        if coprime(C, f):
            Z1 += abs(Wn(nm(C))) ** 2 * H1 * hatPhi(0.0) * phi_ratio(C)
Z1 /= (L1 * F1)

# dual lattice for h
RH = TCUT * L1 * L1 * 4.0 / H1 + 10
HA, HB = lattice_points(RH); HN = HA * HA - HA * HB + HB * HB
CHh = {key(n): CHarr(n, HA, HB) for n in cols1}
print("row points", len(KA), " dual points", len(HA))

def T1_rhs(variant=None):
    tot = 0j
    for C in cols1:
        for t in cols1:
            if not coprime(C, t) or nm(C) * nm(t) > NM1: continue
            ell = L1 / (nm(C) * nm(t))
            Ct = union(C, t)
            maskt = coprime_mask(t, HA, HB)
            xs = [x for x in cols1 if coprime(x, Ct) and nm(C) * nm(t) * nm(x) <= NM1]
            for d in divisors(C):
                wCd = H1 * nm(C) / (nm(d) * L1 * L1 * F1)
                if variant == "no_Nd_in_w": wCd = H1 * nm(C) / (L1 * L1 * F1)
                sgn = mu(d) * mu(t)
                if variant == "drop_mu_t": sgn = mu(d)
                C4 = power(elt(C), 4); de = elt(d)
                for f in fs1:
                    if not coprime(f, Ct): continue
                    f2 = power(elt(f), 2)
                    cx = {}
                    for x in xs:
                        # p_{hf^2}(x) = mu(x) 1_{(x,t)=1} conj chi_x(h f^2) chi_x(C)^4 chi_x(d); xi_1-part kept in Psi
                        cx[key(x)] = mu(x) * np.conj(chi_el(x, f2)) * chi_el(x, C4) * chi_el(x, de)
                    for x1 in xs:
                        c1 = cx[key(x1)]
                        if c1 == 0: continue
                        z1 = nm(C) * nm(t) * nm(x1) / L1
                        for x2 in xs:
                            c2 = cx[key(x2)]
                            if c2 == 0: continue
                            z2 = nm(C) * nm(t) * nm(x2) / L1
                            if variant == "G_inverted":
                                Psi = xi(x1) * np.conj(xi(x2)) * Gquot(x2, x1)
                            else:
                                Psi = xi(x1) * np.conj(xi(x2)) * Gquot(x1, x2)     # (xi G)(x1 x2^{-1})
                            Kpref = (z1 * z2) ** -0.5 * Wn(nm(C) * nm(t) * nm(x1)) * np.conj(Wn(nm(C) * nm(t) * nm(x2)))
                            if Kpref == 0: continue
                            arg = H1 * HN * nm(C) ** 2 / (L1 * L1 * nm(d) * z1 * z2)
                            hs = np.sum(maskt * np.conj(CHh[key(x1)]) * CHh[key(x2)] * hatPhi(arg))
                            tot += sgn * wCd * Psi * c1 * np.conj(c2) * Kpref * hs
    return tot

R1 = T1_rhs()
report("T1 Lemma 7.1: A(W) = Z + displayed sum", A_direct, Z1 + R1)
print("  Z =", Z1, " |A - Z| =", abs(A_direct - Z1))
control("(mu(t) dropped)", A_direct, Z1 + T1_rhs("drop_mu_t"), abs(A_direct - Z1))
control("(N(d) dropped from w_{C,d})", A_direct, Z1 + T1_rhs("no_Nd_in_w"), abs(A_direct - Z1))
control("(G(x2/x1) instead of G(x1/x2))", A_direct, Z1 + T1_rhs("G_inverted"), abs(A_direct - Z1))
print("  [T1 time %.1fs]" % (time.time() - T0))

# ================================================================ common U for T2, T3
bI = 2.0                                     # I_* = [a, b] with b = 2v, v = 1
def Ufun(x):
    x = np.asarray(x, dtype=float)
    return np.where((x > 0) & (x <= bI), x ** 0.7 * np.exp(2.1j * x) * (bI - x) ** 2, 0.0)
def U0fun(x): return np.asarray(x, dtype=float) ** -0.5 * Ufun(x)

# ================================================================ T2: Lemma 7.2
print("=" * 30, "T2  Lemma 7.2 (second Poisson identity, in y)")
def T2_case(C, d, t, ell, Y, xichar, variant=None):
    NMn = int(math.floor(bI * ell))
    cols = squarefree_products(P, NMn)
    Ct = union(C, t); C4 = power(elt(C), 4); de = elt(d)
    ns = [n for n in cols if coprime(n, Ct)]
    # direct M
    YA, YB = lattice_points(14 * Y + 30); YN = YA * YA - YA * YB + YB * YB
    Pv = np.zeros(YA.shape, dtype=complex); P0 = 0j
    for n in ns:
        c = mu(n) * xichar(n) * chi_el(n, C4) * chi_el(n, de) * complex(Ufun(nm(n) / ell))
        if c == 0: continue
        Pv += c * np.conj(CHarr(n, YA, YB))
        if not n: P0 += c
    M_direct = complex(np.sum(Phi(YN / Y) * np.abs(Pv) ** 2) + abs(P0) ** 2)
    # Z
    Z = sum(Y * hatPhi(0.0) * abs(complex(Ufun(nm(g) / ell))) ** 2 * phi_ratio(g) for g in ns)
    # RHS of (eq:arithmetic-poisson-identity)
    Rd = TCUT * ell * ell * bI * bI / Y + 10
    DA, DB = lattice_points(Rd); DN = DA * DA - DA * DB + DB * DB
    CHd = {key(n): CHarr(n, DA, DB) for n in cols}
    tot = 0j
    for g in ns:
        if nm(g) > NMn: continue
        for e in divisors(g):
            for w in cols:
                if not coprime(w, union(g, Ct)) or nm(g) * nm(w) > NMn: continue
                Xp = ell / (nm(g) * nm(w))
                maskw = coprime_mask(w, DA, DB)
                if variant == "drop_hw": maskw = np.ones(DA.shape, dtype=bool)
                r = union(t, minus(g, e))           # tg/e
                fp = union(C, e, w)                 # Cew
                fp4 = power(elt(fp), 4); dee = mul(de, elt(e))
                pref = Y * mu(e) * mu(w) * nm(g) / (nm(e) * ell)
                nn = [n for n in cols if coprime(n, union(r, fp)) and nm(n) <= bI * Xp]
                cn = {}
                for n in nn:
                    if variant == "e_exponent":      # wrong: chi_n(dh) chi_n(Cw)^4 chi_n(e)^4
                        cn[key(n)] = chi_el(n, de) * chi_el(n, power(mul(elt(C), elt(w)), 4)) * chi_el(n, power(elt(e), 4))
                    else:                            # 1_{(n,tg/e)=1} chi_n(de) chi_n(Cew)^4 ; chi_n(h) is vectorised
                        cn[key(n)] = chi_el(n, dee) * chi_el(n, fp4)
                for n1 in nn:
                    x1 = nm(n1) / Xp; u1 = complex(U0fun(x1))
                    if u1 == 0 or cn[key(n1)] == 0: continue
                    for n2 in nn:
                        x2 = nm(n2) / Xp; u2 = complex(U0fun(x2))
                        if u2 == 0 or cn[key(n2)] == 0: continue
                        Psi2 = xichar(n1) * np.conj(xichar(n2)) * Gquot(n2, n1) * a(n1) * np.conj(a(n2))
                        arg = Y * DN * nm(g) ** 2 / (nm(e) * ell * ell * x1 * x2)
                        hs = np.sum(maskw * CHd[key(n1)] * np.conj(CHd[key(n2)]) * hatPhi(arg))
                        tot += pref * Psi2 * cn[key(n1)] * np.conj(cn[key(n2)]) * u1 * np.conj(u2) * hs
    return M_direct, Z, tot

byq = {}
for p in P: byq.setdefault(p.q, []).append(p)
p7a, p7b = byq[7]; p13a, p13b = byq[13]; p19a = byq[19][0]
cases2 = [
    ([], [], [], 30.0, 12.0),
    ([p7a], [p7a], [], 30.0, 7.5),
    ([p7a], [], [p13a], 22.0, 3.3),
    ([p7a, p13b], [p13b], [p7b], 9.0, 0.42),        # Y < 1
    ([p19a], [], [p7a, p7b], 4.0, 25.0),
    ([p13a], [], [], 45.0, 9.0),                   # longer columns: e, w and n all nontrivial together
    ([p19a], [p19a], [], 50.0, 9.0),               # admits g = e of norm 7 with n1, n2 = the two primes of norm 13
]
# Remark: with a RADIAL weight, a pair (n1,n2) whose character chi_{n1} conj(chi_{n2}) is nontrivial on the
# units contributes 0 to both sides (substitute h -> zeta_6 h); cf. O-S4-1 in audit_S4.md. The tests are
# therefore informative only on unit-trivial pairs: diagonal pairs, and e.g. (p13a, p13b), (p37, 1), (p19, p7 p13).
# The last case above is included so that a pair of this kind meets a nontrivial e.
for (C, d, t, ell, Y) in cases2:
    M, Z, R = T2_case(C, d, t, ell, Y, xi1)
    report("T2 Lemma 7.2: N(C)=%d N(d)=%d N(t)=%d ell=%g Y=%g" % (nm(C), nm(d), nm(t), ell, Y), M, Z + R)
C, d, t, ell, Y = cases2[5]
M, Z, R = T2_case(C, d, t, ell, Y, xi1, "drop_hw"); control("T2 (restriction (h,w)=1 dropped)", M, Z + R, abs(M - Z))
M, Z, R = T2_case(C, d, t, ell, Y, xi1, "e_exponent"); control("T2 (chi_n(e)^4 instead of ^5), case 6", M, Z + R, abs(M - Z))
C, d, t, ell, Y = cases2[6]
M, Z, R = T2_case(C, d, t, ell, Y, xi1, "e_exponent"); control("T2 (chi_n(e)^4 instead of ^5), case 7", M, Z + R, abs(M - Z))
print("  [T2 time %.1fs]" % (time.time() - T0))

# ================================================================ T3: Lemma 7.3 regrouping
print("=" * 30, "T3  Lemma 7.3 (regrouping into the (r,f',k') form)")
L3 = 60.0; v3 = 1.0; cI = 1.0; Sig = 150.0; F3 = 2.0; H3 = 100.0
NM3 = int(2 * v3 * L3)
cols3 = squarefree_products(P, NM3)
def Q_direct_and_Z():
    Q = 0.0; Zt = 0.0; nCt = 0; Ymin = 1e300
    for C in cols3:
        for t in cols3:
            if not coprime(C, t) or nm(C) * nm(t) > 2 * v3 * L3: continue
            nCt += 1
            ell = L3 / (nm(C) * nm(t))
            Ct = union(C, t); C4 = power(elt(C), 4)
            ns = [n for n in cols3 if coprime(n, Ct) and nm(n) <= bI * ell]
            for d in divisors(C):
                wCd = H3 * nm(C) / (nm(d) * L3 * L3 * F3)
                Ycd = cI * Sig * L3 * F3 * nm(d) / (H3 * nm(C) ** 2)
                Ymin = min(Ymin, Ycd)
                YA, YB = lattice_points(14 * Ycd + 30); YN = YA * YA - YA * YB + YB * YB
                de = elt(d)
                Pv = np.zeros(YA.shape, dtype=complex); P0 = 0j
                for n in ns:
                    c = mu(n) * xi1(n) * chi_el(n, C4) * chi_el(n, de) * complex(Ufun(nm(n) / ell))
                    if c == 0: continue
                    Pv += c * np.conj(CHarr(n, YA, YB))
                    if not n: P0 += c
                Q += wCd * (np.sum(Phi(YN / Ycd) * np.abs(Pv) ** 2) + abs(P0) ** 2)
                Zt += wCd * Ycd * hatPhi(0.0) * sum(abs(complex(Ufun(nm(g) / ell))) ** 2 * phi_ratio(g) for g in ns)
    return complex(Q), Zt, nCt, Ymin
Q3, Z3, nCt, Ymin = Q_direct_and_Z()
print("(C,t) pairs:", nCt, "  min Y_{C,d} = %.4g (Y < 1 occurs)" % Ymin)

def T3_rhs(variant=None):
    tot = 0j
    Rm = TCUT * H3 * L3 * bI * bI / (cI * Sig * F3) + 10
    MA, MB = lattice_points(Rm); MN = MA * MA - MA * MB + MB * MB
    CHm = {key(n): CHarr(n, MA, MB) for n in cols3}
    nrf = 0
    for r in cols3:
        for fp in cols3:
            if not coprime(r, fp) or nm(r) * nm(fp) > 2 * v3 * L3: continue
            nrf += 1
            X0 = L3 / (nm(r) * nm(fp))
            weight = cI * Sig / L3 ** 2 * nm(r) * (tau(r) if variant != "tau_to_1" else 1)
            fp5 = power(elt(fp), 5)
            nn = [n for n in cols3 if coprime(n, union(r, fp)) and nm(n) <= bI * X0]
            if variant == "no_divisibility":
                # wrong: k' unrestricted (sum over all k' != 0 instead of f' | k')
                KA_, KB_ = lattice_points(TCUT * H3 * L3 * bI * bI / (cI * Sig * F3 * nm(r) ** 2) + 10)
                KN_ = KA_ * KA_ - KA_ * KB_ + KB_ * KB_
            for n1 in nn:
                x1 = nm(n1) / X0; u1 = complex(U0fun(x1))
                if u1 == 0: continue
                for n2 in nn:
                    x2 = nm(n2) / X0; u2 = complex(U0fun(x2))
                    if u2 == 0: continue
                    Psi2 = xi1(n1) * np.conj(xi1(n2)) * Gquot(n2, n1) * a(n1) * np.conj(a(n2))
                    if variant == "no_divisibility":
                        ks = np.sum(CHarr(n1, KA_, KB_) * np.conj(CHarr(n2, KA_, KB_)) * chi_el(n1, power(elt(fp), 4)) * np.conj(chi_el(n2, power(elt(fp), 4)))
                                    * hatPhi(cI * Sig * F3 * KN_ * nm(r) ** 2 / (H3 * L3 * x1 * x2)))
                    else:
                        # k' = f' m : chi_n(k') chi_n(f')^4 = chi_n(f')^5 chi_n(m),  N(k') = N(f') N(m)
                        c12 = chi_el(n1, fp5) * np.conj(chi_el(n2, fp5))
                        ks = c12 * np.sum(CHm[key(n1)] * np.conj(CHm[key(n2)]) *
                                          hatPhi(cI * Sig * F3 * nm(fp) * MN * nm(r) ** 2 / (H3 * L3 * x1 * x2)))
                    tot += weight * Psi2 * u1 * np.conj(u2) * ks
    return tot, nrf
R3, nrf = T3_rhs()
print("(r,f') pairs:", nrf)
report("T3 Lemma 7.3: Q = calZ + (r,f',k') form", Q3, Z3 + R3)
print("  calZ =", Z3, " |Q - calZ| =", abs(Q3 - Z3))
control("T3 (tau(r) replaced by 1)", Q3, Z3 + T3_rhs("tau_to_1")[0], abs(Q3 - Z3))
control("T3 (restriction f'|k' dropped)", Q3, Z3 + T3_rhs("no_divisibility")[0], abs(Q3 - Z3))
print("  [T3 time %.1fs]" % (time.time() - T0))

# ================================================================ T4: abstract preimage count
print("=" * 30, "T4  per-prime preimage count (l.2550-2568)")
primes_abs = list(range(7))
bad4 = 0; n4 = 0
for r_mask in range(1 << 7):
    for f_mask in range(1 << 7):
        if r_mask & f_mask: continue
        if bin(r_mask).count("1") + bin(f_mask).count("1") > 5: continue
        for k_mask in range(1 << 7):     # prime support of k' (exponents > 1 irrelevant)
            # enumerate (t, C, e, w, d) with t|r, f'=C e w disjoint, e|k', (w,k')=1, d|(C,k')
            s = 0
            fl = [p for p in primes_abs if f_mask >> p & 1]
            rl = [p for p in primes_abs if r_mask >> p & 1]
            for tsub in range(1 << len(rl)):
                for assign in itertools.product(range(3), repeat=len(fl)):
                    Cm = sum(1 << fl[i] for i in range(len(fl)) if assign[i] == 0)
                    em = sum(1 << fl[i] for i in range(len(fl)) if assign[i] == 1)
                    wm = sum(1 << fl[i] for i in range(len(fl)) if assign[i] == 2)
                    if em & ~k_mask: continue            # e | k'
                    if wm & k_mask: continue             # (w, k') = 1
                    CK = Cm & k_mask
                    nd = 1 << bin(CK).count("1")         # d | (C, k')
                    s += nd * (-1) ** bin(em).count("1") * (-1) ** bin(wm).count("1")
            target = (1 << len(rl)) * (1 if (f_mask & ~k_mask) == 0 else 0)
            n4 += 1
            if s != target: bad4 += 1
print("T4 cases %d failures %d" % (n4, bad4))
tests += 1; fails += (bad4 > 0)

# ================================================================ T5: symbolic scale identities
print("=" * 30, "T5  symbolic scale identities")
import sympy as sp
Hs, Ls, Fs, Ss, cIs, NC, Nd, Nt, Ng, Ne, Nw, Nh, Rs, Fps, Nr, Nk, Nfp, v_ = sp.symbols(
    'H L F Sigma c_I NC Nd Nt Ng Ne Nw Nh R Fp Nr Nk Nfp v', positive=True)
ell = Ls / (NC * Nt); w = Hs * NC / (Nd * Ls ** 2 * Fs); Ycd = cIs * Ss * Ls * Fs * Nd / (Hs * NC ** 2)
subs_r = {Nr: Nt * Ng / Ne, Nfp: NC * Ne * Nw, Nk: Nd * Ne * Nh}
chk = []
chk.append(("X'_0 = ell/(N g N w) = L/(N r N f')", sp.simplify(ell / (Ng * Nw) - (Ls / (Nr * Nfp)).subs(subs_r))))
chk.append(("w Y N(g)/(N(e) ell) = c_I Sigma N(r)/L^2", sp.simplify(w * Ycd * Ng / (Ne * ell) - (cIs * Ss * Nr / Ls ** 2).subs(subs_r))))
chk.append(("Y N(h) N(g)^2/(N(e) ell^2) = c_I Sigma F N(k') N(r)^2/(H L)",
            sp.simplify(Ycd * Nh * Ng ** 2 / (Ne * ell ** 2) - (cIs * Ss * Fs * Nk * Nr ** 2 / (Hs * Ls)).subs(subs_r))))
chk.append(("w Y ell = c_I Sigma/(N(C)^2 N(t))", sp.simplify(w * Ycd * ell - cIs * Ss / (NC ** 2 * Nt))))
# Lemma 7.1 normalisation: (1/(LF)) * H * mu(d)/N(d) * 1/sqrt(Nu1 Nu2), Nu_i = Nt * Nx_i, z_i = NC Nt Nx_i / L
Nx1, Nx2 = sp.symbols('Nx1 Nx2', positive=True)
z1 = NC * Nt * Nx1 / Ls; z2 = NC * Nt * Nx2 / Ls
chk.append(("(H/(LF)) /(N(d) sqrt(Nu1 Nu2)) = w_{C,d} (z1 z2)^{-1/2}",
            sp.simplify(Hs / (Ls * Fs) / (Nd * Nt * sp.sqrt(Nx1 * Nx2)) - w / sp.sqrt(z1 * z2))))
chk.append(("H N(h)/(N(d) Nu1 Nu2) = H N(h) N(C)^2/(L^2 N(d) z1 z2)",
            sp.simplify(Hs * Nh / (Nd * Nt ** 2 * Nx1 * Nx2) - Hs * Nh * NC ** 2 / (Ls ** 2 * Nd * z1 * z2))))
Xp = Ls / (Rs * Fps); Sp = Xp * Fps; Hp = Hs * Ls / (Ss * Fs * Rs ** 2)
chk.append(("Sigma' = X'F' = L/R", sp.simplify(Sp - Ls / Rs)))
chk.append(("H'/Sigma' = H/(Sigma F R)", sp.simplify(Hp / Sp - Hs / (Ss * Fs * Rs))))
chk.append(("(Sigma R/L^2) R (Sigma')^2 = Sigma", sp.simplify((Ss * Rs / Ls ** 2) * Rs * Sp ** 2 - Ss)))
# y-range domination: 4 C_Phi v^2 L^2 F^2 N(d)/(H N(C)^2) <= Y_{C,d}  <=>  4 C_Phi v^2 L F <= c_I Sigma
CPhi = sp.symbols('C_Phi', positive=True)
ratio = sp.simplify((4 * CPhi * v_ ** 2 * Ls ** 2 * Fs ** 2 * Nd / (Hs * NC ** 2)) / Ycd)
chk.append(("N(y)max / Y_{C,d} = 4 C_Phi v^2 L F/(c_I Sigma)", sp.simplify(ratio - 4 * CPhi * v_ ** 2 * Ls * Fs / (cIs * Ss))))
for name, val in chk:
    tests += 1
    ok = (val == 0)
    if not ok: fails += 1
    print("%-64s %s" % (name, "OK" if ok else "FAIL: %s" % val))

print("=" * 30)
print("TOTAL tests %d failures %d   (time %.1fs)" % (tests, fails, time.time() - T0))
