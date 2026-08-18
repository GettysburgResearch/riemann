# L-98002 — A positive squarefree shell forces the eventual Lorenz marginal to zero

Claim ID: `L-98002`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Depends on: `L-98000/L-98001`; classical PNT and squarefree density  
RH status: **not assumed**

Use the weighted target coordinates

\[
t_X(k)={1\over\sqrt k}T(X/k)
       ={4\sqrt X\over k}-{3\over\sqrt k}
\qquad(k\le X).
\tag{L-98002.1}
\]

Let

\[
T_O(X)=\sum_{\substack{k\le X\\\mu(k)=-1}}t_X(k)
\]

be the complete odd target demand, and let

\[
T_{E,+}(X)=
\sum_{\substack{k<X/2\\\mu(k)=+1}}t_X(k)
\tag{L-98002.2}
\]

be the target mass of the even atoms with strictly positive scalar coordinate.
The condition `k<X/2` is exact because `Q_*(X/k)>0` exactly when `X/k>2`.

Then

\[
\boxed{
T_O(X)-T_{E,+}(X)
=
{3\over\pi^2}
\left(4\log2+3\sqrt2-6\right)\sqrt X
+o(\sqrt X).
}
\tag{L-98002.3}
\]

Since

\[
4\log2+3\sqrt2-6>0,
\tag{L-98002.4}
\]

we have

\[
\boxed{T_O(X)>T_{E,+}(X)}
\tag{L-98002.5}
\]

for every sufficiently large real `X`.

## Proof

For a squarefree integer,

\[
\mathbf1_{\mu=-1}={\mu^2-\mu\over2},
\qquad
\mathbf1_{\mu=+1}={\mu^2+\mu\over2}.
\]

Therefore, up to the harmless single boundary index at `X/2`,

\[
\begin{aligned}
2[T_O(X)-T_{E,+}(X)]
={}&
\sum_{X/2\le k\le X}\mu(k)^2t_X(k)\\
&-\sum_{k\le X}\mu(k)t_X(k)
-\sum_{k<X/2}\mu(k)t_X(k).
\end{aligned}
\tag{L-98002.6}
\]

The prime number theorem in Möbius form gives

\[
\sum_{k\le y}{\mu(k)\over k}=o(1),
\qquad
\sum_{k\le y}{\mu(k)\over\sqrt k}=o(\sqrt y).
\tag{L-98002.7}
\]

Using (L-98002.1), both signed sums on the right of (L-98002.6) are
`o(sqrt(X))`.

For the squarefree shell, the standard density theorem

\[
\sum_{k\le y}\mu(k)^2={6\over\pi^2}y+O(\sqrt y)
\]

and partial summation give

\[
\begin{aligned}
{1\over\sqrt X}
\sum_{X/2\le k\le X}\mu(k)^2t_X(k)
&\longrightarrow
{6\over\pi^2}
\int_{1/2}^{1}
\left({4\over u}-{3\over\sqrt u}\right)\,du\\
&={6\over\pi^2}
\left(4\log2+3\sqrt2-6\right).
\end{aligned}
\tag{L-98002.8}
\]

Combining (L-98002.6)--(L-98002.8) proves (L-98002.3).

For positivity of the constant, the elementary integral bound `log 2>1/2`
and `sqrt(2)>4/3` give

\[
4\log2+3\sqrt2-6
>2+4-6=0.
\]

## Interpretation

At large endpoints, the odd demand lies beyond the total target capacity of all
even atoms carrying positive scalar. Therefore, whenever total target capacity
is available, the fractional-knapsack optimizer must use every positive-scalar
even atom and complete the target using zero-scalar atoms from the shell
`X/2<=k<=X`. Its marginal scalar price is exactly `lambda=0`.

The result is unconditional because the positive squarefree shell has a main
term of order `sqrt(X)` while the two Möbius-signed corrections are `o(sqrt(X))`.
It does not prove total target capacity or the signed scalar.