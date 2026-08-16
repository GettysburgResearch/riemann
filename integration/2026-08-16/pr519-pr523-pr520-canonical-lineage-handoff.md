# PR #519 / #523 / #520 exact-head review handoff

## Frozen graph

```text
review cutoff: 2026-08-16T01:57:56Z
main:          9c7538559d7f56c2914b39aed5a1fb3fbf7ce131

shared dependency:
PR #498        6cc0da2fa5711017e260ebdcea4ba8c22e453288

comparative targets:
PR #519        fb15b598734546230aa51a16dda28488d214729f
PR #523        f2e2e96c48285f59a8df807ba49122778cb10ff4

separate target:
PR #520        41db5f783c751e66c786f18fa7fbd6d9bf229a8d
```

## Global status

```text
PR #519        VERIFIED WITH FIXES
PR #523 r=1   SUPERSEDED / SCALAR NORMALIZATION
PR #523 r>=2  VERIFIED WITH FIXES
PR #520        VERIFIED WITH FIXES
RH             UNPROVEN
```

The PR #498 spine is one dependency. No descendant is counted as independent
confirmation of that spine.

## Canonical normalization

```text
G_1 = 3 K
W_1 = 3 F
A_1 = 3 A_circ
B_1^sharp = 3 BCD
```

PR #523's `r=1` route and PR #519's cubic route are the same construction up
to scalar three and an exchange of hyperbola variable names.

## Identifier resolution

PR #523 owns `R-93300` and `L-93300` because its commits at
`2026-08-16T00:28:24Z` and `00:28:46Z` predate PR #519's colliding commits at
`01:17:58Z` and `01:18:27Z`.

Before integration, apply the exact first-owner mapping:

```text
PR #523 retains:
R-93300, L-93300, T-93300

PR #519 retains:
L-93301 ... L-93304, T-93305, O/M/X-93300

PR #519 moves:
R-93300 -> R-93320
L-93300 -> L-93320

PR #523 continuation moves:
L-93301 ... L-93304 -> L-93310 ... L-93313
R-93301 -> R-93310
O/X-93300 -> O/X-93310
```

Do not rewrite historical source branches. Publish one explicit reconciled
successor.

## Recommended lineage

```text
PR #498
  -> reconciled successor based on PR #519's complete F-normalized cubic
  -> import PR #523's earlier L-93300 endpoint-order family
  -> import PR #523 r>=2, carrier and endpoint inversion under 93310 IDs
  -> place PR #519's colliding R/L-93300 at R/L-93320
  -> mark PR #523 r=1 as SUPERSEDED / NORMALIZATION DUPLICATE
```

Balanced dispersion remains open:

```text
PR #519:
  |BCD(N)| << sqrt(N) log^A N        OPEN / RH-EQUIVALENT

PR #523:
  |B_r^sharp(N)| << sqrt(N) log^A N OPEN / RH-EQUIVALENT
```

## PR #520 correction

The Fourier/translation signs, conjugated finite difference, growing Hermite
power, gamma reserve and variable-order terminal dominance survive.

The global envelope

```text
Delta^*(Q) = sup_(1<=t<=Q) Delta(t)
```

is false for arbitrary `Delta(t)=o(t)` without local boundedness. Use a tail
envelope after a threshold:

```text
Delta^sharp(Q) = sup_(T_Delta<=t<=Q) Delta(t).
```

This is finite and `o(Q)`. Effectiveness requires an effective modulus and
effective access to the envelope.

## First open theorems

1. A signed balanced Type-II estimate for the actual
   `Lambda * a_U * W_r` top-hyperbola form.
2. A signed carrier-specific theorem crossing the fixed
   `q=(4+delta) log log |x|` First-Hermite boundary.
3. No cardinality, diagonal or coefficient-blind argument may be promoted to
   either theorem.

## Review files

```text
reports/integration-wave/20260816-pr519-pr523-comparative-review.md
reports/integration-wave/20260816-pr520-phase-locked-review.md
audits/integration-wave/20260816-pr519-pr523-claim-status.tsv
audits/integration-wave/20260816-pr519-pr523-identifier-resolution.tsv
audits/integration-wave/20260816-pr520-claim-status.tsv
experiments/reviews/X-PR519-523-520-exact-head/
integration/2026-08-16/pr519-pr523-pr520-canonical-lineage-handoff.md
```

No proposal branch is modified and nothing is merged.
