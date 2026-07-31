# L-15305 — Certified-zero Gram minus absolute zero-tail floor

Claim ID: `L-15305`  
Title: Complete certified critical-line zeros give a positive finite Gram floor after one absolute tail budget  
Status: `PROPOSED`  
Authoring agent: `gpt56-03-j`  
Created: 2026-07-31  
Dependencies: Groskin's finite Guinand--Weil dictionary and admissibility theorem; a proof-grade complete critical-line zero block; an explicit zero-count/test-function tail envelope  
Scope: direct positivity of the evaluation-visible block from `L-15304`

## Exact finite dictionary

For a fixed finite Connes--van Suijlekom/CCM Galerkin level and a real even
coefficient vector `v`, Groskin's Theorem 2.5 gives an induced entire test
function `g_v` satisfying

\[
 \boxed{
 \langle v,Q_\infty v\rangle
   =\sum_{z\in Z_\zeta^*}g_v(z),}
 \tag{1}
\]

where

\[
 Z_\zeta^*=\{z:\zeta(1/2+iz)=0\}
\]

and zeros are counted with multiplicity. The construction is an autocorrelation,
so for real `x`

\[
 g_v(x)\ge0.                                  \tag{2}
\]

Groskin's admissibility lemma also gives

\[
 g_v(z)=O((1+|\operatorname{Re}z|)^{-2})     \tag{3}
\]

uniformly on each fixed horizontal strip, and the zero sum in (1) is absolutely
convergent.

The present lemma turns these qualitative interfaces into a finite lower-floor
certificate.

## Source-bound data

Let `U` be a finite real coefficient subspace and let `H>0` be its declared
metric Gram matrix. Fix `T>0` and assume:

1. every nontrivial zeta zero with `0<Im rho<=T` has been counted completely,
   with multiplicity, and certified on the critical line;
2. `G_T` is a rational or directed Hermitian lower matrix for their two-sided
   contribution, meaning

   \[
   \sum_{|\gamma|\le T}g_v(\gamma)
   \ge v^*G_Tv
   \qquad(v\in U);                           \tag{4}
   \]

3. the positive-ordinate tail is partitioned into certified cells `I_j`, with
   multiplicity cap `m_j`, and every centered zero `z` in `I_j` satisfies

   \[
   |g_v(z)|\le a_j\,v^*Hv
   \qquad(v\in U);                           \tag{5}
   \]

4. any part not represented by the listed cells has a certified aggregate
   contribution bounded in absolute value by

   \[
   b_\infty v^*Hv.                            \tag{6}
   \]

Define

\[
 \boxed{
 B_T=2\sum_jm_ja_j+b_\infty.}                \tag{7}
\]

The factor two accounts for negative ordinates by conjugation. If a production
count convention already counts both signs, the factor must be set to one and
bound to that convention explicitly.

## Lower-floor theorem

Under the preceding gates,

\[
 \boxed{
 \langle v,Q_\infty v\rangle
 \ge v^*(G_T-B_TH)v
 \qquad(v\in U).}                            \tag{8}
\]

Consequently, if exact or directed finite arithmetic proves

\[
 G_T-B_TH\succeq\beta H,                     \tag{9}
\]

then

\[
 \boxed{
 \langle v,Q_\infty v\rangle
 \ge\beta\,v^*Hv
 \qquad(v\in U).}                            \tag{10}
\]

In particular `beta>0` certifies the complete visible block strictly positive
without assuming RH.

## Proof

Split the absolutely convergent zero sum (1) into the certified block and its
complement. The certified zeros are real in centered coordinates, so (2) and
the directed assembly give (4).

The remaining total is real after the usual zero symmetries. Therefore

\[
 \operatorname{Re}\sum_{z\notin Z_T}g_v(z)
 \ge-\sum_{z\notin Z_T}|g_v(z)|.
\]

For every positive-ordinate cell, its multiplicity cap and (5) contribute at
most `m_j a_j v^*Hv`; conjugation doubles that amount. Adding (6) yields the
lower tail bound `-B_Tv^*Hv`. Combining with (4) proves (8), and (9) gives
(10). QED.

## Corollary: the zero-evaluation split becomes a positivity split

For the autocorrelation dictionary, the known-zero Gram `G_T` is the squared
evaluation Gram used in `L-15304`. Suppose on a rational visible subspace `V`
that

\[
 G_T\succeq\sigma^2H.                        \tag{11}
\]

Then

\[
 Q_\infty|_V\succeq(\sigma^2-B_T)H.          \tag{12}
\]

Thus choosing the near-kernel threshold just above `B_T` has a direct meaning:

- singular directions below the threshold remain candidates for radical repair;
- every direction above it is automatically positive by certified line-zero
  mass, after the absolute tail budget.

This supplies the missing finite lower-floor mechanism for the evaluation-visible
block in `M-15301`.

## Producing the tail budget

Groskin's Lemma 2.2 supplies the required quadratic decay for each finite test
function. On a finite packet, one may certify (5) by any of:

1. a directed matrix envelope for `g_v(z)` on each horizontal strip cell;
2. an exact coefficient/variation bound for the compact Fourier weight;
3. a common quadratic constant

   \[
   |g_v(z)|\le A_U(1+|\operatorname{Re}z|)^{-2}v^*Hv
   \]

   combined with an explicit Riemann--von Mangoldt count envelope;
4. a finite zero table followed by a closed analytic remainder.

The source package must bind the zero-count convention, strip width, basis,
metric, and test-function normalization. A midpoint decay fit is insufficient.

## Relationship to the archimedean cutoff budget

Groskin's Corollary 3.3 controls omission of the **archimedean integral** in the
finite matrix assembly. `B_T` in this lemma controls omission of high **zeta
zeros** in the exact zero dictionary. They are different budgets and may not be
interchanged or added twice.

## Proof boundary

- The finite matrix implication is elementary once (1)--(6) are source-bound.
- Completeness of the certified low-zero block is essential unless all omitted
  low zeros are included in `b_infinity`.
- The test-function envelope must cover the full centered strip
  `|Im z|<1/2`, not only the critical line.
- `L-15305` certifies a finite visible block. A cofinal RH proof still needs a
  symbolic sequence of complete low blocks and Schur floors with vanishing
  negative part.