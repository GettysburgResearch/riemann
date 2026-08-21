# L-26202 — Positive inverse, digital dual, and Selberg data of the dyadic dipole source

Claim ID: `L-26202`  
Title: The compact carry-dipole source has a positive Dirichlet inverse, positive generalized prime weights, and an exact binary-digit dual  
Status: **PROPOSED EXACT ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: `L-26201`; PR #236 `L-23011/L-23012`; the generalized Selberg coefficient identity  
Scope: source-specific positive algebra; no coercivity or RH conclusion

## 1. Positive inverse

Retain

\[
 \Omega_2(s)
 =
 \frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}.
\tag{L-26202.1}
\]

Its inverse is

\[
 \boxed{
 A_2^\star(s)
 =
 \Omega_2(s)^{-1}
 =
 \frac{\zeta(s)}
 {(1-2^{-s})(1-2^{-s-1})}.}
\tag{L-26202.2}
\]

At every odd prime, the local factor is the ordinary positive geometric
series.  At `2`, with `x=2^(-s)`,

\[
 \frac1{(1-x)^2(1-x/2)}
 =
 \sum_{\nu\ge0}
 \left(2\nu+2^{-\nu}\right)x^\nu.
\tag{L-26202.3}
\]

Consequently the coefficient function is

\[
 \boxed{
 a_2^\star(2^\nu m)
 =
 2\nu+2^{-\nu}
 \qquad(m\ {\rm odd}),}
\tag{L-26202.4}
\]

and

\[
 a_2^\star(n)>0
\tag{L-26202.5}
\]

for every positive integer.  Coefficientwise,

\[
 \boxed{
 a_2^\star*\omega_2=\varepsilon.}
\tag{L-26202.6}
\]

The generic Brion mechanism tried to manufacture a numerator factor on every
line direction.  Here the complete inverse and every sign are explicit at one
Euler prime.

## 2. Positive generalized von Mangoldt sequence

Define

\[
 -\frac{(A_2^\star)'}{A_2^\star}(s)
 =
 \sum_{n\ge1}\frac{\Lambda_2^\star(n)}{n^s}.
\tag{L-26202.7}
\]

At odd prime powers,

\[
 \Lambda_2^\star(p^k)=\log p.
\tag{L-26202.8}
\]

At powers of two,

\[
 \boxed{
 \Lambda_2^\star(2^k)
 =
 \left(2+2^{-k}\right)\log2.}
\tag{L-26202.9}
\]

Thus

\[
 \Lambda_2^\star(n)\ge0.
\tag{L-26202.10}
\]

The generalized Selberg identity therefore reads

\[
 \boxed{
 \omega_2*(a_2^\star\log^2)
 =
 \Lambda_2^\star\log
 +\Lambda_2^\star*\Lambda_2^\star,}
\tag{L-26202.11}
\]

and every coefficient on the right is nonnegative.

This coefficient positivity does not control the critical inverse by itself.
It does supply the correct positive forcing for the reflected two-frequency
identity of PR #241.

## 3. Exact binary-digit dual

Let

\[
 c_2(n)=1-v_2(n).
\tag{L-26202.12}
\]

PR #236 proves

\[
 \sum_{n\le N}c_2(n)=s_2(N)\ge0,
\tag{L-26202.13}
\]

where `s_2(N)` is the binary digit sum.  Its Dirichlet series is

\[
 C_2(s)
 =
 \zeta(s)\frac{1-2^{1-s}}{1-2^{-s}}.
\tag{L-26202.14}
\]

Multiplication by (L-26202.1) gives a finite polynomial:

\[
 \boxed{
 C_2(s)\Omega_2(s)
 =
 (1-2^{1-s})(1-2^{-s-1})
 =
 1-\frac52\,2^{-s}+4^{-s}.}
\tag{L-26202.15}
\]

Equivalently,

\[
 \boxed{
 c_2*\omega_2
 =
 \varepsilon-\frac52\delta_2+\delta_4.}
\tag{L-26202.16}
\]

This is an exact finite digital recurrence.  It is stronger than a
polylogarithmic partial-sum estimate: the complete odd Möbius source and all
four opposite-parity layers collapse to three atoms after convolution by the
binary-digit dual.

## 4. Additive-logarithmic form

Put

\[
 \kappa_2
 =
 \sum_{n\ge1}\frac{c_2(n)}{\sqrt n}\delta_{\log n},
 \qquad
 \beta_2^\star
 =
 \sum_{n\ge1}\frac{\omega_2(n)}{\sqrt n}\delta_{\log n}.
\tag{L-26202.17}
\]

Then (L-26202.16) becomes

\[
 \boxed{
 \kappa_2*\beta_2^\star
 =
 \delta_0
 -\frac{5}{2\sqrt2}\delta_{\log2}
 +\frac12\delta_{2\log2}.}
\tag{L-26202.18}
\]

Let

\[
 S_2(t)=e^{-t/2}s_2(\lfloor e^t\rfloor)\ge0.
\tag{L-26202.19}
\]

The exact distributional identity from PR #236 is

\[
 \left(\partial_t+\frac12\right)S_2=\kappa_2.
\tag{L-26202.20}
\]

Writing

\[
 w_\infty(t)=e^{-t/2}{\bf1}_{t\ge0},
\tag{L-26202.21}
\]

the unique causal solution of (L-26202.18)--(L-26202.20) is

\[
 \boxed{
 S_2*\beta_2^\star
 =
 w_\infty
 -\frac{5}{2\sqrt2}\tau_{\log2}w_\infty
 +\frac12\tau_{2\log2}w_\infty.}
\tag{L-26202.22}
\]

The right side is elementary, finite, and exponentially decaying.

## 5. Three exact faces of one source

The coefficient `omega_2` simultaneously has:

1. **carry face**
   \[
   \omega_2\mapsto\Gamma_2(n,m),
   \]
   the compact sign dipole of `L-26201`;

2. **digital face**
   \[
   c_2*\omega_2
   =
   \varepsilon-\frac52\delta_2+\delta_4;
   \]

3. **Selberg face**
   \[
   \omega_2*(a_2^\star\log^2)
   =
   \Lambda_2^\star\log
   +\Lambda_2^\star*\Lambda_2^\star
   \quad\text{with a nonnegative right side.}
   \]

This is the source-specific recombination absent from the generic bounded-rank
and automatic-line proposals.  Any proposed cancellation must be verified
simultaneously in all three faces.

## 6. Correct reflected consumer

The diagonal reflected identity alone is a global weighted Hardy norm.  For a
physical logarithmic block, the correct consumer is PR #241 `L-9518`, with
independent frequencies `t,s` and the block kernel

\[
 \Phi_{J,\alpha}(t-s).
\]

Insert `A_2^\star`, `omega_2`, and `Lambda_2^\star` into that exact
two-frequency identity before splitting the inner and outer carry bands.
Every cross term between the four parity layers must remain in the coupled
normal Gram.

A scalar positive Selberg identity or a rowwise estimate is not sufficient.

## 7. Proof boundary

Closed exactly:

- positive inverse coefficients;
- positive generalized prime weights;
- coefficientwise Selberg forcing;
- the finite binary-digit convolution;
- the additive three-tap output;
- the identification of the correct two-frequency consumer.

Open:

- a critical lower or upper bound for convolution by `S_2` on the actual
  source;
- a reflected reserve comparing the two carry-dipole bands;
- the defect-to-slack transport theorem;
- RH.
