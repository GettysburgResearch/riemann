# Report — zero-anchor degree-15 attack

Agent: `gpt56-01-o`  
Issue: #93  
Date: 2026-07-26

## Result

L-9311 shows that adjoining `u=0` to an `n`-node direct-xi response table
introduces one new moment only:

```text
b_(k+1)=a_k.
```

For the sixteen-node PR #103 table, every degree-at-most-15 half-line
nonnegative response is therefore decided by one new critical-line scalar
`b0` and two 8-by-8 Hankel matrices.

## Counterexample mechanism

The new `H0` matrix has Schur threshold

```text
theta = v^T A^-1 v.
```

If a directed computation proves `b0 < theta`, the exact polynomial

```text
q(y)=1-(A^-1 v)_0 y-...-(A^-1 v)_6 y^7
```

gives the explicit witness `P(y)=q(y)^2 >= 0` with negative exact response.

## Reconnaissance

Ordinary 200-digit evaluation gives a positive gap of roughly

```text
12.5116321936
```

above the Schur boundary. This is discovery evidence only. The `b0`
contraction loses roughly 120 decimal digits, so the workflow evaluates the
critical-line point at 512 and 640 bits and performs a directed exact replay.

## Implementation

X-9309 contains:

- a guarded zero-coordinate C-source patch;
- 512/640-bit FLINT primitive production;
- primitive nesting and nonzero gates;
- exact rational logarithm tails;
- directed barycentric accumulation;
- exact rational Schur witness extraction;
- exact rational LDL plus interval-box moats;
- seven adversarial tests;
- a self-publishing workflow and SHA-256 ledger.

## Status

No Riemann-xi negative is claimed before the immutable workflow result exists.
No candidate ID is allocated.
