"""SIEGEL Level-2 audit, part 2, steps 6-7 (degree concentration; Archimedean size bound).
Our own code; nothing from the audited repositories is executed.  Run: python3 -I s6_s7_concentration_size.py

 (6a) OAI Lemma 6 / Banks Lemma 4.2, toy replay of the weighted greedy selection (mod split primes P < 2^26,
      selection compared between two primes): S1, S2, max weight, versus the a-priori bounds
      w <= 96 H^{2/3} U, S2 <= 192 M H^{-1/3} U, and the first term of (master) (3/4)(1 + S2/S1).
      Also the heuristic 2/H (centroid of the simplex alpha1 + H(alpha2+alpha3) <= W).
 (6b) Kerr's weight 8: exact counts r, W = sum(i+j+k), sum i over i + w(j+k) <= D for several weights w;
      the threshold ratio W / sum(i) -> 1 + 2/w, so (3/4)(1 + 2/w) < 1 iff w > 6; Kerr's w = 8 gives 5/4 < 4/3.
 (7a) OAI (upper)/Banks Lem 5.1 and the divisibility bound, exact toy sandwich: N(Delta) as the determinant of the
      4M x 4M integer regular representation (python-flint), then
         sum_{admissible p} 4 E_p log p  <=  log|N(Delta)|  <=  4[(M/2) log M + (S1+S2)(log N + (1/2)log q + log 8)],
      plus the sharper per-embedding Hadamard bound and v_p(N(Delta)) >= 4 E_p.
 (7b) Guo Lemma 3.2 chain on toys (exact integers):  H = sum_P H_p log p  <=  sum_P v_p(G) log p  <=  log G
      <= log covol(iota(Z^n)) = (1/2) log det(iota^T iota)  <=  sum log ||iota(e_i)||_2,  and  H <= n log n + sum log w_i,
      where G = gcd of maximal minors (= product of the row-HNF diagonal), w_{r,s} = (p0/b0)^{s0-1} b0^{r+s}; also
      ||iota(e_{r,s})||_inf <= w_{r,s}.
"""
import math
import itertools
import numpy as np
import flint
import mpmath as mp
import sympy as sp
from sympy import isprime
from sympy.ntheory.residue_ntheory import sqrt_mod

mp.mp.dps = 50
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
    res = []
    P = start
    while len(res) < count:
        P -= 1
        if isprime(P) and legendre(d, P) == 1 and legendre(2, P) == 1:
            res.append(P)
    return res


def conductor(d):
    return abs(d) if d % 4 == 1 else 4 * abs(d)


def chi(d, p):
    """Kronecker symbol (D/p), D the fundamental discriminant attached to squarefree d."""
    D = d if d % 4 == 1 else 4 * d
    return sp.jacobi_symbol(D % p, p) if p % 2 == 1 else (0 if D % 2 == 0 else (1 if D % 8 in (1, 7) else -1))


# ------------------------------------------------------------------ greedy weighted selection mod P


def greedy(d, N, H, P):
    a = sqrt_mod(d % P, P)
    b = sqrt_mod(2, P)
    ab = a * b % P
    ns = np.array(list(itertools.product(range(N), repeat=4)), dtype=np.int64)
    n1, n2, n3, n4 = ns.T
    Z = [(n1 + n2 * a + n3 * b + n4 * ab) % P, (n1 - n2 * a + n3 * b - n4 * ab) % P,
         (n1 - n2 * a - n3 * b + n4 * ab) % P]
    M = N ** 4
    pw = [[np.ones(M, dtype=np.int64)] for _ in range(3)]

    def pwr(j, k):
        while len(pw[j]) <= k:
            pw[j].append(pw[j][-1] * Z[j] % P)
        return pw[j][k]

    B = np.zeros((0, M), dtype=np.int64)
    piv = []
    kept = []
    W = 0
    while len(kept) < M:
        for k in range(W // H + 1):
            a1 = W - H * k
            for a2 in range(k + 1):
                a3 = k - a2
                v = pwr(0, a1) * pwr(1, a2) % P * pwr(2, a3) % P
                if piv:
                    c = v[piv]
                    v = (v - (c @ B) % P) % P
                nz = np.nonzero(v)[0]
                if len(nz) == 0:
                    continue
                c0 = nz[0]
                v = v * pow(int(v[c0]), P - 2, P) % P
                if piv:
                    B = (B - np.outer(B[:, c0], v) % P) % P
                B = np.vstack([B, v])
                piv.append(c0)
                kept.append((a1, a2, a3))
                if len(kept) == M:
                    return kept
        W += 1
    return kept


# ------------------------------------------------------------------ (6a)
rows6 = []
okbounds = True
agree = True
for (d, N) in ((-163, 3), (5, 3), (-163, 4), (13, 4), (-163, 5)):
    P1, P2 = split_primes(d, 2, 2 ** 26)
    M = N ** 4
    U = N ** (4 / 3)
    for H in (1, 2, 3, 4, 6, 8, 12, 16, 24, 32):
        if N == 5 and H not in (1, 2, 4, 8, 16, 32):
            continue
        k1 = greedy(d, N, H, P1)
        if N <= 4 and H in (1, 4, 16):
            agree &= (sorted(k1) == sorted(greedy(d, N, H, P2)))
        S1 = sum(x[0] for x in k1)
        S2 = sum(x[1] + x[2] for x in k1)
        wmax = max(x[0] + H * (x[1] + x[2]) for x in k1)
        if H <= N:  # range of Cor 4 / Lemma 6
            okbounds &= wmax <= 96 * H ** (2 / 3) * U and S2 <= 192 * M * H ** (-1 / 3) * U
        rows6.append((d, N, H, S1, S2, wmax, S2 / S1 if S1 else float('inf')))
rep(okbounds and agree, "(6a) greedy selection: a-priori bounds w_max <= 96 H^(2/3) U and S2 <= 192 M H^(-1/3) U hold "
    "for every toy with H <= N (the range of Cor 4); selections agree mod two primes")
for N in (3, 4, 5):
    sel = [r for r in rows6 if r[1] == N]
    info(f"(6a) N={N}: (d, H, S1, S2, w_max, S2/S1, 2/H, first term (3/4)(1+S2/S1)) = " + "; ".join(
        f"({r[0]},{r[2]},{r[3]},{r[4]},{r[5]},{r[6]:.3f},{2 / r[2]:.3f},{0.75 * (1 + r[6]):.3f})" for r in sel))
# monotone decrease of S2/S1 in H and the threshold S2/S1 < 1/3 needed for (3/4)(1+S2/S1) < 1
for N in (4, 5):
    sel = [r for r in rows6 if r[1] == N and r[0] == -163]
    dec = all(sel[i + 1][6] <= sel[i][6] for i in range(len(sel) - 1))
    first_ok = next((r[2] for r in sel if r[6] < 1 / 3), None)
    rep(dec, f"(6a) d=-163, N={N}: S2/S1 decreases monotonically in H; first H with S2/S1 < 1/3 (needed for the "
        f"leading coefficient (3/4)(1+S2/S1) < 1): H = {first_ok}. Lemma 6's guaranteed ratio (C0/c0)/H = "
        f"{192 * 4 * 97 ** 2}/H is far more pessimistic (needs H > {3 * 192 * 4 * 97 ** 2}); harmless (T6).")

# ------------------------------------------------------------------ (6b) Kerr weight


def kerr_counts(D, w):
    r = W = Si = 0
    for J in range(D // w + 1):
        imax = D - w * J
        cnt = imax + 1
        mult = J + 1  # number of (j,k) with j + k = J
        r += mult * cnt
        Si += mult * imax * (imax + 1) // 2
        W += mult * (imax * (imax + 1) // 2 + J * cnt)
    return r, W, Si


ok6b = True
lines = []
for w in (4, 5, 6, 7, 8, 12, 16):
    D = 6000
    r, W, Si = kerr_counts(D, w)
    ratio = W / Si
    rh = kerr_counts(3000, w)
    rh = rh[1] / rh[2]
    lines.append(f"w={w}: W/sum(i)={ratio:.5f} (1+2/w={1 + 2 / w:.5f}), (3/4)*ratio={0.75 * ratio:.4f}")
    # finite-D deviation is O(1/D): require it small and shrinking from D=3000 to D=6000
    ok6b &= abs(ratio - (1 + 2 / w)) < 1e-3 and abs(ratio - (1 + 2 / w)) < abs(rh - (1 + 2 / w))
dev = []
for D in (3000, 6000):
    r8, W8, Si8 = kerr_counts(D, 8)
    dev.append((abs(r8 / (D ** 3 / 384) - 1), abs(W8 / (5 * D ** 4 / 6144) - 1)))
ok6b &= dev[1][0] < dev[0][0] and dev[1][1] < dev[0][1] and max(dev[1]) < 1e-2
lines.append(f"w=8 relative deviations of r, W from D^3/384, 5D^4/6144: D=3000 {dev[0][0]:.4f}, {dev[0][1]:.4f}; "
             f"D=6000 {dev[1][0]:.4f}, {dev[1][1]:.4f} (O(1/D))")
rep(ok6b, "(6b) Kerr weight w: exact counts at D=3000, 6000 give W/sum(i) -> 1 + 2/w (our derivation: "
    "sum(j+k)/sum(i) = (D^4/(12w^3))/(D^4/(24w^2)) = 2/w). Leading coefficient (3/4)(1+2/w) < 1 iff w > 6; "
    "Kerr's w = 8 gives 15/16 < 1 (equivalently 5/4 < 4/3, with 13/10 in between). " + "; ".join(lines))

# ------------------------------------------------------------------ (7a) exact sandwich


def mul(x, y, d):
    x1, x2, x3, x4 = x
    y1, y2, y3, y4 = y
    return (x1 * y1 + d * x2 * y2 + 2 * x3 * y3 + 2 * d * x4 * y4,
            x1 * y2 + x2 * y1 + 2 * x3 * y4 + 2 * x4 * y3,
            x1 * y3 + x3 * y1 + d * x2 * y4 + d * x4 * y2,
            x1 * y4 + x4 * y1 + x2 * y3 + x3 * y2)


def regrep(x, d):
    x1, x2, x3, x4 = x
    # columns: x*1, x*a, x*b, x*ab in basis (1, a, b, ab)
    c1 = (x1, x2, x3, x4)
    c2 = (d * x2, x1, d * x4, x3)
    c3 = (2 * x3, 2 * x4, x1, x2)
    c4 = (2 * d * x4, 2 * x3, d * x2, x1)
    return [[c1[i], c2[i], c3[i], c4[i]] for i in range(4)]


ok7 = True
sand = []
for (d, N, H) in ((-163, 2, 1), (-163, 2, 3), (5, 2, 4), (13, 2, 6), (-7, 2, 2), (-3, 2, 5), (-163, 3, 2), (5, 3, 4)):
    P1, P2 = split_primes(d, 2, 2 ** 26)
    kept = greedy(d, N, H, P1)
    kept2 = greedy(d, N, H, P2)
    M = N ** 4
    ns = list(itertools.product(range(N), repeat=4))
    thetas = [(n[0], n[1], n[2], n[3]) for n in ns]
    sig = lambda x: (x[0], -x[1], x[2], -x[3])
    st = lambda x: (x[0], -x[1], -x[2], x[3])
    amax = max(max(k) for k in kept)
    pows = []
    for th in thetas:
        L = [[(1, 0, 0, 0)], [(1, 0, 0, 0)], [(1, 0, 0, 0)]]
        for j, g in enumerate((th, sig(th), st(th))):
            for _ in range(amax):
                L[j].append(mul(L[j][-1], g, d))
        pows.append(L)
    big = [[0] * (4 * M) for _ in range(4 * M)]
    for i, (a1, a2, a3) in enumerate(kept):
        for jn in range(M):
            L = pows[jn]
            e = mul(mul(L[0][a1], L[1][a2], d), L[2][a3], d)
            R = regrep(e, d)
            for r in range(4):
                for c in range(4):
                    big[4 * i + r][4 * jn + c] = R[r][c]
    normD = flint.fmpz_mat(big).det()
    nd = int(normD)
    q = conductor(d)
    S1 = sum(k[0] for k in kept)
    S2 = sum(k[1] + k[2] for k in kept)
    logN = float(mp.log(abs(mp.mpf(nd)))) if nd != 0 else float('-inf')
    upper = 4 * ((M / 2) * math.log(M) + (S1 + S2) * (math.log(N) + 0.5 * math.log(q) + math.log(8)))
    # sharper: per-embedding Hadamard with actual row norms
    emb = []
    for sa in (1, -1):
        for sb in (1, -1):
            av = sa * mp.sqrt(mp.mpf(d)) if d > 0 else sa * mp.sqrt(-d) * 1j
            bv = sb * mp.sqrt(2)
            emb.append((av, bv))
    had = 0
    for (av, bv) in emb:
        for (a1, a2, a3) in kept:
            s = 0
            for jn in range(M):
                L = pows[jn]
                e = mul(mul(L[0][a1], L[1][a2], d), L[2][a3], d)
                val = e[0] + e[1] * av + e[2] * bv + e[3] * av * bv
                s += abs(val) ** 2
            had += float(mp.log(mp.sqrt(s)))
    lower = 0.0
    lower_all = 0.0
    vp_ok = True
    for p in sp.primerange(3, amax + 1):
        Ep = sum(k[0] // p for k in kept)
        if p > H and q % p and chi(d, p) == -1 and Ep:
            lower += 4 * Ep * math.log(p)
            v = 0
            t = abs(nd)
            while t % p == 0:
                t //= p
                v += 1
            vp_ok &= v >= 4 * Ep
    ok = nd != 0 and lower <= logN + 1e-9 and logN <= had + 1e-9 and had <= upper + 1e-9 and vp_ok
    ok7 &= ok and sorted(kept) == sorted(kept2)
    sand.append((d, N, H, M, S1, S2, lower, logN, had, upper))
rep(ok7, "(7a) exact sandwich in 8 toys: N(Delta) != 0, v_p(N(Delta)) >= 4 E_p for admissible p, and "
    "sum_adm 4E_p log p <= log|N(Delta)| <= per-embedding Hadamard <= OAI (upper) (x4)")
info("(7a) (d, N, H, M, S1, S2, divisibility lower, log|N(Delta)|, Hadamard actual, OAI upper) = " + "; ".join(
    f"({r[0]},{r[1]},{r[2]},{r[3]},{r[4]},{r[5]},{r[6]:.1f},{r[7]:.1f},{r[8]:.1f},{r[9]:.1f})" for r in sand))
info("(7a) at toy sizes log|N(Delta)| sits far below the Hadamard bound and far above the admissible-prime "
     "divisibility (few admissible primes <= max alpha1): no contradiction is expected or obtained; the toys only "
     "certify that both inequalities are correctly oriented and that N(Delta) != 0")

# ------------------------------------------------------------------ (7b) Guo Lemma 3.2 chain


def guo_iota_exact(d, p0, s0, m):
    cols = [(r, s) for r in range(p0) for s in range(s0)]
    G = [(u, v) for u in range(m) for v in range(1, m)]
    rows = []
    for (u, v) in G:
        px = [(1, 0)]
        py = [(1, 0)]
        for _ in range(p0):
            A, B = px[-1]
            px.append((A * u + B * v * d, A * v + B * u))
            A, B = py[-1]
            py.append((A * u - B * v * d, -A * v + B * u))
        for j in range(s0):
            rA, rB = [], []
            for (r, s) in cols:
                if j > r:
                    rA.append(0)
                    rB.append(0)
                    continue
                c = math.perm(r, j)
                A1, B1 = px[r - j]
                A2, B2 = py[s]
                rA.append(c * (A1 * A2 + B1 * B2 * d))
                rB.append(c * (A1 * B2 + B1 * A2))
            rows.append(rA)
            rows.append(rB)
    return rows, cols


ok7b = True
chain = []
for (d, p0start, s0) in ((-3, 31, 1), (-3, 41, 2), (-7, 31, 1), (-7, 41, 2), (5, 37, 1), (-1, 31, 2),
                         (13, 59, 1)):
    q = conductor(d)
    p0 = next(p for p in sp.primerange(max(p0start, 4 * q), 400) if legendre(d, p) == -1)
    m = math.isqrt(p0 - 1) + 1
    rows, cols = guo_iota_exact(d, p0, s0, m)
    A = flint.fmpz_mat(rows)
    n = len(cols)
    assert A.rank() == n
    # row-HNF: A = U [T; 0] with U unimodular, T upper triangular n x n, so the elementary divisors of A are
    # those of T and G = gcd of maximal minors = |det T| = product of the HNF diagonal (SNF itself is too slow)
    Hm = A.hnf()
    diag = [int(Hm[i, i]) for i in range(n)]
    assert all(diag) and all(Hm[i, j] == 0 for i in range(n, A.nrows()) for j in range(n))
    Gint = 1
    for x in diag:
        Gint *= abs(x)
    logG = float(mp.log(mp.mpf(Gint)))
    diag = [Gint]
    Pset = [p for p in sp.primerange(3, p0 + 1) if legendre(d, p) == -1]
    Hp = {p: sum(min(r // p, s0 - 1 - s) for (r, s) in cols) for p in Pset}
    Htoy = sum(Hp[p] * math.log(p) for p in Pset)
    vpG = {}
    for p in Pset:
        v = 0
        for x in diag:
            x = abs(x)
            while x % p == 0:
                x //= p
                v += 1
        vpG[p] = v
    sumP = sum(vpG[p] * math.log(p) for p in Pset)
    gram = (A.transpose() * A).det()
    logcov = 0.5 * float(mp.log(mp.mpf(int(gram))))
    colnorm = 0.0
    inf_ok = True
    b0 = 2 * math.sqrt(p0 * q)
    sumlogw = 0.0
    for ci, (r, s) in enumerate(cols):
        col = [rows[ri][ci] for ri in range(len(rows))]
        colnorm += 0.5 * float(mp.log(mp.mpf(sum(x * x for x in col)))) if any(col) else float('-inf')
        lw = (s0 - 1) * math.log(p0 / b0) + (r + s) * math.log(b0)
        sumlogw += lw
        inf_ok &= max(abs(x) for x in col) <= math.exp(lw) * (1 + 1e-12)
    rhs = n * math.log(n) + sumlogw
    ok = (all(vpG[p] >= Hp[p] for p in Pset) and Htoy <= sumP + 1e-9 and sumP <= logG + 1e-9
          and logG <= logcov + 1e-9 and logcov <= colnorm + 1e-9 and Htoy <= rhs and inf_ok)
    ok7b &= ok
    chain.append((d, p0, s0, n, Htoy, sumP, logG, logcov, colnorm, rhs, sum(vpG[p] == Hp[p] for p in Pset), len(Pset)))
rep(ok7b, "(7b) Guo Lemma 3.2 chain holds in all 7 toys (with p0 >= 4q, so w_{r,s} is Guo's): v_p(G) >= H_p for "
    "every inert p <= p0, H <= sum_P v_p(G) log p <= log G <= log covol <= sum log||col||_2, H <= n log n + "
    "sum log w_i, and ||iota(e_{r,s})||_inf <= w_{r,s}")
info("(7b) (d, p0, s0, n, H, sum_P v_p(G) log p, log G, log covol, column Hadamard, Lemma 3.2 RHS, "
     "#{p: v_p(G)=H_p}/#P) = " + "; ".join(
         f"({c[0]},{c[1]},{c[2]},{c[3]},{c[4]:.1f},{c[5]:.1f},{c[6]:.1f},{c[7]:.1f},{c[8]:.1f},{c[9]:.1f},"
         f"{c[10]}/{c[11]})" for c in chain))
info("(7b) the dominant loss in Lemma 3.2 at toy size is the n log n term and the sup-norm weights w_{r,s} "
     "(which use b0 = 2 sqrt(p0 q) for every derivative order); asymptotically n log n = o(p0^2 s0 log p0), "
     "so it does not affect the exponent 11/20")

print("\n".join(out))
print(f"\nSUMMARY: {sum(1 for o in out if o.startswith('PASS'))} PASS, {fails} FAIL")
