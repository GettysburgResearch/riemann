"""The ALTERNANT CLOSED FORM for defect numerators (T-108522 machine
layer).

Core identity (divided differences / partial fractions; proof in the
standalone file): for distinct x_1..x_d and every r >= 0,

  (I)   h_r(x)^m = sum over (j_1..j_{m-1}) in [d]^{m-1} of
        prod_t x_{j_t}^{d-1+ ...}: concretely
        sum_r h_r(x)^m T^r
          = sum_{jvec} [prod_t x_{j_t}^{d-1}]
            / [ prod_i (1 - T x_i prod_t x_{j_t})
                * prod_t prod_{a != j_t} (x_{j_t} - x_a) ] .

Consequences verified here:
  (II)  m = 2: N_{2,d}(T) = sum_j x_j^{d-1} prod_{a != j}(1 - x_a^2 T)
        * prod_{a<b, a,b != j}(1 - x_a x_b T) / prod_{a != j}(x_j - x_a)
        — THE GENERAL-RANK SQUARE DEFECT IN CLOSED FORM (the open
        problem of T-108508).
  (III) the T-108510 top-coefficient law c_top = (-1)^C(d-1,2) e_d^(d-1)
        drops out of (II).

Checks:
  A1  (II) == G_3 (d=3) and == the PROVED T-108508 closed forms at
      d = 4 (symbolic, sympy).
  A2  (II) == the matrix-route N_{2,d} (companion + Sym^2 +
      Faddeev-LeVerrier + h-series) at exact integer points for
      d = 5, 6, 7 (Fractions; the proof is the derivation — these are
      corroboration at ranks beyond all previous closed forms).
  A3  (I) coefficientwise at exact integer points: (m,d) = (3,2),
      (3,3), (4,2), (4,3), (5,2), r <= 12.
  A4  (III): top coefficient of (II) symbolically for d = 3, 4, 5.

rh_established = false.
"""
import json
import sys
import time
from fractions import Fraction as Fr
from itertools import combinations
from math import comb

import sympy as sp

sys.path.insert(0, '.')


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "ok": bool(ok), "detail": str(detail)})
    say(("PASS " if ok else "FAIL ") + name)


# ---------------- symbolic layer ------------------------------------

def alternant_m2(xs, T):
    d = len(xs)
    tot = 0
    for j in range(d):
        num = xs[j] ** (d - 1)
        for a in range(d):
            if a != j:
                num *= (1 - xs[a] ** 2 * T)
        for a in range(d):
            for b in range(a + 1, d):
                if a != j and b != j:
                    num *= (1 - xs[a] * xs[b] * T)
        den = 1
        for a in range(d):
            if a != j:
                den *= (xs[j] - xs[a])
        tot += num / den
    return sp.cancel(sp.together(tot))


def gauss_G(xs, T, d):
    """G_d = sum_j (-1)^{j(j-1)/2} e_j(Lambda^2) T^j."""
    lam = [xs[i] * xs[j] for i in range(d) for j in range(i + 1, d)]
    prod = sp.Integer(1)
    for w in lam:
        prod = sp.expand(prod * (1 + w * T))
    G = 0
    for j in range(len(lam) + 1):
        G += sp.Integer(-1) ** (j * (j - 1) // 2) * prod.coeff(T, j) * T ** j
    return sp.expand(G)


def a1():
    T = sp.symbols('T')
    # d = 3
    xs = sp.symbols('x1:4')
    alt = alternant_m2(list(xs), T)
    check("A1 d=3 alternant == G_3",
          sp.expand(alt - gauss_G(list(xs), T, 3)) == 0)
    # d = 4: G_4 + 2 e4 h2 T^3 - 2 e4^2 e2 T^5
    xs = sp.symbols('x1:5')
    alt = alternant_m2(list(xs), T)
    e = [sp.Integer(1)]
    prod = sp.Integer(1)
    for x in xs:
        prod = sp.expand(prod * (1 + x * T))
    e = [prod.coeff(T, j) for j in range(5)]
    h2 = sp.expand(e[1] ** 2 - e[2])
    ref = sp.expand(gauss_G(list(xs), T, 4)
                    + 2 * e[4] * h2 * T ** 3
                    - 2 * e[4] ** 2 * e[2] * T ** 5)
    check("A1 d=4 alternant == T-108508 closed form",
          sp.expand(alt - ref) == 0)


def a4():
    T = sp.symbols('T')
    for d in (3, 4, 5):
        xs = list(sp.symbols(f'x1:{d+1}'))
        alt = sp.expand(alternant_m2(xs, T))
        top = alt.coeff(T, d * (d - 1) // 2)
        ed = sp.prod(xs)
        ref = sp.Integer(-1) ** comb(d - 1, 2) * ed ** (d - 1)
        check(f"A4 d={d} top coefficient law",
              sp.expand(top - ref) == 0)


# ---------------- exact integer layer -------------------------------

def alternant_m2_at(xv, Tdeg):
    """coefficients of (II) as exact Fractions at integer point xv."""
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


def poly_mul(P, Q):
    R = [0] * (len(P) + len(Q) - 1)
    for i, p in enumerate(P):
        if p:
            for jj, q in enumerate(Q):
                R[i + jj] += p * q
    return R


def h_seq_at(xv, n):
    """h_r(xv) via Newton's identity from elementary symmetrics."""
    d = len(xv)
    e = [1]
    prod = [1]
    for x in xv:
        prod = poly_mul(prod, [1, x])
    e = prod[:]                       # e[k] with sign: prod = sum e_k T^k
    h = [1]
    for r in range(1, n + 1):
        s = 0
        for k in range(1, min(r, d) + 1):
            s += (-1) ** (k + 1) * e[k] * h[r - k]
        h.append(s)
    return h


def sym2_det_at(xv, Tdeg):
    """det(1 - Sym^2 T) coefficients at the point: weights x_i x_j."""
    d = len(xv)
    poly = [Fr(1)]
    for i in range(d):
        for j in range(i, d):
            poly = poly_mul(poly, [1, -xv[i] * xv[j]])
    return poly[:Tdeg + 1]


def a2():
    pts = {5: [(1, 2, 3, 4, 5), (2, -1, 3, -2, 5)],
           6: [(1, 2, 3, 4, 5, 6), (2, -1, 3, -2, 5, 7)],
           7: [(1, 2, 3, 4, 5, 6, 7)]}
    for d, xs in pts.items():
        degN = comb(d, 2)
        for xv in xs:
            alt = alternant_m2_at(list(xv), degN)
            h = h_seq_at(list(xv), degN + comb(d + 1, 2) + 6)
            Q = sym2_det_at(list(xv), comb(d + 1, 2))
            N = []
            for r in range(degN + 4):
                s = Fr(0)
                for i in range(min(r, len(Q) - 1) + 1):
                    s += Q[i] * h[r - i] ** 2
                N.append(s)
            tail = all(v == 0 for v in N[degN + 1:])
            check(f"A2 d={d} point {xv}",
                  tail and [Fr(v) for v in N[:degN + 1]] == alt,
                  f"N={N[:degN+1]} alt={alt}")


def a3():
    cases = [(3, (2, 3)), (3, (1, 2, 3)), (4, (2, 3)), (4, (1, 2, 3)),
             (5, (2, 3))]
    for m, xv in cases:
        d = len(xv)
        h = h_seq_at(list(xv), 14)
        ok = True
        for r in range(13):
            lhs = Fr(h[r] ** m)
            rhs = Fr(0)
            # sum over jvec in [d]^{m-1}
            idxs = [[]]
            for _ in range(m - 1):
                idxs = [i + [t] for i in idxs for t in range(d)]
            for jv in idxs:
                w = 1
                for t in jv:
                    w *= xv[t]
                num = 1
                den = 1
                for t in jv:
                    num *= xv[t] ** (d - 1)
                    for a in range(d):
                        if a != t:
                            den *= (xv[t] - xv[a])
                # coefficient of T^r in prod_i (1 - T x_i w)^{-1}
                #   = h_r(x_1 w, ..., x_d w) = w^r h_r(x)
                rhs += Fr(num * w ** r * h[r], den)
            if lhs != rhs:
                ok = False
                break
        check(f"A3 series identity m={m} x={xv}", ok)


def main():
    a1()
    a4()
    a2()
    a3()
    allok = all(c["ok"] for c in CHECKS)
    json.dump({"checks": CHECKS, "all_ok": allok,
               "rh_established": False},
              open('matrix/alternant_defect.json', 'w'), indent=1)
    say("ALL OK" if allok else "FAILURES PRESENT")


if __name__ == "__main__":
    main()
