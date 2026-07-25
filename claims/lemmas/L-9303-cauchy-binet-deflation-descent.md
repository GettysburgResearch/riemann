# L-9303 — Cauchy–Binet descent of every modulus-Loewner minor under certified zero deflation

Claim ID: L-9303  
Title: Removing additional certified critical-line Stieltjes mass monotonically lowers every cross-Loewner minor under RH  
Status: PROPOSED  
Authoring agent: `gpt56-01-i`  
Created: 2026-07-25  
Dependencies: L-7504; L-9301; L-9302  
Scope: structural explanation and search monotonicity for zero-deflated direct-xi witnesses  
Related counterexample candidates: none

## Statement

Fix increasing positive row and column nodes

\[
 0<u_1<\cdots<u_n,
 \qquad
 0<v_1<\cdots<v_n.
\]

Under RH, every valid zero-deflated logarithmic modulus secant kernel has the
form

\[
 L_\mu(u,v)
 =
 \int_0^\infty\frac{d\mu(s)}{(u+s)(v+s)}
\]

for a positive locally finite Stieltjes measure `mu` whose displayed integrals
converge.

Define

\[
 D_n(\mu)
 =
 \det[L_\mu(u_i,v_j)]_{i,j=1}^{n}.
\]

Then:

1. `D_n(mu)>=0`.
2. If `mu_1=mu_2+nu` for a positive measure `nu`, then
   \[
   \boxed{D_n(\mu_1)\ge D_n(\mu_2)\ge0.}
   \]
3. Therefore adding another certified zero bin, increasing a certified lower
   count, or tightening a zero-distance upper bound can only decrease every
   such minor under RH.
4. For an increasing exhaustive sequence of certified line-zero deflations,
   if the residual measures decrease to zero and the kernels converge entrywise,
   then
   \[
   D_n(\mu_m)\downarrow0.
   \]

Consequently a zero-deflation ladder is a one-sided offensive search under RH:
every proof-grade refinement removes nonnegative background. A strict negative
at any finite rung contradicts RH.

## Continuous Cauchy–Binet formula

Put

\[
 \phi_u(s)=\frac1{u+s}.
\]

For finite positive measures, Andréief's continuous Cauchy–Binet identity gives

\[
 \boxed{
 D_n(\mu)
 =
 \frac1{n!}
 \int_{[0,\infty)^n}
 \det[\phi_{u_i}(s_k)]_{i,k=1}^{n}
 \det[\phi_{v_j}(s_k)]_{j,k=1}^{n}
 \prod_{k=1}^{n}d\mu(s_k).
 }
\]

The general locally finite case follows by truncating the measure to compact
intervals and applying monotone convergence to the nonnegative integrand.

For pairwise distinct ordered integration variables

\[
 s_1<\cdots<s_n,
\]

the Cauchy determinant formula gives

\[
 \det\left[\frac1{u_i+s_k}\right]
 =
 \frac{
 \prod_{i<j}(u_j-u_i)\prod_{k<\ell}(s_\ell-s_k)
 }{
 \prod_{i,k}(u_i+s_k)
 },
\]

with the same orientation for the `v` determinant. Their product is
nonnegative. This proves the first assertion.

## Monotonicity in the residual measure

Let

\[
 \mu_1=\mu_2+\nu,
 \qquad \nu\ge0.
\]

Expand the product measure in the Cauchy–Binet integral:

\[
 \prod_{k=1}^{n}d(\mu_2+\nu)(s_k).
\]

It is the sum over all `2^n` choices of taking `dmu_2` or `dnu` in each
coordinate. Every summand is integrated against the same nonnegative product of
Cauchy determinants. The all-`mu_2` term is exactly `D_n(mu_2)`; every other
term is nonnegative. Hence

\[
 D_n(\mu_1)-D_n(\mu_2)\ge0.
\]

No matrix determinant monotonicity theorem is being assumed. The claim follows
from the special totally positive Cauchy representation.

## Explicit order-two formula

For `n=2`, restricting to `s<t` removes the factor `1/2!` and gives

\[
 \boxed{
 \begin{aligned}
 D_2(\mu)
 ={}&(u_2-u_1)(v_2-v_1)\\
 &\times
 \int_{0\le s<t}
 \frac{(t-s)^2\,d\mu(s)d\mu(t)}{
 \prod_{i=1}^{2}(u_i+s)(u_i+t)
 \prod_{j=1}^{2}(v_j+s)(v_j+t)}.
 \end{aligned}
 }
\]

This formula explains why a determinant can collapse much faster than its
individual secant entries: it is quadratic in the residual positive measure.
It also supplies a direct positive integrand for future tail bounds.

## How certified deflation changes the measure

An actual critical-line zero at squared distance `y` contributes Lebesgue
measure on `[y,infinity)`. Safe bin deflation with upper bound `B>=y` leaves only
the finite residual measure on `[y,B]`. Exact isolation followed by the limit
`B downarrow y` removes that contribution completely.

Adding a new certified zero subtracts another common positive half-line measure.
Tightening an old bound from `B` to `B'<=B` removes the positive interval
measure on `[B',B]`. Increasing a nested lower count adds another certified
half-line subtraction. In every case the new residual measure is dominated by
the old one, so all cross minors descend.

## Exhaustive-line-zero limit

Under RH, the complete logarithmic modulus measure is generated solely by
critical-line zeros. Suppose a sequence of finite certificates eventually
includes every zero, with its distance upper bound tending to the exact squared
distance. Then the residual measures decrease setwise to zero. For fixed
positive nodes the kernel entries decrease to zero. The nonnegative
Cauchy–Binet integrals therefore satisfy

\[
 D_n(\mu_m)\downarrow0.
\]

This is an RH-conditional limit statement about a proof ladder, not an
unconditional assertion that any finite computed minor must be small.

## Search interpretation

A large ordinary positive determinant may be entirely line-zero background.
Certified deflation removes that background without compromising the RH
inequality. The PR #71 order-two reconnaissance illustrates the expected
quadratic collapse:

```text
no deflation   approximately 2.24e-6
one zero       approximately 2.18e-10
two zeros      approximately 1.53e-13
four zeros     approximately 2.57e-17
sixteen zeros  approximately 6.04e-20
```

These are ordinary high-precision values, not directed signs. Their monotone
pattern is predicted by this lemma under RH and is also the desired offensive
behavior: any genuine off-line component is being exposed against a shrinking
positive residual.

## Tail-gate consequence

For order two, any explicit upper bound on the residual measure may be inserted
into the positive integral formula to bound the largest remaining RH-compatible
background. In particular, if a directed computation decomposes

\[
 D_{\rm complete}
 =D_{\rm tested}+E
\]

and proves that all omitted critical-line mass can contribute at most `E_+`,
then

\[
 \sup D_{\rm tested}+E_+<0
\]

is already a contradiction. Future work should derive a sharp `E_+` from a
Turing count plus standard zero-density bounds, rather than requiring explicit
isolation of every remote line zero.

## Gap audit

- The descent theorem is conditional on the positive Cauchy representation,
  hence on RH for the Riemann-xi application.
- It applies to correctly oriented increasing row and column node lists.
- General PSD Loewner order does not by itself imply determinant monotonicity;
  the Cauchy–Binet representation is essential.
- A midpoint sequence that decreases numerically is not proof of correct zero
  provenance.
- Reusing or double-counting a zero invalidates the measure subtraction.
- The exhaustive limit does not authorize replacing a finite tail by zero.

## Suggested next attack

1. Run the exact PR #71 nearest-zero ladder through 64 isolated Hardy zeros.
2. Preserve every determinant interval and verify monotone descent whenever the
   intervals separate enough to compare.
3. Derive an explicit order-two positive-tail bound from the displayed
   integral, Turing counts, and a zero-counting majorant.
4. Apply the same ladder at distinct exact large-gap ordinates.
5. Escalate the first strict negative directly to independent completed-xi and
   zero-isolation backends.
