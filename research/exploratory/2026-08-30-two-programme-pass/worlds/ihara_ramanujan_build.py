"""World 'ihara_ramanujan': Ihara zeta functions of two exact Ramanujan cubic
graphs, K4 and the Petersen graph.

Deterministic build script (no input, no randomness).  Run from pass root:

    python3 -m worlds.ihara_ramanujan_build

regenerates worlds/ihara_ramanujan.json identically.

All arithmetic is exact (int / Fraction).  NO floats anywhere in this file.

What is computed and PROVED HERE (exact, asserted, embedded as witnesses):

  1. Characteristic polynomials of the adjacency matrices via exact
     Faddeev-LeVerrier (charpoly_of_matrix), plus their COMPLETE integer
     factorizations:  K4: (x-3)(x+1)^3;  Petersen: (x-3)(x-1)^5(x+2)^4.

  2. RAMANUJAN CERTIFICATE, fully exact and factorization-independent:
     s(x) = charpoly(x)/(x-3) (exact division, remainder 0; 3 is a simple
     root; -3 is not a root, so s carries exactly the nontrivial spectrum).
     From s, power sums of its roots via Newton (power_sums_from_satake on
     the reversed monic polynomial), then the power sums of the SQUARED
     roots are p_{2k}, giving the exact integer polynomial s2(y) whose roots
     are the squares of the nontrivial eigenvalues.  Sturm root counting
     (count_real_roots_in, exact rational endpoints) certifies s2 has NO
     roots in (8, B] for B beyond the Cauchy bound, and none in (9/2, B]
     either, while all distinct roots lie in (0, 8].  Hence every eigenvalue
     lambda != 3 satisfies lambda^2 <= 8 (indeed <= 9/2): Ramanujan.

  3. BASS THREE-TERM IDENTITY, instance-proved coefficient-wise for BOTH
     graphs (and for the double cover of K4):
         det(I - uB) = (1 - u^2)^{|E|-|V|} det(I - Au + 2u^2 I)
     with B the 2|E| x 2|E| non-backtracking (Hashimoto) edge operator built
     explicitly from the graph.  LHS = reversed exact charpoly of B; RHS
     computed TWICE independently: exact cofactor determinant of the
     polynomial matrix (subset-DP cofactor expansion over Q[u]) and the
     spectral product prod_lambda (1 - lambda u + 2 u^2).

  4. GEODESIC SIDE anchored combinatorially: N_m = tr(B^m) (exact integer
     matrix powers) equals an INDEPENDENT pure-DFS count of closed
     non-backtracking tailless rooted oriented cycles of length m, for
     m = 1..12; and equals the power sums of the inverse roots of
     det(I - uB) (power_sums_from_satake).  Anchors: K4 N_3 = 24
     (4 triangles x 6 rootings), N_4 = 24 (3 quadrilaterals x 8);
     Petersen N_3 = N_4 = 0 (girth 5), N_5 = 120 (12 pentagons x 10).

  5. EULER PRODUCT WINDOW: primitive geodesic class counts P_m from the
     exact Moebius-type recursion N_m = sum_{d|m} d P_d are nonnegative
     integers (K4: P_3 = 8, P_4 = 6; Petersen: P_5 = 24), and
     zeta(u) * prod_{m<=12} (1 - u^m)^{P_m} = 1 + O(u^13) exactly; the
     zeta coefficients a_0..a_12 are nonnegative integers.

  6. FUNCTIONAL EQUATION, exact: with h(u) = det(I - Au + 2u^2 I), the
     reflection q^n u^{2n} h(1/(qu)) == h(u) holds coefficient-wise (q = 2),
     and the cleared-denominator FE for 1/zeta holds with an exactly
     computed sign (-1)^{|E|-|V|}: +1 for K4, -1 for Petersen.

  7. GRAPH-RH FOR THESE INSTANCES: every nontrivial eigenvalue lambda has
     disc = lambda^2 - 8 < 0 exactly, so the two roots of 2u^2 - lambda u + 1
     form a complex-conjugate pair with product 1/2, i.e. |u|^2 = 1/2: all
     nontrivial poles of zeta lie ON the circle |u| = 1/sqrt(2) = q^{-1/2}
     (Re s = 1/2 under u = q^{-s}).  Trivial poles u = 1, 1/2 are off it.

  8. TWIST INSTANCE: for the bipartite double cover D of K4 (8 vertices,
     12 edges), zeta_D = zeta_K4 * L(u, chi) with L the Artin-Ihara
     L-function of the sign character; all polynomials computed
     independently (including via D's own 24x24 edge operator) and the
     factorization asserted coefficient-wise.

  9. Detector runs (core.reconstruct.detect) on the quadratic local factors
     1/(1 - lambda u + 2u^2) with purity weight (q, w) = (2, 1): full pass
     for the nontrivial factors lambda in {-1, 1, -2}; REFUSAL at A4_PURITY
     for the trivial Perron factor lambda = 3 (disc = 1 > 0) - the detector
     separates the trivial pole pair from the pure ones.

Imported (cited, never fabricated): the geodesic Euler-product definition
and rationality (Ihara 1966), the general Ihara-Bass theorem (Bass 1992;
Hashimoto 1989), graph-RH <=> Ramanujan framing and functional equations
(Terras 2011 book; Sunada 1986), covering theory of graph zetas
(Stark-Terras 1996/2000), existence of infinite Ramanujan families
(Lubotzky-Phillips-Sarnak 1988; Margulis 1988; Marcus-Spielman-Srivastava
2015), sharpness (Alon-Boppana; Nilli 1991).

Nothing here bears on the classical RH: rh_established = false.
"""

from fractions import Fraction

from core.exact import (
    F,
    charpoly_of_matrix,
    charpoly_from_power_sums,
    count_real_roots_in,
    is_integer_poly,
    poly_add,
    poly_divmod,
    poly_eval,
    poly_mul,
    poly_scale,
    poly_trim,
    power_sums_from_satake,
    series_of_rational,
)
from core.reconstruct import detect
from core.worlds import cell, save_world, validate_world

Q_REG = 2          # both graphs are (q+1)-regular with q = 2
NM_MAX = 12        # geodesic-count / Euler-window depth


# ---------------------------------------------------------------------------
# small exact helpers (Fractions only)
# ---------------------------------------------------------------------------

def poly_pow(p, k):
    out = [Fraction(1)]
    for _ in range(k):
        out = poly_mul(out, p)
    return out


def ipoly_str(p):
    p = poly_trim([F(c) for c in p]) or [Fraction(0)]
    assert is_integer_poly(p)
    return "[" + ", ".join(str(int(c)) for c in p) + "]"


def det_poly_matrix(M):
    """Exact determinant of a matrix of polynomials over Q: cofactor
    expansion memoized on column subsets (O(2^n n) polynomial operations).
    M[i][j] is a low-first Fraction coefficient list."""
    n = len(M)
    prev = {0: [Fraction(1)]}
    for r in range(n):
        cur = {}
        for S, val in prev.items():
            if not val:
                continue
            for c_col in range(n):
                if (S >> c_col) & 1:
                    continue
                entry = M[r][c_col]
                if not poly_trim(entry):
                    continue
                j = bin(S & ((1 << c_col) - 1)).count("1")
                term = poly_mul(entry, val)
                if (r + j) % 2 == 1:
                    term = poly_scale(term, -1)
                newS = S | (1 << c_col)
                cur[newS] = poly_add(cur.get(newS, []), term)
        prev = cur
    return prev.get((1 << n) - 1, [])


def three_term_matrix(A, sign=-1):
    """Polynomial matrix I - (sign=-1) A u + q u^2 I  (entries in Q[u]).
    sign=+1 gives I + A u + q u^2 I (used for the sign-character twist)."""
    n = len(A)
    diag = [Fraction(1), Fraction(0), Fraction(Q_REG)]
    return [[(diag if i == j else poly_trim([Fraction(0),
                                             Fraction(sign * A[i][j])]))
             for j in range(n)] for i in range(n)]


def safe_count(p, a, b):
    """Sturm count on (a, b] with both endpoints certified non-roots (safe
    also for non-squarefree p: the last chain element divides p)."""
    a, b = F(a), F(b)
    assert a < b
    assert poly_eval(p, a) != 0 and poly_eval(p, b) != 0
    return count_real_roots_in(p, a, b)


def tmul(a, b, K):
    """Truncated series product mod u^K."""
    out = [Fraction(0)] * K
    for i, x in enumerate(a[:K]):
        if x == 0:
            continue
        for j, y in enumerate(b[:K - i]):
            if y == 0:
                continue
            out[i + j] += x * y
    return out


def tpow(p, e, K):
    out = [Fraction(1)] + [Fraction(0)] * (K - 1)
    base = ([F(c) for c in p] + [Fraction(0)] * K)[:K]
    while e:
        if e & 1:
            out = tmul(out, base, K)
        base = tmul(base, base, K)
        e >>= 1
    return out


# ---------------------------------------------------------------------------
# graphs and their non-backtracking (Hashimoto) edge operators
# ---------------------------------------------------------------------------

def k4_adjacency():
    return [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]


def petersen_adjacency():
    """Outer 5-cycle 0..4, spokes i ~ 5+i, inner pentagram 5+i ~ 5+((i+2)%5)."""
    A = [[0] * 10 for _ in range(10)]

    def link(i, j):
        A[i][j] = 1
        A[j][i] = 1

    for i in range(5):
        link(i, (i + 1) % 5)
        link(i, 5 + i)
        link(5 + i, 5 + ((i + 2) % 5))
    return A


def directed_edges(A):
    n = len(A)
    return [(i, j) for i in range(n) for j in range(n) if A[i][j]]


def hashimoto_matrix(A):
    """B[e][f] = 1 iff f follows e without backtracking: head(e) = tail(f)
    and head(f) != tail(e)."""
    E = directed_edges(A)
    m = len(E)
    B = [[1 if E[a][1] == E[b][0] and E[b][1] != E[a][0] else 0
          for b in range(m)] for a in range(m)]
    return E, B


def int_mat_mul(X, Y):
    n = len(X)
    return [[sum(X[i][t] * Y[t][j] for t in range(n)) for j in range(n)]
            for i in range(n)]


def traces_of_powers(B, M):
    n = len(B)
    P = [row[:] for row in B]
    out = [sum(P[i][i] for i in range(n))]
    for _ in range(M - 1):
        P = int_mat_mul(P, B)
        out.append(sum(P[i][i] for i in range(n)))
    return out


def closed_geodesic_count(A, m):
    """INDEPENDENT combinatorial count (pure integer DFS, no linear algebra)
    of closed non-backtracking tailless rooted oriented cycles of length m:
    directed-edge sequences e_1..e_m, consecutive steps non-backtracking
    INCLUDING the wrap-around e_m -> e_1 (the tailless condition)."""
    n = len(A)
    nbrs = [[j for j in range(n) if A[i][j]] for i in range(n)]
    total = 0
    for a0 in range(n):
        for b0 in nbrs[a0]:
            stack = [(b0, a0, 1)]           # (current, previous, edges used)
            while stack:
                v, prev, used = stack.pop()
                if used == m:
                    # closed iff back at a0; tailless iff first edge (a0,b0)
                    # does not backtrack the last edge (prev, v)
                    if v == a0 and b0 != prev:
                        total += 1
                    continue
                for w in nbrs[v]:
                    if w != prev:
                        stack.append((w, v, used + 1))
    return total


# ---------------------------------------------------------------------------
# per-graph exact analysis
# ---------------------------------------------------------------------------

def analyze_graph(name, A, eig_factors):
    """eig_factors: complete integer eigenvalue factorization [(lambda, mult)].
    Every claim below is asserted exactly before being embedded."""
    n = len(A)
    for i in range(n):
        assert A[i][i] == 0
        assert sum(A[i]) == Q_REG + 1
        for j in range(n):
            assert A[i][j] in (0, 1) and A[i][j] == A[j][i]
    Elist = directed_edges(A)
    twoE = len(Elist)
    Eu = twoE // 2
    r1 = Eu - n                       # r - 1 = |E| - |V|
    assert r1 == n * (Q_REG - 1) // 2

    # (1) exact charpoly + complete integer factorization -------------------
    charA = charpoly_of_matrix(A)
    assert is_integer_poly(charA) and len(charA) == n + 1 and charA[-1] == 1
    expected = [Fraction(1)]
    for lam, mult in eig_factors:
        expected = poly_mul(expected,
                            poly_pow([Fraction(-lam), Fraction(1)], mult))
    assert charA == expected
    assert sum(m for _, m in eig_factors) == n

    # trivial eigenvalue 3 simple; -3 absent (non-bipartite)
    assert poly_eval(charA, 3) == 0
    s, rem = poly_divmod(charA, [Fraction(-3), Fraction(1)])
    assert rem == []
    assert poly_eval(s, 3) != 0
    assert poly_eval(charA, -3) != 0
    d = len(s) - 1                    # number of nontrivial eigenvalues

    # (2) Ramanujan certificate: Sturm on s2, factorization-independent ----
    satake_s = list(reversed(s))      # prod (1 - lambda T), constant term 1
    assert satake_s[0] == 1
    ps = power_sums_from_satake(satake_s, 2 * d)
    p_sq = [ps[2 * k - 1] for k in range(1, d + 1)]   # p_k of squared roots
    s2 = charpoly_from_power_sums(p_sq, d)
    assert is_integer_poly(s2) and s2[-1] == 1
    s2_expected = [Fraction(1)]
    for lam, mult in eig_factors:
        if lam != 3:
            s2_expected = poly_mul(
                s2_expected, poly_pow([Fraction(-lam * lam), Fraction(1)], mult))
    assert s2 == s2_expected          # independent confirmation
    cauchy = 1 + max(abs(c) for c in s2[:-1])
    hi = max(F(cauchy), Fraction(9))  # strictly above 8 and above all roots
    n_above8 = safe_count(s2, Fraction(8), hi)
    assert n_above8 == 0              # RAMANUJAN: no lambda^2 > 8
    n_above92 = safe_count(s2, Fraction(9, 2), hi)
    assert n_above92 == 0             # stronger: lambda^2 <= 9/2
    assert safe_count(s2, -hi, Fraction(0)) == 0
    distinct = len({lam for lam, _ in eig_factors if lam != 3})
    assert safe_count(s2, Fraction(0), Fraction(8)) == distinct

    # (3) pole purity: each nontrivial quadratic has conjugate roots on
    #     |u|^2 = 1/q exactly (disc < 0, root product 1/q) -----------------
    purity_bits = []
    for lam, _ in eig_factors:
        if lam == 3:
            continue
        disc = Fraction(lam * lam - 4 * Q_REG)
        assert disc < 0
        purity_bits.append(
            f"lambda={lam}: disc=lambda^2-8={int(disc)}<0, so the roots of "
            f"2u^2-{lam}u+1 are a conjugate pair with product 1/2: |u|^2=1/2")
    # trivial factor splits off the circle: (1-3u+2u^2) = (1-u)(1-2u)
    assert poly_mul([Fraction(1), Fraction(-1)],
                    [Fraction(1), Fraction(-2)]) == \
        [Fraction(1), Fraction(-3), Fraction(2)]

    # (4) Bass three-term identity, all three legs computed ----------------
    h_dp = det_poly_matrix(three_term_matrix(A))     # cofactor route
    h_spec = [Fraction(1)]
    for lam, mult in eig_factors:                    # spectral route
        h_spec = poly_mul(
            h_spec, poly_pow([Fraction(1), Fraction(-lam), Fraction(Q_REG)],
                             mult))
    assert h_dp == h_spec
    _, Bmat = hashimoto_matrix(A)
    assert len(Bmat) == twoE
    charB = charpoly_of_matrix(Bmat)
    assert is_integer_poly(charB) and charB[-1] == 1
    det_I_uB = list(reversed(charB))                 # det(I - uB), low-first
    assert det_I_uB[0] == 1
    inv_zeta = poly_mul(
        poly_pow([Fraction(1), Fraction(0), Fraction(-1)], r1), h_dp)
    assert det_I_uB == inv_zeta                      # BASS, instance-proved
    assert len(inv_zeta) - 1 == 2 * Eu

    # (5) geodesic counts: three independent computations agree ------------
    trB = traces_of_powers(Bmat, NM_MAX)
    Ndfs = [closed_geodesic_count(A, m) for m in range(1, NM_MAX + 1)]
    assert trB == Ndfs
    psB = power_sums_from_satake([F(c) for c in det_I_uB], NM_MAX)
    assert psB == [Fraction(x) for x in trB]

    # primitive geodesic classes and exact Euler-product window ------------
    P = {}
    for m in range(1, NM_MAX + 1):
        acc = trB[m - 1] - sum(dd * P[dd] for dd in range(1, m) if m % dd == 0)
        assert acc % m == 0
        P[m] = acc // m
        assert P[m] >= 0
    K = NM_MAX + 1
    zc = series_of_rational([Fraction(1)], inv_zeta, K)   # a_0 .. a_12
    assert all(c.denominator == 1 and c >= 0 for c in zc)
    Tser = (list(zc) + [Fraction(0)] * K)[:K]
    for m in range(1, NM_MAX + 1):
        if P[m]:
            fac = [Fraction(0)] * K
            fac[0] = Fraction(1)
            fac[m] = Fraction(-1)
            Tser = tmul(Tser, tpow(fac, P[m], K), K)
    assert Tser[0] == 1 and all(c == 0 for c in Tser[1:])

    # (6) functional equation, exact ---------------------------------------
    q = Fraction(Q_REG)
    assert len(h_dp) - 1 == 2 * n
    refl = [h_dp[2 * n - j] * q ** (j - n) for j in range(2 * n + 1)]
    assert poly_trim(refl) == h_dp        # q^n u^{2n} h(1/(qu)) == h(u)
    Dz = len(inv_zeta) - 1                # = 2n + 2(r-1)
    lhs = [inv_zeta[Dz - j] * q ** (j - n) for j in range(Dz + 1)]
    rhs = poly_scale(
        poly_mul(poly_pow([Fraction(1), Fraction(0), -q * q], r1), h_dp),
        Fraction(-1) ** r1)
    assert poly_trim(lhs) == poly_trim(rhs)
    fe_sign = (-1) ** r1

    # anchors for geodesic counts (hand-derived combinatorics) -------------
    assert trB[0] == 0 and trB[1] == 0    # simple graph: no 1- or 2-geodesics
    if name == "K4":
        assert trB[2] == 24 and Ndfs[2] == 24   # 4 triangles x 3 starts x 2 dirs
        assert trB[3] == 24                     # 3 quadrilaterals x 4 x 2
        assert P[3] == 8 and P[4] == 6          # primitive classes
    if name == "Petersen":
        assert trB[2] == 0 and trB[3] == 0      # girth 5
        assert trB[4] == 120                    # 12 pentagons x 5 starts x 2 dirs
        assert P[5] == 24                       # 12 pentagons x 2 orientations

    # witness strings -------------------------------------------------------
    Wit = {
        "charpoly":
            f"{name}: charpoly(A) = {ipoly_str(charA)} (low-first, exact "
            f"Faddeev-LeVerrier) = prod (x-lambda)^m over "
            f"{eig_factors} (asserted coefficient-wise)",
        "ramanujan":
            f"{name}: s = charpoly/(x-3) exact (remainder 0, 3 simple, -3 "
            f"not a root); s2(y) with roots = squared nontrivial eigenvalues "
            f"= {ipoly_str(s2)} via Newton power sums p_2k; exact Sturm: "
            f"#roots in (8, {hi}] = 0 and in (9/2, {hi}] = 0; all {distinct} "
            f"distinct roots in (0, 8]; hence lambda^2 <= 8 (indeed <= 9/2) "
            f"for every eigenvalue lambda != 3: RAMANUJAN, fully exact",
        "bass":
            f"{name}: Bass identity proved coefficient-wise: det(I - uB) "
            f"(reversed exact charpoly of the {twoE}x{twoE} Hashimoto "
            f"operator) == (1-u^2)^{r1} * det(I - Au + 2u^2 I), the latter "
            f"computed twice (exact cofactor determinant over Q[u] == "
            f"spectral product); 1/zeta = {ipoly_str(inv_zeta)} "
            f"(degree {2 * Eu} = 2|E|)",
        "geodesics":
            f"{name}: N_m = tr(B^m) (exact integer powers) == independent "
            f"DFS count of closed non-backtracking tailless cycles == power "
            f"sums of inverse roots of det(I-uB), m=1..{NM_MAX}: "
            f"{trB}; primitive classes P_m = "
            f"{[P[m] for m in range(1, NM_MAX + 1)]} (nonnegative integers); "
            f"zeta coefficients a_0..a_{NM_MAX} = "
            f"{[int(c) for c in zc]} (nonnegative integers); "
            f"zeta * prod_(m<={NM_MAX}) (1-u^m)^P_m == 1 + O(u^13) exactly",
        "fe":
            f"{name}: exact reflection 2^{n} u^{2 * n} h(1/(2u)) == h(u) "
            f"coefficient-wise, h = det(I - Au + 2u^2 I); "
            f"cleared-denominator FE for 1/zeta holds with sign "
            f"(-1)^(r-1) = {fe_sign:+d}",
        "purity": f"{name}: " + "; ".join(purity_bits) +
            "; trivial factor (1-3u+2u^2) = (1-u)(1-2u): poles u=1, u=1/2 "
            "with |u|^2 in {1, 1/4}, OFF the circle |u|^2 = 1/2 "
            "(analogues of s=0, s=1)",
    }
    return {"name": name, "n": n, "E": Eu, "r1": r1, "charA": charA,
            "h": h_dp, "inv_zeta": inv_zeta, "s2": s2, "trB": trB, "P": P,
            "zc": zc, "fe_sign": fe_sign, "witness": Wit}


# ---------------------------------------------------------------------------
# twist instance: bipartite double cover of K4
# ---------------------------------------------------------------------------

def double_cover_check(k4):
    """zeta_D = zeta_K4 * L(u, chi) for the sign character chi of the
    bipartite double cover D of K4; every polynomial computed independently."""
    A = k4_adjacency()
    D = [[0] * 8 for _ in range(8)]
    for i in range(4):
        for j in range(4):
            if A[i][j]:
                D[i][4 + j] = 1
                D[4 + i][j] = 1
    for i in range(8):
        assert sum(D[i]) == 3 and D[i][i] == 0

    charA = k4["charA"]
    charD = charpoly_of_matrix(D)
    neg_charA = [((-1) ** k) * F(c) for k, c in enumerate(charA)]  # charA(-x)
    assert charD == poly_trim(poly_mul(charA, neg_charA))

    h_D = det_poly_matrix(three_term_matrix(D))            # det(I - A_D u + 2u^2)
    h_plus = det_poly_matrix(three_term_matrix(A, sign=+1))  # det(I + A u + 2u^2)
    assert h_D == poly_mul(k4["h"], h_plus)

    om = [Fraction(1), Fraction(0), Fraction(-1)]          # 1 - u^2
    inv_zeta_D = poly_mul(poly_pow(om, 4), h_D)            # |E|-|V| = 12-8 = 4
    inv_L_chi = poly_mul(poly_pow(om, 2), h_plus)          # Artin-Ihara L(u,chi)
    assert inv_zeta_D == poly_mul(k4["inv_zeta"], inv_L_chi)

    # third leg: the cover's own 24x24 Hashimoto operator
    _, BD = hashimoto_matrix(D)
    assert len(BD) == 24
    charBD = charpoly_of_matrix(BD)
    assert list(reversed(charBD)) == inv_zeta_D

    return {
        "witness":
            "bipartite double cover D of K4 (8 vertices, 12 edges, cubic): "
            "charpoly(A_D) == charpoly(A) * charpoly(A)(-x) exactly; "
            "det(I - A_D u + 2u^2) == det(I - Au + 2u^2) * det(I + Au + 2u^2) "
            "(all by exact cofactor determinants); with L(u,chi)^-1 = "
            "(1-u^2)^2 det(I + Au + 2u^2) (Artin-Ihara, sign character), "
            "1/zeta_D == (1/zeta_K4) * (1/L(u,chi)) coefficient-wise; "
            "independently confirmed by 1/zeta_D == det(I - u B_D) from the "
            "cover's own 24x24 non-backtracking operator; 1/L(u,chi) = " +
            ipoly_str(inv_L_chi),
        "inv_L_chi": inv_L_chi,
    }


# ---------------------------------------------------------------------------
# detector runs on the quadratic local factors
# ---------------------------------------------------------------------------

def run_detector():
    runs = []
    cases = [("K4 nontrivial lambda=-1", -1, True),
             ("Petersen nontrivial lambda=1", 1, True),
             ("Petersen nontrivial lambda=-2", -2, True),
             ("trivial Perron factor lambda=3 (control)", 3, False)]
    for label, lam, expect_pass in cases:
        sat = [Fraction(1), Fraction(-lam), Fraction(2)]
        ser = series_of_rational([Fraction(1)], sat, 12)
        v = detect(ser, mode="coefficients", weight=(2, 1), holdout=4)
        dd = v.as_dict()
        got = {c["axiom"]: c["status"] for c in dd["cells"]}
        if expect_pass:
            assert dd["refusal"] is None, (label, dd)
            assert got == {"A1_FINITE_RANK": "HOLDS", "A2_EFFECTIVITY": "HOLDS",
                           "A3_INTEGRALITY": "HOLDS", "A4_PURITY": "HOLDS",
                           "A5_HELD_OUT": "HOLDS"}, (label, got)
        else:
            assert dd["refusal"] == "A4_PURITY", (label, dd)
            assert got["A4_PURITY"] == "FAILS"
        assert dd["object"]["degree"] == 2
        runs.append({"label": label, "weight": [2, 1], "mode": "coefficients",
                     "series": f"a_k of 1/(1 - ({lam})u + 2u^2), window 12",
                     "verdict": dd})
    return runs


# ---------------------------------------------------------------------------
# the world record
# ---------------------------------------------------------------------------

def build_world(k4, pet, cover, detector_runs):
    ihara = "Y. Ihara (1966), zeta functions of discrete cocompact p-adic groups"
    bass = "H. Bass (1992), Ihara-Selberg zeta of a tree lattice"
    hashimoto = "K. Hashimoto (1989), zeta functions of finite graphs (edge operator)"
    terras = ("A. Terras (2011), Zeta Functions of Graphs: A Stroll through "
              "the Garden, Cambridge Univ. Press")
    stark_terras = ("H. M. Stark, A. A. Terras (1996; Part II 2000), zeta "
                    "functions of finite graphs and coverings, Adv. Math.")
    lps = "A. Lubotzky, R. Phillips, P. Sarnak (1988), Ramanujan graphs"
    kotani_sunada = "M. Kotani, T. Sunada (2000), zeta functions of finite graphs"

    both = lambda key: k4["witness"][key] + " || " + pet["witness"][key]

    ladder = {
        "L0_WELL_DEFINED": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("zeta_G(u) = prod over primitive geodesic classes [P] of "
                     "(1 - u^len(P))^-1; for a finite graph 1/zeta is an "
                     "explicit integer polynomial, computed exactly here: " +
                     both("bass")),
            citation=ihara),
        "L1_MULTIPLICATIVITY": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("the coefficients a_n of zeta count effective divisors "
                     "(multisets of primitive classes of total length n), the "
                     "graph analogue of multiplicativity over prime powers; "
                     "verified exactly on the degree-12 window: " +
                     both("geodesics")),
            citation=ihara + "; " + terras),
        "L2_EULER_PRODUCT": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("Euler product over prime geodesic cycles; window-exact "
                     "instance check: primitive class counts P_m from "
                     "N_m = sum_{d|m} d P_d are nonnegative integers and "
                     "zeta * prod_(m<=12)(1-u^m)^P_m == 1 + O(u^13) for both "
                     "graphs (see L1 witness); full identity imported"),
            citation=ihara + "; " + terras),
        "L3_BOUNDED_DEGREE_RATIONAL": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("in the norm variable N(P)^-s = u^len(P) every local "
                     "factor is (1 - N(P)^-s)^-1: degree 1 uniformly; global "
                     "rationality proved exactly here: 1/zeta is a degree-"
                     "2|E| integer polynomial (12 for K4, 30 for Petersen), "
                     "coefficient lists embedded in the L0 witness"),
            citation=ihara),
        "L4_WEIGHT_DUALITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("exact reflection q^n u^2n h(1/(qu)) == h(u) verified "
                     "coefficient-wise for both graphs (self-duality under "
                     "u <-> 1/(qu), i.e. s <-> 1-s); nontrivial inverse-root "
                     "pairs are conjugate with |u|^2 = 1/q exactly: " +
                     both("purity")),
            citation=terras),
        "L5_CONDUCTOR_GAMMA_ROOT": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("gamma-factor analogue: the elementary factor "
                     "(1-u^2)^(r-1), r-1 = |E|-|V| (2 for K4, 5 for "
                     "Petersen); conductor analogue trivial (finite "
                     "unramified object); root-number analogue computed "
                     "exactly here: the cleared-denominator FE holds with "
                     "sign (-1)^(r-1) = +1 for K4 and -1 for Petersen; note "
                     "the completion is canonical in form but not unique "
                     "(Terras gives three standard FEs)"),
            citation=ihara + "; " + terras),
        "L6_CONTINUATION_FE": cell(
            "HOLDS", "PROVED_HERE",
            witness=("continuation: zeta is the reciprocal of an explicit "
                     "polynomial (rationality), proved here for both "
                     "instances via the exact three-leg Bass identity; FE: " +
                     both("fe")),
            citation=ihara + "; " + bass),
        "L7_TWIST_TENSOR_COMPAT": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("character-twist instance proved exactly: " +
                     cover["witness"] + " || CAVEAT (honesty): twists by "
                     "characters of covers are fully available (Artin-Ihara "
                     "theory), but no Rankin-Selberg-style tensor product of "
                     "two graph zetas is known to this build; the tensor "
                     "half of this cell rests on the twist instance only"),
            citation=stark_terras),
        "L8_REALIZATION": cell(
            "HOLDS", "PROVED_HERE",
            witness=("three realizations: spectral (adjacency operator; "
                     "exact charpolys and factorizations), dynamical/"
                     "combinatorial (non-backtracking edge shift: zeta = "
                     "1/det(I - uB) with B built explicitly; N_m = tr B^m "
                     "== independent DFS geodesic counts, m <= 12, both "
                     "graphs), and group-theoretic (Ihara's original p-adic "
                     "quotient setting, imported); the Bass identity tying "
                     "them together is instance-proved coefficient-wise"),
            citation=hashimoto + "; " + bass + "; " + kotani_sunada),
        "L9_EXPLICIT_FORMULA_POSITIVITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("explicit formula instance: N_m = tr(B^m) = power sums "
                     "of the inverse roots of det(I-uB) (= poles side), "
                     "verified exactly for m <= 12 on both graphs; the "
                     "positivity/purity input is supplied INDEPENDENTLY by "
                     "self-adjointness of the adjacency operator (A = A^T, "
                     "real spectrum - here even fully factored over Z) plus "
                     "the spectral gap certified by exact Sturm counting "
                     "(no roots of s2 in (8, B], in fact none in (9/2, B]); "
                     "this is precisely the mechanism slot that stands OPEN "
                     "in the zeta world"),
            citation=terras),
    }

    mechanisms = {
        "EULER_PRODUCT": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("supplied by unique factorization of closed geodesics "
                     "into powers of primitive classes; window-exact Euler "
                     "product check to degree 12 on both graphs (L2)"),
            citation=ihara),
        "DUALITY_FE": cell(
            "HOLDS", "PROVED_HERE",
            witness=("supplied by the u <-> 1/(qu) symmetry of each "
                     "quadratic local factor 1 - lambda u + q u^2; exact "
                     "reflection and cleared-denominator FE verified "
                     "coefficient-wise for both graphs, signs +1 / -1"),
            citation=terras),
        "TRACE_FORMULA": cell(
            "HOLDS", "PROVED_HERE",
            witness=("Ihara-Bass identity det(I-uB) = (1-u^2)^(r-1) "
                     "det(I-Au+qu^2) proved coefficient-wise for K4 (deg 12) "
                     "and Petersen (deg 30): LHS from the exact charpoly of "
                     "the explicitly built Hashimoto operator, RHS computed "
                     "twice (cofactor determinant over Q[u] and spectral "
                     "product); geodesic side anchored combinatorially: "
                     "tr(B^m) == pure-DFS geodesic counts, m <= 12 "
                     "(K4: N_3 = 24 = 4 triangles x 6, N_4 = 24; Petersen: "
                     "N_3 = N_4 = 0 (girth 5), N_5 = 120 = 12 pentagons x 10)"),
            citation=ihara + "; " + bass + "; " + hashimoto),
        "POSITIVITY_PURITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("supplied by adjacency-operator self-adjointness "
                     "(real spectrum) + spectral gap: the Ramanujan bound "
                     "lambda^2 <= 8 = 4q certified by exact Sturm counting "
                     "on s2 for both graphs; consequently every nontrivial "
                     "pole is pure: |u|^2 = 1/q exactly. " + both("ramanujan")),
            citation=lps + "; " + terras),
        "TENSOR_OPS": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("present in the form of character twists via Galois "
                     "covers (Artin-Ihara L-functions): exact double-cover "
                     "factorization instance for K4 embedded at L7; CAVEAT: "
                     "no tensor operation pairing two different graph zetas "
                     "is known to this build - the mechanism is partial"),
            citation=stark_terras),
        "FAMILY": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("K4 and Petersen sit in the family of cubic Ramanujan "
                     "graphs; infinite (q+1)-regular Ramanujan families "
                     "exist for q = p (Lubotzky-Phillips-Sarnak 1988; "
                     "Margulis 1988) and bipartite for all degrees "
                     "(Marcus-Spielman-Srivastava 2015); Alon-Boppana "
                     "(Nilli 1991) makes 2 sqrt(q) the sharp family-level "
                     "bound, so the Ramanujan certificate is extremal"),
            citation=(lps + "; G. Margulis (1988); A. Marcus, D. Spielman, "
                      "N. Srivastava (2015); N. Alon (1986); A. Nilli (1991)")),
    }

    critical_line = {
        "status": "THEOREM",
        "detail": ("Graph RH holds for both instances: every nontrivial pole "
                   "u_0 of zeta_G (root of det(I - Au + 2u^2) outside the "
                   "trivial factor (1-u)(1-2u)) satisfies |u_0|^2 = 1/2 "
                   "exactly, i.e. lies ON |u| = q^(-1/2); under u = q^(-s) "
                   "this is Re(s) = 1/2. Proved here: complete integer "
                   "factorization of both charpolys; for every nontrivial "
                   "lambda, disc = lambda^2 - 8 < 0 exactly, so the roots of "
                   "2u^2 - lambda u + 1 are a conjugate pair with product "
                   "1/2; plus the factorization-independent Sturm "
                   "certificate lambda^2 <= 8. Trivial poles u = 1, 1/2 "
                   "(|u|^2 = 1, 1/4) are off the circle (analogues of "
                   "s = 0, 1). The equivalence graph-RH <=> Ramanujan for "
                   "(q+1)-regular graphs is imported. This theorem is about "
                   "graph zetas only and implies nothing about the "
                   "classical RH."),
        "rigor": "PROVED_HERE",
        "citation": (ihara + "; " + hashimoto + "; T. Sunada (1986); " +
                     lps + "; " + terras),
        "witness": both("ramanujan") + " || " + both("purity"),
    }

    world = {
        "id": "ihara_ramanujan",
        "title": "Ihara zeta functions of two Ramanujan cubic graphs "
                 "(K4 and Petersen)",
        "definition": ("For a finite connected (q+1)-regular graph G, "
                       "zeta_G(u) = prod over equivalence classes [P] of "
                       "primitive closed backtrackless tailless cycles of "
                       "(1 - u^len(P))^-1, |u| small; equivalently "
                       "1/zeta_G(u) = det(I - uB) = (1-u^2)^(|E|-|V|) "
                       "det(I - Au + q u^2 I) (Ihara-Bass). Here G = K4 "
                       "(n=4, |E|=6) and the Petersen graph (n=10, |E|=15), "
                       "both cubic (q=2), with explicit integer adjacency "
                       "matrices."),
        "arithmetic_class": ("EXACT_RATIONAL combinatorial-spectral world: "
                             "Ihara zetas of finite 3-regular graphs (q=2); "
                             "a function-field-like setting where the "
                             "positivity/purity mechanism is independently "
                             "supplied (operator self-adjointness + "
                             "spectral gap)"),
        "ladder": ladder,
        "mechanisms": mechanisms,
        "critical_line": critical_line,
        "sources": [
            "Y. Ihara (1966), J. Math. Soc. Japan (discrete subgroups of "
            "PL(2) over p-adic fields; the graph zeta's origin)",
            "K. Hashimoto (1989), Adv. Stud. Pure Math. (edge operator, "
            "zeta functions of finite graphs)",
            "H. Bass (1992), Internat. J. Math. (Ihara-Selberg zeta of a "
            "tree lattice; three-term determinant identity)",
            "T. Sunada (1986), L-functions in geometry",
            "H. M. Stark, A. A. Terras (1996, 2000), Adv. Math. (graph "
            "zetas and coverings; Artin-Ihara L-functions)",
            "M. Kotani, T. Sunada (2000), J. Math. Sci. Univ. Tokyo",
            "A. Terras (2011), Zeta Functions of Graphs: A Stroll through "
            "the Garden, Cambridge Univ. Press",
            "A. Lubotzky, R. Phillips, P. Sarnak (1988), Combinatorica "
            "(Ramanujan graphs)",
            "G. Margulis (1988), explicit expander constructions",
            "N. Alon (1986); A. Nilli (1991) (Alon-Boppana bound)",
            "A. Marcus, D. Spielman, N. Srivastava (2015), Ann. of Math. "
            "(interlacing families I: bipartite Ramanujan graphs)",
        ],
        "rh_established": False,
        "notes": ("This world is the positive control for the mechanism "
                  "matrix: unlike the zeta world, the POSITIVITY_PURITY "
                  "slot is filled by an independently supplied structure "
                  "(self-adjointness of the adjacency operator + exactly "
                  "certified spectral gap), and the critical-line statement "
                  "is a THEOREM for these instances. Every HOLDS above "
                  "rests on Fraction-exact computation or an explicit "
                  "citation; the general Ihara-Bass theorem and the "
                  "geodesic Euler-product identity are imported, but both "
                  "are also instance-verified here (coefficient-wise / to "
                  "degree 12). Graph-RH theorems imply nothing about the "
                  "classical Riemann Hypothesis: rh_established = false."),
        "detector_runs": {
            "description": ("core.reconstruct.detect on coefficient "
                            "expansions of the quadratic local factors "
                            "1/(1 - lambda u + 2u^2), purity weight "
                            "(q, w) = (2, 1), window 12, holdout 4; the "
                            "trivial Perron factor lambda = 3 is a control "
                            "expected to be REFUSED at A4_PURITY "
                            "(disc = 1 > 0)"),
            "runs": detector_runs,
        },
    }
    return world


def main():
    k4 = analyze_graph("K4", k4_adjacency(), [(3, 1), (-1, 3)])
    pet = analyze_graph("Petersen", petersen_adjacency(),
                        [(3, 1), (1, 5), (-2, 4)])
    cover = double_cover_check(k4)
    detector_runs = run_detector()
    world = build_world(k4, pet, cover, detector_runs)
    probs = validate_world(world)
    assert not probs, probs
    path = save_world(world, "worlds")
    print("wrote", path)
    print("ladder:", {k: v["status"] for k, v in world["ladder"].items()})
    print("mechanisms:",
          {k: v["status"] for k, v in world["mechanisms"].items()})
    print("critical_line:", world["critical_line"]["status"])
    print("detector refusals:",
          [r["verdict"]["refusal"] for r in detector_runs])
    print("K4 1/zeta:", ipoly_str(k4["inv_zeta"]))
    print("Petersen 1/zeta:", ipoly_str(pet["inv_zeta"]))


if __name__ == "__main__":
    main()
