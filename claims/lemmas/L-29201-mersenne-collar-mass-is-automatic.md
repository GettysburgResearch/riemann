# L-29201 — The Mersenne collar mass is automatic

Claim ID: `L-29201`  
Title: Every nonnegative carry sub-saturation already has logarithmic total parent mass on the Mersenne rows  
Status: **PROPOSED COMPLETE EXACT LEMMA — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #285 `T-28001`; the diagonal carry coefficient `chi_(n,n)(j)=1`  
Scope: removes the separate asymptotic collar condition from MCF; it does not construct the support-feasible flow

## 1. Parent mass and a diagonal carry column

Let

\[
d(n,j)\ge0,
\qquad 2\le n\le X,\quad 1\le j<n,
\]

be any nonnegative split flow.  Put

\[
P_d(n)=\sum_{j=1}^{n-1}d(n,j).
\tag{L-29201.1}
\]

For every nontrivial split of the parent `n`,

\[
\chi_{n,n}(j)
=\left\lfloor\frac nn\right\rfloor
 -\left\lfloor\frac jn\right\rfloor
 -\left\lfloor\frac{n-j}{n}\right\rfloor
=1.
\tag{L-29201.2}
\]

Every carry coefficient is nonnegative.  Therefore the complete load in column
`q=n` satisfies

\[
L_n(d)
:=\sum_{m=n}^{X}\sum_{j=1}^{m-1}
 d(m,j)\chi_{m,n}(j)
\ge P_d(n).
\tag{L-29201.3}
\]

Consequently, for every nonnegative **sub-saturation**

\[
L_q(d)\le w_X(q)
=q^{-1/2}\log(X/q),
\qquad2\le q\le X,
\tag{L-29201.4}
\]

one has the pointwise parent bound

\[
\boxed{
P_d(n)\le n^{-1/2}\log(X/n).
}
\tag{L-29201.5}
\]

No support condition, Möbius estimate, or prime estimate is used.

## 2. Mersenne collar

Let

\[
\mathcal M_X=
\sum_{2^r-1\le X}P_d(2^r-1),
\qquad r\ge2.
\tag{L-29201.6}
\]

Since

\[
2^r-1\ge2^{r-1},
\]

(L-29201.5) gives

\[
\begin{aligned}
\mathcal M_X
&\le
\log X
\sum_{r\ge2}(2^r-1)^{-1/2}\\
&\le
\log X
\sum_{r\ge2}2^{-(r-1)/2}\\
&=(1+\sqrt2)\log X.
\end{aligned}
\tag{L-29201.7}
\]

Thus

\[
\boxed{
\mathcal M_X\le(1+\sqrt2)\log X.
}
\tag{L-29201.8}
\]

The same estimate applies when the two extreme orientations are stored as
separate variables, because their sum is part of `P_d(n)`.

## 3. Consequence for MCF

PR #285 defines Mersenne-Collar Fragmentation by:

1. exact nonnegative saturation;
2. binary-window support away from Mersenne rows;
3. extreme support on Mersenne rows;
4. an independently asserted `X^o(1)` collar bound.

Item 4 is redundant.  Items 1--3 imply the stronger logarithmic estimate
(L-29201.8) automatically.

Therefore the genuine theorem is the **support-feasibility statement**

\[
\boxed{
\begin{gathered}
 d_X(n,j)\ge0,\\
 L_q(d_X)=w_X(q),\\
 n-L(n)<j<L(n)
 \quad(n\ne2^r-1),\\
 j\in\{1,n-1\}
 \quad(n=2^r-1).
\end{gathered}}
\tag{L-29201.9}
\]

Any flow satisfying (L-29201.9) already obeys

\[
\mathcal R_\eta(X)
\ge-(1+\sqrt2)\log X
\tag{L-29201.10}
\]

by the exact eta-source pairing of `L-28002`.  The one-sided Mellin--Landau
consumer of `T-28001` then yields RH.

## 4. Why this matters

The open MCF problem is no longer an asymptotic optimization problem.  It is an
exact finite cone-membership problem at each endpoint.  No quantitative rate
has to be extracted from a producer once feasibility and support are proved.

This also supplies a fail-closed review rule: a proposed MCF proof may not spend
research effort on estimating Mersenne mass while leaving exact support
feasibility unproved.  The mass estimate follows from one diagonal column.

## 5. Proof boundary

Closed exactly:

- the pointwise parent-mass bound for every nonnegative sub-saturation;
- the explicit logarithmic Mersenne-collar estimate;
- removal of the separate collar-rate hypothesis from MCF;
- support-feasible MCF implies the eta lower envelope and RH.

Open:

- construction of the exact support-feasible flow (L-29201.9);
- RH.
