# L-19865 — Regularized profile estimates imply affine one-sided Weil coercivity

Claim ID: `L-19865`  
Status: **PROVED ABSTRACT OPERATOR ADAPTER — HYBRID SOURCE PROFILE GATES REQUIRE REVIEW**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-07  
Dependencies: positive operator Riemann--von Mangoldt theorem `L-19821`; rank-one support large sieve `L-19818`; exact residual factorization  
Scope: converts profile estimates into the noncircular affine hypothesis of `L-19861`

## 1. Setup

Let `V_R` be a finite Hilbert space with ordinary Gram `H_R=I` after
whitening. Let

\[
 D_R\succeq0
 \tag{L-19865.1}
\]

be the ordinary Gram of the **complete exact residual** attached to the finite
vectors, and let `A_R` be their exact localized Weil matrix.

Let `A_R^0` be the line-centered positive zero comparator obtained by replacing
every centered zero parameter `gamma+i delta` by its ordinate `gamma`, retaining
multiplicity. Choose `tau_R>0` and put

\[
 \widehat D_R=D_R+\tau_RI.
 \tag{L-19865.2}
\]

## 2. Line-centered gate

Assume the complete residual profile satisfies the profile, derivative, and
logarithmic-moment LMIs of `L-19821`. Then there are `a_R>0`, a Hermitian bounded
density correction `C_R`, and an error `alpha_R>=0` such that

\[
 A_R^0=a_RD_R+C_R+E_R^0,
 \tag{L-19865.3}
\]

\[
 -c_0\widehat D_R\preceq C_R\preceq c_0\widehat D_R,
 \tag{L-19865.4}
\]

and

\[
 -\alpha_R\widehat D_R
 \preceq E_R^0\preceq
 \alpha_R\widehat D_R.
 \tag{L-19865.5}
\]

In the standard radial normalization,

\[
 a_R=\log R+O(1),
 \qquad
 \alpha_R=o(\log R).
 \tag{L-19865.6}
\]

Equations (L-19865.3)--(L-19865.5) immediately give the one-sided bound

\[
 A_R^0
 \succeq
 (a_R-c_0-\alpha_R)D_R
 -(c_0+\alpha_R)\tau_RI.
 \tag{L-19865.7}
\]

## 3. Actual-minus-line gate

Assume the complete reflected/off-line block obeys

\[
 \boxed{
 -\delta_R\widehat D_R
 \preceq A_R-A_R^0
 \preceq\delta_R\widehat D_R,}
 \tag{L-19865.8}
\]

where

\[
 \delta_R=o(\log R).
 \tag{L-19865.9}
\]

The rank-one Bessel support large sieve `L-19818` supplies (L-19865.8) on a
positive-measure set of supports once the complete two-end profile satisfies:

```text
one pointwise graph envelope;
one positive Bessel sum for the other factor;
the correctly scaled support derivative;
Bessel endpoint and stationary-alias ledgers;
collective endpoint summation.
```

The corrected `k>R` range is `L-19863`; the geometric periodization fold is
`L-19864`.

## 4. Exact affine lower bound

Define

\[
 c_R=a_R-c_0-\alpha_R-\delta_R
 \tag{L-19865.10}
\]

and

\[
 \sigma_R=-(c_0+\alpha_R+\delta_R)\tau_R.
 \tag{L-19865.11}
\]

For all sufficiently large `R`, `c_R>0`, and

\[
 \boxed{
 A_R-\sigma_RI\succeq c_RD_R.}
 \tag{L-19865.12}
\]

This is the exact affine one-sided hypothesis of `L-19861`. It does not assert
`A_R>=0`; indeed `sigma_R` is generally negative.

### Proof

Add the lower sides of (L-19865.7) and (L-19865.8), separate the coefficients of
`D_R` and `tau_RI`, and use (L-19865.10)--(L-19865.11). QED.

## 5. Target-only upper bound

Let `p_R` be a unit target and put

\[
 m_R=D_R(p_R,p_R).
 \tag{L-19865.13}
\]

The upper sides of (L-19865.3)--(L-19865.5) and (L-19865.8) give

\[
 \begin{aligned}
 A_R(p_R,p_R)-\sigma_R
 \le{}&[a_R+c_0+\alpha_R+\delta_R]m_R\\
 &+2(c_0+\alpha_R+\delta_R)\tau_R.
 \end{aligned}
 \tag{L-19865.14}
\]

Choose

\[
 \boxed{\tau_R=m_R.}
 \tag{L-19865.15}
\]

Then

\[
 \boxed{
 A_R(p_R,p_R)-\sigma_R
 \le C_R^{\rm tar}c_Rm_R,}
 \tag{L-19865.16}
\]

where `C_R^tar` remains bounded if
`alpha_R+delta_R=o(a_R)` and in any case is `R^(o(1))` under the declared
profile budgets.

For the hybrid residual theorem `L-19862`,

\[
 m_R\le e^{-B L_R}
 \tag{L-19865.17}
\]

with arbitrarily large fixed `B`, while

\[
 \theta_2(D_R)\ge1.
 \tag{L-19865.18}
\]

Therefore

\[
 {C_R^{\rm tar}m_R\over\theta_2(D_R)}\longrightarrow0.
 \tag{L-19865.19}
\]

`L-19861` then gives a simple isolated even ground line and an exponentially
small ordinary target angle.

## 6. Why the shift is load bearing

If `tau_R` were deleted before the profile estimates were proved, the lower
bound would read `A_R>=c_RD_R>=0` and would already establish cofinal Weil
positivity on a dense diagonal. The small regularizing metric keeps every
profile operation well typed and converts its loss into the scalar shift
`sigma_R`.

The target pays only

\[
 |\sigma_R|=R^{o(1)}m_R,
\]

which is negligible because its exact residual energy is exponentially small.
Thus the shift removes circularity without damaging ground-state selection.

## 7. Source-specific production interface

For the exterior-cardinal hybrid reservoir of `L-19862`, a proof certificate for
(L-19865.3)--(L-19865.9) must contain:

1. the exact global-minus-finite residual transform for every source column;
2. a finite branch partition of its two-end phases;
3. positive line-centered profile, derivative, and logarithmic-moment Grams;
4. Bessel and support-derivative sums in the same `D_R+tau_RI` metric;
5. the Bessel endpoint ledger, including the corrected `k>R` aggregate;
6. the independent geometric fold ledger;
7. a support-average certificate for every oscillatory actual-minus-line branch;
8. a proof that all phase-neutral off-line terms are retained in the main or
   scalar correction, not discarded.

The smooth cardinal frame gives dimension `R^(o(1))` and graph envelope
`R^(1/4+o(1))`; `L-19818` then has a strict power reserve. These source-specific
bounds are a concrete analytic theorem, not implied by the abstract algebra.

## 8. Proof boundary

- Sections 1--6 are exact operator algebra.
- `L-19821` and `L-19818` prove the abstract analytic mechanisms.
- Independent review must still reconstruct the complete hybrid residual
  profile and verify every LMI in Section 7 in the exact finite CCM
  normalization.
- This is now the only indefinite-form input in the affine hybrid route.