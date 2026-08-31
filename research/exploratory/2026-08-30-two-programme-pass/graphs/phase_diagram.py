"""C5/C6 continuation — the TWO-INVARIANT PHASE DIAGRAM (Lane 3).

For every graph in a certified corpus (capped-ladder families, GP
members with 2n <= 22, Moebius ladders, Petersen), compute EXACTLY:

  - the Cheeger/edge-expansion constant
        h(G) = min_{0 < |S| <= n/2} e(S, S-bar) / |S|
    (exhaustive over all subsets, exact Fractions);
  - the frustration index f(G) = |E| - maxcut(G) (exhaustive maxcut) —
    the minimum number of edges whose removal makes G bipartite
    (f = 0 iff bipartite);
  - the Sturm-certified breach verdict RAM / POS / NEG / BOTH (cut
    283/100 with the census separation guard; guard-flagged spectra
    get an adaptive rational cut, the witness16 method).

Question deposited by O-108006/T-108514: the two failure directions
(expansion vs near-bipartiteness) — are they SEPARATED by the two
structural invariants (h, f/m)?  This script produces the exact
diagram; the reading lives in the claim addendum.

Exact integer/Fraction arithmetic throughout. Writes
graphs/phase_diagram.json. rh_established = false.
"""
import json
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, '.')
sys.path.insert(0, 'graphs')
from core.exact import charpoly_of_matrix, count_real_roots_in, poly_eval
from telescope import gp, petersen, squares_poly, girth, bipartite

R1 = Fr(283, 100)


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


# ---------------- constructors --------------------------------------

def capped_ladder(k, cap):
    """Diamond head + k-rung corridor + cap matching on far 6
    positions; n = 2k + 10; Hamiltonian frame 0..n-1."""
    n = 2 * k + 10
    E = {(i, (i + 1) % n) for i in range(n)}
    E |= {(0, 2), (1, 3)}
    for j in range(k):
        E.add((4 + j, n - 1 - j))
    base = 4 + k
    for (r, s) in cap:
        E.add((base + r, base + s))
    A = [[0] * n for _ in range(n)]
    for (i, j) in E:
        A[i][j] = A[j][i] = 1
    assert all(sum(row) == 3 for row in A)
    return A


def moebius(m):
    """Moebius ladder on 2m vertices: cycle C_{2m} + m diameters."""
    n = 2 * m
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        A[i][(i + 1) % n] = A[(i + 1) % n][i] = 1
        A[i][(i + m) % n] = A[(i + m) % n][i] = 1
    return A


CAPS = {
    "708cap": ((0, 3), (1, 5), (2, 4)),
    "709cap": ((0, 5), (1, 3), (2, 4)),
    "706cap": ((0, 2), (1, 4), (3, 5)),
    "crosscap": ((0, 3), (1, 4), (2, 5)),
}


# ---------------- exact verdict (with adaptive cut) -----------------

def adaptive_cut(p2, n):
    """Rational r with 8 < r^2 <= (smallest eigenvalue-square above 8),
    certified by Sturm; assumes at least one square in (8, 9)."""
    lo, hi = Fr(8), Fr(9)
    while hi - lo > Fr(1, 10 ** 8):
        mid = (lo + hi) / 2
        if count_real_roots_in(p2, Fr(8), mid) == 0:
            lo = mid
        else:
            hi = mid
    # lo < smallest square <= hi; pick rational r with 8 < r^2 <= lo
    for k in range(3, 14):
        num = 1
        d = 10 ** k
        # smallest integer num with (num/d)^2 > 8
        num = int((8 ** 0.5) * d) + 1
        while Fr(num, d) ** 2 <= 8:
            num += 1
        r = Fr(num, d)
        if r * r <= lo:
            assert count_real_roots_in(p2, Fr(8), r * r) == 0
            return r
    raise RuntimeError("no rational cut found")


def verdict(A):
    p = charpoly_of_matrix(A)
    p2 = squares_poly(A)
    unt = count_real_roots_in(p2, Fr(8), Fr(9))
    if poly_eval(p2, Fr(9)) == 0:
        unt -= 1
    if unt == 0:
        return "RAM", None
    guard = count_real_roots_in(p2, Fr(8), R1 * R1)
    cut = R1 if guard == 0 else adaptive_cut(p2, len(A))
    pos = count_real_roots_in(p, cut, Fr(3))
    if poly_eval(p, Fr(3)) == 0:
        pos -= 1
    neg = count_real_roots_in(p, Fr(-3), -cut)
    if poly_eval(p, -cut) == 0:
        neg -= 1
    v = ("BOTH" if pos and neg else "POS" if pos else
         "NEG" if neg else "RAM")
    return v, (str(cut) if cut != R1 else None)


# ---------------- exact h and frustration (one subset pass) ---------

def h_and_frustration(A):
    n = len(A)
    masks = [sum(1 << j for j in range(n) if A[i][j]) for i in range(n)]
    m_edges = sum(sum(row) for row in A) // 2
    full = (1 << n) - 1
    best_h = None
    maxcut = 0
    half = n // 2
    for S in range(1, 1 << (n - 1)):      # fix vertex n-1 outside S
        comp = full ^ S
        cut = 0
        T = S
        while T:
            v = (T & -T).bit_length() - 1
            cut += (masks[v] & comp).bit_count()
            T &= T - 1
        if cut > maxcut:
            maxcut = cut
        k = S.bit_count()
        if k <= half:
            r = Fr(cut, k)
            if best_h is None or r < best_h:
                best_h = r
        elif n - k <= half:
            r = Fr(cut, n - k)
            if best_h is None or r < best_h:
                best_h = r
    return best_h, m_edges - maxcut, m_edges


# ---------------- corpus --------------------------------------------

def corpus():
    out = []
    for name, cap in CAPS.items():
        for k in range(2, 7):
            out.append((f"ladder[{name},k={k}]", capped_ladder(k, cap)))
    for nn in range(5, 12):
        for kk in range(1, nn // 2 + (nn % 2)):
            if kk > nn // 2:
                continue
            out.append((f"GP({nn},{kk})", gp(nn, kk)))
    out.append(("Moebius8", moebius(8)))
    out.append(("Moebius10", moebius(10)))
    return out


def main():
    rows = []
    for name, A in corpus():
        t0 = time.time()
        v, cutused = verdict(A)
        h, f, m_edges = h_and_frustration(A)
        row = {"name": name, "n": len(A), "girth": girth(A),
               "bipartite": bipartite(A), "verdict": v,
               "adaptive_cut": cutused,
               "h_exact": str(h), "h_float": float(h),
               "frustration": f, "edges": m_edges,
               "f_over_m": float(Fr(f, m_edges))}
        rows.append(row)
        say(f"{name}: n={len(A)} verdict={v} h={h} f={f} "
            f"({time.time()-t0:.1f}s)")
    # class extremes
    classes = {}
    for r in rows:
        c = classes.setdefault(r["verdict"], {"h": [], "f": []})
        c["h"].append(Fr(r["h_exact"]))
        c["f"].append(Fr(r["frustration"], r["edges"]))
    summary = {v: {"h_min": str(min(c["h"])), "h_max": str(max(c["h"])),
                   "fm_min": str(min(c["f"])), "fm_max": str(max(c["f"])),
                   "count": len(c["h"])}
               for v, c in classes.items()}
    json.dump({"note": __doc__.strip().split("\n")[0],
               "rows": rows, "class_extremes": summary,
               "rh_established": False},
              open('graphs/phase_diagram.json', 'w'), indent=1)
    say("class extremes: " + json.dumps(summary))
    say("done")


if __name__ == "__main__":
    main()
