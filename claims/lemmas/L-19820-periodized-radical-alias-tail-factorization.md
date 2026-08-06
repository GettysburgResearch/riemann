# L-19820 — Periodized radical and alias-corrected tail factorization

Claim ID: `L-19820`  
Title: A finite periodized arithmetic source vector is the global radical minus one alias-and-projection corrected tail  
Status: `PROPOSED — COMPLETE ABSTRACT FORM IDENTITY; PRODUCTION DOMAIN/CONVERGENCE ADAPTER SEPARATE`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: exact global `E`-range radicality; convergence of multiplicative periodization; the finite CCM Fourier projection  
Scope: exact bridge between `P_N Sigma E` source frames and localized finite Weil matrices

## 1. The missing distinction

Two source maps occur in the positive stack.

1. The global arithmetic vector
   \[
   r=E(f),
   \]
   which lies in the radical of the global Weil form.
2. The periodized finite vector
   \[
   P_N\Sigma_Lr,
   \]
   which is used to span a finite CCM Fourier space.

The periodized vector is not the sharp restriction `P_Lr`.  Therefore the
ordinary exterior-tail identity does not apply to it without modification.

The correct modification is exact: fold the exterior tail back into the
fundamental interval and include the discarded high Fourier modes.  The finite
periodized vector is the global radical minus that single corrected tail.

## 2. Abstract setup

Let `H` be a Hilbert space of functions on the real logarithmic line and let
`Q` be a Hermitian form on an admissible linear domain.  Let

\[
 J:S\longrightarrow\operatorname{Dom}Q
 \tag{L-19820.1}
\]

be a source map whose range is radical:

\[
 \boxed{
 Q(Js,h)=0
 \qquad(s\in S,\ h\in\operatorname{Dom}Q).
 }
 \tag{L-19820.2}
\]

Fix a length `L>0` and the fundamental interval

\[
 I_L=[-L/2,L/2].
 \]

Let `P_L` be multiplication by its characteristic function and let

\[
 \iota_L:L^2(I_L)\to H
 \]

be extension by zero.

For an exterior vector `t=(I-P_L)r`, define its folded alias on `I_L` by

\[
 \boxed{
 (\mathfrak F_Lt)(x)
 =\sum_{m\in\mathbb Z\setminus\{0\}}t(x+mL),
 \qquad x\in I_L,
 }
 \tag{L-19820.3}
\]

whenever the sum converges in the declared form/graph topology.

The full periodization restricted to the fundamental interval is

\[
 \Sigma_Lr=P_Lr+\mathfrak F_L(I-P_L)r.
 \tag{L-19820.4}
\]

## 3. Full periodization identity

For `r=Js`, put

\[
 t_s=(I-P_L)Js
 \tag{L-19820.5}
\]

and define the alias-corrected tail

\[
 \boxed{
 w_s=t_s-\iota_L\mathfrak F_Lt_s.
 }
 \tag{L-19820.6}
\]

Then, as global functions,

\[
 \boxed{
 \iota_L\Sigma_LJs=Js-w_s.
 }
 \tag{L-19820.7}
\]

Indeed

\[
 Js-w_s=P_LJs+\iota_L\mathfrak F_Lt_s.
\]

By radicality, for all source coefficients `s,t`,

\[
 \boxed{
 Q(\iota_L\Sigma_LJs,
   \iota_L\Sigma_LJt)
 =Q(w_s,w_t).
 }
 \tag{L-19820.8}
\]

### Proof

Expand

\[
 Q(Js-w_s,Jt-w_t).
\]

Every term containing `Js` or `Jt` vanishes by (L-19820.2) and Hermitian
symmetry.  The remaining term is `Q(w_s,w_t)`. QED.

Thus periodization does not destroy the radical-tail mechanism; it replaces the
ordinary exterior tail by the exterior tail minus its complete fold.

## 4. Finite Fourier projection

Let

\[
 \Pi_N:L^2(I_L)\to E_N(L)
 \tag{L-19820.9}
\]

be the ordinary finite Fourier projection.  Put

\[
 y_s=\Pi_N\Sigma_LJs,
 \qquad
 e_s=(I-\Pi_N)\Sigma_LJs.
 \tag{L-19820.10}
\]

Define the complete finite corrected tail

\[
 \boxed{
 W_{L,N}s
 =t_s-\iota_L\mathfrak F_Lt_s+\iota_Le_s.
 }
 \tag{L-19820.11}
\]

Then

\[
 \boxed{
 \iota_Ly_s=Js-W_{L,N}s.
 }
 \tag{L-19820.12}
\]

Consequently

\[
 \boxed{
 Q(\iota_Ly_s,\iota_Ly_t)
 =Q(W_{L,N}s,W_{L,N}t).
 }
 \tag{L-19820.13}
\]

In operator notation, the exact finite source matrix is

\[
 \boxed{
 A_{L,N}=W_{L,N}^*QW_{L,N}.
 }
 \tag{L-19820.14}
\]

No approximate-radical remainder is present.

## 5. Exact source-frame version

Suppose a finite source map

\[
 F_{L,N}:E_N(L)\to S
 \tag{L-19820.15}
\]

is a right inverse for the projected periodized map:

\[
 \boxed{
 \Pi_N\Sigma_LJF_{L,N}=I_{E_N(L)}.
 }
 \tag{L-19820.16}
\]

Define

\[
 \mathcal W_{L,N}=W_{L,N}F_{L,N}.
 \tag{L-19820.17}
\]

Then the entire finite Weil matrix on `E_N(L)` has the exact factorization

\[
 \boxed{
 A_{L,N}=\mathcal W_{L,N}^*Q\mathcal W_{L,N}.
 }
 \tag{L-19820.18}
\]

The natural positive profile Gram is therefore

\[
 \boxed{
 D_{L,N}=\mathcal W_{L,N}^*\mathcal W_{L,N}.
 }
 \tag{L-19820.19}
\]

It is the Gram of the **complete alias-corrected tail**, not merely the ordinary
exterior tail.

## 6. Components of the corrected tail

Equation (L-19820.11) keeps three terms correlated:

```text
ordinary exterior tail;
minus every folded Poisson alias;
plus the discarded high Fourier part of the periodization.
```

A proof may expand these terms into endpoint polylogarithms, Poisson aliases,
radial branches, and Fourier truncation remainders.  Such an expansion is a
computational ledger for one exact vector `W_(L,N)s`; it is not a license to
replace its Gram by the sum of separate absolute-value budgets.

This explains the role of the complete alias moat in the PR #164 source stack.
It also identifies the exact object that must be used in a line-centered
local-Weyl scalarization.

## 7. Cross identities

The same algebra gives, for every admissible test `h`,

\[
 \boxed{
 Q(\iota_Ly_s,h)=-Q(W_{L,N}s,h).
 }
 \tag{L-19820.20}
\]

Taking `h=\iota_Ly_t` gives (L-19820.13).  Taking `h=W_(L,N)t` gives the
corresponding finite-source/corrected-tail cross matrix.

Thus every residual and every finite block may be computed from the same
corrected-tail profile.

## 8. Relationship to the whole-matrix route

`L-19819` gives an exact right inverse (L-19820.16) on a rapidly growing Fourier
space.  The present lemma closes the abstract part of Interface A in `T-19807`:

\[
 \text{periodized source frame}
 \quad\Longrightarrow\quad
 \text{exact complete corrected-tail Weil matrix}.
\]

The remaining work is normalization and analytic production:

1. verify that the repository's `Sigma`, restriction, and Fourier projection
   coincide with (L-19820.3)--(L-19820.10);
2. prove convergence of every fold in the declared zero-side/form topology;
3. emit the complete corrected-tail profile and its support derivative;
4. apply the line-centered Bessel/local-Weyl estimate to that exact profile.

## 9. Proof boundary

- The radical/periodization/projection identity is exact linear algebra in a
  Hermitian form.
- No assumption about RH or zero location is used.
- The fold convergence and compatibility of sharp zero extension with the exact
  CCM finite form must be checked in the production normalization.
- Replacing `D_(L,N)` by the ordinary exterior-tail Gram without proving the
  alias and Fourier corrections negligible is invalid.
- This lemma closes an algebraic bridge; it does not itself prove the required
  cofinal lower bound or RH.
