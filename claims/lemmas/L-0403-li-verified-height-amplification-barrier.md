# L-0403 — Verified-height amplification barrier for the Li transform

Claim ID: L-0403  
Title: A zero-height lower bound forces the exponential Li signature to quadratic index scale  
Status: PROPOSED  
Authoring agent: `gpt56-04`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-0340; T-0310 only for the numerical corollary  
Scope: strategic scale barrier for Issue #14  
Related counterexample candidates: negative Li coefficients induced by hypothetical off-line zeros

## Statement

Let `rho=beta+i*gamma` be a nontrivial zero with `0<beta<1/2`, and put

\[
z_\rho=1-\frac1\rho.
\]

If `|gamma|>=T>0`, then

\[
1<|z_\rho|<\exp\left(\frac1{2T^2}\right),
\qquad
|z_\rho|^n<\exp\left(\frac{n}{2T^2}\right).
\]

Therefore, if `A>1` and `|z_rho|^n>=A`, necessarily

\[
n>2T^2\log A.
\]

The reflected right-of-line zero `1-conjugate(rho)` has transformed modulus
`1/|z_rho|`.

### Corollary using the verified height

Assume T-0310: every nontrivial zero with
`0<|gamma|<=3*10^12` lies on the critical line.  Every hypothetical off-line
zero then has `|gamma|>3*10^12`, and its left-side transformed power satisfies

\[
|z_\rho|^n<e
\]

for every

`n <= 18,000,000,000,000,000,000,000,000`.

The X-0401 search through `n=100000` is smaller than this first possible
single-zero `e`-fold amplification scale by a factor `1.8*10^20`.

This is a strategic barrier, not a positivity theorem for Li coefficients.

## Proof

L-0340 gives

\[
|z_\rho|^2-1=\frac{1-2\beta}{|\rho|^2}.
\]

For `0<beta<1/2`, the numerator lies strictly between zero and one, while
`|rho|^2>=gamma^2>=T^2`.  Hence

\[
1<|z_\rho|^2<1+\frac1{T^2}.
\]

Using `log(1+x)<x` for `x>0`,

\[
\log|z_\rho|<\frac12\log\left(1+\frac1{T^2}\right)
<\frac1{2T^2}.
\]

Exponentiation proves the first two bounds.  If `|z_rho|^n>=A`, then
`log A<n/(2T^2)`, proving the index inequality.

For `rho_star=1-conjugate(rho)`, direct algebra gives

\[
z_{\rho_\star}=\frac1{\overline{z_\rho}}.
\]

Under T-0310 take `T=3*10^12`; then

`2*T^2 = 18,000,000,000,000,000,000,000,000`.

For every integer at or below that index the exponent is at most one, while the
preceding inequalities are strict, so the transformed power is strictly below
`e`.

## Motivation

An off-line zero produces an exponentially growing transformed power, but the
first unexcluded zero must be extremely high.  The natural index scale is
quadratic in its height.  Extending a linear scan from `10^5` to `10^6` or
`10^9` does not approach that scale.

Future work should target singularities within radial distance `O(T^-2)` and
angular distance `O(T^-1)` of `z=1`, or develop arithmetic formulas that can
evaluate selected enormous indices without constructing every predecessor.

## Analytic and dependency audit

The generic bound uses only the algebraic identity in L-0340 and the ordinary
real logarithm.  It uses no zero sum, contour, or RH assumption.  T-0310 is used
only for the numerical corollary and has not been independently reproduced in
this repository.

## Gap audit

- This bounds one transformed zero power, not the complete symmetrically ordered
  Li zero sum.
- It does not prove positivity below the displayed scale.
- Many small contributions can interact, and another mechanism could produce a
  negative coefficient.
- A zero closer to the critical line amplifies more slowly, so the estimate is a
  worst-case barrier.

## Adversarial tests

Check the critical-line endpoint, the limit `beta->0`, the reciprocal reflected
transform, and the distinction between an individual modulus bound and an
absolute-convergence claim.

## Remaining uncertainty

No algebraic gap is known.  The strategic interpretation is motivation, not a
finite-index exclusion theorem.

## Suggested next attack

Develop a rigorous Padé, contour, or moment reconstruction capable of resolving
a pole just inside the unit circle near `z=1` against the known on-circle zero
population.
