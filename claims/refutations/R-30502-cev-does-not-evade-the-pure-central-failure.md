# R-30502 — CEV does not evade the known pure-central failure

Claim ID: `R-30502`  
Title: The shift-terminalized eta flow is the pure central producer, whose pointwise positivity is already known to fail at finite endpoints  
Status: **ROUTE-SCOPE CORRECTION**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-30503`; PR #247 `R-23803`  
Scope: pointwise positivity only; subpower optimized debt remains open

## 1. Exact identification

`L-30503` proves for every finite target

\[
D_w^{\eta}=D_w^{\rm central}.
\]

Thus the complete stage-recombined flow produced by the unshifted eta cascade is not a new positive producer. It is the canonical pure central-halving producer written in reciprocal-eta coordinates.

## 2. Imported finite failure

PR #247 `R-23803` records that the pure central descending producer develops negative coefficients at finite endpoints. Therefore

\[
\boxed{
D_{w_X}^{\eta}\not\ge0
}
\]

for all endpoints.

The exact failure does not depend on how the same flow is decomposed into eta stages, analytic profiles, or adjacent-tree commutators. Recombination cannot turn a negative coefficient of the unique central flow into a positive one.

## 3. What remains live

The following statements are distinct:

```text
central producer is coefficientwise nonnegative     false;
central producer has subpower negative capacity      open;
cycle-optimized balanced debt is subpower             open;
```

`T-30501` uses only the second statement through the stronger explicit CEV bound. It does not assert pointwise positivity.

However, a continuation which presents the eta-resolvent recombination itself as a positivity breakthrough is rejected by this mutation. A genuine closing construction must add noncentral Pascal cycles or prove a source-specific debt estimate.

## 4. Strategic consequence

The exact cutoff correction and weighted eta reserve on PR #317 remain useful analytic tools, but the preferred next attack is no longer another central-only recurrence. It is:

\[
\boxed{
\text{eta-resolvent central flow}
+\text{source-bound noncentral cycle transport}
\longrightarrow
\text{subpower optimized Cycle Debt}.
}
\]

## 5. Status

```text
eta resolvent / central producer equality     PROPOSED COMPLETE EXACT
pure central pointwise positivity             FALSE
CEV                                            OPEN / RH-BEARING
cycle-corrected completion                     OPEN
Riemann Hypothesis                             UNPROVEN
```