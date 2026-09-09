#!/usr/bin/env python3
"""X-108515: stdlib-exact replay for the Segre defect bridge
(standalone/2026-08-31-segre-defect-bridge/PROOF.md).

Checks (EXACT integer/rational arithmetic, standard library only):
  V1  COARSE BRIDGE at exact integer points: for m = 2..5 at four
      (a, b) points and m = 6 at one point,
        K_m(T) := det(1 - A^{tensor m} T) * sum_r h_r^m T^r
      is a polynomial (tail window of 8 coefficients vanishes exactly)
      and equals
        N_m(T) * prod_{k=1}^{floor(m/2)}
                 det(1 - Sym^{m-2k}(A) b^k T)^(C(m,k) - C(m,k-1)),
      where every determinant on both sides is computed from the
      ACTUAL matrices (Kronecker/tensor power on the left, explicit
      symmetric-power matrices on the right) by integral
      Faddeev-LeVerrier -- an evaluation route fully independent of
      the weight-multiset algebra used in discovery.
  V2  DEFECT CONSISTENCY: N_m recomputed from the T-108500 definition
      det(1 - Sym^m(A) T) * sum h_r^m T^r with its own tail window.
  V3  EULERIAN SPECIALIZATION: N_m at (a, b) = (2, 1) equals the
      Eulerian polynomial A_m(T), m = 2..6 (Corollary 1 of the proof).
  V4  SELF-DUALITY instance: coefficient reversal
      N_m[i] * b^(m*i) == N_m[m-1-i] * b^(m*(m-1)/2 ... ) -- concretely
      N_m(T) = b^(m(m-1)/2) T^(m-1) N_m(1/(b^m T)) checked
      coefficientwise at the integer points (T-108500(3) instance,
      reproved geometrically as Theorem 3 of the standalone file).

Self-contained standard library only. rh_established: false.
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


# ---------------- exact matrix tool kit (integers throughout) --------

def mat_mul(A, B):
    n, p, q = len(A), len(B), len(B[0])
    Bt = list(zip(*B))
    return [[sum(A[i][k] * Bt[j][k] for k in range(p)) for j in range(q)]
            for i in range(n)]


def kron(A, B):
    na, nb = len(A), len(B)
    return [[A[i // nb][j // nb] * B[i % nb][j % nb]
             for j in range(na * nb)] for i in range(na * nb)]


def tensor_power(A, m):
    M = A
    for _ in range(m - 1):
        M = kron(M, A)
    return M


def sym_power(A, j):
    """Matrix of Sym^j(A) on the monomial basis e0^(j-i) e1^i.
    A acts on column vectors: A e0 = A[0][0] e0 + A[1][0] e1, etc."""
    if j == 0:
        return [[1]]
    n = j + 1
    S = [[0] * n for _ in range(n)]
    p, r = A[0][0], A[1][0]     # image of e0
    q, s = A[0][1], A[1][1]     # image of e1
    for i in range(n):          # source monomial e0^(j-i) e1^i
        # (p e0 + r e1)^(j-i) (q e0 + s e1)^i, coefficient of
        # e0^(j-t) e1^t:
        for u in range(j - i + 1):
            for v in range(i + 1):
                t = u + v
                coef = (comb(j - i, u) * p ** (j - i - u) * r ** u *
                        comb(i, v) * q ** (i - v) * s ** v)
                S[t][i] += coef
    return S


def det_one_minus_T(M):
    """Coefficients [d_0..d_n] of det(1 - M T) for an integer matrix,
    by integral Faddeev-LeVerrier: det(lambda I - M) =
    lambda^n - c_1 lambda^(n-1) - ... - c_n, and
    det(1 - M T) = 1 - c_1 T - c_2 T^2 - ... - c_n T^n."""
    n = len(M)
    I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    coeffs = [1]
    Mk = [row[:] for row in M]
    for k in range(1, n + 1):
        tr = sum(Mk[i][i] for i in range(n))
        assert tr % k == 0
        ck = tr // k
        coeffs.append(-ck)
        if k < n:
            Nk = [[Mk[i][j] - (ck if i == j else 0) for j in range(n)]
                  for i in range(n)]
            Mk = mat_mul(M, Nk)
    return coeffs


def poly_mul(P, Q):
    R = [0] * (len(P) + len(Q) - 1)
    for i, p in enumerate(P):
        if p:
            for j, q in enumerate(Q):
                R[i + j] += p * q
    return R


def poly_pow(P, e):
    R = [1]
    for _ in range(e):
        R = poly_mul(R, P)
    return R


def h_sequence(a, b, n):
    h = [1, a]
    for _ in range(2, n + 1):
        h.append(a * h[-1] - b * h[-2])
    return h[:n + 1]


def series_times_poly(D, h, m, upto):
    """Coefficients 0..upto of (sum_i D[i] T^i) * (sum_r h_r^m T^r)."""
    hp = [v ** m for v in h[:upto + 1]]
    out = []
    for r in range(upto + 1):
        out.append(sum(D[i] * hp[r - i]
                       for i in range(min(r, len(D) - 1) + 1)))
    return out


def defect_numerator(a, b, m, tail=8):
    """N_m at the integer point via T-108500: det(1 - Sym^m A T) * F."""
    A = [[0, -b], [1, a]]
    Q = det_one_minus_T(sym_power(A, m))
    h = h_sequence(a, b, m + tail + len(Q))
    K = series_times_poly(Q, h, m, m - 1 + tail)
    ok_tail = all(v == 0 for v in K[m:])
    return K[:m], ok_tail


def eulerian(m):
    """Eulerian polynomial A_m(T) coefficients, Worpitzky/explicit."""
    return [sum((-1) ** i * comb(m + 1, i) * (s + 1 - i) ** m
                for i in range(s + 1)) for s in range(m)]


POINTS = [(1, 2), (3, 1), (-2, 5), (0, 1)]


# ---------------- rank-d machinery for V5 (d = 3, 4; m = 2) ----------

def companion(elems):
    """d x d companion with det(1 - A T) = 1 - e1 T + e2 T^2 - ...
    (verified per instance by the V5 sanity check)."""
    d = len(elems)
    A = [[0] * d for _ in range(d)]
    for i in range(1, d):
        A[i][i - 1] = 1
    for i in range(d):
        k = d - i                      # e_k goes to row i with sign
        A[i][d - 1] = (-1) ** (k + 1) * elems[k - 1]
    return A


def h_seq_rank(elems, n):
    d = len(elems)
    h = [1]
    for r in range(1, n + 1):
        s = 0
        for k in range(1, min(r, d) + 1):
            s += (-1) ** (k + 1) * elems[k - 1] * h[r - k]
        h.append(s)
    return h


def sym2_matrix(A):
    d = len(A)
    basis = [(i, j) for i in range(d) for j in range(i, d)]
    idx = {b: t for t, b in enumerate(basis)}
    S = [[0] * len(basis) for _ in range(len(basis))]
    for (i, j) in basis:
        col = idx[(i, j)]
        for k in range(d):
            for l in range(d):
                c = A[k][i] * A[l][j]
                kk, ll = min(k, l), max(k, l)
                S[idx[(kk, ll)]][col] += c
    # e_i e_j with i != j maps via (Ae_i)(Ae_j); e_i^2 via (Ae_i)^2:
    # the double loop above counts e_i e_j (i<j) once per (k,l) pair
    # and e_i^2 correctly, since (i,j) fixed with i <= j and (k,l)
    # ranges over ordered pairs, merging k>l into (l,k).
    return S


def lam2_matrix(A):
    d = len(A)
    basis = [(i, j) for i in range(d) for j in range(i + 1, d)]
    idx = {b: t for t, b in enumerate(basis)}
    L = [[0] * len(basis) for _ in range(len(basis))]
    for (i, j) in basis:
        col = idx[(i, j)]
        for k in range(d):
            for l in range(k + 1, d):
                L[idx[(k, l)]][col] += (A[k][i] * A[l][j]
                                        - A[k][j] * A[l][i])
    return L


def v5():
    """coarse bridge at m = 2, ranks 3 and 4 (exact integer points):
    det(1 - A tensor A T) * sum h_r^2 T^r == N_{2,d} * det(1 - Lam^2 T),
    where N_{2,d} is computed from the Sym^2 route (T-108500). Rank 4
    is the first rank whose defect carries correction layers beyond
    the Gauss-sign polynomial (T-108508), so this tests the bridge
    against a structurally nontrivial defect."""
    cases = {3: [(1, 2, 3), (2, -1, 2), (0, 1, -2)],
             4: [(1, 2, 3, 2), (2, -1, 0, 3), (1, 0, -2, 1)]}
    for d, pts in cases.items():
        for elems in pts:
            A = companion(list(elems))
            # sanity: charpoly of A must be 1 - e1 T + e2 T^2 - ...
            cp = det_one_minus_T(A)
            expect = [1] + [(-1) ** k * elems[k - 1]
                            for k in range(1, d + 1)]
            check(f"V5 companion d={d} {elems}", cp == expect,
                  f"cp={cp}")
            n2 = d * d
            h = h_seq_rank(list(elems), n2 + 10)
            D = det_one_minus_T(tensor_power(A, 2))
            K = series_times_poly(D, h, 2, n2 + 8)
            tail_ok = all(v == 0 for v in K[n2 + 1:])
            Q = det_one_minus_T(sym2_matrix(A))
            NN = series_times_poly(Q, h, 2, len(Q) + 8)
            deg_n = (d * (d - 1)) // 2
            ntail = all(v == 0 for v in NN[deg_n + 1:])
            N = NN[:deg_n + 1]
            R = poly_mul(N, det_one_minus_T(lam2_matrix(A)))
            R = R + [0] * (n2 + 1 - len(R))
            check(f"V5 bridge d={d} m=2 {elems}",
                  tail_ok and ntail and K[:n2 + 1] == R[:n2 + 1],
                  f"K={K[:n2+1]} R={R[:n2+1]}")


def v12():
    for m in range(2, 7):
        pts = POINTS if m <= 5 else [(1, 2)]
        for (a, b) in pts:
            A = [[0, -b], [1, a]]
            n = 2 ** m
            D = det_one_minus_T(tensor_power(A, m))
            h = h_sequence(a, b, n + 10)
            K = series_times_poly(D, h, m, n + 8)
            tail_ok = all(v == 0 for v in K[n + 1:])
            check(f"V1 tail m={m} (a,b)=({a},{b})", tail_ok)
            N, ntail = defect_numerator(a, b, m)
            check(f"V2 defect tail m={m} (a,b)=({a},{b})", ntail)
            R = list(N)
            for k in range(1, m // 2 + 1):
                ck = comb(m, k) - comb(m, k - 1)
                S = sym_power(A, m - 2 * k)
                bk = b ** k
                Sc = [[bk * x for x in row] for row in S]
                R = poly_mul(R, poly_pow(det_one_minus_T(Sc), ck))
            R = R + [0] * (n + 1 - len(R))
            check(f"V1 bridge m={m} (a,b)=({a},{b})",
                  K[:n + 1] == R[:n + 1],
                  f"K={K[:n+1]} R={R[:n+1]}")


def v3():
    for m in range(2, 7):
        N, ntail = defect_numerator(2, 1, m)
        check(f"V3 Eulerian m={m}", ntail and N == eulerian(m),
              f"N={N} A_m={eulerian(m)}")


def v4():
    for m in range(2, 7):
        pts = POINTS if m <= 5 else [(1, 2)]
        for (a, b) in pts:
            N, _ = defect_numerator(a, b, m)
            # N_m(T) = b^(m(m-1)/2) T^(m-1) N_m(1/(b^m T)):
            # coefficientwise  N[i] == b^(m(m-1)/2) * N[m-1-i] / b^(m*(m-1-i))
            w = Fr(b) ** (m * (m - 1) // 2)
            ok = all(Fr(N[i]) == w * Fr(N[m - 1 - i]) /
                     Fr(b) ** (m * (m - 1 - i)) for i in range(m))
            check(f"V4 self-duality m={m} (a,b)=({a},{b})", ok)


def main():
    v12()
    v3()
    v4()
    v5()
    os.makedirs(os.path.join(os.path.dirname(__file__), "results"),
                exist_ok=True)
    allok = all(c["ok"] for c in CHECKS)
    with open(os.path.join(os.path.dirname(__file__), "results",
                           "verification.json"), "w") as f:
        json.dump({"experiment": "X-108515-segre-bridge",
                   "checks": CHECKS, "all_ok": allok,
                   "arithmetic_class": "EXACT_RATIONAL",
                   "rh_established": False}, f, indent=1)
    print("ALL OK" if allok else "FAILURES PRESENT")
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
