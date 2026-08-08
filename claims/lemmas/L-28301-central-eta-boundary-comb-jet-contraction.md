# L-28301 — Exact eta boundary-comb jet contraction

Claim ID: `L-28301`  
Title: The central carry dilation kernel is a positive mass contraction plus logarithmic dipoles, giving a strict finite-jet contraction with one exported derivative  
Status: **PROPOSED COMPLETE EXACT ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-x`  
Created: 2026-08-08  
Scope: boundary-aware continuum operator underlying the central carry cascade; no RH conclusion

## 1. Exact logarithmic convolution

Extend a function `f` by zero on `(1,infinity)` and define

\[
 (\mathcal Tf)(x)
 =\sum_{k\ge1}\big[f(2kx)-f((2k+1)x)\big],
 \qquad 0<x\le1.
 \tag{L-28301.1}
\]

At every fixed `x` the sum is finite.  Introduce logarithmic coordinates

\[
 G(t)=e^{-t}f(e^{-t})\mathbf1_{t\ge0}.
 \tag{L-28301.2}
\]

For every integer `a>=1`,

\[
 e^{-t}f(ae^{-t})
 ={1\over a}G(t-\log a).
 \tag{L-28301.3}
\]

Therefore

\[
 \boxed{
 e^{-t}(\mathcal Tf)(e^{-t})
 =(\mathfrak b*G)(t),
 }
 \tag{L-28301.4}
\]

where the locally finite signed logarithmic boundary comb is

\[
 \boxed{
 \mathfrak b
 =\sum_{k\ge1}
 \left[
 {1\over2k}\delta_{\log(2k)}
 -{1\over2k+1}\delta_{\log(2k+1)}
 \right].
 }
 \tag{L-28301.5}
\]

This is the complete continuum boundary source.  It is already present before
the discrete shift `2kq-1` is introduced.

## 2. Eta symbol and mass

For `Re(s)>0`,

\[
\begin{aligned}
 \widehat{\mathfrak b}(s)
 &=\sum_{k\ge1}
 \left[(2k)^{-s-1}-(2k+1)^{-s-1}\right]\\
 &=1-\eta(s+1),
\end{aligned}
\tag{L-28301.6}
\]

where

\[
 \eta(z)=\sum_{n\ge1}(-1)^{n-1}n^{-z}.
\]

At the mass point,

\[
 \boxed{
 \rho:=\widehat{\mathfrak b}(0)=1-\log2.
 }
 \tag{L-28301.7}
\]

Thus the exact critical mass factor found in the one-pass carry computation is
the total mass of the eta boundary comb.

## 3. Positive residual plus monotone dipoles

Write

\[
\begin{aligned}
 \mathfrak b
={}&\sum_{k\ge1}
 \left({1\over2k}-{1\over2k+1}\right)
 \delta_{\log(2k)}\\
 &+\sum_{k\ge1}{1\over2k+1}
 \left[
 \delta_{\log(2k)}-\delta_{\log(2k+1)}
 \right].
\end{aligned}
\tag{L-28301.8}
\]

The first line is a positive measure of total mass `rho`.  The second line is
an adjacent logarithmic transport.  Its exact first-moment cost is

\[
 \boxed{
 \mathfrak c
 =\sum_{k\ge1}{1\over2k+1}
 \log{2k+1\over2k}.
 }
 \tag{L-28301.9}
\]

Since `log(1+x)<x` for `x>0`,

\[
\begin{aligned}
 \mathfrak c
 &<\sum_{k\ge1}{1\over2k(2k+1)}\\
 &=\sum_{k\ge1}
 \left({1\over2k}-{1\over2k+1}\right)\\
 &=\rho.
\end{aligned}
\tag{L-28301.10}
\]

Consequently

\[
 \boxed{
 \theta_*:=\rho+\mathfrak c
 <2(1-\log2)<1.
 }
 \tag{L-28301.11}
\]

The last inequality uses the elementary bound `log 2>1/2`.

## 4. Bounded-Lipschitz pairing

For every bounded Lipschitz function `F`, the decomposition above gives the
absolutely convergent estimate

\[
 \boxed{
 \left|\int F\,d\mathfrak b\right|
 \le
 \rho\|F\|_\infty
 +\mathfrak c\,\operatorname{Lip}(F).
 }
 \tag{L-28301.12]
\]

Indeed the positive line costs its total mass, while each dipole costs its
coefficient times the logarithmic displacement of its endpoints.

This estimate retains the cancellation which is destroyed by the divergent
termwise total variation

\[
 \sum_k\left({1\over2k}+{1\over2k+1}\right)=\infty.
\]

## 5. Strict finite-jet contraction

For a bounded `C^(M+1)` function define

\[
 \mathcal J_M(F)=\sum_{m=0}^{M}\|F^{(m)}\|_\infty.
 \tag{L-28301.13}
\]

Let

\[
 (\mathcal BF)(t)=\int F(t-u)\,d\mathfrak b(u).
 \tag{L-28301.14}
\]

Apply (L-28301.12) to `u mapsto F^(m)(t-u)`.  Since its Lipschitz constant is
at most `||F^(m+1)||_infinity`,

\[
 \|(\mathcal BF)^{(m)}\|_\infty
 \le
 \rho\|F^{(m)}\|_\infty
 +\mathfrak c\|F^{(m+1)}\|_\infty.
 \tag{L-28301.15}
\]

Summing for `0<=m<=M` yields

\[
 \boxed{
 \mathcal J_M(\mathcal BF)
 \le
 \theta_*\mathcal J_M(F)
 +\mathfrak c\|F^{(M+1)}\|_\infty,
 \qquad \theta_*<1.
 }
 \tag{L-28301.16}
\]

Thus the complete analytic boundary operator has a strict current-jet reserve.
The only exported quantity is one higher derivative.  There is no ambient
same-scale loss and no appeal to pointwise monotonicity of later iterates.

For a function with a finite full jet norm

\[
 \mathcal J_\infty(F)=\sum_{m\ge0}\|F^{(m)}\|_\infty<\infty,
\]

monotone convergence gives the genuine contraction

\[
 \boxed{
 \mathcal J_\infty(\mathcal BF)
 \le\theta_*\mathcal J_\infty(F).
 }
 \tag{L-28301.17}

## 6. Boundary-jet interpretation

For the stopped critical profile, ordinary derivatives generate endpoint delta
jets.  `R-28301` shows that omitting them invalidates the smooth monotonicity
argument.  The present theorem gives the corrected architecture:

```text
smooth finite jet bank
    -> strict factor theta_*<1
    + one exported top derivative;

endpoint distributions
    -> explicit eta dipoles
    -> finite Pascal/Peano boundary ledger.
```

The adjacent dipoles

\[
 \delta_{\log(2k)}-\delta_{\log(2k+1)}
\]

are the continuum counterparts of the adjacent-tree commutators on PR #272.
This statement is an identification of source geometry, not yet an asserted
isometry between the two completed norms.

## 7. Proof boundary

Closed exactly:

- the complete logarithmic boundary comb;
- its eta symbol and mass;
- positive-mass plus dipole decomposition;
- the strict constant `theta_*<1`;
- bounded-Lipschitz pairing;
- finite-jet contraction with one exported derivative.

Open:

- a source-bound finite Pascal/Peano realization of every exported endpoint jet;
- a uniform recurrence for that finite boundary ledger;
- the carry Cycle-Debt or physical source estimate;
- RH.
