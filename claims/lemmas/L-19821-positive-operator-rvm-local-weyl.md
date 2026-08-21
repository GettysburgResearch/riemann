# L-19821 — Positive operator Riemann–von Mangoldt local Weyl theorem

Claim ID: `L-19821`  
Title: One profile-derivative Gram gives the line-centered main density and the Bessel bound needed by the rank-one support sieve  
Status: `PROPOSED — COMPLETE OPERATOR STIELTJES PROOF; PROFILE NORMALIZATION SEPARATE`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: the Riemann--von Mangoldt formula with `S(T)=O(log T)`; elementary operator-valued variation  
Scope: Interface B of `T-19807`

## 1. Setup

Let `H_R` and `K_R` be finite-dimensional Hilbert spaces.  Let

\[
 \Phi_R(u):H_R\to K_R,
 \qquad u\in[a,b],
 \tag{L-19821.1}
\]

be continuously differentiable, where

\[
 0<a<b<\infty
 \tag{L-19821.2}
\]

are fixed independently of `R`.  Assume the profile vanishes at the endpoints;
a fixed smooth partition of unity reduces the general compactly supported case
to this form.

Put

\[
 \boxed{
 D_R={1\over2\pi}
 \int_a^b\Phi_R(u)^*\Phi_R(u)\,du.
 }
 \tag{L-19821.3}
\]

Let `G_R>0`, let `tau_R>0`, and set

\[
 \widehat D_R=D_R+\tau_RG_R.
 \tag{L-19821.4}
\]

Assume the profile, derivative, and logarithmic-moment LMIs

\[
 \boxed{
 {1\over2\pi}\int_a^b
 \Phi_R^*\Phi_R\,du
 \preceq C_0\widehat D_R,
 }
 \tag{L-19821.5}
\]

\[
 \boxed{
 {1\over2\pi}\int_a^b
 (\partial_u\Phi_R)^*(\partial_u\Phi_R)\,du
 \preceq B_R^2\widehat D_R,
 }
 \tag{L-19821.6}
\]

and

\[
 \boxed{
 {1\over2\pi}\int_a^b
 \left|\log{u\over2\pi}\right|
 \Phi_R(u)^*\Phi_R(u)\,du
 \preceq C_{\log}\widehat D_R.
 }
 \tag{L-19821.7}
\]

Equation (L-19821.5) is automatic with `C_0=1` from the definition, but it is
retained to accommodate finite partitions and directed enclosures.

## 2. Line-centered zero matrix

Let the positive ordinates of all nontrivial zeta zeros, counted with
multiplicity and without assuming RH, be

\[
 0<\gamma_1\leq\gamma_2\leq\cdots.
\]

Define the line-centered profile matrix

\[
 \boxed{
 A_R^0={1\over R}
 \sum_{aR\leq\gamma\leq bR}
 \Phi_R(\gamma/R)^*\Phi_R(\gamma/R).
 }
 \tag{L-19821.8}
\]

Every summand is positive semidefinite.  Off-line zeros enter only through their
ordinates and multiplicities; no critical-line assumption occurs in `A_R^0`.

## 3. Theorem

There is a Hermitian logarithmic-density correction

\[
 C_R={1\over2\pi}
 \int_a^b
 \log{u\over2\pi}
 \Phi_R(u)^*\Phi_R(u)\,du
 +c_*D_R
 \tag{L-19821.9}
\]

with a fixed normalization constant `c_*`, such that

\[
 \boxed{
 -\eta_R\widehat D_R
 \preceq
 A_R^0-(\log R)D_R-C_R
 \preceq
 \eta_R\widehat D_R,
 }
 \tag{L-19821.10}
\]

where

\[
 \boxed{
 \eta_R
 \leq
 C{(1+B_R)\log(2R)\over R}.
 }
 \tag{L-19821.11}
\]

Moreover

\[
 \boxed{
 -C\widehat D_R\preceq C_R\preceq C\widehat D_R
 }
 \tag{L-19821.12}
\]

and hence

\[
 \boxed{
 A_R^0\preceq
 [\log R+C+\eta_R]\widehat D_R.
 }
 \tag{L-19821.13}
\]

Equivalently, the unnormalized profile family satisfies the Bessel LMI

\[
 \boxed{
 \sum_{aR\leq\gamma\leq bR}
 \Phi_R(\gamma/R)^*\Phi_R(\gamma/R)
 \preceq
 CR\log R\,\widehat D_R
 }
 \tag{L-19821.14}
\]

for all sufficiently large `R`.

If

\[
 B_R=R^{3/8+o(1)},
 \tag{L-19821.15}
\]

then

\[
 \eta_R=R^{-5/8+o(1)}.
 \tag{L-19821.16}
\]

Thus the line-centered counting remainder is far below the scale needed in
`T-19807`.

## 4. Scalar variation bound

Fix `x in H_R` and put

\[
 F_x(u)=\|\Phi_R(u)x\|^2.
 \tag{L-19821.17}
\]

Then

\[
 |F_x'(u)|
 \leq2\|\Phi_R(u)x\|
       \|\partial_u\Phi_R(u)x\|.
\]

Cauchy--Schwarz and (L-19821.5)--(L-19821.6) give

\[
 \boxed{
 \operatorname{Var}_{[a,b]}F_x
 \leq
 C B_R\langle\widehat D_Rx,x\rangle.
 }
 \tag{L-19821.18}
\]

The endpoint term vanishes under the stated support convention.  With a finite
smooth partition, the endpoint values are charged by the same profile Gram and
only alter the constant.

## 5. Riemann--von Mangoldt Stieltjes decomposition

Write

\[
 N(T)=M(T)+S(T)+E(T),
 \tag{L-19821.19}
\]

where

\[
 M'(T)={1\over2\pi}\log{T\over2\pi}+O(T^{-1}),
 \tag{L-19821.20}
\]

\[
 S(T)=O(\log(2T)),
 \qquad
 E(T)=O(T^{-1}).
 \tag{L-19821.21}
\]

For the scalar quadratic form of (L-19821.8),

\[
 \langle A_R^0x,x\rangle
 ={1\over R}\int_{aR}^{bR}F_x(t/R)\,dN(t).
 \tag{L-19821.22}
\]

The main term gives, after `t=Ru`,

\[
 {1\over R}\int F_x(t/R)\,dM(t)
 =\log R\langle D_Rx,x\rangle
  +\langle C_Rx,x\rangle
  +O(R^{-1})\langle\widehat D_Rx,x\rangle.
 \tag{L-19821.23}
\]

The `S` term is integrated by parts:

\[
 {1\over R}\int_{aR}^{bR}F_x(t/R)\,dS(t)
 =-{1\over R}
 \int_a^bS(Ru)F_x'(u)\,du,
 \tag{L-19821.24}
\]

with the endpoint term absent.  Equations (L-19821.18) and
`S(Ru)=O(log R)` give

\[
 \left|
 {1\over R}\int F_x(t/R)\,dS(t)
 \right|
 \leq
 C{B_R\log R\over R}
 \langle\widehat D_Rx,x\rangle.
 \tag{L-19821.25}
\]

The `E` term and the derivative error in (L-19821.20) are bounded by
`C/R` times the same metric.  This proves the scalar form of
(L-19821.10).  Since it holds for every `x`, the Loewner inequality follows.
Equation (L-19821.12) follows from (L-19821.7), and
(L-19821.13)--(L-19821.14) are immediate. QED.

## 6. Multi-branch and matrix-valued profiles

A fixed finite family of radial, endpoint, parity, or source channels is handled
by replacing `K_R` with their Hilbert direct sum.  The derivative Gram in
(L-19821.6) then contains every branch and every support derivative before the
operator norm is taken.

The theorem is dimension-free except through the proof of the graph LMIs.  In
particular no entrywise summation over a growing source frame is needed.

## 7. Connection to the rank-one support sieve

After whitening by `widehat D_R`, equation (L-19821.14) is exactly the Bessel
hypothesis (L-19818.9) with

\[
 E_R\ll R\log R.
\]

The derivative version required by (L-19818.10) follows by applying the same
argument to the declared support-derivative profile, or by including it as a
separate branch in (L-19821.6).

Thus one positive operator Stieltjes theorem supplies both:

1. the line-centered main lower profile in `T-19807`;
2. the one-sided Bessel energy that prevents squaring the source envelope in
   `L-19818`.

## 8. Endpoint, central, and unbounded profile ranges

The fixed interval `[a,b]` is the clean core theorem.  A production profile may
have:

- a central region near zero;
- finitely many Airy/fold windows;
- an unbounded tail.

These are handled by a finite partition.  The central and tail pieces must carry
explicit logarithmic-moment and derivative-Gram bounds; Airy windows may be
charged by their shrinking measure.  No piece may be dropped merely because it
is small pointwise.

## 9. Proof boundary

- The operator Stieltjes calculation is unconditional and does not assume RH.
- The exact constant in `C_R` depends on the repository's one-sided/two-sided
  zero-count and Fourier normalization.
- Production must verify (L-19821.5)--(L-19821.7) for the complete
  alias-corrected profile of `L-19820`.
- The theorem treats the line-centered positive matrix.  The actual-minus-line
  horizontal/reflected block is handled separately by `L-19818`.
