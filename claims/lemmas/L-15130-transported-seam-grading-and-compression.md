# L-15130 — Transported seam grading, exact odd-trace cancellation, and compression coherence

Claim ID: `L-15130`  
Status: **PROVED FINITE/OPERATOR-THEORETIC LEMMA; SOURCE INTERTWINING MUST BE CHECKED**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15129`; elementary graded linear algebra  
Scope: constructs the anti-commuting grading needed by centered determinant parity  
Related counterexample candidates: none

## 1. Invariant finite formulation

Use the finite readout space and matrices `(G,B)` of `L-15129`. Let `J` be a linear map satisfying

\[
J^2=I,
\tag{L-15130.1}
\]

\[
J^*G=GJ,
\tag{L-15130.2}
\]

and the odd seam-form identity

\[
\boxed{J^*BJ=-B.}
\tag{L-15130.3}
\]

Equation (L-15130.2) means that `J` is a self-adjoint involution for the `G`-inner product. Equation (L-15130.3) means that the seam form changes sign when both entries are graded.

Let

\[
T=G^{-1}B,
\qquad
K=G^{1/2}TG^{-1/2},
\qquad
\Gamma=G^{1/2}JG^{-1/2}.
\]

Then

\[
\boxed{
\Gamma=\Gamma^*=\Gamma^{-1},
\qquad
\Gamma K\Gamma=-K.}
\tag{L-15130.4}
\]

### Proof

Since `J` is a `G`-self-adjoint involution, transport by the unitary identification from `(E,G)` to Euclidean coordinates makes `Gamma` a self-adjoint unitary involution. The form identity (L-15130.3) is equivalent to

\[
JTJ=-T
\]

on the `G`-Hilbert space. Similarity by `G^(1/2)` gives `Gamma K Gamma=-K`. QED.

## 2. Exact odd-trace cancellation

For every integer `r>=0`,

\[
\begin{aligned}
\operatorname{Tr}(K^{2r+1})
&=\operatorname{Tr}(\Gamma K^{2r+1}\Gamma)\\
&=-\operatorname{Tr}(K^{2r+1}).
\end{aligned}
\]

Therefore

\[
\boxed{\operatorname{Tr}(K^{2r+1})=0.}
\tag{L-15130.5}
\]

By `L-15129`, every odd Gram-cyclic and normalized Cauchy--Laplace coefficient vanishes as well.

In particular,

\[
\boxed{
\operatorname{CL}_3(G,B)=\operatorname{Tr}(K^3)=0.}
\tag{L-15130.6}
\]

The centered classical function `xi(1/2+w)` is even, so its logarithmic derivative is odd and its order-three coefficient is also zero. Thus (L-15130.6) closes the order-three scalar/trace comparison once the finite seam family satisfies (L-15130.1)--(L-15130.3).

## 3. Concrete two-sided seam construction

Let the finite seam readout retain both orientations:

\[
E=E_+\oplus E_-.
\]

Put

\[
J=\begin{pmatrix}I&0\\0&-I\end{pmatrix},
\qquad
G=\begin{pmatrix}G_+&0\\0&G_-\end{pmatrix},
\tag{L-15130.7}
\]

and suppose the signed seam form has only opposite-side entries:

\[
\boxed{B=\begin{pmatrix}0&C\\C^*&0\end{pmatrix}.}
\tag{L-15130.8}
\]

Then all hypotheses above hold. This is the exact finite realization of a seam reflection that swaps the two orientations, with the side-sign operator as the grading.

For a Sobolev sandwich, let the seam involution on the target space be

\[
S=\begin{pmatrix}0&U^*\\U&0\end{pmatrix}
\]

and let the smoothing/readout map be side preserving,

\[
A=\begin{pmatrix}A_+&0\\0&A_-\end{pmatrix}.
\]

Then `B=A^*SA` has the form (L-15130.8). Equivalently, if `Sigma` is the side sign on the target and `J` the side sign on the source,

\[
AJ=\Sigma A,
\qquad
\Sigma S\Sigma=-S,
\tag{L-15130.9}
\]

implies

\[
J(A^*SA)J=-A^*SA.
\]

This is the transported anti-commuting grading requested by the determinant construction. It must be established before the two seam orientations are quotiented or mixed.

## 4. Same-side obstruction

For any proposed seam matrix, define

\[
B_{\rm even}=\frac12(B+J^*BJ),
\qquad
B_{\rm odd}=\frac12(B-J^*BJ).
\tag{L-15130.10}
\]

Then `B_odd` satisfies the grading identity and `B_even` is the exact same-side/parity-breaking defect. The grading construction works for the original matrix if and only if

\[
\boxed{B_{\rm even}=0.}
\tag{L-15130.11}
\]

Replacing `B` by `B_odd` is not a harmless repair: it changes the even trace moments and hence changes the determinant target. A production proof must show (L-15130.11), not impose it by symmetrization after the fact.

## 5. Finite compression must preserve the grading

Let `K=K*` on a Hilbert space, let `Gamma` be a self-adjoint involution with `Gamma K Gamma=-K`, and let `P` be a finite-rank orthogonal projection. If

\[
\boxed{[P,\Gamma]=0,}
\tag{L-15130.12}
\]

then on `PH`

\[
\Gamma_P=P\Gamma P,
\qquad
K_P=PKP
\]

satisfy

\[
\Gamma_P^2=P,
\qquad
\Gamma_PK_P\Gamma_P=-K_P.
\tag{L-15130.13}
\]

Thus every finite compression has zero odd traces exactly.

For an arbitrary projection, put `Q=I-P`. Direct expansion gives the exact defects

\[
\boxed{\Gamma_P^2-P=-P\Gamma Q\Gamma P,}
\tag{L-15130.14}
\]

and

\[
\boxed{
\Gamma_PK_P+K_P\Gamma_P
=-P\Gamma QKP-PKQ\Gamma P.}
\tag{L-15130.15}
\]

These formulas show why strong convergence of arbitrary compressions is not enough for exact finite parity. The finite readout basis must be chosen in `Gamma`-homogeneous pairs, or an explicit leakage estimate must be carried all the way to the odd moments.

## 6. Exact counterexample to arbitrary compression

Take

\[
K=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
\Gamma=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Then `Gamma K Gamma=-K`. Let `P` be the orthogonal projection onto the line spanned by `(2,1)`:

\[
P=\frac15\begin{pmatrix}4&2\\2&1\end{pmatrix}.
\]

The projection does not commute with `Gamma`, and

\[
\boxed{\operatorname{Tr}((PKP)^3)=\frac{64}{125}\ne0.}
\tag{L-15130.16}
\]

Thus a non-grading-preserving finite-rank compression manufactures a cubic trace even though the original operator has perfect spectral symmetry.

## 7. Proof boundary for the Shimizu construction

The centered seam reflection announced in the manuscript supplies a natural **candidate** for the two-sided swap `S`. It does not, by self-adjointness alone, supply the side-sign grading on the Sobolev reference space. A complete proof must exhibit:

1. the two seam orientations before quotienting;
2. a source grading `J` and target grading `Sigma`;
3. the intertwining `AJ=Sigma A`;
4. the oddness `Sigma S Sigma=-S`;
5. grading-invariant finite readout projections.

These five identities are finite/operator equalities and can be checked without knowing any zeta zero. Their absence is the smallest exact obstruction to the order-three step.
