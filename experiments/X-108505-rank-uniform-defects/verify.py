#!/usr/bin/env python3
"""X-108505: exact replay for O-108505 (rank-uniform pointwise-square
defect structure; Gauss-sign law proved rank 2 / verified rank 3 / refuted
rank 4 with witnesses; self-duality refuted at rank 3).

Uses the deposited pass core (documented dependency, as in X-108002).
All arithmetic EXACT_RATIONAL. rh_established: false."""
import json
import os
import sys
from fractions import Fraction as Fr

PASS_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "..", "..", "research", "exploratory",
                         "2026-08-30-two-programme-pass")
sys.path.insert(0, os.path.abspath(PASS_ROOT))

from core.exact import (minimal_rational_form, power_sums_from_satake,   # noqa
                        op_ext2, op_sym2, elementary_from_power_sums,
                        satake_poly_from_power_sums,
                        coefficient_sequence_from_satake)

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "ok": bool(ok), "detail": detail})
    if not ok:
        print(f"FAIL {name}: {detail}")
    return ok


def satake_from_es(es):
    d = len(es)
    sat = [Fr(1)] + [Fr(0)] * d
    for k in range(1, d + 1):
        sat[k] = (-1) ** k * Fr(es[k - 1])
    return sat


def square_defect(es):
    sat = satake_from_es(es)
    d = len(es)
    n = 4 * (d * (d + 1) // 2) + 10
    hs = coefficient_sequence_from_satake(sat, n)
    mf = minimal_rational_form([x * x for x in hs])
    assert mf is not None
    return mf, sat


def gauss_sign_prediction(es):
    sat = satake_from_es(es)
    d = len(es)
    r2 = d * (d - 1) // 2
    ps = power_sums_from_satake(sat, 2 * r2 + 4)
    e_ext = elementary_from_power_sums(op_ext2(ps, r2), r2)
    pred = [Fr(1)] + [(-1) ** (j * (j - 1) // 2) * e_ext[j - 1]
                      for j in range(1, r2 + 1)]
    while pred and pred[-1] == 0:
        pred.pop()
    return pred


def sym2_denominator(es):
    sat = satake_from_es(es)
    d = len(es)
    r = d * (d + 1) // 2
    ps = power_sums_from_satake(sat, 2 * r + 4)
    return satake_poly_from_power_sums(op_sym2(ps, r), r)


def main():
    r3_cases = [(1, 2, 3), (2, -1, 5), (-2, 3, 7), (3, 1, 2), (5, 2, -3)]
    r4_cases = [(1, 2, 3, 2), (2, 1, -1, 3), (1, 0, 2, -1), (3, -2, 1, 5)]

    # V1: denominator is Sym^2 and deg N = C(d,2) at ranks 3 and 4
    ok = True
    for es in r3_cases + r4_cases:
        (P, Q), sat = square_defect(es)
        d = len(es)
        ok &= (Q == sym2_denominator(es))
        ok &= (len(P) - 1 == d * (d - 1) // 2)
    check("V1_sym2_denominator_and_degree", ok)

    # V2: Gauss-sign law exact at rank 3
    ok = all(square_defect(es)[0][0] == gauss_sign_prediction(es)
             for es in r3_cases)
    check("V2_gauss_sign_law_rank3", ok)

    # V3: Gauss-sign law REFUTED at rank 4 — every witness must disagree,
    # and the canonical witness must match the recorded value
    ok = all(square_defect(es)[0][0] != gauss_sign_prediction(es)
             for es in r4_cases)
    (P, _), _ = square_defect((1, 2, 3, 2))
    ok &= (P == [Fr(x) for x in (1, 2, -1, -7, 2, -8, -8)])
    check("V3_gauss_sign_refuted_rank4", ok,
          "recorded witness (1,2,3,2) -> [1,2,-1,-7,2,-8,-8]")

    # V4: self-duality fails at rank 3 under ANY scale (adversarial-review
    # strengthening: the old check tested only the scale det^2). A scaled
    # palindrome means: exist rationals lam, c with
    # P[dN-j] = lam * c^j * P[j] for all j. With P[0]=1 and P[1] != 0 both
    # lam and c are forced by j=0,1; refute by checking j=2,3.
    (P, _), _ = square_defect((1, 2, 3))
    dN = len(P) - 1
    assert P[0] == 1 and P[1] != 0 and P[dN] != 0
    lam = P[dN] / P[0]
    c = P[dN - 1] / (lam * P[1])
    any_scale_palin = all(P[dN - j] == lam * c ** j * P[j]
                          for j in range(dN + 1))
    check("V4_self_duality_fails_rank3_any_scale", not any_scale_palin,
          f"N={[str(x) for x in P]}: forced lam={lam}, c={c} already fail "
          f"at j=2: {P[dN-2]} != {lam * c**2 * P[2]}")

    # V5: rank-4 sporadic palindrome recorded as data
    (P, _), _ = square_defect((1, 0, 2, -1))
    check("V5_rank4_sporadic_palindrome",
          P == [Fr(x) for x in (1, 0, -3, -5, -3, 0, 1)])

    here = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(here, "results"), exist_ok=True)
    all_ok = all(c["ok"] for c in CHECKS)
    with open(os.path.join(here, "results", "verification.json"), "w") as f:
        json.dump({"experiment": "X-108505-rank-uniform-defects",
                   "claim": "O-108505", "checks": CHECKS, "all_ok": all_ok,
                   "arithmetic_class": "EXACT_RATIONAL",
                   "rh_established": False}, f, indent=1)
    print(("PASS_108505_RANK_UNIFORM_DEFECTS" if all_ok else
           "FAIL_108505_RANK_UNIFORM_DEFECTS") + f" checks={len(CHECKS)}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
