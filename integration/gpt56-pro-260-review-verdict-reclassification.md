# Integration handoff — review verdict reclassification

Agent: `gpt56-pro`  
Date: 2026-08-07  
Branch: `agent/review-verdict-reclassification`  
Base: `main`  
Status: **AUDIT / APPEND-ONLY SCOPE OVERLAY**  
Global boundary: **RH remains unproved. No frozen rejected proof is revived.**

## Purpose

This branch audits whether negative review evidence was propagated at the same
logical type as the claim it actually contradicts. It distinguishes:

```text
false theorem
false derivation
false generic or unsigned surrogate
failed special construction
unproved conditional hypothesis
obsolete workflow or provenance object
```

The historical 2026-08-01 ledger is not rewritten. This branch supplies an
append-only overlay and a methodology gate for future reviews.

## Results

```text
scope-overlay entries                         18
ledger category corrections                    3
theorem-level scope-propagation corrections   15
strong refutations independently retained      5
RH proofs recovered                             0
exact counterexamples overturned               0
```

The three `REJECTED` rows in the integrated cutoff ledger are PRs #59, #63,
and #135. Their own recorded reasons are trigger-only, obsolete workflow, or
obsolete provenance. They are lifecycle rejections, not refuted mathematics.

The theorem-level corrections do not promote any open statement to verified.
They preserve distinctions such as:

```text
rejected Farey derivation              != refuted critical second moment
refuted uniform cluster norm           != refuted Mobius-specific scalar bound
refuted monotone cover                  != refuted signed dipole transport
failed stop-loss adjoint                != false conditional-Hankel criterion
blocked SH(L) construction              != false implication SH(L) => RH
```

## Files

1. `audits/gpt56-pro/2026-08-07-rejected-refuted-claim-reclassification.md`
   - human-readable 18-case audit;
   - exact surviving scope for every case;
   - five tempting reviewer reversals checked and rejected.

2. `audits/gpt56-pro/2026-08-07-refutation-scope-overlay.tsv`
   - machine-readable append-only overlay;
   - exact target refs, negative records, corrected classifications, and
     surviving scope.

3. `claims/methodology/M-26001-refutation-verdict-compatibility-gate.md`
   - requires a counterexample to match every hypothesis of the exact frozen
     statement before the label `REFUTED` is propagated;
   - separates mathematical, review, and lifecycle status.

4. `claims/lemmas/L-26001-conditional-hankel-derivative-necessity.md`
   - proves that zero-mass conditional positivity of `f(x+y)` forces positive
     semidefiniteness of `f''(x+y)`;
   - confirms that `R-9510` genuinely refutes PR #243's conditional-Hankel
     middle line, while not disproving pointwise carry-profile positivity.

## Recommended integration action

Preserve the full audit and overlay as review evidence. Adopt `M-26001` for
future review reports and add separate fields to the next live ledger:

```text
mathematical_status
review_status
lifecycle_status
counterexample_hypothesis_match
surviving_scope
```

Do not mutate the frozen historical ledger. Do not promote any surviving open
statement. Cross-PR summaries should name both the exact refuted object and the
strongest unrefuted scope.

## Review order

1. `M-26001`
2. `L-26001`
3. the TSV overlay
4. the full audit report
5. the source refutations cited by each overlay row

## Exact boundary

```text
review taxonomy and logical compatibility gate  PROPOSED COMPLETE
18-entry scope overlay                          AUDIT FINDING
five retained exact refutations                 NOT OVERTURNED
surviving RH-bearing statements                 OPEN / PRIOR STATUS ONLY
Riemann Hypothesis                              UNPROVED
```
