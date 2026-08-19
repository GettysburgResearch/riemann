# L-99000 — Exact pole-centered mixed source and signed first-chaos current

Claim ID: `L-99000`  
Status: **COMPLETE EXACT SOURCE IDENTITY**  
Created: 2026-08-18

Define

\[
 \widetilde B_\theta(s)
 =\left(\frac{s}{s-1}B_\diamond(s)\right)^\theta,
 \qquad \Re s>1.
\tag{L-99000.1}
\]

By `R-99000`, `B_diamond(s)=(3/8)(s-1)(1+O(s-1))`, so

\[
 \widetilde B_\theta(1)=(3/8)^\theta\ne0.
\]

At every nontrivial zeta zero `rho`, the factor `rho/(rho-1)` is finite and
nonzero.  Thus pole centering removes only the deterministic singularity at
one and preserves every conclusion-producing zeta singularity.

Put

\[
 \Psi(s)=\log\frac{s}{s-1}+\log B_\diamond(s).
\]

Then

\[
 \boxed{
 \Psi'(s)
 =\frac1s-\frac1{s-1}
 +\frac d{ds}\log[(1-2^{-s})(1-2^{-s-1})]
 -\frac{\zeta'}{\zeta}(s).
 }
\tag{L-99000.2}
\]

This is the exact first-chaos source: one signed continuum-minus-prime current,
plus the explicit two-adic finite correction.  The cancellation at `s=1` is
inside this signed source and is destroyed by separate absolute values or
separate positive-trace payments.

For every fixed `theta>0`, fractionalization multiplies the singularity order
but does not move any singularity.  A zero `rho=beta+i gamma` contributes to the
pole-centered heat packet at exponential rate

\[
 (\beta-1/2)^2
\]

in amplitude and `2(beta-1/2)^2` in local energy, independently of `theta`.
Only the polynomial prefactor depends on the fractional order.
