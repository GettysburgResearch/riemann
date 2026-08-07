# M-15405 — Eta-window and reflection-linearized positive programme

Claim ID: `M-15405`  
Title: Replace the ratio-64 double prime-pair problem by a ratio-8 parity stream and a linear Selberg contour ledger  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15414`, `L-15415`, `T-15406`  
Scope: positive-only continuation of Issue #180

## Executive reduction

The previous triangular programme used `h=log 4`, integer contrast coefficient
`2`, and a ratio-64 active annulus. `L-15414` shows that the whole construction
works for every fixed `h>0`.

The recommended proof-facing specialization is

```text
h = log 2,
contrast coefficient = sqrt(2),
active annulus ratio = 8.
```

Its pole factor is exactly the Dirichlet-eta factor `1-2^(1-s)`. It admits
three independent producers:

1. one direct ratio-8 signed triangular prime-power window;
2. four cumulative hinge values in `Q(sqrt(2))`;
3. triangular smoothing of the explicit parity stream
   `Lambda(N)-2 Lambda(N/2)`.

The eta alignment does not prove the critical estimate. It reduces the
arithmetic footprint and exposes one exact parity covariance in the probability
region.

## Reflection-linearized energy

The required prime-side mean square contains a quadratic double prime-power
sum. `L-15415` gives the exact meromorphic identity

```text
F(s)F(1-s)
 = -F'(s)-zeta''(s)/zeta(s)-X(s)F(s),
F=-zeta'/zeta,
X=chi'/chi.
```

The coefficient stream of `zeta''/zeta` is

```text
Lambda(n) log n + (Lambda*Lambda)(n) >= 0.
```

After a vertical integration by parts, a reflected weighted energy therefore
uses only:

- one ordinary von Mangoldt stream;
- one positive Selberg stream;
- one explicit gamma/archimedean convolution;
- one contour-residue ledger.

This is the new proof architecture. The bulk `X^2` prime-pair bookkeeping is
linearized exactly; the RH content is isolated in the contour defect between a
positive Hardy norm and its reflected bilinear form.

## Stage A — exact ratio-eight producer

For every exact translation `x`:

1. enumerate every prime power in `[exp(x-3h),exp(x)]`;
2. evaluate the three affine pieces of the eta triangular window outwardly;
3. replay the four hinges with exact coefficients in `Q(sqrt(2))`;
4. replay the parity-von-Mangoldt coefficient stream;
5. require all directed intervals to overlap;
6. preserve a duplicate-free manifest and breakpoint convention.

The smaller annulus is useful for long exact mean-square blocks and for testing
candidate reflection identities. It does not change the theorem strength.

## Stage B — single Selberg-stream replay

For a vertical line `Re s=c>1`, use the symmetric weight

```text
W_G(s)=Ghat(s-1/2) Ghat(1/2-s).
```

Compute the right side of `L-15415.10` from:

1. the finite/rapidly convergent von Mangoldt contraction;
2. the nonnegative coefficients
   `Lambda log + Lambda*Lambda`;
3. directed `chi'/chi` and its convolution with `F`;
4. the derivative transferred to `W_G'` by integration by parts.

This gives an independent linear replay of the reflected quadratic form. No
prime-pair manifest is trusted.

## Stage C — contour-strip ledger

Move the contour from `Re s=c>1` toward the critical line. The certificate must
record separately:

- the canceled zeta pole at `s=1`;
- every trivial-zero residue;
- every nontrivial-zero residue or indentation term crossed;
- horizontal-edge bounds;
- the final reflected boundary value.

No assumption that all crossed zeros lie on the critical line is permitted.
The ledger may consume already certified critical-line zero balls, but every
unresolved region remains an interval contribution.

## Stage D — exact positive hinge

Let `H_G(sigma)` be the Abel--Hardy energy of `T-15406`, and let `R_G(sigma)`
be the reflected bilinear energy supplied by `L-15415`. The missing theorem is a
uniform estimate for the defect

```text
Delta_G(sigma)=H_G(sigma)-R_G(sigma)
```

after the contour ledger is inserted.

Promising forms are:

1. a Pick/de Branges Gram representation of `Delta_G`;
2. a matrix-valued von Mangoldt-chain carré du champ;
3. a signed Selberg flow whose only noncompact channels are zero residues;
4. a finite-section Loewner inequality stable under the `sigma->0` limit.

A scalar absolute-value estimate is disallowed: `L-15411` proves it loses an
order-`X^2` cancellation.

## Stage E — proof-producing finite experiments

For exact finite blocks, retain four ledgers:

```text
positive Hardy Gram,
reflected Selberg replay,
contour/residue contribution,
remaining defect.
```

Use rational/dyadic frozen vectors and exact piecewise integration. A finite
pattern is reconnaissance until one symbolic all-support estimate is proved.

The first empirical question is not merely whether `Q_h` is small. It is
whether the directly computed defect has a stable positive Gram factorization
as the block and translation grow.

## No-go gates

Reject any proposed completion that:

- invokes `|epsilon_2|<=1` after leaving the real half-plane `s>1`;
- replaces `F(s)F(1-s)` by `|F(s)|^2` for `Re s!=1/2`;
- shifts a contour without a zero-residue ledger;
- applies positivity of the Selberg coefficients to the full signed reflected
  expression;
- bounds diagonal and off-diagonal prime terms separately;
- proves a bound only for `sigma>=sigma_0>0`.

## Success condition

Either of the following finishes the positive route:

```text
sup_(sigma>0) H_G(sigma) < infinity,
```

or, equivalently,

```text
sup_(X>=1) X^-1 integral |Q_h(x)|^2 dx < infinity.
```

Through `T-15406`, either statement proves RH. `M-15405` supplies a smaller
producer and a linearized bulk identity; it does not prove the final defect
estimate.
