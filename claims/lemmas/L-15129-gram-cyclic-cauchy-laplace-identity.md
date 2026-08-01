# L-15129 — The Gram-cyclic Cauchy--Laplace coefficient is exactly the trace of one matrix power

Claim ID: `L-15129`  
Status: **PROVED FINITE-DIMENSIONAL IDENTITY**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: finite-dimensional linear algebra; the finite `det_2` identity  
Scope: closes the operator-side same-matrix identity at order three and at every order  
Related counterexample candidates: none

## 1. Why a Gram-corrected definition is necessary

Let `E` be an `n`-dimensional complex readout space with a chosen, not necessarily orthonormal, basis. Let

\[
G=G^*>0
\]

be its Gram matrix and let

\[
B=B^*
\]

be the matrix of one Hermitian seam/boundary form. The represented operator is not `B`; it is

\[
\boxed{T=G^{-1}B.}
\tag{L-15129.1}
\]

It is self-adjoint for the `G`-inner product. Its ordinary self-adjoint matrix in orthonormalized coordinates is

\[
K=G^{-1/2}BG^{-1/2},
\tag{L-15129.2}
\]

and `K` is similar to `T`.

A cyclic scalar coefficient must therefore insert one inverse Gram contraction at every gluing. Omitting those contractions produces a basis-dependent number and cannot equal an operator trace.

## 2. Universal Gram-cyclic coefficient

For every integer `ell>=2`, define

\[
\boxed{
\mathfrak c_\ell(G,B)
=
\sum_{a_1,b_1,\ldots,a_\ell,b_\ell}
B_{a_1b_1}(G^{-1})_{b_1a_2}
B_{a_2b_2}(G^{-1})_{b_2a_3}
\cdots
B_{a_\ell b_\ell}(G^{-1})_{b_\ell a_1}.}
\tag{L-15129.3}
\]

Then

\[
\boxed{
\mathfrak c_\ell(G,B)
=\operatorname{Tr}((G^{-1}B)^\ell)
=\operatorname{Tr}(K^\ell).}
\tag{L-15129.4}
\]

### Proof

Expanding the diagonal of `(BG^-1)^ell` gives exactly the contraction in (L-15129.3). Cyclicity of the finite trace gives

\[
\operatorname{Tr}((BG^{-1})^\ell)
=\operatorname{Tr}((G^{-1}B)^\ell).
\]

Finally `K=G^(1/2) T G^(-1/2)`, so `K` and `T=G^-1B` are similar and have the same power traces. QED.

## 3. Order three explicitly

At the first load-bearing odd order,

\[
\boxed{
\mathfrak c_3(G,B)
=\sum_{a,b,c,d,e,f}
B_{ab}(G^{-1})_{bc}
B_{cd}(G^{-1})_{de}
B_{ef}(G^{-1})_{fa}
=\operatorname{Tr}(K^3).}
\tag{L-15129.5}
\]

This is the exact order-three same-matrix identity. It is a polynomial/rational identity in one Gram matrix and one seam matrix; no limit, determinant, or number-theoretic input is needed.

## 4. Scalar Cauchy--Laplace family from the same matrix

Define, for `|w|<||T||^-1`,

\[
\boxed{
\mathscr C_{G,B}(w)
=w\operatorname{Tr}\!\left(T^2(I+iwT)^{-1}\right).}
\tag{L-15129.6}
\]

Because `T` is similar to `K`, this is basis independent. It is also exactly the logarithmic derivative of the finite regularized determinant:

\[
\boxed{
\mathscr C_{G,B}(w)
=\frac{d}{dw}\log\det{}_2(I+iwK).}
\tag{L-15129.7}
\]

Expanding the resolvent gives

\[
\boxed{
\mathscr C_{G,B}(w)
=\sum_{\ell=2}^{\infty}(-i)^{\ell-2}\mathfrak c_\ell(G,B)w^{\ell-1}.}
\tag{L-15129.8}
\]

Consequently, if the normalized scalar Cauchy--Laplace coefficient is defined by

\[
\operatorname{CL}_\ell(G,B)
:=i^{\ell-2}[w^{\ell-1}]\mathscr C_{G,B}(w),
\tag{L-15129.9}
\]

then

\[
\boxed{
\operatorname{CL}_\ell(G,B)
=\mathfrak c_\ell(G,B)
=\operatorname{Tr}(K^\ell)
\qquad(\ell\ge2).}
\tag{L-15129.10}
\]

In particular,

\[
\boxed{
i[w^2]\mathscr C_{G,B}(w)=\operatorname{Tr}(K^3).}
\tag{L-15129.11}
\]

This proves the operator-side scalar/cyclic identity at order three and all orders, provided both are constructed from the same pair `(G,B)` by (L-15129.3)/(L-15129.6).

## 5. Basis-change invariance

For an invertible coordinate change `C`, put

\[
G'=C^*GC,
\qquad
B'=C^*BC.
\]

Then

\[
(G')^{-1}B'=C^{-1}(G^{-1}B)C.
\]

Hence

\[
\boxed{
\mathfrak c_\ell(G',B')=\mathfrak c_\ell(G,B),
\qquad
\mathscr C_{G',B'}=\mathscr C_{G,B}.}
\tag{L-15129.12}
\]

This supplies a decisive audit: any proposed scalar coefficient that changes under a readout reparametrization is not the trace coefficient.

## 6. Kernel form

If the finite operator is represented by a finite-rank kernel

\[
k(x,y)=\sum_{a,b}e_a(x)T_{ab}\overline{e_b(y)}
\]

in an orthonormal realization, then

\[
\boxed{
\operatorname{Tr}(K^3)
=\iiint k(x_1,x_2)k(x_2,x_3)k(x_3,x_1)\,d\mu(x_1)d\mu(x_2)d\mu(x_3).}
\tag{L-15129.13}
\]

The analogous `ell`-fold closed loop equals `Tr(K^ell)`. This is the rigorous finite-window cyclic-integral construction already used in earlier versions of the Shimizu programme; the present lemma records the indispensable Gram factors for arbitrary finite readout coordinates.

## 7. Proof boundary

This lemma proves the complete **operator-side** same-matrix identity. It does not prove that a separately constructed classical explicit-formula scalar probe is the function `mathscr C_(G,B)`. That bridge requires an explicit pullback formula showing that the classical scalar coefficient tensor is precisely (L-15129.3), including every inverse Gram factor. `R-15108` isolates that remaining source-level obligation.
