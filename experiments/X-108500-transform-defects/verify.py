#!/usr/bin/env python3
"""X-108500: stdlib-exact replay of the finite content of T-108500
(exact defect law for pointwise transforms of degree-2 local data).

Self-contained: standard library only, Fraction arithmetic throughout,
no floats anywhere. The symbolic discovery layer (sympy) lives in
research/exploratory/2026-08-30-two-programme-pass/matrix/; THIS replay
re-derives every claimed identity independently at many exact integer
instantiations, so the two routes must agree.

Checks (all EXACT_RATIONAL):
  D1  m=2,3,4 defect law: for 24 integer (a,b) pairs, the Berlekamp-Massey
      minimal rational form of sum h_k^m T^k equals N_m / det(1-Sym^m T)
      as a rational function (cross-multiplied), with the CLAIMED closed
      forms N_2 = 1+bT, N_3 = 1+2abT+b^3T^2,
      N_4 = 1 + b(3a^2-b)T + b^3(3a^2-b)T^2 + b^6T^3.
  D2  degeneration: at a=0 (trace-zero locus) the reduced form of the m=2
      transform is 1/(1-b^2T^2) exactly (defect-denominator cancellation).
  D3  self-duality: coefficient identity c_{m-1-r} = b^{m(m-1)/2-mr} c_r
      for m=2,3,4 at the same instantiation set.
  D4  linear-coefficient law c_1 = a^m - h_m for m=2..6 at instantiations
      (h_m computed independently by the recursion).
  D5  Cauchy/Hadamard: sum h_k(A)h_k(B) T^k = (1 - bA bB T^2)/det(1-A(x)B T)
      at 12 instantiation pairs (tensor denominator built from power sums).
  D6  Jacobi-Trudi instance: h_k h_{k+2} - h_{k+1}^2 = -b^{k+1}, k <= 20.
  D7  Adams relabelling: sum h_{2k} T^k = (1+bT)/(1-(a^2-2b)T+b^2T^2).

rh_established: false, always.
"""
import json
import os
import sys
from fractions import Fraction as Fr

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "ok": bool(ok), "detail": detail})
    if not ok:
        print(f"FAIL {name}: {detail}")
    return ok


# ---- minimal exact toolkit (self-contained by convention) ----------------

def trim(p):
    p = [Fr(x) for x in p]
    while p and p[-1] == 0:
        p.pop()
    return p


def pmul(a, b):
    if not a or not b:
        return []
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return trim(out)


def series_of_rational(P, Q, n):
    P = [Fr(x) for x in P]; Q = [Fr(x) for x in Q]
    out = []
    for k in range(n):
        c = P[k] if k < len(P) else Fr(0)
        for j in range(1, min(k, len(Q) - 1) + 1):
            c -= Q[j] * out[k - j]
        out.append(c / Q[0])
    return out


def berlekamp_massey(s):
    s = [Fr(x) for x in s]
    C, B = [Fr(1)], [Fr(1)]
    L, m, bb = 0, 1, Fr(1)
    for n in range(len(s)):
        d = s[n]
        for i in range(1, L + 1):
            if i < len(C):
                d += C[i] * s[n - i]
        if d == 0:
            m += 1
            continue
        coef = d / bb
        if 2 * L <= n:
            Told = list(C)
            need = len(B) + m
            if len(C) < need:
                C += [Fr(0)] * (need - len(C))
            for i, bc in enumerate(B):
                C[i + m] -= coef * bc
            L, B, bb, m = n + 1 - L, Told, d, 1
        else:
            need = len(B) + m
            if len(C) < need:
                C += [Fr(0)] * (need - len(C))
            for i, bc in enumerate(B):
                C[i + m] -= coef * bc
            m += 1
    return trim(C) or [Fr(1)]


def minimal_form(series):
    a = [Fr(x) for x in series]
    Q = berlekamp_massey(a)
    L = len(Q) - 1
    if 2 * L + 2 > len(a):
        return None
    P = trim(pmul(a, Q)[:max(L, 1)])
    if series_of_rational(P or [Fr(0)], Q, len(a)) != a:
        return None
    return (P or [Fr(0)]), Q


def hseq(a, b, n):
    h = [Fr(1), Fr(a)]
    while len(h) < n:
        h.append(a * h[-1] - b * h[-2])
    return h[:n]


def sym_m_denominator(a, b, m):
    """det(1 - Sym^m(A) T) at integer (a,b): product over weight monomials,
    built exactly from power sums p_j(Sym^m) = h_m(alpha^j, beta^j) using
    trace/det of A^j: (tr A^j, det A^j) obtained by the recursion
    t_{j} = a t_{j-1} - b t_{j-2}."""
    a, b = Fr(a), Fr(b)
    d = m + 1
    # traces of A^j
    tr = [Fr(2), a]
    for _ in range(m * d + 2):
        tr.append(a * tr[-1] - b * tr[-2])
    ps = []
    for j in range(1, d + 1):
        t, dt = tr[j], b ** j
        h0, h1 = Fr(1), t
        for _ in range(m - 1):
            h0, h1 = h1, t * h1 - dt * h0
        ps.append(h1)
    # Newton: e_k from p_1..p_d, then satake = sum (-1)^k e_k T^k
    e = [Fr(1)]
    for k in range(1, d + 1):
        acc = Fr(0)
        for i in range(1, k + 1):
            acc += (-1) ** (i - 1) * e[k - i] * ps[i - 1]
        e.append(acc / k)
    return [(-1) ** k * e[k] for k in range(d + 1)]


def claimed_defect(a, b, m):
    a, b = Fr(a), Fr(b)
    if m == 2:
        return [Fr(1), b]
    if m == 3:
        return [Fr(1), 2 * a * b, b ** 3]
    if m == 4:
        return [Fr(1), b * (3 * a * a - b), b ** 3 * (3 * a * a - b), b ** 6]
    raise ValueError(m)


PAIRS = [(1, 2), (2, 3), (-1, 2), (3, 5), (5, 2), (-2, 11), (4, 7), (1, 1),
         (2, 1), (-3, 13), (6, 5), (7, 3), (-4, 5), (1, -2), (2, -3),
         (-5, 7), (8, 11), (3, 2), (-1, 1), (9, 4), (10, 7), (-6, 17),
         (11, 13), (5, 6)]


def d1():
    ok = True
    for m in (2, 3, 4):
        for (av, bv) in PAIRS:
            h = hseq(av, bv, 2 * (m + 1) + 8)
            seq = [x ** m for x in h]
            mf = minimal_form(seq)
            if mf is None:
                return check("D1_defect_law", False, f"no form m={m} {(av,bv)}")
            P, Q = mf
            N = claimed_defect(av, bv, m)
            D = sym_m_denominator(av, bv, m)
            ok &= (pmul(N, Q) == pmul(D, P))
            if not ok:
                return check("D1_defect_law", False, f"m={m} {(av,bv)}")
    return check("D1_defect_law", ok, f"m=2,3,4 x {len(PAIRS)} instantiations")


def d2():
    ok = True
    for bv in (2, 3, 5, 7, -2):
        h = hseq(0, bv, 20)
        seq = [x * x for x in h]
        mf = minimal_form(seq)
        P, Q = mf
        ok &= (P == [Fr(1)] and Q == trim([Fr(1), Fr(0), Fr(-bv * bv)]))
    return check("D2_supersingular_degeneration", ok,
                 "reduced form 1/(1-b^2 T^2) at a=0")


def d3():
    ok = True
    for m in (2, 3, 4):
        e = m * (m - 1) // 2
        for (av, bv) in PAIRS:
            N = claimed_defect(av, bv, m)
            while len(N) < m:
                N.append(Fr(0))
            for r in range(m):
                lhs = N[m - 1 - r]
                # c_{m-1-r} * b^{mr} == c_r * b^{e}  (cleared form)
                ok &= (lhs * Fr(bv) ** (m * r) == N[r] * Fr(bv) ** e)
    return check("D3_self_duality", ok, "c_{m-1-r} b^{mr} = c_r b^{m(m-1)/2}")


def d4():
    ok = True
    for m in range(2, 7):
        for (av, bv) in PAIRS[:12]:
            h = hseq(av, bv, m + 2)
            # c_1 directly: coefficient of T in N_m = (series * D)_1
            D = sym_m_denominator(av, bv, m)
            full = hseq(av, bv, 2 * (m + 1) + 8)
            s = [x ** m for x in full]
            NfromD = pmul(s, D)
            c1 = NfromD[1] if len(NfromD) > 1 else Fr(0)
            ok &= (c1 == Fr(av) ** m - h[m])
    return check("D4_linear_coefficient_law", ok, "c_1 = a^m - h_m, m=2..6")


def d5():
    ok = True
    pairs2 = [((1, 2), (2, 3)), ((3, 5), (-1, 2)), ((5, 2), (4, 7)),
              ((2, 1), (1, 1)), ((-2, 11), (3, 2)), ((7, 3), (-4, 5)),
              ((1, -2), (2, -3)), ((9, 4), (5, 6)), ((8, 11), (11, 13)),
              ((6, 5), (10, 7)), ((-3, 13), (-5, 7)), ((-6, 17), (2, 3))]
    for (aA, bA), (aB, bB) in pairs2:
        n = 18
        hA = hseq(aA, bA, n)
        hB = hseq(aB, bB, n)
        seq = [x * y for x, y in zip(hA, hB)]
        mf = minimal_form(seq)
        if mf is None:
            return check("D5_cauchy_hadamard", False, f"{(aA,bA,aB,bB)}")
        P, Q = mf
        # tensor denominator from power sums p_k = tA_k * tB_k
        def traces(a, b, n):
            t = [Fr(2), Fr(a)]
            while len(t) < n + 1:
                t.append(a * t[-1] - b * t[-2])
            return t[1:]
        pt = [x * y for x, y in zip(traces(aA, bA, 8), traces(aB, bB, 8))]
        e = [Fr(1)]
        for k in range(1, 5):
            acc = Fr(0)
            for i in range(1, k + 1):
                acc += (-1) ** (i - 1) * e[k - i] * pt[i - 1]
            e.append(acc / k)
        D = [(-1) ** k * e[k] for k in range(5)]
        N = [Fr(1), Fr(0), -Fr(bA) * Fr(bB)]
        ok &= (pmul(N, Q) == pmul(D, P))
    return check("D5_cauchy_hadamard", ok, "12 instantiation pairs")


def d6():
    ok = True
    for (av, bv) in PAIRS[:10]:
        h = hseq(av, bv, 24)
        for k in range(20):
            ok &= (h[k] * h[k + 2] - h[k + 1] ** 2 == -Fr(bv) ** (k + 1))
    return check("D6_jacobi_trudi_hankel_minor", ok)


def d7():
    ok = True
    for (av, bv) in PAIRS[:10]:
        h = hseq(av, bv, 40)
        seq = [h[2 * k] for k in range(20)]
        N = [Fr(1), Fr(bv)]
        D = [Fr(1), -(Fr(av) ** 2 - 2 * Fr(bv)), Fr(bv) ** 2]
        ok &= (series_of_rational(N, D, 20) == seq)
    return check("D7_adams_relabelling", ok)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(here, "results"), exist_ok=True)
    all_ok = all([d1(), d2(), d3(), d4(), d5(), d6(), d7()])
    with open(os.path.join(here, "results", "verification.json"), "w") as f:
        json.dump({"experiment": "X-108500-transform-defects",
                   "claim": "T-108500", "checks": CHECKS, "all_ok": all_ok,
                   "arithmetic_class": "EXACT_RATIONAL",
                   "rh_established": False,
                   "scope_note": ("finite exact replay of the theorem's "
                                  "computed content; the general-m proofs are "
                                  "in standalone/2026-08-30-transform-defect-law/"
                                  "PROOF.md")}, f, indent=1)
    print(("PASS_108500_TRANSFORM_DEFECTS" if all_ok else
           "FAIL_108500_TRANSFORM_DEFECTS") + f" checks={len(CHECKS)}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
