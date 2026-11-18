"""SIEGEL Level-2 audit, part 1, steps 2-4 (Frobenius congruence, unitriangular weight-lowering change of basis,
p-adic extraction).  Our own code; nothing from the audited repositories is executed.
Run: python3 -I s2_s4_frobenius_extraction.py

 (2a) OAI (frobenius)/Banks Lem 6.1: in R = Z[a,b], a^2=d, b^2=2, for odd p not dividing 2d:
      theta^p == g(theta) (mod pR) with g = 1, tau, sigma, sigma*tau according to ((d/p),(2/p)).
      Checked for every basis element and for random theta (exact integer arithmetic), many d, all odd p < 400.
 (2b) Kerr (3)-(4): same with a^2 = D (D the fundamental discriminant itself, O = Z[sqrt D, sqrt 2]).
 (2c) Guo (3.9): rho((u+vt)^p) == u - vt (mod p) for chi(p) = -1; Guo (3.6): xi^{p0} == 2u - xi mod (p0, f_{u,v});
      derivative stability: every z-derivative of z^p - w at (u+vt, u-vt) has remainder == 0 mod p.
 (3a) Kerr Lem 2: transition matrix from monomials x1^i x2^j x3^k (i + 8(j+k) <= D) to
      G = x1^v (x1^p - x_l)^e x2^j x3^k is unitriangular in the weight order and G lies in L_D (p > 8).
 (3b) Guo (3.8): g_{r,s}^{(p)} = z^{r-ph} w^s (z^p - w)^h, h = min(floor(r/p), s0-1-s) is an integer basis of
      the rectangle (unitriangular in r), and every monomial stays in the rectangle.
 (4)  OAI Lemma 7 / Banks Lem 6.2, exact toy replay *in R itself* (not only through the norm):
      greedy weighted selection of rows R_alpha (selection done mod two split primes, then CERTIFIED exactly:
      retained rows are F_P-independent hence K-independent; each skipped row is in the K-span of earlier retained
      rows, certified by exact integer rank of the regular representation); Delta is reconstructed exactly in
      R = Z+Za+Zb+Zab by CRT from determinants under the four embeddings modulo many split primes; then
      v_p(Delta) (min over the 4 integer coordinates) is compared with
        E_p      = sum floor(alpha_1/p)                          (the lemma, Frobenius sigma or sigma*tau, p > H)
        E_full_p = sum over the coordinates that the Frobenius class maps into the variable set
                   (Frob 1: all three; sigma: 1,2; sigma*tau: 1,3; tau: 2,3), our own strengthening/control.
"""
import random
import math
from fractions import Fraction
import flint
from sympy import isprime, nextprime
from sympy.ntheory.residue_ntheory import sqrt_mod

random.seed(20261117)
out = []
fails = 0


def rep(ok, msg):
    global fails
    if not ok:
        fails += 1
    out.append(("PASS " if ok else "FAIL ") + msg)


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def odd_primes(n):
    return [p for p in range(3, n) if isprime(p)]


# ---------------- arithmetic in R = Z[a,b], a^2 = d, b^2 = 2 (coordinates on 1, a, b, ab) --------------
def mulR(x, y, d, m=None):
    x0, x1, x2, x3 = x
    y0, y1, y2, y3 = y
    z = (x0 * y0 + d * x1 * y1 + 2 * x2 * y2 + 2 * d * x3 * y3,
         x0 * y1 + x1 * y0 + 2 * (x2 * y3 + x3 * y2),
         x0 * y2 + x2 * y0 + d * (x1 * y3 + x3 * y1),
         x0 * y3 + x3 * y0 + x1 * y2 + x2 * y1)
    if m is not None:
        z = tuple(c % m for c in z)
    return z


def powR(x, e, d, m):
    r = (1, 0, 0, 0)
    b = tuple(c % m for c in x)
    while e:
        if e & 1:
            r = mulR(r, b, d, m)
        b = mulR(b, b, d, m)
        e >>= 1
    return r


def sig(x):
    return (x[0], -x[1], x[2], -x[3])


def tau(x):
    return (x[0], x[1], -x[2], -x[3])


def sigtau(x):
    return (x[0], -x[1], -x[2], x[3])


# ---------------- (2a)/(2b) Frobenius congruence ----------------
def frob_check(dlist, label):
    tested = 0
    bad = 0
    classes = {}
    for d in dlist:
        for p in odd_primes(400):
            if d % p == 0:
                continue
            chi, two = legendre(d, p), legendre(2, p)
            g = {(1, 1): lambda x: x, (1, -1): tau, (-1, 1): sig, (-1, -1): sigtau}[(chi, two)]
            name = {(1, 1): "1", (1, -1): "tau", (-1, 1): "sigma", (-1, -1): "sigma*tau"}[(chi, two)]
            classes[name] = classes.get(name, 0) + 1
            thetas = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)] + \
                     [tuple(random.randint(-10**6, 10**6) for _ in range(4)) for _ in range(6)]
            for th in thetas:
                lhs = powR(th, p, d, p)
                rhs = tuple(c % p for c in g(th))
                tested += 1
                if lhs != rhs:
                    bad += 1
    rep(bad == 0, f"{label}: theta^p == Frob_p(theta) mod pR in {tested} exact tests "
                  f"(class counts {classes})")


frob_check([-1, -2, -3, -5, -7, -163, 3, 5, 6, 7, 13, 229, -1155, 10**9 + 7, -(10**9 + 9)], "(2a) OAI/Banks R=Z[sqrt d, sqrt 2]")
frob_check([-3, -4, 5, -7, -8, 12, 13, -20, 24, 28, -163, -1155, 1009], "(2b) Kerr O=Z[sqrt D, sqrt 2]")

# ---------------- (2c) Guo quadratic-remainder congruences ----------------
bad = 0
cnt = 0
for d in [-1, -2, -3, -7, -163, 2, 3, 5, 13, 229]:
    for p in odd_primes(200):
        if d % p == 0 or legendre(d, p) != -1:
            continue
        for u in range(0, 12):
            for v in range(1, 12):
                # rho((u+vt)^p) mod p, computed in Z[t]/(t^2-d)
                x = (u % p, v % p)
                r = (1, 0)
                e = p
                b = x
                while e:
                    if e & 1:
                        r = ((r[0] * b[0] + d * r[1] * b[1]) % p, (r[0] * b[1] + r[1] * b[0]) % p)
                    b = ((b[0] * b[0] + d * b[1] * b[1]) % p, (2 * b[0] * b[1]) % p)
                    e >>= 1
                cnt += 1
                if r != (u % p, (-v) % p):
                    bad += 1
                # derivatives j>=1 of z^p - w: p!/(p-j)! z^{p-j}, coefficient divisible by p
                for j in (1, 2, p - 1, p):
                    coef = math.perm(p, j)
                    if coef % p != 0:
                        bad += 1
rep(bad == 0, f"(2c) Guo (3.9): rho((u+vt)^p) == u - vt (mod p), {cnt} cases; derivatives of z^p-w carry factor p")

bad = 0
cnt = 0
for d in [-1, -2, -3, -7, -163, 2, 3, 5, 13]:
    for p0 in [x for x in odd_primes(400) if x > 50]:
        if d % p0 == 0 or legendre(d, p0) != -1:
            continue
        m = math.isqrt(p0 - 1) + 1  # ceil(sqrt p0) for non-square p0
        for u in (0, 1, m - 1):
            for v in (1, m - 1):
                f = flint.nmod_poly([(u * u - d * v * v) % p0, (-2 * u) % p0, 1], p0)
                xi = flint.nmod_poly([0, 1], p0)
                lhs = xi.pow_mod(p0, f)
                rhs = flint.nmod_poly([(2 * u) % p0, p0 - 1], p0) % f
                cnt += 1
                if lhs != rhs:
                    bad += 1
                # irreducibility mod p0 (d v^2 a non-residue)
                if len(f.roots()) != 0:
                    bad += 1
rep(bad == 0, f"(2c) Guo (3.6): xi^p0 == 2u - xi mod (p0, f_uv) and f_uv irreducible, {cnt} cases")

# ---------------- (3a) Kerr Lemma 2 triangularity ----------------
def kerr_basis_check(Dg, p, l):
    mons = [(i, j, k) for i in range(Dg + 1) for j in range(Dg // 8 + 1) for k in range(Dg // 8 + 1) if i + 8 * (j + k) <= Dg]
    idx = {m: n for n, m in enumerate(sorted(mons, key=lambda m: (m[0] + 8 * (m[1] + m[2]), m)))}
    ok_in = True
    ok_tri = True
    for (i, j, k) in mons:
        e, v = divmod(i, p)
        for mm in range(e + 1):
            # x1^v (x1^p - x_l)^e x2^j x3^k -> term C(e,mm) (-1)^mm x1^{v + p(e-mm)} x_l^mm x2^j x3^k
            mon = (v + p * (e - mm), j + (mm if l == 2 else 0), k + (mm if l == 3 else 0))
            if mon not in idx:
                ok_in = False
                continue
            if mm > 0 and idx[mon] >= idx[(i, j, k)]:
                ok_tri = False
    return ok_in and ok_tri, len(mons)


allok = True
sizes = []
for Dg in (40, 64, 97):
    for p in (11, 13, 17, 23):
        for l in (2, 3):
            ok, nm = kerr_basis_check(Dg, p, l)
            allok &= ok
            sizes.append(nm)
rep(allok, f"(3a) Kerr Lem 2: G_ijk in L_D and unitriangular in weight order (D in {{40,64,97}}, p in {{11,13,17,23}}, l in {{2,3}}; up to {max(sizes)} monomials)")


# ---------------- (3b) Guo adapted basis ----------------
def guo_basis_check(p0, s0, p):
    ok = True
    n = p0 * s0
    rows = []
    for r in range(p0):
        for s in range(s0):
            h = min(r // p, s0 - 1 - s)
            vec = {}
            for k in range(h + 1):
                mon = (r - p * k, s + k)
                if not (0 <= mon[0] < p0 and 0 <= mon[1] < s0):
                    ok = False
                vec[mon] = vec.get(mon, 0) + math.comb(h, k) * (-1) ** k
                if k > 0 and not (mon[0] < r):
                    ok = False
            rows.append(vec)
    # integer basis: transition matrix unitriangular in the order (r, s) -> determinant +-1; verify with flint
    order = {(r, s): r * s0 + s for r in range(p0) for s in range(s0)}
    M = flint.fmpz_mat(n, n)
    for i, vec in enumerate(rows):
        for mon, c in vec.items():
            M[i, order[mon]] = c
    return ok and abs(int(M.det())) == 1


allok = True
for (p0, s0) in [(31, 3), (37, 4), (41, 5), (61, 6)]:
    for p in [3, 5, 7, 11]:
        allok &= guo_basis_check(p0, s0, p)
rep(allok, "(3b) Guo (3.8): adapted polynomials stay in the rectangle and form an integer basis (det = +-1), "
           "(p0,s0) in {(31,3),(37,4),(41,5),(61,6)}, p in {3,5,7,11}")


# ---------------- (4) exact toy replay of OAI Lemma 7 in R ----------------
def split_primes(d, count, start):
    P = start
    res = []
    while len(res) < count:
        P = nextprime(P)
        if P % 8 == 1 and legendre(d, P) == 1:
            res.append(P)
    return res


def theta_vec(N):
    pts = []
    for n1 in range(N):
        for n2 in range(N):
            for n3 in range(N):
                for n4 in range(N):
                    pts.append((n1, n2, n3, n4))
    return pts


def embed(th, sd, s2, e1, e2, P):
    return (th[0] + e1 * th[1] * sd + e2 * th[2] * s2 + e1 * e2 * th[3] * sd * s2) % P


def row_mod(alpha, pts, sd, s2, e1, e2, P):
    a1, a2, a3 = alpha
    r = []
    for th in pts:
        x1 = embed(th, sd, s2, e1, e2, P)      # nu(theta)
        x2 = embed(th, sd, s2, -e1, e2, P)     # nu(sigma theta)
        x3 = embed(th, sd, s2, -e1, -e2, P)    # nu(sigma tau theta)
        r.append(pow(x1, a1, P) * pow(x2, a2, P) * pow(x3, a3, P) % P)
    return r


def greedy_mod(N, H, d, P, maxw):
    sd = sqrt_mod(d % P, P)
    s2 = sqrt_mod(2, P)
    pts = theta_vec(N)
    M = len(pts)
    alphas = sorted([(a1, a2, a3) for a1 in range(maxw + 1) for a2 in range(maxw // H + 1) for a3 in range(maxw // H + 1)
                     if a1 + H * (a2 + a3) <= maxw], key=lambda a: (a[0] + H * (a[1] + a[2]), a))
    basis = []   # list of (pivot, row) in reduced echelon form mod P
    retained, skipped = [], []
    for al in alphas:
        r = row_mod(al, pts, sd, s2, 1, 1, P)
        for piv, br in basis:
            c = r[piv]
            if c:
                r = [(x - c * y) % P for x, y in zip(r, br)]
        nz = next((i for i, x in enumerate(r) if x), None)
        if nz is None:
            skipped.append(al)
        else:
            inv = pow(r[nz], P - 2, P)
            r = [(x * inv) % P for x in r]
            # keep fully reduced
            newb = []
            for piv, br in basis:
                c = br[nz]
                if c:
                    br = [(x - c * y) % P for x, y in zip(br, r)]
                newb.append((piv, br))
            basis = newb + [(nz, r)]
            retained.append(al)
            if len(retained) == M:
                break
    return retained, skipped, len(retained) == M


def exact_row_R(alpha, pts, d):
    """Row R_alpha with entries in R (integer coordinates), exact."""
    a1, a2, a3 = alpha
    row = []
    for th in pts:
        x = (1, 0, 0, 0)
        for (base, e) in ((th, a1), (sig(th), a2), (sigtau(th), a3)):
            for _ in range(e):
                x = mulR(x, base, d)
        row.append(x)
    return row


def regrep_vectors(row, d):
    """Q-basis multiples e*row, e in {1,a,b,ab}, flattened to integer vectors (K-span <-> Q-span)."""
    vecs = []
    for e in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]:
        v = []
        for x in row:
            v.extend(mulR(e, x, d))
        vecs.append(v)
    return vecs


def certify_skipped(retained, skipped, pts, d, H):
    """Exact certificate that each skipped row lies in the K-span of the retained rows preceding it."""
    key = lambda a: (a[0] + H * (a[1] + a[2]), a)
    allr = sorted(retained, key=key)
    exp_rows = {al: regrep_vectors(exact_row_R(al, pts, d), d) for al in allr}
    nok = 0
    for al in skipped:
        prev = [b for b in allr if key(b) < key(al)]
        base = [v for b in prev for v in exp_rows[b]]
        target = [c for x in exact_row_R(al, pts, d) for c in x]
        if not base:
            ok = all(c == 0 for c in target)
        else:
            r0 = 4 * len(prev)   # retained rows are K-independent, so their Q-expansions are Q-independent
            r1 = flint.fmpz_mat(base + [target]).rank()
            ok = (r0 == r1)
        nok += ok
    return nok == len(skipped)


def crt_pair(r1, m1, r2, m2):
    g = pow(m1, -1, m2)
    t = ((r2 - r1) * g) % m2
    return r1 + m1 * t, m1 * m2


def delta_exact(retained, pts, d, N, Sabs):
    """Reconstruct Delta = det(R_alpha)_{alpha in retained} in R by CRT over split primes."""
    M = len(pts)
    q_bound_log = 0.5 * M * math.log(M) + Sabs * math.log(8 * N * math.sqrt(abs(d) * 4)) + 5
    need = q_bound_log + math.log(4)
    res = [0, 0, 0, 0]
    mod = 1
    P = 2**61
    used = 0
    while math.log(mod) < need + 40:
        P = nextprime(P)
        if not (P % 8 == 1 and legendre(d, P) == 1):
            continue
        sd = sqrt_mod(d % P, P)
        s2 = sqrt_mod(2, P)
        nus = {}
        for e1 in (1, -1):
            for e2 in (1, -1):
                A = flint.nmod_mat([row_mod(al, pts, sd, s2, e1, e2, P) for al in retained], P)
                nus[(e1, e2)] = int(A.det())
        inv4 = pow(4, P - 2, P)
        c0 = sum(nus.values()) * inv4 % P
        c1 = sum(e1 * v for (e1, e2), v in nus.items()) * inv4 * pow(sd, P - 2, P) % P
        c2 = sum(e2 * v for (e1, e2), v in nus.items()) * inv4 * pow(s2, P - 2, P) % P
        c3 = sum(e1 * e2 * v for (e1, e2), v in nus.items()) * inv4 * pow(sd * s2 % P, P - 2, P) % P
        cs = [c0, c1, c2, c3]
        if mod == 1:
            res, mod = cs, P
        else:
            for i in range(4):
                res[i], newmod = crt_pair(res[i], mod, cs[i], P)
            mod = newmod
        used += 1
    coords = [r if r <= mod // 2 else r - mod for r in res]
    # independent verification at a fresh split prime (not used in the CRT): nu(Delta) from coordinates == det mod P'
    Pv = nextprime(3 * 10**18)
    while not (Pv % 8 == 1 and legendre(d, Pv) == 1):
        Pv = nextprime(Pv)
    sd = sqrt_mod(d % Pv, Pv)
    s2 = sqrt_mod(2, Pv)
    A = flint.nmod_mat([row_mod(al, pts, sd, s2, 1, 1, Pv) for al in retained], Pv)
    lhs = int(A.det())
    rhs = (coords[0] + coords[1] * sd + coords[2] * s2 + coords[3] * sd * s2) % Pv
    assert lhs == rhs, "CRT reconstruction of Delta failed the fresh-prime check"
    return coords, used


def vp(n, p):
    if n == 0:
        return 10**9
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def frob_class(d, p):
    return {(1, 1): "1", (1, -1): "tau", (-1, 1): "sigma", (-1, -1): "sigma*tau"}[(legendre(d, p), legendre(2, p))]


cases = [(-163, 2, 1), (-163, 2, 3), (-7, 2, 2), (5, 2, 4), (13, 2, 6), (-1, 2, 3), (-3, 2, 5), (229, 2, 2),
         (-163, 3, 2), (5, 3, 4)]
lemma_fail = 0
full_fail = 0
lemma_tests = 0
full_tests = 0
eq_lemma = 0
rows_report = []
for (d, N, H) in cases:
    D = d if d % 4 == 1 else 4 * d
    q = abs(D)
    maxw = 30 * H + 40 if N == 2 else 22 * H + 30
    sel = []
    for P in split_primes(d, 2, 2**62 + 12345):
        retained, skipped, full = greedy_mod(N, H, d, P, maxw)
        sel.append((retained, skipped, full))
    same = sel[0][0] == sel[1][0] and sel[0][2] and sel[1][2]
    retained, skipped = sel[0][0], sel[0][1]
    pts = theta_vec(N)
    cert = certify_skipped(retained, skipped, pts, d, H) if same else False
    Sabs = sum(sum(a) for a in retained)
    coords, used = delta_exact(retained, pts, d, N, Sabs)
    nonzero = any(coords)
    S1 = sum(a[0] for a in retained)
    S2 = sum(a[1] + a[2] for a in retained)
    maxa1 = max(a[0] for a in retained)
    line = [f"d={d} N={N} H={H}: M={len(retained)} rows, selection agrees mod 2 primes={same}, skipped rows certified exactly={cert}, "
            f"Delta != 0: {nonzero} (CRT over {used} primes, verified at a fresh prime), S1={S1}, S2={S2}, max alpha1={maxa1}"]
    rep(same and cert and nonzero, line[0])
    for p in odd_primes(maxa1 + 1):
        if D % p == 0:
            continue
        cls = frob_class(d, p)
        v = min(vp(c, p) for c in coords)
        E1 = sum(a[0] // p for a in retained)
        E2 = sum(a[1] // p for a in retained)
        E3 = sum(a[2] // p for a in retained)
        Efull = {"1": E1 + E2 + E3, "sigma": E1 + E2, "sigma*tau": E1 + E3, "tau": E2 + E3}[cls]
        # weight-lowering conditions for the full replacement:
        #   coordinate 1 -> coordinate 1/2/3 needs p > 1 (Frob 1) or p > H (sigma, sigma*tau);
        #   coordinates 2,3 -> 2,3 needs H(p-1) > 0;  coordinate 2/3 -> coordinate 1 needs Hp > 1.
        admissible = (cls in ("sigma", "sigma*tau") and p > H)
        if admissible:
            lemma_tests += 1
            if v < E1:
                lemma_fail += 1
            if v == E1:
                eq_lemma += 1
        if cls == "1" or cls == "tau" or p > H:
            full_tests += 1
            if v < Efull:
                full_fail += 1
        if E1 or E2 or E3:
            rows_report.append(f"   p={p} Frob={cls}{' (admissible)' if admissible else ''}: v_p(Delta)={v}, E_p={E1}, E_full={Efull}")
    out.extend(rows_report)
    rows_report = []

rep(lemma_fail == 0, f"(4) OAI Lem 7 in R: v_p(Delta) >= E_p for every admissible p in every toy case: {lemma_tests} tests, "
                     f"{lemma_fail} failures, equality in {eq_lemma}")
rep(full_fail == 0, f"(4) control/strengthening: v_p(Delta) >= E_full_p for all four Frobenius classes: {full_tests} tests, {full_fail} failures")

print("\n".join(out))
print(f"\nSUMMARY: {sum(1 for o in out if o.startswith('PASS'))} PASS, {fails} FAIL")
