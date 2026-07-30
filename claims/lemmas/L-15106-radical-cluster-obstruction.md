# L-15106 — Localized global radicals force a near-zero Ritz cluster

Claim ID: `L-15106`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-10`  
Created: 2026-07-30  
Dependencies: `L-15102`, finite-dimensional min--max, and the imported infinite-dimensional global Weil radical  
Scope: audit the denominator in the natural-ground positive RH route  
Related counterexample candidates: none

## 1. Abstract cluster theorem

Let `q` be a Hermitian form on a common domain and let

\[
 r_1,\ldots,r_m\in\operatorname{Rad}(q)
 \tag{L-15106.1}
\]

be linearly independent. For one localization parameter `a`, choose exact
decompositions

\[
 r_j=p_{j,a}+t_{j,a},
 \qquad p_{j,a},t_{j,a}\in D(q),
 \tag{L-15106.2}
\]

where the `p_(j,a)` belong to one local Hilbert space. Define their Hilbert Gram
and local form Gram matrices

\[
 S_a=(\langle p_{i,a},p_{j,a}\rangle)_{i,j=1}^m,
 \qquad
 G_a=(q(p_{i,a},p_{j,a}))_{i,j=1}^m.
 \tag{L-15106.3}
\]

Assume `S_a` is positive definite. Then

\[
 \boxed{
 G_a=(q(t_{i,a},t_{j,a}))_{i,j=1}^m.}
 \tag{L-15106.4}
\]

The generalized Ritz values of `q` on

\[
 P_a=\operatorname{span}\{p_{1,a},\ldots,p_{m,a}\}
\]

are exactly the eigenvalues of

\[
 R_a=S_a^{-1/2}G_aS_a^{-1/2}.
 \tag{L-15106.5}
\]

Consequently, if the localized closed form has compact-resolvent operator with
ordered eigenvalues

\[
 \lambda_1(a)\le\lambda_2(a)\le\cdots,
\]

then

\[
 \boxed{
 \lambda_m(a)\le\lambda_{\max}(R_a)
 \le\|R_a\|_{op}.}
 \tag{L-15106.6}
\]

If

\[
 \lambda_{\min}(S_a)\ge s_*>0,
 \qquad
 |q(t_{i,a},t_{j,a})|\le\varepsilon_a,
 \tag{L-15106.7}
\]

then the elementary row-sum estimate gives

\[
 \boxed{
 \lambda_m(a)\le\frac{m\varepsilon_a}{s_*}.}
 \tag{L-15106.8}
\]

Thus every finite family of independent global radical vectors creates the same
number of localized Ritz directions near zero as their tails disappear.

### Proof

Polarizing the radical decomposition identity in `L-15102` gives

\[
 q(p_{i,a},p_{j,a})=q(t_{i,a},t_{j,a}),
\]

which is (L-15106.4). The remaining statements are the standard generalized
Rayleigh--Ritz formula and min--max principle. Under (L-15106.7),

\[
 \|G_a\|_{op}\le m\varepsilon_a,
 \qquad
 \|S_a^{-1/2}\|_{op}^2\le s_*^{-1},
\]

proving (L-15106.8). QED.

## 2. Consequence for one-target coercivity

Take `m>=2` and select `p_(1,a)` as the proposed ground target. There is a
nonzero vector

\[
 w_a\in P_a\cap p_{1,a}^{\perp}.
\]

Its Rayleigh value satisfies

\[
 \frac{q(w_a,w_a)}{\|w_a\|^2}
 \le\lambda_{\max}(R_a).
 \tag{L-15106.9}
\]

Suppose a one-target complement gate is attempted with

\[
 U_a\ge\frac{q(p_{1,a},p_{1,a})}{\|p_{1,a}\|^2}
 \tag{L-15106.10}
\]

and ordinary `L2` coercivity

\[
 q(w,w)-U_a\|w\|^2\ge h_a\|w\|^2
 \quad(w\perp p_{1,a}).
 \tag{L-15106.11}
\]

Then necessarily

\[
 \boxed{
 h_a\le\lambda_{\max}(R_a)-U_a.}
 \tag{L-15106.12}
\]

In particular, when the chosen target and another independent localized radical
both have tail-scale Rayleigh values, the allowed complement coercivity is at
most tail scale. The leakage numerator and the natural spectral gap are then not
independent asymptotic quantities.

This does not prove that every weighted coercivity used in `L-14302` fails. It
proves that a one-dimensional natural-ground isolation theorem must confront the
entire localized radical cluster rather than only one Hermite/prolate vector.

## 3. Weil specialization

The Connes--Consani global Weil radical contains

\[
 E(\mathcal S_{ev}^{0}),
 \qquad
 \mathcal S_{ev}^{0}
 =\{f\in\mathcal S(\mathbb R):
     f\text{ even},\ f(0)=\widehat f(0)=0\},
 \tag{L-15106.13}
\]

an infinite-dimensional space. Choose any fixed number of independent Hermite
sources in this class and localize their `E`-images with the same smooth
multiplier.

The Gaussian/super-Gaussian estimates of `L-15101` and `L-15104` apply mode by
mode. Provided the local Hilbert Gram remains nondegenerate, (L-15106.8) gives
arbitrarily long localized near-zero Ritz clusters.

Therefore the exact global radical simultaneously provides:

- the strongest target approximation mechanism;
- an obstruction to proving that one such target is naturally spectrally
  isolated.

## 4. Strategic consequence

The primary positive route should not assume that the Xi target becomes the
unique natural ground direction. More robust alternatives are:

1. quotient or constrain away the other radical directions while preserving the
   CCM special commutator;
2. use a boundary-selected resolvent direction as in `L-15105`;
3. develop a higher-rank/matrix-valued real-zero theorem for the whole radical
   cluster;
4. prove that a distinguished boundary functional selects the Xi radical in the
   continuum limit.

The sharp boundary-resolvent family is presently the cleanest finite theorem:
it creates a one-dimensional special kernel by construction, without demanding
a pre-existing gap between clustered natural Ritz values.

## Gap audit

- The theorem supplies upper bounds on low Ritz values, not lower bounds and not
  their signs.
- Uniform nondegeneracy of `S_a` must be proved for the selected radical family.
  For fixed independent global vectors it is expected from ordinary localization
  convergence, but it is retained as an explicit gate.
- Tail smallness in the Weil form is stronger than ordinary `L2` tail smallness;
  `L-15104` provides one route for smooth Hermite targets.
- The cluster theorem does not refute the finite natural-ground results in
  PR #150. It explains why their asymptotic gap hypothesis may be the wrong
  global invariant.
