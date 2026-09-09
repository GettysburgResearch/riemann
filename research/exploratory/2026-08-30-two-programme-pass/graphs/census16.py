"""n = 16 Hamiltonian-cubic SPECTRAL census with breach sides — either
finds a positive-end-only breach below 48 vertices or extends the
negative-end law to n = 16.

Design (v2; v1's per-diagram class scan was too slow): purity, the
untempered count, and the breach side are SPECTRAL invariants, so the
census needs only the DISTINCT CHARACTERISTIC POLYNOMIALS. Enumerate
chord diagrams with dihedral dedup, compute the charpoly once per new
canonical diagram, and group by charpoly (keeping one representative
adjacency). Certify once per distinct spectrum. The distinct-charpoly
count is an UPPER-BOUND grouping of isomorphism classes (cospectral
mates merge; iso-duplicates with different canonical keys cost time but
not correctness). girth/diameter recorded for non-Ramanujan
representatives only. Checkpoints hourly. Writes graphs/census16.json.
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
                       bipartite, purity_certificate)

N = 16
R1 = Fr(283, 100)


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def main():
    t0 = time.time()
    seen = set()
    by_cp = {}
    cnt = 0
    for m in perfect_matchings(list(range(N))):
        cnt += 1
        if cnt % 200000 == 0:
            say(f"  {cnt} diagrams, {len(seen)} canonical, "
                f"{len(by_cp)} spectra ({time.time()-t0:.0f}s)")
        key = canon_diagram(N, m)
        if key in seen:
            continue
        seen.add(key)
        A = diagram_to_adj(N, m)
        if A is None:
            continue
        cp = tuple(charpoly_of_matrix(A))
        if cp not in by_cp:
            by_cp[cp] = A
    say(f"n=16: {len(by_cp)} distinct spectra "
        f"({len(seen)} canonical diagrams) in {time.time()-t0:.0f}s")

    n_ram = 0
    breach = {"neg_only": 0, "pos_only": 0, "both": 0}
    flagged = []
    nonram_rows = []
    pos_only = []
    for i, (cp, A) in enumerate(by_cp.items()):
        ram, nunt = purity_certificate(A)
        if ram:
            n_ram += 1
        else:
            p = list(cp)
            p2 = squares_poly(A)
            row = {"idx": i, "untempered_squares": nunt}
            if count_real_roots_in(p2, 8, R1 * R1) != 0:
                flagged.append(i)
                row["flag"] = "square in (8, 8.0089]"
            else:
                pos = count_real_roots_in(p, R1, 3)
                if poly_eval(p, Fr(3)) == 0:
                    pos -= 1
                neg = count_real_roots_in(p, -3, -R1)
                if poly_eval(p, -R1) == 0:
                    neg -= 1
                d_, _c = diameter_and_connected(A)
                row.update({"breach_pos": pos, "breach_neg": neg,
                            "girth": girth(A), "diameter": d_,
                            "bipartite": bipartite(A)})
                k = ("both" if pos and neg else
                     "pos_only" if pos else "neg_only")
                breach[k] += 1
                if k == "pos_only":
                    pos_only.append(i)
                    say(f"POSITIVE-END-ONLY spectrum at n=16: idx {i}")
            nonram_rows.append(row)
        if i and i % 1000 == 0:
            say(f"  certified {i}/{len(by_cp)} "
                f"(nonram {len(nonram_rows)}) ({time.time()-t0:.0f}s)")
    say(f"Ramanujan {n_ram}/{len(by_cp)} spectra; breach {breach}; "
        f"flagged {flagged}; pos_only {pos_only}")
    with open("graphs/census16.json", "w") as f:
        json.dump({"scope_note": ("Hamiltonian cubic n=16 by DISTINCT "
                                  "SPECTRUM (chord diagrams, dihedral "
                                  "dedup, charpoly grouping): purity/"
                                  "side verdicts exact per spectrum; "
                                  "cospectral iso-classes merge — "
                                  "counts are of spectra, not graphs"),
                   "n_spectra": len(by_cp), "n_ramanujan": n_ram,
                   "breach_sides": breach, "flagged": flagged,
                   "pos_only": pos_only,
                   "nonramanujan_rows": nonram_rows,
                   "rh_established": False}, f, indent=1)
    say("census16 done")


if __name__ == "__main__":
    main()
