# R-96100 — L-94200 conflates two rows, and its fixed-product FRONTIER-CHAIN cannot supply logarithmic transport

Claim ID: `R-96100`  
Status: **EXACT REFUTATION OF THE PUBLISHED PROOF; DISCRETE-TAIL POSITIVITY REMAINS OPEN**  
Created: 2026-08-16  
Frozen parent: PR #542 at `ca5fb69c15cda29b3b589660f9be44ea2f440677`  
Affected source: PR #537, `L-94200` at `2c2d4dd834ee61c54a6f8bdd7ba204a01896d593`  
RH status: **unproved**

## 1. Two different row families were identified as one

The parabolic endpoint family used on the `L-94100` line is

\[
 b_Y^{\rm par}(m)
 =2\sqrt m\left[
   \log\frac Ym-2\left(1-\sqrt{\frac mY}\right)
 \right]\mathbf 1_{m\le Y},
\]

\[
 A_Y^{\rm par}(m)=\frac{b_Y^{\rm par}(m)}{m-1},
 \qquad
 D_Y(j)=(j+1)\Delta_j^2A_Y^{\rm par}(j).
\tag{R-96100.1}
\]

This is a local three-node second difference: for fixed `j`, only the entries
`m=j,j+1,j+2` occur.

The row consumed by PR #542 is instead the discrete-tail family

\[
 T_Y(m)=
 \sum_{n=m}^{\lfloor Y\rfloor}
 \frac1{\sqrt n}\log\frac Yn,
 \qquad
 A_Y^{\rm tail}(m)=\frac{T_Y(m)}{m-1},
\]

\[
 Q_Y^{\rm tail}(j)
 =(j+1)\Delta_j^2A_Y^{\rm tail}(j).
\tag{R-96100.2}
\]

Expanding the three tail sets gives exactly

\[
 Q_Y^{\rm tail}(j)
 =\frac{A_j}{\sqrt j}\log\frac Yj\,\mathbf1_{Y\ge j}
 -\frac{B_j}{\sqrt{j+1}}\log\frac Y{j+1}\,\mathbf1_{Y\ge j+1}
 +C_j\sum_{n\ge j+2}\frac1{\sqrt n}
   \log\frac Yn\,\mathbf1_{Y\ge n},
\tag{R-96100.3}
\]

where

\[
 A_j=\frac{j+1}{j-1},\qquad
 B_j=\frac{(j+1)(j-2)}{j(j-1)},\qquad
 C_j=\frac2{j(j-1)}.
\]

Thus the infinite-tail formula in `L-94200.6` comes from (R-96100.2), not
from the parabolic expression (R-96100.1).

The difference is already strict at

\[
 Y=5,\qquad j=2.
\]

A rational directed enclosure gives

\[
 0.961804605140695709815227351637
 <D_5(2)<
 0.961804605140695709815227351638,
\]

whereas

\[
 2.055317945796903836581139290740
 <Q_5^{\rm tail}(2)<
 2.055317945796903836581139290741.
\]

In particular,

\[
 \boxed{D_5(2)\ne Q_5^{\rm tail}(2).}
\tag{R-96100.4}
\]

There is also an asymptotic separation. For fixed `j`, the local parabolic row
is `O_j(log Y)`, while the positive tail in (R-96100.3) is `asymp_j sqrt(Y)`.
The two families cannot agree after a notational correction.

Therefore the implication

```text
parabolic endpoint atom theorem
    -> row formula L-94200.6
```

is false.

## 2. The fixed-product FRONTIER-CHAIN has no distinct logarithmic positions

Keeping the discrete-tail row, write

\[
 G_j(Y)=\sqrt Y\,Q_Y^{\rm tail}(j)
       =\sum_{m\ge1}q_j(m)\Psi(Y/m),
\]

with

\[
 \Psi(u)=\sqrt u\log u\,\mathbf1_{u\ge1}
\]

and

\[
 q_j(m)=
 \begin{cases}
 0,&m<j,\\
 A_j,&m=j,\\
 -B_j,&m=j+1,\\
 C_j,&m\ge j+2.
 \end{cases}
\]

For a finite prime product `P`, the exact grouped expansion is

\[
 \sum_{d\mid P}\mu(d)G_j(Y/d)
 =\sum_{n\ge1}\omega_{P,j}(n)\,
   \mathcal K_{\log Y}(\log n),
\]

\[
 \omega_{P,j}(n)
 =\sum_{d\mid(n,P)}\mu(d)q_j(n/d),
 \qquad
 \mathcal K_x(t)=e^{(x-t)/2}(x-t)_+.
\tag{R-96100.5}
\]

For a fixed product `n=dm`, every divisor-cube vertex in the inner sum of
(R-96100.5) is evaluated at the same knot `log n`. Such vertices do not bracket
one another in logarithmic position.

The obstruction is visible in the smallest nontrivial fixture:

\[
 P=2,\qquad j=2,\qquad n=4.
\]

Here `A_2=3`, `C_2=1`, and

\[
 \boxed{
 \omega_{2,2}(4)=q_2(4)-q_2(2)=1-3=-2.
 }
\tag{R-96100.6}
\]

Both terms in (R-96100.6) multiply exactly
`\mathcal K_x(\log4)`. A convex packet needs distinct knots
`a<b<c`; no within-`n` logarithmic packet exists.

Consequently the statements in `L-94200` that the transport

```text
never combines different products n
```

and simultaneously uses adjacent atoms that bracket the shoulder in logarithmic
position are incompatible with the displayed grouped formula.

## 3. Correct boundary

The refutation proves:

```text
parabolic row = discrete-tail row                  FALSE
fixed-product cube gives distinct log positions    FALSE
within-n convex FRONTIER-CHAIN                      FALSE
universal discrete-tail sieve positivity            NOT REFUTED
cross-n/global reservoir transport                  REQUIRED / OPEN
PR #542 Mellin-Landau consumer                      CONDITIONAL ON THAT OPEN THEOREM
Riemann Hypothesis                                  UNPROVED
```

The exact directed replay is `X-96100`.
