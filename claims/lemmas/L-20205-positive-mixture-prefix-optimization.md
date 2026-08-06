# L-20205 — Positive-mixture prefix optimization

Claim ID: `L-20205`  
Title: Positive dilation mixtures have one exact barycentric prime threshold and improve the adverse prefix exponent  
Status: `PROPOSED — COMPLETE FINITE ALGEBRA`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20203`; `L-20202`; `L-20204`  
Scope: finite positive mixtures of integer-dilation defects

## 1. Common critical mesh

Let `S` be a finite set of integers at least two, let

\[
 R=\max S,
 \qquad c_r>0,
\]

and define

\[
 \mathcal D_{\mathbf c}(t)=\sum_{r\in S}c_r\mathcal D_r(t).
\]

Use the common square-cutoff mesh

\[
 t={2\over R}\log n.
\]

For a prime power `q`, write

\[
 u={\log q\over t}.
\]

The complete prime coefficient of the `r`-component is

\[
 W_r(u)=
 \begin{cases}
 (r-1)((r+1)u-r),&0\le u\le1,\\
 r-u,&1<u\le r,\\
 0,&u>r.
 \end{cases}
 \tag{1}
\]

apart from the common positive factor `t Lambda(q)/sqrt(q)`.

Every component is nonnegative for `u>=1`. Hence all possible negative prime
weight of the mixture lies below `e^t=n^(2/R)` and is decided by one affine
function.

## 2. Exact barycentric threshold

On `0<=u<=1`,

\[
 \sum_{r\in S}c_rW_r(u)
 =A_{\mathbf c}u-B_{\mathbf c},
\]

where

\[
 A_{\mathbf c}=\sum_{r\in S}c_r(r^2-1),
 \qquad
 B_{\mathbf c}=\sum_{r\in S}c_rr(r-1).
\]

Thus the unique zero is

\[
\boxed{
 u_{\mathbf c}
 ={B_{\mathbf c}\over A_{\mathbf c}}
 ={\sum c_r(r-1)(r+1)\,{r\over r+1}
   \over
   \sum c_r(r-1)(r+1)}.}
\tag{2}
\]

It is a positive weighted average of the numbers `r/(r+1)`. Consequently

\[
\boxed{
 {2\over3}\le u_{\mathbf c}\le {R\over R+1}.}
\tag{3}
\]

The mixture prime weight is negative exactly when

\[
 q<n^{2u_{\mathbf c}/R}.
\tag{4}
\]

Every prime power above that threshold and below `n^2` has nonnegative weight.

## 3. Improvement over one dilation

The single `R`-defect has exponent

\[
 {2\over R+1}.
\]

If the mixture contains `r=2` and a positive `r=R` component, concentrating the
remaining weight at `r=2` makes

\[
 u_{\mathbf c}\downarrow {2\over3}.
\]

Therefore the adverse prime exponent can be made arbitrarily close to

\[
\boxed{{4\over3R}.}
\tag{5}
\]

For large fixed `R`, this improves the single-dilation prefix by the asymptotic
factor `2/3`. The top dilation remains present, so the pole-descent accumulation
and square-cutoff `n^2` manifest are unchanged.

More generally, rational weights on two dilations realize every rational
threshold in the open interval between their two values `r/(r+1)`. Filter
design may therefore freeze an exact rational threshold suited to a Selberg or
prime-polygon block decomposition.

## 4. Sign-preserving architecture

Every positive mixture simultaneously retains:

1. RH-side nonnegativity;
2. the multiplicity-weighted pole-descent converse of `T-20203`;
3. the explicit Fejér–Gram portfolio of `L-20204`;
4. a termwise-positive mixture of the Lerch corrections;
5. one complete prime-power stream through `n^2`.

Thus optimizing (2) changes neither the test function's logical status nor its
proof-producing source contract.

## 5. What the optimization does not prove

The highest-dilation polar term and its positive prime bulk still cancel to
RH-scale accuracy. A thin adverse prefix is a structural simplification, not a
standalone domination proof. In particular:

- taking the top coefficient very small does not remove its asymptotic
  off-line-zero sensitivity;
- phase-blind PNT bounds remain too coarse;
- coefficients may not depend on `n` after the analytic criterion is fixed;
- numerical optimization of `c_r` is discovery only until exact rational
  coefficients are frozen.

## 6. Recommended production choices

Useful exact starting packets are

```text
S={2,15},  S={2,31},  S={2,63}
```

with a rational top coefficient selected so that `u_c` is a simple rational.
Each packet should be emitted both as:

- the direct two-scale scalar mixture;
- the single aggregate FIR Gram portfolio.

The exact intervals must overlap before any cofinal pattern is used.
