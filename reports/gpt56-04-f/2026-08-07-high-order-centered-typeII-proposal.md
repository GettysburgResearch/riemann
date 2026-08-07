# High-order centered Type-II proposal after the positive review

Agent: `gpt56-04-f`  
Date: 2026-08-07  
Branch: `agent/gpt56-04-f/151-finsler-target-completion`  
Frozen review input: PR #158 at `7902480c92a34e8ca5788e8e1e844ac3727e3a4e`  
Imported arithmetic source: PR #216 at `b76eef1b769584aa9d66d082bfc6634126f986a2`  
Status: **PROPOSED PENDING INDEPENDENT REVIEW; RH NOT CLAIMED PROVED**

## Executive result

The latest review verified the repaired analytic and finite-Gram front half but
correctly rejected the claim that an undeclared Vaughan/Heath--Brown
“Type-II estimate” had been completed.

This pass closes the missing architecture at the exact level:

1. ordinary-prime and full-von-Mangoldt safe blocks are polynomially equivalent;
2. both are the same adjoint/normal geometry, not the rejected product geometry;
3. high-order compact safe windows annihilate every finite polynomial pole
   model required by a fixed Heath--Brown order;
4. every decomposition row can be centered independently in the Gram quotient;
5. the truncated Heath--Brown identity, tuple coefficients, and Type-I/II
   partition are finite and exact;
6. all cross rows reduce to a finite vector of positive self-energies;
7. strict scale-contraction composition is proved for scalar, finite-vector,
   and tensor systems;
8. a quantitative increasing-order theorem shows exactly what coefficient rate
   suffices to force RH.

The only remaining proposed arithmetic theorem is the centered packet estimate
`CP(K)` in `M-15112`.

## 1. Prime/full-`Lambda` bridge

For the fixed compact safe window `H`,

\[
 Q_H^\Lambda-Q_H^{\mathbb P}
 =\sum_{k\ge2}\sum_p{\log p\over p^{k/2}}
 H(x-k\log p).
\]

On a block `[J,J+1]`, the prime-square layer is `O_H(J)` by elementary integral
comparison, and every layer `k>=3` is absolutely summable. Therefore

\[
 \sup_{J\le x\le J+1}
 |Q_H^\Lambda(x)-Q_H^{\mathbb P}(x)|
 \ll_H1+J.
\]

It follows that

\[
 \mathcal B_J^\Lambda
 \le2\mathcal B_J^{\mathbb P}+O_H(J^2)
\]

and conversely. Polynomial and `exp(o(J))` growth are equivalent for the two
sources.

Both blocks are exactly

\[
 \langle H,\mathcal P^*\chi_J\mathcal P H\rangle.
\]

This is the adjoint/factor-ratio orientation verified in PR #216.

## 2. High-order null quotient

For `m>=1`, define

\[
 H^{[m]}
 =\Delta_0^{m-1}\Delta_{1/2}^{m-1}H,
\]

with multipliers `1-e^(-z)` and `1-2*4^(-z)`. Its transform has order-`m`
zeros at both boundary points and remains zero-free in the open counterexample
strip.

The block kernel annihilates

\[
 u^rdu,
 \qquad
 u^re^{u/2}du,
 \qquad0\le r<m,
\]

in each leg. Therefore an exact decomposition

\[
 \nu=\sum_a\nu_a
\]

may be centered row by row using arbitrary companions in that finite null
space. The companions do not have to recombine.

For row energies `E_a`, Gram Cauchy--Schwarz gives

\[
 B(\nu,\nu)
 \le R\sum_aE_a.
\]

This closes the rowwise-centering and cross-row closure objections from the
review.

## 3. Exact finite Heath--Brown packet

For order `K`, endpoint `X`, and `V=X^(1/K)`, put

\[
 \mu_V(n)=\mu(n)1_{n\le V}.
\]

For every `n<=X`,

\[
 \Lambda(n)
 =\sum_{j=1}^K(-1)^{j-1}{K\choose j}
  (\mu_V^{*j}*\log*1^{*(j-1)})(n).
\]

The proof uses

\[
 R_V=1-\zeta M_V:
\]

all nonzero coefficients of `R_V` lie above `V`, so `R_V^K` has no coefficient
through `V^K=X`.

Every row is expanded into a finite ordered tuple with exact coefficient

\[
 (-1)^{j-1}{K\choose j}
 \mu(d_1)\cdots\mu(d_j)\log q.
\]

A deterministic first-crossing rule assigns the tuple to Type I or Type II and
records its exact destination. No term is hidden under a conventional label.

The `j`-th row has pole order at most `j+1`. Choosing `H^[K+1]` annihilates its
complete inverse Laurent polynomial, so every exact row is independently
centered.

## 4. The correct closure theorem

Let `E_(K,tau)(J)` be the finite vector of centered row self-energies. If

\[
 E_{K,\tau}(J)
 \le a_{K,\tau}(J)
 +\sum_\upsilon b_{K,\tau\upsilon}(J)
  \max_{k\le(1-\delta_K)J+O_K(1)}E_{K,\upsilon}(k)
\]

with subexponential coefficients, then every row energy is `exp(o(J))`.

A tensor version is also proved. If the logarithmic scale weights satisfy

\[
 \sum_s\theta_s\alpha_s<1,
\]

then products of lower-scale auxiliary energies remain subexponential.

No coefficient smaller than one at the adjacent block is required.

## 5. Increasing-order quantitative route

At fixed order, allow the packet estimate to lose

\[
 e^{\epsilon_KJ}.
\]

If the strict scale reserve is `delta_K`, then the row exponent is at most

\[
 {\epsilon_K\over\delta_K}.
\]

Every high-order safe window detects the same rightmost-zero exponent. Hence

\[
 2\Theta_\zeta
 \le{\epsilon_K\over\delta_K}.
\]

A family satisfying

\[
 {\epsilon_K\over\delta_K}\to0
\]

proves RH. The tensor version replaces `delta_K` by `1-kappa_K`.

This is a genuine quantitative review target. It is not enough to say that a
fixed-order packet has “small losses.”

## 6. Exact regression

`X-15125` checks:

- the truncated Heath--Brown identity for `K=3,V=4,X=64` on a symbolic
  completely-additive prime-log basis;
- independent subtraction of two null modes from three Gram rows;
- equality of direct and recombined energies;
- the finite-vector Cauchy bound;
- a three-component strict-scale-contraction recurrence.

Retained values:

```text
Heath-Brown mismatches      none
null-mode energies          0, 0
direct Gram energy          202
recombined centered energy  202
finite-vector upper bound   570
proof SHA-256
3dc50743f1b3b435e2d9b969c5a1191ef0a94e89a4f4ccd17a2b211e6d91dea0
mutation tests              8/8 PASS
```

This is exact algebraic regression only. It does not test `CP(K)` on Riemann
data.

## 7. Exact remaining theorem

The sole proposed arithmetic theorem is:

> For an unbounded sequence of orders `K`, the finite centered Heath--Brown row
> vector satisfies a linear or tensor strict-scale-contraction estimate whose
> coefficient rate tends to zero relative to the contraction reserve.

The estimate must preserve:

1. signed binomial packets before absolute values;
2. independent Laurent-polynomial row centering;
3. adjoint/factor-ratio normal geometry;
4. every Type-I, Type-II, divisor, Möbius, log, and prime-power row;
5. exact support destinations and coefficient rates.

A standard large-sieve citation without this ledger does not prove the theorem.

## SERIOUS RESOLUTION PATH

```text
high-order compact safe window
-> exact full-Lambda / ordinary-prime normal energy
-> exact finite Heath-Brown packet
-> independent rowwise pole centering
-> finite auxiliary Type-I/II energy vector
-> vanishing-rate strict scale contraction
-> rightmost-zero exponent zero
-> RH.
```

All arrows except the centered packet estimate are now explicit.

## Status boundary

```text
Type-II coefficient bookkeeping:       COMPLETE, proposed pending review
Rowwise centering:                      COMPLETE, proposed pending review
Finite auxiliary closure language:     COMPLETE, proposed pending review
Scale-contraction composition:          COMPLETE, proposed pending review
Centered packet analytic estimate:     OPEN / RH-BEARING
Riemann Hypothesis:                     NOT CLAIMED PROVED
```
