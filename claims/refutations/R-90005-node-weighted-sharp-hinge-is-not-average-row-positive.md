# R-90005 — The node-weighted SHARP hinge is not average-row positive

Claim ID: `R-90005` (provisional range)  
Title: Multiplication of the square-root hinge by its carry coordinate destroys average-row positivity at endpoint 18  
Status: **EXACT FINITE REFUTATION — DIRECTED INTERVAL WITNESS**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Depends on: the average-carry inverse formula of `L-32303`; the derivative identity of `T-90009`  
Scope: refutes only the naive average-row lift from SHARP to the endpoint derivative; no refutation of general balanced-flow or cycle-corrected adapters

## 1. The tempting adapter

The parabolic endpoint seed satisfies

\[
 \mathcal D_Xb_X(q)
 =2\sqrt q-{2q\over\sqrt X}
 =2q\left(q^{-1/2}-X^{-1/2}\right).
\tag{R-90005.1}
\]

Thus it is the square-root SHARP hinge multiplied by the carry coordinate.
A tempting continuation is:

```text
h_T(q)=q^-1/2-T^-1/2 has nonnegative average-row inverse

therefore

g_T(q)=2q h_T(q) has nonnegative average-row inverse.
```

This implication is false.

## 2. Average-row inverse

Let

\[
 g_T(q)=2\sqrt q-{2q\over\sqrt T},
 \qquad1\le q\le T,
\tag{R-90005.2}
\]

and define its multiples-Mobius state

\[
 u_T(m)=\sum_{k\le T/m}\mu(k)g_T(mk).
\tag{R-90005.3}
\]

Let `a_T(j)` be the unique average-row inverse:

\[
 g_T(q)=\sum_{n=q}^{T}a_T(n)\beta_{nq}.
\tag{R-90005.4}
\]

The exact adjoint formula of `L-32303` gives

\[
\boxed{
 a_T(j)=
 { (j+1)[j u_T(j)-(j-2)u_T(j+1)]
   +2\sum_{m=j+2}^{T}u_T(m)
  \over j(j-1)}.
}
\tag{R-90005.5}
\]

No approximation enters this formula.

## 3. First mutation

At

\[
 T=18,\qquad j=3,
\]

a 70-digit directed interval evaluation of (R-90005.3)--(R-90005.5) gives

\[
\boxed{
 -0.016357533249176
 <a_{18}(3)
 <-0.016357533249175.
}
\tag{R-90005.6}
\]

Hence

\[
\boxed{a_{18}(3)<0.}
\tag{R-90005.7}
\]

This is the first endpoint mutation in the exact scan: all coefficients at
`3<=T<=17` are positive, while row three becomes negative at `T=18`.
The first-mutation assertion is finite reconnaissance; the single interval
(R-90005.6) is the proof object.

A larger-margin witness is

\[
\boxed{
 -0.385666938614629
 <a_{24}(4)
 <-0.385666938614628.
}
\tag{R-90005.8}
\]

## 4. Exact finite coefficient form at the first witness

For `T=18,j=3`, the adjoint is the finite functional

\[
\begin{aligned}
 a_{18}(3)={}&
 2g(3)-{2\over3}g(4)+{1\over3}g(5)-{5\over3}g(6)
 +{1\over3}g(7)+g(8)\\
 &-{5\over3}g(9)+{1\over3}g(11)+{2\over3}g(12)
 +{1\over3}g(13)-2g(15)\\
 &+{1\over3}g(17)+{5\over3}g(18).
\end{aligned}
\tag{R-90005.9}
\]

The last term vanishes because `g_18(18)=0`. Equation (R-90005.9) may be
verified using only rational arithmetic and directed square-root enclosures.

## 5. Consequence for the live endpoint route

The contact

\[
 \mathcal D_Xb_X(q)=2q h_X(q)
\]

is exact and remains strategically useful. But the node multiplier `q` is not a
positive endomorphism of the average-carry cone.

Therefore none of the following is valid without an additional theorem:

```text
SHARP -> derivative-seed average-row positivity;
SHARP -> endpoint monotonicity;
positive hinge inverse -> positive node-weighted hinge inverse.
```

A successful bridge may still use:

1. Pascal-cycle changes of the split representation;
2. a non-average balanced flow;
3. a coupled source which combines the weighted hinge with the prime-power
   moat before taking a sign;
4. the weighted-Chebyshev barrier of `T-90009` directly.

Those possibilities are not refuted.

## 6. Proof boundary

Refuted exactly:

- preservation of average-row positivity under the column multiplier `q`;
- the naive direct lift from SHARP to the endpoint derivative seed.

Retained:

- the exact derivative/hinge identity;
- SHARP itself;
- cycle-corrected or general balanced-flow adapters;
- endpoint monotonicity as an open RH-sufficient gate;
- RH, which remains unproved.

Replay: `experiments/X-90013-node-weighted-hinge/verify.py`.
