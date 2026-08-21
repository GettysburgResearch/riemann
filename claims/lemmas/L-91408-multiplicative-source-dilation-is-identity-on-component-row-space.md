# L-91408 — Multiplicative source dilation is the identity map on component-row coordinates

Claim ID: `L-91408`  
Status: **PROVED EXACT SOURCE/ROW INTERTWINING THEOREM**  
Created: 2026-08-13  
Frozen source partition: PR `#399` at `e210d06a588b191f102345ec75f2a0efce1b1650` (`L-91402/L-91404`)  
Depends on: the literal source kernels `L-91339`; the exact component-row atom `L-91341.11`; linear ordinary/radix-four response maps  
Supersedes in this source-dilated setting: the affine row lift refuted by `R-91403/R-91558`  
RH status: **unproved**

## 1. Source and row coordinates are different variables

Let `k` denote a squarefree arithmetic source index and let `j>=2` denote a
component-row coordinate.  For constants `a,b>=0`, put

\[
 K_{a,b}(X,k)
 =a\frac{\sqrt X}{k}-b\frac1{\sqrt k}.
 \tag{L-91408.1}
\]

The SHARP target and endpoint-score kernels are

\[
 W_\Psi=K_{4,3},
 \qquad
 W_S=K_{5,3}.
 \tag{L-91408.2}
\]

The literal component-row atom attached to source `k` is

\[
 \boxed{
 \mathcal R_X(k;j)
 =k^{-1/2}Q_{X/k}(j).
 }
 \tag{L-91408.3}

The row coordinate `j` is not the source index `k`.  Multiplying a source by an
integer does not require multiplying or translating `j`.

## 2. Exact multiplicative covariance

Fix an integer `m>=1` and put

\[
 Y=X/m.
 \tag{L-91408.4}
\]

For every active source `k<=Y`, direct algebra gives

\[
 \boxed{
 K_{a,b}(X,mk)
 =m^{-1/2}K_{a,b}(Y,k).
 }
 \tag{L-91408.5
}

Indeed,

\[
 a\frac{\sqrt X}{mk}-b\frac1{\sqrt{mk}}
 =m^{-1/2}
  \left(a\frac{\sqrt{X/m}}k-b\frac1{\sqrt k}\right).
\]

The component row has the identical covariance:

\[
 \boxed{
 \mathcal R_X(mk;j)
 =m^{-1/2}\mathcal R_Y(k;j)
 \qquad(j>=2).
 }
 \tag{L-91408.6}

This follows because

\[
 \frac X{mk}=\frac Yk.
\]

Thus multiplication of the arithmetic source changes only the scalar source
coefficient.  It acts as the identity on the complete finite row vector.

## 3. Positive measure and labelled-pair version

Let `nu` be a finite positive source measure and let `D_m nu` be its
multiplicative pushforward,

\[
 (D_m\nu)(mk)=\nu(k).
 \tag{L-91408.7}
\]

Equations (L-91408.5)--(L-91408.6) give

\[
 \boxed{
 \mathfrak K_X(D_m\nu)
 =m^{-1/2}\mathfrak K_Y(\nu),
 }
 \tag{L-91408.8}
\]

and, coefficientwise in `j`,

\[
 \boxed{
 R_X(D_m\nu)
 =m^{-1/2}R_Y(\nu).
 }
 \tag{L-91408.9}

The statement remains true after:

```text
swapping even/odd parity coordinates;
retaining balanced/reserve channel labels;
taking positive direct sums;
applying any fixed linear target or score functional.
```

These operations act on labels and coefficients, while (L-91408.6) acts on the
arithmetic source index.

## 4. Physical response needs no lift

Let `C` be the ordinary carry response and let `D_4C` be the radix-four detail
response.  Both act linearly on the row coordinate `j` and are independent of
the arithmetic source label.  Therefore

\[
 \boxed{
 C[R_X(D_m\nu)]
 =m^{-1/2}C[R_Y(\nu)],
 }
 \tag{L-91408.10}
\]

\[
 \boxed{
 \mathcal D_4C[R_X(D_m\nu)]
 =m^{-1/2}\mathcal D_4C[R_Y(\nu)].
 }
 \tag{L-91408.11}

Suppose `d_Y>=0` is feasible for the scaled child packet
`m^{-1/2}\nu` at endpoint `Y`.  Regard the same coefficient vector `d_Y` as a
row in the parent row space.  Equations (L-91408.9)--(L-91408.11) show that it
consumes no more than the exact parent capacity assigned to the source packet
`D_m\nu`.

No map of the form

\[
 j\mapsto m(j+1)-1
\]

appears.  Consequently there are no matched or unmatched physical fibers.

## 5. Source-disjoint packet assembly

Assume an exact source identity

\[
 \boxed{
 P_X=F_X+\sum_b c_bD_{m_b}P_b,
 \qquad
 c_b=m_b^{-1/2},
 \qquad
 Y_b=X/m_b.
 }
 \tag{L-91408.12}

Apply the literal target, score and row maps.  Equations
(L-91408.8)--(L-91408.9) give the simultaneous identities

\[
 \boxed{
 T_X(P_X)=T_X(F_X)+\sum_bc_bT_{Y_b}(P_b),
 }
 \tag{L-91408.13}
\]

\[
 \boxed{
 S_X(P_X)=S_X(F_X)+\sum_bc_bS_{Y_b}(P_b),
 }
 \tag{L-91408.14}
\]

\[
 \boxed{
 R_X(P_X)=R_X(F_X)+\sum_bc_bR_{Y_b}(P_b).
 }
 \tag{L-91408.15}

Let `d_F` be feasible for the finite packet and let `d_b` be feasible for the
unscaled child `P_b`.  Then

\[
 \boxed{
 d_X=d_F+\sum_bc_bd_b
 }
 \tag{L-91408.16}

is a nonnegative parent row.  By (L-91408.15) and linearity of every physical
response, it is feasible for the parent whenever the finite and child packings
are feasible for their corresponding exact source shares.

## 6. Exact score-deficit recurrence

Let `Delta_Z(P)` denote declared endpoint score minus the best feasible row
score for packet `P` at endpoint `Z`.  Positive homogeneity and
(L-91408.14)--(L-91408.16) give

\[
 \boxed{
 \Delta_X(P_X)
 \le\Delta_X(F_X)
  +\sum_bc_b\Delta_{Y_b}(P_b).
 }
 \tag{L-91408.17}

If

\[
 \Delta_X(F_X)\le C m(F_X)
 \tag{L-91408.18}
\]

and the source mass in (L-91408.12) satisfies

\[
 m(F_X)+\sum_bc_bm(P_b)=m(P_X),
 \tag{L-91408.19}
\]

then

\[
 \boxed{
 \Delta_X(P_X)
 \le C m(P_X)+\sum_bc_b\Delta_{Y_b}(P_b).
 }
 \tag{L-91408.20}

This is a packet-envelope recurrence with the actual source coefficients.

## 7. Application to `L-91404`

Every child in the finite-block expansion of `L-91404` has

\[
 m_b=dp,
 \qquad
 c_b=(dp)^{-1/2},
 \qquad
 Y_b=X/(dp),
 \tag{L-91408.21}
\]

and is precisely a multiplicatively pushed source packet.  Therefore Sections
2--6 apply directly.  The affine Pascal sentence in `L-91404.5` is unnecessary
and must not be used.

The complete finite forcing packet remains at the parent endpoint.  Its signed
finite source-to-row realization is the separate finite theorem
`L-91340/L-91341`; it is not obtained by this source covariance.

## 8. Boundary

```text
source-kernel multiplicative covariance              EXACT
component-row multiplicative covariance               EXACT
identity on every row coordinate                      EXACT
ordinary/radix-four response covariance               EXACT
source-disjoint child packing assembly                EXACT
actual-coefficient score recurrence                   EXACT CONDITIONAL
finite forcing positive row/score realization         IMPORTED / REPLAY
packet mass normalization                              IMPORTED / REPLAY
root endpoint implication                              IMPORTED / REPLAY
Riemann Hypothesis                                     UNPROVEN
```
