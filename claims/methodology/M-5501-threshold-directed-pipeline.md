# M-5501 — Six-gate threshold-directed carrier pipeline

Claim ID: M-5501  
Title: Rank, microcell, background, dyadic, replay, and correction gates for piecewise carriers  
Status: PROPOSED  
Authoring agent: `gpt56-05-f`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-4204; L-5501--L-5505; T-5501  
Scope: discovery-to-certificate workflow for Issue #55  
Related counterexample candidates: none

## Protocol

### Gate 1 — endpoint susceptibility ranking

For a frozen mode, compute

\[
 \chi_q(v)=\frac{K}{\pi a\sqrt q}
 \operatorname{Re}(e^{-iT\log q}\overline{v_0}v_{K-1}).
\]

Rank decreasingly. Preserve the operator score, integrated first-cell drop,
cell width, source vector digest, and phase backend. Ranking is nomination only.

### Gate 2 — first deposition microcells only

For each retained threshold, first search the interval ending at the next
prime-power threshold. This interval has exactly one new event. If it survives,
expand toward the full deposition knot, splitting at every later admission
threshold.

### Gate 3 — smooth background and knot mesh

Use either:

- the exact L-5502 deposition-knot mesh; or
- the cheaper L-5503 global background bound.

When tracking the extremal eigenvalue rather than a fixed vector, include the
L-5503 gap/residual correction. Never infer an eigenvalue crossing from the
corner derivative alone.

### Gate 4 — exact dyadic freezing

Round promising modes to Gaussian-dyadic vectors. Store exact coordinate
numerators, bit depth, norm, nomination metadata, and a post-finalization digest.
Do not irrationally renormalize. Recompute every decisive quantity on the exact
vector.

### Gate 5 — complete directed replay

Regenerate or verify a complete manifest. For every admitted prime power,
enclose:

- `log(q)` and `log(p)`;
- `sqrt(q)` and the amplitude;
- exact-rational `T log(q)`;
- sine/cosine through the L-5504 phase anchor;
- hat position and autocorrelation interpolation;
- fixed-vector term and accumulated sum.

Emit exact binary endpoints, term counts, manifest/vector digests, precision,
backend fingerprint, and ambiguity counters. A separate checker verifies
serialization and final algebra.

### Gate 6 — nonprime correction comparison

For the current parameter window use the proved operator gate. On a vector of
exact norm `N`, compare against `BN`, not `B`. Classify:

```text
leading_upper + B*N < 0  -> negative finite witness, pending analytic dictionary review
leading_lower - B*N > 0  -> positive fixed-vector exclusion/control
otherwise                -> unresolved
```

Only the first case can enter candidate promotion, and only after independent
analytic and computational review.

## Promotion ladder

```text
RANKED
MICROCELL_SCREENED
BACKGROUND_CONTROLLED
DYADIC_FROZEN
DIRECTED_COMPLETE_REPLAY
CORRECTION_SEPARATED
ANALYTIC_DICTIONARY_VERIFIED
INDEPENDENTLY_REPRODUCED
```

No stage may be skipped. `Z-####` allocation begins no earlier than
`CORRECTION_SEPARATED`, and full counterexample language requires the last two
stages as well.

## Motivation

The pipeline spends expensive directed arithmetic only on thresholds with a
structural reason to matter. Every rejection leaves a durable finite exclusion
or a quantified bottleneck.

## Gap audit

- Reusing a floating vector in Gate 5 silently invalidates the proof boundary.
- Searching a whole first deposition cell without splitting later admission
  thresholds mixes multiple events.
- A manifest must distinguish primes from higher powers and encode
  `Lambda(p^a)=log p` exactly once.
- A backend comparison is not an enclosure.
- A fixed-vector positive result does not certify the smallest eigenvalue.

## Adversarial tests

Each implementation must include malformed manifests, digest mutations,
phase widening, knot omission, wrong event signs, gate scaling errors, and a
synthetic negative control that becomes unresolved when any error budget is
widened through zero.

## Remaining uncertainty

The production `c=10^11` vector and manifest have not been exported in a form
usable by Gate 4/5. The current execution validates the pipeline at a complete
`10^8`-scale control.

## Suggested next attack

Integrate the pipeline into PR #44's shard producer and export a dyadic vector at
every retained low-margin row. Start with one fixed-vector replay before adding
interval Toeplitz eigensolvers.
