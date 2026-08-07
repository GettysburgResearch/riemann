# L-23705 — Greedy mass–slack equivalence

Claim ID: `L-23705`  
Title: The lower-order DBT mass is automatic, and the sharp greedy first moment is equivalent to polylogarithmic total residual slack  
Status: **PROPOSED EXACT/ASYMPTOTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Dependencies: `L-23701`; elementary divisor summation  
Scope: every nonnegative feasible carry vector; no RH input

## 1. Feasible vector and total slack

Fix `X>=2`. Let `d(n)>=0`, `2<=n<=X`, satisfy

\[
\sum_{n=q}^X d(n)\beta_{nq}\le w_X(q),
\qquad
w_X(q)=q^{-1/2}\log(X/q).
\tag{L-23705.1}
\]

Define the final column slack

\[
\boxed{
 s_X(q)=w_X(q)-\sum_{n=q}^X d(n)\beta_{nq}\ge0,}
\tag{L-23705.2}
\]

and its total

\[
\boxed{\Sigma_X(d)=\sum_{q=2}^X s_X(q).}
\tag{L-23705.3}
\]

For the greedy vector of `L-23701`, this is the complete unsaturated blocker
ledger after the backward elimination has terminated.

## 2. A universal square-root moment bound

For every `n>=2`, put

\[
H_n=\sum_{q=2}^n {\beta_{nq}\over\sqrt q}.
\tag{L-23705.4}
\]

Then

\[
\boxed{H_n\ge {\sqrt n\over32}.}
\tag{L-23705.5}
\]

For `n>=8`, restrict to

\[
q\ge\left\lceil{3(n+1)\over4}\right\rceil.
\]

On this interval `floor(n/q)=1` and

\[
\beta_{nq}={2q-n-1\over n+1}\ge{1\over2}.
\]

There are at least `n/8` such integers and `q^(-1/2)>=n^(-1/2)`, which gives
`H_n>=sqrt(n)/16`. The finitely many smaller `n` give (L-23705.5) directly.

Multiply (L-23705.1) by `q^(-1/2)` and sum. Fubini and (L-23705.5) give

\[
\begin{aligned}
{1\over32}\sum_{n=2}^X d(n)\sqrt n
&\le
\sum_{q=2}^X {1\over\sqrt q}
 \sum_{n=q}^X d(n)\beta_{nq}\\
&\le
\sum_{q=2}^X {\log(X/q)\over q}.
\end{aligned}
\]

The last sum is at most

\[
{1\over2}\log^2X+{1\over2}\log X.
\]

Consequently

\[
\boxed{
\sum_{n=2}^X d(n)\sqrt n
\le16\log^2X+16\log X.}
\tag{L-23705.6}
\]

This holds for every feasible nonnegative carry vector, not only the greedy one.

## 3. The lower-order DBT mass is automatic

Since

\[
\log(n+1)+3\le4\sqrt n
\qquad(n\ge2),
\]

(L-23705.6) gives

\[
\boxed{
\mathfrak L_X(d)
:=\sum_{n=2}^X d(n)(\log(n+1)+3)
=O(\log^2X).}
\tag{L-23705.7}
\]

Thus the second estimate in DBT does not require quotient-layer, digit, Selberg,
or Möbius cancellation. It follows solely from feasibility and positivity.

## 4. Total carry mass in one row

Let

\[
S_n=\sum_{q=2}^n\beta_{nq}.
\tag{L-23705.8}
\]

Write

\[
D(n)=\sum_{q=1}^n\left\lfloor{n\over q}\right\rfloor
=\sum_{m\le n}\tau(m).
\]

The floor form of the carry count gives exactly

\[
\boxed{
S_n=D(n)-{2\over n+1}\sum_{j=1}^nD(j).}
\tag{L-23705.9}
\]

The elementary Dirichlet-hyperbola estimate

\[
D(n)=n\log n+(2\gamma-1)n+O(\sqrt n)
\tag{L-23705.10}
\]

and one Euler summation give

\[
\sum_{j=1}^nD(j)
={1\over2}n(n+1)\log n
 +(\gamma-3/4)n^2+(\gamma-1/2)n
 +O(n^{3/2}).
\tag{L-23705.11}
\]

Substitution yields

\[
\boxed{
S_n={n\over2}+O(\sqrt n).}
\tag{L-23705.12}
\]

All constants are absolute. Only the classical elementary `O(sqrt(n))`
divisor bound is used.

## 5. Exact mass–slack reduction

Put

\[
\mathfrak M_X(d)=\sum_{n=2}^X n\,d(n).
\]

By (L-23705.12) and (L-23705.6),

\[
\begin{aligned}
\mathfrak M_X(d)
&=2\sum_{n=2}^X d(n)S_n+O(\log^2X)\\
&=2\sum_{q=2}^X
  \sum_{n=q}^Xd(n)\beta_{nq}+O(\log^2X)\\
&=2\sum_{q=2}^Xw_X(q)-2\Sigma_X(d)+O(\log^2X).
\end{aligned}
\tag{L-23705.13}

The target sum satisfies, by monotone integral comparison,

\[
\sum_{q=2}^Xq^{-1/2}\log(X/q)
=4\sqrt X+O(\log X).
\tag{L-23705.14}
\]

Therefore

\[
\boxed{
\mathfrak M_X(d)
=8\sqrt X-2\Sigma_X(d)+O(\log^2X).}
\tag{L-23705.15}
\]

This is the aggregate conservation law behind the sharp carry constant.

## 6. Corrected form of DBT

For the greedy vector `d_X`, the following are equivalent up to a change of the
fixed logarithmic exponent:

\[
\boxed{
\mathfrak M_X(d_X)
\ge8\sqrt X-O(\log^A X)}
\tag{L-23705.16}
\]

and

\[
\boxed{
\Sigma_X(d_X)=O(\log^{A'}X).}
\tag{L-23705.17}
\]

The lower-order mass `mathfrak L_X` is already `O(log^2 X)` by (L-23705.7).
Hence DBT reduces to one scalar theorem:

> **Greedy Slack Theorem.** The total residual slack left by the exact
> minimum-ratio elimination is polylogarithmic.

No estimate of every coefficient and no full Carry Saturation statement is
required.

## 7. Relation to the proposed quotient-layer proof

The eight-step quotient/digit programme should now be reviewed against the
single quantity `Sigma_X`.

- complete quotient layers must account for every final unsaturated column;
- digit conditional variance must pay total slack, not merely an unweighted
  local fluctuation;
- the reflected Selberg square must be localized to the same blocker source;
- every lower-scale route must decrease `Sigma_X` or enter an explicit
  polylogarithmic boundary budget.

Any proof that does not emit this slack ledger has not established DBT.

## 8. Proof boundary

Closed here:

- a universal `sqrt(n)` moment bound for every feasible vector;
- automatic `O(log^2 X)` control of the lower-order DBT mass;
- the exact reduction of the sharp first moment to total final slack.

Open:

- polylogarithmic total slack for the actual greedy target;
- DBT;
- RH.
