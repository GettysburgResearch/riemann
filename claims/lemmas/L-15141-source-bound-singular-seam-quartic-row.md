# L-15141 — Source-bound singular-seam quartic row

Claim ID: `L-15141`  
Status: **PROVED FINITE CONSTRUCTION; PUBLIC RIEMANN SOURCE PACKAGE INCOMPLETE**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15136`, `L-15138`--`L-15140`; finite-dimensional Hermitian linear algebra  
Scope: the missing executable producer once the manuscript's finite source data are bound

## 1. Source package

Fix one finite window `M` and one finite readout space `E` of dimension `n`.
A **source-bound package** consists of:

1. a positive Hermitian readout Gram matrix `G`;
2. a quartic central-jet coordinate `v_4 in E`;
3. raw and finite-jet contour-coordinate matrices `X_raw,X_jet`;
4. concrete matrices for the seam transpose `N_seam`, comparison trace
   `T_cmp`, logarithmic comparison inverse `LCI`, and orthogonal projection `P`;
5. a Hermitian seam involution `S`, with `S^2=I`;
6. a directed interval for the original scalar coefficient
   `a_(4,M)^lin` and the independent directed target interval for `tau_4`;
7. source, normalization, cutoff, and parameter fingerprints.

All matrices refer to the same basis and the same manuscript normalization.
No matrix may be nominated independently after the quartic value is inspected.

## 2. Complete singular-seam chain

Put

\[
 J=P\,LCI\,T_{\rm cmp}\,N_{\rm seam}.
 \tag{L-15141.1}
\]

The complete raw, jet, and renormalized comparison maps are

\[
 \widetilde R=JX_{\rm raw},
 \qquad C=JX_{\rm jet},
 \qquad R=\widetilde R-C.
 \tag{L-15141.2}
\]

In the nonorthonormal readout coordinates, their signed seam forms are

\[
 B_A=\widetilde R^*S\widetilde R,
 \qquad B_K=R^*SR.
 \tag{L-15141.3}
\]

The represented operators are therefore

\[
 \boxed{A=G^{-1}B_A,\qquad K=G^{-1}B_K.}
 \tag{L-15141.4}
\]

The actual realized quartic central jet is

\[
 \boxed{c_{4,M}=Cv_4.}
 \tag{L-15141.5}
\]

Its source-normalized squared lower bound is

\[
 \boxed{
 \frac{\|Cv_4\|^2}{v_4^*Gv_4}.}
 \tag{L-15141.6}
\]

The complete finite-jet Schatten-four value is

\[
 \boxed{
 \|C\|_4^4
 =\operatorname{Tr}\!\left[
  \left(G^{-1}C^*C\right)^2
 \right].}
 \tag{L-15141.7}
\]

Finally, the first operator-side quartic row is

\[
 \boxed{
 a_{4,M}^{\rm lin},\qquad
 \operatorname{Tr}(A^4),\qquad
 \operatorname{Tr}(K^4),\qquad
 \tau_4.}
 \tag{L-15141.8}
\]

Equations (L-15141.1)--(L-15141.8) are executable without any further operator
notation once the package is supplied.

## 3. Basis invariance

For an invertible readout-coordinate change `Q`, transform

\[
 G\mapsto Q^*GQ,
 \quad X_{\rm raw}\mapsto X_{\rm raw}Q,
 \quad X_{\rm jet}\mapsto X_{\rm jet}Q,
 \quad v_4\mapsto Q^{-1}v_4.
 \tag{L-15141.9}
\]

Then the represented operators transform by similarity and the realized vector
is unchanged:

\[
 A\mapsto Q^{-1}AQ,
 \qquad K\mapsto Q^{-1}KQ,
 \qquad Cv_4\mapsto Cv_4.
 \tag{L-15141.10}
\]

Consequently

\[
 \operatorname{Tr}(A^4),\quad
 \operatorname{Tr}(K^4),\quad
 \|Cv_4\|^2,\quad
 v_4^*Gv_4,\quad
 \|C\|_4^4
 \tag{L-15141.11}
\]

are intrinsic.  `X-15120` verifies these identities under a dense triangular
coordinate change using exact Gaussian-rational arithmetic.

## 4. Persistent-body and decay verdicts

For a sequence of source-bound windows `M_j`, directed intervals

\[
 0<d\le \frac{\|c_{4,M_j}\|^2}{v_{4,M_j}^*G_{M_j}v_{4,M_j}}
 \tag{L-15141.12}
\]

on an unbounded subsequence prove a persistent quartic body and refute
`||C_(M_j)||_4 -> 0`.

Conversely, an upper bound tending to zero on the single vector is necessary,
but not sufficient, for Schatten-four decay.  A proof of full decay must also
emit the complete value (L-15141.7) or a certified upper bound for it.

The quartic target verdict is made only from directed relations among the four
objects in (L-15141.8).  A floating midpoint is never promoted.

## 5. Determinacy and proof boundary

A complete source-bound package determines every output above uniquely.  An
incomplete package does not determine an `actual` row: choosing an unspecified
probe, cutoff, projection, or finite-part coordinate changes the input object
being evaluated.

The public Shimizu v8/v6 text supplies the abstract types and existence theorems
for the chain, but not a coordinate-level package for any first window.
`O-15106` and the retained source-audit certificate enumerate the missing data.
`X-15120` therefore fails closed rather than substitute a Galerkin model or a
surrogate matrix.
