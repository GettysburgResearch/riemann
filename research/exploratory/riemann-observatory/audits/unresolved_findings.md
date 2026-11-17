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


## Other unresolved verification items

- **OpenAI quasi-RH 7/8 Lean formalization** (comparator challenge `riemannZeta_ne_zero_of_seven_eighths_lt_re`): not replayed; building third-party Lean code was blocked by this session's safety policy. Procedure: `audits/lean_replay/README.md`.
- **OpenAI 7/8 manuscript (199 pp.)**: read for structure only, not audited (see `audits/quasi_rh/DOSSIER.md`).
- **Alpöge–Furman Lean claim** and **Knausgård's axiom-dependent Lean proof**: not replayed.
- **Lu–Zaman–Zhao computation** underlying the all-q Landau–Siegel constant 3.0e-3: disclosed external computation, not replayed (`audits/claims_2026/SIEGEL/`).
