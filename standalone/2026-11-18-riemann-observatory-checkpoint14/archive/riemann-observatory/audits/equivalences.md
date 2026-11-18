# Equivalence-track audit scope

Executed 2026-11-17. Three complete preprint texts were read: Báez-Duarte math/0205003v1, Burnol math/0103058v2, BCF1211.5191v1. This is substantive reading, not complete proof verification. Dependency external sources were not all obtained; no full-paper Level 2 or Level 3 is claimed.

## Checked portions

- Burnol §2: reconstructed finite-dimensional jet-projection mechanism and limiting Hilbert/Cauchy Gram block. Checked for m=2 by explicit finite-N computation in the campaign. Full invariant-operator construction in §§3–5 was read but not independently reconstructed.
- BCF Theorem 2 simplicity restriction: tested omission using Q=(1-z)^2. Counterexample proves the restriction cannot simply be deleted while preserving the linear window. This agrees with the published theorem, and is not a published error finding.
- BCF Theorem 1: exact inverse-derivative-moment hypothesis preserved, including its implicit simplicity requirement. No statement that RH alone gives its optimal asymptotic.
- Báez-Duarte Theorem 1.1: reconstructed ordered-limit proof: RH supplies H convergence as n→∞ at fixed small epsilon; then epsilon↓0 gives the target. Pointwise convergence alone is insufficient; no exchange of limits is asserted.

## Local proof-presentation issue requiring context

In the inspected math/0205003v1 p.5, the displayed majorant (1+|tau|)^(-1+2epsilon) has square integrable tail only when epsilon<1/4. The ensuing sentence uses epsilon_0<1/2. Restricting epsilon_0<1/4 fixes this dominated-convergence step, and the proof later requires only "sufficiently small" epsilon. This is a repairable overstatement of the range for that displayed bound, **not a challenge to Theorem 1.1**. No independent reviewer or journal-version comparison yet; do not elevate to a verified published mathematical error. The normalization of Mellin Plancherel measure in (2.6) should also be checked against the PDF rather than extraction before asserting a typographical issue.

## Access failures and correction searches

Bombieri–Lagarias author PDF URL https://websites.umich.edu/~lagarias/doc/bombieri.pdf was located, but shell access returned 403 and web text extraction was garbled. No Li/Bombieri–Lagarias substantive record or audit is claimed by this track. Search results or broken extraction do not constitute reading. Version histories were read from arXiv metadata for the three accessed works. Dedicated search for all later corrections remains incomplete.

## Finding classification

E-FIND-001: "Correct argument, but commonly misinterpreted" — BCF requires simplicity; explicit repeated-root stress test rejects a stronger claim the source does not make. Status: elementary argument supplied; independent review pending.

E-FIND-002: "Valid argument with potentially stronger consequences" — exact double-root optimal window and finite error, derived as an exercise from Burnol's jet method. Status: elementary proof supplied; priority and independent review pending; no novelty claim.

E-FIND-003: "Unresolved ambiguity requiring expert review" — epsilon range of the displayed majorant; local repair stated. No material consequence for main theorem found.
