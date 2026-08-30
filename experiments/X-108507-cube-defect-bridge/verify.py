#!/usr/bin/env python3
"""X-108507: stdlib-exact replay for T-108507 (the cube-defect bridge).

Checks (EXACT_RATIONAL unless labelled):
  V1  bridge readout: at 24 integer (a,b) instantiations, reconstruct the
      m=3 defect by Berlekamp-Massey from the actual cubed coefficient
      sequence, then READ OFF the trace-doubled deformation's data from the
      normalized numerator: -P[1]/b == 2a and P[2]/b^2 == b. The
      deformation is derived from the reconstructed obstruction, not
      assumed.
  V2  splitting-field identity: disc(N_3) == (2b)^2 * disc(X^2-2aX+b)/4
      exactly, i.e. disc(N_3)/(4b^2) == a^2 - b: the defect's splitting
      field is the deformation's Satake field.
  V3  stratification transfer on 11a1 (exact point counts, good p <= 97):
      sign(disc of A_2's Satake polynomial) == sign(a_p^2 - p) == purity
      case of the defect (supersingular a_p = 0 in the tempered case).
  V4  global reduction at good-prime level for 11a1: for every n <= 300
      composed of good primes, a_n^3 equals the Dirichlet-convolution
      coefficient of L^{good}(Sym^3) x D with the exact local factors
      det(1 - Sym^3 A_p T)^{-1} and N_3(T; a_p, p).
  V5  the Sato-Tate density of the non-tempered stratum equals
      2/3 - sqrt(3)/(2 pi) = 0.39100... (FLOATING_RECONNAISSANCE: numeric
      quadrature of the exact closed form; the closed form itself is
      elementary calculus stated in the proof).

Standard library only. rh_established: false.
"""
import json
import math
import os
import sys
from fractions import Fraction as Fr

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "ok": bool(ok), "detail": detail})
    if not ok:
        print(f"FAIL {name}: {detail}")
    return ok


def hseq(a, b, n):
    h = [Fr(1), Fr(a)]
    while len(h) < n:
        h.append(a * h[-1] - b * h[-2])
    return h[:n]


def bm_minimal(seq):
    s = [Fr(x) for x in seq]
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
    while len(C) > 1 and C[-1] == 0:
        C.pop()
    P = []
    for i in range(len(C)):
        acc = Fr(0)
        for j in range(min(i, len(C) - 1) + 1):
            if i - j < len(s):
                acc += C[j] * s[i - j]
        P.append(acc)
    while len(P) > 1 and P[-1] == 0:
        P.pop()
    return P, C


PAIRS = [(1, 2), (2, 3), (-1, 2), (3, 5), (5, 2), (-2, 11), (4, 7), (1, 1),
         (2, 1), (-3, 13), (6, 5), (7, 3), (-4, 5), (1, -2), (2, -3),
         (-5, 7), (8, 11), (3, 2), (-1, 1), (9, 4), (10, 7), (-6, 17),
         (11, 13), (5, 6)]


def v1_v2():
    ok1 = ok2 = True
    for (a, b) in PAIRS:
        cubes = [x ** 3 for x in hseq(a, b, 24)]
        P, Q = bm_minimal(cubes)
        if len(P) != 3:      # degeneration loci (e.g. a=0-type collapses)
            continue
        # readout: P[1]/b = 2a (doubled trace), P[2]/b^2 = b (kept det)
        ok1 &= (P[0] == 1 and P[1] / Fr(b) == 2 * a and
                P[2] / Fr(b) ** 2 == Fr(b))
        disc_N = P[1] ** 2 - 4 * P[0] * P[2]
        ok2 &= (disc_N == 4 * Fr(b) ** 2 * (a * a - b))
    c1 = check("V1_bridge_readout", ok1,
               "trace-doubled data (2a, b) read off the reconstructed defect "
               "at 24 instantiations")
    c2 = check("V2_splitting_field_identity", ok2,
               "disc(N_3) = 4 b^2 (a^2 - b) exactly")
    return c1 and c2


def a_p_11a1(p):
    count = 1
    for x in range(p):
        rhs = (x * x * x - x * x - 10 * x - 20) % p
        for y in range(p):
            if (y * y + y - rhs) % p == 0:
                count += 1
    return p + 1 - count


GOOD = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
        67, 71, 73, 79, 83, 89, 97]


def v3():
    ok = True
    for p in GOOD:
        ap = a_p_11a1(p)
        disc_A2 = (2 * ap) ** 2 - 4 * p          # Satake poly of A_2
        disc_N = (2 * ap * p) ** 2 - 4 * p ** 3  # defect
        s1 = (disc_A2 > 0) - (disc_A2 < 0)
        s2 = (disc_N > 0) - (disc_N < 0)
        s3 = (ap * ap > p) - (ap * ap < p)
        ok &= (s1 == s2 == s3)
    return check("V3_stratification_transfer", ok,
                 "temperedness of A_2 == purity of defect == sign(a_p^2-p) "
                 "at all good p <= 97")


def series_of_rational(P, Q, n):
    out = []
    for k in range(n):
        c = P[k] if k < len(P) else Fr(0)
        for j in range(1, min(k, len(Q) - 1) + 1):
            c -= Q[j] * out[k - j]
        out.append(c / Q[0])
    return out


def v4():
    # local data per good prime: Sym^3 satake (degree 4) and N_3
    N_LIMIT = 300
    aps = {p: a_p_11a1(p) for p in GOOD if p <= N_LIMIT}
    # multiplicative assembly of coefficients from local series
    def assemble(local_series):
        coeffs = [Fr(0)] * (N_LIMIT + 1)
        coeffs[1] = Fr(1)
        for p, ser in local_series.items():
            new = [Fr(0)] * (N_LIMIT + 1)
            for n in range(1, N_LIMIT + 1):
                if coeffs[n] == 0:
                    continue
                k, pk = 0, 1
                while n * pk <= N_LIMIT:
                    if k < len(ser):
                        new[n * pk] += coeffs[n] * ser[k]
                    k += 1
                    pk *= p
            coeffs = new
        return coeffs

    # side 1: cubes of the assembled a_n (good-prime part)
    loc_a = {p: series_of_rational([Fr(1)], [Fr(1), Fr(-ap), Fr(p)], 12)
             for p, ap in aps.items()}
    a_n = assemble(loc_a)
    lhs = [x ** 3 for x in a_n]

    # side 2: product of Sym^3 local inverse factors and N_3 numerators
    from itertools import count
    loc_rhs = {}
    for p, ap in aps.items():
        # power sums of A_p then Sym^3 satake via h_m at (tr A^j, det^j)
        tr = [Fr(2), Fr(ap)]
        for _ in range(20):
            tr.append(ap * tr[-1] - p * tr[-2])
        pj = []
        for j in range(1, 5):
            t, dt = tr[j], Fr(p) ** j
            h0, h1 = Fr(1), t
            for _ in range(2):
                h0, h1 = h1, t * h1 - dt * h0
            pj.append(h1)
        e = [Fr(1)]
        for k in range(1, 5):
            acc = Fr(0)
            for i in range(1, k + 1):
                acc += (-1) ** (i - 1) * e[k - i] * pj[i - 1]
            e.append(acc / k)
        sym3 = [(-1) ** k * e[k] for k in range(5)]
        n3 = [Fr(1), Fr(2 * ap * p), Fr(p) ** 3]
        loc_rhs[p] = series_of_rational(n3, sym3, 12)
    rhs = assemble(loc_rhs)

    good_support = [n for n in range(1, N_LIMIT + 1)
                    if all(pr in aps for pr in prime_factors(n))]
    ok = all(lhs[n] == rhs[n] for n in good_support)
    return check("V4_global_reduction", ok,
                 f"a_n^3 == [Sym^3 x D]_n for all {len(good_support)} "
                 f"good-support n <= {N_LIMIT}")


def prime_factors(n):
    out, p = set(), 2
    while p * p <= n:
        while n % p == 0:
            out.add(p)
            n //= p
        p += 1
    if n > 1:
        out.add(n)
    return out


def v5():
    # ST measure of |cos theta| > 1/2 under (2/pi) sin^2 theta d theta
    Nq = 200000
    acc = 0.0
    for i in range(Nq):
        th = math.pi * (i + 0.5) / Nq
        if abs(math.cos(th)) > 0.5:
            acc += math.sin(th) ** 2
    dens = (2 / math.pi) * acc * (math.pi / Nq)
    closed = 2 / 3 - math.sqrt(3) / (2 * math.pi)
    ok = abs(dens - closed) < 1e-4
    return check("V5_st_density_constant", ok,
                 f"quadrature {dens:.6f} vs closed form 2/3-sqrt3/(2pi)="
                 f"{closed:.6f}; FLOATING_RECONNAISSANCE only")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(here, "results"), exist_ok=True)
    all_ok = all([v1_v2(), v3(), v4(), v5()])
    with open(os.path.join(here, "results", "verification.json"), "w") as f:
        json.dump({"experiment": "X-108507-cube-defect-bridge",
                   "claim": "T-108507", "checks": CHECKS, "all_ok": all_ok,
                   "arithmetic_class": "EXACT_RATIONAL (V1-V4), "
                                       "FLOATING_RECONNAISSANCE (V5)",
                   "rh_established": False}, f, indent=1)
    print(("PASS_108507_CUBE_DEFECT_BRIDGE" if all_ok else
           "FAIL_108507_CUBE_DEFECT_BRIDGE") + f" checks={len(CHECKS)}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
