# L-98913 — A normalized positive-carrier model removes every artificial open-half-plane branch

Claim ID: `L-98913`  
Status: **PROVED EXACT SOURCE/ANALYTIC THEOREM; HEAT ESTIMATE OPEN**  
Created: 2026-08-18  
Depends on: `L-98700`, `L-98912`  
RH status: **not assumed**

The pole-centered object of `L-98912` still contains the two finite dyadic
factors inherited from `B_diamond`. Their inverses are positive carriers:

\[
 (1-2^{-s})^{-\theta}
 =\sum_{k\ge0}\frac{(\theta)_k}{k!}2^{-ks},
\]

\[
 (1-2^{-s-1})^{-\theta}
 =\sum_{k\ge0}\frac{(\theta)_k}{k!}2^{-k}2^{-ks},
\]

with nonnegative coefficients. Tensoring these parity-neutral carriers with
`widetilde B_theta` gives the normalized pole-centered fractional reciprocal
zeta

\[
\boxed{
 \mathfrak B_\theta(s)
 =\left(\frac{s}{(s-1)\zeta(s)}\right)^\theta.
}
\tag{L-98913.1}
\]

For real `s>1` choose the positive branch. The point `s=1` is removable and

\[
\boxed{\mathfrak B_\theta(1)=1.}
\tag{L-98913.2}
\]

Moreover `mathfrak B_theta(s)->1` as `s->+infinity`. Thus the normalization has
a vacuum coefficient and no deterministic branch at the zeta pole.

The source realization is exact. Write

\[
 L_\zeta(s)=\log\zeta(s)
 =\sum_{p^r}\frac1r p^{-rs}.
\]

Then `exp(-theta L_zeta)=Q_theta-S_theta`, where `Q_theta,S_theta` are the
positive even and odd generalized-prime chaoses. The factor

\[
 \left(\frac{s}{s-1}\right)^\theta
\]

is the positive parity-neutral continuum carrier of `L-98912`. Their tensor
product realizes (L-98913.1) before signed observation.

If `rho` is a nontrivial zero of multiplicity `m`, then `rho/(rho-1)` is finite
and nonzero, so `mathfrak B_theta` has a branch singularity of order `m theta`
at `rho`. In the open half-plane `Re s>0`, the zeta pole and all artificial
finite-Euler branches have been removed. Every remaining nonremovable branch
is therefore attached to a nontrivial zeta zero.

## Corrected heat target

Let `mathfrak H_(theta,T)(tau)` denote the Gaussian Mellin heat transform of the
mixed discrete-continuous source realizing `mathfrak B_theta`. An off-line zero
at horizontal displacement `delta` contributes energy with rate
`2 delta^2`, exactly as in the branch-contour calculation of `L-98702`.

The precise remaining theorem is:

> **Normalized Pole-Centered Fractional Heat Estimate (`NPCFHE`).** There is an
> absolute `C` such that, for every sufficiently small fixed `theta>0`, every
> `T>=1`, and every real center,
> \[
> \int |\mathfrak H_{\theta,T}(\tau)|^2w_{T,\tau_0}(\tau)d\tau
> \le (1+T)^C\exp\{C\theta T+o(T)\},
> \]
> from one prescribed cross-scale Gram of the discrete prime chaos and the
> continuum carrier.

`NPCFHE` would imply RH by choosing `theta` after a hypothetical off-line zero.
This lemma does not prove that estimate. It removes all deterministic analytic
branches that invalidated the uncentered formulation and leaves one exact,
source-typed conclusion-producing theorem.
