# M-20202 — `r`-adic full-problem attack

Claim ID: `M-20202`  
Status: `PROPOSED RESEARCH PROGRAM`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Depends on: `T-20203`, `L-20202`–`L-20204`; PRs #216 and #219  
Scope: a cofinal proof programme, not a finite RH claim

## Objective

For one fixed integer `r>=2`, prove

\[
 \left(-\mathcal H_r(n)\right)_+=n^{o(1)},
 \qquad
 \mathcal H_r(n)=
 r^2\Psi\!\left({2\over r}\log n\right)-\Psi(2\log n).
\]

By `T-20203`, this implies RH. The preferred first symbolic target is `r=15`,
for which every negative prime coefficient lies below `n^(1/8)` while the full
prime manifest still ends at `n^2`. Larger fixed values such as `r=31` and
`r=63` reduce the adverse prefix to `n^(1/16)` and `n^(1/32)` respectively.

## Common proof object

Every level must be represented in three exactly overlapping forms:

1. **two-scale scalar:** `r^2 Psi(t)-Psi(rt)`;
2. **finite Gram portfolio:** the aggregate of the four-tap vectors in
   `L-20204`;
3. **Chebyshev–Riesz form:** `A_r(n)+integral E K_(r,n)` from `L-20203`.

A proof-producing implementation must require agreement of all three before a
finite value is retained. This catches normalization, support, prime-power, and
large-cancellation errors.

## Arithmetic decomposition

Split

\[
 [1,n^2]
 = [1,e^2n^{2/(r+1)})
   \cup[e^2n^{2/(r+1)},n^2].
\]

The Riesz kernel is potentially negative only on the first interval and is
nonnegative on the second. The proof must not take an absolute value over the
long interval. Instead:

1. evaluate or bound the short old prefix directly;
2. center the long block against the exact continuous main measure;
3. use a correlation-sensitive identity for the centered block.

## Three serious closure mechanisms

### A. Prime-polygon transport

In PR #219's notation `Psi=F-G`, the target is the renormalized chord

\[
 r^2F(t)-F(rt)+G(rt)-r^2G(t).
\]

Use the exact mass-quantile recurrence for `G*` to group prime-power arrivals
into blocks whose integrated quantile surplus pays the archimedean chord. The
block statement may tolerate negative individual arrivals; only cumulative
transport matters.

### B. Selberg/prime-pair energy

Insert Selberg's convolution identity before estimating the positive-kernel
outer Riesz block. The target is a representation

\[
 \mathcal H_r(n)=\text{positive prime-pair square}+\mathcal R_r(n)
\]

with

\[
 (-\mathcal R_r(n))_+=n^{o(1)}.
\]

This should use the phase-robust finite prime-pair Gram of PR #216. Entrywise
absolute values are forbidden because they destroy the order-one cancellation.

### C. Real-axis Stieltjes production

At a fixed ordinary real point, generate the moments of the Laplace transform
of the same Gram portfolio. Search for an exact continued-fraction recurrence
whose coefficients are manifestly positive after the short-prefix correction.
The off-center GGC formulas may be used only through an independently proved
order-preserving comparison; `R-20201` blocks analytic-continuation shortcuts.

## Positive-mixture design

A finite positive mixture

\[
 \sum_{r\le R}c_r\mathcal D_r,
 \qquad c_r>0,
\]

retains both RH-side positivity and the pole-descent converse. Sample it at
`t=2log(n)/R`. Every negative prime coefficient still lies below
`n^(2/(R+1))`.

The coefficients may be selected by a finite rational linear program to:

- flatten the archimedean chord;
- match a Selberg or polygon transport kernel;
- reduce interval conditioning;
- preserve a simple exact Gram portfolio.

Any selected coefficients must be frozen before cofinal analysis; numerical
optimization is discovery only.

## Finite production ladder

A useful directed ladder is

```text
r = 2, 3, 5, 7, 15
n = exact powers chosen so n^(1/r) is rational
```

with one duplicate-free prime-power stream through `n^2`. The ladder is used to
validate identities and identify the sharp kernel, not to infer RH from finite
positivity.

## Success criterion

The route is complete only after an unbounded theorem proves, for one fixed
portfolio,

\[
 \mathcal H(n)\ge-n^{\varepsilon}
\]

for every `epsilon>0` and all sufficiently large `n`. A finite positive table,
a fitted decay exponent, or an assumed zero expansion is not a substitute.

## Failure modes to preserve

- phase-blind PNT bounds are too wide after the order-`n` cancellation;
- off-center probability measures do not remain positive by analytic
  continuation;
- separately widening the four-tap Gram terms loses their shared cancellation;
- allowing `r` to grow with `n` does not automatically give one fixed analytic
  pole-descent criterion;
- positivity of an averaged finite matrix does not imply positivity at one
  support.
