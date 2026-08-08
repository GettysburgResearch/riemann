# L-30401 — Descendant central capacity has an exact dyadic Haar formula

Claim ID: `L-30401`  
Title: The coefficient of a central edge in a complete central-tree layer cake is an explicit sum of adjacent dyadic block differences  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #272 `L-27204`; `R-30401`  
Scope: finite expanded-tree capacity; no asymptotic source estimate

## 1. Node multiplicities at one depth

Let `T_m` be the complete central tree and let

\[
h_n=[n,\lfloor n/2\rfloor].
\]

At depth `r`, put `L=2^r`.  The `L` node sizes in `T_m` are

\[
\left\lfloor\frac mL\right\rfloor
\quad\text{and}\quad
\left\lceil\frac mL\right\rceil.
\]

The number of nodes of size `n` at this depth is therefore

\[
\boxed{
\nu_{n,r}(m)=
\begin{cases}
 m-L(n-1),&L(n-1)\le m\le Ln,\\
 L(n+1)-m,&Ln\le m\le L(n+1),\\
 0,&\text{otherwise}.
\end{cases}}
\tag{L-30401.1}
\]

The two formulas agree at `m=Ln`, where the value is `L`.

Every occurrence of a node `n` contributes exactly one copy of `h_n`.
Consequently

\[
[h_n]T_m=\sum_{r\ge0}\nu_{n,r}(m),
\tag{L-30401.2}
\]

where the sum is finite.

## 2. Exact Haar-block formula

Let

\[
c_2\ge\cdots\ge c_N\ge0,
\qquad c_{N+1}=0,
\qquad d_m=c_m-c_{m+1},
\]

and extend `c_m=0` for `m>N`.  Put

\[
\mathcal T(c)=\sum_{m=2}^Nd_mT_m
\]

and

\[
\kappa_n=[h_n]\mathcal T(c).
\]

Summation by parts in `m` and (L-30401.1) give

\[
\boxed{
\begin{aligned}
\kappa_n
=\sum_{r\ge0}\Bigg(&
 \sum_{m=2^r(n-1)+1}^{2^rn}c_m\\
&-
 \sum_{m=2^rn+1}^{2^r(n+1)}c_m
\Bigg).
\end{aligned}}
\tag{L-30401.3}
\]

Every displayed block is interpreted using the zero extension beyond `N`.
This is an exact dyadic Haar coefficient formula for the expanded central
capacity.

## 3. Positivity and recurrence

Each pair of blocks in (L-30401.3) has equal length, and every index in the
first block precedes every index in the second.  Hence monotonicity gives

\[
\boxed{
\kappa_n\ge0.
}
\tag{L-30401.4}
\]

The actual capacities also obey the exact downward recurrence

\[
\boxed{
\kappa_n
=d_n+2\kappa_{2n}+\kappa_{2n-1}+\kappa_{2n+1},
}
\tag{L-30401.5}
\]

with `kappa_m=0` above the endpoint.  Indeed every non-root occurrence of
`h_n` has a unique parent of size `2n`, `2n-1`, or `2n+1`; an occurrence of
`h_(2n)` produces two children of size `n`.

Equation (L-30401.5) is the correct factor-two capacity descent.  It replaces
the root-only identity by an exact triangular one.

## 4. Power-source scale

For a power source

\[
c_m=m^{-p},
\qquad p>1,
\]

the `r`th block in (L-30401.3) has the elementary bound

\[
0\le H_{n,r}
\le C_p\,2^{r(1-p)}n^{-p-1}.
\tag{L-30401.6}
\]

One proof pairs the two length-`2^r` blocks and applies the mean-value theorem
to `x^{-p}`.  Summing the geometric series gives

\[
\boxed{
\kappa_n\le C'_p n^{-p-1}.
}
\tag{L-30401.7}
\]

Thus descendants improve the root coefficient by an absolute factor at the
critical source exponent; they do not create the missing factor `n` required by
a zero-debt sibling replacement.  This is why the correct completion should
pay the critical signed capacity rather than demand exact capacity matching.

## 5. Proof boundary

Closed exactly:

1. the node multiplicity formula;
2. the dyadic Haar expansion of actual central capacity;
3. positivity for every decreasing source;
4. the exact factor-two recurrence;
5. the elementary scale bound for power sources.

Open:

1. any claim that `kappa_n` dominates a prescribed source coefficient;
2. a complete source-flow theorem;
3. RH.
