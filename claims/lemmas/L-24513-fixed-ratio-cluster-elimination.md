# L-24513 — Every fixed-ratio carry band is removable at vanishing cost

Claim ID: `L-24513`  
Status: `PROPOSED COMPLETE — constructive elementary theorem`  
Scope: all prime-power constraints `q>=X/R` for fixed `R`  
Issue: #245  
Depends on: `L-24502`, `L-24508`, `L-24511`

Fix an integer

\[
R\ge2.
\]

Let

\[
\mathcal Q_{X,R}
=
\{q=p^a:X/R\le q\le X\}.
\]

For the parabolic seed put

\[
r_X(q)=v_q(b_X^{(0)})-q^{-1/2}\log(X/q).
\]

## Theorem

For every fixed `R` there are constants `X_R` and `C_R`, depending only on `R`, such that for every integer `X>=X_R` there is a nonnegative flow supported on prime powers in the fixed-ratio band,

\[
F_j\ge0,
\qquad
F_j=0\quad\text{unless }j\in\mathcal Q_{X,R},
\tag{L-24513.1}
\]

for which the corrected vector

\[
b_F(m)=b_X^{(0)}(m)+F_{m-1}-F_m
\]

satisfies

\[
\boxed{
v_q(b_F)\le q^{-1/2}\log(X/q)
\qquad(q\in\mathcal Q_{X,R}),}
\tag{L-24513.2}
\]

and the exact objective cost obeys

\[
\boxed{
0\le
J_X(b_X^{(0)})-J_X(b_F)
\le C_R X^{-3/2}.}
\tag{L-24513.3}
\]

No sign condition on the corrected coordinates `b_F(m)` is required.

## 1. Uniform bound for the initial band residual

Write

\[
b_X^{(0)}(m)=\sqrt X\,B(m/X),
\]

where

\[
B(t)=2\sqrt t\,[\log(1/t)-2(1-\sqrt t)].
\]

On `[1/R,1]`,

\[
|B'(t)|
\le
4+\sqrt R(\log R+4)
=:M_R.
\tag{L-24513.4}
\]

If `q>=X/R`, the sum defining `v_q` has at most `R` terms. The mean-value theorem gives

\[
|b_X^{(0)}(kq)-b_X^{(0)}(kq+1)|
\le\frac{M_R}{\sqrt X}.
\]

Also

\[
q^{-1/2}\log(X/q)
\le\frac{\sqrt R\log R}{\sqrt X}.
\]

Hence

\[
\boxed{|r_X(q)|\le K_R X^{-1/2}}
\tag{L-24513.5}
\]

throughout the band, where

\[
K_R=RM_R+\sqrt R\log R.
\]

## 2. Descending cluster algorithm

Partition the prime powers in `Q_(X,R)` into maximal consecutive-prime-power clusters. Process the clusters in decreasing order of their largest member.

At a current cluster `C`, let

\[
e_C=(r_C^{\rm current})_+
\]

be its positive residual vector. Use the exact inverse-positive cluster matrix of `L-24511` and add

\[
F_C=A_C^{-1}e_C\ge0.
\tag{L-24513.6}
\]

This removes every current positive residual in `C`.

A later, lower cluster cannot reactivate `C`. Indeed, a positive child of a direct repair at `q` either is `q-1` or `q+1`, in which case it lies in the same maximal cluster, or is a proper divisor of one of those integers and is at most `(q+1)/2<q` once `q>1`.

Thus the descending algorithm terminates with (L-24513.2).

## 3. Factor descent outside one cluster

Choose `X_R` so that

\[
X/R\ge6.
\]

After the same-scale cluster solve, every positive child `d` outside the cluster satisfies, for a cluster member `q`,

\[
d\le\frac{q+1}{2}\le\frac7{12}q<\frac23q.
\tag{L-24513.7}
\]

Consequently every chain of positive descendants which remains in the band has length at most

\[
L_R=2+\left\lceil\log_{3/2}R\right\rceil.
\tag{L-24513.8}
\]

This bound is independent of `X`.

## 4. Fixed-ratio mass bound

For clusters above `5`, the matrices in `L-24511` have inverse `ell^1` operator norm at most `2`. The exceptional cluster never occurs after enlarging `X_R`, since the entire band then lies above `5`.

A prime power `q` has at most `R+1` divisors `d>=X/R` of `q-1`, and at most `R+1` such divisors of `q+1`: each corresponds to a quotient not exceeding `R+1`. Therefore one unit of cluster defect creates at most

\[
4(R+1)
\tag{L-24513.9}
\]

units of positive descendant mass in the next lower generation, after including the cluster inverse norm.

The initial positive mass is at most

\[
\sum_{q\in\mathcal Q_{X,R}}(r_X(q))_+
\le K_R\sqrt X,
\tag{L-24513.10}
\]

using the crude bound `#Q_(X,R)<=X` and (L-24513.5).

Combining (L-24513.8)--(L-24513.10), the total flow mass satisfies

\[
\boxed{
\sum_{q\in\mathcal Q_{X,R}}F_q
\le
A_R K_R\sqrt X,}
\tag{L-24513.11}
\]

where, for example, one may take

\[
A_R=2\sum_{\ell=0}^{L_R}[4(R+1)]^\ell.
\]

No asymptotic information about primes is used.

## 5. Exact objective cost

For `q>=X/R` and sufficiently large `X`,

\[
\log\frac{q^2}{q^2-1}
\le\frac{2}{q^2-1}
\le\frac{4R^2}{X^2}.
\tag{L-24513.12}
\]

The exact adjacent-flow identity now gives

\[
\begin{aligned}
0\le J_X(b_X^{(0)})-J_X(b_F)
&=\sum_{q\in\mathcal Q_{X,R}}
 F_q\log\frac{q^2}{q^2-1}\\
&\le
\frac{4R^2}{X^2}A_RK_R\sqrt X.
\end{aligned}
\]

Thus (L-24513.3) holds with

\[
C_R=4R^2A_RK_R.
\]

## 6. Consequence

For every fixed `R`, all fixed-ratio constraints can be consumed before the RH-bearing estimate at a cost tending to zero:

\[
\boxed{
q/X\ge1/R
\quad\Longrightarrow\quad
\text{elementary finite repair with }O_R(X^{-3/2})\text{ cost}.}
\tag{L-24513.13}
\]

Therefore any surviving obstruction to the parabolic carry proof must lie in the moving low-ratio region

\[
q/X\longrightarrow0.
\]

The first-cell/Farey fixed-ratio firewalls remain important scalar projections of the complete arithmetic packet, but no **individual fixed-ratio carry band** is the unresolved correction problem.

## Review boundary

The theorem is constructive and finite for every fixed `R`; its constants may grow rapidly with `R`. It does not permit `R=R(X)` without an additional uniform estimate and does not prove RH.
