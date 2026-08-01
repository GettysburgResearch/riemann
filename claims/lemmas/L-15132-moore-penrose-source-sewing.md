# L-15132 — Moore--Penrose source sewing gives the exact finite cyclic coefficient

Claim ID: `L-15132`  
Status: **PROVED FINITE SOURCE-INTERFACE THEOREM**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: finite-dimensional Hilbert-space geometry; Moore--Penrose inverse; Schatten Hölder  
Scope: the classical/readout-coordinate side of the same-matrix coefficient problem  
Related counterexample candidates: none

## 1. The finite readout object

Let `E` be a finite-dimensional readout-coordinate space and let

\[
 U:E\longrightarrow H
 \tag{L-15132.1}
\]

be the synthesis map into a Hilbert space `H`. Redundant coordinates are
allowed. Put

\[
 G=U^*U\succeq0
 \tag{L-15132.2}
\]

and let `G^dagger` be its Moore--Penrose inverse. Let `S=S*` be one signed seam
operator on `H`, and let

\[
 B=U^*SU
 \tag{L-15132.3}
\]

be its readout-coordinate form.

The intrinsic represented space is not all of `E`; it is the quotient by
`ker U`, equivalently `Ran G`. The canonical coevaluation/gluing tensor on that
quotient is `G^dagger`, not the identity matrix and not a freely chosen probe.

Define

\[
 P_U=UG^\dagger U^*.
 \tag{L-15132.4}
\]

Then `P_U` is the orthogonal projection onto `Ran U`.

## 2. The sewn classical coefficient

For every integer `ell>=2`, define the closed source loop

\[
\boxed{
 \operatorname{Sew}_\ell(U,S)
 =
 \sum_{a_1,b_1,\ldots,a_\ell,b_\ell}
 B_{a_1b_1}(G^\dagger)_{b_1a_2}
 \cdots
 B_{a_\ell b_\ell}(G^\dagger)_{b_\ell a_1}.}
 \tag{L-15132.5}
\]

This is the finite source-coordinate formula requested by the determinant
programme. One inverse Gram contraction occurs at every seam gluing.

## 3. Source-sewing theorem

One has

\[
\boxed{
 \operatorname{Sew}_\ell(U,S)
 =\operatorname{Tr}\bigl((G^\dagger B)^\ell\bigr)
 =\operatorname{Tr}_{\operatorname{Ran}U}
  \bigl((P_USP_U)^\ell\bigr).}
 \tag{L-15132.6}
\]

### Proof

The first equality follows by expanding the closed matrix product.

For the second, write `U_0:E/ker U -> Ran U` for the induced isomorphism. The
operator represented on the quotient by `G^dagger B` is conjugate through
`U_0` to the compression `P_U S P_U|Ran U`. Equivalently, use the partial
isometry in the polar decomposition of `U`: on the support of `G`,

\[
 U=V G^{1/2},
 \qquad
 B=G^{1/2}V^*SV G^{1/2},
\]

so the nonzero block of `G^dagger B` is similar to `V^*SV`, which is unitarily
equivalent to `P_U S P_U|Ran U`. Power traces agree. QED.

If `U` is surjective, `P_U=I_H`, and therefore

\[
\boxed{
 \operatorname{Sew}_\ell(U,S)=\operatorname{Tr}(S^\ell).}
 \tag{L-15132.7}
\]

## 4. First nontrivial even order

At `ell=4`,

\[
\boxed{
 \operatorname{Sew}_4(U,S)
 =
 \sum
 B_{a_1b_1}(G^\dagger)_{b_1a_2}
 B_{a_2b_2}(G^\dagger)_{b_2a_3}
 B_{a_3b_3}(G^\dagger)_{b_3a_4}
 B_{a_4b_4}(G^\dagger)_{b_4a_1}.}
 \tag{L-15132.8}
\]

This is quartic in the seam form and is the first coefficient carrying genuine
even determinant data after cubic parity has been imposed.

## 5. Coordinate invariance, including redundant coordinates

Let `C:E'->E` be invertible and replace `U` by `U C`. Recompute

\[
 G_C=C^*GC,
 \qquad
 B_C=C^*BC,
\]

and use the Moore--Penrose inverse of `G_C`. Although a Moore--Penrose inverse
does not obey a naive congruence formula for arbitrary nonunitary `C`, the
projection

\[
 U C\,G_C^\dagger C^*U^*
\]

is still the orthogonal projection onto `Ran U`. Therefore (L-15132.6) gives

\[
\boxed{
 \operatorname{Sew}_\ell(UC,S)
 =\operatorname{Sew}_\ell(U,S).}
 \tag{L-15132.9}
\]

Thus the pseudoinverse-sewn coefficient is intrinsic even for overcomplete
readouts.

## 6. One majorant for every order and every limit

Let

\[
 K_{M,N}=P_{M,N}S_MP_{M,N}|_{\operatorname{Ran}U_{M,N}}
 \tag{L-15132.10}
\]

be any coherent finite-window/readout family obtained by the source sewing
above. Suppose

\[
\boxed{
 \sup_{M,N}\|K_{M,N}\|_2\le C<\infty.}
 \tag{L-15132.11}
\]

Then, for every `ell>=2`,

\[
\boxed{
 |\operatorname{Sew}_\ell(U_{M,N},S_M)|
 =|\operatorname{Tr}(K_{M,N}^\ell)|
 \le C^\ell.}
 \tag{L-15132.12}
\]

Indeed,

\[
 \sum_j|\lambda_j|^\ell
 \le\left(\sum_j|\lambda_j|^2\right)^{\ell/2}.
\]

Consequently, for every `r<1/C`,

\[
\boxed{
 \sum_{\ell=2}^\infty
 |\operatorname{Sew}_\ell|r^{\ell-1}
 \le\frac{C^2r}{1-Cr}.}
 \tag{L-15132.13}
\]

This one geometric bound is independent of `M,N` and simultaneously justifies:

1. finite-readout limits;
2. finite-window limits;
3. interchange of either limit with the determinant power series;
4. local uniform convergence of the logarithmic-derivative series.

If the finite family comes from a Schatten-four sandwich

\[
 K_{M,N}=A_{M,N}^*S_{M,N}A_{M,N},
 \qquad S_{M,N}^2=I,
\]

then it is sufficient to prove

\[
 \sup_{M,N}\|A_{M,N}\|_4^2\le C.
\]

## 7. Exact source-side repair

The canonical coordinate-invariant way to turn one bilinear seam form into a closed
`ell`-loop using the readout Hilbert structure is to insert the quotient
coevaluation `G^dagger` at every gluing. In categorical language,
(L-15132.5) is the trace obtained by alternating the seam tensor and the
Moore--Penrose coevaluation around one directed cycle.

Accordingly, a classical Cauchy--Laplace coefficient can equal a power trace
only after its finite source definition has been shown to be precisely
(L-15132.5). Merely applying one fixed linear probe to a finite-part coordinate
does not perform this sewing. That obstruction is recorded in `R-15109`.

## 8. Proof boundary

1. This theorem proves the source-coordinate sewing identity and the common
   majorant.
2. It does not assert that the scalar probe displayed in the Shimizu manuscript
   is already this sewn tensor.
3. It does not identify the sewn coefficient with a central derivative of
   `xi`.
4. A proof of that final identification would be RH-bearing from the even
   moment hierarchy onward.
