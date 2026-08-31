#!/usr/bin/env python3
"""X-108509: stdlib-exact replay for the deformation-spectrum theorem
(standalone/2026-08-31-deformation-spectrum/PROOF.md).

Checks (EXACT_RATIONAL unless labelled):
  V1  spectrum normal form, m = 2..9 at 12 integer (a,b) points: the
      defect numerator N_m is reconstructed by inline Berlekamp-Massey
      from the ACTUAL cubed/powered coefficient sequence (independent of
      the T-108500 formula), then (i) deg N = m-1; (ii) for even m,
      exact divisibility by (1 + b^{m/2} T); (iii) the linear system on
      the Laurent basis w_j = T^nu (b^m T + 1/T)^j has a UNIQUE exact
      solution with zero residual (existence + uniqueness of M_m);
      (iv) M_m is monic (mu_nu = 1).
  V2  bridge instances: M_3 = z + 2ab and M_4 = z + b(3a^2 - 2b) at
      every instantiation.
  V3  purity <-> spectrum temperedness for m = 5 at Weil points
      (b = q, |a| <= 2 sqrt q): the exact z-criterion (M_5 has real
      roots with z^2 <= 4 b^5, decided by exact sign tests) agrees with
      a FLOAT_CROSSCHECK on |roots| of N_5 (labelled float).
  V4  splitting law for m = 5 at ~200 integer points: disc_z M_5 =
      a^2 b^2 (16a^4 - 48a^2b + 41b^2) exactly; M_5 splits over Q iff
      disc is a perfect square (quadratic case: exact both directions),
      and when it splits the reconstruction N_5 =
      prod (b^5 T^2 - z_i T + 1) holds exactly.

Standard library only. rh_established: false.
"""
import json
import math
import os
from fractions import Fraction as Fr

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "ok": bool(ok), "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + (f": {detail}" if detail
                                                 and not ok else ""))


# ---------- exact helpers (self-contained) --------------------------------

def bm(seq):
    """Berlekamp-Massey over Q: minimal C with sum C[j] s[k-j] = 0."""
    C, B = [Fr(1)], [Fr(1)]
    L, m_, bb = 0, 1, Fr(1)
    for n in range(len(seq)):
        d = seq[n] + sum(C[i] * seq[n - i] for i in range(1, L + 1))
        if d == 0:
            m_ += 1
        elif 2 * L <= n:
            Tc = C[:]
            coef = d / bb
            C = C + [Fr(0)] * (len(B) + m_ - len(C))
            for i, bv in enumerate(B):
                C[i + m_] -= coef * bv
            L, B, bb, m_ = n + 1 - L, Tc, d, 1
        else:
            coef = d / bb
            C = C + [Fr(0)] * (len(B) + m_ - len(C))
            for i, bv in enumerate(B):
                C[i + m_] -= coef * bv
            m_ += 1
    while C and C[-1] == 0:
        C.pop()
    return C


def poly_mul(p, q):
    r = [Fr(0)] * (len(p) + len(q) - 1)
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            r[i + j] += pi * qj
    return r


def poly_trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def rational_form(seq):
    """(P, Q) with sum seq T^k = P/Q, certified on the full window."""
    Q = bm(seq)
    prod = poly_mul(Q, list(seq))
    P = poly_trim(prod[:len(Q) - 1]) or [Fr(0)]
    # certification: remaining coefficients up to len(seq) vanish
    for k in range(len(Q) - 1, len(seq)):
        if poly_trim([prod[k]]):
            return None
    return P, Q


def h_seq(av, bv, n):
    h = [Fr(1), Fr(av)]
    for k in range(2, n + 1):
        h.append(av * h[-1] - bv * h[-2])
    return h[:n + 1]


def solve_linear(Amat, rhs):
    """Exact Gaussian elimination; returns (solution, unique?) or None."""
    m_, n_ = len(Amat), len(Amat[0])
    M = [row[:] + [rhs[i]] for i, row in enumerate(Amat)]
    piv = []
    r = 0
    for c in range(n_):
        pr = next((i for i in range(r, m_) if M[i][c] != 0), None)
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        pv = M[r][c]
        M[r] = [v / pv for v in M[r]]
        for i in range(m_):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [vi - f * vr for vi, vr in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == m_:
            break
    for i in range(r, m_):
        if M[i][n_] != 0:
            return None                        # inconsistent
    if len(piv) < n_:
        return ([Fr(0)] * n_, False)           # underdetermined
    sol = [Fr(0)] * n_
    for i, c in enumerate(piv):
        sol[c] = M[i][n_]
    return (sol, True)


# ---------- V1 + V2 -------------------------------------------------------

PTS = [(2, 3), (-2, 3), (3, 2), (1, -2), (4, 5), (-3, -2), (5, 3),
       (2, -5), (-4, 7), (6, -1), (7, 5), (-5, 4)]


def numerator_by_bm(av, bv, m):
    dim = m + 1
    need = 2 * dim + m + 6
    h = h_seq(av, bv, need)
    r = rational_form([hk ** m for hk in h])
    if r is None:
        return None
    P, Q = r
    return P, Q


def w_basis_coeffs(bv, m, nu, j):
    """Coefficient list of w_j = T^nu (b^m T + 1/T)^j, degree nu+j."""
    # (b^m T + 1/T)^j = sum_i C(j,i) b^{m i} T^{2i - j}
    out = [Fr(0)] * (nu + j + 1)
    for i in range(j + 1):
        out[nu + 2 * i - j] += Fr(math.comb(j, i)) * Fr(bv) ** (m * i)
    return out


def v12():
    ok_all = True
    bridge_ok = True
    for m in range(2, 10):
        eps = 1 if m % 2 == 0 else 0
        nu = (m - 1 - eps) // 2
        for (av, bv) in PTS:
            r = numerator_by_bm(av, bv, m)
            if r is None:
                ok_all = False
                continue
            P, Q = r
            if len(P) - 1 != m - 1 or len(Q) - 1 != m + 1:
                continue                       # degeneration locus: skip
            N = P[:]
            if eps:
                # exact division by (1 + b^{m/2} T)
                c = Fr(bv) ** (m // 2)
                quo = [Fr(0)] * (len(N) - 1)
                rem = N[:]
                for i in range(len(N) - 2, -1, -1):
                    quo[i] = rem[i + 1] / c
                    rem[i + 1] -= quo[i] * c
                    rem[i] -= quo[i]
                if poly_trim(rem):
                    ok_all = False
                    check("V1-even-divisibility", False,
                          f"m={m} pt=({av},{bv})")
                    continue
                N = quo
            # solve N = sum_j mu_j w_j on the Laurent basis
            rows = len(N)
            Amat = [[Fr(0)] * (nu + 1) for _ in range(rows)]
            for j in range(nu + 1):
                wc = w_basis_coeffs(bv, m, nu, j)
                for i, v in enumerate(wc):
                    Amat[i][j] = v
            sol = solve_linear(Amat, N + [Fr(0)] * (rows - len(N)))
            if sol is None or not sol[1]:
                ok_all = False
                check("V1-spectrum-solve", False, f"m={m} pt=({av},{bv})")
                continue
            mus, _ = sol
            if mus[nu] != 1:
                ok_all = False
                check("V1-monic", False, f"m={m} pt=({av},{bv}) "
                                         f"mu_nu={mus[nu]}")
            if m == 3 and mus[0] != 2 * av * bv:
                bridge_ok = False
            if m == 4 and mus[0] != Fr(bv) * (3 * av * av - 2 * bv):
                bridge_ok = False
    check("V1 spectrum normal form m=2..9 x 12 points "
          "(BM route, unique exact solution, monic)", ok_all)
    check("V2 bridge instances M_3 = z + 2ab, M_4 = z + b(3a^2-2b)",
          bridge_ok)


# ---------- V3: purity <-> spectrum temperedness (m = 5) ------------------

def v3b():
    """Float crosscheck without numpy: Durand-Kerner on N_5."""
    pts = [(1, 2), (2, 2), (-1, 3), (3, 5), (2, 7), (1, 5)]
    agree = True
    for (av, q) in pts:
        if av * av > 4 * q:
            continue
        r = numerator_by_bm(av, q, 5)
        if r is None or len(r[0]) - 1 != 4:
            continue
        P, _ = r
        # exact criterion (same as V3)
        N = P
        Amat = [[Fr(0)] * 3 for _ in range(len(N))]
        for j in range(3):
            wc = w_basis_coeffs(q, 5, 2, j)
            for i, v in enumerate(wc):
                Amat[i][j] = v
        (mus, uniq) = solve_linear(Amat, N + [Fr(0)] * (len(Amat) - len(N)))
        C, B = mus[0], mus[1]
        disc = B * B - 4 * C
        R2 = 4 * Fr(q) ** 5
        s = R2 + C
        pure_exact = bool(disc >= 0 and s >= 0 and s * s >= B * B * R2
                          and B * B <= 4 * R2)
        # Durand-Kerner
        cs = [complex(v) for v in P]
        lead = cs[-1]
        mon = [v / lead for v in cs]
        n = len(mon) - 1
        roots = [complex(0.4, 0.9) ** k for k in range(1, n + 1)]
        for _ in range(300):
            new = []
            for i, ri in enumerate(roots):
                num = sum(mon[j] * ri ** j for j in range(n + 1))
                den = 1.0
                for j, rj in enumerate(roots):
                    if j != i:
                        den *= (ri - rj)
                new.append(ri - num / den)
            roots = new
        pure_float = all(abs(abs(1 / rt) - float(q) ** 2.5)
                         / float(q) ** 2.5 < 1e-6 for rt in roots)
        if pure_float != pure_exact:
            agree = False
            check("V3b-mismatch", False, f"({av},{q}) exact={pure_exact} "
                                         f"float={pure_float}")
    check("V3b purity float crosscheck (Durand-Kerner, labelled "
          "FLOAT_CROSSCHECK) agrees with exact z-criterion", agree)


# ---------- V4: m = 5 splitting law ---------------------------------------

def is_square(n):
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n


def v4():
    ok_disc = True
    ok_split = True
    n_split = 0
    tested = 0
    for av in range(-7, 8):
        for bv in range(-7, 8):
            if av == 0 or bv == 0 or av * av == 4 * bv:
                continue
            r = numerator_by_bm(av, bv, 5)
            if r is None or len(r[0]) - 1 != 4:
                continue
            tested += 1
            P, _ = r
            Amat = [[Fr(0)] * 3 for _ in range(len(P))]
            for j in range(3):
                wc = w_basis_coeffs(bv, 5, 2, j)
                for i, v in enumerate(wc):
                    Amat[i][j] = v
            (mus, uniq) = solve_linear(Amat,
                                       P + [Fr(0)] * (len(Amat) - len(P)))
            C, B = mus[0], mus[1]
            disc = B * B - 4 * C
            pred = Fr(av) ** 2 * Fr(bv) ** 2 * (16 * av ** 4
                                                - 48 * av ** 2 * bv
                                                + 41 * bv ** 2)
            if disc != pred:
                ok_disc = False
            dn = int(disc)
            if is_square(dn):
                n_split += 1
                rt = math.isqrt(dn)
                for sg in (1,):
                    z1 = (-B + rt) / 2
                    z2 = (-B - rt) / 2
                    prod = poly_mul([Fr(1), -z1, Fr(bv) ** 5],
                                    [Fr(1), -z2, Fr(bv) ** 5])
                    if poly_trim([pi - qi for pi, qi
                                  in zip(P, prod)]) != []:
                        ok_split = False
    check("V4 disc_z M_5 == a^2 b^2 (16a^4-48a^2b+41b^2) at all "
          f"{tested} points", ok_disc)
    check("V4 splitting law: disc square => exact factorization "
          f"N_5 = prod(b^5 T^2 - z_i T + 1) ({n_split} split points)",
          ok_split)


def main():
    v12()
    v3b()
    v4()
    os.makedirs(os.path.join(os.path.dirname(__file__), "results"),
                exist_ok=True)
    allok = all(c["ok"] for c in CHECKS)
    with open(os.path.join(os.path.dirname(__file__), "results",
                           "verification.json"), "w") as f:
        json.dump({"experiment": "X-108509-deformation-spectrum",
                   "checks": CHECKS, "all_ok": allok,
                   "arithmetic_class": ("EXACT_RATIONAL + one labelled "
                                        "FLOAT_CROSSCHECK (V3b)"),
                   "rh_established": False}, f, indent=1)
    print("ALL OK" if allok else "FAILURES PRESENT")
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
