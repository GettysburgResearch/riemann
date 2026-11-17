# Level-2 audit, Section 4: independent numerical checks of Lemma 4.1 (paper2.tex l.823-857)
# and of the App. A.1 ingredients it rests on (l.2691-2872).
# Run:  python3 -I s4_lemma41_checks.py
import sys, os, itertools, math, cmath
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s4_zw import *

TOL = 1e-8
fails = {}
counts = {}
def check(name, ok):
    counts[name] = counts.get(name, 0) + 1
    if not ok:
        fails[name] = fails.get(name, 0) + 1

P = eisenstein_primes(400)          # primes prime to 6, norm <= 400 (split and inert 5,11,17)
print("primes:", len(P), "inert:", [p.g for p in P if not p.split])
MINUS1 = (-1, 0); FOUR = (4, 0)

def G_sqfree(ps):
    return chi(ps, FOUR).conjugate() * gamma(ps, 3)

# ---------- prime case + composite case of (gj), (g), (convert1), (convert2) ----------
sq = [ps for ps in squarefree_products(P, 2500) if ps]
sq = [ps for ps in sq if len(ps) <= 3]
print("squarefree test moduli:", len(sq))
Gcache = {}
for ps in sq:
    n = elt(ps); mu = (-1) ** len(ps); al = alpha(n)
    g1 = gamma(ps, 1); g2 = gamma(ps, 2); g3 = gamma(ps, 3); gm1 = gamma(ps, -1)
    G = chi(ps, FOUR).conjugate() * g3
    Gcache[n] = G
    check("|gamma_j|=1", abs(abs(g1) - 1) < TOL and abs(abs(g2) - 1) < TOL and abs(abs(g3) - 1) < TOL)
    check("(gj) gamma2^3 = mu alpha", abs(g2 ** 3 - mu * al) < TOL)
    check("(gj) gamma1 gamma2 = mu alpha G", abs(g1 * g2 - mu * al * G) < TOL)
    check("(g) gamma1 gamma_{-1} = chi_n(-1)", abs(g1 * gm1 - chi(ps, MINUS1)) < TOL)
    check("(convert1)", abs(al.conjugate() * g2 * g1 - mu * G) < TOL)
    check("(convert2)", abs(mu * gm1 - chi(ps, MINUS1) / G * al.conjugate() * g2) < TOL)
    check("gamma3 = Gamma_quad (squarefree)", abs(g3 - gamma_quad(n)) < TOL)

# ---------- G is a class function mod 4; chi_c(4) depends on c mod 2 ----------
Gclass = {}
for n, G in Gcache.items():
    t = mod4(n)
    if t in Gclass:
        check("G class function mod 4", abs(Gclass[t] - G) < TOL)
    else:
        Gclass[t] = G
print("classes mod 4 hit by primary squarefree n:", len(Gclass))
chi4 = {}
for ps in sq:
    n = elt(ps); t = (n[0] % 2, n[1] % 2); v = chi(ps, FOUR)
    if t in chi4: check("chi_c(4) class fn mod 2", abs(chi4[t] - v) < TOL)
    else: chi4[t] = v
# (c/(-2))_3 = c mod 2 read as a cube root of unity in F_4
for t, v in chi4.items():
    # find j with omega^j = t mod 2
    for j, u in enumerate([(1, 0), (0, 1), (-1, -1)]):
        if (u[0] % 2, u[1] % 2) == t:
            check("chi_c(4) = (c/-2)_3 = c mod 2", abs(v - OMEGA ** j) < TOL)

# ---------- R: values, class dependence, symmetry, bicharacter, formula ----------
def Rval(pa, pb):
    a = elt(pa); b = elt(pb)
    x = chi(pb, a) / chi(pa, b)
    return x
Rclass = {}
small = [ps for ps in sq if nm(ps) <= 700]
for pa, pb in itertools.product(small, small):
    a = elt(pa); b = elt(pb)
    if set(map(id, pa)) & set(map(id, pb)): continue
    r = Rval(pa, pb)
    check("R in {+-1}", abs(r - 1) < TOL or abs(r + 1) < TOL)
    key = (mod4(a), mod4(b))
    if key in Rclass: check("R depends on classes mod 4", abs(Rclass[key] - r) < TOL)
    else: Rclass[key] = r
    check("R symmetric", abs(r - Rval(pb, pa)) < TOL)
    # G(ab) = G(a) G(b) R(a,b)
    ab = mul(a, b)
    Gab = G_sqfree(pa + pb)
    check("(recip) G(ab)=G(a)G(b)R(a,b)", abs(Gab - Gcache[a] * Gcache[b] * r) < TOL)
    # R = Gamma_quad(ab)/(Gamma_quad(a)Gamma_quad(b))
    check("R = Gq(ab)/(Gq(a)Gq(b))", abs(r - gamma_quad(ab) / (gamma_quad(a) * gamma_quad(b))) < TOL)
print("R classes populated:", len(Rclass))

# square classes in (O/4)^x: representatives 1,-1,lambda,-lambda ; formula (-1)^{eh+fg+fh}
units4 = [(a, b) for a in range(4) for b in range(4) if norm((a, b)) % 2 == 1]
assert len(units4) == 12
def m4(x): return (x[0] % 4, x[1] % 4)
squares = {m4(mul(u, u)) for u in units4}
LAM = (1, 2)
reps = {(0, 0): (1, 0), (1, 0): (-1, 0), (0, 1): LAM, (1, 1): neg(LAM)}
def sqclass(t):
    for (e, f), r in reps.items():
        # t = r * s with s a square  <=> t * r^{-1} in squares ; r^{-1} = r^3 * ... use brute force
        for s in squares:
            if m4(mul(r, s)) == m4(t):
                return (e, f)
    raise ValueError(t)
for (ta, tb), r in Rclass.items():
    e, f = sqclass(ta); g_, h = sqclass(tb)
    check("R = (-1)^{eh+fg+fh}", abs(r - (-1) ** (e * h + f * g_ + f * h)) < TOL)
# Gamma_quad square class table and closed form
for c in [(a, b) for a in range(-9, 10) for b in range(-9, 10) if norm((a, b)) % 2 == 1]:
    gq = gamma_quad(c)
    a, b = c; I = 1j
    check("Gq closed form (1+i^-b+i^a+i^(b-a))/2", abs(gq - (1 + I ** (-b) + I ** a + I ** (b - a)) / 2) < TOL)
    rhs = sum(e_add(-cv(mul(c, mul(y, y))) / 4) for y in [(0, 0), (1, 0), (0, 1), (1, 1)]) / 2
    check("(quadratic-gaussian) Gq(c) = 1/2 sum_{y mod 2} e(-cy^2/4)", abs(gq - rhs) < TOL)
    ef = sqclass(m4(c))
    table = {(0, 0): 1, (1, 0): 1, (0, 1): 1j, (1, 1): -1j}
    check("Gq square-class table", abs(gq - table[ef]) < TOL)

# R(c,c) = chi_c(-1) and the (quotient) identity on all classes
for ps in [ps for ps in sq if len(ps) == 1]:
    c = elt(ps)
    key = (mod4(c), mod4(c))
    # R(c,c) via the formula on square classes
    e, f = sqclass(mod4(c))
    Rcc = (-1) ** (e * f + f * e + f * f)
    check("R(c,c) = chi_c(-1)", abs(Rcc - chi(ps, MINUS1)) < TOL)

def Rform(ta, tb):
    e, f = sqclass(ta); g_, h = sqclass(tb)
    return (-1) ** (e * h + f * g_ + f * h)
# primary class representatives: need a primary prime in each class mod 4 (all 12 classes)
print("G known on", len(Gclass), "of 12 classes")
chim1 = {}
for ps in sq:
    chim1[mod4(elt(ps))] = chi(ps, MINUS1)
def inv4(t):
    for u in units4:
        if m4(mul(u, t)) == (1, 0): return u
for ta in Gclass:
    for tb in Gclass:
        q = m4(mul(tb, inv4(ta)))
        if q not in Gclass: continue
        lhs = chim1[ta] * Gclass[ta].conjugate() * Gclass[tb] * Rform(ta, tb)
        check("(quotient) chi_a(-1) conj G(a) G(b) R(a,b) = G(b/a)", abs(lhs - Gclass[q]) < TOL)

# (crt-a): a(ab) = a(a) a(b) chi_b(a)^4   (xi trivial; xi is multiplicative)
def aco(ps):
    return alpha(elt(ps)).conjugate() * gamma(ps, 2)
for pa, pb in itertools.product(small[:40], small[:40]):
    if set(map(id, pa)) & set(map(id, pb)): continue
    if nm(pa) * nm(pb) > 2500: continue
    lhs = aco(pa + pb)
    rhs = aco(pa) * aco(pb) * chi(pb, elt(pa)) ** 4
    check("(crt-a)", abs(lhs - rhs) < TOL)
    check("(crt-a) symmetric form chi_a(b)^4 = chi_b(a)^4", abs(chi(pb, elt(pa)) ** 4 - chi(pa, elt(pb)) ** 4) < TOL)

print()
for k in sorted(counts):
    print("%-70s tested %5d  failures %d" % (k, counts[k], fails.get(k, 0)))
print("TOTAL failures:", sum(fails.values()))
