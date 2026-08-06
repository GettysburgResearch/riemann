# T-15118 — Diagonal weighted prime energy gives a finite RH gate

Claim ID: `T-15118`  
Title: One cofinal sequence of finitely notched prime-power energies tends to zero under RH and diverges under every false-RH rightmost mode  
Status: **PROPOSED PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15143`; `T-15117`  
Scope: diagonal full-problem criterion and finite directed disproof interface

## 1. Weighted energy

Retain the corrected finitely notched prime signal `R_M` of `T-15117`. For
`0<sigma<1/2`, define

\[
 \boxed{
 \mathcal W_M(\sigma)
 =\int_0^\infty e^{-2\sigma x}|R_M(x)|^2\,dx,}
 \tag{T-15118.1}
\]

allowing the value `+infinity`.

For every finite `M`, `R_M` is produced from one compact prime-power window;
only the final integral ranges over the right half-line.

## 2. Exact zero-free abscissa

Every finite notch transform remains nonzero in

\[
 0<\Re z<1/2.
\]

Therefore `L-15143`, applied to the finite window `G_M`, gives

\[
 \boxed{
 \Theta_\zeta
 =\inf\{\sigma>0:\mathcal W_M(\sigma)<\infty\}
 \qquad(M<\infty).}
 \tag{T-15118.2}
\]

Equivalently,

\[
 \boxed{
 \mathcal W_M(\sigma)<\infty
 \Longleftrightarrow
 \zeta(s)\ne0
 \quad(\Re s>1/2+\sigma).}
 \tag{T-15118.3}
\]

Thus a single finite notch family already detects every zero strictly to the
right of its weighted line. Notching critical-line frequencies changes the
finite size of the energy under RH but never its convergence abscissa.

## 3. RH upper bound from the directed notch moat

Let `U_M` be any rigorous RH-valid uniform bound from `T-15117`:

\[
 |R_M(x)|\le U_M
 \qquad(x\ge0).
 \tag{T-15118.4}
\]

Then, under RH,

\[
 \boxed{
 \mathcal W_M(\sigma)
 \le {U_M^2\over2\sigma}.}
 \tag{T-15118.5}
\]

The exact-zero notch sequence has `U_M->0`. The directed zero-ball version can
also be scheduled so that `U_M->0` by increasing the certified set and tightening
the selected balls.

Choose any sequence

\[
 \sigma_j\downarrow0
\]

and finite notch levels `M_j->infinity` satisfying

\[
 \boxed{
 {U_{M_j}^2\over\sigma_j}\longrightarrow0.}
 \tag{T-15118.6}
\]

Then RH implies

\[
 \boxed{
 \mathcal W_{M_j}(\sigma_j)\longrightarrow0.}
 \tag{T-15118.7}
\]

Such a diagonal always exists once the explicit moat sequence `U_M->0` is
available; for example, choose `M_j` so that

\[
 U_{M_j}\le\sigma_j.
\]

## 4. False-RH divergence on every cofinal diagonal

Suppose RH is false, so `Theta_zeta>0`. For every sequence

\[
 \sigma_j\downarrow0
\]

and every sequence of finite notch levels `M_j`, one has

\[
 \sigma_j<\Theta_\zeta
\]

for all sufficiently large `j`. Equation (T-15118.2) then gives

\[
 \boxed{
 \mathcal W_{M_j}(\sigma_j)=+\infty
 \quad\text{for all sufficiently large }j.}
 \tag{T-15118.8}
\]

This conclusion is immune to:

- phase cancellation between rightmost zeros;
- increasingly many critical-line notches;
- arbitrarily small nonzero horizontal displacement;
- sparse large excursions in an unweighted scalar statistic.

The divergence is an analytic convergence failure, not a selected sample sign.

## 5. Diagonal RH criterion

For any source-bound schedule satisfying

\[
 \sigma_j\downarrow0,
 \qquad M_j<\infty,
 \qquad U_{M_j}^2/\sigma_j\to0,
\]

one has the exact dichotomy

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal W_{M_j}(\sigma_j)\longrightarrow0.}
 \tag{T-15118.9}
\]

More weakly,

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal W_{M_j}(\sigma_j)<\infty
 \text{ for infinitely many }j.}
 \tag{T-15118.10}
\]

The forward implication follows from (T-15118.5). The reverse follows because
false RH makes every sufficiently late energy infinite.

## 6. Finite directed disproof certificate

For `X>0`, define the truncated finite energy

\[
 \boxed{
 \mathcal W_{M,X}(\sigma)
 =\int_0^X e^{-2\sigma x}|R_M(x)|^2\,dx.}
 \tag{T-15118.11}
\]

It is monotone in `X` and satisfies

\[
 \mathcal W_{M,X}(\sigma)\le\mathcal W_M(\sigma).
\]

Under RH, (T-15118.5) gives the universal finite upper bound

\[
 \boxed{
 \mathcal W_{M,X}(\sigma)
 \le {U_M^2\over2\sigma}
 \qquad(X>0).}
 \tag{T-15118.12}
\]

Consequently, a source-bound directed calculation proving

\[
 \boxed{
 \inf\mathcal W_{M,X}(\sigma)
 >{U_M^2\over2\sigma}}
 \tag{T-15118.13}
\]

is a finite RH-disproof witness.

Every ingredient is finite:

1. finitely many certified critical-line zero balls and multiplicities;
2. one exact finite notch window;
3. prime powers in the finite union of annuli used for `0<=x<=X`;
4. exact or outward integration of a piecewise-polynomial square;
5. one explicit transform-tail upper bound `U_M`;
6. the rational comparison in (T-15118.13).

No off-line zero, zero ordinate outside the certified line table, or limiting
computation enters the certificate.

## 7. Exact piecewise integration

For the triangular base, `Q_h` is affine between prime-power deposition knots.
After `M` box convolutions, `R_M` is a compact spline of degree `M+1` between
knots translated by subset sums of the notch lengths. Therefore

\[
 e^{-2\sigma x}|R_M(x)|^2
\]

is an exponential times a polynomial on every finite cell. Its integral has an
explicit endpoint recurrence and can be enclosed using rational notch-length
intervals and directed exponential evaluation.

Alternatively, the convolution identity

\[
 R_M=\mathcal A_{r_M}\cdots\mathcal A_{r_1}R_0
\]

permits a source checker to propagate interval splines without expanding all
prime pairs.

## 8. Prime-side positive target

A proof of RH no longer requires the full uniform limit in `T-15117`. It is
enough to prove, directly from the prime construction, that one cofinal schedule
has

\[
 \boxed{
 \mathcal W_{M_j}(\sigma_j)<\infty}
 \tag{T-15118.14}
\]

for infinitely many `j`, or more quantitatively that it tends to zero.

This is the Hardy-space form of the full arithmetic attack:

```text
critical-line notches remove known boundary spectrum;
exponential weighting chooses a shrinking zero-free strip;
finite weighted prime energy decides whether any anti-causal pole remains.
```

## 9. Connection to Hilbert–Poisson energy

`L-19810/L-19811` express right-of-line zeros as an anti-causal Hardy residual
with a universal Poisson energy gap. Equation (T-15118.2) gives the complementary
prime-side statement: the weighted terminal-prime signal belongs to `L2` exactly
when that right-zero packet is absent.

The two energies need not be numerically equal under the present normalizations,
but their finiteness threshold is the same zero-free abscissa. A future exact
intertwiner between them would turn the universal Poisson gap into a direct
prime-side numerical threshold.

## 10. Proof boundary

- The convergence-abscissa identity is inherited from `L-15143` for every finite
  zero-free notch product.
- The upper bound (T-15118.5) is elementary once the RH-valid moat `U_M` is
  certified.
- The theorem does not prove any prime-side energy finite without using an
  RH-valid upper bound; establishing such finiteness cofinally would prove RH.
- The finite witness requires the complete explicit-formula normalization and a
  directed zero-tail moat.
- RH is neither proved nor disproved by this theorem alone.
