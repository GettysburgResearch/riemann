# Verification record and limits

## What was actually executed

- The newly written verify.py completes 3,192 explicit finite predicates. Many are repeated domain/corner guards; this is not a count of independent analytic cases.
- The 37 classes cover one good class, 35 reflected-ratio classes and one terminal class. All 36 density thresholds are checked against their ten detector monomials. Every relevant quadratic exponent/domain inequality is certified over the entire fixed epsilon interval by exact rational Bernstein coefficients.
- Normal and optimized Python produce byte-identical CHECKS.json. Both detailed executions reproduce CERTIFICATE.json, including every growth coefficient, lower-threshold count, mollifier parameter and class slack.
- Eight actual separately executed `python -O` model mutations are rejected at their stated errors; MUTATIONS.json records the stable expected messages. They test wrong functional-equation power/character, using convexity instead of the new ratio, reverting the correction domain, counting at the upper threshold, deleting the last class, deleting the large-frequency gap, and borrowing an incorrect Mellin shift.
- The complete replay.py repeats all four accepting executions, all eight corrupted executions, and the SHA-256 manifest.
- The final archive is freshly extracted and replayed. A separately generated add-only Git patch is applied in a fresh local Git fixture and the same complete replay is performed there.

These are rational finite bookkeeping/transport tests. No actual L-values, zero locations, theta averages, character census or Gaussian quadrature are computed. No numerical optimizer is a proof premise.

## Proof-development checks

The proof was challenged specifically on: the sign of Q^(1/2-w); Q<=C U versus an unjustified Q~U assumption; matching the CONJUGATE numerator character to the denominator; independent ordinates; control of both L and 1/L from the same analytic logarithm; the upper versus lower exceptional threshold; the mixed pole at xi+w=1; the small-frequency z contour; and the large-frequency epsilon gap.

An initial generic strict-Bernstein helper required only one positive Bernstein coefficient. That would not guarantee strict positivity at the right endpoint for an arbitrary polynomial. Before the final reports it was strengthened to require a positive right-endpoint coefficient, with all coefficients nonnegative; all published strict tests passed again. There was no change to the stated moment or contour values. This was a verifier-development correction, not an analytic proof certified by testing.

Exploratory linear-programming grids for several higher-moment approaches were run separately. They did not establish a route to the critical line and are neither theorem dependencies nor certified optimal barriers. The successful certificate uses the explicitly written rational threshold list and the primary second-moment density formulas only.

## Analytic boundaries

The author of the proof also wrote the checker. No separate AI agent, human referee or proof assistant has verified the new argument. The abstract logarithm lemma uses standard complex analysis; the source composition additionally depends on the adopted full CT identity, the #965 short-support reflection, the #971 exact correction-domain reconstruction, and the exact CT/DF family adapter. The primary de Faveri text was inspected at the recorded scope, but its theorem was not rebuilt. CT v2 fresh body retrieval failed. These limitations are stated in SOURCES.md and are not removed by the numerical fraction or the finite checker.

There is no full-repository validator run, upstream Lean build, transitive axiom audit or GitHub CI result. A proposed global consequence is not an independently accepted theorem. RH and the original generalized native inverse-Mobius moments remain unproved by this work.

## Publication

No remote write was performed. GitHub reading and branch inspection worked; the exposed connector actions contain no create/update/push operations. Local DNS tests for github.com and arxiv.org failed. No gh executable or Git credential helper was available. The patch is a tested local handoff, not a claim that a remote branch is synchronized.

Intended base: #975, edbc27b61208ccc7ee1fa99fa3f4e861f5a03452.
Intended branch: research/reflected-zero-free-ratio-20261018.
New directory only: standalone/2026-10-18-reflected-ratio/.
