"""Extract and fully certify the n = 16 positive-end-only witnesses
(census16 idx 708, 709) and resolve the 18 guard-flagged spectra with
ADAPTIVE rational cuts: isolate each near-8 eigenvalue-square by Sturm
bisection to (q1, q2] with q1 > 8, pick a rational r with
8 < r^2 <= q1 (exact check), and count charpoly roots in (r, 3] and
[-3, -r) with endpoint corrections. Writes graphs/witness16.json.
rh_established = false.
"""
import json
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, '.')
sys.path.insert(0, 'graphs')
from core.exact import charpoly_of_matrix, count_real_roots_in, poly_eval
from telescope import (perfect_matchings, diagram_to_adj, canon_diagram,
                       squares_poly, girth, diameter_and_connected,
                       bipartite)

N = 16
R1 = Fr(283, 100)
TARGETS = {708, 709, 41, 107, 640, 706, 707, 1288, 1608, 1928, 1940,
           2310, 2509, 3093, 3268, 3278, 3280, 3301, 3337, 3355}
POS_ONLY = {708, 709}


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def isolate_and_cut(p2):
    """Return rational r with 8 < r^2 <= (smallest squares-root > 8),
    via Sturm bisection of the smallest root of p2 in (8, 9]."""
    lo, hi = Fr(8), Fr(9)
    # bisect until the interval (lo, hi] contains >= 1 root and
    # (8, lo] contains none and hi - lo is tiny
    for _ in range(40):
        mid = (lo + hi) / 2
        if count_real_roots_in(p2, Fr(8), mid) >= 1:
            hi = mid
        else:
            lo = mid
        if hi - lo < Fr(1, 10 ** 7):
            break
    # smallest root s* in (lo, hi]; need r with 8 < r^2 <= lo
    # (then no square lies in (8, r^2], so sides split cleanly at r)
    assert lo > 8
    # rational sqrt approx of (8 + lo)/2 from below/above
    target = (8 + lo) / 2
    # float-seeded rational approximation of sqrt(target), then exact
    # adjustment into (sqrt 8, sqrt lo]
    import math
    r = Fr(math.sqrt(float(target))).limit_denominator(10 ** 9)
    step = Fr(1, 10 ** 10)
    while r * r <= 8:
        r += step
    while r * r > lo:
        r -= step
    assert 8 < r * r <= lo, "cut adjustment failed"
    return r


def sides_adaptive(p, p2):
    if count_real_roots_in(p2, 8, R1 * R1) == 0:
        r = R1
    else:
        r = isolate_and_cut(p2)
    pos = count_real_roots_in(p, r, 3)
    if poly_eval(p, Fr(3)) == 0:
        pos -= 1
    neg = count_real_roots_in(p, -3, -r)
    if poly_eval(p, -r) == 0:
        neg -= 1
    return pos, neg, r


def main():
    import os
    if os.path.exists("graphs/witness16_reps.json"):
        with open("graphs/witness16_reps.json") as f:
            raw = json.load(f)
        reps = {int(i): (v["A"], tuple(Fr(c) for c in v["cp"]))
                for i, v in raw.items()}
        say(f"loaded {len(reps)} cached representatives")
        certify(reps)
        return
    seen = set()
    by_cp = {}
    idx = 0
    reps = {}
    for m in perfect_matchings(list(range(N))):
        key = canon_diagram(N, m)
        if key in seen:
            continue
        seen.add(key)
        A = diagram_to_adj(N, m)
        if A is None:
            continue
        cp = tuple(charpoly_of_matrix(A))
        if cp not in by_cp:
            by_cp[cp] = idx
            if idx in TARGETS:
                reps[idx] = (A, cp)
            idx += 1
    say(f"re-enumerated: {idx} spectra; extracted {len(reps)} targets")
    with open("graphs/witness16_reps.json", "w") as f:
        json.dump({str(i): {"A": A, "cp": [str(c) for c in cp]}
                   for i, (A, cp) in reps.items()}, f)
    certify(reps)


def certify(reps):
    out = {"witnesses": {}, "flagged_resolved": {},
           "arithmetic_class": "EXACT_RATIONAL (adaptive Sturm cuts)",
           "rh_established": False}
    tally = {"neg_only": 0, "pos_only": 0, "both": 0}
    for i, (A, cp) in sorted(reps.items()):
        p = list(cp)
        p2 = squares_poly(A)
        pos, neg, r = sides_adaptive(p, p2)
        d_, _c = diameter_and_connected(A)
        rec = {"idx": i, "breach_pos": pos, "breach_neg": neg,
               "cut_r": str(r), "girth": girth(A), "diameter": d_,
               "bipartite": bipartite(A)}
        k = ("both" if pos and neg else "pos_only" if pos
             else "neg_only")
        if i in POS_ONLY:
            rec["adjacency"] = A
            rec["charpoly"] = [str(c) for c in p]
            out["witnesses"][str(i)] = rec
        else:
            tally[k] += 1
            out["flagged_resolved"][str(i)] = rec
        say(f"idx {i}: pos={pos} neg={neg} girth={rec['girth']} "
            f"{'WITNESS' if i in POS_ONLY else k}")
    out["flagged_tally"] = tally
    with open("graphs/witness16.json", "w") as f:
        json.dump(out, f, indent=1)
    say(f"done; flagged tally {tally}")


if __name__ == "__main__":
    main()
