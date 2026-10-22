# L-23813 — Profit/debt criterion for balanced carry fragmentation

Claim ID: `L-23813`  
Title: The prime-ramp deficit is exactly the fragmentation profit, and a finite-exception profitable flow would prove RH with only logarithmic debt  
Status: **PROPOSED EXACT LEMMA — COMPLETE FINITE ALGRA; EXISTENCE OF THE PROFITABLE FLOW IS OPEN**  
Authoring agent: `gpt56-pro-09-w`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23808`, `L-23810`  
Scope: exact min-cost reformulation of the balanced carry theorem

## 1. Divisor potential

Let

\[
 \mathcal D(n)=\sum_{q=1}^{n}\left\lfloor\frac nq\right\rfloor
\tag{L-23813.1}
\]

and define

\[
 \boxed{F(n)=\log(n!)-\mathcal D(n),\qquad F(0)=0.}
\tag{L-23813.2}
\]

For one split `n=j+(n-j)`, put

\[
 \pi(n,j)=F(n)-F(j)-F(n-j).
\tag{L-23813.3}
\]

The exact carry-count identity of `L-23808` gives

\[
 \boxed{
 \pi(n,j)
 =\log\binom nj-\sum_{q=2}^{n}\chi_{n,j}(q).}
\tag{L-23813.4}
\]

Thus `pi` is the entropy profit of the split after charging one unit for every
integer carry column it consumes.

## 2. Flow-invariant total profit

Let `d_(n,j)>=0` be any balanced split flow with node divergence `r_m` as in
`L-23808/L-23810`.  Telescoping of the potential `F` gives

\[
\boxed{
 \sum_{n,j}d_{n,j}\pi(n,j)
 =\sum_{m=1}^{X}r_mF(m).}
\tag{L-23813.5}
\]

Suppose that the flow exactly saturates the ramp target,

\[
 \sum_{n,j}d_{n,j}\chi_{n,j}(q)=w_X(q)
 \qquad(2\le q\le X),
\tag{L-23813.6}
\]

with `w_X(1)=0`.  The factorial identity

\[
 \log(n!)=\sum_{p^a\le n}\Lambda(p^a)
 \left\lfloor\frac n{p^a}\right\rfloor
\tag{L-23813.7}
\]

and the definition of `mathcal D` then yield

\[
\boxed{
 \sum_{n,j}d_{n,j}\pi(n,j)
 =\mathcal P(X)-\mathcal C(X),}
\tag{L-23813.8}
\]

where

\[
 \mathcal P(X)=\sum_{p^a\le X}
 \frac{\Lambda(p^a)}{\sqrt{p^a}}
 \log\frac X{p^a}
\tag{L-23813.9}
\]

and

\[
 \mathcal C(X)=\sum_{q=2}^{X}
 \frac1{\sqrt q}\log\frac Xq
 =4\sqrt X+O(\log X).
\tag{L-23813.10}
\]

The total profit is independent of the chosen exact fragmentation.  Pascal
four-cycles redistribute positive and negative split profit but cannot change
its sum.

## 3. Negative-debt program

Define the local debt

\[
 c(n,j)=(-\pi(n,j))_+.
\tag{L-23813.11}
\]

Among exact nonnegative balanced flows, consider

\[
 \boxed{
 \mathfrak D_X=\min_d\sum_{n,j}d_{n,j}c(n,j).}
\tag{L-23813.12}
\]

The dual is

\[
\boxed{
 \begin{aligned}
 \mathfrak D_X=\max_{\varphi}\quad&
     \sum_mr_m\varphi(m),\\
 \text{subject to}\quad&
 \varphi(n)-\varphi(j)-\varphi(n-j)
 \le c(n,j)
 \quad\text{for every retained balanced split.}
 \end{aligned}}
\tag{L-23813.13}
\]

The potential `varphi=-F` is feasible because

\[
 -\pi(n,j)\le(-\pi(n,j))_+.
\]

Therefore

\[
\boxed{
 \mathfrak D_X
 \ge \mathcal C(X)-\mathcal P(X).}
\tag{L-23813.14}
\]

This is a proof firewall: a subpolynomial negative-debt theorem is already
strong enough to control the complete prime-ramp deficit.  It cannot be obtained
by replacing the signed arithmetic family with total variation.

## 4. Finite-exception criterion

Assume that for every sufficiently large `X` there is an exact nonnegative
balanced flow satisfying (L-23813.6), and assume that every split it uses with
negative profit has parent size in one fixed finite set

\[
 \mathcal B\subset\{2,3,\ldots\},
\tag{L-23813.15}
\]

independent of `X`.

For every split of parent `n`,

\[
 \chi_{n,j}(n)=1.
\tag{L-23813.16}
\]

Hence exact feasibility gives

\[
 \sum_jd_{n,j}\le w_X(n).
\tag{L-23813.17}
\]

Let

\[
 C_n=\max_{1\le j<n}(-\pi(n,j))_+.
\]

The complete negative debt is then bounded by

\[
 \sum_{n,j}d_{n,j}c(n,j)
 \le\sum_{n\in\mathcal B}C_nw_X(n)
 =O_{\mathcal B}(\log X).
\tag{L-23813.18}
\]

Combining (L-23813.8) with the nonnegative profit outside `mathcal B` gives

\[
\boxed{
 \mathcal P(X)
 \ge\mathcal C(X)-O_{\mathcal B}(\log X)
 =4\sqrt X-O_{\mathcal B}(\log X).}
\tag{L-23813.19}
\]

The square-screw/Landau transfer therefore yields RH.

This motivates the **finite-exception profitable fragmentation theorem**:
construct an exact nonnegative balanced flow whose unprofitable parent set is
absolute and finite.  It is stronger than the `X^{o(1)}` debt conclusion but is
particularly easy to audit.

## 5. A weaker sufficient form

The finite-exception statement is not necessary.  It is enough to construct
exact nonnegative flows satisfying

\[
\boxed{
 \sum_{n,j}d_{n,j}(-\pi(n,j))_+=X^{o(1)}.}
\tag{L-23813.20}
\]

Then (L-23813.8) implies

\[
 \mathcal P(X)\ge\mathcal C(X)-X^{o(1)},
\]

which is the sharp prime-ramp estimate consumed by `T-23802/T-23803`.

## 6. Proof boundary

Proved here:

- the exact split-profit potential;
- flow invariance of total profit;
- equality with the prime-ramp minus all-integer capacity;
- the min-cost dual and its `-F` firewall;
- the finite-exception and subpolynomial-debt implications to RH.

Not proved here:

- existence of exact nonnegative balanced flows with finite exceptional debt;
- a subpolynomial debt bound;
- RH.
