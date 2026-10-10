"""Exact finite checks for LEMMAS_4BCD_GH.md (cubic Lemmas 4.B, 4.C, 4.D, 4.H; table arithmetic of 4.G).

Status: EXPLORATION / finite exact checks; none of these is a proof of the lemmas.
Run:    python3 -I lemmas_4bcd_gh_checks.py
Arithmetic: exact.  Elements of O = Z[omega] are integer pairs (a, b) <-> a + b*omega.
Character values are cube roots of unity stored as exponents mod 3; correlation sums
F(u, v; j) are stored as exact count vectors [c0, c1, c2] (value c0 + c1 w + c2 w^2) and
compared after reduction by 1 + w + w^2 = 0.  The only floating-point step is [D2-F], which
is labelled as such.  Imports ../../a2/eis.py read-only (no bytecode written).
"""
import sys, os, itertools, cmath, math
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', '..', 'a2')))
import eis  # noqa: E402
from eis import mul, norm, divides, powmod, primary, conj

RESULTS = []
def report(tag, ok, msg, control=False):
    # for a control, "ok" means "the wrong rule was detected (it fails)"
    RESULTS.append((tag, ok, control))
    kind = 'CTRL' if control else 'CHECK'
    print(f"[{tag}] {kind} {'PASS' if ok else 'FAIL'}: {msg}")

# ---------------------------------------------------------------- basic arithmetic
def chi3_prime(x, p):
    """(x/p)_3 as exponent e in {0,1,2} (value w^e), or None if p | x.  p a primary prime."""
    k = eis.sym_prime(x, p)          # (x/p)_6 = zeta^k, zeta = e^{i pi/3}
    return None if k is None else k % 3   # (x/p)_3 = ((x/p)_6)^2 = zeta^{2k} = w^k

def chi6_prime(x, p):
    return eis.sym_prime(x, p)

def elt(fac):
    z = (1, 0)
    for p, a in fac.items():
        for _ in range(a): z = mul(z, p)
    return z

def chi3(fac, x):
    """chi_u(x) = prod_p chi_p(x)^{v_p(u)} (zero-extended); u given by {prime: exponent}."""
    s = 0
    for p, a in fac.items():
        e = chi3_prime(x, p)
        if e is None: return None
        s += a*e
    return s % 3

class Mod:
    """canonical residues of O / m O via a Hermite basis of the lattice m O."""
    def __init__(self, m):
        self.m = m
        a1, b1 = m; a2, b2 = mul(m, (0, 1))
        self.N = abs(a1*b2 - a2*b1)
        def egcd(a, b):
            if b == 0: return (a, 1, 0)
            g, x, y = egcd(b, a % b); return (g, y, x - (a//b)*y)
        g, x, y = egcd(b1, b2)
        if g < 0: g, x, y = -g, -x, -y
        self.g = g; self.w = (x*a1 + y*a2, g); self.d1 = self.N // g
        assert divides(m, (self.d1, 0)) and divides(m, self.w)
    def red(self, z):
        a, b = z; t = b // self.g
        a -= t*self.w[0]; b -= t*self.g
        return (a % self.d1, b)
    def residues(self):
        return [(i, j) for j in range(self.g) for i in range(self.d1)]

def vec_add(V, e, c=1):
    V[e] += c
def vec_red(V):
    return (V[0] - V[2], V[1] - V[2])
def scal(n, e):
    """n * w^e as reduced pair."""
    V = [0, 0, 0]; V[e % 3] += n; return vec_red(V)

def primes_upto(N):
    """primary prime elements prime to 6 with norm <= N (fast replacement for eis.primes_upto)."""
    isp = [True]*(N + 1); isp[0] = isp[1] = False
    for i in range(2, int(N**0.5) + 1):
        if isp[i]: isp[i*i::i] = [False]*len(isp[i*i::i])
    out = []
    for p in range(5, N + 1):
        if not isp[p]: continue
        if p % 3 == 1:
            found = None
            for b in range(0, 2*int(p**0.5) + 3):
                # a^2 - a b + b^2 - p = 0
                D = b*b - 4*(b*b - p)
                if D < 0: continue
                r = math.isqrt(D)
                if r*r == D and (b + r) % 2 == 0:
                    found = ((b + r)//2, b); break
            assert found and norm(found) == p
            out += [primary(found), primary(conj(found))]
        elif p % 3 == 2 and p*p <= N:
            out.append(primary((p, 0)))
    return sorted(set(out), key=lambda z: (norm(z), z))

# primes
PR = primes_upto(40)
P7 = [p for p in PR if norm(p) == 7]
P13 = [p for p in PR if norm(p) == 13]
P19 = [p for p in PR if norm(p) == 19]
P5 = [p for p in PR if norm(p) == 25]
p1, p1b = P7[0], P7[1]
p2 = P13[0]; p3 = P19[0]; q5 = P5[0]
assert p1 != p1b

def neg(z): return (-z[0], -z[1])
def sub(x, y): return (x[0]-y[0], x[1]-y[1])

def F_table(ufac, vfac):
    """F(u,v;j) for all j mod uv: dict canonical j -> count vector."""
    u, v = elt(ufac), elt(vfac); uv = mul(u, v)
    Mu, Mv, Muv = Mod(u), Mod(v), Mod(uv)
    T = {}
    XS = [(x, chi3(ufac, x)) for x in Mu.residues()]
    YS = [(y, chi3(vfac, y)) for y in Mv.residues()]
    XS = [(mul(v, x), e) for x, e in XS if e is not None]
    YS = [(mul(u, y), e) for y, e in YS if e is not None]
    for vx, ex in XS:
        for uy, ey in YS:
            j = Muv.red(sub(vx, uy))
            V = T.get(j)
            if V is None: V = T[j] = [0, 0, 0]
            V[(ex - ey) % 3] += 1
    return T, Muv

def gcd_fac(a, b):
    return {p: min(a[p], b[p]) for p in a if p in b and min(a[p], b[p]) > 0}
def div_fac(a, c):
    out = {p: a[p] - c.get(p, 0) for p in a}
    return {p: e for p, e in out.items() if e > 0}

def L_local(p, c, n1, n2, k, rule=3):
    """predicted local factor L_{p^c} as (integer multiplier, omega exponent) or (0, 0)."""
    P = norm(p); in1 = n1.get(p, 0) > 0; in2 = n2.get(p, 0) > 0
    pk = divides(p, k)
    if not in1 and not in2:
        e = (chi3_prime(elt(n1), p) - chi3_prime(elt(n2), p)) * c % 3
        if pk: m = P - 1
        elif c % rule != 0: m = -1
        else: m = P - 2
        return P**(c - 1) * m, e
    if in1 and in2: raise ValueError
    ok = (c % rule == 0) and not pk
    return (P**(c - 1) * (P - 1), 0) if ok else (0, 0)

def check_B(ufac, vfac, rule=3, conjugate_residual=False):
    """returns (#j checked, #mismatches)."""
    T, Muv = F_table(ufac, vfac)
    C = gcd_fac(ufac, vfac); n1 = div_fac(ufac, C); n2 = div_fac(vfac, C)
    Cel = elt(C); n1e, n2e = elt(n1), elt(n2)
    bad = 0; cnt = 0
    for j in Muv.residues():
        cnt += 1
        got = vec_red(T.get(j, [0, 0, 0]))
        if not divides(Cel, j):
            pred = (0, 0)
        else:
            k = (mul(j, conj(Cel))[0] // norm(Cel), mul(j, conj(Cel))[1] // norm(Cel))
            assert mul(k, Cel) == j
            a = chi3(n1, k); b = chi3(n2, neg(k))
            if a is None or b is None: pred = (0, 0)
            else:
                mult, e = 1, (a - b) if not conjugate_residual else (-a - b)
                for p, c in C.items():
                    m, ee = L_local(p, c, n1, n2, k, rule)
                    mult *= m; e += ee
                pred = scal(mult, e)
        if pred != got: bad += 1
        global NZB
        NZB += got != (0, 0)
    return cnt, bad

# ================================================================= Lemma 4.B
print("== Lemma 4.B: full correlation, cubic local factors ==")
B_CONFIGS = [
    ({p1: 1}, {p1: 1}), ({p1: 2}, {p1: 2}), ({p1: 3}, {p1: 3}), ({p1: 4}, {p1: 1}),
    ({p1: 4}, {p1: 3}), ({p1: 2}, {p1: 3}), ({p1: 2}, {p1: 1, p2: 1}), ({p1: 2, p2: 1}, {p1: 2}),
    ({p1: 1, p1b: 1}, {p1: 2}), ({p1: 3}, {p1: 3, p1b: 1}), ({q5: 2}, {q5: 1}), ({q5: 2}, {q5: 2}),
    ({p2: 1, p3: 1}, {p1: 1}), ({p1: 1}, {p2: 2}),
]
tot = 0; totbad = 0; NZB = 0
for uf, vf in B_CONFIGS:
    n, b = check_B(uf, vf); tot += n; totbad += b
    lab = lambda f: '*'.join(f"N{norm(p)}^{a}" for p, a in f.items())
    print(f"   u={lab(uf):14s} v={lab(vf):14s}  j checked {n:7d}  mismatches {b}")
report('B1', totbad == 0, f"{len(B_CONFIGS)} configurations, all j mod uv ({tot} frequencies, {NZB} with F != 0): exact agreement with the cubic local formula")
n, b = check_B({p1: 3}, {p1: 3}, rule=6)
report('B1-CTRL6', b > 0, f"sextic rule (6|c) at u=v=p^3, N p=7: {b}/{n} mismatches", control=True)
n, b = check_B({p1: 3}, {p1: 4}, rule=6)
report('B1-CTRL6b', b > 0, f"sextic rule at (u,v)=(p^3,p^4): {b}/{n} mismatches", control=True)
n, b = check_B({p1: 1, p2: 1}, {p1: 1, p3: 1}, conjugate_residual=True)
report('B1-CTRLc', b > 0, f"conjugated residual symbol chi-bar_n1(k): {b}/{n} mismatches", control=True)
# corollary: i > j0
def cor_check(i, j0, p):
    T, Muv = F_table({p: i}, {p: j0})
    P = norm(p); Cel = elt({p: j0}); bad = 0
    for j in Muv.residues():
        got = vec_red(T.get(j, [0, 0, 0]))
        pred = (0, 0)
        if j0 % 3 == 0 and divides(Cel, j):
            k = (mul(j, conj(Cel))[0] // norm(Cel), mul(j, conj(Cel))[1] // norm(Cel))
            if not divides(p, k):
                pred = scal(P**(j0 - 1)*(P - 1), (i - j0)*chi3_prime(k, p))
        if got != pred: bad += 1
    return bad
cb = sum(cor_check(i, j0, p1) for i, j0 in [(2, 1), (3, 1), (4, 3), (5, 3), (3, 2), (4, 2)])
report('B2', cb == 0, "Corollary (i > j0): (2,1),(3,1),(4,3),(5,3),(3,2),(4,2) at N p = 7, all j")

# zero frequency
z = 0
for uf, vf in B_CONFIGS:
    T, Muv = F_table(uf, vf)
    got = vec_red(T.get((0, 0), [0, 0, 0]))
    u, v = elt(uf), elt(vf)
    phi = 1
    for p, a in uf.items(): phi *= norm(p)**(a - 1)*(norm(p) - 1)
    pred = scal(phi, 0) if uf == vf else (0, 0)
    z += got != pred
report('B3', z == 0, "zero frequency: F(u,v;0) = phi(u) 1_{u=v}")

# ================================================================= Lemma 4.C
print("== Lemma 4.C: complete-common-support child character ==")
def check_C(D, E, a, b, mode='correct'):
    Tfull, Mfull = F_table({**D, **a} if not set(D) & set(a) else {p: D.get(p, 0) + a.get(p, 0) for p in set(D) | set(a)},
                           {p: E.get(p, 0) + b.get(p, 0) for p in set(E) | set(b)})
    Tde, Mde = F_table(D, E)
    bad = 0; n = 0
    global NZ
    for j in Mfull.residues():
        n += 1
        got = vec_red(Tfull.get(j, [0, 0, 0]))
        NZ += got != (0, 0)
        base = Tde.get(Mde.red(j), [0, 0, 0])
        ca = chi3(a, j); cb = chi3(b, neg(j))
        if ca is None or cb is None: pred = (0, 0)
        else:
            sh = (ca - cb) % 3 if mode == 'correct' else (-ca - cb) % 3
            V = [0, 0, 0]
            for e in range(3): V[(e + sh) % 3] += base[e]
            pred = vec_red(V)
        bad += pred != got
    return n, bad
C_CONFIGS = [   # chosen so that F(D,E;.) is not identically zero
    ({p1: 1}, {p1: 1}, {p2: 1}, {p1b: 1}),
    ({p1: 3}, {p1: 3}, {p2: 1}, {}),
    ({p1: 3}, {p1: 3}, {}, {p1b: 1}),
    ({p1: 1}, {p2: 1}, {p1b: 1}, {q5: 1}),
    ({p1: 1, p2: 1}, {p1: 1}, {p1b: 1}, {p3: 1}),
    ({}, {}, {p1: 2}, {p2: 1}),
    ({p1: 2}, {p1: 2}, {p2: 2}, {}),
]
tot = 0; totbad = 0; NZ = 0
for D, E, a, b in C_CONFIGS:
    n, bd = check_C(D, E, a, b); tot += n; totbad += bd
report('C1', totbad == 0, f"{len(C_CONFIGS)} configurations, all j mod uv ({tot} frequencies, {NZ} with F != 0): F(Da,Eb;j) = F(D,E;j) chi_a(j) chi-bar_b(-j)")
n, bd = check_C({p1: 1}, {p1: 1}, {p2: 1}, {p1b: 1}, mode='conj')
report('C1-CTRLc', bd > 0, f"conjugated sign chi-bar_a(j) at D=E=p (N7), a=N13, b=N7': {bd}/{n} mismatches", control=True)
n, bd = check_C({p1: 3}, {p1: 3}, {p2: 1}, {}, mode='conj')
report('C1-CTRLc3', bd > 0, f"conjugated sign chi-bar_a(j) at D=E=p^3, a=N13: {bd}/{n} mismatches", control=True)
# hypothesis (a, b) = 1 dropped: a = b = p2, D = E = p1
n, bd = check_C({p1: 1}, {p1: 1}, {p2: 1}, {p2: 1})
report('C1-CTRLh', bd > 0, f"hypothesis (a,b)=1 violated (a = b = N13 prime, D = E = N7 prime): {bd}/{n} mismatches", control=True)

# ================================================================= Lemma 4.D
print("== Lemma 4.D: r-classification and bridge CRT factorization ==")
def classify(i, j, p, rule=3):
    """compare k -> chi_p(k)^i chi-bar_p(k)^j with predicted xi * mask over k mod p."""
    M = Mod(p); bad = 0
    in_r = (i - j) % rule != 0
    for k in M.residues():
        e = chi3_prime(k, p)
        got = None if e is None else (i - j)*e % 3
        pred = None if e is None else ((i - j)*e % 3 if in_r else 0)
        bad += got != pred
    # primitivity (mod a prime: nonprincipal) when in r
    nonprincipal = any(chi3_prime(k, p) not in (None, 0) and (i - j)*chi3_prime(k, p) % 3 for k in M.residues())
    return bad, in_r, nonprincipal
bad = 0
for p in (p1, p2, q5):
    for i in range(1, 8):
        for j in range(1, 8):
            b, in_r, npl = classify(i, j, p)
            bad += b + (in_r != npl)
report('D1', bad == 0, "single prime: chi_p^i chi-bar_p^j = xi_p 1 if 3 !| i-j (xi nonprincipal), = 1_{p !| k} if 3 | i-j; i,j in 1..7, N p in {7,13,25}")
b, in_r, npl = classify(4, 1, p1, rule=6)
report('D1-CTRL6', in_r != npl, "sextic classification at (i,j)=(4,1): puts p in r but the cubic character is principal", control=True)
# composite: c = p1 p2 p1b with exponent pairs, primitivity of xi_r
def composite(pairs, rule=3):
    primes = list(pairs)
    cel = elt({p: 1 for p in primes}); M = Mod(cel)
    r = [p for p in primes if (pairs[p][0] - pairs[p][1]) % rule != 0]
    bad = 0
    for k in M.residues():
        es = [chi3_prime(k, p) for p in primes]
        if any(e is None for e in es): got = None
        else: got = sum((pairs[p][0] - pairs[p][1])*e for p, e in zip(primes, es)) % 3
        # predicted: xi_r(k) 1_{(k, c/r) = 1}
        if any(e is None for e in es): pred = None
        else: pred = sum((pairs[p][0] - pairs[p][1])*chi3_prime(k, p) for p in r) % 3
        bad += got != pred
    # primitivity of xi_r: for each prime p0 in r, xi_r is not periodic mod r/p0
    prim = True
    for p0 in r:
        others = [p for p in r if p != p0]
        # find k = 1 mod (r/p0), p0 !| k, with xi_r(k) != 1 : take k running mod r
        rel = elt({p: 1 for p in r}); Mr = Mod(rel); found = False
        for k in Mr.residues():
            if all(divides(p, sub(k, (1, 0))) for p in others) and not divides(p0, k):
                if sum((pairs[p][0]-pairs[p][1])*chi3_prime(k, p) for p in r) % 3: found = True; break
        prim &= found
    return bad, prim
bad = 0; prim_all = True
for ex in itertools.product([(1, 1), (2, 1), (4, 1), (3, 5), (1, 3), (6, 2)], repeat=3):
    pairs = {p1: ex[0], p2: ex[1], p1b: ex[2]}
    b, pr = composite(pairs); bad += b; prim_all &= pr
report('D2', bad == 0 and prim_all, "composite c = p1 p2 p1' (norms 7,13,7), 216 exponent patterns: chi_C chi-bar_D = xi_r 1_{(k,c/r)=1} on all k mod c; xi_r primitive mod r")
# bridge CRT termwise and reciprocity triviality
def crt_termwise(afac, bfac, rfac, xi_exps):
    a, b, r = elt(afac), elt(bfac), elt(rfac)
    m = mul(mul(a, b), r); Mm = Mod(m); Ma, Mb, Mr = Mod(a), Mod(b), Mod(r)
    seen = set(); bad = 0
    br, ar, ab = mul(b, r), mul(a, r), mul(a, b)
    xi = lambda z: (lambda es: None if any(e is None for e in es) else sum(xi_exps[p]*e for p, e in zip(rfac, es)) % 3)([chi3_prime(z, p) for p in rfac])
    for x in Ma.residues():
        for y in Mb.residues():
            for zz in Mr.residues():
                k = Mm.red((mul(br, x)[0] + mul(ar, y)[0] + mul(ab, zz)[0], mul(br, x)[1] + mul(ar, y)[1] + mul(ab, zz)[1]))
                seen.add(k)
                lhs = (chi3(afac, k), chi3(bfac, k), xi(k))
                rhs = []
                for f, g in ((chi3(afac, br), chi3(afac, x)), (chi3(bfac, ar), chi3(bfac, y)), (xi(ab), xi(zz))):
                    rhs.append(None if f is None or g is None else (f + g) % 3)
                bad += tuple(lhs) != tuple(rhs)
    return bad, len(seen) == Mm.N
b1, bij1 = crt_termwise({p2: 1}, {p1b: 1}, {p1: 1}, {p1: 1})
b2, bij2 = crt_termwise({p1: 1}, {q5: 1}, {p2: 1}, {p2: 2})
report('D3', b1 == 0 and b2 == 0 and bij1 and bij2, "bridge CRT: k = br x + ar y + ab z is a bijection and chi_a(k) chi-bar_b(k) xi(k) factors termwise with phase chi_a(br) chi-bar_b(ar) xi(ab)")
# reciprocity: chi_b(a) = chi_a(b) for coprime primary a, b (squarefree products of small primes)
prs = primes_upto(200)
elts = [p for p in prs] + [mul(p, q) for p, q in itertools.combinations(prs[:10], 2)]
bad = 0; bad6 = 0; n = 0
def chi3_elt(x, n_el):  # chi_n(x) for squarefree primary n given as element, via factor list
    return None
fac_of = {p: [p] for p in prs}
for p, q in itertools.combinations(prs[:10], 2): fac_of[mul(p, q)] = [p, q]
for a_, b_ in itertools.combinations(elts, 2):
    fa, fb = fac_of[a_], fac_of[b_]
    if set(fa) & set(fb): continue
    n += 1
    x = sum(chi3_prime(a_, p) for p in fb) % 3; y = sum(chi3_prime(b_, p) for p in fa) % 3
    bad += x != y
    x6 = sum(chi6_prime(a_, p) for p in fb) % 6; y6 = sum(chi6_prime(b_, p) for p in fa) % 6
    bad6 += x6 != y6
report('D4', bad == 0, f"cubic reciprocity chi_b(a) = chi_a(b), {n} coprime primary pairs (primes of norm <= 200 and products): R = 1")
report('D4-CTRL6', bad6 > 0, f"the sextic symbol is NOT reciprocal on the same pairs ({bad6}/{n} differ): the phase is genuinely trivial only at n = 3", control=True)
# floating-point bridge Gauss sum factorization (labelled FLOAT)
def gsum(fac, h, conj_char=False, modexp=None):
    m = elt(fac); M = Mod(m); s = 0
    for x in M.residues():
        e = chi3(fac, x) if modexp is None else modexp(x)
        if e is None: continue
        if conj_char: e = -e
        s += cmath.exp(2j*math.pi*e/3) * eis.e_of(mul(h, x), m)
    return s
afac, bfac, rfac = {p2: 1}, {p1b: 1}, {p1: 1}
a, b, r = elt(afac), elt(bfac), elt(rfac); m = mul(mul(a, b), r); M = Mod(m)
xi = lambda z: chi3_prime(z, p1)
maxerr = 0
for h in [(1, 0), (2, 1), (3, -2), (5, 7)]:
    lhs = 0
    for k in M.residues():
        ca, cb, cx = chi3(afac, k), chi3(bfac, k), xi(k)
        if None in (ca, cb, cx): continue
        lhs += cmath.exp(2j*math.pi*(ca - cb + cx)/3) * eis.e_of(mul(h, k), m)
    ph = (chi3(afac, mul(b, r)) - chi3(bfac, mul(a, r)) + xi(mul(a, b))) % 3
    rhs = cmath.exp(2j*math.pi*ph/3) * gsum(afac, h) * gsum(bfac, h, conj_char=True) * gsum(rfac, h, modexp=xi)
    maxerr = max(maxerr, abs(lhs - rhs))
report('D3-F', maxerr < 1e-9, f"FLOAT (not certified): full bridge Gauss sum = phase * G(a,h) conj(G(b,-h)) G_xi(r,h) (unnormalized); max error {maxerr:.1e}")

# ================================================================= Lemma 4.H
print("== Lemma 4.H: Kummer / fixed numerator, mu_3 ==")
lam = (1, 2)  # 1 + 2 w = sqrt(-3)
two = (2, 0)
W = (0, 1)
def pw(z, e):
    out = (1, 0)
    for _ in range(e): out = mul(out, z)
    return out
prs_big = primes_upto(3000)
nums = {(s, t, r): mul(mul(pw(W, s), pw(two, t)), pw(lam, r)) for s in range(3) for t in range(3) for r in range(3)}
def classes(modulus):
    Mm = Mod(modulus)
    return Mm
M18, M6 = Mod((18, 0)), Mod((6, 0))
per18 = True; per6 = True; sigs = {}
for key, a_ in nums.items():
    tab18 = {}; tab6 = {}; sig = []
    for p in prs_big:
        e = chi3_prime(a_, p); sig.append(e)
        c18 = M18.red(p); c6 = M6.red(p)
        if tab18.setdefault(c18, e) != e: per18 = False
        if tab6.setdefault(c6, e) != e: per6 = False
    sigs[key] = tuple(sig)
report('H1', per18, f"27 numerators w^s 2^t lam^r: A -> chi_A(numerator) is constant on primary primes A in each class mod 18 ({len(prs_big)} primes, norm <= 3000)")
report('H1-CTRL6', not per6, "the same characters are NOT periodic mod 6", control=True)
report('H2', len(set(sigs.values())) == 27, f"exactly {len(set(sigs.values()))} distinct characters among the 27 numerators (units mod cubes: 3 classes)")
# unit -1 is a cube: chi_A(-x) = chi_A(x)
m1 = all(chi3_prime((-1, 0), p) == 0 for p in prs_big)
report('H2b', m1, "chi_A(-1) = 1 on all primary primes (−1 = (−1)^3)")
# tame / exponent <= 1 at a good prime dividing a: A -> (q/A)_3 is periodic mod q on primary primes
q = p1
tabq = {}; perq = True; nonconst = set()
Mq = Mod(q)
for p in prs_big:
    if p == q: continue
    e = chi3_prime(q, p); c = Mq.red(p); nonconst.add(e)
    if tabq.setdefault(c, e) != e: perq = False
report('H3', perq and len(nonconst) == 3, "a = q good prime (N q = 7): A -> chi_A(q) on primary primes A depends only on A mod q (conductor exponent 1 at q) and is nonconstant")
# Frobenius: X^3 = a solvable mod P  <=>  (a/P)_3 = 1  (P prime, P !| 3a)
bad = 0; bad6 = 0; n = 0
for p in primes_upto(200):
    Mp = Mod(p)
    cubes = set(Mp.red(mul(mul(x, x), x)) for x in Mp.residues())
    for a_ in [(2, 0), (0, 1), (1, 2), (3, 1), (5, -2), (7, 3)]:
        if divides(p, a_) or divides(p, (3, 0)): continue
        n += 1
        solv = Mp.red(a_) in cubes
        bad += solv != (chi3_prime(a_, p) == 0)
        bad6 += solv != (chi6_prime(a_, p) == 0)
report('H4', bad == 0, f"Frobenius: X^3 - a has a root mod p iff (a/p)_3 = 1 ({n} pairs, N p <= 200)")
report('H4-CTRL6', bad6 > 0, f"the sextic criterion (a/p)_6 = 1 misclassifies {bad6}/{n} pairs", control=True)

print("== Corollary 4.H: forced residues and the cube form ==")
# For row h' and a frozen moving prime p0 carrying exponent e (0,1,2), the character
#   n -> chi_n(h') chi_{p0}(n)^e   on primary primes n
# is unramified at all good primes iff v_q(h') = 0 mod 3 (good q != p0) and v_{p0}(h') = -e mod 3.
# "unramified at good primes" is tested as: constant on each class n mod 18 (S-part conductor | 18),
# over primary primes n of norm <= 1500 not dividing 6 h' p0.  Finite consistency check only.
prs_n = primes_upto(1500)
prs_f = primes_upto(400)
def factor(z):
    out = {}
    for p in prs_f:
        while divides(p, z):
            out[p] = out.get(p, 0) + 1
            c, d = mul(z, conj(p)); N = norm(p); z = (c//N, d//N)
    return out, z
def strip_S(z):
    vs = 0; vl = 0
    while divides(two, z): c, d = mul(z, conj(two)); z = (c//4, d//4); vs += 1
    while divides(lam, z): c, d = mul(z, conj(lam)); z = (c//3, d//3); vl += 1
    return z, vs, vl
rows = []
for a_ in range(-25, 26):
    for b_ in range(-25, 26):
        z = (a_, b_)
        if z == (0, 0) or norm(z) > 300: continue
        rows.append(z)
p0 = p1
bad = 0; bad6 = 0; nexc = 0
for e in range(3):
    for h in rows:
        good, vs, vl = strip_S(h)
        fac, rest = factor(good)
        assert norm(rest) == 1
        pred = all((a % 3 == 0) for p, a in fac.items() if p != p0) and ((fac.get(p0, 0) + e) % 3 == 0)
        pred6 = all((a % 6 == 0) for p, a in fac.items() if p != p0) and ((fac.get(p0, 0) + e) % 6 == 0)
        tab = {}; const = True
        for n_ in prs_n:
            if divides(n_, h) or n_ == p0: continue
            v = chi3_prime(h, n_)
            v = (v + e*chi3_prime(n_, p0)) % 3
            c = M18.red(n_)
            if tab.setdefault(c, v) != v: const = False; break
        bad += const != pred; bad6 += const != pred6; nexc += const
report('H5', bad == 0, f"forced residue: over {len(rows)} rows h' (N h' <= 300, all units and S-parts) and e in {{0,1,2}}, the mod-18 test agrees with 'v_q(h') = 0 mod 3 off p0, v_p0(h') = -e mod 3' ({nexc} exceptional)")
report('H5-CTRL6', bad6 > 0, f"the sextic rule (mod 6) disagrees on {bad6} rows", control=True)
# cube-form count illustration: exceptional good ideals with forced residue 1 at p0 (e = 2), primary, norm <= Y
for Y in (10**3, 10**4, 10**5):
    # exceptional primary good ideals: p0 * (p0^3)^s * v^3 with v coprime... count = #{v : N(p0) N(v)^3 <= Y} (v any good ideal)
    cnt = 0
    vmax = int((Y/7)**(1/3)) + 2
    # count good ideals of norm <= X via elements up to units: brute force on norms
    X = Y/7
    c = 0
    for a_ in range(-int(2*X**(1/6))-3, int(2*X**(1/6))+4):
        for b_ in range(-int(2*X**(1/6))-3, int(2*X**(1/6))+4):
            z = (a_, b_); Nz = norm(z)
            if z == (0, 0) or Nz**3 > X: continue
            if divides(two, z) or divides(lam, z): continue
            c += 1
    print(f"   (illustration, not a check) Y={Y:>7d}: #exceptional good ideals (h') = p0 * v^3, N <= Y : {c//6:4d};  (Y/7)^(1/3) = {(Y/7)**(1/3):7.2f}")

# ================================================================= Lemma 4.G, absolute local table [G0]
print("== Lemma 4.G [G0]: absolute local correlation table, brute force (cubic analogue of l. 13742-13751) ==")
def n2(z): return z[0]*z[0] - z[0]*z[1] + z[1]*z[1]   # |x + y w|^2, exact
g0bad = 0
for p in (p1, p2):
    P = norm(p)
    for (i, j0) in [(1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (3, 3), (4, 3), (4, 1), (4, 2)]:
        if P == 13 and i + j0 > 5: continue
        T, Muv = F_table({p: i}, {p: j0})
        G = elt({p: j0})
        mx = {'unit': 0, 'nonunit': 0}
        for j in Muv.residues():
            if not divides(G, j): continue
            k = (mul(j, conj(G))[0] // norm(G), mul(j, conj(G))[1] // norm(G))
            cls = 'nonunit' if divides(p, k) else 'unit'
            mx[cls] = max(mx[cls], n2(vec_red(T.get(j, [0, 0, 0]))))
        if i == j0 and i % 3:
            pred = {'unit': P**(2*(i-1)), 'nonunit': (P**(i-1)*(P-1))**2}
        elif i == j0:
            pred = {'unit': (P**(i-1)*(P-2))**2, 'nonunit': (P**(i-1)*(P-1))**2}
        elif j0 % 3 == 0:
            pred = {'unit': (P**(j0-1)*(P-1))**2, 'nonunit': 0}
        else:
            pred = {'unit': 0, 'nonunit': 0}
        g0bad += mx != pred
report('G0', g0bad == 0, "max |F(p^i,p^j0;G k)|^2 over unit / nonunit k equals the cubic table (N p = 7, 13): equal 3!|i: P^{i-1} / P^{i-1}(P-1); equal 3|i: P^{i-1}(P-2) / P^{i-1}(P-1); unequal: P^{j0-1}(P-1) 1_{3|j0} / 0")

# ================================================================= Lemma 4.G table arithmetic
print("== Lemma 4.G: table arithmetic only (per-prime values follow from (LF) in the note; (LF) itself is not checked here) ==")
from fractions import Fraction as Fr
bad = 0; mins = []
for i in range(1, 61):
    rows_ = []
    if i % 3: rows_.append(('eq unit', Fr(4*i, 3), Fr(i)))
    if i % 3: rows_.append(('eq nonunit', Fr(4*i, 3) - Fr(2, 3) + (Fr(1, 3) if i == 1 else 0), Fr(i)))
    if i % 3 == 0: rows_.append(('eq 3|i', Fr(4*i, 3) - 1, Fr(i)))
    for j0 in range(3, i, 3):
        rows_.append(('uneq', i + Fr(j0, 3) - 1, Fr(i + j0, 2)))
    for name, F2, b2 in rows_:
        if F2 < b2: bad += 1
        mins.append((F2 - b2, name, i))
report('G1', bad == 0, f"table arithmetic: F_2 >= b_2 in every listed row, i <= 60; min F_2 - b_2 = {min(mins)[0]} at {min(mins)[1:]}")
# control: nonunit i=1 row without the forced residue (+1/3 removed): F_2/b_2 = 2/3
F2c = Fr(4, 3) - Fr(2, 3); report('G1-CTRL', F2c / 1 == Fr(2, 3) and F2c < 1, "without the forced residue the nonunit i=1 entry is 2/3 < b_2 = 1 (ratio 2/3)", control=True)
# the unequal-row formula as printed in SKETCH: (3i - j0 - 6)/6 vs direct difference
diffbad = 0
for i in range(4, 40):
    for j0 in range(3, i, 3):
        d = i + Fr(j0, 3) - 1 - Fr(i + j0, 2)
        if d != Fr(3*i - j0 - 6, 6): diffbad += 1
report('G2', diffbad == 0, "SKETCH column F_2 - b_2 = (3i - j0 - 6)/6 for the unequal row is the exact difference")

print()
n_ok = sum(1 for t, ok, c in RESULTS if ok and not c); n_chk = sum(1 for t, ok, c in RESULTS if not c)
n_ctl = sum(1 for t, ok, c in RESULTS if c); n_ctl_ok = sum(1 for t, ok, c in RESULTS if c and ok)
print(f"SUMMARY: checks {n_ok}/{n_chk} PASS; failing controls detected {n_ctl_ok}/{n_ctl}")
