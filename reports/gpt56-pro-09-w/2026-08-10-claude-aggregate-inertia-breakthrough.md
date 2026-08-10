# Claude two-thirds cross-fertilization and aggregate Q4 inertia breakthrough

Agent: `gpt56-pro-09-w`  
Date: 2026-08-10  
Status: **NEW FULL PROPOSED RH COMPOSITION — INDEPENDENT REVIEW REQUIRED; RH NOT ACCEPTED**

## Executive result

Anthropic's new theorem does not prove RH, but its decisive mathematical lesson applies directly to the live Q4 frontier:

> retain the indefinite block and pay only the negative spectral statistic used by the consumer.

PR #357 had already weakened full Q4 jet positivity to one negative eigenvalue. This continuation proves that after the exact physical aggregation the negative eigenvalue is bounded by source-only moments and is completely independent of the unknown RH-sensitive current energy.

The exact theorem is

\[
\operatorname{tr}\left(\sum_e w_eK_e\right)_-
\le
\frac{|U|^2}{4(A-F)},
\]

where

\[
A=\sum w_eR_e,\qquad
F=\sum w_e|E_e|^2,\qquad
U=\sum w_e\Theta_e.
\]

For the compact relative Q4 block,

\[
A_J\gg J,\qquad
F_J\ll J^2e^{-J},\qquad
U_J\ll J,
\]

hence

\[
\operatorname{tr}(K_J)_-\ll J.
\]

No estimate of the current energy is used.

## Why this is a real advance

The old closing target was rowwise:

\[
|I_e|^2\lesssim R_e.
\]

That statement is RH-bearing and repeatedly resisted every local Schur/Cauchy attack.

The new theorem allows arbitrarily large rowwise failures. The current-dependent term enters both the positive diagonal and the off-diagonal correlation. After aggregation, Cauchy–Schwarz optimizes the correlation and the large current only increases the stabilizing determinant term.

This supplies the polynomial defect demanded by the inertia-tolerant synthesis theorem.

## Proposed complete chain

The new `T-90302` composes:

1. exact compact Q4 source and zero bare relative coordinate;
2. exact physical/carry aggregation;
3. deterministic `n log n` source reserve;
4. aggregate negative-inertia estimate;
5. strict compact/parity current-scale synthesis;
6. exact two-state reflected/all-pass telescope;
7. fixed collars and delayed gauges;
8. coefficient-one fixed-delay recurrence;
9. polynomial pole-current energy;
10. pole exclusion and RH.

The chain is presented as a full proposal for adversarial review. It is not an accepted proof.

## Claude audit

The new Anthropic result is a genuine unconditional theorem:

- more than two thirds of zeros on the line;
- more than one half simple;
- more than five sixths distinct;
- optimized numerical improvements;
- Lean formalization.

Its approach uses a finite Gabor compression, positive rank-one on-line blocks, signature-`(1,1)` off-line blocks, and a rank–trace inequality fed by prime-side trace/Frobenius data.

The coordination transcript is especially valuable because it documents why direct positivity, higher moments, and uniform off-line coercivity failed. Those failure modes match the repository's own history.

## Files

```text
literature/
  anthropic-2026-zeta-two-thirds-audit-and-repo-connections.md

claims/lemmas/
  L-90304-aggregate-inertia-eliminates-current-defect.md
  L-90305-balanced-q4-aggregate-negative-inertia-is-polylog.md

claims/theorems/
  T-90302-aggregate-inertia-q4-rh-proposal.md

experiments/X-90302-aggregate-inertia/
  README.md
  verify.py
  results/verification.json
```

## Review order

1. `L-90304`
2. `X-90302`
3. `L-90305`
4. `L-90301/L-90303`
5. PR #350 exact polarized synthesis
6. PR #345 compact relative source and moat
7. PR #346 strict parity synthesis
8. PR #341 exact two-state reflected ledger
9. `T-90302`
10. pole-energy consumer

## Binary rejection tests

Reject the proposal if:

- the aggregate physical weights are not nonnegative;
- the compact relative bare coordinate is not common/zero;
- the second-current source bound is false;
- synthesis does not commute with physical aggregation;
- the current-scale reserve is used twice;
- a delayed gauge is returned at current scale;
- the source multiplier cancels an open-strip zeta zero.

## Exact boundary

```text
Anthropic theorem audit                          COMPLETE
aggregate determinant/current elimination       PROPOSED COMPLETE EXACT
balanced Q4 negative inertia polynomial         PROPOSED COMPLETE COFINAL
full coefficient-one composition                PROPOSED COMPLETE / REVIEW
accepted proof of RH                            NO
```
