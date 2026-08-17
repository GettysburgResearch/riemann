# L-93293 — Positive spectral representation and quantitative carrier mean square

Claim ID: `L-93293`  
Status: **PROVED UNCONDITIONAL CARRIER-AVERAGE THEOREM**  
Created: 2026-08-18  
Depends on: `L-93281`, `L-93292`; Chebyshev's bound for `psi`  
RH status: **not assumed**

Fix `q>=1` and an integer `m>=1`. Put

\[
 a_n=\frac{\Lambda(n)}{\sqrt n}h_{q,m}(\log n),
\qquad
 S_{q,m}(t)=\sum_{n\ge2}a_ne^{it\log n}.
\tag{L-93293.1}
\]

The Gaussian finite-difference weight makes `sum |a_n|^2` convergent. The
centered covariance of PR #546 is

\[
 \mathfrak C_{q,m}(t)=S_{q,m}(t)-S_{q,m}^{\rm cont}(t),
\tag{L-93293.2}
\]

where `S_cont` is the Fourier transform of an `L1 intersection L2` function.

## 1. Exact autocorrelation

For every real shift `u`, the Besicovitch carrier autocorrelation exists and is

\[
\boxed{
\begin{aligned}
 \mathscr A_{q,m}(u)
 &:={}
 \lim_{T\to\infty}\frac1T
 \int_T^{2T}
 \mathfrak C_{q,m}(t+u)
 \overline{\mathfrak C_{q,m}(t)}\,dt\\
 &=\sum_{n\ge2}
 \frac{\Lambda(n)^2}{n}
 |h_{q,m}(\log n)|^2e^{iu\log n}.
\end{aligned}}
\tag{L-93293.3}
\]

Indeed, distinct logarithmic frequencies are orthogonal in long carrier
averages. The continuous model has finite global `L2` norm, so its normalized
mean square and both cross terms tend to zero.

Consequently `A_(q,m)` is positive definite, with positive atomic spectral
measure

\[
\boxed{
 d\sigma_{q,m}
 =\sum_{n\ge2}\frac{\Lambda(n)^2}{n}
 |h_{q,m}(\log n)|^2\delta_{\log n}.
}
\tag{L-93293.4}
\]

This is the requested positive spectral representation for the corrected
phase-locked covariance.

## 2. Quantitative energy

Chebyshev's theorem implies

\[
 \sum_{n\le e^U}\frac{\Lambda(n)^2}{n}\ll1+U^2.
\tag{L-93293.5}
\]

For fixed `m`, the finite-difference Gaussian satisfies

\[
 |h_{q,m}(u)|^2
 \ll_m\left(1+\frac{u^4}{q^2}\right)e^{-u^2/(8q)}
 \qquad(u\ge0,q\ge1).
\tag{L-93293.6}
\]

Dyadic decomposition in `u/sqrt(q)` therefore gives

\[
\boxed{
 \mathscr A_{q,m}(0)
 =\sum_{n\ge2}|a_n|^2\ll_m q.
}
\tag{L-93293.7}
\]

In particular, for every fixed threshold `H>0`,

\[
\boxed{
 \limsup_{T\to\infty}\frac1T
 \left|\{t\in[T,2T]:|\mathfrak C_{q,m}(t)|\ge H\}\right|
 \ll_m\frac q{H^2}.
}
\tag{L-93293.8}
\]

This is an unconditional quantitative advance for the corrected carrier, not
the refuted raw `SID_H` field. It controls carrier density but does not remove
one prescribed exceptional carrier.
