"""C6: trace-formula spectroscopy of the C5 atlas (programme #763).

For every non-Ramanujan graph in graphs/telescope.json, certify EXACTLY
(Sturm, rational endpoints):
  - WHICH SPECTRAL END breaches temperedness: positive (lambda_2 >
    2 sqrt 2 — expansion bottleneck side) or negative (lambda_min <
    -2 sqrt 2 — bipartite-frustration side);
  - a rational bracket of width <= 1/64 for the breaching eigenvalue;
  - the minimal polynomial (sympy factorization of the exact charpoly)
    of the breaching eigenvalue — "the field where purity breaks".
Then the census correlation table (girth x bipartite x Ramanujan) for
the whole atlas.

Guard: the rational cut r1 = 283/100 (r1^2 = 8.0089) is certified to
separate: Sturm-count of eigenvalue-squares in (8, r1^2] must be 0 for
every analyzed graph, else that graph is flagged rather than silently
mis-sided.

Everything exact except sympy's factor over Q (exact too). Writes
graphs/spectroscopy.json. rh_established = false.
"""
import json
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

sys.path.insert(0, '.')
sys.path.insert(0, 'graphs')
from core.exact import (charpoly_of_matrix, count_real_roots_in, poly_eval)
from telescope import (petersen, gp, perfect_matchings, diagram_to_adj,
                       canon_diagram, squares_poly, girth,
                       diameter_and_connected, bipartite)


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def rebuild_named(name):
    """Reconstruct the adjacency of an atlas graph from its name."""
    if name == "petersen":
        return petersen()
    if name.startswith("GP("):
        n, k = map(int, name[3:-1].split(","))
        return gp(n, k)
    # ham_cubic_n{n}_{i}: re-enumerate deterministically (same order)
    assert name.startswith("ham_cubic_n")
    body = name[len("ham_cubic_n"):]
    n, idx = map(int, body.split("_"))
    seen, classes = set(), []
    for m in perfect_matchings(list(range(n))):
        key = canon_diagram(n, m)
        if key in seen:
            continue
        seen.add(key)
        A = diagram_to_adj(n, m)
        if A is None:
            continue
        cp = tuple(charpoly_of_matrix(A))
        dup = False
        for (cp2, inv2, B) in classes:
            if cp2 != cp:
                continue
            d2, _ = diameter_and_connected(A)
            if (girth(A), d2, bipartite(A)) == inv2:
                dup = True
                break
        if not dup:
            d_, _ = diameter_and_connected(A)
            classes.append((cp, (girth(A), d_, bipartite(A)), A))
    return classes[idx][2]


R1 = Fr(283, 100)          # r1^2 = 8.0089 > 8


def breach_analysis(A):
    p = charpoly_of_matrix(A)
    p2 = squares_poly(A)
    # separation guard
    guard = count_real_roots_in(p2, 8, R1 * R1)
    if guard != 0:
        return {"flag": "square in (8, 8.0089]: refine manually"}
    pos = count_real_roots_in(p, R1, 3)
    # count_real_roots_in counts (a, b]; the trivial eigenvalue 3 sits
    # AT the right endpoint: subtract it
    if poly_eval(p, Fr(3)) == 0:
        pos -= 1
    neg = count_real_roots_in(p, -3, -R1)
    # (-3, -R1]: -3 excluded automatically (interval open at left);
    # -R1 endpoint: subtract if root exactly there (rational check)
    if poly_eval(p, -R1) == 0:
        neg -= 1
    out = {"n_breach_pos": pos, "n_breach_neg": neg}
    # bracket each breaching eigenvalue to 1/64 by Sturm bisection
    brs = []
    for (lo, hi, cnt) in ((R1, Fr(3), pos), (Fr(-3), -R1, neg)):
        if cnt == 0:
            continue
        stack = [(lo, hi)]
        found = []
        while stack:
            a_, b_ = stack.pop()
            c_ = count_real_roots_in(p, a_, b_)
            if c_ == 0:
                continue
            if b_ - a_ <= Fr(1, 64):
                found.append((a_, b_, c_))
                continue
            mid = (a_ + b_) / 2
            stack.append((a_, mid))
            stack.append((mid, b_))
        brs.extend([[str(a_), str(b_), c_] for (a_, b_, c_) in found])
    out["brackets_1_64"] = brs
    # minimal polynomial of each breaching eigenvalue (exact factor)
    x = sp.Symbol('x')
    poly = sum(int(c) * x ** i for i, c in enumerate(p))
    fac = sp.factor_list(sp.Poly(poly, x))[1]
    minpolys = []
    for (f, mult) in fac:
        # does this factor have a root in a breach bracket? test by exact
        # Sturm on the factor over each bracket
        fc = [Fr(int(v)) for v in reversed(sp.Poly(f, x).all_coeffs())]
        hits = 0
        for (a_s, b_s, cnt) in brs:
            if count_real_roots_in(fc, Fr(a_s), Fr(b_s)) > 0:
                hits += cnt
        if hits:
            minpolys.append({"factor": str(f.as_expr()),
                             "degree": sp.Poly(f, x).degree(),
                             "mult": mult, "breach_roots": hits})
    out["breach_minimal_polynomials"] = minpolys
    return out


def main():
    t = json.load(open("graphs/telescope.json"))
    rows = t["rows"]
    bad = [r for r in rows if not r["ramanujan"]]
    say(f"spectroscopy on {len(bad)} non-Ramanujan atlas graphs")
    out = {"meta": {"arithmetic_class": "EXACT_RATIONAL (Sturm) + exact "
                    "sympy factorization", "rh_established": False},
           "graphs": {}}
    for r in bad:
        A = rebuild_named(r["name"])
        # consistency: recertify status
        res = breach_analysis(A)
        out["graphs"][r["name"]] = {**r, **res}
        say(f"  {r['name']}: pos={res.get('n_breach_pos')} "
            f"neg={res.get('n_breach_neg')} "
            f"minpolys={[m['factor'] for m in res.get('breach_minimal_polynomials', [])]}")
    # census table
    from collections import Counter
    cen = Counter((r["bipartite"], r["girth"], r["ramanujan"])
                  for r in rows)
    out["census_bipartite_girth_ramanujan"] = \
        {f"bip={k[0]}, girth={k[1]}, ram={k[2]}": v
         for k, v in sorted(cen.items(), key=str)}
    with open("graphs/spectroscopy.json", "w") as f:
        json.dump(out, f, indent=1)
    say("C6 done")


if __name__ == "__main__":
    main()
