# Post-density-drift consolidation of the carry/Möbius RH programme

Date: 2026-08-08  
Agent: `gpt56-08`  
Branch: `agent/gpt56-08/267-affine-green-boundary-lift`  
Status: **REVIEW-READY CONDITIONAL SPINE; RH UNPROVED**

## Executive conclusion

The live repository is not finished as an unconditional proof of RH.

A late stress test is decisive: the prime-only queue proposed on this branch has a deterministic positive drift of order

\[
\sqrt X/\log^2X.
\]

That route has been withdrawn rather than passed forward as the final theorem.

The corrected consolidation is materially stronger and cleaner:

```text
finite positivity / transport geometry          closed at proposed-exact scope
prime-only queue subpower rate                  proposed refuted
one safe inverse-zeta source omega_2             explicit
parity analysis frame and finite reconstruction explicit
negative carry rows                              confined to quotient cells 2,3,4
actual generalized-prime source                  explicit positive synthesis
carry-space Schur reserve                        uniform and explicit
physical two-frequency source-image map          open
strict source-image recurrence                   open
```

The remaining object is named `SIFD` in `T-26704`.

## 1. What the carry programme has actually completed

### Positive finite geometry

- Every signed feasible state has an explicit affine prime-boundary lift.
- The least affine charge has an exact finite dual.
- The ordinary-prime system admits a nonnegative correction with objective exactly equal to the actual ordinary-prime ramp.
- The parabolic seed is already a positive carry-row combination and admits positive endpoint atoms.
- Green, Skorokhod, endpoint-scale, and constraint-dipole coordinates are now interfaces for constructing or measuring the same scalar, not independent proof obligations.

This resolves the geometric question “can the finite object be made positive?” It does not resolve the arithmetic question “is its objective at least `4 sqrt(X)-X^o(1)`?”

## 2. The queue correction

The exact consecutive-prime queue and its max-flow/min-cut characterization remain useful finite algebra.

However, prime-to-prime blocks conserve total ordinary-prime incidence. Prime sampling of the zero-mass continuum defect has the first density correction

\[
4(1-\gamma)\frac{\sqrt X}{\log^2X},
\]

which must be exported by every such transport. Therefore the queue cannot be subpower.

This correction removes an apparent final theorem and prevents an invalid review handoff.

## 3. Why squarefree collectors are not yet a proof

Squarefree composite endpoints are exactly neutral on every proper prime power and can compress ordinary-prime incidence. This fixes the finite obstruction to prime-only transport.

But their complete Farkas dual retains the logarithmic ray `y_p=log p`, whose pairing is the prime-ramp discrepancy itself. Consequently the all-scale squarefree collector theorem remains RH-bearing. It is an alternative producer, not an unconditional closure.

## 4. The canonical fixed source

The source

\[
\omega_2
=
\mu-rac32\delta_2*\mu+rac12\delta_4*\mu
\]

is now the preferred common coordinate because it simultaneously has:

- a reciprocal-zeta Dirichlet multiplier with no open-strip cancellation;
- four complete opposite-parity layers;
- a positive Dirichlet inverse;
- nonnegative generalized prime weights;
- a three-atom binary-digit dual;
- a compact two-row averaged carry image;
- a compact pointwise factor-five carry wavelet;
- finite synthesis from a parity-paired Euler frame.

The fixed bottom functional

\[
5c_X(2)+3c_X(3)
\]

is a valid RH consumer, but its sign remains open. It is not separately assumed in the consolidated spine; `SIFD` is intended to produce the shell estimate that controls it.

## 5. What remains in SIFD

The carry-side source has already been localized and supplied with a strict reserve. The missing theorem is a congruence between two explicit finite objects:

1. the independent-frequency physical factor-ratio matrix from PR #241;
2. the generalized-prime carry-feature matrix on quotient cells `2,3,4`.

A valid proof must produce the map, every boundary row, and a strict recurrence. The required inequality is not a generic operator norm: it is restricted to the complete parity-paired source image and must preserve every cross term.

The decisive quantitative condition is

\[
\sum_r\theta_r<\kappa_0,
\]

where `kappa_0` is the explicit carry reserve and `theta_r` are the complete lower-block charges.

## 6. Why the existing exact results do not automatically imply SIFD

- A positive Selberg coefficient sequence gives forcing, not an upper bound.
- A carry-space reserve does not identify the physical source metric.
- Finite Bezout reconstruction preserves the source but does not bound the transition matrix.
- Factor-five sign localization is a scalar/carry statement, not a physical normal-Gram congruence.
- Complete-fiber half-pole nullity removes a false boundary charge but does not account for all quotient collars.
- Finite positive matrices at selected levels cannot establish the uniform recurrence.

These are precisely the checks a cautious reviewer should apply.

## 7. Review package

Primary new files on this branch:

```text
claims/refutations/
  R-26702-prime-tail-queue-subpower-fails.md

claims/theorems/
  T-26703-prime-tail-queue-rh-proposal.md       [corrected / superseded]
  T-26704-consolidated-parity-factor-five-review-spine.md

reports/gpt56-08/
  2026-08-08-post-drift-consolidated-rh-review.md
```

Inherited finite construction files remain valuable:

```text
L-26701  affine oversupport lift
L-26702  least-charge dual and Green/dipole bridge
L-26703  zero-tax positive ordinary-prime deformation
L-26704  exact prime-tail queue/min-cut algebra
L-26705  fixed-ratio tail localization
X-26701  exact rational affine/Green replay
```

## 8. Recommended adversarial order

1. Audit PR #274 `R-27302` and determine whether the queue refutation is valid.
2. Audit PR #241 `L-9518`, especially the independent-frequency normalization.
3. Audit the parity frame and Bezout reconstruction on PR #263.
4. Audit `omega_2` source identities, factor-five localization, and generalized-prime synthesis on PRs #268/#269.
5. Audit the carry reserve independently.
6. Ask for the missing SIFD source map. If it is absent, the proof is incomplete regardless of every prior exact identity.
7. If a map is produced, audit every collar and the strict reserve-minus-charge inequality.
8. Only then review the recurrence-to-RH transfer.

## 9. Final status

```text
Full unconditional proof of RH          NO
Review-ready corrected proof spine       YES
Prime-only queue completion              WITHDRAWN / PROPOSED REFUTED
Single canonical open producer           SIFD
Conditional SIFD-to-RH implication       COMPLETE PROPOSAL
```

The correct pre-public statement is:

> The repository has reached a sharply consolidated conditional proposal with one explicit physical source-image transition theorem still unproved. It has not reached a full unconditional proof of RH.
