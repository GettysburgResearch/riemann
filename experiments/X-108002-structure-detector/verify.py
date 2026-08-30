#!/usr/bin/env python3
"""X-108002: battery verification of the trace-to-object structure detector
(T-108002), programme #763.

Unlike X-108500/X-108501 (independent replays), this experiment
intentionally exercises the deposited instrument itself —
research/exploratory/2026-08-30-two-programme-pass/core/reconstruct.py —
because the instrument and its refusal semantics ARE the claimed object.
All arithmetic inside the instrument is EXACT_RATIONAL (stdlib Fraction).

Battery (each row: expected refusal axiom, or None for full pass):
  B1  genuine elliptic-type local data (deg 2, weight (p,1))  -> None
  B2  Mobius local data mu(p^k)                               -> A2_EFFECTIVITY
      (finite-rank VIRTUAL object; witness numerator [1, -1]; per
      Brauer-Nesbitt-type limits, trace data cannot certify
      non-semisimplicity — the claim is exactly A1-holds/A2-fails)
  B3  structureless integer sequence                          -> A1_FINITE_RANK
  B4  non-integral local factor (roots 2, 1/2)                -> A3_INTEGRALITY
  B5  integral but weight-violating factor (roots 3, 1/3 at
      claimed weight (3,1): product 1 != 3)                   -> A4_PURITY
  B6  held-out violation: genuine prefix with one corrupted
      tail term                                               -> A5_HELD_OUT
  B7  tensor compatibility: A(x)A predicted vs actual         -> HOLDS
  B8  tensor incompatibility: perturbed product data          -> FAILS
  B9  function-field Mobius contrast: sum_f mu(f) T^{deg f} =
      1 - qT at q=2,3 — finite rank, VIRTUAL (A2 fails), and the
      virtual part IS pure of weight (q,2)-style: recorded verbatim

rh_established: false, always.
"""
import json
import os
import sys
from fractions import Fraction as Fr

PASS_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "..", "..", "research", "exploratory",
                         "2026-08-30-two-programme-pass")
sys.path.insert(0, os.path.abspath(PASS_ROOT))

from core.reconstruct import detect, tensor_compatibility  # noqa: E402
from core.exact import (coefficient_sequence_from_satake,   # noqa: E402
                        power_sums_from_satake, op_tensor,
                        satake_poly_from_power_sums)

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "ok": bool(ok), "detail": detail})
    if not ok:
        print(f"FAIL {name}: {detail}")
    return ok


def refusal_of(series, **kw):
    return detect(series, **kw).refusal


def main():
    results = {}

    sat = [Fr(1), Fr(2), Fr(2)]  # a_2 = -2 at p=2 (11a1-type), weight (2,1)
    good = coefficient_sequence_from_satake(sat, 24)
    v1 = detect(good, weight=(2, 1))
    check("B1_genuine_full_pass", v1.refusal is None,
          str([c["axiom"] + ":" + c["status"] for c in v1.cells]))

    mob = [Fr(1), Fr(-1)] + [Fr(0)] * 22
    v2 = detect(mob, weight=(2, 0))
    ok2 = (v2.refusal == "A2_EFFECTIVITY"
           and v2.object["numerator"] == "[1, -1]"
           and v2.object["degree"] == 0)
    check("B2_mobius_virtual_refusal", ok2,
          f"refusal={v2.refusal}, object={v2.object}")

    junk = [Fr(1)] + [Fr((-1) ** k * ((k * k * k) % 7 - 3)) for k in range(1, 23)]
    check("B3_structureless_refusal", refusal_of(junk) == "A1_FINITE_RANK")

    nonint = coefficient_sequence_from_satake([Fr(1), Fr(-5, 2), Fr(1)], 24)
    check("B4_nonintegral_refusal",
          refusal_of(nonint, weight=(2, 1)) == "A3_INTEGRALITY")

    # roots 3 and 1/3: satake (1-3T)(1-T/3) -> not integral... use integral
    # weight violation instead: roots with product != q^w but integral:
    # (1-2T)(1-3T) = 1 -5T +6T^2 at claimed weight (5,1): reciprocity fails
    wv = coefficient_sequence_from_satake([Fr(1), Fr(-5), Fr(6)], 24)
    check("B5_weight_violation_refusal",
          refusal_of(wv, weight=(5, 1)) == "A4_PURITY")

    corrupted = list(good)
    corrupted[-2] += 1
    v6 = detect(corrupted, weight=(2, 1))
    # corruption near the tail: the full-window rational form may fail (A1)
    # or the held-out prediction must catch it; either refusal is a correct
    # rejection, and silent acceptance is the failure mode being tested
    check("B6_corrupted_tail_caught",
          v6.refusal in ("A1_FINITE_RANK", "A5_HELD_OUT"),
          f"refusal={v6.refusal}")

    pa = power_sums_from_satake(sat, 20)
    pt = op_tensor(pa, pa, 4)
    satT = satake_poly_from_power_sums(pt[:4], 4)
    prod_seq = coefficient_sequence_from_satake(satT, 16)
    t7 = tensor_compatibility(sat, sat, prod_seq)
    check("B7_tensor_compatibility_holds", t7["status"] == "HOLDS")

    bad_prod = list(prod_seq)
    bad_prod[5] += 1
    t8 = tensor_compatibility(sat, sat, bad_prod)
    check("B8_tensor_incompatibility_fails",
          t8["status"] == "FAILS" and "mismatch at index 5" in t8["witness"])

    # B9: function-field Mobius contrast: the AFFINE zeta of F_q[x] is
    # sum_{monic f} u^{deg f} = 1/(1-qu), so sum_{monic f} mu(f) u^{deg f}
    # = 1 - q u exactly. Computed here by exhaustive Mobius over monic
    # polynomials of degree < 7 (independent of the identity), then fed to
    # the detector: expected verdict = finite-rank VIRTUAL (A2 fails) with
    # numerator witness exactly [1, -q] — and that virtual part is PURE
    # (single root q, i.e. weight 2 in the |alpha| = q^{w/2} normalization):
    # the function-field Mobius object is virtual-but-pure, the sharpest
    # contrast row to the number-field side.
    for q in (2, 3):
        mu_series = ff_mobius_series(q, 7)
        v9 = detect(mu_series, weight=(q, 0))
        ok9 = (v9.refusal == "A2_EFFECTIVITY" and v9.object["degree"] == 0)
        ok9 &= v9.object["numerator"] == f"[1, {-q}]"
        check(f"B9_ff_mobius_virtual_q{q}", ok9,
              f"refusal={v9.refusal}, object={v9.object}")
        results[f"ff_mobius_q{q}_numerator"] = v9.object["numerator"]

    here = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(here, "results"), exist_ok=True)
    all_ok = all(c["ok"] for c in CHECKS)
    with open(os.path.join(here, "results", "verification.json"), "w") as f:
        json.dump({"experiment": "X-108002-structure-detector",
                   "claim": "T-108002", "checks": CHECKS, "all_ok": all_ok,
                   "extra": results,
                   "arithmetic_class": "EXACT_RATIONAL",
                   "rh_established": False}, f, indent=1)
    print(("PASS_108002_STRUCTURE_DETECTOR" if all_ok else
           "FAIL_108002_STRUCTURE_DETECTOR") + f" checks={len(CHECKS)}")
    return 0 if all_ok else 1


def ff_mobius_series(q, n_max):
    """sum over monic f in F_q[x], deg f < n_max, of mu(f) u^{deg f}: exact
    exhaustive computation via factorization counting. mu(f) = 0 unless f
    squarefree, else (-1)^{number of irreducible factors}. Uses the exact
    recursion for the number of monic irreducibles and a divisor sieve over
    monic polynomials encoded as coefficient tuples."""
    # enumerate monic polynomials by tuples of coefficients (c_0..c_{d-1})
    from itertools import product as iproduct

    def poly_mulmod(f, g):
        out = [0] * (len(f) + len(g) - 1)
        for i, a in enumerate(f):
            for j, b in enumerate(g):
                out[i + j] = (out[i + j] + a * b) % q
        return tuple(out)

    monics = {0: [(1,)]}
    for d in range(1, n_max):
        monics[d] = [tuple(cs) + (1,) for cs in iproduct(range(q), repeat=d)]
    # irreducibles by sieve: a monic of degree d is irreducible iff it is not
    # a product of lower-degree monics (nontrivially)
    composites = set()
    for d1 in range(1, n_max):
        for d2 in range(d1, n_max):
            if d1 + d2 >= n_max:
                break
            for f in monics[d1]:
                for g in monics[d2]:
                    composites.add(poly_mulmod(f, g))
    irred = {d: [f for f in monics[d] if f not in composites]
             for d in range(1, n_max)}
    # mu via DFS over squarefree products of distinct irreducibles (ordered
    # by degree, so we can prune once the next degree no longer fits)
    all_irred = [(d, f) for d in sorted(irred) for f in irred[d]]

    series = [0] * n_max

    def dfs(idx, poly, sign, deg):
        series[deg] += sign
        for k in range(idx, len(all_irred)):
            d, f = all_irred[k]
            if deg + d >= n_max:
                break  # degrees are nondecreasing from here on
            dfs(k + 1, poly_mulmod(poly, f), -sign, deg + d)

    dfs(0, (1,), 1, 0)
    return [Fr(x) for x in series]


if __name__ == "__main__":
    sys.exit(main())
