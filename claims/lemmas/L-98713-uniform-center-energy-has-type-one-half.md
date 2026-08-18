# L-98713 — The phase-blind uniform-center energy has exact exponential type one half

Claim ID: `L-98713`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Depends on: `L-98710`, `L-98711`, `R-98710`  
RH status: **not assumed**

For fixed `0<theta<1`, put

\[
A_{\theta}(T)
=\sum_{n\ge1}\frac{|b_\theta(n)|}{\sqrt n}
 e^{-(\log n)^2/(4T)}.
\]

The Euler product of the absolute coefficients has the form

\[
\boxed{
D_{\theta}^{\rm abs}(s)
:=\sum_{n\ge1}\frac{|b_\theta(n)|}{n^s}
=\zeta(s)^\theta H_{\theta}^{\rm abs}(s),
}
\tag{L-98713.1}
\]

where `H_theta^abs` is holomorphic and nonzero in a classical dented
neighborhood of `s=1`.

For an odd prime, the local absolute factor is

\[
1+\sum_{k\ge1}a_\theta(k)p^{-ks}
=2-(1-p^{-s})^\theta.
\]

Multiplying by `(1-p^{-s})^theta` gives `1+O_theta(p^{-2s})`, so the residual
Euler product converges absolutely for `Re s>1/2`. The dyadic factor is one
fixed-prime holomorphic nonzero multiplier and does not alter the singular
exponent.

Gaussian Selberg--Delange therefore gives

\[
\boxed{
A_\theta(T)
=c_\theta^{\rm abs}
 T^{\theta-1/2}e^{T/4}(1+o(1)),
\qquad c_\theta^{\rm abs}>0.
}
\tag{L-98713.2}
\]

Since `w_T` has total mass one,

\[
E_{\theta,T}(\tau_0)
\le A_\theta(T)^2
\]

for every center. Conversely, the Bohr twist in `R-98710` gives

\[
\sup_{\tau_0}E_{\theta,T}(\tau_0)
\gg_\theta e^{T/2}T^{2\theta-3/2}.
\]

Consequently

\[
\boxed{
\lim_{T\to\infty}
\frac1T\log\sup_{\tau_0\in\mathbb R}
E_{\theta,T}(\tau_0)
=\frac12.
}
\tag{L-98713.3}
\]

The phase-blind exponential rate is thus exactly `1/2`, independently of how
small `theta` is. No change of the constants `96` or of the
`T^(3/4)log^2 T=o(T)` remainder can repair `L-98703.1` at uniform-center scope.
