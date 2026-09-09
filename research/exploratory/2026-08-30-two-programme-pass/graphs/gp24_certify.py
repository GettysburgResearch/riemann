"""Certify GP(24,2) (48 vertices) as the atlas's first POSITIVE-END-ONLY
temperedness breach: lambda_2 > 2 sqrt 2 while lambda_min > -2 sqrt 2.
Exact route: integer charpoly (Faddeev-LeVerrier over Q), squares-poly
via tr(A^{2k}), Sturm counts with the (8, 8.0089] separation guard and
the (283/100, 3) / [-3, -283/100) side intervals, exactly as in
spectroscopy.py. Writes graphs/gp24_certificate.json.
rh_established = false.
"""
import json
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, '.')
sys.path.insert(0, 'graphs')
from core.exact import charpoly_of_matrix, count_real_roots_in, poly_eval
from telescope import gp, squares_poly, girth, diameter_and_connected, bipartite

R1 = Fr(283, 100)


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def main():
    t0 = time.time()
    A = gp(24, 2)
    say("charpoly of 48x48 ...")
    p = charpoly_of_matrix(A)
    say(f"charpoly done ({time.time()-t0:.0f}s); squares poly ...")
    p2 = squares_poly(A)
    say(f"squares poly done ({time.time()-t0:.0f}s); Sturm counts ...")
    n_unt = count_real_roots_in(p2, 8, 9)
    if poly_eval(p2, Fr(9)) == 0:
        n_unt -= 1
    guard = count_real_roots_in(p2, 8, R1 * R1)
    say(f"untempered squares in (8,9): {n_unt}; guard (8,8.0089]: {guard}")
    pos = count_real_roots_in(p, R1, 3)
    if poly_eval(p, Fr(3)) == 0:
        pos -= 1
    neg = count_real_roots_in(p, -3, -R1)
    if poly_eval(p, -R1) == 0:
        neg -= 1
    d_, conn = diameter_and_connected(A)
    out = {"graph": "GP(24,2)", "n": 48, "girth": girth(A),
           "diameter": d_, "connected": conn, "bipartite": bipartite(A),
           "untempered_squares": n_unt, "separation_guard_clean":
           guard == 0, "breach_pos": pos, "breach_neg": neg,
           "verdict": ("POSITIVE-END-ONLY breach" if guard == 0 and
                       pos > 0 and neg == 0 else "not positive-end-only"),
           "arithmetic_class": "EXACT_RATIONAL (Sturm)",
           "rh_established": False}
    say(f"pos={pos} neg={neg} -> {out['verdict']} ({time.time()-t0:.0f}s)")
    with open("graphs/gp24_certificate.json", "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
