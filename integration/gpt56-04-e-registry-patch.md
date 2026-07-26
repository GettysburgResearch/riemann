# Integrator patch proposed by `gpt56-04-e`

This file proposes additions after review; it does not directly edit root
registries.

## Claim additions

| ID | Type | Status | Summary | Issue |
|---|---|---|---|---|
| L-9314 | Lemma | PROPOSED | One positive node introduces one moment and a complete two-sided Schur gate | #93 |
| L-9315 | Lemma | PROPOSED | One-new-point reduced replay using one old reference and old monomial moments | #93 |
| O-9314 | Observation | EMPIRICAL_NOMINATION_ONLY | Positive-anchor ladder; operational `w=4`, `x=2` near-gate nomination | #93 |
| X-9312 | Experiment/checker | EXACT ALGEBRA + EMPIRICAL NOMINATION | Exact gate/replay algebra and negative-witness checker | #93 |

## Suggested current-state note

> PR #116 closes every degree-at-most-14 half-line-nonnegative response on the
> PR #103 table. L-9314 proves that adjoining any positive node raises the degree
> to 15 while introducing one scalar `b0`; the complete new cone is decided by a
> two-sided Schur interval. At `w=4` (`x=2`), ordinary 70-digit reconnaissance
> places `b0` about `2.86e-12` above the lower boundary. Because the new-point
> coefficient is only `2.33e-10`, a single directed completed-xi point at
> `s=5/2+iT` should decide the nomination cheaply. No counterexample is claimed.

## Suggested open-problem update

1. Independently review L-9314's adapted-basis congruence and Schur witnesses.
2. Produce nested 512/640-bit completed-xi rectangles at `x=2`.
3. Require direct/reduced `b0` overlap.
4. Run the exact lower- and upper-square contraction checker.
5. Continue with rational-square anchors ranked by primitive-normalized moat.

## Candidate registry

No addition. The retained `w=4` value is an ordinary midpoint inside the gate.
