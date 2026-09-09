"""World 'ihara_nonramanujan': the Ihara zeta function of an EXACT
non-Ramanujan cubic graph -- the ablation witness that

    Euler product + functional equation + trace formula do NOT force
    the critical line.

Deterministic build script (no input, no randomness).  Run from pass root:

    python3 -m worlds.ihara_nonramanujan_build

regenerates worlds/ihara_nonramanujan.json identically.

PRIMARY OBJECT: the prism graph Y_16 = C_16 x K_2 (Cartesian product),
3-regular, 32 vertices, 48 edges; equivalently the Cayley graph of the
dihedral group D_16 (order 32) with connection set {r, r^-1, s} (verified
entrywise below).  Its Ihara zeta function is

    zeta(u)^-1 = (1 - u^2)^{m-n} det(I - A u + 2 u^2 I),   m-n = 16,

(Ihara/Hashimoto/Bass; q = 2 for a 3-regular graph).  SECONDARY OBJECT:
the smaller prism Y_9 (18 vertices), found by a deterministic exact sweep
over all prisms n = 3..15 -- the task's suggested n = 14 does NOT certify
(Y_14 is Ramanujan) while n = 15 does; the smallest certifying prism is
n = 9.

What is computed and PROVED here (Fraction / integer arithmetic ONLY; no
floating point anywhere in this file):

  1. Graph exactness: adjacency matrices built explicitly; 3-regularity,
     symmetry, zero diagonal, connectivity (BFS), girth 4 (via
     non-backtracking traces) all asserted; dihedral Cayley realization
     asserted entrywise from an explicit group multiplication table.
  2. Characteristic polynomial of A by TWO independent exact methods
     (Faddeev-LeVerrier, and Newton from exact integer traces of A^k),
     asserted equal, integer, degree 2n.
  3. TOTAL REALNESS of the spectrum proved by Sturm alone (no spectral
     theorem import): the squarefree part of char(A) has exactly
     deg-many distinct real roots in (-4, 4]; nothing above 3, nothing
     below -3 except the bipartite -3.
  4. NON-RAMANUJAN CERTIFICATE (exact, the headline): strip the trivial
     eigenvalues (+3, and -3 when bipartite), build the polynomial whose
     roots are the SQUARES of the remaining eigenvalues via power sums
     (Newton), take its squarefree part, check nonvanishing at 8 and 9,
     and Sturm-count roots in (8, 9]: count = 1 >= 1.  Hence there is a
     real eigenvalue lambda with 8 < lambda^2 < 9, i.e.
     2*sqrt(2) < |lambda| < 3: the Ramanujan bound |lambda| <= 2 sqrt(2)
     FAILS.  An 8-step exact bisection pins lambda^2 into a rational
     interval of width 1/256.
  5. BASS/IHARA DETERMINANT IDENTITY PROVED IN FULL for both graphs: the
     non-backtracking edge matrix B (2m x 2m, 0/1, two successors per
     directed edge) is built explicitly; tr(B^k) computed exactly for
     k = 1..2m; det(I - uB) is reconstructed from these power sums by
     Newton (a degree-2m polynomial with constant term 1 is DETERMINED
     by p_1..p_{2m}), and asserted coefficientwise equal to
     (1-u^2)^{m-n} det(I - Au + 2u^2 I).  The vertex determinant
     D(u) = det(I - Au + 2u^2 I) is itself computed by two independent
     exact routes (substitution u^{2n} char((1+2u^2)/u), and a
     Chebyshev-style trace recursion), asserted equal.
  6. FUNCTIONAL EQUATION PROVED EXACTLY as coefficient identities:
     (2u^2)^{2n} D(1/(2u)) = D(u), i.e. c_{deg-j} = 2^{deg/2-j} c_j; and
     for the completed Xi(u) = ((1-u^2)(1-4u^2))^{m-n} D(u) the same
     symmetry xi_{deg-j} = 2^{deg/2-j} xi_j (root number +1).  The map
     u -> 1/(2u) is s -> 1-s under u = 2^{-s}.
  7. EULER PRODUCT over primitive closed geodesics: pi_d (oriented
     primitive classes of length d) extracted from tr(B^k) by Moebius
     inversion, integrality and nonnegativity asserted, and the product
     prod_{d<=32} (1-u^d)^{-pi_d} asserted equal to the series of
     1/zeta^-1 through u^32 (exact binomial series).
  8. TWIST/TENSOR structure, exact: char(A_{Y16}) and D_{Y16} factor as
     the product of the two K_2-character branches (A_{C16} +- I), and
     as the Artin-Ihara factorization for the double cover Y_16 -> Y_8
     with the explicitly signed (voltage -1 on one cycle edge per layer)
     twisted adjacency: zeta_{Y16}^-1 = zeta_{Y8}^-1 * L(u,chi)^-1.
  9. CRITICAL LINE IS FALSE, with the exact translation: every pole of
     zeta_G is a root of some 1 - lambda u + 2u^2 (or of (1-u^2)); for
     the certified lambda with lambda^2 > 8 the two roots u0 are real and
     distinct with u+ u- = 1/2, and NEITHER has modulus 2^{-1/2}: a real
     root with |u0| = 2^{-1/2} would mean u0 = +-2^{-1/2} and
     0 = 2u0^2 - lambda u0 + 1 = 2 - (+-lambda) 2^{-1/2}, forcing
     lambda^2 = 8 -- contradicting lambda^2 > 8.  Since u+ != u- and
     |u+ u-| = 1/2 = (2^{-1/2})^2, exactly one root lies strictly inside
     and one strictly outside |u| = 2^{-1/2}: under u = 2^{-s} the graph
     has poles with Re(s) != 1/2.
 10. Detector runs (core.reconstruct.detect) on exact coefficient data:
     the necessary-only purity branch of the detector PASSES on 1/D
     (self-reciprocity = FE holds!) although purity is FALSE -- an
     honest display that FE-type symmetry does not see the violation --
     while on the full zeta^-1 the detector REFUSES at A4 (defect from
     the (1-u^2)^{m-n} factor).  Both annotated.

Nothing here bears on RH over Q; the world is an ABLATION CONTROL: the
mechanisms EULER_PRODUCT, DUALITY_FE, TRACE_FORMULA all HOLD exactly,
yet POSITIVITY_PURITY FAILS and the critical line is FALSE.
rh_established = false.
"""

from fractions import Fraction
from math import comb

from core.exact import (
    F,
    poly_mul,
    poly_divmod,
    poly_eval,
    poly_trim,
    poly_deriv,
    poly_scale,
    charpoly_of_matrix,
    charpoly_from_power_sums,
    satake_poly_from_power_sums,
    power_sums_from_satake,
    coefficient_sequence_from_satake,
    series_of_rational,
    count_real_roots_in,
    is_integer_poly,
)
from core.reconstruct import detect
from core.worlds import cell, validate_world, save_world

# ---------------------------------------------------------------------------
# Fixed data of the world (all literals; no randomness anywhere)
# ---------------------------------------------------------------------------
NCYC_MAIN = 16          # primary prism: Y_16, 32 vertices
NCYC_SMALL = 9          # smallest certifying prism found by the sweep below
SWEEP_RANGE = range(3, 16)   # deterministic sweep over prisms n = 3..15
Q_GRAPH = 2             # q = degree - 1 for a 3-regular graph
K_EULER = 32            # Euler-product window in powers of u
BISECT_STEPS = 8        # exact bisection refinement of the certificate


def fmt(p):
    return "[" + ", ".join(str(F(c)) for c in p) + "]"


# ---------------------------------------------------------------------------
# Section 1: graphs, exactly
# ---------------------------------------------------------------------------

def idx(i, j, n):
    """Vertex index of (i mod n, j) in the prism Y_n; j in {0,1}."""
    return 2 * (i % n) + j


def prism_adjacency(n):
    """Adjacency matrix of Y_n = C_n x K_2: vertex (i,j) is adjacent to
    (i+-1, j) (cycle edges) and (i, 1-j) (rung).  3-regular, 2n vertices."""
    NV = 2 * n
    A = [[0] * NV for _ in range(NV)]
    for i in range(n):
        for j in (0, 1):
            v = idx(i, j, n)
            for w in (idx(i + 1, j, n), idx(i - 1, j, n), idx(i, 1 - j, n)):
                A[v][w] = 1
    return A


def cayley_dihedral(n):
    """Cayley graph of the dihedral group D_n = <r, s | r^n, s^2, (rs)^2>
    (order 2n) with symmetric connection set S = {r, r^-1, s}, built from
    the explicit multiplication rule (r^i s^e)(r^j s^d) =
    r^{i + (-1)^e j} s^{e+d}.  Indexed by v(r^i s^e) = 2i + e."""
    NV = 2 * n

    def mul(g, h):
        i, e = g
        j, d = h
        return ((i + j) % n if e == 0 else (i - j) % n, (e + d) % 2)

    S = [(1, 0), (n - 1, 0), (0, 1)]
    A = [[0] * NV for _ in range(NV)]
    for i in range(n):
        for e in (0, 1):
            for x in S:
                w = mul((i, e), x)
                A[2 * i + e][2 * w[0] + w[1]] += 1
    return A


def graph_sanity(A):
    """Exact structural checks: symmetric 0/1 matrix, zero diagonal,
    3-regular, connected (BFS).  Returns number of vertices."""
    NV = len(A)
    for i in range(NV):
        assert A[i][i] == 0, "loop found"
        assert sum(A[i]) == 3, "not 3-regular"
        for j in range(NV):
            assert A[i][j] in (0, 1) and A[i][j] == A[j][i]
    seen = {0}
    frontier = [0]
    while frontier:
        v = frontier.pop()
        for w in range(NV):
            if A[v][w] and w not in seen:
                seen.add(w)
                frontier.append(w)
    assert len(seen) == NV, "not connected"
    return NV


def traces_of_matrix(A, K):
    """tr(A^k) for k = 1..K, exact integer arithmetic (dense but skipping
    zero entries of A, which is sparse)."""
    NV = len(A)
    P = [row[:] for row in A]
    out = [sum(P[i][i] for i in range(NV))]
    for _ in range(K - 1):
        P = [[sum(A[i][t] * P[t][j] for t in range(NV) if A[i][t])
              for j in range(NV)] for i in range(NV)]
        out.append(sum(P[i][i] for i in range(NV)))
    return out


def charpoly_from_traces(A):
    """Monic char poly of A via Newton's identities from exact traces --
    an exact method independent of Faddeev-LeVerrier."""
    NV = len(A)
    return charpoly_from_power_sums([F(x) for x in traces_of_matrix(A, NV)],
                                    NV)


# ---------------------------------------------------------------------------
# Section 2: exact spectral certificates (Sturm only; no spectral theorem)
# ---------------------------------------------------------------------------

def pgcd(a, b):
    """Monic gcd in Q[T] by the Euclidean algorithm (exact Fractions)."""
    a = poly_trim(a)
    b = poly_trim(b)
    while b:
        _, r = poly_divmod(a, b)
        a, b = b, poly_trim(r)
    return [c / a[-1] for c in a] if a else a


def squarefree_part(p):
    """p / gcd(p, p'): same distinct roots, all simple.  Exact."""
    g = pgcd(p, poly_deriv(p))
    q, r = poly_divmod(p, g)
    assert r == [], "squarefree division not exact"
    return q


def strip_trivial(phi):
    """Divide out the trivial eigenvalue +3 (Perron root; simplicity is
    asserted, not imported) and, when the graph is bipartite, -3.
    Returns (psi, list_of_stripped_labels)."""
    psi, r = poly_divmod(phi, [F(-3), F(1)])          # divide by (T - 3)
    assert r == [], "+3 is not an eigenvalue?!"
    stripped = ["+3"]
    if poly_eval(psi, -3) == 0:
        psi, r = poly_divmod(psi, [F(3), F(1)])       # divide by (T + 3)
        assert r == []
        stripped.append("-3")
    assert poly_eval(psi, 3) != 0, "+3 not simple"
    assert poly_eval(psi, -3) != 0, "-3 not simple"
    return psi, stripped


def squared_roots_poly(psi):
    """Monic polynomial whose roots are the SQUARES of the roots of the
    monic polynomial psi, via power sums: p_k({mu^2}) = p_{2k}({mu}),
    then Newton.  Exact over Q; degree preserved."""
    d = len(psi) - 1
    sigma = list(reversed(psi))                 # u^d psi(1/u): det(1 - mu u)
    assert sigma[0] == 1                        # psi is monic
    p = power_sums_from_satake(sigma, 2 * d)
    even = [p[2 * k - 1] for k in range(1, d + 1)]
    return charpoly_from_power_sums(even, d)


def realness_certificate(phi, bipartite):
    """Prove BY STURM ALONE that every root of phi is real, lies in
    (-4, 4], that no root exceeds 3, and that no root is below -3
    (except -3 itself in the bipartite case).  Uses the squarefree part
    so that 'count == degree' accounts for every distinct root."""
    sf = squarefree_part(phi)
    d = len(sf) - 1
    assert count_real_roots_in(sf, -4, 4) == d, \
        "spectrum not certified totally real"
    assert count_real_roots_in(sf, 3, 4) == 0, "root above 3?!"
    below = count_real_roots_in(sf, -4, -3)
    assert below == (1 if bipartite else 0), "root below -3?!"
    return d


def nonramanujan_certificate(A, n):
    """The exact non-Ramanujan certificate for the prism Y_n.  Returns a
    dict of exact data (all integers / Fractions / strings)."""
    phi = charpoly_from_traces(A)
    assert is_integer_poly(phi)
    psi, stripped = strip_trivial(phi)
    bipartite = ("-3" in stripped)
    assert bipartite == (n % 2 == 0)            # prism bipartite iff n even
    realness_certificate(phi, bipartite)

    sq = squared_roots_poly(psi)                # roots = lambda^2, nontrivial
    assert is_integer_poly(sq)
    sf = squarefree_part(sq)
    # endpoints must not be roots, so (8, 9] counting is open-interval exact
    v8, v9 = poly_eval(sq, 8), poly_eval(sq, 9)
    assert v8 != 0 and v9 != 0
    assert poly_eval(sf, 8) != 0 and poly_eval(sf, 9) != 0
    cnt = count_real_roots_in(sf, 8, 9)
    # nothing hides in [9, 10]: all nontrivial lambda^2 < 9 (realness cert
    # bounds |lambda| < 3 after stripping), re-checked directly:
    assert count_real_roots_in(sf, 8, 10) == cnt
    # sanity: every distinct squared eigenvalue is real in (-1, 9]
    assert count_real_roots_in(sf, -1, 9) == len(sf) - 1

    interval = None
    if cnt >= 1:
        # deterministic exact bisection: pin ONE root of sf in (8,9) into a
        # dyadic rational interval of width 2^-BISECT_STEPS
        lo, hi = F(8), F(9)
        for _ in range(BISECT_STEPS):
            mid = (lo + hi) / 2
            assert poly_eval(sf, mid) != 0
            if count_real_roots_in(sf, lo, mid) >= 1:
                hi = mid
            else:
                lo = mid
        assert count_real_roots_in(sf, lo, hi) >= 1
        interval = (lo, hi)
    return {"phi": phi, "psi": psi, "stripped": stripped, "sq": sq,
            "sf": sf, "sq_at_8": v8, "sq_at_9": v9, "count_8_9": cnt,
            "interval": interval, "bipartite": bipartite}


# ---------------------------------------------------------------------------
# Section 3: Ihara zeta -- Bass identity proved in full
# ---------------------------------------------------------------------------

def detpoly_from_phi(phi):
    """D(u) = det(I - A u + 2 u^2 I) from char(A), via the exact polynomial
    identity det((1+2u^2) I - u A) = u^{NV} char((1+2u^2)/u)
            = sum_j char_j (1+2u^2)^j u^{NV-j}."""
    NV = len(phi) - 1
    s = [F(1), F(0), F(2)]                      # 1 + 2u^2
    D = []
    spow = [F(1)]
    for j in range(NV + 1):
        term = [F(0)] * (NV - j) + poly_scale(spow, phi[j])
        D = [(D[k] if k < len(D) else F(0)) +
             (term[k] if k < len(term) else F(0))
             for k in range(max(len(D), len(term)))]
        spow = poly_mul(spow, s)
    return poly_trim(D)


def detpoly_via_chebyshev(A):
    """Independent route to D(u): its inverse roots are, for each
    eigenvalue lambda, the pair alpha, beta with alpha+beta = lambda and
    alpha beta = 2; so p_k(D) = sum_lambda t_k(lambda) where t_0 = 2,
    t_1 = lambda, t_k = lambda t_{k-1} - 2 t_{k-2} (integer coefficient
    polynomials in lambda), evaluated on traces of A.  Newton then
    reconstructs D.  Exact."""
    NV = len(A)
    s = [NV] + traces_of_matrix(A, 2 * NV)      # s[j] = tr(A^j), s[0] = NV
    tprev, tcur = [2], [0, 1]
    P = []
    for k in range(1, 2 * NV + 1):
        if k > 1:
            tk = [0] + tcur
            for i, c in enumerate(tprev):
                tk[i] -= 2 * c
            tprev, tcur = tcur, tk
        P.append(sum(c * s[j] for j, c in enumerate(tcur)))
    return satake_poly_from_power_sums([F(x) for x in P], 2 * NV)


def directed_edges(n):
    """The 2m directed edges of Y_n in a fixed deterministic order."""
    edges = []
    for i in range(n):
        for j in (0, 1):
            v = idx(i, j, n)
            edges.append((v, idx(i + 1, j, n)))
            edges.append((idx(i + 1, j, n), v))
            if j == 0:
                edges.append((v, idx(i, 1, n)))
                edges.append((idx(i, 1, n), v))
    return edges


def nonbacktracking_traces(A, n, K):
    """tr(B^k), k = 1..K, for the Hashimoto non-backtracking edge matrix B
    of Y_n: B[(a,b)][(c,d)] = 1 iff b == c and (c,d) != (b,a).  Each
    directed edge has exactly q = 2 successors (3-regular), so B-powers
    are computed by exact sparse row sums.  tr(B^k) = number of closed
    non-backtracking TAILLESS paths of length k with a marked starting
    edge (the wrap-around step e_k -> e_1 is also non-backtracking)."""
    edges = directed_edges(n)
    m2 = len(edges)
    eid = {e: k for k, e in enumerate(edges)}
    succ = []
    for (a, b) in edges:
        ss = [eid[(b, c)] for c in range(2 * n) if A[b][c] and c != a]
        assert len(ss) == Q_GRAPH
        succ.append(ss)
    P = [[0] * m2 for _ in range(m2)]           # P = B^1
    for e, ss in enumerate(succ):
        for f in ss:
            P[e][f] = 1
    out = [sum(P[e][e] for e in range(m2))]
    for _ in range(K - 1):
        P = [[x + y for x, y in zip(P[succ[e][0]], P[succ[e][1]])]
             for e in range(m2)]                # P <- B P, sparse row sums
        out.append(sum(P[e][e] for e in range(m2)))
    return out


def poly_power(p, k):
    out = [F(1)]
    for _ in range(k):
        out = poly_mul(out, p)
    return out


def bass_identity_proof(A, n):
    """FULL exact proof of the Bass/Ihara three-term determinant identity
    for Y_n:  det(I - uB) == (1-u^2)^{m-n} det(I - Au + 2u^2 I).

    Both sides are degree-2m polynomials with constant term 1.  The left
    side is DETERMINED by its inverse-root power sums p_1..p_{2m} =
    tr(B^k) (Newton); we compute those exactly and reconstruct.  The
    right side is computed from char(A) by two independent exact routes.
    Equality is asserted coefficientwise.  Returns (D, R, N, phi)."""
    NV = 2 * n
    m_minus_n = n                               # m = 3n edges, 2n vertices
    phi = charpoly_from_traces(A)
    phiFL = charpoly_of_matrix(A)               # independent exact method
    assert phi == phiFL, "charpoly methods disagree"
    D = detpoly_from_phi(phi)
    assert D == detpoly_via_chebyshev(A), "D routes disagree"
    assert is_integer_poly(D) and D[0] == 1 and len(D) - 1 == 2 * NV
    assert D[-1] == F(2) ** NV                  # leading coefficient 2^NV

    R = poly_mul(poly_power([F(1), F(0), F(-1)], m_minus_n), D)
    assert len(R) - 1 == 2 * (3 * n) and R[0] == 1 and is_integer_poly(R)

    N = nonbacktracking_traces(A, n, len(R) - 1)
    # power sums of R's inverse roots must equal tr(B^k), k = 1..2m ...
    assert power_sums_from_satake(R, len(R) - 1) == [F(x) for x in N]
    # ... and Newton reconstruction from tr(B^k) must return R exactly:
    assert satake_poly_from_power_sums([F(x) for x in N], len(R) - 1) == R
    return D, R, N, phi


def functional_equation_proof(D, m_minus_n):
    """Exact FE identities.  D-level: c_{deg-j} = 2^{deg/2 - j} c_j, i.e.
    (2u^2)^{NV} D(1/(2u)) = D(u).  Xi-level: same symmetry for
    Xi = ((1-u^2)(1-4u^2))^{m-n} D (root number +1)."""
    deg = len(D) - 1
    for j in range(deg + 1):
        assert D[deg - j] == F(2) ** (deg // 2 - j) * D[j], ("D FE", j)
    gam = poly_mul([F(1), F(0), F(-1)], [F(1), F(0), F(-4)])
    Xi = poly_mul(poly_power(gam, m_minus_n), D)
    degx = len(Xi) - 1
    for j in range(degx + 1):
        assert Xi[degx - j] == F(2) ** (degx // 2 - j) * Xi[j], ("Xi FE", j)
    return degx


def mobius(d):
    out, x, p = 1, d, 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            if x % p == 0:
                return 0
            out = -out
        p += 1
    if x > 1:
        out = -out
    return out


def euler_product_window(R, N, K):
    """Primitive oriented geodesic classes pi_d by Moebius inversion of
    N_k = tr(B^k) = sum_{d|k} d pi_d (unique primitive decomposition of a
    marked closed geodesic); integrality/nonnegativity asserted; then the
    Euler product prod_{d<=K} (1-u^d)^{-pi_d} is asserted equal to the
    coefficient series of zeta = 1/R through u^K (binomial series,
    Fractions)."""
    pi = {}
    for d in range(1, K + 1):
        s = sum(mobius(d // e) * N[e - 1] for e in range(1, d + 1)
                if d % e == 0)
        assert s % d == 0, "pi_d not integral"
        pi[d] = s // d
        assert pi[d] >= 0, "pi_d negative"
    prod = [F(1)] + [F(0)] * K
    for d in range(1, K + 1):
        if pi[d] == 0:
            continue
        factor = [F(0)] * (K + 1)
        j = 0
        while d * j <= K:
            factor[d * j] = F(comb(pi[d] - 1 + j, j))
            j += 1
        prod = poly_mul(prod, factor)[:K + 1]
        prod += [F(0)] * (K + 1 - len(prod))
    zser = series_of_rational([F(1)], R, K + 1)
    assert prod == zser, "Euler product window mismatch"
    return pi


# ---------------------------------------------------------------------------
# Section 4: tensor / twist structure, exact factorizations
# ---------------------------------------------------------------------------

def cycle_adjacency(n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        C[i][(i + 1) % n] = 1
        C[i][(i - 1) % n] = 1
    return C


def factorization_checks(phi16, D16):
    """(a) K_2-character factorization: A(Y_16) = A(C_16) (+) A(K_2)
    (Cartesian), so char and D factor over the two K_2 characters
    eps = +-1 via the branches A(C_16) +- I.  (b) Artin-Ihara
    factorization for the double cover Y_16 -> Y_8: voltage -1 on one
    cycle edge per layer gives the signed twisted adjacency A_chi with
    char(A_16) = char(A_8) char(A_chi) and D_16 = D_8 D_chi, i.e.
    zeta_{Y16}^-1 = zeta_{Y8}^-1 L(u,chi)^-1 (the (1-u^2) exponents add:
    16 = 8 + 8).  All asserted exactly."""
    C16 = cycle_adjacency(16)
    Cp = [[C16[i][j] + (1 if i == j else 0) for j in range(16)]
          for i in range(16)]
    Cm = [[C16[i][j] - (1 if i == j else 0) for j in range(16)]
          for i in range(16)]
    php, phm = charpoly_of_matrix(Cp), charpoly_of_matrix(Cm)
    assert poly_mul(php, phm) == phi16
    assert poly_mul(detpoly_from_phi(php), detpoly_from_phi(phm)) == D16

    A8 = prism_adjacency(8)
    graph_sanity(A8)
    Achi = [row[:] for row in A8]
    for j in (0, 1):
        v1, v2 = idx(7, j, 8), idx(0, j, 8)
        Achi[v1][v2] = -1
        Achi[v2][v1] = -1
    phi8, phichi = charpoly_of_matrix(A8), charpoly_of_matrix(Achi)
    assert poly_mul(phi8, phichi) == phi16
    D8, Dchi = detpoly_from_phi(phi8), detpoly_from_phi(phichi)
    assert poly_mul(D8, Dchi) == D16
    return phichi


# ---------------------------------------------------------------------------
# Section 5: witness builders
# ---------------------------------------------------------------------------

# Exact expected values (pinned; every one re-computed and asserted above)
PHI16 = [9, 0, -496, 0, 10360, 0, -105968, 0, 597700, 0, -1998992, 0,
         4212216, 0, -5829200, 0, 5429854, 0, -3446544, 0, 1497000, 0,
         -444304, 0, 89300, 0, -11888, 0, 1000, 0, -48, 0, 1]
SF16 = [-1, 27, -181, 391, -343, 125, -19, 1]
PHI9 = [0, 0, 108, -36, -945, 144, 3081, -108, -4662, -4, 3564, 0, -1395,
        0, 279, 0, -27, 0, 1]
SF9 = [0, 36, -333, 1161, -1966, 1748, -823, 199, -23, 1]
N16_PREFIX = [0, 0, 0, 128, 0, 192, 0, 640, 0, 2880, 0, 9152]
N9_PREFIX = [0, 0, 0, 72, 0, 108, 0, 360, 36, 1620, 1584, 5148]
SWEEP_EXPECT = {3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1, 10: 0, 11: 1,
                12: 0, 13: 1, 14: 0, 15: 1}
INT16 = (Fraction(519, 64), Fraction(2077, 256))
INT9 = (Fraction(1061, 128), Fraction(2123, 256))

TWO_LINE_ARGUMENT = (
    "TWO-LINE EXACT ARGUMENT that the certified eigenvalue forces "
    "off-critical poles: the poles of zeta_G attached to lambda are the "
    "roots u0 of 1 - lambda u + 2u^2.  (1) For real lambda with "
    "lambda^2 > 8 the discriminant lambda^2 - 8 is > 0, so the two roots "
    "are real and distinct, with product u+ u- = 1/2.  (2) If a real root "
    "had |u0| = 1/sqrt(2) then u0 = +-2^(-1/2), and 0 = 2u0^2 - lambda u0 "
    "+ 1 = 2 -+ lambda 2^(-1/2) forces lambda = +-2 sqrt(2), i.e. "
    "lambda^2 = 8, contradicting lambda^2 > 8.  Hence neither root has "
    "modulus 1/sqrt(2); since they are distinct real numbers with "
    "|u+ u-| = 1/2 = (2^(-1/2))^2, exactly one lies strictly inside and "
    "one strictly outside the critical circle |u| = 2^(-1/2).  Under "
    "u = 2^(-s) these are poles with Re(s) != 1/2.")


def build_certificates():
    """Primary (Y_16) and secondary (Y_9) non-Ramanujan certificates plus
    the deterministic sweep over all prisms n = 3..15."""
    W = {}

    # --- primary Y_16
    A16 = prism_adjacency(NCYC_MAIN)
    assert graph_sanity(A16) == 32
    assert cayley_dihedral(NCYC_MAIN) == A16    # Cayley realization, exact
    c16 = nonramanujan_certificate(A16, NCYC_MAIN)
    assert c16["phi"] == [F(x) for x in PHI16]
    assert c16["stripped"] == ["+3", "-3"] and c16["bipartite"]
    assert c16["sf"] == [F(x) for x in SF16]
    assert c16["count_8_9"] == 1
    assert c16["sq_at_8"] == 9074667075536209
    assert c16["sq_at_9"] == 3651732441147117666304
    assert c16["interval"] == INT16
    W["nonram16"] = (
        "EXACT NON-RAMANUJAN CERTIFICATE for Y_16 = C_16 x K_2 (32 "
        "vertices, 3-regular, bipartite): char(A) = " + fmt(c16["phi"]) +
        " (degree 32, computed by BOTH Faddeev-LeVerrier and Newton-from-"
        "traces, equal).  Trivial eigenvalues +3, -3 stripped exactly "
        "(simple: psi(+-3) != 0).  The degree-30 polynomial of SQUARED "
        "nontrivial eigenvalues (power sums p_{2k} + Newton) has "
        "squarefree part " + fmt(c16["sf"]) + "; its values at the "
        "endpoints are sq(8) = 9074667075536209 != 0 and sq(9) = "
        "3651732441147117666304 != 0, and the EXACT Sturm count of roots "
        "in (8, 9] is 1 (also 1 in (8, 10]: nothing hides in [9,10]).  "
        "Hence some real eigenvalue lambda has 8 < lambda^2 < 9, i.e. "
        "2 sqrt(2) < |lambda| < 3: the Ramanujan bound FAILS.  (A root of "
        "the squared-roots polynomial in (8,9) is automatically the "
        "square of a REAL root: mu^2 real positive forces mu real; total "
        "realness of spec(A) is ALSO proved by Sturm: the squarefree "
        "char poly has exactly deg-many distinct real roots in (-4,4], "
        "none in (3,4], and only -3 in (-4,-3].)  8-step exact bisection "
        "pins lambda^2 into (519/64, 2077/256] (width 1/256).")

    # --- sweep over prisms n = 3..15 (deterministic; includes the task's
    #     suggested n = 14 and n = 15)
    sweep = []
    smallest = None
    for n in SWEEP_RANGE:
        An = prism_adjacency(n)
        graph_sanity(An)
        cn = nonramanujan_certificate(An, n)
        assert cn["count_8_9"] == SWEEP_EXPECT[n], (n, cn["count_8_9"])
        sweep.append({"n": n, "vertices": 2 * n,
                      "stripped": cn["stripped"],
                      "sturm_count_sq_in_(8,9]": cn["count_8_9"],
                      "verdict": ("NON-RAMANUJAN (certified)"
                                  if cn["count_8_9"] else
                                  "Ramanujan (certified: no squared "
                                  "nontrivial eigenvalue in (8,10])"),
                      "lambda_sq_interval":
                          (str(cn["interval"][0]) + " < lambda^2 <= " +
                           str(cn["interval"][1])) if cn["interval"]
                          else None})
        if cn["count_8_9"] and smallest is None:
            smallest = n
    assert smallest == NCYC_SMALL == 9
    W["sweep"] = (
        "DETERMINISTIC EXACT SWEEP over all prisms Y_n, n = 3..15 (same "
        "Sturm certificate pipeline as Y_16, both directions certified): "
        "NON-Ramanujan for n = 9, 11, 13, 15 (count in (8,9] equals 1); "
        "Ramanujan for n = 3..8, 10, 12, 14 (count in (8,10] equals 0).  "
        "In particular the task's candidate n = 14 (28 vertices) does NOT "
        "certify -- Y_14 is Ramanujan -- while n = 15 (30 vertices) "
        "does.  The smallest certifying prism is n = 9 (18 vertices), "
        "kept as the second certified example.  (Search restricted to "
        "the prism family; smaller non-prism cubic non-Ramanujan graphs "
        "were not searched for.)")

    # --- secondary Y_9
    A9 = prism_adjacency(NCYC_SMALL)
    assert graph_sanity(A9) == 18
    assert cayley_dihedral(NCYC_SMALL) == A9
    c9 = nonramanujan_certificate(A9, NCYC_SMALL)
    assert c9["phi"] == [F(x) for x in PHI9]
    assert c9["stripped"] == ["+3"] and not c9["bipartite"]
    assert c9["sf"] == [F(x) for x in SF9]
    assert c9["count_8_9"] == 1
    assert c9["sq_at_8"] == 10442693632
    assert c9["sq_at_9"] == 1065245272200
    assert c9["interval"] == INT9
    W["nonram9"] = (
        "SECOND CERTIFIED EXAMPLE, SMALLER: Y_9 = C_9 x K_2 (18 vertices, "
        "3-regular, non-bipartite): char(A) = " + fmt(c9["phi"]) + "; "
        "only +3 stripped (odd prism, -3 not an eigenvalue); squared-"
        "roots polynomial (degree 17) has squarefree part " +
        fmt(c9["sf"]) + " with sq(8) = 10442693632 != 0, sq(9) = "
        "1065245272200 != 0, and Sturm count 1 in (8, 9] (and in (8, "
        "10]).  Certified interval: 1061/128 < lambda^2 <= 2123/256 "
        "(the violating eigenvalue is lambda = -(1 + 2 cos(pi/9)) "
        "numerically, but ONLY the exact Sturm data is used).")

    return W, A16, A9, c16, c9, sweep


def build_zeta_witnesses(W, A16, A9):
    """Bass identity (full proof), FE, Euler product, factorizations."""
    D16, R16, N16, phi16 = bass_identity_proof(A16, NCYC_MAIN)
    assert N16[:12] == N16_PREFIX
    assert next(k + 1 for k, x in enumerate(N16) if x) == 4  # girth 4
    W["bass16"] = (
        "BASS/IHARA DETERMINANT IDENTITY PROVED IN FULL for Y_16: the "
        "96 x 96 non-backtracking edge matrix B was built explicitly "
        "(each directed edge has exactly q = 2 successors); tr(B^k) "
        "computed exactly for k = 1..96 (first twelve: " +
        str(N16_PREFIX) + "; girth 4).  det(I - uB) is a degree-96 "
        "polynomial with constant term 1, hence DETERMINED by these 96 "
        "power sums via Newton; the reconstruction equals "
        "(1-u^2)^16 * det(I - Au + 2u^2 I) COEFFICIENTWISE.  D(u) = "
        "det(I - Au + 2u^2 I) itself was computed by two independent "
        "exact routes (substitution u^32 char((1+2u^2)/u), and the "
        "Chebyshev-style trace recursion t_k = lambda t_{k-1} - 2 "
        "t_{k-2}), equal; deg D = 64, D(0) = 1, leading coefficient "
        "2^32 = 4294967296.  So zeta^-1 = (1-u^2)^16 D(u), degree 96: "
        "rationality of zeta is PROVED, not imported, for this graph.")

    degx16 = functional_equation_proof(D16, NCYC_MAIN)
    assert degx16 == 128
    W["fe16"] = (
        "FUNCTIONAL EQUATION PROVED EXACTLY (coefficient identities in "
        "Z): (2u^2)^32 D(1/(2u)) = D(u), i.e. c_{64-j} = 2^{32-j} c_j "
        "for all j; and for the completed Xi(u) = ((1-u^2)(1-4u^2))^16 "
        "D(u) (degree 128), xi_{128-j} = 2^{64-j} xi_j for all j -- "
        "symmetric under u -> 1/(2u), which is s -> 1-s under u = "
        "2^(-s); root number +1 (midpoint identity is trivially "
        "consistent).  The completion by (1-u^2)(1-4u^2) factors "
        "(vanishing at u = +-1, +-1/2, the s = 0 and s = 1 points) is "
        "one member of the standard family of graph FEs.")

    pi16 = euler_product_window(R16, N16, K_EULER)
    W["euler16"] = (
        "EULER PRODUCT over primitive closed geodesics, exact window "
        "u^32: oriented primitive class counts pi_d from Moebius "
        "inversion of N_k = tr(B^k) = sum_{d|k} d pi_d (every marked "
        "closed geodesic is a unique power of a primitive one); all "
        "pi_d integral and >= 0; pi_1 = pi_2 = pi_3 = 0, pi_4 = 32, "
        "pi_6 = 32, pi_8 = 64, pi_10 = 288, pi_12 = 736; the product "
        "prod_{d<=32} (1-u^d)^(-pi_d) equals the coefficient series of "
        "1/[(1-u^2)^16 D(u)] through u^32 EXACTLY (binomial series in "
        "Fractions).")
    assert (pi16[4], pi16[6], pi16[8], pi16[10], pi16[12]) == \
        (32, 32, 64, 288, 736)

    phichi = factorization_checks(phi16, D16)
    W["factor16"] = (
        "EXACT TWIST/TENSOR FACTORIZATIONS: (a) K_2-character branches: "
        "char(A(Y_16)) = char(A(C_16)+I) * char(A(C_16)-I) and D_{Y16} "
        "= D_+ * D_- (Cartesian-product spectral splitting along the "
        "two characters of the K_2 factor), asserted coefficientwise.  "
        "(b) ARTIN-IHARA for the double cover Y_16 -> Y_8: with voltage "
        "-1 on one cycle edge per layer, the signed twisted adjacency "
        "A_chi = " + "char " + fmt(phichi) + " satisfies char(A_16) = "
        "char(A_8) char(A_chi) and D_16 = D_8 D_chi, i.e. zeta_{Y16}^-1 "
        "= zeta_{Y8}^-1 * L(u,chi)^-1 with the (1-u^2) exponents adding "
        "as 16 = 8 + 8.  Both proved exactly.")

    D9, R9, N9, _ = bass_identity_proof(A9, NCYC_SMALL)
    assert N9[:12] == N9_PREFIX
    degx9 = functional_equation_proof(D9, NCYC_SMALL)
    assert degx9 == 72
    pi9 = euler_product_window(R9, N9, 24)
    assert (pi9[4], pi9[6], pi9[8], pi9[9], pi9[10], pi9[11]) == \
        (18, 18, 36, 4, 162, 144)
    W["bass9"] = (
        "The same FULL proofs for Y_9: tr(B^k) for k = 1..54 on the "
        "54 x 54 edge matrix (first twelve: " + str(N9_PREFIX) + "); "
        "Newton reconstruction equals (1-u^2)^9 D_9(u) coefficientwise "
        "(deg D_9 = 36, leading 2^18); FE identities at D- and Xi-level "
        "(deg Xi = 72); Euler product window u^24 with pi_4 = 18, pi_6 "
        "= 18, pi_8 = 36, pi_9 = 4 (the two 9-cycles, one per layer, in "
        "two orientations each), pi_10 = 162, pi_11 = 144: all exact.")
    return W, D16, R16, D9, R9


# ---------------------------------------------------------------------------
# Section 6: detector runs (honestly annotated)
# ---------------------------------------------------------------------------

def run_detector(D16, R16, D9):
    runs = []

    def cells_of(d):
        return {c["axiom"]: (c["status"], c["rigor"]) for c in d["cells"]}

    # run A: spectral determinant of Y_16, weight (2,1)
    vA = detect(coefficient_sequence_from_satake(D16, 136),
                mode="coefficients", weight=(2, 1), holdout=4).as_dict()
    ca = cells_of(vA)
    assert vA["refusal"] is None
    assert ca["A1_FINITE_RANK"] == ("HOLDS", "EXACT_RATIONAL")
    assert ca["A2_EFFECTIVITY"] == ("HOLDS", "EXACT_RATIONAL")
    assert ca["A3_INTEGRALITY"] == ("HOLDS", "EXACT_RATIONAL")
    assert ca["A4_PURITY"] == ("HOLDS", "NECESSARY_ONLY")
    assert ca["A5_HELD_OUT"] == ("HOLDS", "EXACT_RATIONAL")
    assert vA["object"]["degree"] == 64
    runs.append({
        "name": "Y16_spectral_determinant_weight_(2,1)",
        "weight": [2, 1], "mode": "coefficients",
        "series": "coefficients of 1/D(u), D = det(I - Au + 2u^2 I) of "
                  "Y_16, window 136, holdout 4",
        "verdict": vA,
        "annotation": (
            "HONEST ANNOTATION -- THE ABLATION LESSON IN MINIATURE: A4 "
            "reports HOLDS with rigor NECESSARY_ONLY because for degree "
            "64 the detector can only test self-reciprocity under a -> "
            "q^w/a = 2/a, and self-reciprocity HOLDS (it is exactly the "
            "functional equation, proved in this build).  Yet purity is "
            "FALSE: this world's Sturm certificate exhibits an inverse-"
            "root pair off |a| = sqrt(2).  The detector's necessary "
            "conditions cannot see the violation: FE-type symmetry does "
            "NOT imply purity.  The detector is NOT evidence for purity "
            "here and is recorded only to demonstrate that gap.")})

    # run B: full zeta^-1 of Y_16, weight (2,1) -- REFUSES at A4
    vB = detect(coefficient_sequence_from_satake(R16, 202),
                mode="coefficients", weight=(2, 1), holdout=4).as_dict()
    cb = cells_of(vB)
    assert vB["refusal"] == "A4_PURITY"
    assert cb["A4_PURITY"] == ("FAILS", "EXACT_RATIONAL")
    assert cb["A1_FINITE_RANK"][0] == "HOLDS"
    assert cb["A5_HELD_OUT"][0] == "HOLDS"
    assert vB["object"]["degree"] == 96
    runs.append({
        "name": "Y16_full_inverse_zeta_weight_(2,1)",
        "weight": [2, 1], "mode": "coefficients",
        "series": "coefficients of 1/[(1-u^2)^16 D(u)] (the full "
                  "zeta_{Y16}), window 202, holdout 4",
        "verdict": vB,
        "annotation": (
            "HONEST ANNOTATION: the A4 refusal (exact self-reciprocity "
            "defect polynomial) is driven by the (1-u^2)^16 factor, "
            "whose inverse roots +-1 are not exchanged by a -> 2/a.  It "
            "is a correct exact refusal, but it detects the TRIVIAL "
            "factor, not the interesting spectral impurity; the latter "
            "is invisible to self-reciprocity (see run "
            "Y16_spectral_determinant) and is certified by Sturm in "
            "this build instead.")})

    # run C: spectral determinant of Y_9
    vC = detect(coefficient_sequence_from_satake(D9, 80),
                mode="coefficients", weight=(2, 1), holdout=4).as_dict()
    cc = cells_of(vC)
    assert vC["refusal"] is None
    assert cc["A4_PURITY"] == ("HOLDS", "NECESSARY_ONLY")
    assert vC["object"]["degree"] == 36
    runs.append({
        "name": "Y9_spectral_determinant_weight_(2,1)",
        "weight": [2, 1], "mode": "coefficients",
        "series": "coefficients of 1/D_9(u), window 80, holdout 4",
        "verdict": vC,
        "annotation": (
            "Same phenomenon as run Y16_spectral_determinant on the "
            "18-vertex example: necessary-only purity passes (FE holds) "
            "while actual purity is refuted by the exact Sturm "
            "certificate.")})
    return runs


# ---------------------------------------------------------------------------
# Section 7: the world record
# ---------------------------------------------------------------------------

def build_world(W, sweep, detector_runs):
    ihara = ("Y. Ihara (1966), zeta functions of discrete cocompact "
             "subgroups of PGL_2 over p-adic fields (the original "
             "rationality/determinant theorem, regular case)")
    hashimoto = ("K. Hashimoto (1989), zeta functions of finite graphs "
                 "via the edge (non-backtracking) matrix")
    bass = ("H. Bass (1992), the Ihara-Selberg zeta function of a tree "
            "lattice (three-term determinant identity for general "
            "graphs)")
    stark_terras = ("H. M. Stark and A. A. Terras (1996), zeta functions "
                    "of finite graphs and coverings (functional "
                    "equations, graph-RH formulation)")
    stark_terras2 = ("H. M. Stark and A. A. Terras (2000), zeta "
                     "functions of finite graphs and coverings, part II "
                     "(Artin-Ihara L-functions of graph coverings)")
    terras = ("A. A. Terras (2011), Zeta Functions of Graphs: A Stroll "
              "through the Garden (Cambridge)")
    lps = ("A. Lubotzky, R. Phillips and P. Sarnak (1988), Ramanujan "
           "graphs (Combinatorica; the |lambda| <= 2 sqrt(q) "
           "definition)")
    alon_nilli = ("N. Alon (1986), eigenvalues and expanders; A. Nilli "
                  "(1991), on the second eigenvalue of a graph "
                  "(Alon-Boppana bound)")
    kotani_sunada = ("M. Kotani and T. Sunada (2000), zeta functions of "
                     "finite graphs (pole locations vs the spectrum)")

    ladder = {
        "L0_WELL_DEFINED": cell(
            "HOLDS", "PROVED_HERE",
            witness=("Y_16 and Y_9 built explicitly; symmetry, 0/1 "
                     "entries, zero diagonal, 3-regularity, connectivity "
                     "(BFS) all asserted; girth 4 read off exactly from "
                     "tr(B^k) (first nonzero at k = 4).  zeta_G(u) = "
                     "prod over primitive closed geodesics of (1 - "
                     "u^L(P))^-1 is a well-defined rational function: "
                     "its inverse is the degree-96 (resp. 54) integer "
                     "polynomial computed here.  " + W["bass16"]),
            citation=ihara),
        "L1_MULTIPLICATIVITY": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("local(geodesic)-global multiplicativity: marked "
                     "closed non-backtracking tailless paths form, under "
                     "unique decomposition into powers of primitives, "
                     "the free-monoid structure that gives N_k = "
                     "sum_{d|k} d pi_d; Moebius inversion yields "
                     "INTEGRAL, NONNEGATIVE pi_d for all d <= 32 "
                     "(asserted), and the Euler product re-multiplies "
                     "to the zeta series exactly through u^32.  " +
                     W["euler16"]),
            citation=ihara + "; " + terras),
        "L2_EULER_PRODUCT": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=(W["euler16"] + "  Same for Y_9 through u^24 (" +
                     W["bass9"] + ")  The identity for all degrees is "
                     "Ihara's theorem (imported); the window is proved "
                     "here."),
            citation=ihara),
        "L3_BOUNDED_DEGREE_RATIONAL": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("zeta^-1 IS a polynomial (degree 96 / 54), proved "
                     "here via the Bass identity -- rationality is "
                     "exact, not imported.  The spectral local factors "
                     "are UNIFORMLY DEGREE 2: D(u) = prod over "
                     "eigenvalues lambda of (1 - lambda u + 2u^2) (an "
                     "algebraic identity via u^{2n} char((1+2u^2)/u), "
                     "no diagonalization needed), one quadratic per "
                     "eigenvalue -- the graph analogue of bounded-"
                     "degree local L-factors.  " + W["bass16"]),
            citation=bass + "; " + hashimoto),
        "L4_WEIGHT_DUALITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("weight-coherence and self-duality, exact: each "
                     "local quadratic 1 - lambda u + 2u^2 has inverse-"
                     "root product exactly q = 2 (the weight datum), "
                     "and the involution a -> 2/a fixes the global "
                     "inverse-root multiset: (2u^2)^32 D(1/(2u)) = D(u) "
                     "is asserted coefficientwise (c_{64-j} = 2^{32-j} "
                     "c_j).  A is symmetric (asserted), and total "
                     "realness of the spectrum is PROVED by Sturm "
                     "count = degree.  NOTE THE ABLATION: duality "
                     "coherence holds in full while purity FAILS -- "
                     "the pair (alpha, beta = 2/alpha) can be real "
                     "with |alpha| != sqrt(2)."),
            citation=stark_terras),
        "L5_CONDUCTOR_GAMMA_ROOT": cell(
            "HOLDS", "PROVED_HERE",
            witness=("canonical completion with exact FE and root "
                     "number +1: " + W["fe16"] + "  The (1-u^2)^{m-n} "
                     "factor is the canonical 'gamma-like' prefactor of "
                     "the Bass identity (Euler characteristic exponent "
                     "m - n = 16, resp. 9); conductor-type data is "
                     "trivial (finite graph, no ramification).  The "
                     "specific completion ((1-u^2)(1-4u^2))^{m-n} used "
                     "for the symmetric form is one of the standard "
                     "family of graph functional equations."),
            citation=stark_terras),
        "L6_CONTINUATION_FE": cell(
            "HOLDS", "PROVED_HERE",
            witness=("continuation is trivial and exact: zeta = 1/R "
                     "with R the explicitly computed integer polynomial "
                     "(degree 96 for Y_16, 54 for Y_9); the functional "
                     "equation is proved as exact coefficient "
                     "identities at both D-level and completed "
                     "Xi-level: " + W["fe16"] + " " + W["bass9"]),
            citation=bass + "; " + stark_terras),
        "L7_TWIST_TENSOR_COMPAT": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=(W["factor16"] + "  These are the graph-zeta "
                     "analogues of twisting (Artin-Ihara L-function of "
                     "a character of the deck group) and tensor "
                     "decomposition (Cartesian-product character "
                     "splitting)."),
            citation=stark_terras2),
        "L8_REALIZATION": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("THREE exact realizations: (i) dynamical -- zeta_G "
                     "is the Bowen-Lanford/Artin-Mazur zeta of the non-"
                     "backtracking edge shift: the 0/1 transition "
                     "matrix B is built explicitly and det(I - uB) = "
                     "zeta^-1 is proved in full from its traces; (ii) "
                     "combinatorial/group-theoretic -- Y_16 and Y_9 are "
                     "the Cayley graphs of the dihedral groups of "
                     "orders 32 and 18 with connection set {r, r^-1, "
                     "s}, asserted ENTRYWISE from the explicit group "
                     "multiplication; (iii) spectral -- the eigenvalue "
                     "package is pinned by exact integer char polys "
                     "computed by two independent methods.  " +
                     W["bass16"]),
            citation=hashimoto + "; " + bass + "; " + kotani_sunada),
        "L9_EXPLICIT_FORMULA_POSITIVITY": cell(
            "FAILS", "REFUTED_BY_WITNESS",
            witness=("THE ABLATION CELL.  An exact, finite explicit "
                     "formula EXISTS and is proved here: tr(B^k) = "
                     "sum_{d|k} d pi_d pairs geodesic counts against "
                     "the 96 inverse roots of zeta^-1 with no analytic "
                     "remainder (Bass identity proved in full).  But "
                     "the POSITIVITY half -- a Weil-positivity-type "
                     "principle that would force all nontrivial poles "
                     "onto |u| = 2^(-1/2), equivalently all nontrivial "
                     "|lambda| <= 2 sqrt(2) -- is REFUTED: " +
                     W["nonram16"] + "  " + W["nonram9"] + "  " +
                     TWO_LINE_ARGUMENT),
            citation=lps + "; " + kotani_sunada),
    }

    mechanisms = {
        "EULER_PRODUCT": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("present, supplied by primitive closed geodesics "
                     "(free monoid of marked closed non-backtracking "
                     "tailless paths under primitive decomposition): " +
                     W["euler16"]),
            citation=ihara),
        "DUALITY_FE": cell(
            "HOLDS", "PROVED_HERE",
            witness=("present, supplied by self-adjointness of A "
                     "(symmetric, asserted) and the reciprocal pairing "
                     "alpha beta = 2 in each local quadratic; FE proved "
                     "as exact coefficient identities (D-level and "
                     "completed Xi-level, root number +1): " +
                     W["fe16"]),
            citation=stark_terras),
        "TRACE_FORMULA": cell(
            "HOLDS", "PROVED_HERE",
            witness=("present, supplied by the Bass/Hashimoto "
                     "determinant identity -- the graph trace formula "
                     "-- PROVED IN FULL here for both graphs (not just "
                     "window-checked): 96 resp. 54 exact traces of the "
                     "non-backtracking operator determine det(I - uB) "
                     "by Newton, and it equals (1-u^2)^{m-n} det(I - "
                     "Au + 2u^2 I) coefficientwise.  " + W["bass16"] +
                     " " + W["bass9"]),
            citation=bass + "; " + hashimoto),
        "POSITIVITY_PURITY": cell(
            "FAILS", "REFUTED_BY_WITNESS",
            witness=("REFUTED BY EXACT WITNESS -- the point of this "
                     "world.  Self-adjointness of A supplies REALNESS "
                     "of the spectrum (proved by Sturm) but NOT the "
                     "Ramanujan/purity bound |lambda| <= 2 sqrt(2): "
                     "the tree-spectrum positivity that pins poles to "
                     "the critical circle has no analogue here.  " +
                     W["nonram16"] + "  " + W["nonram9"] + "  The "
                     "detector's necessary-only purity branch even "
                     "PASSES on 1/D (self-reciprocity = FE holds), "
                     "demonstrating exactly which mechanism is missing: "
                     "see detector_runs annotations."),
            citation=lps + "; " + alon_nilli),
        "TENSOR_OPS": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=(W["factor16"]),
            citation=stark_terras2),
        "FAMILY": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("present: the prism family {Y_n} with the exact "
                     "sweep n = 3..15 plus n = 16 (see sweep table in "
                     "detector_runs), and the vertical covering "
                     "structure Y_8 -> Y_16 with exact Artin-Ihara "
                     "factorization.  HONEST NOTE: unlike the Hasse "
                     "family sweep in world ff_elliptic_f5, membership "
                     "in this family does NOT enforce the critical "
                     "line -- the family contains certified Ramanujan "
                     "members (n <= 8, 10, 12, 14) and certified "
                     "non-Ramanujan members (n = 9, 11, 13, 15, 16); "
                     "as n grows the nontrivial spectral radius tends "
                     "to 3, so prisms are also a certified NON-example "
                     "of an expander family.  " + W["sweep"]),
            citation=alon_nilli),
    }

    critical_line = {
        "status": "FALSE",
        "detail": (
            "The graph-RH (Stark-Terras formulation): for a (q+1)-"
            "regular connected graph write u = q^(-s); zeta_X satisfies "
            "the Riemann hypothesis iff every pole of zeta_X with "
            "0 < Re(s) < 1 has Re(s) = 1/2, iff every nontrivial pole "
            "in u has |u| = q^(-1/2), iff X is Ramanujan.  Here q = 2 "
            "and the statement is FALSE for Y_16 and for Y_9: both "
            "graphs are certified non-Ramanujan by exact Sturm counts, "
            "and the certified eigenvalue translates to a pair of real "
            "poles of zeta_G, one strictly inside and one strictly "
            "outside |u| = 2^(-1/2).  THE ABLATION READING: this world "
            "has an exact Euler product (L2), an exactly proved "
            "functional equation (L6), and an exactly proved trace "
            "formula (TRACE_FORMULA / Bass identity), yet the critical "
            "line FAILS.  Those three mechanisms therefore CANNOT "
            "jointly force the critical line; whatever forces it in "
            "the worlds where it is a theorem (e.g. ff_elliptic_f5) "
            "must be a genuine positivity/purity input absent here.  "
            "Nothing about RH itself follows; rh_established = false."),
        "rigor": "REFUTED_BY_WITNESS",
        "citation": (stark_terras + "; " + lps + "; " + kotani_sunada),
        "witness": (W["nonram16"] + "  " + W["nonram9"] + "  " +
                    "TRANSLATION TO POLES: zeta^-1 = (1-u^2)^{m-n} * "
                    "prod_lambda (1 - lambda u + 2u^2) exactly (proved "
                    "here), so poles of zeta attached to lambda are the "
                    "roots u0 of 1 - lambda u + 2u^2 = 0.  " +
                    TWO_LINE_ARGUMENT + "  For the certified lambda "
                    "(8 < lambda^2 < 9) the roots are also poles of "
                    "zeta and not cancelled: zeta = 1/R identically "
                    "with R the computed polynomial."),
    }

    world = {
        "id": "ihara_nonramanujan",
        "title": ("Ihara zeta of exact non-Ramanujan cubic graphs "
                  "(prisms Y_16 and Y_9): the ablation witness against "
                  "'Euler product + FE + trace formula => critical "
                  "line'"),
        "definition": (
            "Primary: Y_16 = C_16 x K_2, the 3-regular prism on 32 "
            "vertices (equivalently Cay(D_16, {r, r^-1, s})), with "
            "Ihara zeta zeta(u)^-1 = (1-u^2)^16 det(I - Au + 2u^2 I) "
            "(q = 2).  Secondary: Y_9 (18 vertices), the smallest "
            "certifying prism from a deterministic sweep n = 3..15.  "
            "Spectrum of Y_n is {2 cos(2 pi k/n) +- 1}; all "
            "certificates below use only exact integer/Fraction "
            "computations (char polys, Sturm counts), never that "
            "closed form."),
        "arithmetic_class": (
            "EXACT_RATIONAL / EXACT_INTEGER combinatorial; Ihara zeta "
            "function of a finite 3-regular graph -- the function-"
            "field-like world where all three classical mechanisms "
            "hold exactly but purity fails"),
        "ladder": ladder,
        "mechanisms": mechanisms,
        "critical_line": critical_line,
        "sources": [
            "Y. Ihara (1966), On discrete subgroups of the two by two "
            "projective linear group over p-adic fields (J. Math. Soc. "
            "Japan)",
            "K. Hashimoto (1989), Zeta functions of finite graphs and "
            "representations of p-adic groups (Adv. Stud. Pure Math. "
            "15)",
            "H. Bass (1992), The Ihara-Selberg zeta function of a tree "
            "lattice (Internat. J. Math.)",
            "H. M. Stark and A. A. Terras (1996), Zeta functions of "
            "finite graphs and coverings (Adv. Math.)",
            "H. M. Stark and A. A. Terras (2000), Zeta functions of "
            "finite graphs and coverings, Part II (Adv. Math.)",
            "A. A. Terras (2011), Zeta Functions of Graphs: A Stroll "
            "through the Garden (Cambridge Univ. Press)",
            "A. Lubotzky, R. Phillips, P. Sarnak (1988), Ramanujan "
            "graphs (Combinatorica 8)",
            "N. Alon (1986), Eigenvalues and expanders (Combinatorica "
            "6); A. Nilli (1991), On the second eigenvalue of a graph "
            "(Discrete Math.)",
            "M. Kotani and T. Sunada (2000), Zeta functions of finite "
            "graphs (J. Math. Sci. Univ. Tokyo 7)",
            "J. Friedman (2008), A proof of Alon's second eigenvalue "
            "conjecture and related problems (Mem. Amer. Math. Soc.)",
        ],
        "rh_established": False,
        "notes": (
            "THIS IS THE PASS'S SHARPEST INDEPENDENCE WITNESS.  It "
            "separates the mechanism axes with exact certificates on "
            "both sides: EULER_PRODUCT holds (exact geodesic product, "
            "window u^32), DUALITY_FE holds (coefficient-identity FE, "
            "root number +1), TRACE_FORMULA holds (Bass identity "
            "proved IN FULL from 96 exact non-backtracking traces -- "
            "not window-checked, determined), and yet POSITIVITY_"
            "PURITY FAILS and the critical line is FALSE, certified "
            "twice (32-vertex Y_16 and 18-vertex Y_9) by exact Sturm "
            "counts with dyadic-rational localization of lambda^2 in "
            "(519/64, 2077/256] resp. (1061/128, 2123/256].  "
            "Consequently no argument of the shape 'Euler product + "
            "functional equation + trace formula => critical line' can "
            "be valid in any category containing this world: any "
            "credible route to critical-line statements must consume a "
            "positivity/purity input that this world falsifies "
            "(compare the OPEN L9 slot of the zeta world and the "
            "PROVED degree-form positivity of ff_elliptic_f5).  "
            "Secondary findings recorded honestly: the task's "
            "suggested smaller candidate n = 14 does NOT certify "
            "(Y_14 is Ramanujan, proved exactly); n = 15 certifies; "
            "the smallest certifying prism is n = 9; smaller NON-PRISM "
            "cubic non-Ramanujan graphs were not searched for.  The "
            "detector's necessary-only purity branch passes on the "
            "impure spectral determinant (annotated in detector_runs): "
            "self-reciprocity (= FE) does not see the violation -- the "
            "operational content of the ablation.  NO floats appear "
            "anywhere in this build; every HOLDS/FAILS is an exact "
            "integer/Fraction computation or a named imported theorem.  "
            "Nothing here bears on RH over Q: rh_established = false."),
        "detector_runs": {
            "description": (
                "core.reconstruct.detect on exact coefficient data of "
                "the Y_16 and Y_9 spectral determinants and the full "
                "Y_16 inverse zeta at weight (2,1), each honestly "
                "annotated (necessary-only purity passes on impure "
                "data; the full-zeta refusal is driven by the trivial "
                "(1-u^2)^16 factor); plus the exact prism sweep table "
                "and the certified localization intervals."),
            "runs": None,        # filled in main()
            "prism_sweep": sweep,
            "certified_intervals": {
                "Y16": "519/64 < lambda^2 <= 2077/256 (width 1/256), "
                       "with 8 < lambda^2 < 9 and Sturm count 1 in "
                       "(8, 9]",
                "Y9": "1061/128 < lambda^2 <= 2123/256 (width 1/256), "
                      "with 8 < lambda^2 < 9 and Sturm count 1 in "
                      "(8, 9]"},
            "nonbacktracking_trace_prefixes": {
                "Y16_tr_Bk_k_1_12": N16_PREFIX,
                "Y9_tr_Bk_k_1_12": N9_PREFIX},
        },
    }
    return world


def main():
    W, A16, A9, c16, c9, sweep = build_certificates()
    W, D16, R16, D9, R9 = build_zeta_witnesses(W, A16, A9)
    detector_runs = run_detector(D16, R16, D9)
    world = build_world(W, sweep, detector_runs)
    world["detector_runs"]["runs"] = detector_runs
    probs = validate_world(world)
    assert not probs, probs
    path = save_world(world, "worlds")
    print("wrote", path)
    print("ladder:", {k: v["status"] for k, v in world["ladder"].items()})
    print("mechanisms:",
          {k: v["status"] for k, v in world["mechanisms"].items()})
    print("critical_line:", world["critical_line"]["status"])
    print("sweep verdicts:",
          {e["n"]: e["sturm_count_sq_in_(8,9]"] for e in sweep})
    print("certified intervals: Y16", str(INT16[0]), "-", str(INT16[1]),
          "| Y9", str(INT9[0]), "-", str(INT9[1]))
    print("detector runs:",
          [(r["name"], r["verdict"]["refusal"]) for r in detector_runs])


if __name__ == "__main__":
    main()
