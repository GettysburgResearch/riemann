# T-9506 — One critical second moment of the analytic totient error is equivalent to RH

Claim ID: `T-9506`  
Title: The endpoint-free quadratic energy already detects every off-line zero  
Status: `PROPOSED — COMPLETE TRANSFER THEOREM; SECOND-MOMENT BOUND OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-9512`; Mellin Cauchy--Schwarz and standard analytic continuation  
Scope: full Riemann Hypothesis  
Related counterexample candidates: none

## Criterion

Let `E^AN` be the analytic summatory-totient error from `L-9512`. Then

\[
\boxed{
\mathrm{RH}
\iff
\int_1^X|E^{\rm AN}(t)|^2dt
=O_\varepsilon(X^{2+\varepsilon})
\quad\text{for every }\varepsilon>0.}
\tag{T-9506.1}
\]

Equivalently, define the endpoint-free positive energy

\[
\boxed{
\mathfrak M(x)
=x^{-5}\int_1^x|E^{\rm AN}(t)|^2dt.}
\tag{T-9506.2}
\]

Then

\[
\boxed{
\mathrm{RH}
\iff
\mathfrak M(x)=O_\varepsilon(x^{-3+\varepsilon}).}
\tag{T-9506.3}
\]

Thus the positive-energy route requires only one quadratic local-to-Bohr
estimate. The endpoint square in `mathfrak A` is useful for the exact pointwise
growth exponent in `T-9504`, but is not logically required to prove RH.

## RH implies the moment bound

Under RH, the classical analytic-part criterion gives, for every `delta>0`,

\[
E^{\rm AN}(t)=O_\delta(t^{1/2+\delta}).
\]

Taking `delta=epsilon/4` and integrating gives

\[
\int_1^X|E^{\rm AN}(t)|^2dt
\ll_\varepsilon
\int_1^X t^{1+\varepsilon/2}dt
\ll_\varepsilon X^{2+\varepsilon}.
\]

## The moment bound implies RH

By `L-9512`, initially for `Re s>2`,

\[
\boxed{
F(s):=
-\frac{\zeta(s-1)}{s(s-1)\zeta(s)}
+\frac{3/\pi^2}{s-2}
=\int_1^\infty E^{\rm AN}(x)x^{-s-1}dx.}
\tag{T-9506.4}
\]

Fix a compact subset of `Re s>1/2` and let its minimum real part be
`sigma>1/2`. Choose `epsilon>0` with

\[
\epsilon<2\sigma-1.
\tag{T-9506.5}
\]

On a dyadic block `[Y,2Y]`, Cauchy--Schwarz and (T-9506.1) give

\[
\begin{aligned}
\int_Y^{2Y}|E^{\rm AN}(x)|x^{-\sigma-1}dx
&\le
\left(\int_Y^{2Y}|E^{\rm AN}(x)|^2dx\right)^{1/2}
\left(\int_Y^{2Y}x^{-2\sigma-2}dx\right)^{1/2}\\
&\ll_\varepsilon
Y^{1+\varepsilon/2}Y^{-\sigma-1/2}\\
&=Y^{-(\sigma-1/2-\varepsilon/2)}.
\end{aligned}
\tag{T-9506.6}
\]

The exponent is strictly negative by (T-9506.5). Summation over dyadic blocks
converges normally on the compact set. Hence the Mellin integral in
(T-9506.4) defines a holomorphic function throughout

\[
\Re s>\frac12.
\tag{T-9506.7}
\]

Every nontrivial zero `rho` with `Re rho>1/2` would give a genuine pole of the
left side of (T-9506.4): `zeta(rho-1)` is nonzero, and the rational factors do
not vanish there. Therefore no such zero exists. Functional-equation symmetry
proves RH.

No pointwise upgrade, Lipschitz argument, high moment, zero simplicity, or
residue estimate is used.

## Exact mean-square exponent

Define

\[
\Theta_2
=\frac12\limsup_{X\to\infty}
\frac{
\log\left(
1+X^{-2}\int_1^X|E^{\rm AN}(t)|^2dt
\right)
}{\log X}.
\tag{T-9506.8}
\]

The same Mellin-abscissa argument, together with the zero-free-half-plane upper
transfer, gives

\[
\boxed{
\Theta_2
=\sup_{\zeta(\rho)=0}\Re\rho-\frac12.}
\tag{T-9506.9}
\]

Equivalently, the best exponent `a` in

\[
\int_1^X|E^{\rm AN}(t)|^2dt
=O_\varepsilon(X^{2+a+\varepsilon})
\]

is exactly

\[
a=2\Theta_\zeta.
\]

For the lower bound, a hypothetical stronger mean-square exponent would make
(T-9506.4) holomorphic to the right of a line crossing a genuine rightmost-zero
pole. The upper bound follows from the corresponding pointwise zero-free-region
estimate for `E^AN`.

## Relation to the Bohr factorization

`L-9513` proves the conjectured `O(D)` square energy for the complete
full-period resonant packet. `T-9506` shows that it is enough to transfer that
quadratic scale to physical intervals of critical length while retaining the
complete tail.

The exact remaining theorem is therefore a second-moment local-to-Bohr estimate,
not an unbounded hierarchy:

\[
\boxed{
\int_X^{2X}|E^{\rm AN}(t)|^2dt
\ll_\varepsilon X^{2+\varepsilon}.}
\tag{T-9506.10}
\]

Higher moments in `T-9505` remain a useful alternative because they recover
pointwise bounds by elementary regularity, but they are stronger than necessary
for the RH implication.

## Proof boundary

- The equivalence is a Mellin/Hardy transfer theorem.
- The critical second-moment estimate (T-9506.10) is not proved here.
- Positivity of the moment does not bound it.
- A full-period Bohr estimate cannot be substituted for the physical dyadic
  moment without a local-to-Bohr theorem.
