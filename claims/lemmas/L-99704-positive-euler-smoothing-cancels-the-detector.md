# L-99704 — Every absolutely subcritical positive Euler smoothing cancels the reciprocal-zeta detector

Claim ID: `L-99704`  
Status: **PROVED EXACT ANALYTIC FIREWALL**  
Created: 2026-08-20  
RH status: **not assumed**

Let `0<=theta_p<=1` and define the positive Euler smoothing

\[
G_\theta(z)=\prod_p(1-\theta_pp^{-z})^{-1}.
\tag{L-99704.1}
\]

Put `a_p=1-theta_p`. Assume that for every `sigma>sigma_0>=0`,

\[
\sum_p a_pp^{-\sigma}<\infty.
\tag{L-99704.2}
\]

Then

\[
R_\theta(z)
:=\frac{G_\theta(z)}{\zeta(z)}
=
\prod_p\frac{1-p^{-z}}{1-\theta_pp^{-z}}.
\tag{L-99704.3}
\]

For `Re z>=sigma>sigma_0`, the logarithm of one local factor is

\[
\log(1-p^{-z})-
\log(1-(1-a_p)p^{-z})
=-a_pp^{-z}+O(a_pp^{-2\sigma}+a_p^2p^{-2\sigma}).
\]

Thus (L-99704.2) gives locally uniform convergence of the logarithm on
`Re z>sigma_0`. Therefore

\[
\boxed{
R_\theta\text{ is holomorphic and zero-free on }\Re z>\sigma_0.
}
\tag{L-99704.4}
\]

Multiplying any reciprocal-zeta witness by `G_theta` replaces `1/zeta(z)` by
the holomorphic factor `R_theta(z)`. Every zeta-zero pole in that half-plane is
cancelled.

The local coefficient identity is already visible at one prime:

\[
\frac{1-x}{1-\theta x}
=1-(1-\theta)\sum_{k\ge1}\theta^{k-1}x^k.
\tag{L-99704.5}
\]

The residual signed coefficients may be absolutely small, but the detector has
been removed with them.

## Consequence

Any proposed closure of the native parity source by a coefficientwise positive
Euler completion satisfying

\[
\sum_p(1-\theta_p)p^{-1/2}<\infty
\]

cannot prove RH through the reciprocal-zeta pole mechanism: it cancels those
poles identically. The critical proof must retain a nonsummable parity boundary
and exploit conditional owner covariance rather than absolute subcriticality.

This theorem does not forbid finite-prime smoothing, compact logarithmic boxes,
or signed/source-correlated transformations whose Mellin multiplier is
zero-free. It forbids the tempting strategy “make every Euler tail absolutely
small by a positive product and then apply Landau.”
