"""Certify the double-Petersen dumbbell DP20 (two copies of Petersen
minus an edge, the four degree-2 vertices rejoined pairwise across:
u1-u2, v1-v2) as a POSITIVE-END-ONLY temperedness breach on 20
vertices — improving the positive-end existence witness from 48
(GP(24,2)) to 20 and the minimal-order bracket to (14, 20].
Exact route as in gp24_certify.py. Writes graphs/dp20_certificate.json.
rh_established = false.
"""
import json
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, '.')
sys.path.insert(0, 'graphs')
from core.exact import charpoly_of_matrix, count_real_roots_in, poly_eval
from telescope import squares_poly, girth, diameter_and_connected, bipartite

R1 = Fr(283, 100)


def dp20():
    E = set()
    for i in range(5):
        E |= {(i, (i + 1) % 5), (i + 5, (i + 2) % 5 + 5), (i, i + 5)}
    P = [[0] * 10 for _ in range(10)]
    for (i, j) in E:
        P[i][j] = P[j][i] = 1
    P[0][1] = P[1][0] = 0                  # remove outer edge (0,1)
    A = [[0] * 20 for _ in range(20)]
    for i in range(10):
        for j in range(10):
            A[i][j] = P[i][j]
            A[10 + i][10 + j] = P[i][j]
    A[0][10] = A[10][0] = 1                # u1 - u2
    A[1][11] = A[11][1] = 1                # v1 - v2
    return A


def main():
    t0 = time.time()
    A = dp20()
    assert all(sum(r) == 3 for r in A)
    p = charpoly_of_matrix(A)
    p2 = squares_poly(A)
    n_unt = count_real_roots_in(p2, 8, 9)
    if poly_eval(p2, Fr(9)) == 0:
        n_unt -= 1
    guard = count_real_roots_in(p2, 8, R1 * R1)
    pos = count_real_roots_in(p, R1, 3)
    if poly_eval(p, Fr(3)) == 0:
        pos -= 1
    neg = count_real_roots_in(p, -3, -R1)
    if poly_eval(p, -R1) == 0:
        neg -= 1
    d_, conn = diameter_and_connected(A)
    out = {"graph": "DP20 = dumbbell(Petersen - e, uncrossed)",
           "n": 20, "girth": girth(A), "diameter": d_,
           "connected": conn, "bipartite": bipartite(A),
           "untempered_squares": n_unt,
           "separation_guard_clean": guard == 0,
           "breach_pos": pos, "breach_neg": neg,
           "verdict": ("POSITIVE-END-ONLY breach" if guard == 0 and
                       pos > 0 and neg == 0 else "NOT positive-end-only"),
           "charpoly": [str(c) for c in p],
           "arithmetic_class": "EXACT_RATIONAL (Sturm)",
           "rh_established": False}
    print(f"unt={n_unt} guard={guard} pos={pos} neg={neg} -> "
          f"{out['verdict']} ({time.time()-t0:.0f}s)")
    with open("graphs/dp20_certificate.json", "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
