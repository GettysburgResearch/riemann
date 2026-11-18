"""SIEGEL Level-2 audit, part 2, step 5 (nonvanishing / zero estimate).
Our own code; nothing from the audited repositories is executed.  Run: python3 -I s5_nonvanishing.py

Notation: d squarefree, a = sqrt(d), b = sqrt(2), theta_n = n1 + n2 a + n3 b + n4 ab, n in E_N = {0..N-1}^4,
points z_n = (theta_n, sigma theta_n, sigma tau theta_n) = A n  (OAI (A) / Banks Theta), M = N^4.
All ranks are computed modulo primes P that split completely in K = Q(a, b) (a, b mapped to square roots mod P).
rank_P <= rank_K always, so "rank_P = full" CERTIFIES full rank over K; a rank deficiency mod P is reported as
"mod two primes" (not a certificate) unless it is forced by a dimension count or an explicit polynomial.

 (5a) OAI Lemma 3 / Cor 4, Banks Prop 3.4 / Cor 3.5 (spanning by box monomials):
      minimal cube t such that rows (A n)^alpha, alpha in [0,t]^3, span F_P^{E_N}; compared with
        - the dimension floor (t+1)^3 >= N^4,
        - Lemma 3's sufficient cube  (t - 3(N-1) + 1)^3 > (4N-3)^4, t >= 3(N-1),
        - Cor 4's cube-equivalent T = 32 U (H = 1), U = N^{4/3};
      uniformity in d (several fields, |d| up to ~10^9); uniformity in the aspect ratio t1/t2.
 (5b) Necessity of the Q-independence hypothesis (d = 2, i.e. q = 8, which all four papers exclude/omit):
      fiber argument => the minimal spanning cube is >= (max fiber) - 1 ~ N^2/2, so Lemma 3's conclusion FAILS for
      the degenerate map once N is large; explicit low-degree vanishing polynomial; Kerr's q = 8 lattice has a
      rank-3 subgroup in a plane (mu <= 1), verified exactly with sympy.
 (5c) Masser-type zero estimate (Kerr Lemma 6 + Lemma 7): minimal total degree D_min(N) of a nonzero polynomial
      vanishing on {A n : n in E_N}, versus Masser's bound ((N-1)/3)^{4/3} and the dimension count.
 (5d) Guo Lemma 3.3, sharp subset form: for ANY set G of pairs (u,v), 0<=u<p0, 1<=v<=(p0-1)/2, with 2|G| > p0,
      the Stepanov argument proves injectivity of iota_G; we certify injectivity (rank mod a 61-bit prime = p0 s0)
      at the exact threshold |G| = (p0+1)/2 for random G, many (d, p0, s0), including s0 far above p0/30;
      plus Guo's actual grid (m = ceil(sqrt p0)).
"""
import math
import random
import itertools
import numpy as np
import flint
import sympy as sp
from sympy import isprime
from sympy.ntheory.residue_ntheory import sqrt_mod

random.seed(20261117)
out = []
fails = 0


def rep(ok, msg):
    global fails
    if not ok:
        fails += 1
    out.append(("PASS " if ok else "FAIL ") + msg)


def info(msg):
    out.append("INFO " + msg)


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def split_primes(d, count, start):
    """primes P < 2^31 (so numpy int64 products do not overflow) with (d/P) = (2/P) = 1."""
    res = []
    P = start
    while len(res) < count:
        P -= 1
        if isprime(P) and legendre(d, P) == 1 and legendre(2, P) == 1:
            res.append(P)
    return res


def points_mod(d, N, P, b_is_a=False):
    a = sqrt_mod(d % P, P)
    b = a if b_is_a else sqrt_mod(2, P)
    ab = a * b % P
    ns = np.array(list(itertools.product(range(N), repeat=4)), dtype=np.int64)
    n1, n2, n3, n4 = ns[:, 0], ns[:, 1], ns[:, 2], ns[:, 3]
    z1 = (n1 + n2 * a + n3 * b + n4 * ab) % P
    z2 = (n1 - n2 * a + n3 * b - n4 * ab) % P
    z3 = (n1 - n2 * a - n3 * b + n4 * ab) % P
    return [z1, z2, z3], ns


def powers(z, kmax, P):
    pw = [np.ones_like(z)]
    for _ in range(kmax):
        pw.append(pw[-1] * z % P)
    return pw


def rank_rows(alphas, Z, P):
    kmax = [max(al[j] for al in alphas) for j in range(3)]
    pw = [powers(Z[j], kmax[j], P) for j in range(3)]
    rows = np.empty((len(alphas), len(Z[0])), dtype=np.int64)
    for i, (x, y, w) in enumerate(alphas):
        rows[i] = pw[0][x] * pw[1][y] % P * pw[2][w] % P
    m = flint.nmod_mat(rows.shape[0], rows.shape[1], rows.ravel().tolist(), P)
    return m.rank()


def box(t1, t2, t3):
    return list(itertools.product(range(t1 + 1), range(t2 + 1), range(t3 + 1)))


def lemma3_cube(N):
    t = 3 * (N - 1)
    while (t - 3 * (N - 1) + 1) ** 3 <= (4 * N - 3) ** 4:
        t += 1
    return t


# ---------------------------------------------------------------- (5a) minimal spanning cube, uniformity in d
DS = [-1, -3, -7, -163, 5, 13, 229, -1000003, 999999937]
for dd in DS:
    assert all(e == 1 for e in sp.factorint(abs(dd)).values())
tmin_table = {}
for N in (2, 3, 4, 5):
    M = N ** 4
    floor_t = math.ceil(M ** (1 / 3) - 1e-9) - 1
    while (floor_t + 1) ** 3 < M:
        floor_t += 1
    row = []
    for dd in DS:
        P1, P2 = split_primes(dd, 2, 2 ** 31 - 1)
        Z1, _ = points_mod(dd, N, P1)
        Z2, _ = points_mod(dd, N, P2)
        t = floor_t
        while rank_rows(box(t, t, t), Z1, P1) < M:
            t += 1
        # certificate: rank mod P1 full at t; deficiency at t-1 confirmed mod P2 (or forced by dimension)
        forced = (t) ** 3 < M
        conf = forced or rank_rows(box(t - 1, t - 1, t - 1), Z2, P2) < M
        row.append((dd, t, conf))
    ts = sorted(set(r[1] for r in row))
    tmin_table[N] = ts
    rep(len(ts) == 1 and all(r[2] for r in row),
        f"(5a) N={N}: minimal spanning cube t is the same for all {len(DS)} fields d in {DS}: t_min = {ts} "
        f"(dimension floor {floor_t}; Lemma 3 sufficient cube {lemma3_cube(N)}; Cor 4 T=32N^(4/3) = "
        f"{32 * N ** (4 / 3):.0f}); rows/cols at t_min = {(ts[0] + 1) ** 3}/{M}")

# aspect-ratio uniformity at N = 4: boxes (rho*t2, t2, t2)
N = 4
M = N ** 4
dd = -163
P1, P2 = split_primes(dd, 2, 2 ** 31 - 1)
Z1, _ = points_mod(dd, N, P1)
vols = []
for rho in (1, 2, 4, 8, 16, 32):
    t2 = 0
    while rank_rows(box(rho * t2, t2, t2), Z1, P1) < M:
        t2 += 1
    vol = (rho * t2 + 1) * (t2 + 1) ** 2
    vols.append((rho, t2, vol / M))
rep(max(v[2] for v in vols) < 3.0,
    "(5a) aspect-ratio uniformity, N=4, d=-163: minimal box (rho*t2, t2, t2) that spans, (rho, t2, rows/M) = "
    + ", ".join(f"({r},{t},{v:.2f})" for r, t, v in vols)
    + "; the needed number of rows stays O(M) for every aspect ratio (Lemma 3's budget is a product condition)")

# ---------------------------------------------------------------- (5b) necessity: the degenerate map (d = 2)


def max_fiber_d2(N):
    # fibers of (z1, z3) for a = b = sqrt2: z1 = (n1 + 2 n4) + sqrt2 (n2 + n3), z3 = (n1 + 2 n4) - sqrt2 (n2 + n3)
    c1 = {}
    c2 = {}
    for n1 in range(N):
        for n4 in range(N):
            c1[n1 + 2 * n4] = c1.get(n1 + 2 * n4, 0) + 1
    for n2 in range(N):
        for n3 in range(N):
            c2[n2 + n3] = c2.get(n2 + n3, 0) + 1
    return max(c1.values()) * max(c2.values())


# exact check that z2 separates points inside a fiber, so (t+1) >= fiber size is necessary for spanning
N = 6
a2 = sp.sqrt(2)
fib = {}
for n in itertools.product(range(N), repeat=4):
    n1, n2, n3, n4 = n
    key = (n1 + 2 * n4, n2 + n3)
    z2 = (n1 - 2 * n4, n3 - n2)  # z2 = (n1 - 2n4) + sqrt2 (n3 - n2), coordinates over Q(sqrt2)
    fib.setdefault(key, set()).add(z2)
sizes_ok = all(len(v) == sum(1 for n in itertools.product(range(N), repeat=4)
                             if (n[0] + 2 * n[3], n[1] + n[2]) == k) for k, v in list(fib.items())[:40])
rep(sizes_ok, "(5b) d=2 map: z2 is injective on every (z1,z3)-fiber (checked exactly on 40 fibers at N=6), so "
    "spanning by a cube [0,t]^3 forces t+1 >= max fiber size")
Nstar = None
for N in range(2, 400):
    if max_fiber_d2(N) - 1 > lemma3_cube(N):
        Nstar = N
        break
rep(Nstar is not None,
    f"(5b) WITNESS (hypothesis necessity, not an error): for the degenerate map (d=2, kernel coordinates "
    f"Q-dependent) Lemma 3's budget holds with the cube t={lemma3_cube(Nstar)} at N={Nstar}, but spanning needs "
    f"t >= {max_fiber_d2(Nstar) - 1} (max fiber {max_fiber_d2(Nstar)}); so the Q-independence hypothesis of "
    f"OAI Lem 3 / Banks Prop 3.4 is load-bearing.  All papers exclude d=2 (q=8) or leave it to finiteness.")
# minimal spanning cube for the degenerate map at small N, versus generic
deg_rows = []
for N in (2, 3, 4):
    M = N ** 4
    P = split_primes(2, 1, 2 ** 31 - 1)[0]
    Zd, _ = points_mod(2, N, P, b_is_a=True)
    # are the points distinct?  (yes: kernel has no rational vector)
    distinct = len(set(zip(*(z.tolist() for z in Zd)))) == M
    t = 0
    while rank_rows(box(t, t, t), Zd, P) < M:
        t += 1
    deg_rows.append((N, distinct, t, max_fiber_d2(N) - 1, tmin_table[N][0]))
rep(all(r[1] and r[2] >= r[3] for r in deg_rows),
    "(5b) degenerate map, small N: (N, points distinct, minimal spanning cube, fiber lower bound, generic t_min) = "
    + ", ".join(str(r) for r in deg_rows))

# Kerr's normalization at q = 8: gamma's with sqrt q = 2 sqrt2, sqrt(2q) = 4
s2 = sp.sqrt(2)
g1 = sp.Matrix([1, 1, 1])
g2 = sp.Matrix([2 * s2, -2 * s2, -2 * s2])
g3 = sp.Matrix([s2, s2, -s2])
g4 = sp.Matrix([4, -4, 4])
plane_vecs = [g1, g4, g2 - 2 * g3]
in_plane = all(sp.simplify(v[0] - v[2]) == 0 for v in plane_vecs)
# Z-independence of g1, g4, g2-2g3 over Q: write entries in basis {1, sqrt2}
def qcoords(v):
    res = []
    for e in v:
        e = sp.expand(e)
        c1 = e.coeff(s2)
        c0 = sp.expand(e - c1 * s2)
        res += [c0, c1]
    return res
Qm = sp.Matrix([qcoords(v) for v in plane_vecs])
rank3 = Qm.rank() == 3
ker_v = sp.Matrix([4, s2, -2 * s2, -1])
pi_v = sp.simplify(sp.Matrix.hstack(g1, g2, g3, g4) * ker_v)
rep(in_plane and rank3 and pi_v == sp.zeros(3, 1),
    "(5b) Kerr at q=8 (M1 witness): gamma1, gamma4, gamma2-2gamma3 are Z-independent and lie in the plane x1=x3, "
    "so l_1 >= 3 and Masser's mu <= (4-3)/1 = 1 < 4/3; the kernel v=(4, sqrt2, -2sqrt2, -1) has Q-dependent "
    "coordinates. Lemma 7's hypothesis genuinely fails at q=8 (one conductor; covered only by implicit finiteness).")
# explicit low-degree vanishing polynomial at q = 8 in Kerr's coordinates: x1 - x3 = 2 sqrt2 (2 n2 + n3)
Nn = 4
okpoly = True
for n in itertools.product(range(Nn), repeat=4):
    x = n[0] * g1 + n[1] * g2 + n[2] * g3 + n[3] * g4
    val = sp.expand((x[0] - x[2]) / (2 * s2))
    if not (val.is_integer and 0 <= val <= 3 * (Nn - 1)):
        okpoly = False
Nk = None
for N in range(2, 100000):
    if 3 * N - 2 < ((N - 1) / 3) ** (4 / 3):
        Nk = N
        break
rep(okpoly, f"(5b) q=8: F(x) = prod_(s=0)^(3N-3) (x1 - x3 - 2 sqrt2 s), total degree 3N-2, vanishes on all Kerr points "
    f"(exact check N={Nn}); it beats Masser's 4/3-bound ((N-1)/3)^(4/3) from N={Nk} on.")

# ---------------------------------------------------------------- (5c) Masser-type minimal vanishing degree


def total_degree_alphas(D):
    return [(i, j, k) for i in range(D + 1) for j in range(D + 1 - i) for k in range(D + 1 - i - j)]


dmin_rows = []
for N in (2, 3, 4, 5, 6, 7):
    M = N ** 4
    per_field = []
    for dd in (-163, 5, -1000003):
        P1, P2 = split_primes(dd, 2, 2 ** 31 - 1)
        Z1, _ = points_mod(dd, N, P1)
        Z2, _ = points_mod(dd, N, P2)
        D = 0
        while rank_rows(total_degree_alphas(D), Z1, P1) == math.comb(D + 3, 3):
            D += 1   # full rank mod P1 at D certifies: no nonzero K-polynomial of degree <= D vanishes
        # at D: deficiency mod P1; confirm mod P2 (a vanishing polynomial exists mod two primes; over K it exists
        # for sure once C(D+3,3) > N^4)
        conf = rank_rows(total_degree_alphas(D), Z2, P2) < math.comb(D + 3, 3)
        per_field.append((D, conf or math.comb(D + 3, 3) > M))
    Ddim = 0
    while math.comb(Ddim + 3, 3) <= M:
        Ddim += 1
    Ds = sorted(set(x[0] for x in per_field))
    masser = ((N - 1) / 3) ** (4 / 3)
    kerrD = math.floor(0.5 * masser)
    dmin_rows.append((N, Ds, all(x[1] for x in per_field), Ddim, masser, kerrD))
rep(all(len(r[1]) == 1 and r[2] and r[1][0] >= r[4] and r[1][0] > r[5] for r in dmin_rows),
    "(5c) minimal total degree D_min of a nonzero polynomial vanishing on {A n : n in E_N}, three fields "
    "d in {-163, 5, -1000003} (identical in all three); lower bound certified (full rank mod P at D_min-1), "
    "existence at D_min confirmed mod two primes. (N, D_min, dimension-count degree, Masser bound "
    "((N-1)/3)^(4/3), Kerr's D) = "
    + ", ".join(f"({r[0]},{r[1][0]},{r[3]},{r[4]:.2f},{r[5]})" for r in dmin_rows)
    + ". Masser's bound (Kerr Lemma 6 with mu = 4/3) holds in every case.")
info("(5c) D_min sometimes lies one below the dimension-count degree (N = 4, 5, 7): the projected lattice box is "
     "not in general position for total degree. This is our observation, not a claim of any paper; it is "
     "consistent with Masser's theorem, which is a lower bound only.")
ratios = [r[1][0] / r[0] ** (4 / 3) for r in dmin_rows if r[0] >= 3]
info("(5c) D_min / N^(4/3) = " + ", ".join(f"{x:.3f}" for x in ratios)
     + f" (dimension count gives -> 6^(1/3) = {6 ** (1 / 3):.3f}); Masser's constant 3^(-4/3) = {3 ** (-4 / 3):.3f} "
       "is lossy by a factor ~7 but has the same exponent 4/3 = (rank 4)/(3 coordinates)")
# degenerate map: minimal vanishing degree
deg_dmin = []
for N in (3, 4, 5, 6):
    M = N ** 4
    P = split_primes(2, 1, 2 ** 31 - 1)[0]
    Zd, _ = points_mod(2, N, P, b_is_a=True)
    D = 0
    while rank_rows(total_degree_alphas(D), Zd, P) == math.comb(D + 3, 3):
        D += 1
    deg_dmin.append((N, D, 2 * N - 1))
rep(all(r[1] <= r[2] for r in deg_dmin),
    "(5c) degenerate map d=2: (N, minimal vanishing degree mod P, explicit 2N-1 bound) = "
    + ", ".join(str(r) for r in deg_dmin) + "; linear in N, not N^(4/3)")

# ---------------------------------------------------------------- (5d) Guo Lemma 3.3, sharp subset form
PBIG = 2 ** 61 - 1


def guo_iota_rank(d, p0, s0, G, P=PBIG):
    """rank mod P of iota_G: Z^{p0 s0} -> Z^{2|G| s0}; columns (r,s), rows (u,v,j, coefficient)."""
    cols = [(r, s) for r in range(p0) for s in range(s0)]
    rows = []
    for (u, v) in G:
        # powers of x = u + v t and y = u - v t in Z[t]/(t^2-d), mod P, as pairs (A, B) = A + B t
        px = [(1, 0)]
        py = [(1, 0)]
        for _ in range(p0):
            A, B = px[-1]
            px.append(((A * u + B * v * d) % P, (A * v + B * u) % P))
            A, B = py[-1]
            py.append(((A * u - B * v * d) % P, (-A * v + B * u) % P))
        for j in range(s0):
            rA = []
            rB = []
            for (r, s) in cols:
                if j > r:
                    rA.append(0)
                    rB.append(0)
                    continue
                c = math.perm(r, j) % P
                A1, B1 = px[r - j]
                A2, B2 = py[s]
                rA.append(c * (A1 * A2 + B1 * B2 * d) % P)
                rB.append(c * (A1 * B2 + B1 * A2) % P)
            rows.append(rA)
            rows.append(rB)
    m = flint.nmod_mat(len(rows), len(cols), [x for rr in rows for x in rr], P)
    return m.rank(), len(cols)


cases = []
for d in (-163, -7, 5, 13, -1, 229, -3):
    for p0 in sp.primerange(11, 62):
        if legendre(d, p0) != -1:
            continue
        for s0 in sorted(set([1, 2, max(1, p0 // 30), max(1, p0 // 6), (p0 - 1) // 2])):
            if s0 * p0 > 900:
                continue
            cases.append((d, p0, s0))
random.shuffle(cases)
cases = cases[:40]
nok = 0
minimal = []
for (d, p0, s0) in cases:
    pool = [(u, v) for u in range(p0) for v in range(1, (p0 - 1) // 2 + 1)]
    G = random.sample(pool, (p0 + 1) // 2)
    rk, nc = guo_iota_rank(d, p0, s0, G)
    nok += rk == nc
    minimal.append((d, p0, s0, rk, nc))
rep(nok == len(cases),
    f"(5d) Guo Lemma 3.3 at the exact Stepanov threshold |G| = (p0+1)/2 (2|G| = p0+1 > p0), random G, "
    f"{len(cases)} cases (d, p0 in [11,61] inert, s0 from 1 up to (p0-1)/2): injective (certified, rank mod 2^61-1 "
    f"= p0 s0) in {nok}/{len(cases)}; one fewer point makes 2|G| s0 < p0 s0 rows, so injectivity is then impossible: "
    f"the Stepanov count is exactly the dimension count")
info("(5d) sample (d, p0, s0, rank, cols): " + ", ".join(str(x) for x in minimal[:8]))
# Guo's actual grid m = ceil(sqrt p0), with s0 = floor(p0/30) and s0 = 3, 5
gg = []
for (d, p0start) in ((-163, 37), (-7, 31), (5, 37), (13, 31), (-3, 41), (229, 43), (-163, 61)):
    p0 = next(p for p in sp.primerange(p0start, 200) if legendre(d, p) == -1)
    m = math.isqrt(p0 - 1) + 1
    G = [(u, v) for u in range(m) for v in range(1, m)]
    for s0 in sorted(set([max(1, p0 // 30), 3, 5])):
        rk, nc = guo_iota_rank(d, p0, s0, G)
        gg.append((d, p0, m, s0, rk == nc, 2 * m * (m - 1) * s0, nc))
rep(all(x[4] for x in gg), "(5d) Guo's actual grid 0<=u<m, 1<=v<m, m=ceil(sqrt p0): injective in all "
    + f"{len(gg)} cases (d, p0, m, s0, injective, rows, cols): " + ", ".join(str(x) for x in gg))

print("\n".join(out))
print(f"\nSUMMARY: {sum(1 for o in out if o.startswith('PASS'))} PASS, {fails} FAIL")
