# Averaged carry commutator — full-problem attack

Date: 2026-08-08  
Agent: `gpt56-08`

## Executive result

The latest source/carry audit on PR #269 proved that every zeroth-order carry window contains a factor of `zeta` and cancels the RH pole. This pass differentiates that cancellation rather than adding another carry surrogate.

The new exact chain is

```text
all atomized carry positions
-> uniform average
-> canonical continuum carry kernel
-> complete omega_2 source
-> compact two-band pole-blind wavelet
-> first logarithmic commutator
-> pole-preserving ordinary-prime top-quarter contrast
-> exact discrete factor-five carry scalar + explicit 3/8 boundary
-> positive local normal energy
-> RH criterion.
```

The first logarithmic commutator is the minimal pole-preserving correction: at every zeta zero it has a nonzero simple-pole residue, including for multiple zeros.

## Main finite statistic

For

\[
 W_X(q)=
 \begin{cases}
 2q/X-1,&X/2<q\le X,\\
 1/2-4q/X,&X/4<q\le X/2,\\
 0,&q\le X/4,
 \end{cases}
\]

define

\[
 \mathfrak P(X)=X^{-1/2}\sum_{q\le X}\Lambda(q)W_X(q).
\]

Its transform is

\[
 -\frac{(1-2^{-s})(1-2^{-s-1})(s-1)}{s(s+1)}
 \frac{\zeta'(s)}{\zeta(s)},
 \qquad s=z+1/2.
\]

Every nontrivial zero survives.

The complete positive energy is

\[
 \mathfrak E(J)=\int_J^{J+1}|\mathfrak P(e^t)|^2dt.
\]

RH is equivalent to `mathfrak E(J)=e^{o(J)}`.

## Exact source-image map

The continuum commutator is not merely analogous to the carry package. For integer endpoints it satisfies

\[
 \mathcal R_X^{cont}
 =\mathcal R_X^{disc}
 +\frac{2}{X(X+1)}
 [B(X)-3B(X/2)+2B(X/4)-\log2],
\]

where `B(Y)=sum_(n<=Y)n Lambda(n)`. The bracket tends to `3X^2/16`, so the boundary tends to `3/8`.

The discrete scalar is

\[
 \mathcal R_X^{disc}
 =\frac1{X+1}\sum_j\sum_m\Lambda_\omega(m)Z_{X,m}(j),
\]

using exactly the factor-five source wavelets and generalized-prime weights of PR #269.

Thus the former abstract boundary/transverse decomposition has been replaced at scalar level by an exact formula with no unidentified remainder.

## Second commutator

The next logarithmic commutator is

\[
 \beta_\omega*(U^2k)
 =U^2z_\omega
  +2\lambda_\omega*(Uz_\omega)
  +C_\omega*z_\omega,
\]

where

\[
 C_\omega
 =\Lambda_\omega\log
  +\Lambda_\omega*\Lambda_\omega\ge0.
\]

This is the proposed mechanism for controlling the local normal energy. It keeps the complete Selberg convolution, both annulus bands, and the explicit continuum/discrete boundary in one ledger.

## Exact replay

`X-27601` uses only the Python standard library and exact `Fraction` arithmetic. It checks:

```text
carry-position average rows          2,079
omega inverse rows                     160
first commutator rows                  156
second commutator rows                 156
Selberg rows                            160
continuum/discrete boundary rows       156
transform rows                          17
source mutations                       3/3 rejected
```

Verdict:

```text
PASS_EXACT_AVERAGED_CARRY_COMMUTATOR_ALGEBRA
```

Proof-object SHA-256:

```text
4b82004193838f2ca5ba5295bf9d55199bf36d3c7e5f643304a9ffce71fbd82b
```

## Exact frontier

The result is not an unconditional proof of RH. The open theorem is:

```text
PAE:
int_J^(J+1) |mathfrak P(exp t)|^2 dt = exp(o(J)).
```

Unlike DCRS, PTQ, generic SIFD, or an unspecified boundary Schur complement, `PAE` is one explicit positive finite prime-annulus energy. Its complete source, physical window, carry image, boundary correction, and zero residues are all written down.

A future proof must use the second commutator or another genuine arithmetic cancellation theorem; restating `PAE` as a prime error estimate does not close it.
