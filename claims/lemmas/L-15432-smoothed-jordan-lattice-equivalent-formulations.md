# L-15432 — Equivalent formulations of the smoothed-Jordan lattice gate

Claim ID: `L-15432`  
Title: Christoffel mixture, random sieve, prime-adjoining renewal, and Selberg-square forms of the integer-endpoint inequality  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: `L-15428`, `L-15430`, `L-15431`  
Scope: the integer-endpoint gate `Y_s(log N)>=0`  
Related counterexample candidates: none

## Setup

Fix `0<s<1`, put

\[
 F_s(n)=\prod_{p\mid n}(1-p^{-s}),\qquad
 c_s=\zeta(1+s)^{-1},
\]

and let `n_s` and `I_s(x)=\int_0^{\log x}n_s(r)dr` be the beta-resolvent kernel and its primitive from `L-15431`.  The endpoint discrepancy is

\[
 Y_s(\log N)=
 \sum_{n<N}{F_s(n)\over n}n_s\!\left(\log{N\over n}\right)
 -c_s I_s(N).
\]

`L-15431` proves that positivity of these integer values is equivalent to positivity for every real translation.

## I. Positive Christoffel mixture

The beta source has the positive exponential expansion

\[
 \beta_s(t)=\sum_{k\ge0}b_{s,k}e^{-\lambda_k t},
 \qquad b_{s,k}>0,\quad \lambda_k=3+2k.
\]

Solving `n_s'+s n_s=beta_s`, `n_s(0)=0`, gives

\[
 \boxed{
 n_s(t)=\sum_{k\ge0}w_{s,k}
 (e^{-st}-e^{-\lambda_k t}),\qquad
 w_{s,k}={b_{s,k}\over\lambda_k-s}>0.}
\]

For `r>0`, define the weighted quadrature error

\[
 \mathcal E_{s,r}(N)=
 N^{-r}\sum_{n<N}F_s(n)n^{r-1}
 -c_s{1-N^{-r}\over r}.
\]

Then, by locally uniform summation,

\[
 \boxed{
 Y_s(\log N)=
 \sum_{k\ge0}w_{s,k}
 [\mathcal E_{s,s}(N)-\mathcal E_{s,\lambda_k}(N)].}
\]

The complete positive mixture is load-bearing.  Componentwise positivity of every bracket is not asserted and ordinary reconnaissance finds failures for sufficiently large `lambda`.

## II. Random squarefree sieve

Let `Q` be the random squarefree integer obtained by selecting each prime independently with probability `p^{-s}`.  Then

\[
 \boxed{F_s(n)=\Pr((n,Q)=1),}
\]

and independence gives

\[
 \boxed{c_s=\mathbb E[\varphi(Q)/Q].}
\]

Consequently

\[
 \boxed{
 Y_s(\log N)=\mathbb E_Q\left[
 \sum_{\substack{n<N\\(n,Q)=1}}
 {1\over n}n_s\!\left(\log{N\over n}\right)
 -{\varphi(Q)\over Q}I_s(N)
 \right].}
\]

The integrand is not nonnegative for every deterministic `Q`; the prime-set average is essential.

## III. Exact prime-adjoining renewal

For a finite prime set `P`, define

\[
 F_{s,P}(n)=\prod_{\substack{p\in P\\p\mid n}}(1-p^{-s}),
 \qquad
 c_{s,P}=\prod_{p\in P}(1-p^{-1-s}),
\]

\[
 L_{s,P}(x)=\sum_{n<x}{F_{s,P}(n)\over n}
 n_s\!\left(\log{x\over n}\right),
 \qquad
 D_{s,P}(x)=L_{s,P}(x)-c_{s,P}I_s(x).
\]

If `p notin P`, separation of multiples of `p` gives

\[
 \boxed{L_{s,P\cup\{p\}}(x)=L_{s,P}(x)-p^{-1-s}L_{s,P}(x/p).}
\]

Therefore

\[
 \boxed{
 \begin{aligned}
 D_{s,P\cup\{p\}}(x)
 ={}&D_{s,P}(x)-p^{-1-s}D_{s,P}(x/p)\\
 &+p^{-1-s}c_{s,P}[I_s(x)-I_s(x/p)].
 \end{aligned}}
\]

Here `I_s(y)=0` for `y<=1`.  This is the exact two-scale recursion that a coupled discrepancy-plus-tail invariant must propagate.

A second homogeneous form uses the upper tail

\[
 T_s(x)=I_s(\infty)-I_s(x)
\]

and

\[
 G_{s,P}(x)=c_{s,P}I_s(\infty)-L_{s,P}(x).
\]

Then

\[
 \boxed{G_{s,P\cup\{p\}}(x)
 =G_{s,P}(x)-p^{-1-s}G_{s,P}(x/p),}
\]

while `D_{s,P}+G_{s,P}=c_{s,P}T_s`.  Thus the desired sign is equivalent to the two-sided sandwich

\[
 0\le D_{s,P}(x)\le c_{s,P}T_s(x).
\]

This is the natural coupled discrepancy/beta-tail state.

## IV. Selberg-square/LCM form

For squarefree `d`, define the multiplicative coefficients

\[
 \lambda_s(p)=\sqrt{1-p^{-s}}-1,
 \qquad
 \lambda_s(d)=\prod_{p\mid d}\lambda_s(p).
\]

Then

\[
 \boxed{F_s(n)=\left(\sum_{d\mid n}\lambda_s(d)\right)^2.}
\]

Also

\[
 \boxed{c_s=\sum_{d,e\ge1}{\lambda_s(d)\lambda_s(e)\over[d,e]},}
\]

with absolute convergence after the standard finite-prime truncation and limiting passage.

Hence

\[
 \boxed{
 Y_s(\log N)=\sum_{d,e\ge1}\lambda_s(d)\lambda_s(e)
 \mathcal K_{s,N}([d,e]),}
\]

where

\[
 \mathcal K_{s,N}(L)=
 {1\over L}\sum_{m<N/L}{1\over m}
 n_s\!\left(\log{N\over Lm}\right)
 -{1\over L}I_s(N).
\]

The full LCM quadratic form is the exact Selberg-square formulation.  The kernel is not claimed positive semidefinite on arbitrary coefficient vectors; the multiplicative vector `lambda_s` and the endpoint cross term must remain coupled.

## Closed shortcuts

The following stronger statements are not used and are generally false or unsupported:

1. positivity of every Christoffel component;
2. positivity for each deterministic squarefree `Q`;
3. pointwise positivity of the unsmoothed Jordan discrepancy;
4. plain monotonicity of `L_{s,P}` or `D_{s,P}` in the scale;
5. positivity of the LCM kernel for arbitrary vectors.

## Proof boundary

All four representations are exact finite algebra followed by monotone/absolutely convergent limits in their stated domains.  They do not prove the endpoint sign.  The remaining theorem is a uniform invariant for the prime-adjoining recurrence, equivalently positivity of the terminal LCM quadratic form on the specific multiplicative vector.