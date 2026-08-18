# L-98712 — The fractional heat packet's first variation is the phase-locked prime-power carrier

Claim ID: `L-98712`  
Status: **PROVED EXACT TRANSFORM THEOREM**  
Created: 2026-08-18  
Depends on: `L-98700`, `L-98711`  
RH status: **not assumed**

Since

\[
B_\diamond(s)^\theta=e^{\theta\log B_\diamond(s)},
\]

one has on every finite cutoff and then by Gaussian dominated convergence

\[
\left.\partial_\theta\mathscr B_{\theta,T}(\tau)\right|_{\theta=0}
=\mathcal H_T[\log B_\diamond](\tau),
\tag{L-98712.1}
\]

where `mathcal H_T` denotes the exact logarithmic Gaussian coefficient window.
Writing

\[
\log B_\diamond(s)
=-\sum_{q\in\mathcal Q}\lambda_\diamond(q)q^{-s},
\]

and applying the log-number generator gives

\[
\boxed{
 i\partial_\tau
 \left.\partial_\theta\mathscr B_{\theta,T}(\tau)\right|_{\theta=0}
=-\sum_{q\in\mathcal Q}
 \frac{\Lambda_\diamond(q)}{\sqrt q}
 e^{-(\log q)^2/(4T)}e^{-i\tau\log q},
}
\tag{L-98712.2}
\]

with

\[
\Lambda_\diamond(q)=\lambda_\diamond(q)\log q\ge0.
\]

Thus the tangent of the fractional proposal is not an abstract Fock trace. It
is the explicit phase-locked generalized-prime carrier. After subtracting the
finite dyadic gauge, this is the same arithmetic carrier class which appears in
the independent First-Hermite covariance lane.

Consequently any proof of PLFHE must control (L-98712.2), together with all of
its Sibuya support cumulants. A kernel redesign or phase-independent positive
completion cannot remove this tangent: safe-line preconditioners cancel in the
phase-locked covariance, as in the gauge-invariance theorem of the
First-Hermite route.
