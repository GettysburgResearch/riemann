# L-106506 — Weighted companion collision is a canonical-correlation defect

Claim ID: `L-106506`  
Status: **PROVED EXACT FOR FINITE SIMPLE MODEL SPACES; CONFLUENT EXTENSION BY DIFFERENTIATION**  
Created: 2026-08-25  
Depends on: `L-106505`; finite Blaschke model-space kernels  
RH status: **not assumed**

Retain the reduced quotient

\[
U=\omega B_+\overline{B_-}
\]

and a diagonal positive contraction `R=M_r` on `L^2(0,infinity)`.  Let the
upper zeros of `B_-` and `B_+` be

\[
b_j^-=a_j^-+iy_j^-,
\qquad
b_k^+=a_k^++iy_k^+.
\]

For a simple zero `b=a+iy`, use the normalized model vector

\[
e_b(\xi)=\sqrt{2y}\,e^{-(y+ia)\xi},
\qquad \xi\ge0.
\tag{L-106506.1}

Let `E_-` and `E_+` be the synthesis maps with these columns.

## 1. Three explicit Grams

Define

\[
G_-=E_-^*E_-,
\qquad
G_+=E_+^*E_+,
\qquad
C=E_-^*E_+.
\]

Their entries are the normalized Cauchy kernels

\[
\boxed{
(G_-)_{jk}
={2\sqrt{y_j^-y_k^-}
 \over y_j^-+y_k^-+i(a_j^--a_k^-)},
}
\tag{L-106506.2}

with the analogous formula for `G_+`, and

\[
\boxed{
C_{jk}
={2\sqrt{y_j^-y_k^+}
 \over y_j^-+y_k^++i(a_j^--a_k^+)}.
}
\tag{L-106506.3}

The current-weighted denominator Gram is

\[
R_-=E_-^*RE_-,
\]

that is,

\[
\boxed{
(R_-)_{jk}
=2\sqrt{y_j^-y_k^-}
\int_0^\infty
 r(\xi)e^{-(y_j^-+y_k^-+i(a_j^--a_k^-))\xi}\,d\xi.
}
\tag{L-106506.4}

For `r=r^sharp_(K,h)`, this is a completely explicit Laplace transform of the
positive Xi cross-current profile.

## 2. Projection formula

The two model projections are

\[
Q_-=E_-G_-^{-1}E_-^*,
\qquad
Q_+=E_+G_+^{-1}E_+^*.
\]

Cyclicity and `T_(B_+)T_(B_+)^*=I-Q_+` turn the collision of `L-106505` into

\[
\mathcal C_R
=\operatorname{tr}(Q_-RQ_-)
-\operatorname{tr}(Q_-RQ_-Q_+).
\]

Substituting the synthesis formulas gives

\[
\boxed{
\mathcal C_R(B_+,B_-)
=
\operatorname{tr}(G_-^{-1}R_-)
-
\operatorname{tr}
\left(
G_+^{-1}C^*G_-^{-1}R_-G_-^{-1}C
\right).
}
\tag{L-106506.5)

This is basis independent and nonnegative.

Equivalently, if

\[
A=G_-^{-1/2}CG_+^{-1/2},
\qquad
W=G_-^{-1/2}R_-G_-^{-1/2},
\]

then

\[
\boxed{
\mathcal C_R
=\operatorname{tr}\left(W(I-AA^*)\right).
}
\tag{L-106506.6)

The singular values of `A` are the canonical correlations between the two
companion model spaces.  The only conclusion-bearing deficit is their failure
to cover the current-weighted denominator directions.

## 3. Confluent and unequal-dimensional blocks

For a zero of multiplicity `q`, replace `e_b` by its first `q` derivatives in
`b`; equations (L-106506.2)--(L-106506.6) persist with confluent Cauchy and
Laplace blocks.  If the dimensions differ, `A` is rectangular and
`I-AA^*` automatically retains every unmatched denominator direction.

## 4. Scope

No lower bound on the canonical correlations is asserted.  In particular,
source-density contraction does not imply `AA^*` is close to the identity.
The formula removes all ambiguity about the remaining fifth-endpoint task:
one must bound the explicit positive trace in (L-106506.6), together with the
pole-height reserve of `L-106505`, below the `97/1000` allowance.
