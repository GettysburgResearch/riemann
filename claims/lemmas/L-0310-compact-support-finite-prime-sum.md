# L-0310 — Compact support makes the prime-power sum finite

Claim ID: L-0310  
Title: Compact logarithmic support makes explicit-formula prime sums finite  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: none beyond the definition of support  
Scope: elementary support reduction for Weil/explicit-formula searches  
Related counterexample candidates: finite Weil witnesses

## Statement

Let `h:R->C` satisfy `h(x)=0` whenever `|x|>A`, where `A>=0`.  Then
\[
 \sum_{n=2}^{\infty}\frac{\Lambda(n)}{\sqrt n}\,h(\log n)
\]
has only finitely many nonzero terms, namely those with
\[
 n\le e^A.
\]
Equivalently, writing `n=p^m`, only prime powers satisfying
\[
 m\log p\le A
\]
can contribute.

The same conclusion holds for any sum whose `n`-th term contains the factor
`h(log n)`.

## Proof

If the `n`-th term is nonzero, then `h(log n)!=0`.  Since `n>=2`,
`\log n>0`, and the support condition gives
\[
 \log n\le A.
\]
Exponentiation, which is increasing on the real line, yields `n<=e^A`.
There are only finitely many integers in `[2,e^A]`, proving finiteness.

The von Mangoldt function `Lambda(n)` is nonzero only when `n=p^m` is a prime
power.  For such an `n`,
\[
 \log n=m\log p,
\]
so the contribution condition is exactly `m log p<=A`.  ∎

## Motivation

A compact-support test family can turn the prime side of a Weil explicit
formula into an exactly finite arithmetic object.  This is one reason the
finite-matrix route in Issue #1 can aim for compact certificates.

## Analytic domain audit

No analytic continuation, contour, or branch is used.  The logarithm is the
ordinary real logarithm of a positive integer.

## Dependency audit

The lemma is purely elementary.  It does **not** establish that a proposed
test function is admissible for any explicit formula, nor that its transform
normalization is correct.

## Gap audit

- Compact support on the wrong side of a Fourier/Mellin transform may not
  truncate the prime sum.
- Support at the endpoint `A` permits `n=e^A` if that is an integer.
- A numerical function merely small outside `[-A,A]` is not compactly
  supported.
- Archimedean, pole, and zero terms may remain infinite even when the prime sum
  is finite.

## Adversarial tests

- `A<log 2`: the prime sum is empty.
- `A=log 4`: contributions can include `2`, `3`, and `4`.
- Replace exact support by exponential decay and verify that the conclusion
  fails.

## Remaining uncertainty

Application to `D-0001` requires an independent audit of which function has
compact support and the exact scaling of `A=log c`.

## Suggested next attack

Use this lemma in the `Q-0004` reconstruction to enumerate every prime-power
threshold and verify endpoint conventions exactly.
