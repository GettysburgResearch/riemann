# L-21506 — Average raw cardinals first and invert zeta only on a safe support

Claim ID: `L-21506`  
Title: A large-measure zero-avoidance set removes the source-inverse singularities without entering the support large sieve  
Status: **PROPOSED — COMPLETE MEASURE/CONGRUENCE THEOREM; RAW-SOURCE PROFILE LMI REMAINS**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: the smooth differential cardinals of `L-15631`; Riemann--von Mangoldt; a standard local minimum-modulus estimate for zeta  
Scope: quantitative source-frame selection for the PR #202 whole-matrix/prolate support-average routes

## 1. Why the right inverse should not be averaged

For the smooth cardinal columns `f_(k,L)` of `L-15631`, the exact projected
arithmetic image is diagonal:

\[
 \boxed{
 P_N\Sigma_LE(f_{k,L})
 =z_k(L)e_k,
 \qquad
 z_k(L)=\zeta\!\left({1\over2}+i{2\pi k\over L}\right).
 }
 \tag{L-21506.1}
\]

The exact Fourier-space right inverse divides the `k`th source by `z_k(L)`.
That inverse is singular at a zeta-cycle support and may have a large support
derivative nearby.  Inserting it into a support large sieve before choosing the
support creates an unnecessary conditioning problem.

The correct order is:

1. perform all phase averaging on the raw columns `f_(k,L)`;
2. remove the small set of lengths where any `z_k(L)` is too small;
3. select a support in the intersection;
4. only then apply the exact diagonal congruence `Z_L^-1`.

## 2. Fixed-dimensional support block

Fix a constant `ell_0>0`, let `A` be large, and consider

\[
 \mathcal I_A=[A,A+\ell_0].
 \tag{L-21506.2}
\]

Choose a bandwidth `H_A>=2` with

\[
 \log H_A=o(\sqrt A)
 \tag{L-21506.3}
\]

and use the fixed cutoff

\[
 N_A=\left\lfloor {A H_A\over2\pi}\right\rfloor.
 \tag{L-21506.4}
\]

Then for every `L in I_A` and `|k|<=N_A`,

\[
 \left|{2\pi k\over L}\right|\le H_A.
 \tag{L-21506.5}
\]

The coefficient dimension is fixed throughout the whole support block, which
is essential for applying one matrix-valued support-average theorem.

## 3. Large-measure zeta-safe set

Let `Z_A` be the multiset of ordinates of all nontrivial zeta zeros with

\[
 |\gamma|\le2H_A+2.
\]

Set

\[
 \delta_A={1\over[A H_A\log(2H_A)]^2}.
 \tag{L-21506.6}
\]

Delete every length `L in I_A` for which

\[
 \left|{2\pi k\over L}-\gamma\right|<\delta_A
 \tag{L-21506.7}
\]

for some `|k|<=N_A` and `gamma in Z_A`.  Denote the remaining set by
`S_A`.

For one fixed positive ordinate `gamma`, only `O(1+gamma)` integers can resonate
inside a length interval of fixed size.  At a resonance,

\[
 \left|{d\over dL}{2\pi k\over L}\right|
 \asymp {\gamma\over A}.
\]

Thus the total deleted length for that ordinate is `O(delta_A A)`.  The
unconditional zero count

\[
 \#Z_A=O(H_A\log(2H_A))
\]

gives

\[
 \boxed{
 |\mathcal I_A\setminus S_A|
 \ll\delta_A A H_A\log(2H_A)
 \ll {1\over A H_A\log(2H_A)}
 =o(1).
 }
 \tag{L-21506.8}
\]

Hence `S_A` has asymptotically full measure in every fixed logarithmic support
block.

## 4. Uniform minimum modulus on the safe set

A standard local product estimate in a fixed strip implies that, when
`1/2+it` is at distance at least `delta` from the ordinate of every nearby
zero,

\[
 |\zeta(1/2+it)|^{-1}
 \le
 \exp\{C\log(2H)[\log(2H)+\log(1/\delta)]\}.
 \tag{L-21506.9}
\]

The same estimate, after logarithmic differentiation, controls the `t`
derivative.  With (L-21506.3) and (L-21506.6), uniformly for `L in S_A`,

\[
 \boxed{
 \|Z_L^{-1}\|+\|\partial_LZ_L^{-1}\|
 \le\exp(o(A))=R^{o(1)},
 \qquad R=e^A,
 }
 \tag{L-21506.10}
\]

where

\[
 Z_L=\operatorname{diag}(z_k(L))_{|k|\le N_A}.
 \tag{L-21506.11}
\]

The bounded-height range is absorbed by finite compactness and the same
explicit deletion.

## 5. Intersection with phase-good supports

Let `G_A subset I_A` be any support set produced by a raw-source phase-average
argument, and suppose

\[
 |I_A\setminus G_A|=o(1).
 \tag{L-21506.12}
\]

Equations (L-21506.8) and (L-21506.12) give

\[
 |G_A\cap S_A|=\ell_0-o(1)>0
 \tag{L-21506.13}
\]

for all sufficiently large `A`.  Thus one may choose

\[
 \boxed{L_A^*\in G_A\cap S_A.}
 \tag{L-21506.14}
\]

At this support the raw-source phase estimate and the exact Fourier right
inverse both hold.  The large sieve never differentiates `Z_L^-1` and never
crosses a zeta-cycle singularity.

## 6. Exact congruence transfer

Let `A_src(L)` and `D_src(L)` be Hermitian matrices in the raw source
coordinates.  Their Fourier-space matrices at a safe support are

\[
 \boxed{
 A_F=Z_L^{-*}A_{src}Z_L^{-1},
 \qquad
 D_F=Z_L^{-*}D_{src}Z_L^{-1}.
 }
 \tag{L-21506.15}
\]

Every Loewner inequality between `A_src` and `D_src` transfers with **no loss**:

\[
 A_{src}\succeq cD_{src}
 \quad\Longleftrightarrow\quad
 A_F\succeq cD_F.
 \tag{L-21506.16}
\]

Likewise all generalized eigenvalues of the pair are unchanged.  Thus a
relative profile/scalarization theorem should be proved in raw coordinates and
then transported exactly.

For an absolute lower bound in the ordinary Fourier metric, suppose only

\[
 A_{src}\succeq-r_AI.
 \tag{L-21506.17}
\]

Then (L-21506.10) gives

\[
 \boxed{
 A_F\succeq-r_A R^{o(1)}I.
 }
 \tag{L-21506.18}
\]

Every fixed power saving in `r_A` therefore survives the postselection and
right-inverse congruence.

More naturally, if the raw metric is the image Gram

\[
 G_{src}=Z_L^*Z_L,
\]

then

\[
 A_{src}\succeq-r_AG_{src}
 \quad\Longleftrightarrow\quad
 A_F\succeq-r_AI
 \tag{L-21506.19}
\]

exactly, with no condition-number factor.

## 7. Consequence for the complete-frame programme

The source-surjectivity problem separates into two independent tasks.

### Raw analytic task

Prove the complete alias-corrected profile Gram, line-centered local-Weyl LMI,
and rephased horizontal support-average estimate for the raw smooth cardinal
columns.  Their graph and support derivatives are polynomial or
subexponential and contain no `1/zeta` poles.

### Finite arithmetic postselection

Use `S_A` to choose a support at which the diagonal projected image is
invertible.  Exact congruence then gives the same relative LMI on the complete
finite Fourier/CCM space.

This removes the need for a uniformly smooth zeta inverse on the entire support
block and repairs the quantifier mismatch between generic source surjectivity
and positive-measure phase selection.

## 8. Proof boundary

- The deleted-measure estimate and finite-dimensional congruence are exact.
- The minimum-modulus input is standard but must be pinned in the repository's
  completed-zeta convention before publication.
- The theorem does not prove the raw-source profile LMI or its power-saving
  support average.
- It does not prove that a different prolate global-anchor frame has the same
  tail hierarchy; it supplies a clean route for the smooth complete-cardinal
  frame and the whole-matrix theorem.
- No RH conclusion is claimed.
