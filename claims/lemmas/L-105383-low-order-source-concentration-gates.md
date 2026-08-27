# L-105383 — Low-order Xi source positivity follows from two explicit concentration ratios

Claim ID: `L-105383`  
Status: **PROVED EXACT IMPLICATION THEOREM — XI CONCENTRATION ESTIMATES OPEN**  
Created: 2026-08-23  
Depends on: `L-105380`, `L-105381`  
RH status: **not assumed**

## 1. Odd derivatives: one fourth-moment ratio pays both order-two blocks

Use the odd tilted law of `L-105380`. Put

\[
x=\mathbb E[X]>0,
\qquad
q={\mathbb E[X^2]\over\mathbb E[X]^2},
\qquad
r_3={\mathbb E[X^3]\over\mathbb E[X]^3}.
\tag{L-105383.1}
\]

Moment log-convexity gives

\[
\boxed{r_3\ge q^2.}
\tag{L-105383.2}
\]

Indeed, Cauchy--Schwarz applied to `X^(1/2)` and `X^(3/2)` gives
`E[X^2]^2<=E[X]E[X^3]`.

The unshifted order-two source determinant is

\[
\det\mathsf A_2^{(0)}
={x^2\over90}(5-3q).
\tag{L-105383.3}
\]

The shifted determinant is

\[
\det\mathsf A_2^{(1)}
={x^4\over37800}
\left(35q+15r_3-42q^2\right).
\tag{L-105383.4}
\]

Using (L-105383.2),

\[
35q+15r_3-42q^2
\ge q(35-27q).
\tag{L-105383.5}
\]

Therefore

\[
\boxed{
q\le{35\over27}
\Longrightarrow
\mathsf A_2^{(0)}\succeq0
\quad\text{and}\quad
\mathsf A_2^{(1)}\succeq0.
}
\tag{L-105383.6}
\]

The bound also implies `q<5/3`, so the unshifted determinant has strict margin
unless the endpoint degeneracy is reached through another zero pivot.

Equivalently, it is enough that

\[
\boxed{
{\operatorname{Var}(X)\over\mathbb E[X]^2}
\le{8\over27}.
}
\tag{L-105383.7}
\]

This is a single coefficient-of-variation estimate for the positive tilted Xi
law.

## 2. Even derivatives: one reciprocal concentration ratio pays both order-one pivots

Use the even tilted law of `L-105381` and put

\[
\alpha=\mathbb E[X]\mathbb E[X^{-1}],
\qquad
q={\mathbb E[X^2]\over\mathbb E[X]^2}.
\tag{L-105383.8}
\]

Both satisfy `alpha>=1` and `q>=1`. The two regularized order-one source
coefficients are

\[
a_0^{\rm ev}={3-\alpha\over6},
\tag{L-105383.9}
\]

and

\[
a_1^{\rm ev}
={\mathbb E[X]\over360}
\left(15-10\alpha+3\alpha q\right).
\tag{L-105383.10}
\]

Since `q>=1`,

\[
15-10\alpha+3\alpha q
\ge15-7\alpha.
\]

Hence

\[
\boxed{
\alpha\le{15\over7}
\Longrightarrow
\mathsf A_1^{(0)}\succeq0
\quad\text{and}\quad
\mathsf A_1^{(1)}\succeq0.
}
\tag{L-105383.11}
\]

The same hypothesis automatically gives `alpha<3`, paying the first pivot.
Thus one reciprocal-moment concentration estimate controls both even
order-one source reserves.

## 3. Strict high-concentration margins

If the normalized tilted laws converge in moments to a point mass, then

\[
q\to1,
\qquad
r_3\to1,
\qquad
\alpha\to1.
\]

The limiting determinant factors are

\[
5-3q\to2,
\qquad
35q+15r_3-42q^2\to8,
\]

and the even coefficients converge to

\[
a_0^{\rm ev}\to{1\over3},
\qquad
a_1^{\rm ev}/\mathbb E[X]\to{1\over45}.
\]

Thus the trigonometric point-mass cone of `L-105382` has strict finite-order
source margins. The unresolved issue is proving the required concentration
uniformly in the actual Xi derivative tail.

## 4. Source matrices versus boundary capacity

The conclusions above concern only the fixed source matrices. To obtain a
boundary matrix one must still prove the critical atomic domination

\[
\mathsf C_{k,\Omega}^{(a)}
\preceq
\mathsf A_k^{(a)}.
\]

At order one this becomes the explicit residue capacities of
`L-105380--L-105381`. At order two it remains an operator inequality even after
source positivity is known.

## 5. Scope

The constants `35/27` and `15/7` are convenient sufficient thresholds, not
claimed sharp for Xi. Positivity of the Fourier kernel alone does not imply
either threshold; broad positive distributions violate them. No all-order
source theorem, critical capacity theorem, low-order descent or RH conclusion
is proved.
