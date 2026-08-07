# D-23801 — One-sided carry envelope coordinates

Definition ID: `D-23801`  
Title: The prime ramp admits a finite nonnegative carry packing with a canonical descending producer  
Status: **PROPOSED EXACT FINITE DEFINITION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-23`  
Created: 2026-08-07  
Issue: #238  
Scope: finite definitions only; RH is not claimed

## 1. Carry matrix

For integers `2<=q<=n`, write

\[
n=a_{nq}q+r_{nq},
\qquad0\le r_{nq}<q,
\]

and define

\[
\boxed{
\beta_{nq}
=\frac{a_{nq}(q-1-r_{nq})}{n+1}.}
\tag{D-23801.1}
\]

Put `beta_(nq)=0` for `q>n`. Then

\[
\beta_{nq}\ge0,
\qquad
\beta_{nn}=\frac{n-1}{n+1}>0.
\tag{D-23801.2}
\]

For an endpoint `X>=2`, let `B_X` be the lower-triangular matrix

\[
(B_X)_{nq}=\beta_{nq},
\qquad2\le n,q\le X.
\tag{D-23801.3}
\]

## 2. Prime-ramp target and binomial rows

Define

\[
\boxed{
w_X(q)=q^{-1/2}\log(X/q),
\qquad2\le q\le X,}
\tag{D-23801.4}
\]

and

\[
\boxed{
G_n=\frac1{n+1}\sum_{j=0}^n\log\binom nj.}
\tag{D-23801.5}
\]

The complete prime-power ramp is

\[
\boxed{
\mathcal P(X)
=\sum_{q=p^k\le X}\Lambda(q)w_X(q).}
\tag{D-23801.6}
\]

## 3. Carry packings

A **one-sided carry packing** is a vector

\[
d=(d(2),\ldots,d(X))
\]

satisfying

\[
\boxed{
d(n)\ge0,
\qquad B_X^Td\le w_X}
\tag{D-23801.7}
\]

coordinatewise. Its unused ramp is

\[
\boxed{
\rho_d(q)=w_X(q)-(B_X^Td)(q)\ge0.}
\tag{D-23801.8}
\]

Define its weighted mass and coefficient mass by

\[
\mathcal M_X(d)=\sum_{n=2}^Xn\,d(n),
\qquad
\mathcal C_X(d)=\sum_{n=2}^Xd(n).
\tag{D-23801.9}
\]

No upper carry cover is part of the minimal proposal.

## 4. Canonical descending greedy packing

Initialize

\[
\rho_X^{(X)}(q)=w_X(q).
\]

For `n=X,X-1,...,2`, set

\[
\boxed{
 d_X^{\rm gr}(n)
 =\min_{\substack{2\le q\le n\\\beta_{nq}>0}}
 \frac{\rho_X^{(n)}(q)}{\beta_{nq}}}
\tag{D-23801.10}
\]

and update

\[
\rho_X^{(n-1)}(q)
=\rho_X^{(n)}(q)-d_X^{\rm gr}(n)\beta_{nq}
\qquad(q\le n).
\tag{D-23801.11}
\]

Already terminal columns are left unchanged. The minimum is always over a
nonempty set because `beta_(nn)>0`.

Every residual remains nonnegative, so

\[
\boxed{
 d_X^{\rm gr}\ge0,
\qquad B_X^Td_X^{\rm gr}\le w_X.}
\tag{D-23801.12}
\]

Fix the least minimizing column as the exact tie rule. This makes the producer
deterministic.

## 5. Pivot potential and final residual

Put

\[
\boxed{
a(q)=2-64q^{-1/2}}
\tag{D-23801.13}
\]

and let

\[
a_+(q)=\max(a(q),0).
\]

For any packing define the positive residual potential

\[
\boxed{
\mathcal R_X^+(d)
=\sum_{q=2}^Xa_+(q)\rho_d(q).}
\tag{D-23801.14}
\]

The canonical quantity in the full proposal is

\[
\boxed{
\mathcal R_X^{\rm gr}
=\mathcal R_X^+(d_X^{\rm gr}).}
\tag{D-23801.15}
\]

## 6. Greedy Residual theorem

The sole open finite theorem in the clean proposal is:

> **GR — Greedy Residual theorem.** For every `epsilon>0`,
> \[
> \boxed{
> \mathcal R_X^{\rm gr}
> \le C_\varepsilon X^\varepsilon}
> \tag{D-23801.16}
> \]
> for all sufficiently large square endpoints `X=N^2`.

GR is weaker than exact Carry Saturation. It allows off-diagonal pivots, zero
rows, and a nonzero final residual. It asks only that the residual left in one
explicit positive potential be subpolynomial.

## 7. Proof boundary

This definition closes no asymptotic theorem. It fixes one finite matrix, one
finite producer, one finite residual statistic, and one unambiguous proposed
hinge. The deduction `GR => RH` is proved separately in `L-23801`--`T-23801`.
