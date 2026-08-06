# L-20208 — Sharp Fejer ramp barrier at the first prime half-knot

Claim ID: `L-20208`  
Title: Every nonzero finite RH-positive FIR filter pays a strictly negative first-prime coefficient at half support  
Status: **PROPOSED — COMPLETE FINITE ALGEBRAIC PROOF**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: Fejer--Riesz factorization; elementary conditional negativity of the distance kernel  
Scope: every finite real even trigonometric filter used against the zeta screw function

## 1. Spectral and prime-ramp coordinates

Let

\[
 P(x)=\sum_{k=1}^{N}\lambda_k(1-\cos kx)
\]

be a nonzero real trigonometric polynomial satisfying

\[
 P(x)\ge0\qquad(x\in\mathbb R).
\]

Define its ramp transform

\[
\boxed{
 L_P(s)=\sum_{k=1}^{N}\lambda_k(k-s)_+,
 \qquad s\ge0.}
\]

For the filtered screw statistic

\[
 \mathcal S_P(t)=\sum_{k=1}^{N}\lambda_k\Psi(kt),
\]

the coefficient of a prime power `q` is exactly

\[
\boxed{
 -t\,{\Lambda(q)\over\sqrt q}\,
 L_P\!\left({\log q\over t}\right).}
\]

Thus nonnegative prime weight corresponds to `L_P<=0` at the normalized prime
location.

## 2. Fejer factorization

Since `P>=0`, Fejer--Riesz gives a polynomial `A` with

\[
 P(x)=|A(e^{ix})|^2.
\]

Because `P(0)=0`, one has `A(1)=0`; hence

\[
 A(z)=(1-z)Q(z),
 \qquad
 Q(z)=\sum_{j=0}^{N-1}q_jz^j.
\]

Set `q_-1=q_N=0` and

\[
 a_j=q_j-q_{j-1}\qquad(0\le j\le N).
\]

Then `a_j` are the coefficients of `A` and

\[
 \sum_{j=0}^{m}a_j=q_m.
\]

## 3. Two exact ramp identities

Write the Fourier expansion

\[
 P(x)=c_0+2\sum_{k=1}^{N}c_k\cos kx.
\]

The chosen convention gives

\[
 c_0=\sum_k\lambda_k,
 \qquad
 c_k=-\frac{\lambda_k}{2}\quad(k\ge1).
\]

The distance-kernel identity for the zero-sum vector `a` is

\[
 \sum_{j,\ell=0}^{N}|j-\ell|a_j\overline{a_\ell}
 =-2\sum_{m=0}^{N-1}|q_m|^2.
\]

On the other hand the left side equals

\[
 2\sum_{k=1}^{N}k c_k.
\]

Therefore

\[
\boxed{
 L_P(0)=\sum_{k=1}^{N}k\lambda_k
 =2\sum_{j=0}^{N-1}|q_j|^2>0.}
\]

Also `c_0=sum_j|a_j|^2`, so

\[
\begin{aligned}
 L_P(1/2)
 &=L_P(0)-\frac12\sum_k\lambda_k\\
 &=2\sum_j|q_j|^2-rac12\sum_j|q_j-q_{j-1}|^2\\
 &=\frac12\sum_{j=0}^{N}|q_j+q_{j-1}|^2.
\end{aligned}
\]

Hence

\[
\boxed{
 L_P(1/2)>0.}
\]

No nonzero finite RH-positive FIR filter can make the normalized half-knot prime
coefficient nonnegative.

## 4. Sharp quantitative barrier

The quadratic form

\[
 \sum_{j=0}^{N}|q_j+q_{j-1}|^2
\]

has the tridiagonal matrix with diagonal `2` and adjacent entries `1`. Its least
eigenvalue is

\[
 4\sin^2\!\left({\pi\over2(N+1)}\right).
\]

Using `L_P(0)=2||q||_2^2` gives the sharp inequality

\[
\boxed{
 {L_P(1/2)\over L_P(0)}
 \ge
 \sin^2\!\left({\pi\over2(N+1)}\right).}
\]

Equality is attained, up to a scalar, by

\[
\boxed{
 q_j=(-1)^j\sin\!\left({(j+1)\pi\over N+1}\right),
 \qquad0\le j<N.}
\]

Consequently

\[
 \inf_{\deg P\le N}
 {L_P(1/2)\over L_P(0)}
 =\sin^2\!\left({\pi\over2(N+1)}\right)
 \sim {\pi^2\over4N^2}.
\]

## 5. Zeta consequence

At the base support `t=log 4`, the first prime `q=2` sits exactly at

\[
 {\log2\over\log4}=\frac12.
\]

Its filtered coefficient is therefore

\[
 -\log4\,{\log2\over\sqrt2}\,L_P(1/2)<0.
\]

So every nonzero finite trigonometric screw square retains an unavoidable
negative first-prime channel. The best possible degree-`N` filter reduces that
debt only quadratically, by the sharp factor above.

This explains structurally why the signed terminal-flat attempt of `T-20204`
could make every prime coefficient positive only by reversing the RH spectral
sign.

## 6. Research consequence

A viable full proof cannot eliminate all adverse prime weight with one finite
RH-positive FIR filter. It must instead do at least one of:

1. control the unavoidable first-prime debt by a positive bulk transport;
2. pass to a growing-degree endpoint-concentrated limit with a quantitative
   cofinal remainder;
3. use an infinite/noncompact positive filter with an independently justified
   transform and source domain;
4. prove the equivalent prime-polygon or Chebyshev-Riesz domination directly.

The equality vector gives the canonical finite endpoint-concentrated filter for
such a growing-degree attack.
