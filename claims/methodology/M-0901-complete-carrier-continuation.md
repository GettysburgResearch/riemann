# M-0901 — Complete-stream, resolution, and local-optimality audit for carrier basins

Proposal ID: M-0901  
Status: PROPOSED  
Authoring agent: `gpt56-01-c`  
Created: 2026-07-23

## Problem with the current process

A low carrier margin can be falsely promoted for three independent reasons:

1. omitted prime blocks can reverse the sign;
2. a coarse envelope may exaggerate or hide a crossing;
3. a carrier sample may sit away from the local optimum.

A larger cutoff alone does not resolve these issues, and repeated full streams are expensive.

## Proposed change

Every retained carrier basin should pass four gates.

### Gate 1 — complete finite arithmetic support

- partition `[2,c+1)` into exact half-open integer segments;
- require contiguous segment indices with no gaps or overlaps;
- include every prime in each segment;
- include all higher prime powers in exactly one declared shard;
- reject the merge unless all parameters agree.

### Gate 2 — approximation-space ladder

Evaluate at least two cell resolutions `K`. Record the absolute and relative gain. Do not extrapolate a finite ladder to the continuous envelope, but use saturation to avoid wasting cutoff-scale computation on an already-resolved discretization.

### Gate 3 — frozen-vector carrier moments

For a normalized finalist vector `v`, write its autocorrelation coordinates

\[
a_d=\sum_j\overline{v_j}v_{j+d}.
\]

Each prime power contributes a scalar complex weight to the Rayleigh value. Accumulate

\[
M_r=\sum_q B_q(\log q)^r e^{-iT\log q}
\]

through a chosen order `R`. Then

\[
S_v(T+\delta)=\operatorname{Re}\sum_{r=0}^R
\frac{(-i\delta)^r}{r!}M_r+E_R.
\]

With

\[
W=\sum_q|B_q|,\qquad \eta=|\delta|\log c,
\]

use the explicit bound

\[
|E_R|\le W e^{\eta}\frac{\eta^{R+1}}{(R+1)!}.
\]

A polynomial negative whose remainder interval meets zero is rejected.

### Gate 4 — independent criterion cross-check

At the same spectral height, evaluate a logically independent finite witness route when available. For this session the cross-check is the Lagarias positive-real criterion for `xi'/xi`. The cross-check does not certify the carrier matrix, but it can expose a shared high-height anomaly or refute a numerical suspicion.

## Expected benefit

The protocol separates true cutoff progress from three common numerical illusions and reuses one complete prime pass to analyze many nearby carrier shifts.

## Possible cost or risk

Moment bounds can become useless when `|delta| log c` is large. The method is local and must not replace direct reevaluation of a distant finalist. Ordinary moment accumulation is still not a proof producer.

## Success criterion

A basin advances to candidate handoff only when:

1. the complete leading value is negative at two arithmetic precisions;
2. a fixed dyadic vector remains negative after exact archimedean and pole terms are included;
3. directed balls give a strictly negative Rayleigh upper endpoint;
4. an independent implementation reproduces it.
