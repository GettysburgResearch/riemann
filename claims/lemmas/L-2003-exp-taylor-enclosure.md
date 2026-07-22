# L-2003 — Positive Taylor enclosure for the exponential

Claim ID: L-2003  
Title: A positive Taylor polynomial with a geometric majorant encloses the real exponential  
Status: PROPOSED  
Authoring agent: `gpt56-03-b`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: none  
Scope: real exponential on a nonnegative bounded interval  
Related counterexample candidates: arithmetic finite witnesses involving `e^gamma`

## Statement

Let `x>=0`, let `M>=0`, and assume `x<M+2`. Put

\[
 S_M(x)=\sum_{j=0}^{M}\frac{x^j}{j!},
 \qquad
 a_{M+1}(x)=\frac{x^{M+1}}{(M+1)!}.
\]

Then

\[
 S_M(x)\le e^x\le
 S_M(x)+\frac{a_{M+1}(x)}{1-x/(M+2)}.
\]

If `0<=a<=b`, monotonicity therefore gives an enclosure of `e^[a,b]` by evaluating the lower formula at `a` and the upper formula at `b`, with outward rounding.

## Motivation

This supplies the last transcendental component of the independent Robin verifier. The relevant input is an interval around `gamma`, which lies in `(0,1)`, so the condition is extremely mild even for a modest Taylor order.

## Proof

The exponential series has nonnegative terms for `x>=0`, hence

\[
 S_M(x)\le e^x.
\]

For every `r>=0`, the ratio of successive omitted terms satisfies

\[
 \frac{x^{M+2+r}/(M+2+r)!}
      {x^{M+1+r}/(M+1+r)!}
 =\frac{x}{M+2+r}
 \le\frac{x}{M+2}<1.
\]

Therefore the entire tail is bounded by a geometric series beginning with `a_{M+1}(x)`:

\[
 e^x-S_M(x)
 \le a_{M+1}(x)
      \sum_{r=0}^{\infty}\left(\frac{x}{M+2}\right)^r
 =\frac{a_{M+1}(x)}{1-x/(M+2)}.
\]

The interval statement follows because the real exponential is strictly increasing. ∎

## Analytic domain audit

Only the real exponential for nonnegative arguments is used. No complex exponential, branch choice, or analytic continuation occurs.

## Dependency audit

The proof uses the ordinary power series for `e^x`, positivity of its terms, and a geometric-series comparison.

## Gap audit

- The denominator must be proved positive; the implementation rejects parameter choices with `x>=M+2`.
- The first omitted term is indexed `M+1`; an off-by-one error invalidates the majorant.
- The lower endpoint must be evaluated at the lower input and the upper endpoint at the upper input.

## Adversarial tests

- Enclose `exp(log 2)` using L-2001 and confirm the interval contains `2`.
- Use deliberately too few terms and confirm the code rejects a nonpositive tail denominator.
- Increase `M` and verify that the upper endpoint contracts.

## Remaining uncertainty

No mathematical gap is known. Implementation indexing and directed multiplication remain review targets.

## Suggested next attack

Add an optional range reduction `e^x=2^k e^r` for future criteria requiring much larger positive arguments.
