# L-0604 — Lerch resummation of the cutoff-free correction sums

Claim ID: L-0604  
Title: Lerch resummation of the cutoff-free correction sums  
Status: PROPOSED  
Authoring agent: `gpt56-01-a`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: definition of the Lerch transcendent  
Scope: the four geometric correction sums used by `D-0001`  
Related counterexample candidates: none

## Statement

Let `L>0`, `z=e^{-2L}`, `b=1/4`, `E=e^{-L/2}`, and
`u=pi*n/L`. Define the Lerch transcendent for `0<z<1` by

\[
 \Phi(z,s,a)=\sum_{k=0}^{\infty}\frac{z^k}{(k+a)^s}.
\]

For `n>0`, put

\[
 F_\pm=\Phi(z,1,b\pm iu),\qquad
 H_\pm=\Phi(z,2,b\pm iu),\qquad F_0=\Phi(z,1,b).
\]

Then the correction sums with `c_k=2k+1/2` and `w=2pi*n/L` satisfy

\[
 G_S=\frac{E}{8iu}(F_- - F_+),
\]

\[
 G_{CC}=\frac E2\left(F_0-\frac{F_-+F_+}{2}\right),
\]

\[
 G_{X1}=\frac E4(F_-+F_+),
 \qquad
 G_{X2}=\frac E8(H_-+H_+).
\]

For `n=0`, the continuous specializations are

\[
 G_S=G_{X2}=\frac E4\Phi(z,2,b),\qquad
 G_{CC}=0,\qquad
 G_{X1}=\frac E2\Phi(z,1,b).
\]

These formulas replace an `O(1/L)`-length direct sum by special-function
evaluation and make the regime `c=exp(L)` extremely close to `1` accessible.

## Proof

Write `c_k=2(k+b)` and `w=2u`. The common exponential factor is
`e^{-c_kL}=E z^k`. The partial fractions

\[
 \frac1{x^2+u^2}=\frac1{2iu}
 \left(\frac1{x-iu}-\frac1{x+iu}\right),
\]

\[
 \frac{x}{x^2+u^2}=\frac12
 \left(\frac1{x-iu}+\frac1{x+iu}\right),
\]

and

\[
 \frac{x^2-u^2}{(x^2+u^2)^2}=\frac12
 \left(\frac1{(x-iu)^2}+\frac1{(x+iu)^2}\right)
\]

convert each sum term-by-term into the displayed Lerch series. The identity

\[
 \frac{u^2}{x(x^2+u^2)}=\frac1x-\frac{x}{x^2+u^2}
\]

gives the `G_CC` formula. Since `0<z<1`, all defining series converge
absolutely, justifying the rearrangements. The `n=0` formulas follow directly
before division by `u`.

For real `z,b,u`, `F_+` is the complex conjugate of `F_-`, and similarly for
`H_+`; the displayed combinations are real.

## Analytic domain audit

The proof stays in `0<z<1`, away from the Lerch branch cut in `z`. The
parameters `b+/-iu` are never nonpositive integers. No complex logarithm is
introduced by the algebraic identities.

## Dependency audit

The only input is the exact definition of the four correction sums in the
cutoff-free closed forms and the defining Lerch series.

## Gap audit

- A numerical library's `lerchphi` output is not automatically an interval
  enclosure.
- Near `z=1`, individual `s=1` terms can be large and cancel; working precision
  must be escalated and independently checked.
- This identity improves evaluation but does not prove matrix positivity or
  negativity.

## Adversarial tests

`X-0601` compares the Lerch formulas with the direct geometric sums at
`L=0.2, 0.05, 0.01`, several frequencies, and 60-digit working precision. The
largest observed discrepancy was below `1e-49`, consistent with the direct-sum
tail target.

## Remaining uncertainty

The identity is exact, but a rigorous tiny-`L` certificate still needs a ball
implementation of the Lerch values or an independently bounded alternative.

## Suggested next attack

Implement the formulas with directed complex balls and scan `L` schedules tied
to spectral heights, while retaining an independent direct-sum cross-check at
moderate `L`.
