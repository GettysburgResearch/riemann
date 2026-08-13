# L-92201 — Order four is a pair of `2 x 2` curvature determinants

Claim ID: `L-92201`  
Status: **PROVED EXACT DIVIDED-DIFFERENCE REDUCTION**  
Created: 2026-08-13  
Depends on: `L-92200`  
RH status: **unproved**

## 1. Order-four factors

For

\[
 0<t_1<t_2<t_3<t_4,
 \qquad
 p_i=p(t_i),
\]

`L-92200` gives

\[
 \det H
 =\frac{A_4B_4}{\Delta_+(x)^2},
 \tag{L-92201.1}
\]

where

\[
 A_4=\det[1,t,p,tp]_{t=t_i},
 \qquad
 B_4=\det[1,t,tp,t^2p]_{t=t_i}.
 \tag{L-92201.2}

## 2. Newton reduction

Let

\[
 \Delta(t)=\prod_{i<j}(t_j-t_i)>0.
\]

For any two functions `f,g`, the Newton divided-difference transform gives

\[
\boxed{
\begin{aligned}
 \det[1,t,f,g]_{t=t_i}
 =\Delta(t)
 \det\begin{pmatrix}
  [t_1,t_2,t_3]f &[t_1,t_2,t_3]g\\
  [t_1,t_2,t_3,t_4]f &[t_1,t_2,t_3,t_4]g
 \end{pmatrix}.
\end{aligned}}
\tag{L-92201.3}

Therefore

\[
\boxed{
 A_4=\Delta(t)
 \det\begin{pmatrix}
  [123]p &[123](tp)\\
  [1234]p &[1234](tp)
 \end{pmatrix},
}
\tag{L-92201.4}

and

\[
\boxed{
 B_4=\Delta(t)
 \det\begin{pmatrix}
  [123](tp) &[123](t^2p)\\
  [1234](tp) &[1234](t^2p)
 \end{pmatrix}.
}
\tag{L-92201.5}

Here `[123]` and `[1234]` denote the corresponding second and third divided
differences.

The first open order is therefore not one `4 x 4` sign.  It is the product of
two `2 x 2` signs in the interlacing string

\[
 p,\quad tp,\quad t^2p.
\]

## 3. Confluent limit

When all four nodes coalesce at `t`, the two reduced determinants tend, up to
the common positive factor `1/12`, to

\[
\boxed{
 \mathfrak A_4(t)
 =p''(tp)'''-p'''(tp)''
 =3(p'')^2-2p'p''',
}
\tag{L-92201.6
}

and

\[
\boxed{
\begin{aligned}
 \mathfrak B_4(t)
 ={}&(tp)''(t^2p)'''-(tp)'''(t^2p)''\\
 ={}&-2t^2p'p'''+3t^2(p'')^2
 -2tpp'''+6tp'p''\\
 &-6pp''+12(p')^2.
\end{aligned}}
\tag{L-92201.7
}

Thus a local order-four failure appears when these two generalized curvatures
have opposite signs.

## 4. Stieltjes reading

Under RH,

\[
 p(t)=\int_0^\infty\frac{d\mu(r)}{t+r}.
\]

Write

\[
 M_k(t)=\int_0^\infty\frac{d\mu(r)}{(t+r)^k}.
\]

Then

\[
 p=M_1,
 \quad p'=-M_2,
 \quad p''=2M_3,
 \quad p'''=-6M_4.
\]

The first local factor becomes

\[
 \boxed{
 \mathfrak A_4
 =12(M_3^2-M_2M_4)\le0
 }
\tag{L-92201.8}

by moment log-convexity.

The second is

\[
\boxed{
\begin{aligned}
 \mathfrak B_4
 =-12\{&M_1M_3-M_2^2
 +t(-M_1M_4+M_2M_3)\\
 &+t^2(M_2M_4-M_3^2)\}\le0,
\end{aligned}}
\tag{L-92201.9}

where the bracket is the corresponding `[0,\infty)` localizing Gram
determinant.  Hence the two factors have the same sign under RH.

## 5. New order-four target

For the actual Xi function, order four reduces to proving the finite-node sign
regularity

\[
 \boxed{
 A_4\le0,
 \qquad
 B_4\le0
 }
 \tag{L-92201.10}

for every safe quadruple, or an equivalent statement that their product is
nonnegative together with the already-proved lower-order minors.

The verified-line reserve method on PR #446 suggests pairing each hypothetical
high off-line orbit with **two** low critical-line orbit directions.  That
construction remains open.

## 6. Exact boundary

```text
order-four 4 x 4 determinant                FACTORED EXACTLY
first alternant -> 2 x 2 divided differences EXACT
second alternant -> 2 x 2 divided differences EXACT
confluent Wronskians                         EXACT
RH/Stieltjes signs                           STANDARD
actual-Xi order-four signs                   OPEN
Riemann Hypothesis                           UNPROVED
```
