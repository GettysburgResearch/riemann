"""Independent adversarial verification of T-108515 Theorem 1 (coarse Segre
bridge), Lemma 1 (ballot decomposition), degree bookkeeping, and Corollary 1
(Eulerian specialization), incl. N_5(2,1) = A_5.

Pure Python, exact integers. Polynomials in (alpha, beta) are dicts
{(i, j): c} meaning sum c * alpha^i beta^j. T-polynomials/series are lists of
such dicts. NOTHING is imported from the repo.

Provenance: written by the adversarial verification wave (piece 1
verifier of workflow wf_4b1aed99-0be), adopted into the campaign as
the fast full-symbolic check for Theorem 1; m = 2..6 complete in
seconds. rh_established = false.
"""
from math import comb
from itertools import product, permutations


# ---------- 2-variable polynomial arithmetic ----------
def padd(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + v
        if r[k] == 0:
            del r[k]
    return r


def pscale(p, c):
    return {k: c * v for k, v in p.items()} if c else {}


def pmul(p, q):
    r = {}
    for (i1, j1), c1 in p.items():
        for (i2, j2), c2 in q.items():
            k = (i1 + i2, j1 + j2)
            r[k] = r.get(k, 0) + c1 * c2
    return {k: v for k, v in r.items() if v != 0}


def ppow(p, n):
    r = {(0, 0): 1}
    for _ in range(n):
        r = pmul(r, p)
    return r


ONE = {(0, 0): 1}


# ---------- T-polynomial arithmetic (lists of alpha-beta dicts) ----------
def tmul(P, Q, trunc=None):
    n = len(P) + len(Q) - 1 if trunc is None else trunc + 1
    R = [dict() for _ in range(n)]
    for i, pi in enumerate(P):
        if not pi:
            continue
        for j, qj in enumerate(Q):
            if i + j >= n or not qj:
                continue
            R[i + j] = padd(R[i + j], pmul(pi, qj))
    return R


def teq(P, Q):
    n = max(len(P), len(Q))
    for i in range(n):
        pi = P[i] if i < len(P) else {}
        qi = Q[i] if i < len(Q) else {}
        if pi != qi:
            return False
    return True


def lin_factor(w):
    """1 - w*T for a monomial weight dict w."""
    return [ONE, pscale(w, -1)]


# ---------- building blocks ----------
def h_poly(r):
    """Complete homogeneous h_r(alpha, beta) directly (no recurrence)."""
    return {(r - i, i): 1 for i in range(r + 1)}


def sym_det(m, k):
    """det(1 - Sym^{m-2k}(A) * (alpha*beta)^k * T): weights
    alpha^{m-2k-i} beta^i * (alpha beta)^k, i = 0..m-2k."""
    P = [ONE]
    for i in range(m - 2 * k + 1):
        P = tmul(P, lin_factor({(m - k - i, k + i): 1}))
    return P


def d_full_bits(m):
    """det(1 - A^{tensor m} T) via the explicit 2^m eigenvalue products."""
    P = [ONE]
    for bits in product([0, 1], repeat=m):
        j = sum(bits)
        P = tmul(P, lin_factor({(m - j, j): 1}))
    return P


def series_hm(m, trunc):
    return [ppow(h_poly(r), m) for r in range(trunc + 1)]


# ---------- checks ----------
def check_lemma1(mmax=14):
    ok = True
    for m in range(1, mmax + 1):
        lhs = ppow({(1, 0): 1, (0, 1): 1}, m)          # (alpha+beta)^m
        rhs = {}
        total_dim = 0
        for k in range(m // 2 + 1):
            ck = comb(m, k) - comb(m, k - 1) if k >= 1 else 1
            assert ck >= 0
            strand = {(m - k - i, k + i): 1 for i in range(m - 2 * k + 1)}
            rhs = padd(rhs, pscale(strand, ck))
            total_dim += ck * (m - 2 * k + 1)
        if lhs != rhs or total_dim != 2 ** m:
            ok = False
            print(f"  LEMMA 1 FAILS at m={m}")
    print(f"Lemma 1 character identity, m=1..{mmax}: {'PASS' if ok else 'FAIL'}")
    return ok


def check_degree_formula(mmax=40):
    ok = True
    for m in range(2, mmax + 1):
        s = sum((comb(m, k) - comb(m, k - 1)) * (m - 2 * k + 1)
                for k in range(1, m // 2 + 1))
        if (m - 1) + s != 2 ** m - 2:
            ok = False
            print(f"  DEGREE FORMULA FAILS at m={m}")
    print(f"Degree bookkeeping (m-1)+sum c_k(m-2k+1) = 2^m-2, m=2..{mmax}: "
          f"{'PASS' if ok else 'FAIL'}")
    return ok


def defect_N(m, window=4):
    """N_m = det(1 - Sym^m(A) T) * sum_r h_r^m T^r, with tail check."""
    trunc = m - 1 + window
    S = series_hm(m, trunc)
    Q = sym_det(m, 0)  # k=0 strand IS det(1 - Sym^m(A) T)
    NP = tmul(Q, S, trunc)
    for i in range(m, trunc + 1):
        assert not NP[i], f"N_{m} tail nonzero at T^{i}: {NP[i]}"
    return NP[:m]


def check_theorem1(m):
    trunc = 2 ** m + 4
    S = series_hm(m, trunc)
    D = d_full_bits(m)
    # cross-check D against the binomial-collected form
    D2 = [ONE]
    for j in range(m + 1):
        for _ in range(comb(m, j)):
            D2 = tmul(D2, lin_factor({(m - j, j): 1}))
    assert teq(D, D2), f"m={m}: two routes to det(1 - A^tensor-m T) disagree"

    K = tmul(D, S, trunc)
    tail = all(not K[i] for i in range(2 ** m + 1, trunc + 1))
    ktop = K[2 ** m - 2]
    deg_ok = bool(ktop) and all(not K[i] for i in range(2 ** m - 1, 2 ** m + 1))

    N = defect_N(m)
    R = list(N)
    for k in range(1, m // 2 + 1):
        ck = comb(m, k) - comb(m, k - 1)
        f = sym_det(m, k)
        for _ in range(ck):
            R = tmul(R, f)
    ident = teq(K[: 2 ** m + 1], R)
    print(f"Theorem 1, m={m}: K-series tail vanishes: {tail}; "
          f"deg K = 2^m - 2 = {2**m - 2}: {deg_ok}; "
          f"K == N_m * prod_k det(1 - Sym^(m-2k) b^k T)^c_k: {ident}")
    return tail and deg_ok and ident


def eulerian_desc(m):
    """A_m(T) coefficients by brute-force descent count over S_m."""
    coeffs = [0] * m
    for perm in permutations(range(m)):
        d = sum(1 for i in range(m - 1) if perm[i] > perm[i + 1])
        coeffs[d] += 1
    return coeffs


def eulerian_worpitzky(m, window=4):
    """(1-T)^{m+1} * sum_r (r+1)^m T^r, tail-checked."""
    trunc = m - 1 + window
    num = [0] * (trunc + 1)
    for i in range(min(m + 2, trunc + 1)):
        num[i] = (-1) ** i * comb(m + 1, i)
    ser = [(r + 1) ** m for r in range(trunc + 1)]
    out = [sum(num[i] * ser[r - i] for i in range(r + 1))
           for r in range(trunc + 1)]
    assert all(v == 0 for v in out[m:]), f"Worpitzky tail fails at m={m}"
    return out[:m]


def check_corollary1(mmax=6):
    ok = True
    for m in range(2, mmax + 1):
        N = defect_N(m)
        Nspec = [sum(c.values()) for c in N]        # alpha = beta = 1
        Adesc = eulerian_desc(m)
        Aworp = eulerian_worpitzky(m)
        good = (Nspec == Adesc == Aworp)
        pal = Nspec == Nspec[::-1]
        print(f"Corollary 1, m={m}: N_m(2,1) = {Nspec}; descent A_m = {Adesc};"
              f" Worpitzky = {Aworp}; equal: {good}; palindromic: {pal}")
        ok = ok and good and pal
    return ok


def show_small_N():
    def render(NP):
        # convert to (a,b) only for display of m=3
        return NP
    N3 = defect_N(3)
    # expected: 1 + 2ab T + b^3 T^2  ->  T^1: 2(a b) = 2(al+be)(al be)
    exp3 = [ {(0, 0): 1}, {(2, 1): 2, (1, 2): 2}, {(3, 3): 1} ]
    print(f"N_3 == 1 + 2abT + b^3T^2: {teq(N3, exp3)}")


if __name__ == "__main__":
    ok = True
    ok &= check_lemma1()
    ok &= check_degree_formula()
    show_small_N()
    for m in (2, 3, 4, 5, 6):
        ok &= check_theorem1(m)
    ok &= check_corollary1(6)
    print("OVERALL:", "ALL PASS" if ok else "FAILURES PRESENT")
