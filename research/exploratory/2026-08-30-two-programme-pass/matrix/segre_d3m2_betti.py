"""Equivariant Betti characters of the Segre embedding of P^2 x P^2
(dim V = 3, m = 2): Tor_i^{Sym(W)}(R, C)_j with W = V x V,
R = + (Sym^j V) x (Sym^j V), via exact Koszul homology per torus
weight (integer matrices, Fraction rank; the diagonal GL_3 torus
weight = the TOTAL exponent vector in x1, x2, x3 across both tensor
factors). Ground truth for the Lascoux-strand derivation of the
general-rank square defect (T-108508 general-d problem; T-108515
Corollary 2). rh_established = false.
"""
import json
import time
from fractions import Fraction as Fr
from itertools import combinations, product

D = 3


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


# W basis: pairs (a, b), a, b in 0..D-1  (x_a in factor 1, x_b in 2)
WB = [(a, b) for a in range(D) for b in range(D)]      # 9


def monomials(deg):
    """exponent vectors of degree deg in D variables."""
    if deg < 0:
        return []
    out = []

    def rec(pos, rem, cur):
        if pos == D - 1:
            out.append(tuple(cur + [rem]))
            return
        for v in range(rem + 1):
            rec(pos + 1, rem - v, cur + [v])
    rec(0, deg, [])
    return out


def Rbasis(j):
    """pairs (mono1, mono2) of degree j each."""
    ms = monomials(j)
    return [(u, v) for u in ms for v in ms]


def wt(el):
    """total exponent vector of a basis element of Lambda^i W x R."""
    S, (u, v) = el
    w = [0] * D
    for (a, b) in S:
        w[a] += 1
        w[b] += 1
    for i in range(D):
        w[i] += u[i] + v[i]
    return tuple(w)


def act(wvec, mono_pair):
    """multiply R_j element by W basis vector (a, b)."""
    (a, b) = wvec
    (u, v) = mono_pair
    uu = list(u)
    uu[a] += 1
    vv = list(v)
    vv[b] += 1
    return (tuple(uu), tuple(vv))


def rank_Fr(rows):
    mat = [dict(r) for r in rows if r]
    rank = 0
    pivcol_of = {}
    for r in mat:
        while r:
            c = min(r)
            if c in pivcol_of:
                pr, pv = pivcol_of[c]
                fct = Fr(r[c], 1) / pv
                for cc, vv in pr.items():
                    nv = r.get(cc, Fr(0)) - fct * vv
                    if nv == 0:
                        r.pop(cc, None)
                    else:
                        r[cc] = nv
            else:
                break
        if r:
            c = min(r)
            pivcol_of[c] = (r, Fr(r[c]))
            rank += 1
    return rank


def component(i, j):
    """basis of Lambda^i W x R_{j-i}, grouped by weight."""
    if j - i < 0 or i < 0 or i > len(WB):
        return {}
    groups = {}
    for S in combinations(range(len(WB)), i):
        Sv = tuple(WB[k] for k in S)
        for mp in Rbasis(j - i):
            el = (S, mp)
            w = wt((Sv, mp))
            groups.setdefault(w, []).append(el)
    return groups


def differential(dom, cod_index, j, i):
    rows = []
    for (S, mp) in dom:
        row = {}
        for pos, k in enumerate(S):
            sign = (-1) ** pos
            S2 = tuple(x for x in S if x != k)
            m2 = act(WB[k], mp)
            col = cod_index.get((S2, m2))
            if col is not None:
                row[col] = row.get(col, 0) + sign
        rows.append(row)
    return rows


def main():
    JMAX = 7
    tor = {}
    comp_cache = {}

    def comp(i, j):
        if (i, j) not in comp_cache:
            comp_cache[(i, j)] = component(i, j)
        return comp_cache[(i, j)]

    for j in range(0, JMAX + 1):
        for i in range(0, min(j, 9) + 1):
            gi = comp(i, j)
            gdn = comp(i - 1, j) if i >= 1 else {}
            gup = comp(i + 1, j)
            row = {}
            for w, dom in gi.items():
                cod = gdn.get(w, [])
                cod_index = {el: c for c, el in enumerate(cod)}
                rk_dn = rank_Fr(differential(dom, cod_index, j, i)) \
                    if i >= 1 and cod else 0
                dom_up = gup.get(w, [])
                dom_index = {el: c for c, el in enumerate(dom)}
                rk_up = rank_Fr(differential(dom_up, dom_index, j,
                                             i + 1)) if dom_up else 0
                # if i == 0, the map to degree -1 is zero: rk_dn = 0
                if i == 0:
                    rk_dn = 0
                hdim = len(dom) - rk_dn - rk_up
                if hdim:
                    row[w] = hdim
            if row:
                tor[(i, j)] = row
                say(f"Tor_{i} @ j={j}: dim "
                    f"{sum(row.values())} over {len(row)} weights")
        # free memory of low components no longer needed
        comp_cache.clear()
    say("assembling characters (weights as sorted exponent lists)")
    out = {}
    for (i, j), row in sorted(tor.items()):
        # collapse weight -> multiplicity, symmetric-function fingerprint
        out[f"{i},{j}"] = {" ".join(map(str, w)): d
                           for w, d in sorted(row.items())}
    json.dump(out, open('matrix/segre_d3m2_betti.json', 'w'), indent=1)
    say("done")


if __name__ == "__main__":
    main()
