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

Assume the complete residual profile satisfies a positive operator
Riemann--von Mangoldt decomposition

\[
 A_R^0=a_RD_R+C_R+E_R^0,
 \tag{L-19865.3}
\]

with `a_R>0`,

\[
 -c_{0,R}\widehat D_R
 \preceq C_R\preceq
 c_{0,R}\widehat D_R,
 \tag{L-19865.4}
\]

and

\[
 -\alpha_R\widehat D_R
 \preceq E_R^0\preceq
 \alpha_R\widehat D_R.
 \tag{L-19865.5}
\]

For a profile localized to ordinates comparable with one radial scale, the
standard theorem gives

\[
 a_R=\log R+O(1).
 \tag{L-19865.6}
\]

For the hybrid multi-scale residual of `L-19862`, no universal formula such as
(L-19865.6) is assumed: `a_R`, `c_(0,R)`, and `alpha_R` must be certified for
the complete profile and its actual frequency partition.

Equations (L-19865.3)--(L-19865.5) give

\[
 A_R^0
 \succeq
 (a_R-c_{0,R}-\alpha_R)D_R
 -(c_{0,R}+\alpha_R)\tau_RI.
 \tag{L-19865.7}
\]

## 3. Actual-minus-line gate, including central ordinates

Assume the complete reflected/off-line block obeys

\[
 \boxed{
 -\delta_R\widehat D_R
 \preceq A_R-A_R^0
 \preceq\delta_R\widehat D_R.}
 \tag{L-19865.8}
\]

The number `delta_R` must cover **all** ordinate ranges.

The rank-one Bessel support large sieve `L-19818` supplies the oscillatory part
of (L-19865.8) for zero ordinates comparable with the support/radial scale once
the complete two-end profile satisfies:

```text
one pointwise graph envelope;
one positive Bessel sum for the other factor;
the correctly scaled support derivative;
Bessel endpoint and stationary-alias ledgers;
collective endpoint summation.
```

It does not control a fixed or central ordinate block whose phase derivative is
not on that dyadic scale. Such a block must be retained as an exact finite
Hermitian matrix and certified inside (L-19865.8), or absorbed into an additional
scalar shift with a separate target-line upper certificate. A hypothetical low
off-line zero may not be silently placed in the high-frequency large-sieve
remainder.

The corrected `k>R` range is `L-19863`; the geometric periodization fold is
`L-19864`.

## 4. Exact affine lower bound

Define

\[
 c_R=a_R-c_{0,R}-\alpha_R-\delta_R
 \tag{L-19865.9}
\]

and

\[
 \sigma_R=-(c_{0,R}+\alpha_R+\delta_R)\tau_R.
 \tag{L-19865.10}
\]

Whenever

\[
 \boxed{c_R>0,}
 \tag{L-19865.11}
\]

one has

\[
 \boxed{
 A_R-\sigma_RI\succeq c_RD_R.}
 \tag{L-19865.12}
\]

This is the exact affine one-sided hypothesis of `L-19861`. It does not assert
`A_R>=0`; `sigma_R` is generally negative.

### Proof

Add the lower sides of (L-19865.7) and (L-19865.8), separate the coefficients of
`D_R` and `tau_RI`, and use (L-19865.9)--(L-19865.10). QED.

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
 \le{}&[a_R+c_{0,R}+\alpha_R+\delta_R]m_R\\
 &+2(c_{0,R}+\alpha_R+\delta_R)\tau_R.
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

where one may take

\[
 C_R^{\rm tar}
 ={a_R+3(c_{0,R}+\alpha_R+\delta_R)\over c_R}.
 \tag{L-19865.17}
\]

For the hybrid residual theorem `L-19862`,

\[
 m_R\le e^{-B L_R}
 \tag{L-19865.18}
\]

with arbitrarily large fixed `B`, while

\[
 \theta_2(D_R)\ge1.
 \tag{L-19865.19}
\]

The exact closing rate is therefore

\[
 \boxed{C_R^{\rm tar}m_R\longrightarrow0.}
 \tag{L-19865.20}
\]

No particular asymptotic for `a_R` or `delta_R` is needed beyond
(L-19865.11) and (L-19865.20).

## 6. Why the shift is load bearing

If `tau_R` were deleted before the profile estimates were proved, the lower
bound would read `A_R>=c_RD_R>=0` and would already establish cofinal Weil
positivity on a dense diagonal. The small regularizing metric keeps every
profile operation well typed and converts its loss into the scalar shift
`sigma_R`.

The target pays

\[
 |\sigma_R|
 =(c_{0,R}+\alpha_R+\delta_R)m_R,
\]

which is negligible whenever (L-19865.20) holds. Thus the shift removes
circularity without damaging ground-state selection.

## 7. Source-specific production interface

For the exterior-cardinal hybrid reservoir of `L-19862`, a proof certificate for
(L-19865.3)--(L-19865.8) must contain:

1. the exact global-minus-finite residual transform for every source column;
2. a complete frequency partition, including bounded and central ordinates;
3. positive line-centered profile, derivative, and logarithmic-moment Grams on
   every high-frequency branch;
4. an exact finite matrix enclosure for every central ordinate block not covered
   by support averaging;
5. Bessel and support-derivative sums in the same `D_R+tau_RI` metric;
6. the Bessel endpoint ledger, including the corrected `k>R` aggregate;
7. the independent geometric fold ledger;
8. a support-average certificate for every eligible oscillatory
   actual-minus-line branch;
9. a proof that all phase-neutral off-line terms are retained in the main,
   central, or scalar correction, not discarded;
10. the strict inequalities `c_R>0` and `C_R^tar m_R->0`.

The smooth cardinal frame gives dimension `R^(o(1))` and a controlled graph
envelope on the high-frequency branches; `L-19818` then has a power reserve
there. The bounded-ordinate block remains an explicit finite affine gate rather
than an inferred large-sieve consequence.

## 8. Proof boundary

- Sections 1--6 are exact operator algebra.
- `L-19821` and `L-19818` prove the abstract high-frequency mechanisms.
- Independent review must reconstruct the complete hybrid residual profile,
  central block, and every LMI in Section 7 in the exact finite CCM
  normalization.
- This is the only indefinite-form input in the affine hybrid route.