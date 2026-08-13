# R-91633 — Weighted literal entropy and one-use parent capacity

Claim ID: `R-91633`  
Status: **EXACT CAPACITY REFUTATION; CORRECTED CLOSURE IN `L-91634`**  
Created: 2026-08-14  
Depends on: carry coordinates `beta_(nq)`; `L-90029`; `L-91632`  
RH status: **unproved**

## 1. Carry–entropy duality

For

\[
\beta_{nq}=\frac1{n+1}\sum_{j=0}^n
\left(\left\lfloor\frac nq\right\rfloor-
\left\lfloor\frac jq\right\rfloor-
\left\lfloor\frac{n-j}{q}\right\rfloor\right)
\]

and

\[
G_n=\frac1{n+1}\sum_{j=0}^n\log\binom nj,
\]

Legendre's identity

\[
\log(m!)=\sum_{q\le m}\Lambda(q)\left\lfloor\frac mq\right\rfloor
\]

gives, after averaging the binomial identity over `j`,

\[
\boxed{G_n=\sum_{q=2}^n\Lambda(q)\beta_{nq}.}
\tag{R-91633.1}
\]

Thus for every finite row `d`, with `C_d(q)=sum_n d(n) beta_(nq)`, finite Fubini gives

\[
\boxed{\mathcal S(d):=\sum_nd(n)G_n
      =\sum_{q\ge2}\Lambda(q)C_d(q).}
\tag{R-91633.2}
\]

## 2. Sharp parent score ceiling

At endpoint `X`, let

\[
w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X},
\qquad
\mathcal P(X)=\sum_{q\le X}\frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
\]

If a nonnegative physical row is parent feasible, `C_d(q)<=w_X(q)`, then `Lambda(q)>=0` and (R-91633.2) imply

\[
\boxed{\mathcal S(d)\le\mathcal P(X).}
\tag{R-91633.3}
\]

Equality holds when `C_d=w_X`. By `L-90029`, radix-four detail feasibility implies ordinary feasibility, so the same ceiling applies to every row admitted by the RH consumer.

## 3. Exact obstruction

Put `X=256x`, `1<=x<=67`, and `D=Sigma-mathcal P`. A termwise physical interpretation of

\[
\sum_{j=0}^4 2^{j-4}D(4^jx)
\]

would charge one parent row the literal entropy

\[
\mathcal P(X)+\frac12\mathcal P(X/4)+\frac14\mathcal P(X/16)
 +\frac18\mathcal P(X/64)+\frac1{16}\mathcal P(X/256).
\tag{R-91633.4}
\]

This exceeds `mathcal P(X)`, since

\[
\mathcal P(X/4)=\mathcal P(64x)
\ge\frac{\log2}{\sqrt2}\log(32x)>0.
\tag{R-91633.5}
\]

Therefore no nonnegative row feasible for the single target `w_(256x)` can realize or dominate the weighted five-literal-entropy charge. The obstruction is already in ordinary carry coordinates; extra detail columns, affine covariance, or more elaborate provenance cannot remove it.

## 4. Correct accounting

A one-use parent row is counted once. If it saturates `w_X`, its exact entropy is `mathcal P(X)`. Hence the physically correct loss is

\[
\boxed{
\mathcal L^{\rm one}_4(x)
=\sum_{j=0}^4 2^{j-4}\Sigma(4^jx)-\mathcal P(256x),
}
\tag{R-91633.6}
\]

not a weighted sum of five copies of `D`. `L-91634` proves that (R-91633.6) is uniformly negative and combines it with the exact one-use parent-row identity.

```text
carry–entropy duality                            EXACT
parent-feasible score ceiling                    EXACT
weighted five-literal-row realization            IMPOSSIBLE
scalar theorem L-91632                           RETAINED
correct single-parent closure                    L-91634
Riemann Hypothesis                               UNPROVEN
```
