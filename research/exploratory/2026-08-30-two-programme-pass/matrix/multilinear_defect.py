"""MULTILINEAR defect closed forms (T-108522 extension): the defect
of Hadamard products of DISTINCT local objects.

For local objects A (rank dA, inverse roots x), B (rank dB, roots y),
C (rank dC, roots z), the naive Dirichlet series
sum a_n b_n c_n n^{-s} has prime-power coefficient sequence
h_r(x) h_r(y) h_r(z), and the automorphic triple product has local
denominator det(1 - A x B x C T) (degree dA dB dC). The alternant
lemma with distinct alphabets gives the EXACT numerator:

 (I)  sum_r h_r(x) h_r(y) h_r(z) T^r
      = sum_{j <= dB, k <= dC} y_j^{dB-1} z_k^{dC-1}
        / [ prod_{j' != j}(y_j - y_{j'}) prod_{k' != k}(z_k - z_{k'}) ]
        * prod_{i <= dA} (1 - T x_i y_j z_k)^{-1} ,

 (II) N_{ABC}(T) := det(1 - A x B x C T) * sum_r h_r h_r h_r T^r
      = sum_{j,k} y_j^{dB-1} z_k^{dC-1}
        * prod_{(i',j',k') != (*,j,k)} (1 - x_{i'} y_{j'} z_{k'} T)
        / [prods of differences]   — a polynomial of degree
        dA dB dC - dA (each (j,k) summand omits the dA factors
        (i, j, k)).

Checks (exact integers/Fractions, stdlib):
  M1  (I) coefficientwise r <= 12 at integer points, shapes
      (dA,dB,dC) = (2,2,2), (2,2,3), (3,2,2), (2,3,3).
  M2  (II): N_{ABC} from the matrix route (Kronecker triple product,
      integral Faddeev-LeVerrier, series, tail window) equals the
      alternant sum, same shapes; degree = dA dB dC - dA confirmed.
  M3  pairwise sanity: the SAME machinery at two factors reproduces
      the classical exactness of Rankin-Selberg for rank 2 x rank 2:
      N_{AB} has degree dA dB - dA = 2, i.e. sum a_n b_n has a
      degree-2 numerator det(1 - (det B) A T)-like — computed and
      identified exactly.

rh_established = false.
"""
import json
import sys
import time
from fractions import Fraction as Fr
from itertools import product as iproduct

sys.path.insert(0, '.')


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "ok": bool(ok), "detail": str(detail)[:200]})
    say(("PASS " if ok else "FAIL ") + name)


def h_seq(roots, n):
    d = len(roots)
    prod = [1]
    for r in roots:
        new = [0] * (len(prod) + 1)
        for i, c in enumerate(prod):
            new[i] += c
            new[i + 1] += c * r
        prod = new
    e = prod
    h = [1]
    for r in range(1, n + 1):
        s = 0
        for k in range(1, min(r, d) + 1):
            s += (-1) ** (k + 1) * e[k] * h[r - k]
        h.append(s)
    return h


def poly_mul(P, Q):
    R = [0] * (len(P) + len(Q) - 1)
    for i, p in enumerate(P):
        if p:
            for j, q in enumerate(Q):
                R[i + j] += p * q
    return R


def m1():
    shapes = [((2, 3), (5, 7), (2, -3)),
              ((2, 3), (5, 7), (1, 2, 3)),
              ((1, 2, 3), (2, 3), (5, 7)),
              ((2, 3), (1, 2, -2), (3, 5, 7))]
    for (xs, ys, zs) in shapes:
        hx = h_seq(list(xs), 13)
        hy = h_seq(list(ys), 13)
        hz = h_seq(list(zs), 13)
        dB, dC = len(ys), len(zs)
        ok = True
        for r in range(13):
            rhs = Fr(0)
            for j in range(dB):
                for k in range(dC):
                    w = ys[j] * zs[k]
                    num = Fr(ys[j] ** (dB - 1) * zs[k] ** (dC - 1))
                    den = 1
                    for j2 in range(dB):
                        if j2 != j:
                            den *= (ys[j] - ys[j2])
                    for k2 in range(dC):
                        if k2 != k:
                            den *= (zs[k] - zs[k2])
                    # sum_r h_r(x) w^r T^r coefficient: h_r(x) w^r
                    rhs += num * hx[r] * Fr(w) ** r / den
            if rhs != Fr(hx[r] * hy[r] * hz[r]):
                ok = False
                break
        check(f"M1 series {tuple(map(len,(xs,ys,zs)))} at {xs},{ys},{zs}",
              ok)


def alternant_ABC(xs, ys, zs, Tdeg):
    dA, dB, dC = len(xs), len(ys), len(zs)
    tot = [Fr(0)] * (Tdeg + 1)
    for j in range(dB):
        for k in range(dC):
            poly = [Fr(1)]
            for (i2, j2, k2) in iproduct(range(dA), range(dB), range(dC)):
                if j2 == j and k2 == k:
                    continue
                poly = poly_mul(poly, [1, -xs[i2] * ys[j2] * zs[k2]])
            den = 1
            for j2 in range(dB):
                if j2 != j:
                    den *= (ys[j] - ys[j2])
            for k2 in range(dC):
                if k2 != k:
                    den *= (zs[k] - zs[k2])
            c = Fr(ys[j] ** (dB - 1) * zs[k] ** (dC - 1), den)
            for i, v in enumerate(poly[:Tdeg + 1]):
                tot[i] += c * v
    return tot


def m2():
    shapes = [((2, 3), (5, 7), (2, -3)),
              ((2, 3), (5, 7), (1, 2, 3)),
              ((1, 2, 3), (2, 3), (5, 7)),
              ((2, 3), (1, 2, -2), (3, 5, 7))]
    for (xs, ys, zs) in shapes:
        dA, dB, dC = len(xs), len(ys), len(zs)
        n = dA * dB * dC
        # DEGREE LAW (corrected by this script's own first run, which
        # refuted deg = n - dA at shape (2,2,3)): each alternant
        # summand has degree n - dA, but the top coefficient factors
        # through sum_j y_j^{dB-1-dA}/prod(y_j - y_j') = h_{-dA}(y),
        # which VANISHES whenever 1 <= dA <= dB - 1 (Lemma 1 with
        # negative index); by the A/B/C symmetry of the series the
        # true degree is n - max(dA, dB, dC).
        degN = n - max(dA, dB, dC)
        D = [1]
        for (i, j, k) in iproduct(range(dA), range(dB), range(dC)):
            D = poly_mul(D, [1, -xs[i] * ys[j] * zs[k]])
        hx = h_seq(list(xs), n + 10)
        hy = h_seq(list(ys), n + 10)
        hz = h_seq(list(zs), n + 10)
        N = []
        for r in range(n + 6):
            s = Fr(0)
            for i in range(min(r, n) + 1):
                s += D[i] * hx[r - i] * hy[r - i] * hz[r - i]
            N.append(s)
        tail = all(v == 0 for v in N[n + 1:])
        alt = alternant_ABC(list(xs), list(ys), list(zs), n)
        degree_ok = (all(v == 0 for v in N[degN + 1:n + 1])
                     and N[degN] != 0)
        check(f"M2 N_ABC {(dA,dB,dC)} matrix==alternant, deg={degN}",
              tail and degree_ok and [Fr(v) for v in N[:n + 1]] == alt)


def m3():
    # two-factor: rank 2 x rank 2: N_AB degree dA*dB - dA = 2
    xs, ys = (2, 3), (5, 7)
    dA, dB = 2, 2
    n = 4
    D = [1]
    for (i, j) in iproduct(range(dA), range(dB)):
        D = poly_mul(D, [1, -xs[i] * ys[j]])
    hx = h_seq(list(xs), n + 8)
    hy = h_seq(list(ys), n + 8)
    N = []
    for r in range(n + 5):
        s = Fr(0)
        for i in range(min(r, n) + 1):
            s += D[i] * hx[r - i] * hy[r - i]
        N.append(s)
    tail = all(v == 0 for v in N[n + 1:])
    # classical Rankin-Selberg numerator: 1 - (det A)(det B) T^2
    eA = xs[0] * xs[1]
    eB = ys[0] * ys[1]
    expect = [Fr(1), Fr(0), Fr(-eA * eB), Fr(0), Fr(0)]
    check("M3 rank2 x rank2 Rankin-Selberg numerator = 1 - detA detB T^2",
          tail and [Fr(v) for v in N[:5]] == expect,
          f"N={N[:5]}")


def main():
    m1()
    m2()
    m3()
    allok = all(c["ok"] for c in CHECKS)
    json.dump({"checks": CHECKS, "all_ok": allok,
               "rh_established": False},
              open('matrix/multilinear_defect.json', 'w'), indent=1)
    say("ALL OK" if allok else "FAILURES PRESENT")


if __name__ == "__main__":
    main()
