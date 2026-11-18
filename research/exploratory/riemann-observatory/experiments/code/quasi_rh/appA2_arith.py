# appA2_arith.py -- exact/numerical checks of the arithmetic layer of App. A.2 of
# "The Quasi-Riemann Hypothesis" (paper2.tex l.2874-3282, l.3438-3450).
# Own code only (appA_zw.py); nothing from the OpenAI repository.  Run: python3 -I appA2_arith.py
import sys, os, math, cmath, itertools, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy
import appA_zw as Z
from appA_zw import mul, add, sub, neg, conj, norm, ONE, ZERO, LAM, UNITS, ZETA6, W

random.seed(20261117)
TOL = 1e-9
FAIL = []; COUNT = {}
def check(tag, ok, info=None):
    COUNT[tag] = COUNT.get(tag, 0) + 1
    if not ok:
        FAIL.append((tag, info))
        if len([f for f in FAIL if f[0] == tag]) <= 3: print("FAIL", tag, info)
def close(a, b, tol=TOL): return abs(a - b) < tol
t0 = time.time()

def vval(x, q):
    """q-adic valuation of nonzero x."""
    k = 0
    while Z.divides(q, x): x = Z.exdiv(x, q); k += 1
    return k
def gcd(x, y):
    g, _, _ = Z.egcd(x, y); return g
def cub_direct(x, d):
    """(x/d)_3 exponent of omega via the sextic table (d primary coprime to 6), None if not coprime."""
    k = Z.chi_fast(d, x)
    return None if k is None else (2 * k) % 6 // 2
def cub(x, d):
    if norm(d) == 1: return 0
    return Z.cubic_sym_recip(x, d)

# ---- 0. validate the reciprocity-based cubic symbol against the direct definition ----
prim = [x for x in ((a, b) for a in range(-25, 26) for b in range(-25, 26))
        if Z.is_primary(x) and 1 < norm(x) <= 500 and math.gcd(norm(x), 6) == 1]
for d in prim[:120]:
    for _ in range(25):
        x = (random.randint(-60, 60), random.randint(-60, 60))
        if Z.is_zero(x): continue
        check("A2.0 cubic_sym_recip==direct", Z.cubic_sym_recip(x, d) == cub_direct(x, d), (x, d))
print("validated reciprocity-based cubic symbol %.1fs" % (time.time() - t0))

# ---- setup: S = {lambda, 2}, Psi_0 a character mod 2 (conductor supported on S) ----
def chi6c(n, x, j):
    k = Z.chi_fast(n, x)
    if k is None: return 0
    return ZETA6 ** ((j * k) % 6)
def Psi0(n, which):
    if which == 0: return 1.0
    k = [k for k in range(3) if Z.cong(n, Z.pw((0, 1), k), (2, 0))][0]
    return W ** k               # n -> (n/-2)_3, a character of (O/2)^x
def phi(x, which):
    if not Z.is_primary(x) or Z.divides((2, 0), x): return 0
    if norm(x) == 1: return Psi0(x, which)   # x = 1
    return ZETA6 ** ((2 * Z.chi_fast(x, LAM)) % 6) * Psi0(x, which)

for Lval in [(18, 0)]:
    L = Lval
    # ---- 1. phi periodic mod L ----
    for which in (0, 1):
        for _ in range(400):
            x = (random.randint(-40, 40), random.randint(-40, 40))
            t = (random.randint(-5, 5), random.randint(-5, 5))
            if Z.is_zero(x) or Z.is_zero(add(x, mul(L, t))): continue
            check("A2.1 phi periodic mod L", close(phi(x, which), phi(add(x, mul(L, t)), which)), (x, t))
    RES_L = Z.residues(L)
    def phihat(h0, which):
        return sum(phi(x, which) * Z.e_xn(neg(mul(h0, x)), L) for x in RES_L if not Z.is_zero(x)) / norm(L)
    PHIHAT = {which: {h0: phihat(h0, which) for h0 in RES_L} for which in (0, 1)}
    for which in (0, 1):
        check("A2.1 |phihat|<=1", max(abs(v) for v in PHIHAT[which].values()) <= 1 + 1e-12)
        check("A2.1 sum phihat = phi(0) = 0", close(sum(PHIHAT[which].values()), 0))
        for _ in range(60):
            x = (random.randint(-30, 30), random.randint(-30, 30))
            s = sum(PHIHAT[which][h0] * Z.e_xn(mul(x, h0), L) for h0 in RES_L)
            check("A2.1 Fourier inversion of phi", close(s, phi(x, which) if not Z.is_zero(x) else 0), x)
print("phi / phihat done %.1fs" % (time.time() - t0))

# ---- 2. (eq:ray-fourier) and the e(-y/p) Gauss sum ----
def gam(p, j):
    return Z.gauss(p, j % 6) if j % 6 else None
GAM = {}
def G(p, j):
    key = (p, j % 6)
    if key not in GAM: GAM[key] = Z.gauss(p, j % 6)
    return GAM[key]
def C_def(p, j, h):
    return sum(chi6c(p, y, j) * Z.e_xn(neg(mul(h, y)), p) for y in Z.residues(p)) / norm(p)
def C_claim(p, j, h):
    N = norm(p)
    if j % 6 != 0:
        if Z.divides(p, h): return 0
        return N ** -0.5 * chi6c(p, (-1, 0), j) * G(p, j) * chi6c(p, h, -j)
    return (1 - 1 / N) if Z.divides(p, h) else -1 / N
pr_small = [p for p in Z.primary_primes(200)]
for p in pr_small:
    for j in range(6):
        for h in Z.residues(p):
            check("A2.2 ray-fourier", close(C_def(p, j, h), C_claim(p, j, h)), (p, j, h))
        for x in random.sample(Z.residues(p), min(25, norm(p))):
            s = sum(C_claim(p, j, h) * Z.e_xn(mul(h, x), p) for h in Z.residues(p))
            check("A2.2 local Fourier inversion", close(s, chi6c(p, x, j)), (p, j, x))
print("ray-fourier done (%d primes, N<=200) %.1fs" % (len(pr_small), time.time() - t0))

# ---- 3. e(z) = breve-e(z/lambda); translation of Fourier modes ----
for _ in range(500):
    num = (random.randint(-99, 99), random.randint(-99, 99)); den = (random.randint(1, 40), random.randint(-40, 40))
    if Z.is_zero(den): continue
    check("A2.3 e(z)=ebreve(z/lambda)", close(Z.e_xn(num, den), Z.eb_xn(num, mul(den, LAM))), (num, den))
# e is trivial on O and O is self-dual: e(x y) = 1 for all y in O iff x in O (spot check x = 1/q)
# nondegeneracy of (x, h) -> e(x h / q) on O/q: sum_x e(h x/q) = N(q) [h == 0 mod q] (needed for Fourier inversion)
for q in [(2, 0), LAM, (5, 0), (1, 3), (18, 0), (4, 2)]:
    for h in Z.residues(q):
        s_ = sum(Z.e_xn(mul(h, y), q) for y in Z.residues(q))
        check("A2.3 nondegenerate pairing O/q", close(s_, norm(q) if Z.divides(q, h) else 0), (q, h))

# ---- 4-10. the cusp construction, multiplier, additive CRT, local transform, summed scalar ----
# Variant (env APPA_EXTRA_S=1): S also contains the split prime pi_7 above 7, so L = 18 pi_7 and the active
# primes are taken from {13, 19, 31, 25}; this exercises the CRT for delta' with an extra prime of M.
EXTRA = os.environ.get("APPA_EXTRA_S") == "1"
PI7 = Z.primary_assoc(Z.split_prime(7))
L = mul((18, 0), PI7) if EXTRA else (18, 0)
M = mul(Z.pw(LAM, 12), Z.pw(L, 4)); M2 = mul(M, M)
QM = [LAM, (-2, 0)] + ([PI7] if EXTRA else [])   # primes dividing M (and L)
print("cusp section: L =", L, "N(L) =", norm(L), "primes of M:", QM)
def ppart(x, q):  # q^{v_q(x)}
    return Z.pw(q, vval(x, q))
def crt2(r1, m1, r2, m2):
    """x == r1 mod m1, x == r2 mod m2 (coprime moduli)."""
    inv = Z.inv_mod(m1, m2)
    t = Z.rmod(mul(sub(r2, r1), inv), m2)
    return Z.rmod(add(r1, mul(m1, t)), mul(m1, m2))

def construct(h0, hp, js, which=0, verbose=False):
    """h0 in O/L; hp: dict prime -> nonzero residue (active primes).  Returns data dict."""
    act = sorted(hp, key=norm)
    r = ONE
    for p in act: r = mul(r, p)
    # representatives h_p == 0 mod M^2
    ht = {}
    for p in act:
        ht[p] = mul(M2, Z.rmod(mul(Z.inv_mod(M2, p), hp[p]), p))
        check("A2.4 rep h_p == h mod p, 0 mod M^2", Z.cong(ht[p], hp[p], p) and Z.divides(M2, ht[p]))
    # z_h = lambda^2 (h0/L + sum h_p/p) = Num / Den
    Den = mul(L, r)
    Num = mul(h0, r)
    for p in act: Num = add(Num, mul(ht[p], mul(L, Z.exdiv(r, p))))
    Num = mul(mul(LAM, LAM), Num)
    g = gcd(Num, Den) if not Z.is_zero(Num) else Den
    a = Z.exdiv(Num, g); c = Z.exdiv(Den, g)
    # reduced denominator of lambda^2 h0 / L
    num0 = mul(mul(LAM, LAM), h0)
    g0 = gcd(num0, L) if not Z.is_zero(num0) else L
    c0raw = Z.exdiv(L, g0)
    # claim: c = c0 r up to a unit
    q = mul(c0raw, r)
    check("A2.4 reduced denominator c = c0 r (unit)", Z.divides(q, c) and Z.divides(c, q), (h0, act, c, q))
    # normalisation
    if Z.divides(LAM, c):
        u = [u for u in UNITS if Z.is_primary(mul(u, a))][0]
    else:
        u = [u for u in UNITS if Z.is_primary(mul(u, c))][0]
    a = mul(u, a); c = mul(u, c)
    c0 = Z.exdiv(c, r)
    check("A2.4 gcd(a,c)=1", Z.is_unit(gcd(a, c)))
    # a = lambda^2 c (h0/L + sum h_p/p) exactly
    # cross-multiplied: a * (L r) == c * lambda^2 (h0 r + sum ht_p L r/p)
    check("A2.4 a = lambda^2 c (h0/L + sum h_p/p)", mul(a, Den) == mul(c, Num))
    # delta' by CRT
    Q1 = r; Q2 = ONE
    for qq in QM:
        if Z.divides(qq, c0):
            Q1 = mul(Q1, Z.pw(qq, vval(M, qq) + vval(c0, qq)))
        else:
            Q2 = mul(Q2, Z.pw(qq, vval(M, qq)))
    ainvQ1 = Z.inv_mod(a, Q1)
    dp = crt2(ainvQ1, Q1, ZERO, Q2)
    check("A2.5 delta' congruences", Z.cong(mul(a, dp), ONE, Q1) and Z.divides(Q2, dp))
    bg = Z.exdiv(sub(mul(a, dp), ONE), c)
    # b_g congruences
    for qq in QM:
        mod = Z.pw(qq, vval(M, qq))
        if Z.divides(qq, c0):
            check("A2.5 b_g == 0 mod q^v(M) (q|c0)", Z.divides(mod, bg))
        else:
            check("A2.5 b_g == -c^{-1} mod q^v(M) (q|M, q!|c0)", Z.cong(mul(bg, c), (-1, 0), mod))
    # g in SL2
    check("A2.5 det g = 1", sub(mul(a, dp), mul(bg, c)) == ONE)
    vl = vval(c, LAM)
    if vl >= 2:
        case = 1; Hm = (ONE, ZERO, ZERO, ONE); u0 = None
    elif vl == 1:
        case = 2
        u0 = [u for u in (LAM, neg(LAM)) if Z.cong(u, c, (3, 0))]
        check("A2.5 u0 unique (case 2)", len(u0) == 1); u0 = u0[0]
        Hm = (ONE, ZERO, u0, ONE)
    else:
        case = 3
        u0 = Z.red(a, (3, 0))
        Hm = (u0, (-1, 0), ONE, ZERO)
    # H^{-1} for det 1: (d -b; -c a)
    Ha, Hb, Hc, Hd = Hm
    check("A2.5 det H = 1", sub(mul(Ha, Hd), mul(Hb, Hc)) == ONE)
    Hi = (Hd, neg(Hb), neg(Hc), Ha)
    ga, gb, gc, gd = a, bg, c, dp
    a1 = add(mul(ga, Hi[0]), mul(gb, Hi[2])); b1 = add(mul(ga, Hi[1]), mul(gb, Hi[3]))
    c1 = add(mul(gc, Hi[0]), mul(gd, Hi[2])); d1 = add(mul(gc, Hi[1]), mul(gd, Hi[3]))
    THREE = (3, 0)
    check("A2.5 g1 == I mod 3", Z.cong(a1, ONE, THREE) and Z.divides(THREE, b1) and Z.divides(THREE, c1) and Z.cong(d1, ONE, THREE), (case, a1, c1))
    # Kubota multiplier kappa(g1) = (c1/a1)_3
    kap = 0 if Z.is_zero(c1) else cub(c1, a1)
    # the paper's formula (eq:ray-multiplier)
    ar = cub(a, r)
    if case == 1:
        claim = (cub(c0, a) + ar) % 3
    elif case == 2:
        a_1 = sub(a, mul(u0, bg))
        check("A2.5 case2 congruence a(c-u0 d') == -u0 mod (a-u0 b_g)", Z.cong(mul(a, sub(c, mul(u0, dp))), neg(u0), a_1))
        check("A2.5 case2 congruence b_g c == -1 mod a", Z.cong(mul(bg, c), (-1, 0), a))
        claim = (cub(neg(u0), a_1) + cub(Z.exdiv(c0, u0), a) + ar) % 3
    else:
        check("A2.5 case3 -b_g c = 1 - a d' == 1 mod 9", Z.cong(neg(mul(bg, c)), ONE, (9, 0)) and neg(mul(bg, c)) == sub(ONE, mul(a, dp)))
        check("A2.5 case3 (d'/(-b_g c))_3 = 1", cub(dp, neg(mul(bg, c))) == 0)
        claim = ((cub(a, c0) if norm(c0) > 1 else 0) + ar) % 3
    check("A2.5 ray-multiplier formula (case %d)" % case, kap == claim, (h0, act, kap, claim))
    kappa0 = (kap - ar) % 3
    return dict(a=a, c=c, c0=c0, r=r, dp=dp, bg=bg, case=case, u0=u0, kap=kap, kappa0=kappa0,
                a1=a1, c1=c1, act=act, H=Hm)

def sigma_eps(c, p):
    sig = Z.rmod(mul(mul(LAM, LAM), Z.exdiv(c, p)), p)
    eps = Z.rmod(neg(Z.inv_mod(mul(mul(Z.pw(LAM, 3), Z.exdiv(c, p)), sig), p)), p)
    return sig, eps
def omega_pj(p, j, eps):
    N = norm(p)
    # G(p, j) is the NORMALISED Gauss sum gamma_j(p) (appA_zw.gauss divides by sqrt N)
    if j == 4: return G(p, 4)
    if j == 0: return -G(p, 2) * chi6c(p, eps, -2)
    return chi6c(p, (-1, 0), j) * G(p, j) * G(p, j + 2) * chi6c(p, eps, -j - 2)
def B_pj(p, j, x):
    N = norm(p)
    if j == 4: return N ** -0.5 * (-1 + N * (1 if Z.divides(p, x) else 0))
    if j == 0: return N ** -0.5 * chi6c(p, x, -2)
    return chi6c(p, x, -j - 2)

# configurations: h0 chosen to realise the three cases of v_lambda(c0)
RES_L = Z.residues(L)
def c0_of(h0):
    num0 = mul(mul(LAM, LAM), h0)
    if Z.is_zero(num0): return ONE
    return Z.exdiv(L, gcd(num0, L))
byv = {0: [], 1: [], 2: []}
for h0 in RES_L:
    v = vval(c0_of(h0), LAM)
    byv[min(v, 2)].append(h0)
print("h0 classes by v_lambda(c0):", {k: len(v) for k, v in byv.items()})
P7, P13, P19, P25 = Z.split_prime(7), Z.split_prime(13), Z.split_prime(19), (-5, 0)
P7 = Z.primary_assoc(P7); P13 = Z.primary_assoc(P13); P19 = Z.primary_assoc(P19)
if EXTRA: P7 = Z.primary_assoc(Z.split_prime(31))   # keep the active primes outside S
configs = []
for v in (0, 1, 2):
    for h0 in random.sample(byv[v], 3 if not EXTRA else 2):
        for act_js in ([(P7, 1)], [(P7, 0)], [(P7, 4)], [(P13, 2)], [(P13, 3)], [(P13, 5)], [(P25, 1)],
                       [(P7, 1), (P13, 1)], [(P7, 1), (P13, 4)], [(P7, 0), (P19, 1)]):
            configs.append((h0, act_js))
print("configurations:", len(configs))
nconf = 0
for h0, act_js in configs:
    js = dict(act_js)
    act = [p for p, _ in act_js]
    tuples = list(itertools.product(*[[h for h in Z.residues(p) if not Z.is_zero(h)] for p in act]))
    datas = []
    for tup in tuples:
        hp = dict(zip(act, tup))
        d = construct(h0, hp, js)
        d['hp'] = hp
        datas.append(d)
    # kappa0, c, c0, case, delta'_0 mod D0 independent of the nonzero h_p
    D0 = mul(Z.pw(LAM, 3), datas[0]['c0'])
    k0set = {d['kappa0'] for d in datas}
    check("A2.6 kappa0 independent of h_p", len(k0set) == 1, (h0, act_js, k0set))
    check("A2.6 c, case independent of h_p", len({(d['c'], d['case']) for d in datas}) == 1)
    check("A2.6 delta'_0 mod D0 independent of h_p", len({Z.red(d['dp'], D0) for d in datas}) == 1)
    check("A2.6 a mod M c0 independent of h_p", len({Z.red(d['a'], mul(M, d['c0'])) for d in datas}) == 1)
    c = datas[0]['c']; c0 = datas[0]['c0']; r = datas[0]['r']; kappa0 = datas[0]['kappa0']
    dp0 = Z.red(datas[0]['dp'], D0); rinv = Z.inv_mod(r, D0)
    se = {p: sigma_eps(c, p) for p in act}
    for d in datas:
        for p in act:
            check("A2.7 a == sigma_p h_p mod p", Z.cong(d['a'], mul(se[p][0], d['hp'][p]), p))
    # test frequencies x = lambda^4 ell
    xs = [(random.randint(-200, 200), random.randint(-200, 200)) for _ in range(40)]
    xs += [mul(p, (random.randint(-9, 9), random.randint(-9, 9))) for p in act for _ in range(4)]
    xs += [ZERO]
    lam4c = mul(Z.pw(LAM, 4), c)
    for x in xs:
        psi = Z.e_xn(neg(mul(mul(dp0, rinv), x)), D0)
        # 8. additive CRT for every tuple
        for d in datas[:12]:
            lhs = Z.eb_xn(neg(mul(d['dp'], x)), lam4c)
            rhs = psi
            for p in act:
                rhs *= Z.e_xn(mul(mul(se[p][1], Z.inv_mod(d['hp'][p], p)), x), p)
            check("A2.8 additive CRT", close(lhs, rhs), (h0, act_js, x))
        # 9. local transform per prime with the actual sigma_p, eps_p
        for p in act:
            j = js[p]; sig, eps = se[p]
            lhs = 0
            for h in Z.residues(p):
                if Z.is_zero(h): continue
                a_h = mul(sig, h)
                lhs += C_claim(p, j, h) * chi6c(p, a_h, -2) * Z.e_xn(mul(mul(eps, Z.inv_mod(h, p)), x), p)
            rhs = chi6c(p, sig, -2) * omega_pj(p, j, eps) * B_pj(p, j, x)
            check("A2.9 local transform (j=%d)" % j, close(lhs, rhs), (p, j, x))
        # 10. summed identity with the true multipliers kappa(g1) of every tuple
        S = 0
        for d in datas:
            cf = 1
            for p in act: cf *= C_claim(p, js[p], d['hp'][p])
            S += cf * (W ** d['kap']).conjugate() * Z.eb_xn(neg(mul(d['dp'], x)), lam4c)
        claim = (W ** kappa0).conjugate() * psi
        for p in act:
            sig, eps = se[p]
            claim *= chi6c(p, sig, -2) * omega_pj(p, js[p], eps) * B_pj(p, js[p], x)
        check("A2.10 summed identity -> scalar * psi * prod B", close(S, claim, 1e-8), (h0, act_js, x, S, claim))
    # |omega_pj| = 1
    for p in act:
        check("A2.9 |omega_pj|=1", close(abs(omega_pj(p, js[p], se[p][1])), 1.0))
    # B_{p,1} is quadratic: B_{p,1}(x) = chi_p(x)^3 in {+-1, 0}
    for p in act:
        if js[p] == 1:
            for x in Z.residues(p):
                b = B_pj(p, 1, x)
                check("A2.9 B_p1 = chi_p^3 real quadratic", close(b, chi6c(p, x, 3)) and abs(b.imag) < 1e-12 and (abs(abs(b) - 1) < 1e-12 or Z.divides(p, x)))
    nconf += 1
    if nconf % 15 == 0: print("  configs done:", nconf, "%.1fs" % (time.time() - t0))
print("cusp construction checks done %.1fs" % (time.time() - t0))

# ---- 11. H -> gamma_sigma reduction (matrix identities) ----
def mm(A, B):
    a, b, c, d = A; e, f, g, h = B
    return (add(mul(a, e), mul(b, g)), add(mul(a, f), mul(b, h)), add(mul(c, e), mul(d, g)), add(mul(c, f), mul(d, h)))
def minv(A):
    a, b, c, d = A; return (d, neg(b), neg(c), a)
def in_Z_plus_3O(x): return x[1] % 3 == 0
gp = (ONE, ZERO, (0, 1), ONE); gm = (ONE, ZERO, (-1, -1), ONE)   # gamma_+ (omega), gamma_- (omega^2)
E = (ZERO, (-1, 0), ONE, ZERO)
# case 2: (1 0; u0 1) gamma_sigma^{-1} = (1 0; x 1) with x in Z+3O
for u0, gs, name in ((LAM, gm, "-"), (neg(LAM), gp, "+")):
    X = mm((ONE, ZERO, u0, ONE), minv(gs))
    check("A2.11 case2 H gamma_%s^-1 lower unipotent in Z+3O" % name, X[0] == ONE and X[1] == ZERO and X[3] == ONE and in_Z_plus_3O(X[2]), X)
    for gs2, name2 in ((gp, "+"), (gm, "-")):
        if gs2 is gs: continue
        X2 = mm((ONE, ZERO, u0, ONE), minv(gs2))
        check("A2.11 case2 wrong pairing excluded", not in_Z_plus_3O(X2[2]), (name, name2))
# case 3: (u0 -1; 1 0) = T_{u0} E ; u0 = m + b w ; b mod 3 decides the cusp
for u0 in [(i, j) for i in range(3) for j in range(3)]:
    Hm = (u0, (-1, 0), ONE, ZERO)
    check("A2.11 case3 H = T_u0 E", mm((ONE, u0, ZERO, ONE), E) == Hm)
    b = u0[1] % 3
    if b == 0:
        X = mm((ONE, neg(u0), ZERO, ONE), Hm)   # T_{-u0} H = E in SL2(Z)
        check("A2.11 case3 b=0 -> gamma_0", X == E)
    elif b == 1:
        # T_{w} E = (-1 -1; 1 0) gamma_-
        X = mm(mm((ONE, sub((0, 1), u0), ZERO, ONE), Hm), minv(gm))
        check("A2.11 case3 b=1 -> gamma_- via SL2(Z)", all(t[1] == 0 for t in X) and in_Z_plus_3O(sub((0, 1), u0)), X)
    else:
        X = mm(mm((ONE, sub((0, -1), u0), ZERO, ONE), Hm), minv(gp))
        check("A2.11 case3 b=2 -> gamma_+ via SL2(Z)", all(t[1] == 0 for t in X) and in_Z_plus_3O(sub((0, -1), u0)), X)

# ---- 12. Lemma 6.3 uniformity: replace k0 by a huge prime k0' == k0 mod M^2 ----
def huge_prime_in_class(p, tries=4000):
    out = []
    for t1 in range(1, 200):
        for t2 in range(-3, 4):
            x = add(p, mul(M2, (t1, t2)))
            n = norm(x)
            if n % 3 == 1 and sympy.isprime(n):
                out.append(x)
                if len(out) >= 2: return out
    return out
unif = 0
for v in (0, 1, 2):
    for h0 in random.sample(byv[v], 2 if not EXTRA else 1):
        for base in ([(P7, 1)], [(P7, 1), (P13, 4)], [(P13, 1), (P19, 0)]):
            k0 = base[0][0]
            fixed = base[1:]
            reps = huge_prime_in_class(k0)
            for k0p in [k0] + reps:
                check("A2.12 k0' primary prime == k0 mod M^2", Z.is_primary(k0p) and Z.cong(k0p, k0, M2) and sympy.isprime(norm(k0p)))
            res = []
            for k0p in [k0] + reps:
                act = [k0p] + [p for p, _ in fixed]
                hp = {}
                for p in act:
                    while True:
                        h = (random.randint(-50, 50), random.randint(-50, 50))
                        if not Z.divides(p, h): break
                    hp[p] = h
                d = construct(h0, hp, None)
                D0 = mul(Z.pw(LAM, 3), d['c0'])
                rbase = k0
                for p, _ in fixed: rbase = mul(rbase, p)
                check("A2.12 r == r_base mod M^2", Z.cong(d['r'], rbase, M2))
                res.append((d['kappa0'], d['case'], d['u0'], d['c0'], Z.red(d['dp'], D0), Z.red(Z.inv_mod(d['r'], D0), D0)))
            check("A2.12 (kappa0, cusp case, u0, c0, delta'_0, r^-1 mod D0) constant on the class of k0 mod M^2",
                  len(set(res)) == 1, (h0, base, res))
            unif += len(res)
print("uniformity: %d constructions, norms of k0' up to %.2e  %.1fs" % (unif, max(norm(x) for x in reps) if reps else 0, time.time() - t0))

print()
print("SUMMARY (check: number of cases)")
for k in sorted(COUNT): print("  %-70s %6d" % (k, COUNT[k]))
print("TOTAL cases:", sum(COUNT.values()), " FAILURES:", len(FAIL))
for f in FAIL[:20]: print("  ", f)
print("time %.1fs" % (time.time() - t0))
