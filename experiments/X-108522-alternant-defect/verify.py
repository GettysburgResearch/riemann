#!/usr/bin/env python3
"""X-108522: stdlib-exact replay for the alternant defect closed form
(standalone/2026-08-31-alternant-defect/PROOF.md).

Checks (EXACT_RATIONAL, standard library only):
  V1  Theorem A at exact integer points, d = 2..7: the alternant
      equals N_{2,d} computed by the independent Sym^2-weight route
      (h-series times det(1 - Sym^2 T), tail-certified window).
  V2  Lemma 2 (the (m-1)-fold partial-fraction series identity)
      coefficientwise r <= 12 at (m, d) = (3,2), (3,3), (4,2), (4,3),
      (5,2), (6,2).
  V3  the top-coefficient value (-1)^C(d-1,2) e_d^(d-1) at the V1
      points, d = 3..7 (numeric instance of the Corollary).

rh_established: false.
"""
import json
import os
from fractions import Fraction as Fr
from math import comb

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "ok": bool(ok), "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + (f": {detail}" if detail
                                                 and not ok else ""))


def poly_mul(P, Q):
    R = [0] * (len(P) + len(Q) - 1)
    for i, p in enumerate(P):
        if p:
            for j, q in enumerate(Q):
                R[i + j] += p * q
    return R


def h_seq_at(xv, n):
    d = len(xv)
    prod = [1]
    for x in xv:
        prod = poly_mul(prod, [1, x])
    e = prod
    h = [1]
    for r in range(1, n + 1):
        s = 0
        for k in range(1, min(r, d) + 1):
            s += (-1) ** (k + 1) * e[k] * h[r - k]
        h.append(s)
    return h


def alternant(xv, Tdeg):
    d = len(xv)
    tot = [Fr(0)] * (Tdeg + 1)
    for j in range(d):
        poly = [Fr(1)]
        for a in range(d):
            if a != j:
                poly = poly_mul(poly, [1, -xv[a] * xv[a]])
        for a in range(d):
            for b in range(a + 1, d):
                if a != j and b != j:
                    poly = poly_mul(poly, [1, -xv[a] * xv[b]])
        den = 1
        for a in range(d):
            if a != j:
                den *= (xv[j] - xv[a])
        c = Fr(xv[j] ** (d - 1), den)
        for i, v in enumerate(poly):
            if i <= Tdeg:
                tot[i] += c * v
    return tot


def sym2_route(xv, degN):
    d = len(xv)
    poly = [Fr(1)]
    for i in range(d):
        for j in range(i, d):
            poly = poly_mul(poly, [1, -Fr(xv[i] * xv[j])])
    h = h_seq_at(xv, degN + len(poly) + 6)
    N = []
    for r in range(degN + 4):
        s = Fr(0)
        for i in range(min(r, len(poly) - 1) + 1):
            s += poly[i] * h[r - i] ** 2
        N.append(s)
    return N


POINTS = {2: [(2, 3)], 3: [(1, 2, 3), (2, -1, 3)],
          4: [(1, 2, 3, 4), (2, -1, 3, -2)],
          5: [(1, 2, 3, 4, 5), (2, -1, 3, -2, 5)],
          6: [(1, 2, 3, 4, 5, 6)], 7: [(1, 2, 3, 4, 5, 6, 7)]}


def v1_v3():
    for d, pts in POINTS.items():
        degN = comb(d, 2)
        for xv in pts:
            alt = alternant(list(xv), degN)
            N = sym2_route(list(xv), degN)
            tail = all(v == 0 for v in N[degN + 1:])
            check(f"V1 d={d} {xv}",
                  tail and [Fr(v) for v in N[:degN + 1]] == alt)
            if d >= 3:
                ed = 1
                for x in xv:
                    ed *= x
                ref = Fr((-1) ** comb(d - 1, 2) * ed ** (d - 1))
                check(f"V3 top d={d} {xv}", alt[degN] == ref,
                      f"{alt[degN]} vs {ref}")


def v2():
    for m, xv in [(3, (2, 3)), (3, (1, 2, 3)), (4, (2, 3)),
                  (4, (1, 2, 3)), (5, (2, 3)), (6, (2, 3))]:
        d = len(xv)
        h = h_seq_at(list(xv), 14)
        ok = True
        idxs = [[]]
        for _ in range(m - 1):
            idxs = [i + [t] for i in idxs for t in range(d)]
        for r in range(13):
            rhs = Fr(0)
            for jv in idxs:
                w = 1
                num = 1
                den = 1
                for t in jv:
                    w *= xv[t]
                    num *= xv[t] ** (d - 1)
                    for a in range(d):
                        if a != t:
                            den *= (xv[t] - xv[a])
                rhs += Fr(num * w ** r * h[r], den)
            if rhs != Fr(h[r] ** m):
                ok = False
                break
        check(f"V2 series m={m} x={xv}", ok)


def main():
    v1_v3()
    v2()
    os.makedirs(os.path.join(os.path.dirname(__file__), "results"),
                exist_ok=True)
    allok = all(c["ok"] for c in CHECKS)
    with open(os.path.join(os.path.dirname(__file__), "results",
                           "verification.json"), "w") as f:
        json.dump({"experiment": "X-108522-alternant-defect",
                   "checks": CHECKS, "all_ok": allok,
                   "arithmetic_class": "EXACT_RATIONAL",
                   "rh_established": False}, f, indent=1)
    print("ALL OK" if allok else "FAILURES PRESENT")
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
