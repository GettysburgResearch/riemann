# L-98912 — A positive continuum carrier removes the zeta-pole branch exactly

Claim ID: `L-98912`  
Status: **PROVED EXACT ALGEBRAIC/LAPLACE THEOREM; HEAT ESTIMATE OPEN**  
Created: 2026-08-18  
Depends on: `L-98700`, `L-98910`  
RH status: **not assumed**

The obstruction in `L-98910` can be removed algebraically without the false
Weyl-invariance step.

For `Re s>1`, define

\[
 C(s)=\frac{s}{s-1}.
\]

Frullani's identity gives the positive Laplace logarithm

\[
\boxed{
 \log C(s)
 =\int_0^\infty e^{-st}\frac{e^t-1}{t}\,dt.
}
\tag{L-98912.1}
\]

The density `(e^t-1)/t` is strictly positive. Hence, for every `theta>0`,
`C(s)^theta` is the Laplace transform of a positive continuous
compound-Poisson/Fock carrier in the same log-coordinate category as the
generalized-prime source.

Define the pole-centered reciprocal-Julia function

\[
\boxed{
 \widetilde B_\theta(s)
 =\left(C(s)B_\diamond(s)\right)^\theta
 =\left(\frac{s(1-2^{-s})(1-2^{-s-1})}
              {(s-1)\zeta(s)}\right)^\theta.
}
\tag{L-98912.2}
\]

Since

\[
 B_\diamond(s)=\frac38(s-1)(1+O(s-1)),
\]

one has

\[
\boxed{
 \widetilde B_\theta(s)=(3/8)^\theta(1+O_\theta(s-1))
}
\tag{L-98912.3}
\]

near `s=1`. The noninteger pole branch is gone.

If `rho` is a nontrivial zeta zero, then `rho` is neither zero nor one, so
`C(rho)` is finite and nonzero. Therefore `widetilde B_theta` retains a branch
singularity of order `m theta` at every zero of multiplicity `m`; the
conclusion-producing zero detector is not cancelled.

Finally, `B_diamond^theta=Q_theta-S_theta` has the exact positive two-channel
source of `L-98700`, while `C^theta` is a positive parity-neutral carrier by
(L-98912.1). Their tensor product gives an exact positive two-channel
realization of `widetilde B_theta` before signed observation. No Weyl
translation is used.

Equivalently, at logarithmic-source level,

\[
 \log\widetilde B_\theta(s)
 =-\theta\left[
 L_\diamond(s)-
 \int_0^\infty e^{-st}\frac{e^t-1}{t}\,dt
 \right].
 \tag{L-98912.4}
\]

Thus the corrected first-chaos object is the exact discrepancy between the
discrete generalized-prime measure and one explicit positive continuum
carrier.

## Open interface

This theorem removes the deterministic branch obstruction but does not prove a
heat-energy estimate. A valid continuation must construct a common cross-scale
Gram coupling the discrete Tao atoms to the continuum carrier and prove a
trace-free heat estimate for the mixed discrete-continuous packet. Call this
open theorem **Pole-Centered Fractional Heat Estimate (`PCFHE`)**.

`PCFHE` is a stricter and better-typed target than the informal Weyl centering
in `L-98703`: the centered analytic function, positive carrier, parity channels,
and zero detector are all explicit and identical on both sides of the proposed
estimate.
