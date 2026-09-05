# L-106450 — Odd endpoint Wronskians are positive exterior-square Xi sources

Claim ID: `L-106450`  
Status: **PROVED EXACT UNCONDITIONAL FOURIER-SOURCE THEOREM**  
Created: 2026-08-25  
Depends on: the classical positive even Xi Fourier kernel; `L-106401` is the case `m=1`  
RH status: **not assumed**

Let

\[
F(t)=\int_{\mathbb R}\Phi(u)e^{iut}\,du,
\qquad \Phi(-u)=\Phi(u)\ge0,
\]

where all moments required below are finite.  The standard Riemann Xi kernel
has these properties.

Fix an odd integer

\[
m=2r+1\ge1
\]

and define the endpoint Wronskian

\[
\boxed{
\mathcal W_m[F](t)
 =F'(t)F^{(m)}(t)-F(t)F^{(m+1)}(t).
}
\tag{L-106450.1}
\]

## 1. Exact Fourier density

Product convolution gives

\[
\widehat{\mathcal W_m[F]}(\xi)
 =i^{m+1}\int_{\mathbb R}
 v^m(u-v)\Phi(u)\Phi(v)\,du,
 \qquad v=\xi-u.
\]

Averaging with the same integral after `u` and `v` are exchanged gives

\[
\begin{aligned}
\widehat{\mathcal W_m[F]}(\xi)
&=-{i^{m+1}\over2}
 \int_{\mathbb R}
 (u-v)(u^m-v^m)
 \Phi(u)\Phi(v)\,du\\
&={(-1)^r\over2}
 \int_{\mathbb R}
 (u-v)^2Q_{m-1}(u,v)
 \Phi(u)\Phi(v)\,du,
\end{aligned}
\tag{L-106450.2}

where

\[
\boxed{
Q_{m-1}(u,v)
 ={u^m-v^m\over u-v}
 =\sum_{j=0}^{m-1}u^{m-1-j}v^j.
}
\tag{L-106450.3}
\]

Because `m` is odd, the real function `x -> x^m` is increasing.  Hence

\[
Q_{m-1}(u,v)\ge0
\]

for every real `u,v`, with the diagonal value `m u^(m-1)>=0`.  Therefore

\[
\boxed{
(-1)^r\widehat{\mathcal W_m[F]}(\xi)\ge0
\qquad(\xi\in\mathbb R).
}
\tag{L-106450.4}

This is a literal exterior-square source: the squared separation `(u-v)^2`
is multiplied by the positive divided difference of the odd monomial.

## 2. The fifth-derivative endpoint

For

\[
m=5
\]

one has `r=2` and

\[
Q_4(u,v)=u^4+u^3v+u^2v^2+uv^3+v^4>0
\]

away from `(u,v)=(0,0)`.  Thus

\[
\boxed{
\widehat{\Xi'\Xi^{(5)}-\Xi\Xi^{(6)}}(\xi)
 ={1\over2}\int_{\mathbb R}
 (2u-\xi)^2Q_4(u,\xi-u)
 \Phi(u)\Phi(\xi-u)\,du
 \ge0.
}
\tag{L-106450.5}

No derivative-saddle approximation, Euler product, zero-location theorem, or
hypothetical zero is used.

## 3. Exact endpoint-companion cancellation

For any real entire `F`, put

\[
E_{0,\pm}=F\pm i\lambda F',
\qquad
E_{m,\pm}=F^{(m)}\pm i\lambda F^{(m+1)}.
\]

Then direct multiplication gives

\[
\boxed{
E_{0,-}E_{m,+}-E_{0,+}E_{m,-}
 =-2i\lambda\mathcal W_m[F].
}
\tag{L-106450.6}

Thus, whenever `m=1 mod 4`, the complete denominator-cancelled endpoint
numerator is the derivative or phase rotation of one nonnegative Fourier
source.  The case `m=5` is the first endpoint which combines this positivity
with the repository's `99.7%` fixed-order entry.

## 4. Scope

Fourier-source positivity is not pointwise positivity after multiplication by
the variable endpoint all-pass phase.  The theorem does not bound the signed
Paley--Wiener complement, prove a source frame covers the companion model
space, or prove a new critical-line percentage.  It removes the
frozen-to-actual numerator interface for every endpoint order `m=1 mod 4`.