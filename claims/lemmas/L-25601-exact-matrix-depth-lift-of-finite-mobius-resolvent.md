# L-25601 — Exact matrix depth lift of the finite Möbius resolvent

Claim ID: `L-25601`  
Title: A nilpotent depth matrix packages the complete finite Möbius resolvent, every reflected cross term, and the physical source synthesis in one exact inverse system  
Status: **PROPOSED EXACT ALGEBRAIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #256  
Dependencies: `L-23201`; PR #241 `L-9518`  
Scope: exact source map and depth incidence; no coercive inequality

## 1. Scalar finite inverse data

Fix `K>=1` and a truncation parameter `V`.  In an absolute-convergence
half-plane put

\[
M_V(s)=\sum_{n\le V}{\mu(n)\over n^s},
\qquad
R_V(s)=1-\zeta(s)M_V(s).
\tag{L-25601.1}
\]

Let

\[
C_V(s)=M_V(s)^{-1}
\]

where defined.  Then

\[
C_V(s)(1-R_V(s))=\zeta(s).
\tag{L-25601.2}
\]

The usual finite inverse is

\[
A_{K,V}(s)=M_V(s)\sum_{j=0}^{K-1}R_V(s)^j.
\tag{L-25601.3}
\]

## 2. Nilpotent depth matrix

Let `S_K` be the nilpotent forward shift on `C^K`,

\[
S_Ke_j=e_{j+1}\quad(0\le j<K-1),
\qquad S_Ke_{K-1}=0.
\tag{L-25601.4}
\]

Thus `S_K^K=0`.  Define

\[
\boxed{
\mathbf A_{K,V}(s)=C_V(s)(I-R_V(s)S_K),}
\tag{L-25601.5}
\]

\[
\boxed{
\mathbf B_{K,V}(s)=
M_V(s)\sum_{j=0}^{K-1}R_V(s)^jS_K^j.}
\tag{L-25601.6}
\]

The finite geometric identity gives exactly

\[
(I-RS_K)\sum_{j=0}^{K-1}R^jS_K^j=I,
\]

and therefore

\[
\boxed{
\mathbf A_{K,V}(s)\mathbf B_{K,V}(s)=I.}
\tag{L-25601.7}
\]

No endpoint approximation or zero hypothesis enters.

## 3. Matrix generalized von Mangoldt sequence

Define the matrix logarithmic derivative

\[
\mathbf L_{K,V}(s)
=-\mathbf A_{K,V}'(s)\mathbf A_{K,V}(s)^{-1}.
\tag{L-25601.8}
\]

Since every matrix is a polynomial in `S_K`, all factors commute.  Direct
differentiation yields

\[
\boxed{
\mathbf L_{K,V}(s)
=\lambda_0(s)I+
\sum_{j=1}^{K-1}\lambda_j(s)S_K^j,}
\tag{L-25601.9}
\]

where

\[
\boxed{
\lambda_0={M_V'\over M_V},
\qquad
\lambda_j=R_V'R_V^{j-1}\quad(j>=1).}
\tag{L-25601.10}
\]

Indeed,

\[
-\mathbf A'\mathbf A^{-1}
={M_V'\over M_V}I
+R_V'S_K(I-R_VS_K)^{-1}.
\]

## 4. Exact scalar synthesis through the endpoint

Let

\[
u_K=e_0,
\qquad
u_K=e_0+\cdots+e_{K-1}.
\]

Then

\[
\nu_K^*\mathbf L_{K,V}\nu_K
={M_V'\over M_V}
+R_V'\sum_{j=0}^{K-2}R_V^j.
\tag{L-25601.11}
\]

The complete zeta logarithmic derivative satisfies

\[
-\frac{\zeta'}\zeta
={M_V'\over M_V}+{R_V'\over1-R_V}.
\tag{L-25601.12}
\]

Consequently

\[
\boxed{
-\frac{\zeta'}\zeta
-\nu_K^*\mathbf L_{K,V}\nu_K
={R_V'R_V^{K-1}\over1-R_V}.}
\tag{L-25601.13}
\]

The arithmetic coefficients of `R_V` are supported strictly above `V`, while
those of `R_V'` have the same support.  Hence the numerator
`R_V'R_V^(K-1)` is supported strictly above

\[
(V+1)^K.
\]

If `V=ceil(X^(1/K))`, the right side of (L-25601.13) has zero coefficient
through the endpoint `X`.  Therefore, coefficientwise through `X`,

\[
\boxed{
\nu_K^*\mathbf L_{K,V}\nu_K
=-\frac{\zeta'}\zeta.}
\tag{L-25601.14}
\]

This is the exact source synthesis map missing from packetwise uses of the
scalar Selberg equation.

## 5. Two-frequency reflected lift

For independent real frequencies `t,s`, form

\[
\mathbf L_+(w)=\mathbf L_{K,V}(w+it),
\qquad
\mathbf L_-(w)=\mathbf L_{K,V}(w-is).
\]

Their tensor product gives the depth-by-depth reflected source

\[
\mathbf L_+(w)\boxtimes\mathbf L_-(w).
\tag{L-25601.15}
\]

The scalar synthesis functional is

\[
(\nu_K\otimes\nu_K)^*
[\mathbf L_+\boxtimes\mathbf L_-]
(\nu_K\otimes\nu_K).
\tag{L-25601.16}
\]

Through endpoint `X` this equals

\[
\left[-{\zeta'\over\zeta}(w+it)\right]
\left[-{\zeta'\over\zeta}(w-is)\right].
\tag{L-25601.17}
\]

Inserting (L-25601.17) into the two-frequency block identity `L-9518` retains
**every** depth cross term and reconstructs the physical factor-ratio normal
Gram exactly.  There is no packet/global source mismatch.

## 6. Bounded incidence, but not bounded arithmetic charge

The matrix generator `I-RS_K` has only a diagonal edge and one forward depth
edge.  Consequently the depth-incidence graph has uniformly bounded local
degree, and all internal depth faces telescope exactly in the matrix product.

This is a genuine bookkeeping improvement.  It does not imply that the
arithmetic coefficient supported on a surviving depth face has bounded divisor
dimension or small norm.  The scalar synthesis functional still contains the
fixed-ratio Möbius shell of PRs #229/#234.

## 7. Interaction with the reserve obstruction

Equation (L-25601.16) gives an exact source map into the aggregate physical
block.  By `R-25601`, the synthesis Gram has a nontrivial kernel and no strict
Schur reserve on the full depth tensor space.  Thus the matrix lift closes the
missing cross-term ledger but does not manufacture the arithmetic frame
inequality.

## 8. Proof boundary

Closed exactly here:

- an invertible finite depth system;
- its matrix logarithmic derivative;
- coefficientwise synthesis of `-zeta'/zeta` through `X`;
- the independent two-frequency reflected tensor;
- every depth cross term and the bounded incidence graph.

Open:

- a source-specific lower frame bound on the actual depth orbit;
- the fixed-ratio shell-energy estimate;
- `RBC(K)` and RH.
