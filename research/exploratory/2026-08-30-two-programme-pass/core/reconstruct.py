"""Trace-to-object structure detector (programme #763, claims band T-1080xx).

Given exact local coefficient data (a_{p^k}) or exact trace data (p_k), the
detector attempts to reconstruct a minimal 'Frobenius-like' local object and
then subjects it to a fixed ordered battery of structural axioms.  Its output
is either a reconstructed object with certificates, or a REFUSAL naming the
FIRST axiom that fails together with an exact witness.  The detector never
guesses: every verdict cell carries its own rigor label.

Axiom battery (ordered):
  A1 FINITE_RANK    minimal rational form P/Q exists and is certified on the
                    window (Berlekamp-Massey; needs 2L+2 <= window length);
  A2 EFFECTIVITY    trivial numerator in coefficient mode (P == [1]); a
                    nontrivial numerator is a virtual/negative part, with the
                    numerator itself as exact witness;
  A3 INTEGRALITY    the local factor lies in Z[T] with constant term 1;
  A4 PURITY(q,w)    exact necessary conditions that all inverse roots have
                    modulus q^{w/2}: (i) self-reciprocity under alpha ->
                    q^w/alpha; (ii) (T - q^w)^{floor(d/2)} divides the exact
                    char poly of Ext^2; complete exact sufficiency for d <= 2;
  A5 HELD_OUT       the reconstruction from a proper prefix exactly predicts
                    the withheld tail;
  A6 TENSOR         (pairwise) reconstructed objects exactly predict the trace
                    data of a claimed product/Sym^2 world.

Rigor: EXACT_RATIONAL for every computation in this file.  Purity sufficiency
beyond degree 2 is labelled NECESSARY_ONLY.  RH is not addressed;
rh_established=false.
"""

from fractions import Fraction
from typing import List, Optional, Sequence

from .exact import (
    F, Poly, poly_trim, poly_eval, poly_divmod, poly_mul,
    minimal_rational_form, series_of_rational, power_sums_from_satake,
    op_ext2, satake_poly_from_power_sums, is_integer_poly,
)

HOLDS = "HOLDS"
FAILS = "FAILS"
SKIPPED = "SKIPPED"
NECESSARY_ONLY = "NECESSARY_ONLY"


class Verdict:
    def __init__(self):
        self.cells = []          # list of dicts: axiom, status, rigor, witness
        self.refusal = None      # first failing axiom name, or None
        self.object = None       # dict describing the reconstructed object

    def add(self, axiom, status, rigor, witness=""):
        self.cells.append({"axiom": axiom, "status": status,
                           "rigor": rigor, "witness": str(witness)})
        if status == FAILS and self.refusal is None:
            self.refusal = axiom

    def as_dict(self):
        return {"object": self.object, "refusal": self.refusal,
                "cells": self.cells, "rh_established": False}


def _fmt(p: Sequence) -> str:
    return "[" + ", ".join(str(F(c)) for c in p) + "]"


def _self_reciprocal_defect(Q: Poly, qw: Fraction) -> Optional[Poly]:
    """For Q(T) = prod (1 - a_i T), the involution a -> q^w / a fixes the root
    multiset iff Q(T) == c * T^d * Q(1/(q^w T)) for the unique consistent
    scalar c.  Returns None when the identity holds exactly, else the exact
    difference polynomial as witness."""
    Q = poly_trim(Q)
    d = len(Q) - 1
    # T^d * Q(1/(q^w T)) has coefficients rev with powers of q^w:
    # sum_j Q[j] T^{d-j} (q^w)^{-j}
    rev = [Q[d - i] / (qw ** (d - i)) for i in range(d + 1)]
    # normalize both to constant term 1 (Q[0] == 1 by convention)
    if rev[0] == 0:
        return Q
    revn = [c / rev[0] for c in rev]
    diff = poly_trim([a - b for a, b in zip(Q, revn)])
    return None if not diff else diff


def detect(series: Sequence, mode: str = "coefficients",
           weight: Optional[tuple] = None, holdout: int = 4) -> Verdict:
    """Run the battery on an exact sequence.

    mode='coefficients': series is a_0=1, a_1, ...   (expansion of 1/L_p-like)
    mode='traces':       series is p_1, p_2, ...     (trace data); internally
                         converted to the generating series sum p_k T^k.
    weight=(q, w):       optional purity claim to test exactly.
    holdout:             number of trailing terms withheld for A5.
    """
    v = Verdict()
    s = [F(x) for x in series]
    if mode == "traces":
        gen = [Fraction(0)] + s            # sum_{k>=1} p_k T^k
    else:
        gen = s
        if not gen or gen[0] != 1:
            v.add("A1_FINITE_RANK", FAILS, "EXACT_RATIONAL",
                  "coefficient mode requires a_0 = 1; got " +
                  (_fmt(gen[:1]) if gen else "empty"))
            return v

    # --- A1: finite rank, certified on the PREFIX (window minus holdout);
    # the withheld tail is then a SUBSTANTIVE held-out test at A5
    # (adversarial-review redesign, 2026-08-30: with A1 on the full window,
    # A5 was provably redundant given L-108001 and could never fire).
    use_holdout = holdout if (holdout > 0 and len(gen) > holdout + 6) else 0
    prefix = gen[: len(gen) - use_holdout] if use_holdout else gen
    pq = minimal_rational_form(prefix)
    if pq is None:
        v.add("A1_FINITE_RANK", FAILS, "EXACT_RATIONAL",
              "no certified minimal rational form on the prefix window of "
              f"length {len(prefix)} (recurrence order too large or unstable)")
        return v
    P, Q = pq
    d = len(Q) - 1
    v.object = {"numerator": _fmt(P), "denominator": _fmt(Q), "degree": d,
                "mode": mode}
    v.add("A1_FINITE_RANK", HOLDS, "EXACT_RATIONAL",
          f"P/Q certified on the {len(prefix)}-term prefix; deg Q = {d}, "
          f"deg P = {len(P)-1}"
          + ("" if use_holdout else " (window too short for a holdout)"))

    # --- A2: effectivity
    if mode == "coefficients":
        if poly_trim(P) == [Fraction(1)]:
            v.add("A2_EFFECTIVITY", HOLDS, "EXACT_RATIONAL",
                  "numerator is 1: pure denominator local factor")
        else:
            v.add("A2_EFFECTIVITY", FAILS, "EXACT_RATIONAL",
                  f"virtual part present: numerator {_fmt(P)}")
    else:
        # traces mode: multiplicity-one effectivity iff P == -T Q' exactly
        from .exact import poly_deriv, poly_scale
        mTQp = poly_trim([Fraction(0)] + poly_scale(poly_deriv(Q), -1))
        if poly_trim(P) == mTQp:
            v.add("A2_EFFECTIVITY", HOLDS, "EXACT_RATIONAL",
                  "trace numerator equals -T Q': all multiplicities are 1")
        else:
            v.add("A2_EFFECTIVITY", FAILS, "EXACT_RATIONAL",
                  f"trace numerator {_fmt(P)} != -T Q' = {_fmt(mTQp)}: "
                  "multiplicities are not identically 1 (possibly virtual)")

    # --- A3: integrality of the local factor
    target = Q if mode == "coefficients" else Q
    if is_integer_poly(target) and target and target[0] == 1:
        v.add("A3_INTEGRALITY", HOLDS, "EXACT_RATIONAL",
              f"local factor in Z[T], constant term 1: {_fmt(target)}")
    else:
        v.add("A3_INTEGRALITY", FAILS, "EXACT_RATIONAL",
              f"local factor not in Z[T] with constant 1: {_fmt(target)}")

    # --- A4: purity at claimed (q, w)
    if weight is None:
        v.add("A4_PURITY", SKIPPED, "EXACT_RATIONAL", "no weight claim supplied")
    elif d == 0:
        v.add("A4_PURITY", SKIPPED, "EXACT_RATIONAL",
              "degree-0 denominator: purity vacuous; virtual part not pure-tested")
    else:
        q, w = weight
        qw = F(q) ** int(w) if int(w) == w else None
        if qw is None:
            v.add("A4_PURITY", SKIPPED, "EXACT_RATIONAL",
                  "non-integer weight not supported exactly")
        else:
            wit = _self_reciprocal_defect(Q, qw)
            if wit is not None:
                v.add("A4_PURITY", FAILS, "EXACT_RATIONAL",
                      "self-reciprocity under a -> q^w/a fails; defect "
                      f"polynomial {_fmt(wit)}")
            else:
                if d == 1:
                    # single rational inverse root a with a = q^w / a
                    a = -Q[1]
                    ok = (a * a == qw)
                    v.add("A4_PURITY", HOLDS if ok else FAILS, "EXACT_RATIONAL",
                          f"inverse root {a}, a^2 {'==' if ok else '!='} q^w={qw}")
                elif d == 2:
                    # COMPLETE test (adversarial-review fix, 2026-08-30):
                    # both inverse roots have modulus q^{w/2} iff
                    #   (product == q^w AND disc <= 0)      [conjugate pair or
                    #    real double root +-q^{w/2}: disc=0 forces a1^2=4q^w]
                    #   OR (a1 == 0 AND product == -q^w)    [real pair +q^{w/2},
                    #    -q^{w/2}: e.g. 1 - q^w T^2]
                    b = Q[2]; a1 = -Q[1]
                    disc = a1 * a1 - 4 * b
                    ok = (b == qw and disc <= 0) or (a1 == 0 and b == -qw)
                    v.add("A4_PURITY", HOLDS if ok else FAILS, "EXACT_RATIONAL",
                          f"deg-2 complete test: trace={a1}, product={b}, "
                          f"q^w={qw}, disc={disc}")
                else:
                    # adversarial-review fix, 2026-08-30: the previous length
                    # guard made this branch dead code for every d >= 3
                    r2 = d * (d - 1) // 2
                    ps = power_sums_from_satake(Q, 2 * r2 + 2)
                    e2 = op_ext2(ps, r2)
                    ext2 = satake_poly_from_power_sums(e2, r2)
                    note = "self-reciprocity holds"
                    if ext2 is not None:
                        # check (1 - q^w T)^{d//2} divides ext2 factor
                        rem = ext2
                        mult = 0
                        div = [Fraction(1), -qw]
                        while True:
                            quo, r = poly_divmod(rem, div)
                            if r:
                                break
                            rem = quo; mult += 1
                        note += f"; (1 - q^w T)^{mult} | Ext^2 factor (need >= {d//2})"
                        if mult < d // 2:
                            v.add("A4_PURITY", FAILS, "EXACT_RATIONAL", note)
                        else:
                            v.add("A4_PURITY", HOLDS, NECESSARY_ONLY, note +
                                  "; exact NECESSARY conditions only for degree > 2")
                    else:
                        v.add("A4_PURITY", HOLDS, NECESSARY_ONLY, note)

    # --- A5: held-out prediction of the withheld tail (SUBSTANTIVE by
    # construction: A1 certified only the prefix, so the tail is genuinely
    # out of sample)
    if use_holdout:
        pred = series_of_rational(P if P else [Fraction(0)], Q, len(gen))
        if pred == gen:
            v.add("A5_HELD_OUT", HOLDS, "EXACT_RATIONAL",
                  f"the {len(prefix)}-term prefix form exactly predicts the "
                  f"withheld {use_holdout} terms")
        else:
            k = next(i for i, (x, y) in enumerate(zip(pred, gen)) if x != y)
            v.add("A5_HELD_OUT", FAILS, "EXACT_RATIONAL",
                  f"first mismatch at index {k}: predicted {pred[k]}, "
                  f"actual {gen[k]}")
    else:
        v.add("A5_HELD_OUT", SKIPPED, "EXACT_RATIONAL",
              "window too short for a holdout")

    return v


def tensor_compatibility(satA: Poly, satB: Poly, product_series: Sequence,
                         n: Optional[int] = None) -> dict:
    """A6: do reconstructed objects A, B exactly predict a claimed A x B world?
    product_series is the coefficient sequence of the claimed product world."""
    from .exact import op_tensor, coefficient_sequence_from_satake
    dt = (len(satA) - 1) * (len(satB) - 1)
    n_ps = max(dt, 2 * (len(satA) + len(satB)))   # robustness fix: op_tensor
    pa = power_sums_from_satake(satA, n_ps)        # needs dt power sums even
    pb = power_sums_from_satake(satB, n_ps)        # for high-degree inputs
    pt = op_tensor(pa, pb, max(dt, 1))
    satT = satake_poly_from_power_sums(pt[:dt], dt) if dt else [Fraction(1)]
    n = n or len(product_series)
    pred = coefficient_sequence_from_satake(satT, n)
    actual = [F(x) for x in product_series[:n]]
    ok = pred[: len(actual)] == actual
    out = {"axiom": "A6_TENSOR", "status": HOLDS if ok else FAILS,
           "rigor": "EXACT_RATIONAL",
           "witness": f"predicted tensor local factor {_fmt(satT)}"}
    if not ok:
        k = next(i for i, (x, y) in enumerate(zip(pred, actual)) if x != y)
        out["witness"] += (f"; first mismatch at index {k}: predicted "
                           f"{pred[k]}, actual {actual[k]}")
    return out
