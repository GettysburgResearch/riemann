# T-15119 — Chebyshev dilation energy criterion

Claim ID: `T-15119`  
Title: The multiplicative dilation energy of the normalized Chebyshev function has growth exponent equal to the rightmost zeta-zero displacement  
Status: **PROPOSED PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15145`; the Euler-product logarithmic derivative; half-plane Paley–Wiener theory; standard fixed-zero-free-half-plane bounds for `zeta'/zeta`  
Scope: one explicit global prime-only criterion equivalent to RH

## 1. The arithmetic energy

Fix any real scale `a>1`, let

\[
 P(t)=\frac{\psi(t)}t,
\]

and define

\[
 \boxed{
 \mathcal E_a(Y)
 =\int_2^Y|P(t)-P(t/a)|^2dt.}
 \tag{T-15119.1}
\]

By `L-15145`, this is exactly the cumulative energy of the causal safe prime
signal

\[
 Q_a(x)=e^{-x/2}[\psi(e^x)-a\psi(e^x/a)].
\]

Let

\[
 \boxed{
 \Theta_\zeta
 =\sup_{\zeta(\rho)=0}
 \left(\Re\rho-\frac12\right).}
 \tag{T-15119.2}
\]

The functional equation gives `0<=Theta_zeta<=1/2`, and RH is exactly
`Theta_zeta=0`.

## 2. Exact Laplace transform

For `Re z>1/2`, absolute convergence gives

\[
 \boxed{
 \mathcal LQ_a(z)
 =-\frac{1-\sqrt a\,a^{-z}}{z+1/2}
  {\zeta'\over\zeta}\!\left(z+\frac12\right).}
 \tag{T-15119.3}
\]

The numerator vanishes at `z=1/2`, canceling the shifted pole of zeta. Its other
zeros lie on the same boundary line `Re z=1/2`; it has no zero in

\[
 0<\Re z<1/2.
\]

Therefore every off-critical zeta zero produces an uncancelled pole of
(T-15119.3) at `z=rho-1/2`.

## 3. Weighted-energy abscissa

Define

\[
 \sigma_2(a)
 =\inf\left\{\sigma>0:
 \int_{\log2}^{\infty}
 e^{-2\sigma x}|Q_a(x)|^2dx<\infty
 \right\}.
 \tag{T-15119.4}
\]

Then

\[
 \boxed{
 \sigma_2(a)=\Theta_\zeta.}
 \tag{T-15119.5}
\]

### Lower bound

Suppose the integral in (T-15119.4) is finite for one `sigma`. For every
`u>sigma`, Cauchy–Schwarz makes the unilateral Laplace transform of `Q_a`
analytic on `Re z>sigma`. On the original half-plane `Re z>1/2` it agrees with
(T-15119.3), so uniqueness continues that meromorphic expression throughout
`Re z>sigma`.

An off-critical zero satisfying

\[
 \Re\rho-\frac12>\sigma
\]

would create an uncancelled pole inside that analytic half-plane, a
contradiction. Hence

\[
 \Theta_\zeta\le\sigma_2(a).
\]

### Upper bound

Fix `sigma>Theta_zeta`. The product in (T-15119.3) is analytic on the closed
half-plane `Re z>=sigma`. On a bounded horizontal range it is bounded after the
removable pole at `z=1/2` is filled in. On every fixed vertical strip separated
from the zeta zeros, the logarithmic derivative has polylogarithmic growth,
while

\[
 {1-\sqrt a\,a^{-z}\over z+1/2}=O_{a,\sigma}((1+|\Im z|)^{-1}).
\]

Thus the squared product is integrable in the vertical variable. For large real
part, the absolutely convergent Euler series is uniformly bounded and the
causal transform does not grow. Consequently

\[
 \sup_{u>\sigma}
 \int_{\mathbb R}|\mathcal LQ_a(u+it)|^2dt<\infty.
 \tag{T-15119.6}
\]

The half-plane Paley–Wiener theorem gives a causal `L^2` inverse. On
`Re z>1/2` its Laplace transform agrees with that of the explicitly defined
prime signal, so uniqueness identifies the inverse with
`e^{-sigma x}Q_a(x)`. Hence the weighted energy is finite for every
`sigma>Theta_zeta`, proving the reverse inequality.

Using (L-15145.12), equation (T-15119.5) is equivalently

\[
 \boxed{
 \Theta_\zeta
 =\inf\left\{\sigma>0:
 \int_2^{\infty}t^{-2\sigma}
 |P(t)-P(t/a)|^2dt<\infty
 \right\}.}
 \tag{T-15119.7}
\]

## 4. Exact growth exponent

For a nonnegative locally integrable density, the abscissa of its Mellin/Laplace
integral equals the upper exponential growth exponent of its cumulative mass.
Applying this to (T-15119.7) yields

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{Y\to\infty}
 \frac{\log(1+\mathcal E_a(Y))}{2\log Y}.}
 \tag{T-15119.8}
\]

Indeed, if the limsup is below `sigma`, integration by parts gives convergence
of the `t^(-2sigma)` weighted energy. Conversely, a subsequence on which the
cumulative energy grows faster than `Y^(2sigma)` forces divergence by retaining
the mass below that endpoint.

Therefore, for every fixed `a>1`,

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathcal E_a(Y)=Y^{o(1)}.}
 \tag{T-15119.9}
\]

A bound polynomial in `log Y`—or any estimate `O_epsilon(Y^epsilon)` for every
`epsilon>0`—would be sufficient.

More generally, if for every `epsilon>0`

\[
 \mathcal E_a(Y)
 \ll_\varepsilon Y^{2\theta+\varepsilon},
\]

then zeta has no zero in

\[
 \Re s>\frac12+\theta.
\]

## 5. The full exponent is off diagonal

Use the exact Gram decomposition of `L-15145`:

\[
 \mathcal E_a(Y)=\mathcal D_a(Y)+\mathcal O_a(Y),
\]

where `D_a` is the diagonal and `O_a` contains all distinct-prime-power pairs.
Since

\[
 \mathcal D_a(Y)=O_a((\log Y)^3),
\]

one has

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{Y\to\infty}
 \frac{\log(1+[\mathcal O_a(Y)]_+)}{2\log Y}.}
 \tag{T-15119.10}
\]

Thus the direct global arithmetic theorem is

\[
 \boxed{
 [\mathcal O_a(Y)]_+=Y^{o(1)}.}
 \tag{T-15119.11}
\]

It is a multiplicative scale-coherence statement for the exact prime-power
measure.

## 6. Relation to PR #216

For `a=4`, `L-15145` proves that the compact triangular window of PR #216 is a
finite signed convolution of `W_4`. The compact energy and the present dilation
energy therefore expose the same rightmost-zero exponent through two different
arithmetic coordinates:

```text
compact triangle:
  bounded-ratio prime-pair spline;

causal scale wavelet:
  exact difference psi(t)/t-psi(t/4)/(t/4).
```

The compact profile is preferable for local multiplicative dispersion. The
causal profile is preferable for Selberg recursion, summatory identities, and
exact integer-threshold production. Neither criterion assumes the other, and
both are equivalent to RH through their independently safe transforms.

## 7. Proposed completion route

The scale-four form is

\[
 \boxed{
 \int_2^Y
 \left|
 {\psi(t)\over t}
 -{\psi(t/4)\over t/4}
 \right|^2dt=Y^{o(1)}.}
 \tag{T-15119.12}
\]

This should be attacked by applying the multiplicative difference to Selberg's
exact convolution identity before taking any absolute values. The desired
output is a scale-recursive energy inequality whose feedback coefficient is
strictly below one or tends to zero. Entrywise bounds on the prime-pair Gram are
incompatible with the empirical cancellation and cannot prove the target.

## 8. Proof boundary

Closed here, subject to independent review of the standard analytic interfaces:

- the exact safe transform and prime signal;
- the equality of the weighted-energy abscissa with `Theta_zeta`;
- the cumulative energy exponent;
- the off-diagonal exponent identity;
- a one-parameter family of prime-only RH criteria.

Open:

\[
 \mathcal E_a(Y)=Y^{o(1)}.
\]

This theorem does not prove that estimate and therefore does not prove RH.
