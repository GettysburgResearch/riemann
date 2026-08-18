# R-98912 — Positive spectral completion has a theta-independent heat-rate floor

Claim ID: `R-98912`  
Status: **PROVED EXACT COMPLETION NO-GO + ASYMPTOTIC TRACE LOWER BOUND**  
Created: 2026-08-18  
Depends on: `L-98913`  
RH status: **not assumed**

Let

\[
 \nu_{\rm pr}=\sum_{p^r}\frac1r\,\delta_{r\log p}
\]

be the generalized-prime log measure and

\[
 \nu_{\rm c}(dt)=\frac{e^t-1}{t}\,dt
\]

be the positive continuum carrier from `L-98912`. The logarithm of the
normalized pole-centered source is the signed measure

\[
 \sigma=\nu_{\rm c}-\nu_{\rm pr}.
\tag{R-98912.1}
\]

The two positive measures are mutually singular: one is absolutely continuous
and the other purely atomic. Hence

\[
 |\sigma|=\nu_{\rm c}+\nu_{\rm pr}.
\tag{R-98912.2}
\]

Consider any positive-metric two-channel realization with an exact
self-adjoint log generator. Its spectral measure is a positive-semidefinite
matrix measure

\[
 M(dt)=\begin{pmatrix}M_{++}(dt)&\theta\sigma(dt)\\
                       \theta\sigma(dt)&M_{--}(dt)
       \end{pmatrix} \succeq0.
\]

Positivity on every Borel set, followed by Radon--Nikodym localization, gives

\[
\boxed{
 M_{++}+M_{--}\ge2\theta|\sigma|
 =2\theta(\nu_{\rm c}+\nu_{\rm pr}).
}
\tag{R-98912.3}
\]

Thus distinct spectral locations cannot be canceled in the positive diagonal
by declaring a cross-scale coupling. Exact generator covariance forces the
usual total-variation price.

For the one-particle half-heat norm use

\[
 w_T(t)=e^{-t/2-t^2/(4T)}.
\]

The continuum part alone gives

\[
\begin{aligned}
 \int_0^\infty w_T(t)\,\nu_{\rm c}(dt)
 &=\int_0^\infty
 e^{-t/2-t^2/(4T)}\frac{e^t-1}{t}\,dt\\
 &=2\sqrt\pi\,T^{-1/2}e^{T/4}(1+o(1)).
\end{aligned}
\tag{R-98912.4}
\]

The last line is the Gaussian saddle at `t=T`; the subtracted `1` is
exponentially negligible. Therefore every such positive spectral completion
has one-particle diagonal trace at least

\[
\boxed{
 4\theta\sqrt\pi\,T^{-1/2}e^{T/4}(1+o(1)).
}
\tag{R-98912.5}
\]

A squared-energy estimate obtained by the `L-98703` mechanism—Schur domination
by the positive diagonal followed by source-norm/trace control—therefore has a
rate floor `1/2`, independent of how small fixed `theta` is. In particular its
claimed first-chaos trace rate `96 theta T` is impossible for all sufficiently
small `theta`.

## Scope

This no-go applies to positive-metric spectral completions that:

1. realize the exact prime/continuum signed log measure;
2. intertwine one self-adjoint total-log generator;
3. pay the heat cross block by the positive diagonal or its Fock trace.

It does not prove that the normalized heat packet itself has rate `1/2` after
pole centering. It proves that positivity plus diagonal Schur payment cannot
establish the desired tunable rate. A surviving fractional route would need an
additional exact off-diagonal cancellation theorem beyond positive completion;
that theorem is already RH-bearing in substance and is not supplied by the Tao
local ports.
