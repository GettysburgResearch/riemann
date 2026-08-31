"""Equivariant Betti characters of the Segre embedding of (P^1)^3:
Tor_i^{Sym(W)}(R, C)_j with W = V x V x V, R = + (Sym^r V)^x3, via
exact Koszul homology per torus weight (integer matrices, Fraction
rank). Outputs each Tor_{i,j} as a character in (alpha, beta) and the
assembled K-polynomial for cross-check against the coarse bridge.
rh_established = false.
"""
import json
import sys
import time
from fractions import Fraction as Fr
from itertools import combinations, product

def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)

# W basis: bits in {0,1}^3 (0 -> x/alpha, 1 -> y/beta)
WB = list(product([0,1], repeat=3))          # 8 vectors
# R_j basis: (i1,i2,i3), 0 <= i_l <= j  (y-degree per factor)
def Rbasis(j):
    return [(i1,i2,i3) for i1 in range(j+1) for i2 in range(j+1)
            for i3 in range(j+1)]

def wt_W(bits):        # (total y-degree contribution)
    return sum(bits)
def wt_R(mono):
    return sum(mono)

def act(bits, mono, j):
    """multiply R_j monomial by W basis vector -> R_{j+1} monomial."""
    return tuple(m + b for m, b in zip(mono, bits))

def rank_Fr(rows, ncols):
    """exact rank of a sparse integer matrix given as list of dicts."""
    mat = [dict(r) for r in rows]
    rank = 0
    pivcol_of = {}
    for r in mat:
        # eliminate with existing pivots
        while r:
            c = min(r)
            if c in pivcol_of:
                pr, pv = pivcol_of[c]
                f = Fr(r[c], 1) / pv
                for cc, vv in pr.items():
                    nv = r.get(cc, Fr(0)) - f*vv
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

def koszul_component(i, j, weight):
    """Basis + differential matrices for the weight component of
    Lambda^i W x R_{j-i} -> Lambda^{i-1} W x R_{j-i+1}.
    weight = total y-degree (0..3j after normalization: element of
    Lambda^i W x R_{j-i} has y-degree sum(bits over subset) + sum(mono))."""
    if j - i < 0 or i < 0 or i > 8:
        return []
    dom = []
    for S in combinations(range(8), i):
        wS = sum(wt_W(WB[k]) for k in S)
        for mono in Rbasis(j - i):
            if wS + wt_R(mono) == weight:
                dom.append((S, mono))
    return dom

def differential(i, j, weight, dom, cod_index):
    rows = []      # one row per domain basis vector: dict col -> int
    for (S, mono) in dom:
        row = {}
        for pos, k in enumerate(S):
            sign = (-1)**pos
            S2 = tuple(x for x in S if x != k)
            m2 = act(WB[k], mono, j - i)
            key = (S2, m2)
            col = cod_index.get(key)
            if col is not None:
                row[col] = row.get(col, 0) + sign
        rows.append(row)
    return rows

def main():
    JMAX = 8
    tor = {}
    for j in range(0, JMAX+1):
        for i in range(0, min(j, 8)+1):
            # component spaces per weight
            weights = set()
            dom_all = koszul_component(i, j, None) if False else None
            # collect weights present
            for S in combinations(range(8), i):
                wS = sum(wt_W(WB[k]) for k in S)
                for mono in Rbasis(j - i) if j - i >= 0 else []:
                    weights.add(wS + wt_R(mono))
            for wgt in sorted(weights):
                dom = koszul_component(i, j, wgt)
                if not dom:
                    continue
                # codomain (i-1, j) same weight
                cod = koszul_component(i-1, j, wgt) if i >= 1 else []
                cod_index = {bm: c for c, bm in enumerate(cod)}
                d_i = differential(i, j, wgt, dom, cod_index) if i >= 1 else [dict() for _ in dom]
                rk_i = rank_Fr([r for r in d_i if r], len(cod)) if i >= 1 else 0
                # incoming from (i+1, j) same weight
                dom_up = koszul_component(i+1, j, wgt) if i+1 <= 8 else []
                dom_index = {bm: c for c, bm in enumerate(dom)}
                d_up = differential(i+1, j, wgt, dom_up, dom_index) if dom_up else []
                rk_up = rank_Fr([r for r in d_up if r], len(dom)) if dom_up else 0
                hdim = len(dom) - rk_i - rk_up
                if hdim:
                    tor.setdefault((i, j), {})[wgt] = hdim
        if any((i, j) in tor for i in range(9)):
            say(f"j={j}: " + "; ".join(
                f"Tor_{i}: {tor[(i,j)]}" for i in range(9) if (i, j) in tor))
    with open('matrix/segre3_betti.json', 'w') as f:
        json.dump({f"{i},{j}": {str(w): d for w, d in v.items()}
                   for (i, j), v in tor.items()}, f, indent=1)
    say("done")

if __name__ == "__main__":
    main()
