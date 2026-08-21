# L-23805 — Gamma–carry convolution factorization

Claim ID: `L-23805`  
Title: One explicit Möbius–Riesz density would make the carry law a convolution factor of `Gamma(2,1/2)`  
Status: **PROPOSED LOAD-BEARING POSITIVITY THEOREM — SINGLE REVIEW HINGE**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `L-23804`; elementary Laplace inversion  
Scope: the exact strip-sensitive theorem in the carry proposal

## 1. The factor quotient

Let `P(s)` be the carry-law transform from `L-23804`:

\[
 P(s)={2s\zeta(s+1)\over(s+1)(s+2)}.
 \tag{L-23805.1}
\]

Let

\[
 g(t)={t\over4}e^{-t/2},
 \qquad t\ge0,
 \tag{L-23805.2}
\]

be the density of a gamma variable of shape `2` and rate `1/2`. Its Laplace
transform is

\[
 G(s)={1\over(1+2s)^2}.
 \tag{L-23805.3}
\]

Define the quotient

\[
 \boxed{
 A(s)={G(s)\over P(s)}
 ={(s+1)(s+2)
  \over8s(s+\tfrac12)^2\zeta(s+1)}.}
 \tag{L-23805.4}
\]

The pole of `zeta(s+1)` at `s=0` cancels the displayed factor `1/s`, and

\[
 A(0)=1.
 \tag{L-23805.5}
\]

## 2. Exact inverse density

The rational part has the partial-fraction decomposition

\[
 { (s+1)(s+2)\over8s(s+\tfrac12)^2}
 ={1\over s}-{7\over8(s+\tfrac12)}
  -{3\over16(s+\tfrac12)^2}.
 \tag{L-23805.6}
\]

Using

\[
 {1\over\zeta(s+1)}
 =\sum_{n\ge1}{\mu(n)\over n^{s+1}}
 \qquad(\Re s>0),
\]

the unique inverse Laplace distribution on the open half-line is the locally
integrable, piecewise smooth function

\[
 \boxed{
 \begin{aligned}
 a(t)=\sum_{n\le e^t}{\mu(n)\over n}
 \bigg[&1-{7\over8}e^{-(t-\log n)/2}\\
       &-{3\over16}(t-\log n)e^{-(t-\log n)/2}
 \bigg].
 \end{aligned}}
 \tag{L-23805.7}
\]

At a knot `t=log n`, the new term enters with value `mu(n)/(8n)`. No term is
omitted or smoothed.

The exact load-bearing theorem is

\[
 \boxed{
 \textbf{GCF:}\qquad a(t)\ge0\quad(t\ge0).}
 \tag{L-23805.8}
\]

## 3. Probability/convolution consequence

If GCF holds, then `a(t)dt` is a probability measure because its Laplace
transform has value one at the origin. Let `S` have density `a`, independently
of the carry variable `T` in `L-23804`. Equations (L-23805.1)--(L-23805.4)
give

\[
 \boxed{
 S+T\overset d=\operatorname{Gamma}(2,1/2).}
 \tag{L-23805.9}
\]

Thus GCF says that the elementary harmonic-interval carry law is an additive
convolution factor of one explicit gamma law.

This is stronger and more structured than pointwise positivity of an arbitrary
Möbius sum: the target gamma distribution, the carry factor, and the residual
factor are all normalized exactly.

## 4. Quotient-layer form

On the interval

\[
 \log r\le t<\log(r+1),
\]

put

\[
 A_r=\sum_{n\le r}{\mu(n)\over n},
 \quad
 B_r=\sum_{n\le r}{\mu(n)\over\sqrt n},
 \quad
 C_r=\sum_{n\le r}{\mu(n)\log n\over\sqrt n}.
 \tag{L-23805.10}
\]

Then (L-23805.7) is exactly

\[
 \boxed{
 a(t)=A_r-e^{-t/2}
 \left[
 {7\over8}B_r+{3\over16}(tB_r-C_r)
 \right].}
 \tag{L-23805.11}
\]

Its derivative is

\[
 a'(t)=e^{-t/2}
 \left[
 {1\over4}B_r+{3\over32}(tB_r-C_r)
 \right].
 \tag{L-23805.12}
\]

Hence every quotient layer has at most one interior critical point. GCF is
therefore equivalent to a completely explicit countable ledger consisting of:

1. the two one-sided endpoint values at every logarithmic integer knot;
2. when it lies inside the interval, the single critical value determined by
   (L-23805.12).

This is a much smaller symbolic target than an arbitrary continuum sign.

## 5. Hausdorff moment probes

If GCF holds and `W=e^{-S}`, then

\[
 \boxed{
 \mathbb E[W^k]
 ={(k+1)(k+2)
  \over8k(k+\tfrac12)^2\zeta(k+1)},
 \qquad k=1,2,\ldots.}
 \tag{L-23805.13}
\]

Consequently every finite Hausdorff difference must satisfy

\[
 \boxed{
 (-1)^r\Delta^r
 \left[
 {(k+1)(k+2)
  \over8k(k+\tfrac12)^2\zeta(k+1)}
 \right]\ge0.}
 \tag{L-23805.14}
\]

These all-order inequalities provide a zero-free real-axis review interface.
They are necessary finite probes; the production proof should still establish
the physical density sign (L-23805.8), or separately justify the analytic
uniqueness step from all integer moments.

## 6. Why this is the genuine arithmetic hinge

The factor `1/zeta(s+1)` in (L-23805.4) is exactly the reciprocal-zeta channel
found by the finite Möbius decoder `L-23803`. It has not been discarded; the
gamma smoothing in (L-23805.6) is precisely the amount needed to turn the sharp
logarithmic carry target into a candidate positive factor.

If an off-critical zero exists, the corresponding pole of `A(s)` lies to the
right of `Re s=-1/2` and produces a slower-decaying oscillatory term in
`a(t)`. Thus no proof may obtain GCF from a phase-blind absolute-value estimate.
A valid proof must preserve the complete quotient-layer signs, use an exact
reflected/Type-II square, or construct the probability factor directly.

## 7. Permitted proof mechanisms

A proof of GCF may use any of the following, provided the complete source is
retained:

1. a direct coupling proving (L-23805.9);
2. a quotient-layer induction using (L-23805.11)--(L-23805.12);
3. an all-order Hausdorff or Stieltjes factorization with a complete uniqueness
   argument;
4. a reflected Selberg/LCM Gram square for the exact Möbius–Riesz density;
5. a source-specific balanced Type-II contraction specialized to
   (L-23805.7).

The first critical Mertens/Farey cell remains a mandatory mutation test: a proof
that takes absolute values before signed recombination is invalid.

## 8. Proof boundary

Closed exactly:

- the quotient transform;
- the physical Möbius–Riesz density;
- the gamma/carry convolution implication;
- the quotient-layer and moment review interfaces.

Open and load bearing:

- GCF, equation (L-23805.8).

A proof of GCF completes the carry proposal through `L-23806/T-23801`. No RH
claim is made by this lemma alone.
