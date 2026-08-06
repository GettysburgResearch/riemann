# Global attack II — signed balanced-semiprime dispersion

Agent: `gpt56-pro-18`  
Date: 2026-08-07  
Issue: #221  
Stacked on: PR #216

## Objective

Complete the final arrow of the ordinary-prime Hardy-energy route:

\[
 [\mathcal O_H^{\mathbb P}(X)]_+=\exp(o(X)).
\]

A proof would imply RH through proposed `T-21502`. This pass deliberately did
not expand another finite ladder.

## What was proved

### 1. Exact prime-ramp wavelet identity

The ordinary-prime signal is exactly

\[
 Q_H^{\mathbb P}(x)
 =\Delta_1^3(I-2T_{\log4})F(x-1),
\]

where

\[
 F(x)=\sum_p\frac{\log p}{\sqrt p}(x-\log p)_+.
\]

The operator has three ordinary vanishing moments and annihilates the
`exp(x/2)` pole model exactly. The full problem is therefore one fixed wavelet
mean-square bound for a convex weighted prime ramp.

### 2. Finite signed Type-II cells

Every unit block is an exact finite sum of cubic factor-ratio cells. The kernel
has only finitely many affine breakpoints over `Q(log 4)`, and each cell is a
balanced Type-II moment with degree at most three.

This removes infinite or numerical kernel bookkeeping. The cell coefficient
vector must remain intact until the last bilinear contraction.

### 3. Absolute-value no-go

The absolute off-diagonal pair ledger satisfies

\[
 \mathcal A_H(X)\ge c e^X
\]

for all sufficiently large `X`. This follows already from the positive
neighborhood of the autocorrelation at zero and the PNT.

Thus entrywise absolute values lose a full exponential factor. The observed
`99.99%` cancellation is not optional conditioning; it is the theorem.

### 4. Resolution uncertainty barrier

For the integral-normalized compressed safe window `H_delta`, once its four
components are disjoint,

\[
 \|H_\delta\|_2^2=\frac{20}{3\delta}.
\]

The diagonal through log height `X` is

\[
 \left(\frac{10}{3}+o(1)\right)\frac{X^2}{\delta}.
\]

Resolution fine enough to separate every log-prime through height `X` needs
`delta<=exp(-X+o(X))`; its diagonal therefore has Hardy exponent `1/2` and masks
the whole possible zero strip. Keeping the diagonal subexponential forces
`log(1/delta)=o(X)` and leaves exponentially many interacting prime pairs.

The signed Type-II form cannot be eliminated by a narrower window.

### 5. Hardy-space connection

The prime energy is a critical local vertical embedding of the prime-supported
linear Dirichlet series. Its Bohr coefficient norm is only polynomial:

\[
 \sum_p\frac{(\log p)^2}{p^{1+2\sigma}}
 \sim\frac1{4\sigma^2}.
\]

The missing step is converting this global torus norm into the arithmetic local
vertical norm after the boundary-safe multiplier. General Dirichlet-Hardy
embedding theorems do not supply that critical shift.

## Attacks that did not close

I tested the following strategies against the exact exponent interface:

1. phase-blind PNT and Vinogradov--Korobov errors;
2. classical Selberg-integral mean squares;
3. unsigned semiprime sieve bounds;
4. ordinary Type-II bounds after independent cell absolute values;
5. shrinking or highly concentrated safe windows;
6. global Bohr-`H^2` coefficient orthogonality;
7. direct use of the centered Selberg Riccati equation.

Each fails at an explicit point:

- PNT and mean-square errors retain positive exponential growth;
- unsigned Type-II estimates destroy the cell cancellation;
- window diagonalization creates exponent `1/2`;
- Bohr orthogonality does not control a bounded vertical interval;
- the quadratic Selberg term has no established dissipative sign.

Primary literature comparisons:

- Brent--Platt--Trudgian, arXiv:2008.06140, obtain the `X^2` PNT mean-square
  upper scale under RH, not unconditionally;
- Goldston--Suriajaya, arXiv:2205.06503, obtain stronger PNT error from strong
  zero pair-correlation assumptions;
- Brevig, arXiv:1606.03101, treats the general Hardy-space-of-Dirichlet-series
  embedding and its critical shift.

These comparisons support the scope boundary: none supplies the signed
critical embedding needed here.

## Exact checker

`X-22101` verifies:

```text
eight formal ramp shifts
moments 0,1,2 vanish
third finite-difference normalization = 6
pole-model factor = 0
narrow L2 prefactor = 20/3
diagonal Hardy exponent at delta=e^-X = 1/2
```

Proof-object SHA-256:

```text
bc8da6a56ff84ed48d33706d2c4478837b6dc9169f784d7d93afec6ff4705a71
```

Eight central/mutation tests are committed. The checker is synthetic exact
algebra only.

## SERIOUS RESOLUTION PATH

A serious full-problem route remains:

```text
prime-only safe signal
-> exact prime ramp wavelet
-> finite signed cubic Type-II cells
-> common-cell Selberg/dispersion inequality
-> subexponential block energy
-> RH.
```

The exact missing theorem is a **signed common-cell contraction**, for example

\[
 \mathcal B_H(j)
 \le P(j)+\varepsilon_j\max_{k<j}\mathcal B_H(k),
 \qquad \varepsilon_j\to0,
\]

or a direct `exp(epsilon*j)` upper bound for every epsilon.

No such inequality was proved in this pass. It cannot be replaced by an
absolute sieve, a finite computation, or a window-resolution argument.

## Status

```text
prime-ramp identity                 PROPOSED / exact
finite cubic Type-II decomposition PROPOSED / exact
absolute-majorant no-go             PROPOSED / complete asymptotic
resolution uncertainty barrier      PROPOSED / complete scaling
critical local-Hardy connection      PROPOSED connection
signed Type-II subexponential bound OPEN
Riemann Hypothesis                   UNPROVED
```
