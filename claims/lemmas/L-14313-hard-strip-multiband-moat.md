# L-14313 — A finite multiband packet leaves only a polynomial Hardy-strip loss

Claim ID: `L-14313`  
Title: The cancellation-aware symbol floor converts to an explicit Hardy complement moat  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: `L-14311`; elementary comparison of weighted and ordinary `L2` norms  
Scope: complement coercivity for the block Temple--Schur route  
Related counterexample candidates: none

## Statement

Let `a=log lambda`, and use the scaled Suzuki form `q_a` on `(-1,1)` with the
modified exact symbol `s_a^+` of `L-14311`. Assume the normalization and symbol
gates in that lemma have been audited, so that

\[
 q_a(w)\ge-\frac2\pi\|w\|_2^2
 +\frac1{2\pi}\int_{\mathbb R}s_a^+(\xi)|\widehat w(\xi)|^2d\xi.
 \tag{L-14313.1}
\]

For every fixed support `a`, the function `s_a^+` is bounded below and tends to
`+infinity` as `|xi|->infinity`. Put

\[
 G=2+\frac2\pi,
 \qquad
 m_a=\inf_{\xi\in\mathbb R}s_a^+(\xi),
 \tag{L-14313.2}
\]

and let

\[
 B_a=\{\xi:s_a^+(\xi)<G\}.
 \tag{L-14313.3}
\]

Then `B_a` has finite measure. Choose

\[
 \eta_a
 =\min\left\{\frac12,
 \frac1{2(1+G-m_a)}\right\}.
 \tag{L-14313.4}
\]

Let `S_a` be the generalized-prolate packet consisting of every eigenspace of
the multiband concentration operator `K_(B_a)` with eigenvalue above `eta_a`.
Then `S_a` is finite dimensional and

\[
 \boxed{
 q_a(w)\ge\frac32\|w\|_2^2
 \qquad(w\perp S_a).}
 \tag{L-14313.5}
\]

The packet obeys the exact rank bound

\[
 \boxed{
 \dim S_a\le
 \left\lceil\frac{|B_a|}{\pi\eta_a}\right\rceil.}
 \tag{L-14313.6}
\]

## Proof

Because `s_a^+(xi)->infinity`, its strict sublevel set at the finite height `G`
has finite measure. Apply `L-14311` with the global lower bound `m_a`, good
floor `G`, and concentration threshold `eta_a`. The resulting ordinary `L2`
floor is

\[
 -\frac2\pi+(1-\eta_a)G+\eta_am_a
 =2-\eta_a(G-m_a).
 \tag{L-14313.7}
\]

The definition (L-14313.4) gives

\[
 \eta_a(G-m_a)\le\frac12,
\]

so (L-14313.5) follows. The trace estimate in `L-14311` proves
(L-14313.6). QED.

## Hardy-strip conversion

Undo the unitary scaling to the logarithmic interval `[-a,a]`. For
`0<tau<1/2`, define

\[
 \|w\|_{a,\tau}^2
 =\int_{-a}^{a}|w(x)|^2\,2\cosh(2\tau x)\,dx.
 \tag{L-14313.8}
\]

On this interval,

\[
 \|w\|_{a,\tau}^2
 \le2\cosh(2\tau a)\|w\|_2^2.
 \tag{L-14313.9}
\]

Consequently the same complement satisfies

\[
 \boxed{
 q_a(w)\ge h_{a,\tau}\|w\|_{a,\tau}^2,
 \qquad
 h_{a,\tau}=\frac{3}{4\cosh(2\tau a)}.}
 \tag{L-14313.10}
\]

For

\[
 \tau_a=\frac12-\frac1a,
 \qquad a\ge4,
 \tag{L-14313.11}
\]

one has `2 tau_a a=a-2` and

\[
 \boxed{
 h_{a,\tau_a}\ge\frac{3e^2}{4e^a}
 =\frac{3e^2}{4\lambda}
 >\frac1\lambda.}
 \tag{L-14313.12}
\]

Thus approaching the full critical strip costs only one power of the support
parameter.

## Enlarging the low packet

If a finite-dimensional space `F_a` is added to `S_a`, the complement shrinks,
so (L-14313.5)--(L-14313.12) remain valid on

\[
 (S_a+F_a)^\perp.
\]

In particular one may add the exact radical truncation `k_lambda` of
`L-14312`, parity partners, or any finite collection of numerical low modes.

## Gap audit

- The abstract multiband concentration argument is exact.
- A production proof still needs a directed global lower bound for `s_a^+` and
  a proof-grade finite cover of its sublevel set.
- The packet can be very large; this theorem proves finiteness and the moat, not
  positivity of the finite low block.
- The Hardy moat is attached to the complement of the enlarged packet, not to
  the complement of one trial vector alone.
