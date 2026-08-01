# M-16301 — Unified finite Stieltjes extensions and additive/multiplicative zero-measure duality

Claim ID: `M-16301`  
Status: **PROPOSED METHODOLOGY; PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-16`  
Created: 2026-08-01  
Origin: pre-public review of PRs #113–#130  
Scope: integration and search design only; no frozen PR verdict is changed

## 1. One canonical one-node extension theorem

PRs #117, #124, #127, and #128 use four coordinate systems for the same finite truncated-Stieltjes operation.

Let an old positive response functional have moments

\[
 a_k=\int y^k\,d\mu(y),
\]

and adjoin one denominator factor `y+w`, with `w>=0`. Put

\[
 b_k=\int \frac{y^k}{y+w}\,d\mu(y).
\]

The universal recurrence is

\[
 \boxed{a_k=b_{k+1}+wb_k.}
\]

All enlarged moments are affine in the sole new scalar `b_0`. If the residual measure is supported on `[A,infinity)`, the complete degree-bounded positivity test is the intersection of two affine PSD pencils:

\[
 H_0(b_0)\succeq0,
\qquad
 H_A(b_0)=M_a-(w+A)H_0(b_0)\succeq0.
\]

The following existing statements are coordinate/congruence corollaries:

```text
PR #117   w=0 zero-anchor specialization;
PR #124   shifted coordinate z=y+w and two Schur gates;
PR #127   support-aware Markov–Padé interval with A>=0;
PR #128   adapted Geronimus basis and reduced contraction.
```

### Proposed integration rule

Use one canonical theorem for the recurrence and affine pencils. Retain the four interfaces as named corollaries and implementations. Renumber PR #127’s current `L-9312`, which collides with PR #117.

This proposal does not retroactively verify or repair either frozen PR.

## 2. Additive and multiplicative witnesses are dual views of one zero measure

Under RH, both of the following are positive-measure statements over critical-line zero ordinates:

1. PR #125 contracts the resolvent kernel through polynomial ordinate filters:
   
   \[
   \sum_\gamma P(\gamma)|\Phi_v(\gamma)|^2.
   \]
2. PR #129 contracts logarithmic quadratic factors:
   
   \[
   \sum_\gamma \phi_\beta(\gamma),
   \qquad
   \phi_\beta(x)=\sum_{r,j}\beta_{rj}\log((x-T_r)^2+u_{rj}).
   \]

They are not equivalent finite criteria, but they interrogate the same putative positive spectral measure through different transforms.

### Proposed candidate protocol

For a cross-height geometry that produces a small directed moat in either interface:

1. freeze the exact heights and horizontal nodes;
2. build both an additive polynomial Pick packet and a multiplicative direct-`xi` response where the available moment constraints permit;
3. source-bind both to the same primitive normalization and zero-table provenance;
4. require each checker to reconstruct its own analytic response positivity;
5. compare signs and sensitivity ledgers.

Agreement is a strong deterministic normalization and source-consistency check. It is not statistical independence and cannot replace independent primitive reproduction.

## 3. The missing finite-to-global theorem

Every reviewed positive result is finite in at least one parameter:

```text
node count;
polynomial degree;
height set;
slab set;
moment order;
point-cloud dimension.
```

Therefore a sequence of finite positive closures cannot imply RH without an additional theorem.

A genuine global route requires one of the following.

### Disproof-completeness alternative

Prove that if an off-line zero exists, then some finite member of a declared increasing family has a strict negative moat. The theorem must quantify:

- how nodes/heights/slabs are selected from the zero;
- exact rational approximation of the witness;
- preservation of strict negativity under finite approximation;
- source and tail bounds.

### Positive-exhaustion alternative

Embed the finite cones into a known RH-equivalent global positive cone and prove:

- density or compact convergence of the finite test functions;
- uniform control of tails and admissibility;
- closure of the positive cone under the limit;
- compatibility of every normalization and zero-count convention.

Until one alternative is proved, finite positivity is a local exclusion only.

## 4. Proposed implementation consequence

Create one canonical source manifest shared by the moment, Pick, and direct-product checkers:

```text
normalization ID and reviewed parent commit;
exact ordinate/height list;
primitive file SHA-256 values;
count/slab artifact SHA-256 values;
common scale conventions;
node and vector/polynomial digests;
logical gate states with immutable evidence locators.
```

The current checkers often validate exact algebra but merely echo source metadata. A common typed manifest would let the finite kernels remain small while making production promotion fail closed.

## Proof boundary

This file is a proposed synthesis and integration plan. It proves no new RH implication, changes no frozen review verdict, and supplies no Riemann numerical result.
