# L-20210 — Stable infinite filters cannot remove the half-knot prime debt

Claim ID: `L-20210`  
Title: The half-knot ramp remains strictly positive for every nonzero `H^2` screw filter, including infinite summable mixtures  
Status: **PROPOSED — COMPLETE HILBERT-SPACE PROOF**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: the Hardy-space Fejer factorization and `L-20209`  
Scope: stable finite or infinite RH-positive translation/FIR filters

## 1. Stable positive filter

Let

\[
 Q(z)=\sum_{j\ge0}q_jz^j\in H^2,
 \qquad q\ne0,
\]

and put

\[
 A(z)=(1-z)Q(z),
 \qquad
 P(x)=|A(e^{ix})|^2.
\]

Then `P>=0`, `P(0)=0`, and `P` is the boundary spectral density of a stable
RH-positive screw filter. Assume its Fourier coefficients have the mild first
moment required to define the prime ramp `L_P`; equivalently, the identities
below may be taken as the closed quadratic-form definition on the first cell.

Let `S` be the unilateral shift on `ell^2(N_0)` and define the discrete boundary
difference

\[
 D=I-S,
\]

with the usual zero extension at the left endpoint.

## 2. Exact first-cell form

The finite identity of `L-20209` extends by `H^2` approximation:

\[
\boxed{
 L_P(s)=2\|q\|_2^2-s\|Dq\|_2^2
 \qquad(0\le s\le1).}
\]

Since `||D||<=2`,

\[
\boxed{
 L_P(s)\ge(1-2s)L_P(0)
 \qquad(0\le s\le1/2).}
\]

Thus every stable positive filter has strictly adverse prime-ramp sign on the
entire open interval `0<=s<1/2`.

At the boundary,

\[
\begin{aligned}
 L_P(1/2)
 &=2\|q\|_2^2-\frac12\|(I-S)q\|_2^2\\
 &=\frac12\|(I+S)q\|_2^2.
\end{aligned}
\]

Therefore

\[
\boxed{
 L_P(1/2)>0.}
\]

Indeed, `(I+S)q=0` forces `q_0=0` and then recursively every `q_j=0`.

## 3. No fixed infinite-mixture escape

The finite sharp constants of `L-20208` tend to zero as the degree grows, so a
sequence of endpoint-concentrated filters can make the half-knot debt arbitrarily
small. The present theorem shows that the limiting debt cannot vanish inside
any fixed stable `H^2` filter.

Consequently, none of the following can remove the first-prime obstruction:

1. a fixed absolutely/square-summable positive mixture of `r`-adic defects;
2. a fixed stable infinite FIR filter;
3. a fixed positive spectral density obtained as an `H^2` Fejer limit.

A zero half-knot debt requires a singular, non-`H^2` endpoint concentration or a
genuinely growing filter family whose degree is part of the cofinal proof.

## 4. Arithmetic interpretation

At base support `t=log 4`, the prime `q=2` has normalized position `s=1/2`.
Hence every nonzero stable RH-positive filter contributes the strictly negative
prime coefficient

\[
 -\log4\,{\log2\over\sqrt2}\,L_P(1/2)<0.
\]

This remains true even for an infinite stable filter. The full proof must pay
this debt through positive prime bulk, pole/archimedean cancellation, or a
cofinal singular limit; it cannot delete the debt by a fixed positive filter.

## 5. Status boundary

The theorem is a no-go and compactness statement. It does not show that the
required growing endpoint-concentrated family exists with a controlled
arithmetic remainder. The exact remaining task is a quantitative cofinal limit
that preserves pole descent while the half-knot debt tends to zero and every
other autocorrelation channel remains controlled.
