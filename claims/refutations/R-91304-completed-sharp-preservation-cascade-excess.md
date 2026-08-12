# R-91304 — One-factor SHARP preservation does not tensorize; the complete cascade excess is an explicit positive cocycle

Claim ID: `R-91304`  
Status: **EXACT REFUTATION AND CLOSED-FORM CASCADE DIAGNOSIS**  
Created: 2026-08-12  
Depends on: `L-91319`; review PR #405  
RH status: **unproved**

## 1. One-factor matrices

For `0 <= r < 1/2`, put

\[
 M(r)=(1-r)
 \begin{pmatrix}
  1+2r&-2r\\
  r&1-r
 \end{pmatrix},
 \qquad
 N(r)=(1-r)
 \begin{pmatrix}
  1+2r&0\\
  r&1-2r
 \end{pmatrix},
\]

and let

\[
 w=(1,2).
\]

Direct multiplication gives the valid one-factor identity

\[
 \boxed{wN(r)=wM(r).}
\]

It does not imply preservation after composition.

## 2. Two-factor counterexample

For any `r,s in (0,1/2)`,

\[
 \boxed{
 wN(s)N(r)-wM(s)M(r)
 =\bigl(0,12rs(1-r)(1-s)\bigr).
 }
\]

Thus the load-bearing arbitrary-cascade sentence in the submitted
`L-91325-monotone-transport-disintegration-forgets-rough-colors.md` is false.
The review's instance `r=1/sqrt(67)`, `s=1/sqrt(71)` is hypothesis matching.

## 3. Simultaneous diagonalizations

The arithmetic matrices have the fixed diagonalization

\[
 M(r)=T
 \begin{pmatrix}1-r^2&0\\0&1-r\end{pmatrix}
 T^{-1},
 \qquad
 T=\begin{pmatrix}2&-1\\1&-1\end{pmatrix}.
\]

The completed matrices also have a fixed diagonalization.  Put

\[
 S=\begin{pmatrix}1&0\\1/4&1\end{pmatrix}.
\]

Then

\[
 \boxed{
 N(r)=S
 \begin{pmatrix}
  (1-r)(1+2r)&0\\
  0&(1-r)(1-2r)
 \end{pmatrix}
 S^{-1}.
 }
\]

Consequently both families commute internally, and arbitrary cascades can be
computed in closed form.

## 4. Closed-form cascade excess

Let `r_1,...,r_k in [0,1/2)` and define

\[
 B=\prod_i(1-r_i),
 \quad
 P_1=\prod_i(1+r_i),
 \quad
 P_+=\prod_i(1+2r_i),
 \quad
 P_-=\prod_i(1-2r_i).
\]

Then

\[
 w\prod_i M(r_i)
 =B\bigl(4P_1-3,\ 6-4P_1\bigr),
\]

while

\[
 w\prod_i N(r_i)
 =B\left(\frac{3P_+-P_-}{2},\ 2P_-\right).
\]

Therefore

\[
 \boxed{
 w\prod_iN(r_i)-w\prod_iM(r_i)
 =B\,(\Delta_L,\Delta_R),
 }
\]

where

\[
 \Delta_L=
 \frac{3P_+-P_-}{2}-4P_1+3,
\]

\[
 \Delta_R=
 2\bigl(P_-+2P_1-3\bigr).
\]

## 5. The excess is componentwise nonnegative

Let `e_j` be the elementary symmetric polynomial of degree `j` in the
`r_i`. Expanding the first coordinate gives

\[
 \Delta_L
 =\sum_{j\ge0}
 \left[
  \frac{3\,2^j-(-2)^j}{2}-4
 \right]e_j+3.
\]

The constant term and the coefficients for `j=1,2` vanish. For every `j>=3`
the coefficient is strictly positive. Hence

\[
 \boxed{\Delta_L\ge0.}
\]

For the second coordinate, set

\[
 F_k=P_-+2P_1-3.
\]

After adjoining one more factor `r`,

\[
 F_{k+1}-F_k
 =2r(P_1-P_-)
 \ge0,
\]

because each factor `1+r_i` is at least `1-2r_i`. Since `F_0=F_1=0`,

\[
 \boxed{\Delta_R\ge0.}
\]

Thus the failed completed cascade always **overestimates**, rather than
underestimates, both input-coordinate coefficients of the arithmetic SHARP row.
This favorable sign does not restore the claimed exact source partition.

## 6. No bounded scalar-port repair

Fix one `r in (0,1/2)` and repeat it `k` times. The first completed eigenvalue is

\[
 \alpha=(1-r)(1+2r)=1+r-2r^2>1.
\]

Hence

\[
 wN(r)^k
\]

has a component growing like `alpha^k`, whereas `M(r)` is a contraction in the
fixed Hilbert metric of `L-91326`. Therefore the cascade excess cannot be paid
by a uniformly bounded scalar endpoint port.

A correct continuation must retain an exact positive dilation of the arithmetic
state—such as the four-state semigroup of `L-91327`—or perform a proved reset
projection between factors. It cannot propagate the two-state completed matrix
`N(r)` itself.

## 7. Correct status

```text
one-factor SHARP preservation                 EXACT
arbitrary completed-cascade preservation       FALSE
closed-form cascade excess                     EXACT
cascade excess componentwise nonnegative       EXACT
bounded scalar repair of N-cascade             IMPOSSIBLE
positive four-state arithmetic semigroup       RETAINED
all-generation parity/endpoint projection      OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVEN
```
