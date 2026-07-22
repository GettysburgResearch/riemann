# L-2002 — Elementary two-sided enclosure for Euler's constant

Claim ID: L-2002  
Title: Harmonic numbers give a self-contained two-sided enclosure for Euler's constant  
Status: PROPOSED  
Authoring agent: `gpt56-03-b`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: L-2001 for certified evaluation of `log n`  
Scope: real Euler--Mascheroni constant  
Related counterexample candidates: Robin and Nicolas arithmetic witnesses

## Statement

For every integer `n>=1`, with

\[
 H_n=\sum_{k=1}^{n}\frac1k,
 \qquad
 \gamma=\lim_{N\to\infty}(H_N-\log N),
\]

one has

\[
 \frac{1}{2(n+1)}
 < H_n-\log n-\gamma
 < \frac{1}{2n}.
\]

Equivalently,

\[
 H_n-\log n-\frac1{2n}
 <\gamma<
 H_n-\log n-\frac1{2(n+1)}.
\]

Thus a rational or dyadic enclosure of `H_n` and `log n` gives a self-contained enclosure of `gamma` without importing stored digits of the constant.

## Motivation

X-0202 obtained `gamma` through a directed Decimal engine. X-2001 needs a genuinely separate route whose only inputs are exact integers. The bound here is strong enough that `n=10^6` leaves an analytic uncertainty below `5*10^-13`, while directed arithmetic controls all rounding.

## Proof

Set

\[
 \phi(x)=\log(1+x)-\frac{x}{1+x}
 \qquad (x>0).
\]

We first prove

\[
 \frac{x^2}{2(1+x)(1+2x)}
 <\phi(x)<
 \frac{x^2}{2(1+x)}.
\]

For the upper bound, define

\[
 U(x)=\frac{x^2}{2(1+x)}-\phi(x).
\]

Then `U(0)=0` by continuous extension and

\[
 U'(x)=\frac{x^2}{2(1+x)^2}>0
 \qquad(x>0).
\]

For the lower bound, define

\[
 L(x)=\phi(x)-\frac{x^2}{2(1+x)(1+2x)}.
\]

Again `L(0)=0`, and direct differentiation gives

\[
 L'(x)=
 \frac{x^2(8x+5)}{2(1+x)^2(1+2x)^2}>0.
\]

This proves the two strict inequalities.

Now

\[
\begin{aligned}
 H_n-\log n-\gamma
 &=\lim_{N\to\infty}
   \left(\log\frac{N}{n}-\sum_{k=n+1}^{N}\frac1k\right)\\
 &=\sum_{k=n}^{\infty}
   \left(\log\left(1+\frac1k\right)-\frac1{k+1}\right)\\
 &=\sum_{k=n}^{\infty}\phi(1/k).
\end{aligned}
\]

Substituting `x=1/k` into the pointwise bounds yields

\[
 \frac{1}{2(k+1)(k+2)}
 <\phi(1/k)<
 \frac{1}{2k(k+1)}.
\]

Both comparison series telescope:

\[
 \sum_{k=n}^{\infty}\frac{1}{2(k+1)(k+2)}
 =\frac1{2(n+1)},
\]

and

\[
 \sum_{k=n}^{\infty}\frac{1}{2k(k+1)}
 =\frac1{2n}.
\]

The desired enclosure follows. ∎

## Analytic domain audit

All logarithms are real and evaluated at positive arguments. The limiting definition of `gamma` is used only through a convergent positive series. No complex branch or continuation occurs.

## Dependency audit

L-2001 is needed only for the machine enclosure of `log n`; the displayed two-sided inequality is proved independently in this file.

## Gap audit

- The harmonic sum must itself be outward rounded or accumulated exactly.
- Subtracting an interval reverses its endpoints; using the same correction endpoint twice is unsound.
- The looser bound `0<H_n-log n-gamma<1/n` would certify the large 5041 margin but is needlessly weak near the 5583 threshold.

## Adversarial tests

- Compare the enclosures at several increasing cutoffs; they must be nested after allowing for directed-rounding noise.
- Verify coarse containment `0.57721<gamma<0.57722` without using stored high-precision digits.
- Deliberately swap the two correction endpoints and confirm a regression test detects the invalid interval.

## Remaining uncertainty

No mathematical gap is known. The finite harmonic accumulation and subtraction code require ordinary independent review.

## Suggested next attack

Replace the termwise harmonic accumulation by a binary-splitting exact rational or Euler--Maclaurin implementation when much narrower intervals are needed at very high scale.
