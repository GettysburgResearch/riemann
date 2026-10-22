# Critical-energy attack: exact exponent, all-moments route, and Bohr closure

Date: 2026-08-07  
Agent: `gpt56-08`  
Branch: `agent/gpt56-08/9512-critical-energy-exponent`  
Status: `PROPOSED`; RH is not claimed proved

## Requested target

The requested uniform bound was

\[
\mathfrak A(x)=O_\varepsilon(x^{-3+\varepsilon}),
\]

where `mathfrak A` is the positive integrated-discrepancy energy of `L-9511`.

That bound was not proved in this pass.

## Exact identification

The state behind the energy is exactly the Kaczorowski--Wiertelak analytic part
of the summatory Euler-totient error:

\[
\mathcal R_1(x)=-E^{\rm AN}(x),
\]

with

\[
E^{\rm AN}(x)
=\frac12\left(1+\sum_{d>=1}\mu(d)\{x/d\}^2\right).
\]

Thus

\[
\mathfrak A(x)
=x^{-4}|E^{\rm AN}(x)|^2
+x^{-5}\left[
{(6/\pi^2)^2\over20}+\int_1^x|E^{\rm AN}(t)|^2dt
\right].
\]

The exact Q[C] checker `X-9512` verifies the finite identity at 72 rational
points without evaluating `pi`.

## Exact exponent theorem

Define

\[
\Theta_{\rm en}
={1\over2}\limsup_{x\to\infty}
{\log(1+x^3\mathfrak A(x))\over\log x}.
\]

`T-9504` proves

\[
\Theta_{\rm en}
=\sup_{\zeta(\rho)=0}\Re\rho-\frac12.
\]

Hence a hypothetical off-line zero forces a polynomially growing positive
energy mode. No phase cancellation, zero simplicity, or residue lower bound is
needed because the energy retains the endpoint square.

This theorem also proves that the requested energy estimate is exactly RH, not
a softer positive inequality hidden behind the scalar criterion.

## New all-moments route

`T-9505` replaces the pointwise estimate by the positive hierarchy

\[
\int_X^{2X}|E^{\rm AN}(t)|^{2k}dt
\ll_{k,\varepsilon}X^{k+1+\varepsilon}.
\]

An unbounded sequence of passing moment orders suffices for RH. The
unconditional dyadic Lipschitz bound

\[
|E^{\rm AN}(y)-E^{\rm AN}(x)|
\ll\log X\,|y-x|
\]

turns the `2k`-th moment into the pointwise exponent

\[
\frac12+\frac1{4k+2}.
\]

This exactly matches the finite-moment loss in Alberto Verjovsky's July 2026
local-moment criterion for Möbius Fourier polynomials. The agreement is recorded
in `O-9512`; neither criterion currently supplies the required moment bounds.

## Complete Bohr/resonant energy

For

\[
S_D(x)=\sum_{d<=D}\mu(d)
\left(\{x/d\}^2-\frac13\right),
\]

`L-9513` proves the exact pair covariance

\[
\operatorname{mean}
[f(x/d)f(x/e)]
={g^2\over12de}+{g^4\over180d^2e^2},
\qquad g=(d,e),
\]

and the positive Jordan factorization

\[
\begin{aligned}
\mathcal B_D={}&
{1\over12}\sum_{q<=D}J_2(q)
\left(\sum_{q|d<=D}{\mu(d)\over d}\right)^2\\
&+{1\over180}\sum_{q<=D}J_4(q)
\left(\sum_{q|d<=D}{\mu(d)\over d^2}\right)^2.
\end{aligned}
\]

Consequently

\[
\mathcal B_D\ll D
\]

unconditionally. The full-period resonant packet already has the conjectured
root-mean-square size.

`X-9513` verifies 144 pair covariances and twelve packet factorizations exactly.

## Sharp remaining sub-obstruction

The missing theorem is no longer generic positivity. It is a local-to-Bohr
transference at critical Farey resolution.

Denominators near `D` generate rational frequencies separated by `D^-2`, while
a physical interval of length `D` resolves only `D^-1`. A phase-blind large
sieve therefore loses one full power. The unresolved near-resonant clusters are
exactly where the Mertens/rightmost-zero information survives.

The sharp target is either:

1. for an unbounded sequence of `k`, prove the critical multilinear moment
   estimate above; or
2. prove a Möbius-weighted local-to-Bohr inequality for the complete
   Bernoulli-plus-tail packet, then extend it to unbounded even moments.

## Closed shortcut

`R-9503` proves that one prime filter

\[
I-p^{-1/2}T_{\log p}
\]

has norm `1+p^-1/2` on translation-invariant energies. Thus the Euler cascade
cannot be closed by multiplying prime-by-prime contractions. All-prime
cancellation or a source-specific boundary Lyapunov functional is required.

## SERIOUS RESOLUTION PATH

The strongest current route is:

1. exact analytic-totient/Farey frequency expansion;
2. exact Jordan-square control of resonances;
3. a Möbius-weighted estimate for near resonances on intervals of critical
   length;
4. multilinear extension for unbounded moment order;
5. `T-9505` upgrades the moment ladder to the uniform critical energy bound;
6. `T-9504` then forces the rightmost-zero displacement to vanish.

The path is complete as a reduction. Step 3, and then its unbounded-moment
extension, remain unproved and carry the RH content.
