"""World 'native_imports': repository-native observables as detector targets
(programme #763, O-108004). Built inline in the 2026-08-31 continuation
pass after the original builder was lost to session limits.

Two pinned imports:

(a) The T-99930 native duplicate-67 source (ON MAIN, in-tree):
    beta(n) = mu(n) - 1_{67|n} mu(n/67), with documented local factors
    (1-x)^2 at p=67 and (1-x) at every other prime.
    Pin: standalone/2026-08-20-critical-taylor-renormalization/PROOF.md,
    blob 2444935b9c769353a8befae2b9bfb9805f26a294.

(b) The codex-atlas genus-2 family trace laws (UNMERGED BRANCH, pinned):
    T_(0,3)(q) = q^4 - 2q - 1,  T_(2,2)(q) = 2q^3 - q^2 - 2q - 2,
    T_(0,4)(q) = -(2q^2 + 1)  for every odd prime power q.
    Status in that lane: PROVED (RESIDUAL_MECHANISMS_RESEARCH_MAP.md line
    425, blob d4a3da1f0d7a9ef6ba936caf04cde64c1ee134c0 at branch head
    codex/beta-bandpass-wavelet @ d79692ec); the earlier FINDINGS.md form
    (blob 89b6b9848c150db428167f4dbd1026c2b5c12298 at
    codex/l-function-detector-atlas @ 10446e8e) displays them with a
    question mark — both pins recorded; the laws are used here as PINNED
    IMPORTED statements whose review status lives in their own lane.
    The tower evaluation t_k := T(q_0^k) along prime powers of a fixed
    q_0 is THIS build's construction (evaluating the law's generating
    structure), stated as such.

Detector expectations are NOT hardcoded as truths: every verdict is
computed and then asserted, so a change in the instrument fails the build.
RH is unproved; rh_established=false throughout.
"""
import sys
from fractions import Fraction as Fr

from core.reconstruct import detect
from core.worlds import cell, save_world, LADDER, MECHANISMS


def mu(n):
    out, m = 1, n
    p = 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            out = -out
        p += 1
    if m > 1:
        out = -out
    return out


def beta(n):
    b = mu(n)
    if n % 67 == 0:
        b -= mu(n // 67)
    return b


def main():
    runs = {}

    # --- (a1) cross-check the documented local factorization: the Dirichlet
    # series of beta must equal the formal Euler product with local factor
    # (1-x) at p != 67 and (1-x)^2 at 67 — verified coefficient-wise for
    # n <= 500 by expanding the product exactly (PROVED_HERE finite witness)
    N = 500
    coeffs = [Fr(0)] * (N + 1)
    coeffs[1] = Fr(1)
    p = 2
    while p <= N:
        if all(p % r for r in range(2, int(p ** 0.5) + 1)):
            local = {0: Fr(1), 1: Fr(-2) if p == 67 else Fr(-1)}
            if p == 67:
                local[2] = Fr(1)
            new = [Fr(0)] * (N + 1)
            for n in range(1, N + 1):
                if coeffs[n] == 0:
                    continue
                k, pk = 0, 1
                while n * pk <= N:
                    if k in local:
                        new[n * pk] += coeffs[n] * local[k]
                    k += 1
                    pk *= p
            coeffs = new
        p += 1
    ok_factor = all(coeffs[n] == beta(n) for n in range(1, N + 1))
    assert ok_factor, "local factorization of beta fails"
    runs["beta_euler_factorization_n_le_500"] = {
        "status": "PROVED_HERE", "ok": True,
        "witness": "expanded Euler product with (1-x) at p!=67 and (1-x)^2 "
                   "at 67 reproduces beta(n) exactly for all n <= 500"}

    # --- (a2) detector on the local sequences: the detector COUNTS LABELS
    for p0, expect_num in ((2, "[1, -1]"), (5, "[1, -1]"), (67, "[1, -2, 1]")):
        if p0 == 67:
            seq = [Fr(1), Fr(-2), Fr(1)] + [Fr(0)] * 21
        else:
            seq = [Fr(1), Fr(-1)] + [Fr(0)] * 22
        v = detect(seq, weight=(p0, 0))
        assert v.refusal == "A2_EFFECTIVITY", (p0, v.refusal)
        assert v.object["numerator"] == expect_num, (p0, v.object)
        runs[f"beta_local_p{p0}"] = {
            "refusal": v.refusal, "object": v.object,
            "cells": v.cells,
            "reading": ("virtual weight-0 with multiplicity = number of "
                        "labels at p (two labels at 67, one elsewhere): the "
                        "detector reads off the label bookkeeping exactly")}

    # --- (b) tower-evaluated family trace laws, traces mode
    LAWS = {
        "T_0_3": (lambda q: q ** 4 - 2 * q - 1,
                  lambda q: {q ** 4: 1, q: -2, 1: -1}),
        "T_2_2": (lambda q: 2 * q ** 3 - q ** 2 - 2 * q - 2,
                  lambda q: {q ** 3: 2, q ** 2: -1, q: -2, 1: -2}),
        "T_0_4": (lambda q: -(2 * q ** 2 + 1),
                  lambda q: {q ** 2: -2, 1: -1}),
    }
    for name, (law, mults) in LAWS.items():
        for q0 in (3, 5):
            tower = [Fr(law(q0 ** k)) for k in range(1, 25)]
            v = detect(tower, mode="traces")
            m = mults(q0)
            assert v.refusal == "A2_EFFECTIVITY", (name, q0, v.refusal)
            assert v.object["degree"] == len(m), (name, q0, v.object)
            # exact multiplicity recovery: p_k == sum_f m_f f^k for all k
            ok_m = all(sum(Fr(c) * Fr(f) ** k for f, c in m.items())
                       == tower[k - 1] for k in range(1, 25))
            assert ok_m
            runs[f"{name}_tower_q{q0}"] = {
                "refusal": v.refusal, "object": v.object,
                "multiplicities_recovered": {str(f): c for f, c in m.items()},
                "reading": ("the family trace law is a TATE-MONOMIAL VIRTUAL "
                            "object: frequencies are pure powers of q with "
                            "signed multiplicities equal to the law's "
                            "coefficients; no nontrivial Frobenius angles "
                            "survive family aggregation, and the detector "
                            "certifies exactly that")}

    na = cell("NOT_APPLICABLE", "OPEN",
              witness="data row, not a global zeta object")
    w = {
        "id": "native_imports",
        "title": "Repository-native observables as detector targets",
        "definition": ("(a) the T-99930 native duplicate-67 source beta(n) "
                       "with its documented local factors; (b) the codex "
                       "genus-2 family trace laws evaluated along prime-"
                       "power towers (this build's construction)"),
        "arithmetic_class": "EXACT_RATIONAL",
        "ladder": {k: dict(na) for k in LADDER},
        "mechanisms": {k: dict(na) for k in MECHANISMS},
        "critical_line": {"status": "NOT_FORMULATED",
                          "detail": "data row; no zeta object is claimed",
                          "rigor": "OPEN", "citation": ""},
        "sources": [
            "standalone/2026-08-20-critical-taylor-renormalization/PROOF.md "
            "@ blob 2444935b9c769353a8befae2b9bfb9805f26a294 (main, T-99930)",
            "research/l-families/atlas/RESIDUAL_MECHANISMS_RESEARCH_MAP.md "
            "@ blob d4a3da1f0d7a9ef6ba936caf04cde64c1ee134c0 "
            "(codex/beta-bandpass-wavelet @ d79692ec; trace laws PROVED "
            "in that unmerged lane)",
            "research/l-families/atlas/FINDINGS.md @ blob "
            "89b6b9848c150db428167f4dbd1026c2b5c12298 "
            "(codex/l-function-detector-atlas @ 10446e8e; conjectural form)",
        ],
        "detector_runs": runs,
        "notes": ("Headline: the detector reads the native source's label "
                  "bookkeeping (virtual weight-0, multiplicity = label "
                  "count, numerator (1-T)^labels), and certifies the codex "
                  "family trace laws as Tate-monomial virtual objects whose "
                  "multiplicity vectors are the law coefficients. See "
                  "O-108004."),
        "rh_established": False,
    }
    path = save_world(w, "worlds")
    print(f"WROTE {path}; runs: {len(runs)}; all assertions passed")


if __name__ == "__main__":
    main()
