"""C7 extension: n = 14 Hamiltonian-cubic census + breach-side hunt.

Question deposited by spectroscopy.json: in the n <= 12 atlas every
temperedness breach is at the NEGATIVE spectral end (near-bipartiteness),
never the positive end (expansion failure). Does a positive-end breach
(lambda_2 > 2 sqrt 2) occur at n = 14 at all — and if so, does any graph
breach ONLY at the positive end?

Enumeration: chord diagrams on C_14 (13!! = 135135 matchings), dihedral
dedup, then spectral + (girth, diameter, bipartite) class dedup as in
telescope.py n = 12 (same cospectral-merge caveat, same purity-safety:
purity and breach side are spectral invariants). Sturm-certified counts
of eigenvalues in (283/100, 3) and (-3, -283/100] per non-Ramanujan
class, with the (8, 8.0089] separation guard.

Writes graphs/census14.json. rh_established = false.
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

N = 14
R1 = Fr(283, 100)


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def main():
    t0 = time.time()
    seen, classes = set(), []
    cnt = 0
    for m in perfect_matchings(list(range(N))):
        cnt += 1
        if cnt % 20000 == 0:
            say(f"  {cnt} diagrams, {len(classes)} classes "
                f"({time.time()-t0:.0f}s)")
        key = canon_diagram(N, m)
        if key in seen:
            continue
        seen.add(key)
        A = diagram_to_adj(N, m)
        if A is None:
            continue
        cp = tuple(charpoly_of_matrix(A))
        dup = False
        for (cp2, inv2, _) in classes:
            if cp2 != cp:
                continue
            d2, _c = diameter_and_connected(A)
            if (girth(A), d2, bipartite(A)) == inv2:
                dup = True
                break
        if not dup:
            d_, _c = diameter_and_connected(A)
            classes.append((cp, (girth(A), d_, bipartite(A)), A))
    say(f"n=14: {len(classes)} Hamiltonian cubic classes "
        f"(spectral+invariant dedup) in {time.time()-t0:.0f}s")

    rows = []
    n_ram = 0
    breach = {"neg_only": 0, "pos_only": 0, "both": 0}
    flagged = []
    for i, (cp, inv, A) in enumerate(classes):
        ram, nunt = purity_certificate(A)
        row = {"name": f"ham_cubic_n14_{i}", "girth": inv[0],
               "diameter": inv[1], "bipartite": inv[2],
               "ramanujan": ram, "untempered_squares": nunt}
        if not ram:
            p = charpoly_of_matrix(A)
            p2 = squares_poly(A)
            if count_real_roots_in(p2, 8, R1 * R1) != 0:
                flagged.append(row["name"])
                row["flag"] = "square in (8, 8.0089]"
            else:
                pos = count_real_roots_in(p, R1, 3)
                if poly_eval(p, Fr(3)) == 0:
                    pos -= 1
                neg = count_real_roots_in(p, -3, -R1)
                if poly_eval(p, -R1) == 0:
                    neg -= 1
                row["breach_pos"], row["breach_neg"] = pos, neg
                k = ("both" if pos and neg else
                     "pos_only" if pos else "neg_only")
                breach[k] += 1
        else:
            n_ram += 1
        rows.append(row)
    say(f"Ramanujan {n_ram}/{len(rows)}; breach sides {breach}; "
        f"flagged {flagged}")
    with open("graphs/census14.json", "w") as f:
        json.dump({"scope_note": ("Hamiltonian cubic n=14 via chord "
                                  "diagrams, spectral+invariant dedup "
                                  "(cospectral-mate merge possible; "
                                  "purity/breach side are spectral, "
                                  "class count could undercount)"),
                   "n_classes": len(rows), "n_ramanujan": n_ram,
                   "breach_sides": breach, "flagged": flagged,
                   "rows": rows, "rh_established": False}, f, indent=1)
    say("C7-14 done")


if __name__ == "__main__":
    main()
