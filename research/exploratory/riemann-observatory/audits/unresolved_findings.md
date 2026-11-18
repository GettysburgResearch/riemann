# Unresolved findings

```text
Status: AUDIT FINDINGS (Level 2/3, adjudicated where flagged)
Scope: specific claims named per finding; not whole-paper verdicts
Exact sources or dependencies: per finding (evidence path)
What was actually run: independent auditor and adjudicator agents with recomputation (Arb/mpmath/exact arithmetic) where stated
Smallest remaining gap: human expert confirmation; Lean replays not performed
```

These items are **not** characterized as errors. They are open questions for expert review.


## FND-0005 — A. Yang, "Explicit bounds on zeta(s) in the critical strip and a zero-free region", arXiv:2301.03165 v1/v2; JMAA 534 (2024)

*Location:* Littlewood-type constant: v1 21.432 vs v2/published 21.233 · *Classification:* `suspected_gap` · *Public characterization allowed:* False

The constant change between versions is a version difference, and downstream constants (Bellotti 2024, BTY 2026, Fiori-Jaskari 2026) are not weakened. The auditor reports that the written argument does not cover v1's 21.432 for the full stated range; adjudication kept this as a suspected gap without a public witness.

*Full record:* `audits/L2_flag_audits/F3-yang-constant.md`


## FND-0011 — Planat-Raymond, arXiv:2611.06245v1 (Nov 2026): claim Lambda < 0.156821

*Location:* certificate · *Classification:* `no_issue_found_in_inspected_portion (claim not verified)` · *Public characterization allowed:* False

Status classification only: unrefereed, large certificate not replayed; see report for inputs required.

*Full record:* `audits/L2_flag_audits/F8-dbn-claims.md`


## FND-0015 — arXiv:2503.24275 (claim that every nontrivial zero of the Davenport-Heilbronn function lies on the critical line)

*Location:* main claim · *Classification:* `verified_error (Observatory-internal; external citation pending one more independent Level-2 check)` · *Public characterization allowed:* False

Contradicted by certified off-line zeros of the Davenport-Heilbronn function (campaign C2: complete certified list for |t| <= 300, lowest at 0.8085171824566373855 + 85.6993484853775921719i) and by Davenport-Heilbronn 1936 (zeros with sigma > 1). The C2 adjudicator asked for one more independent Level-2 check before citing outside the Observatory.

*Full record:* `proposals/independent_campaigns/C2-countermodel-zoo/FINAL.md (sec. 7.8)`


## FND-0016 — Bétermin-Šamaj-Travěnec, Conjecture 1.1 (Epstein-type lattice sum threshold)

*Location:* Conjecture 1.1 · *Classification:* `conjecture refuted (Observatory theorem C2-ADJ-2; external citation pending one more independent check)` · *Public characterization allowed:* False

Using the exact Chowla-Selberg value Z_k(1/2) = 2gamma + 2log(k/4pi) + 8 sum d(N) K_0(2 pi N k), at k = 4 pi e^{-gamma} the value is 8.39e-20 > 0, and the true threshold exceeds e^gamma/(4pi) by 5.95e-21, contradicting the conjecture as stated. Refuting a conjecture is not an error in the source; the conjecture was stated as open.

*Full record:* `proposals/independent_campaigns/C2-countermodel-zoo/FINAL.md`

## Other unresolved verification items

- **OpenAI quasi-RH 7/8 Lean formalization** (comparator challenge `riemannZeta_ne_zero_of_seven_eighths_lt_re`): not replayed; building third-party Lean code was blocked by this session's safety policy. Procedure: `audits/lean_replay/README.md`.
- **OpenAI 7/8 manuscript (199 pp.)**: read for structure only, not audited (see `audits/quasi_rh/DOSSIER.md`).
- **Alpöge–Furman Lean claim** and **Knausgård's axiom-dependent Lean proof**: not replayed.
- **Lu–Zaman–Zhao computation** underlying the all-q Landau–Siegel constant 3.0e-3: disclosed external computation, not replayed (`audits/claims_2026/SIEGEL/`).
