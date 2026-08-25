# L-103007 — Every symmetric Plücker rectangle has positive ordered Euler activity

Claim ID: `L-103007`  
Status: **PROVED EXACT SCALAR-CARRIER THEOREM**  
Created: 2026-08-25  
Depends on: `L-103006`; PR #730 `T-105440.6`  
RH status: **not assumed**

Take four ordered labels

\[
1<2<i<j
\]

inside one squarefree occurrence. Let their scalar activities satisfy

\[
1>a\ge b\ge c\ge d>0.
\]

Let

\[
A=\prod_{2<t<i}(1-x_t),
\qquad
B=\prod_{i<t<j}(1-x_t),
\]

so `0<A,B<=1`. The extreme-pair edge weights are

\[
\begin{aligned}
q_{12}&=ab,\\
q_{1i}&=ac(1-b)A,\\
q_{2i}&=bcA,\\
q_{1j}&=ad(1-b)A(1-c)B,\\
q_{2j}&=bdA(1-c)B,\\
q_{ij}&=cdB.
\end{aligned}
\tag{L-103007.1}
\]

The symmetric rectangle of `L-103006` is

\[
\mathscr R
=2q_{12}+2q_{ij}-q_{1i}-q_{1j}-q_{2i}-q_{2j}.
\]

Put

\[
S=a+b-ab.
\]

Then

\[
\boxed{
\mathscr R
=2ab+2cdB-SA[c+d(1-c)B].
}
\tag{L-103007.2}
\]

Since `A<=1`,

\[
\mathscr R
\ge
2ab-Sc+Bd[2c-S(1-c)].
\tag{L-103007.3}
\]

## Case 1: `2c-S(1-c)>=0`

The last term is nonnegative, while

\[
2ab-Sc
\ge
c(2a-S)
=c(a-b+ab)
\ge0.
\]

## Case 2: `2c-S(1-c)<0`

Because `Bd<=c`, multiplication by the negative bracket gives

\[
Bd[2c-S(1-c)]
\ge
c[2c-S(1-c)].
\]

Therefore

\[
\mathscr R
\ge
f(c)
:=2ab-2Sc+(2+S)c^2.
\]

The convex quadratic has minimizer

\[
c_*={S\over2+S}.
\]

If `c_*>=b`, then `f` is decreasing on `[0,b]` and

\[
f(c)\ge f(b)
=b^2(3a+b-ab)>0.
\]

If `c_*<b`, then

\[
f(c)\ge f(c_*)
=2ab-{S^2\over2+S}.
\]

But `c_*<b` gives

\[
{S^2\over2+S}<Sb,
\]

and `S=a+b-ab<=2a`, so `Sb<=2ab`. Hence `f(c_*)>0`.

Thus in every case

\[
\boxed{\mathscr R>0.}
\tag{L-103007.4}
\]

## Consequence for the cycle carrier

`L-103006` expresses the complete row-zero cycle as a positive average of the rectangles `mathscr R`. Therefore its scalar ordered-activity carrier is nonnegative for every decreasing prime-activity sequence, including the literal values `p^{-1/2}` and every homogeneous-carrier specialization produced by the common source algebra.

The conclusion-facing cycle may therefore be centered by subtracting a favorable deterministic carrier. Only the translation-dependent physical fluctuation can remain adverse.

This theorem is scalar. It does not assert positivity after replacing the activities by distinct multiplicative shift operators; that firewall is recorded in `R-103001`.