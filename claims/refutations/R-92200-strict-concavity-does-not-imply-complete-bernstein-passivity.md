# R-92200 — Strict concavity does not imply complete-Bernstein passivity

Claim ID: `R-92200`  
Status: **EXACT RATIONAL HIGH-ORBIT FIREWALL**  
Created: 2026-08-14  
Depends on: `L-92100/L-92101`; `T-92200`  
RH status: **unproved**

## 1. A verified-anchor-shaped control

Take

\[
 B=1000,
 \qquad
 a=\frac25,
 \qquad
 r_0=\frac{B^2}{4}=250000,
\]

and define the positive safe admittance

\[
\boxed{
 p_B(t)
 =\frac2{t+r_0}
  +\frac{4(t+B^2-a^2)}
  {(t+B^2-a^2)^2+(2aB)^2}.
 }
\tag{R-92200.1}
\]

It is the squared-pole model consisting of:

```text
one lower real critical anchor of weight 2;
one high conjugate off-line pair, each pole of weight 2.
```

Put

\[
 Z_B(t)=\frac1{p_B(t)}.
\]

The height separation satisfies the same coarse domination inequality used in
`L-92201`:

\[
 B^2>2160\log(B+3).
\]

## 2. Every scalar/order-three shadow passes

Exact simplification gives

\[
 Z_B''(t)
 =-\frac{800\,P(t)}{Q(t)^3},
\]

where `Q(t)>0` for `t>0` and

\[
\begin{aligned}
P(t)={}&343321435546890625t^3\\
&+1029967657470632812492500t^2\\
&+1029969030762026367221250001200t\\
&+343323138427858398437343748599999936.
\end{aligned}
\]

Every coefficient is positive.  Therefore

\[
 \boxed{Z_B''(t)<0\qquad(t>0).}
\]

The same model has `Z_B'(t)>0`, and its conjugate impedance
`t/Z_B(t)=t p_B(t)` has the monotonicity/concavity signs occurring in the
one-, two-, and three-node Caratheodory shadows.

Thus ordinary scalar passivity and the complete order-three conclusion of
`T-92200` do not force the all-order network property.

## 3. Exact higher-Loewner failure

Form the three-node Loewner matrix of `Z_B` at

\[
 t_1=\frac14,
 \qquad
 t_2=600000,
 \qquad
 t_3=600000000.
\]

Its entries are

\[
 L_{ii}=Z_B'(t_i),
 \qquad
 L_{ij}=\frac{Z_B(t_i)-Z_B(t_j)}{t_i-t_j}.
\]

Direct rational simplification gives

\[
\boxed{
\det L
=-\frac{
121963925874180597805406777183433564656326573094570826250190338142395019531250000000000000
}{
1902244056492281038040828852656511743924817971347701869400802989494251324696057698781162756917531329
}<0.
}
\tag{R-92200.2}
\]

Hence `Z_B` is not matrix monotone of order three and is not a complete
Bernstein function, despite strict ordinary concavity.

## 4. Meaning for the zeta programme

The verified critical reserve can close the first nontrivial scalar curvature
of the actual Xi impedance.  It does not automatically synthesize the full
positive Krein string.

The next genuine level is not another scalar derivative sign.  It is a
matrix-order statement, for example:

\[
 \boxed{
 \left(
 \frac{Z(t_i)-Z(t_j)}{t_i-t_j}
 \right)_{i,j=1}^3\succeq0
 }
\]

on every safe packet, with diagonal derivatives.

Any claimed passage

```text
Z increasing + Z concave + conjugate shadows
    =>
Z complete Bernstein
```

is therefore invalid.

## 5. Exact boundary

```text
real anchor plus high off-line pair                  EXACT
Z increasing and strictly concave                    EXACT
all low scalar shadows                               PASS
three-node Loewner determinant                       STRICTLY NEGATIVE
ordinary concavity -> complete Bernstein             REFUTED
actual-Xi three-node Loewner positivity              OPEN
all-order Xi passive string                          OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
