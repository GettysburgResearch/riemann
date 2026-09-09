"""STABLE LAYER LAWS for the square defect (T-108522 corollary work).

Setting: N_{2,d} - G_d = the correction layers of T-108508. Two facts
make each layer a STABLE symmetric function:
  (1) restriction: setting x_d = 0 sends N_{2,d} -> N_{2,d-1} and
      G_d -> G_{d-1} (immediate from the alternant / the weight
      multisets), so the T^j-corrections form a compatible sequence;
  (2) a compatible sequence of weight-2j symmetric functions is the
      image of a UNIQUE element of the ring of symmetric functions,
      and that element is determined by its specialization at
      d = 2j variables (e_1..e_{2j} algebraically independent there).
Hence: computing corr_j := [T^j](N_{2,2j} - G_{2j}) SYMBOLICALLY at
d = 2j and expressing it in the e-basis PROVES the closed layer law
for ALL d.

This script computes corr_3 (at d = 6), corr_4 (at d = 8) and corr_5
(at d = 10) exactly, decomposes them in the e-monomial basis by
matching monomial-symmetric coefficients, and tests T-108508's
conjectured continuation corr_3 = 2 sum_{i>=4} (-1)^i e_i h_{6-i}.
Truncated-series arithmetic: only T-coefficients up to j are ever
formed. Exact integers throughout (dict polynomials, stdlib).
rh_established = false.
"""
import json
import sys
import time
from itertools import combinations

sys.path.insert(0, '.')


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


# ---- dict polynomials over exponent tuples -------------------------

def pmul(p, q):
    r = {}
    for k1, c1 in p.items():
        for k2, c2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2))
            r[k] = r.get(k, 0) + c1 * c2
    return {k: v for k, v in r.items() if v}


def padd(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + v
        if not r[k]:
            del r[k]
    return r


def pscale(p, c):
    return {k: c * v for k, v in p.items()} if c else {}


def one(d):
    return {(0,) * d: 1}


def var(d, i):
    e = [0] * d
    e[i] = 1
    return {tuple(e): 1}


def tser_mul(P, Q, J):
    """truncated T-series (lists of dict-polys) product to order J."""
    R = [dict() for _ in range(J + 1)]
    for i, pi in enumerate(P[:J + 1]):
        if not pi:
            continue
        for j, qj in enumerate(Q[:J + 1 - i]):
            if qj:
                R[i + j] = padd(R[i + j], pmul(pi, qj))
    return R


def lin(d, w, sign=-1):
    """1 + sign*w*T as a truncated series."""
    return [one(d), pscale(w, sign)]


def h_poly(d, r):
    """h_r in d variables: all monomials of degree r."""
    out = {}

    def rec(pos, rem, cur):
        if pos == d - 1:
            out[tuple(cur + [rem])] = 1
            return
        for v in range(rem + 1):
            rec(pos + 1, rem - v, cur + [v])
    if r == 0:
        return one(d)
    rec(0, r, [])
    return out


def e_poly(d, k):
    """e_k in d variables."""
    out = {}
    for S in combinations(range(d), k):
        e = [0] * d
        for i in S:
            e[i] = 1
        out[tuple(e)] = 1
    return out if k else one(d)


def corr_layer(d, J):
    """[T^0..T^J] of N_{2,d} and of G_d; return N - G lists."""
    # Q = det(1 - Sym^2 T) truncated
    Q = [one(d)]
    for i in range(d):
        for j in range(i, d):
            w = pmul(var(d, i), var(d, j))
            Q = tser_mul(Q, lin(d, w), J)
    # series sum h_r^2 T^r truncated
    S = [pmul(h_poly(d, r), h_poly(d, r)) for r in range(J + 1)]
    N = tser_mul(Q, S, J)
    # G_d truncated: sum (-1)^{j(j-1)/2} e_j(Lam^2) T^j
    P = [one(d)]
    for i in range(d):
        for j in range(i + 1, d):
            w = pmul(var(d, i), var(d, j))
            P = tser_mul(P, lin(d, w, +1), J)     # prod(1 + w T)
    G = [pscale(P[j], (-1) ** (j * (j - 1) // 2)) for j in range(J + 1)]
    return [padd(N[j], pscale(G[j], -1)) for j in range(J + 1)]


# ---- e-basis decomposition of a symmetric polynomial ----------------

def partitions(n, maxpart):
    if n == 0:
        yield ()
        return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest


def e_monomial(d, lam):
    p = one(d)
    for part in lam:
        p = pmul(p, e_poly(d, part))
    return p


def decompose_e(d, poly, weight):
    """decompose weight-homogeneous symmetric poly in e-monomials by
    solving on monomial coefficients (greedy elimination in
    lex-sorted partition order)."""
    residual = dict(poly)
    coeffs = {}
    for lam in sorted(partitions(weight, min(d, weight)), reverse=True):
        # e_lam has leading (lex-max) monomial = conjugate partition
        # exponent; instead of theory, solve greedily: pick the
        # coefficient of the exponent vector that e_lam leads in.
        pass
    # simpler robust route: linear solve via distinct monomial keys
    lams = sorted(partitions(weight, min(d, weight)))
    mats = [e_monomial(d, lam) for lam in lams]
    keys = sorted(set().union(*[set(m) for m in mats], set(residual)))
    import fractions
    Fr = fractions.Fraction
    A = [[Fr(m.get(k, 0)) for m in mats] for k in keys]
    b = [Fr(residual.get(k, 0)) for k in keys]
    # least-squares-free exact Gaussian elimination (overdetermined,
    # consistent iff decomposable)
    ncols = len(lams)
    rows = [row + [bb] for row, bb in zip(A, b)]
    piv = []
    r0 = 0
    for c in range(ncols):
        pr = None
        for r in range(r0, len(rows)):
            if rows[r][c] != 0:
                pr = r
                break
        if pr is None:
            continue
        rows[r0], rows[pr] = rows[pr], rows[r0]
        pv = rows[r0][c]
        rows[r0] = [v / pv for v in rows[r0]]
        for r in range(len(rows)):
            if r != r0 and rows[r][c] != 0:
                f = rows[r][c]
                rows[r] = [v - f * w for v, w in zip(rows[r], rows[r0])]
        piv.append(c)
        r0 += 1
    # consistency
    for r in range(r0, len(rows)):
        if rows[r][ncols] != 0:
            raise RuntimeError("not decomposable in e-basis")
    sol = [Fr(0)] * ncols
    for r, c in enumerate(piv):
        sol[c] = rows[r][ncols]
    return {lams[c]: sol[c] for c in range(ncols) if sol[c]}


def render(dec):
    return " + ".join(f"{v}*e{list(lam)}" for lam, v in
                      sorted(dec.items(), reverse=True))


def main():
    out = {"rh_established": False}
    # corr_3 at d = 6
    say("corr_3 at d = 6 ...")
    d = 6
    layers = corr_layer(d, 3)
    for j in range(3):
        assert not layers[j], f"unexpected correction at T^{j}"
    dec3 = decompose_e(d, layers[3], 6)
    say("corr_3 = " + render(dec3))
    # conjectured: 2(e4 h2 - e5 h1 + e6 h0)
    conj = padd(padd(pscale(pmul(e_poly(d, 4),
                                 padd(pmul(e_poly(d, 1), e_poly(d, 1)),
                                      pscale(e_poly(d, 2), -1))), 2),
                     pscale(pmul(e_poly(d, 5), e_poly(d, 1)), -2)),
                pscale(e_poly(d, 6), 2))
    match = padd(layers[3], pscale(conj, -1)) == {}
    say(f"corr_3 == 2 sum_(i>=4) (-1)^i e_i h_(6-i): {match}")
    out["corr3"] = {"e_basis": {str(list(k)): str(v)
                                for k, v in dec3.items()},
                    "matches_T108508_conjecture": bool(match)}
    # corr_4 at d = 8
    say("corr_4 at d = 8 ...")
    d = 8
    layers = corr_layer(d, 4)
    dec4 = decompose_e(d, layers[4], 8)
    say("corr_4 = " + render(dec4))
    out["corr4"] = {"e_basis": {str(list(k)): str(v)
                                for k, v in dec4.items()}}
    # corr_5 at d = 10
    say("corr_5 at d = 10 ...")
    d = 10
    layers = corr_layer(d, 5)
    dec5 = decompose_e(d, layers[5], 10)
    say("corr_5 = " + render(dec5))
    out["corr5"] = {"e_basis": {str(list(k)): str(v)
                                for k, v in dec5.items()}}
    json.dump(out, open('matrix/stable_layers.json', 'w'), indent=1)
    say("done")


if __name__ == "__main__":
    main()
