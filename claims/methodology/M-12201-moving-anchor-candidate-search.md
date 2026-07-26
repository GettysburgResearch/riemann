# M-12201 — Moving-anchor candidate search

Claim ID: M-12201  
Title: Search an enlarged direct-xi response cone using one new primitive per anchor  
Status: PROPOSED  
Authoring agent: `gpt56-05-j`  
Created: 2026-07-26  
Dependencies: L-12201; T-12202; L-12203; L-12204  
Scope: proof-producing moving-anchor searches on stored direct-xi moment tables

## Objective

Exploit one proof-grade degree-even response table repeatedly. Each candidate pair `(ordinate shift, anchor t)` requires only one new direct completed-xi point, while all other degree-odd moments are inherited exactly.

## Gate 1 — Old-table closure

Require:

- exact node and normalization fingerprints;
- directed old moments `a_0,...,a_(2m)`;
- exact positivity certificates for the inherited blocks used by T-12202;
- the complete count-deflation provenance of the old functional.

If the old degree-even cone is unresolved, do not launch moving-anchor promotion.

## Gate 2 — Deterministic anchor ladder

Begin with

```text
t in {1, 4, 16, 64, 256}
```

and every stored ordinate shift. These anchors cover:

- a near-line Riemann-Siegel control (`t=1`);
- an easy-half-plane cross-backend control (`t=4`);
- a balanced conditioning ladder;
- an upper-Schur stress test (`t=256`).

Additional rational anchors are inserted only around the smallest dimensionless boundary distance.

## Gate 3 — One new primitive

Evaluate

\[
 F_T(t)=\log\left|\xi\!\left(\frac12+\sqrt t+iT\right)\right|^2
       -\text{the exact inherited deflation profile}.
\]

For `sqrt(t)+1/2>1`, prefer a directed Euler-product or Dirichlet-series implementation independent of the old Riemann-Siegel producer. Preserve the same completed-xi scale exactly or form a scale-free point difference.

## Gate 4 — Dual reconstruction

Compute `c_0` by both:

1. the direct `(n+1)`-point barycentric contraction;
2. L-12204's one-point-difference-plus-old-moments formula.

Reject nonoverlapping intervals. Intersect overlapping intervals before the sign test.

## Gate 5 — Two-Schur decision

Use directed old moment intervals and exact rational linear algebra to enclose

\[
 \theta_0,
 \qquad
 U_t=\frac{A_0-\theta_1}{t}.
\]

Compute

\[
 I_{\rm lower}=I(c_0)-I(\theta_0),
\]

and

\[
 I_{\rm upper}=I(U_t)-I(c_0).
\]

The verdict is:

```text
upper(I_lower) < 0  -> LOWER_SQUARE_NOMINATION
upper(I_upper) < 0  -> UPPER_SHIFTED_SQUARE_NOMINATION
lower(I_lower) >= 0 and lower(I_upper) >= 0 -> CERTIFIED_TABLE_POSITIVE
otherwise -> UNRESOLVED
```

A nomination exports the exact rationalized witness polynomial and directly contracts it against the primitive rectangles. The Schur computation is discovery and cross-check; the final sign is a fixed-polynomial interval.

## Gate 6 — Width consistency

Reconstruct the L-12203 width polynomial `R_t`. Its old-table interval must overlap

\[
 t(U_t-\theta_0).
\]

A negative upper endpoint for the width is a dependency or implementation failure, because the inherited degree-even table already certifies `R_t>=0`.

## Gate 7 — Candidate ranking

When both walls remain positive, rank by

\[
 \rho_t=\frac{c_0-\theta_0}{U_t-\theta_0}
\]

and retain both distances

\[
 \rho_t,
 \qquad 1-\rho_t.
\]

Do not rank by raw absolute slack alone: L-12203 shows that the interval width can collapse rapidly as the anchor moves right.

For interval data, use a conservative rational enclosure of `rho_t` only after proving the width lower endpoint positive.

## Gate 8 — Precision escalation

A direction-specific uncertainty ledger identifies contributions from:

- the new point rectangle;
- the reference point rectangle;
- each old moment;
- Schur solves;
- logarithmic scale and deflation terms.

Refine the largest weighted contributors first. Stop when one wall is strictly separated or the configured precision cap is reached.

## Gate 9 — Promotion boundary

A strict moving-anchor negative remains only a proposed RH witness until:

1. the direct-xi primitive is independently reproduced;
2. the old moment and count-deflation artifacts are independently replayed;
3. L-9308/L-9309/L-9310 and T-12202 are adversarially reviewed;
4. the fixed witness polynomial is contracted by a small independent checker;
5. normalization and scale fingerprints agree.

Only then may a `Z-####` candidate be allocated.

## Cross-avenue inspiration

- PR #117 supplies the one-new-moment zero-anchor architecture.
- PR #110 shows that intrinsic support scales can be much better conditioned than inherited microscopic grids.
- PR #103 supplies many ordinate shifts whose primitives can be reused.
- The easy-half-plane moving points offer an arithmetic backend independent of the high-carrier Riemann-Siegel core.

## Suggested production work

1. certify the `t=4` control at the `483/1024` shift;
2. scan the five-anchor ladder across every stored PR #103 shift;
3. freeze the best lower-wall and upper-wall nominees;
4. request new direct-xi points only near those nominees.