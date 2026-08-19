# L-99001 — Fractional order changes only the heat prefactor, never the heat type

Claim ID: `L-99001`  
Status: **COMPLETE LOCAL HANKEL THEOREM**  
Created: 2026-08-18

Let `sigma_0` be the observation line and suppose that in a slit neighborhood
of `rho=beta+i gamma`,

\[
 F_\theta(s)=H_\theta(s)(s-\rho)^{-\kappa_\theta},
 \qquad H_\theta(\rho)\ne0,
 \qquad \kappa_\theta>0.
\]

For the Gaussian Mellin packet

\[
 \mathcal H_{\theta,T}(\tau)
 =\frac{1}{2\pi i}\int F_\theta(s)
 e^{T(s-\sigma_0-i\tau)^2}\,ds,
\]

move the contour through a Hankel loop around `rho`.  Setting `tau=gamma` and
`s=rho+w/sqrt(T)` gives

\[
 \boxed{
 \mathcal H_{\theta,T}(\gamma)
 =c_{\rho,\theta}
 T^{\kappa_\theta/2-1/2}
 e^{(\beta-\sigma_0)^2T}
 (1+O_{\rho,\theta}(T^{-1/2})).
 }
\tag{L-99001.1}
\]

The exact power of `T` depends on the normalization of the Hankel packet; the
exponential type does not:

\[
 \boxed{
 \limsup_{T\to\infty}\frac1T
 \log|\mathcal H_{\theta,T}(\gamma)|
 =(\beta-\sigma_0)^2.
 }
\tag{L-99001.2}
\]

For a zeta zero of multiplicity `m`, fractionalization changes
`kappa_theta` to `m theta`; it leaves `beta` unchanged.  Therefore tuning
`theta` can alter only polynomial factors and constants.  It cannot make an
off-line singularity grow at a different exponential rate.

Applied to the pole-centered reciprocal-Julia function on `sigma_0=1/2`, every
off-line zero has amplitude type `(beta-1/2)^2` and energy type
`2(beta-1/2)^2`, independently of the fractional intensity.  Any source-side
upper estimate with an arbitrarily small `theta`-proportional exponential type
is already a zero-location theorem; it cannot follow from fractionalization
alone.
