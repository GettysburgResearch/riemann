"""WITNESS16_STRUCTURE deposited question — non-diamond heads.

The minimal positive-end-only graphs are DIAMOND-headed capped
ladders. Do 6-vertex heads (the same five simple-graph-valid 3-chord
matchings that classify the caps) also open positive-only windows?

Frame: Hamiltonian cycle 0..n-1, n = 2k + 12; HEAD chords = a valid
matching on positions {0..5}; corridor rungs (6+j, n-1-j), j < k;
CAP chords = a valid matching on the far six positions (base 6+k).
All 5 x 5 head/cap pairs, corridor k = 2..6 (n = 16..24), verdicts
Sturm-exact via the phase_diagram machinery (adaptive cuts on guard
flags); Cheeger h and frustration f exhaustive for n <= 22 (feeds the
O-108517 diagram). Charpoly-keyed dedup (mirror/reversal pairs merge;
cospectral-mate caveat as in the census).

Exact throughout. Writes graphs/head_cap_atlas.json.
rh_established = false.
"""
import json
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, '.')
sys.path.insert(0, 'graphs')
from core.exact import charpoly_of_matrix
from telescope import girth, bipartite
from phase_diagram import verdict, h_and_frustration

# the five simple-graph-valid 3-chord matchings on six cycle-consecutive
# positions (from the cap-window analysis):
VALID = {
    "s708": ((0, 3), (1, 5), (2, 4)),
    "s709": ((0, 5), (1, 3), (2, 4)),
    "s706": ((0, 2), (1, 4), (3, 5)),
    "cross": ((0, 3), (1, 4), (2, 5)),
    "m708": ((0, 4), (1, 3), (2, 5)),
}


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def build(k, head, cap):
    n = 2 * k + 12
    E = {(i, (i + 1) % n) for i in range(n)}
    for (r, s) in head:
        E.add((min(r, s), max(r, s)))
    for j in range(k):
        E.add((6 + j, n - 1 - j))
    base = 6 + k
    for (r, s) in cap:
        E.add((base + min(r, s), base + max(r, s)))
    A = [[0] * n for _ in range(n)]
    for (i, j) in E:
        if A[i][j]:
            return None
        A[i][j] = A[j][i] = 1
    if not all(sum(row) == 3 for row in A):
        return None
    return A


def main():
    t0 = time.time()
    rows = []
    seen_cp = {}
    for hname, head in VALID.items():
        for cname, cap in VALID.items():
            for k in range(2, 7):
                A = build(k, head, cap)
                if A is None:
                    say(f"invalid: {hname}/{cname} k={k}")
                    continue
                n = len(A)
                cp = tuple(charpoly_of_matrix(A))
                if cp in seen_cp:
                    seen_cp[cp].append(f"{hname}/{cname}/k{k}")
                    continue
                seen_cp[cp] = [f"{hname}/{cname}/k{k}"]
                v, cut = verdict(A)
                row = {"head": hname, "cap": cname, "k": k, "n": n,
                       "verdict": v, "adaptive_cut": cut,
                       "girth": girth(A), "bipartite": bipartite(A)}
                if n <= 22:
                    h, f, m_edges = h_and_frustration(A)
                    row.update({"h": str(h), "frustration": f,
                                "edges": m_edges})
                rows.append(row)
                say(f"{hname}/{cname} k={k} (n={n}): {v}"
                    + (f", h={row.get('h')}, f={row.get('frustration')}"
                       if n <= 22 else "")
                    + f" ({time.time()-t0:.0f}s)")
    # summary: which head/cap pairs ever go positive-end-only?
    pos_pairs = sorted({(r["head"], r["cap"]) for r in rows
                        if r["verdict"] == "POS"})
    verd_seq = {}
    for r in rows:
        verd_seq.setdefault(f"{r['head']}/{r['cap']}", {})[r["k"]] = \
            r["verdict"]
    out = {"note": __doc__.strip().split("\n")[0],
           "rows": rows,
           "cospectral_merges": {str(v[0]): v[1:] for v in
                                 seen_cp.values() if len(v) > 1},
           "positive_only_pairs": [list(p) for p in pos_pairs],
           "verdict_sequences": verd_seq,
           "rh_established": False}
    json.dump(out, open('graphs/head_cap_atlas.json', 'w'), indent=1)
    say(f"done: {len(rows)} rows; POS pairs: {pos_pairs}")


if __name__ == "__main__":
    main()
