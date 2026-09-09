"""O-108517 sharpening — exhaustive frustration at the minimal
positive-end-only order.

The n = 16 census counts SPECTRA, so cospectral mates of the three
positive-end-only spectra (idx 706, 708, 709) could in principle be
different graphs with different frustration indices. This script
closes that gap: re-enumerate ALL Hamiltonian-cubic n = 16 chord
diagrams (dihedral dedup, as census16), keep EVERY canonical diagram
whose exact charpoly equals one of the three positive-only spectra
(cheap triangle/trace prefilter, then exact charpoly), and compute the
exact frustration index f = |E| - maxcut (exhaustive) and Cheeger
constant h (exhaustive) for each. Outcome decides, exhaustively at the
minimal order within the Hamiltonian-cubic scope: does every minimal
positive-end-only graph have f >= 3?

Exact integers throughout. Writes graphs/pos16_frustration.json.
rh_established = false.
"""
import json
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, '.')
sys.path.insert(0, 'graphs')
from core.exact import charpoly_of_matrix
from telescope import perfect_matchings, diagram_to_adj, canon_diagram

N = 16


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def load_targets():
    reps = json.load(open('graphs/witness16_reps.json'))
    tg = {}
    for idx in ('706', '708', '709'):
        tg[idx] = tuple(int(c) for c in reps[idx]['cp'])
    return tg


def invariants(A):
    """(#triangles, tr A^4) from bitmask adjacency."""
    masks = [sum(1 << j for j in range(N) if A[i][j]) for i in range(N)]
    tri = 0
    for u in range(N):
        for v in range(u + 1, N):
            if A[u][v]:
                tri += (masks[u] & masks[v]).bit_count()
    tri //= 3
    A2 = [[sum(A[i][t] * A[t][j] for t in range(N)) for j in range(N)]
          for i in range(N)]
    tr4 = sum(A2[i][j] * A2[j][i] for i in range(N) for j in range(N))
    return tri, tr4


def cp_invariants(cp):
    """triangles and tr A^4 from a charpoly (Newton power sums).
    cp[i] = coefficient of x^i, monic degree N."""
    e = [(-1) ** k * cp[N - k] for k in range(N + 1)]   # e_k
    p = [0] * 5
    p[1] = e[1]
    for k in range(2, 5):
        s = 0
        for i in range(1, k):
            s += (-1) ** (i - 1) * e[i] * p[k - i]
        s += (-1) ** (k - 1) * k * e[k]
        p[k] = s
    return p[3] // 6, p[4]


def h_and_f(A):
    masks = [sum(1 << j for j in range(N) if A[i][j]) for i in range(N)]
    full = (1 << N) - 1
    best_h = None
    maxcut = 0
    for S in range(1, 1 << (N - 1)):
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
        kk = min(k, N - k)
        r = Fr(cut, kk)
        if best_h is None or r < best_h:
            best_h = r
    return best_h, 24 - maxcut


def main():
    t0 = time.time()
    targets = load_targets()
    pre = {}
    for idx, cp in targets.items():
        pre[idx] = cp_invariants(list(cp))
        say(f"target {idx}: (triangles, trA4) = {pre[idx]}")
    prefset = set(pre.values())
    seen = set()
    matches = []
    cnt = 0
    surv = 0
    for m in perfect_matchings(list(range(N))):
        cnt += 1
        if cnt % 200000 == 0:
            say(f"  {cnt} diagrams, {len(seen)} canonical, "
                f"{surv} prefilter survivors, {len(matches)} matches "
                f"({time.time()-t0:.0f}s)")
        key = canon_diagram(N, m)
        if key in seen:
            continue
        seen.add(key)
        A = diagram_to_adj(N, m)
        if A is None:
            continue
        if invariants(A) not in prefset:
            continue
        surv += 1
        cp = tuple(charpoly_of_matrix(A))
        for idx, tcp in targets.items():
            if cp == tcp:
                h, f = h_and_f(A)
                matches.append({"spectrum_idx": idx,
                                "diagram": [list(p) for p in m],
                                "h": str(h), "frustration": f})
                say(f"  MATCH idx {idx}: f = {f}, h = {h} "
                    f"(canonical #{len(seen)})")
    fvals = sorted({r["frustration"] for r in matches})
    out = {"note": __doc__.strip().split("\n")[0],
           "diagrams_seen": cnt, "canonical": len(seen),
           "prefilter_survivors": surv,
           "matches": matches, "frustration_values": fvals,
           "conclusion_f_ge_3": bool(fvals and min(fvals) >= 3),
           "rh_established": False}
    json.dump(out, open('graphs/pos16_frustration.json', 'w'), indent=1)
    say(f"done: {len(matches)} matching graphs, f values {fvals} "
        f"({time.time()-t0:.0f}s)")


if __name__ == "__main__":
    main()
