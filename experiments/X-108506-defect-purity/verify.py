#!/usr/bin/env python3
"""X-108506: exact replay for O-108506 (angle-stratified purity of the m=3
defect). Standard library only, EXACT_RATIONAL. rh_established: false."""
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


def a_p_11a1(p):
    """Exact a_p for 11a1: y^2 + y = x^3 - x^2 - 10x - 20 over F_p."""
    count = 1  # point at infinity
    for x in range(p):
        rhs = (x * x * x - x * x - 10 * x - 20) % p
        for y in range(p):
            if (y * y + y - rhs) % p == 0:
                count += 1
    return p + 1 - count


def main():
    # W1: exact a_p values for the two witness primes
    a2, a3 = a_p_11a1(2), a_p_11a1(3)
    check("W1_exact_point_counts", a2 == -2 and a3 == -1, f"a_2={a2}, a_3={a3}")

    # W2: the two-case purity criterion on the witnesses
    # p=2: N_3 = 1 + 2*a*p*T + p^3 T^2 with a=-2, p=2 -> 1 - 8T + 8T^2
    # disc = (2ap)^2 - 4 p^3
    d2 = (2 * a2 * 2) ** 2 - 4 * 2 ** 3
    d3 = (2 * a3 * 3) ** 2 - 4 * 3 ** 3
    check("W2_witness_discriminants", d2 > 0 and d3 < 0,
          f"disc(p=2)={d2}>0 (impure), disc(p=3)={d3}<0 (pure)")

    # W3: criterion equivalence: sign(disc) == sign(a^2 - p) for all good
    # primes p <= 97 of 11a1 (exact; disc = 4p^2(a^2 - p))
    ok = True
    strata = {"pure": [], "impure": [], "boundary": []}
    for p in [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
              61, 67, 71, 73, 79, 83, 89, 97]:
        ap = a_p_11a1(p)
        disc = (2 * ap * p) ** 2 - 4 * p ** 3
        s1 = (disc > 0) - (disc < 0)
        s2 = (ap * ap > p) - (ap * ap < p)
        ok &= (s1 == s2)
        ok &= (ap * ap <= 4 * p)  # Hasse, exact
        key = "impure" if s1 > 0 else ("pure" if s1 < 0 else "boundary")
        strata[key].append(p)
    check("W3_criterion_all_good_primes_le_97", ok,
          f"pure={strata['pure']}, impure={strata['impure']}, "
          f"boundary={strata['boundary']}")

    # W4 (adversarial-review strengthening; the old check was tautological):
    # for every good prime p <= 97, CUBE the actual coefficient sequence of
    # 1/(1 - a_p T + p T^2), reconstruct its minimal rational form by
    # Berlekamp-Massey, and verify the numerator equals the claimed
    # N_3 = 1 + 2 a_p p T + p^3 T^2 with the two-case purity criterion
    # applied to the RECONSTRUCTED numerator: disc < 0 (pure: conjugate
    # inverse roots with product exactly p^3) iff a_p^2 < p.
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
            dd = s[n]
            for i in range(1, L + 1):
                if i < len(C):
                    dd += C[i] * s[n - i]
            if dd == 0:
                m += 1
                continue
            coef = dd / bb
            if 2 * L <= n:
                Told = list(C)
                need = len(B) + m
                if len(C) < need:
                    C += [Fr(0)] * (need - len(C))
                for i, bc in enumerate(B):
                    C[i + m] -= coef * bc
                L, B, bb, m = n + 1 - L, Told, dd, 1
            else:
                need = len(B) + m
                if len(C) < need:
                    C += [Fr(0)] * (need - len(C))
                for i, bc in enumerate(B):
                    C[i + m] -= coef * bc
                m += 1
        while len(C) > 1 and C[-1] == 0:
            C.pop()
        # numerator = (seq * C) truncated
        out = [Fr(0)] * (len(C))
        for i in range(len(C)):
            acc = Fr(0)
            for j in range(i + 1):
                if j < len(C) and i - j < len(s):
                    acc += C[j] * s[i - j]
            out[i] = acc
        while len(out) > 1 and out[-1] == 0:
            out.pop()
        return out, C

    ok = True
    for p in [2, 3, 5, 7, 13, 17, 19, 23]:
        ap = a_p_11a1(p)
        cubes = [x ** 3 for x in hseq(ap, p, 22)]
        P, Q = bm_minimal(cubes)
        if ap == 0:
            # supersingular degeneration (T-108500 Theorem 3 phenomenon at
            # m=3): the defect cancels and the REDUCED form is
            # 1/(1 + p^3 T^2); the reduced object has conjugate roots of
            # modulus p^{3/2} — pure, consistent with a^2 = 0 < p
            ok &= (P == [Fr(1)] and Q == [Fr(1), Fr(0), Fr(p) ** 3])
            continue
        Npred = [Fr(1), Fr(2 * ap * p), Fr(p) ** 3]
        ok &= (P == Npred)
        disc = (2 * ap * p) ** 2 - 4 * p ** 3
        ok &= ((disc < 0) == (ap * ap < p))
        if disc < 0:
            ok &= (P[2] == Fr(p) ** 3)   # product of conjugate inverse roots
    check("W4_pure_case_modulus_from_reconstruction", ok,
          "N_3 reconstructed by BM from actual cubed sequences at 8 primes "
          "(supersingular p=19 handled as the reduced degenerate form); "
          "purity criterion applied to the reconstructed numerator")

    # W5 (strengthened): derive the m=2 defect from the actual SQUARED
    # sequences: BM numerator must be exactly [1, p] at every tested prime
    # (uniformly pure, single inverse root -p of modulus p = p^{2/2}...
    # weight-2 monomial), in contrast to the stratified m=3 case.
    ok = True
    for p in [2, 3, 5, 7, 13]:
        ap = a_p_11a1(p)
        sqs = [x ** 2 for x in hseq(ap, p, 18)]
        P, Q = bm_minimal(sqs)
        ok &= (P == [Fr(1), Fr(p)])
    check("W5_m2_always_pure_from_reconstruction", ok,
          "m=2 defect [1, p] reconstructed from actual squared sequences at "
          "5 primes: uniformly pure; stratification starts at m=3")

    here = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(here, "results"), exist_ok=True)
    all_ok = all(c["ok"] for c in CHECKS)
    with open(os.path.join(here, "results", "verification.json"), "w") as f:
        json.dump({"experiment": "X-108506-defect-purity",
                   "claim": "O-108506", "checks": CHECKS, "all_ok": all_ok,
                   "strata_11a1_le_97": strata,
                   "arithmetic_class": "EXACT_RATIONAL",
                   "rh_established": False}, f, indent=1)
    print(("PASS_108506_DEFECT_PURITY" if all_ok else
           "FAIL_108506_DEFECT_PURITY") + f" checks={len(CHECKS)}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
