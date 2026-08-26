# L-106671 — Endpoint free energy is a literal source-evaluation Pick determinant

Claim ID: `L-106671`  
Status: **PROVED EXACT FOR REDUCED FINITE ENDPOINT FACTORS**  
Created: 2026-08-26  
Depends on: `L-106620`, `L-106650`, `L-106670`  
RH status: **not assumed**

Let a reduced endpoint pair have the common-outer factorization

\[
N=OB_+,
\qquad
D=OB_-,
\qquad
R=N-D.
\]

Let `B_-^sh` be a denominator subfactor and let
`b_1,...,b_m` be its simple zeros.  Use the Hardy kernel synthesis at these
nodes and write its Gram as `G`.

## 1. Source values at denominator nodes

At a denominator zero `b_r`,

\[
D(b_r)=0,
\]

so

\[
\boxed{
v_r:=B_+(b_r)
={N(b_r)\over O(b_r)}
={R(b_r)\over O(b_r)}.
}
\tag{L-106671.1}
\]

Put `V=diag(v_1,...,v_m)`.  The adverse compression has Gram

\[
E^*P_{B_+H^2}E=V^*GV,
\]

while the favorable numerator-model compression has Gram

\[
H=G-V^*GV.
\tag{L-106671.2}
\]

Therefore `L-106670` becomes

\[
\boxed{
\mathfrak Z_\tau
=
{\det(G-\tau V^*GV)\over\det G}.
}
\tag{L-106671.3}
\]

Entrywise,

\[
\boxed{
(G-\tau V^*GV)_{rs}
=G_{rs}\left(1-\tau\overline{v_r}v_s\right).
}
\tag{L-106671.4}
\]

This is the Pick matrix of the strict Schur function
`sqrt(tau) B_+` evaluated at the actual denominator nodes.  It is positive
definite for every `0<tau<1`, even when the unregularized overlap is singular.

## 2. Frozen fifth-endpoint source

For the mesoscopic Riemann--Siegel gauge of `L-106620`,

\[
N_j=R_{0,j}C_{5,j},
\qquad
D_j=C_{0,j}R_{5,j},
\]

and the source difference is exactly

\[
\boxed{
R_j=N_j-D_j
=2i\lambda_j\left(h\,DH_5-(Dh)H_5\right).
}
\tag{L-106671.5}
\]

Consequently every node value in (L-106671.3) is the literal quantity

\[
\boxed{
v_{j,r}
=
{2i\lambda_j\left(h\,DH_5-(Dh)H_5\right)(b_{j,r})
\over O_j(b_{j,r})}.
}
\tag{L-106671.6}
\]

No numerator-zero enumeration, transport matrix, inverse Gram, or external
frame constant appears in the determinant statement.

## 3. Confluent form

At a denominator zero of multiplicity `q`, replace the kernel column by its
first `q` derivative kernels and replace the scalar value by the triangular
jet of multiplication by `B_+`.  Formula (L-106671.3) persists verbatim with
that confluent block.  Common factors are removed before forming the packet.

## 4. Boundary

The positive Fourier density of the fifth Wronskian controls diagonal
real-line source energies.  It does not, by itself, lower-bound
(L-106671.3): the complex node evaluations and the common outer denominator
retain the degree-zero phase geometry.  The determinant identifies that
remaining Xi-specific statement exactly; it does not assume it.
