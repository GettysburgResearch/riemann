# L-20207 — Prime-knot concavity on the compact base cell

Claim ID: `L-20207`  
Title: The prime-positive compact-cell minimum occurs at prime-power knots or the two fixed endpoints  
Status: `PROPOSED — COMPLETE ELEMENTARY CONVEXITY PROOF`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20205`; `L-20206`; the decomposition `Psi=F-G` from PR #219  
Scope: fixed `0<a<b<log2`, integer `r>=2`

## 1. Archimedean curvature

Use

\[
 \Psi(t)=F(t)-G(t),
 \qquad
 G(t)=\sum_q{\Lambda(q)\over\sqrt q}(t-\log q)_+.
\]

The explicit archimedean curvature is

\[
\boxed{
 F''(t)=e^{t/2}-{e^{-5t/2}\over1-e^{-2t}}.}
\tag{1}
\]

Its derivative is strictly positive for every `t>0`:

\[
\begin{aligned}
F'''(t)={}&{1\over2}e^{t/2}
+{5\over2}{e^{-5t/2}\over1-e^{-2t}}
+{2e^{-9t/2}\over(1-e^{-2t})^2}>0.
\end{aligned}
\tag{2}
\]

Thus `F''` is strictly increasing on the positive half-line.

## 2. Strict concavity between prime knots

Fix

\[
 0<a<b<\log2.
\]

Then `G(t)=0` for every `t in [a,b]`. Hence

\[
 \mathcal D_r(t)=r^2F(t)-F(rt)+G(rt).
\tag{3}
\]

On an open interval containing no point

\[
 t={\log q\over r}
\]

with `q` a prime power, the function `G(rt)` is affine. Therefore

\[
\begin{aligned}
\mathcal D_r''(t)
&=r^2F''(t)-r^2F''(rt)\\
&<0,
\end{aligned}
\tag{4}
\]

because `rt>t` and `F''` is strictly increasing.

Thus `D_r` is strictly concave on every prime-free cell.

At a prime-power knot `t=log(q)/r`, the function is continuous and its first
derivative jumps upward by

\[
 r{\Lambda(q)\over\sqrt q}>0.
\tag{5}
\]

No other nonsmooth point occurs.

## 3. Exact minimum reduction

Let

\[
 \mathcal K_r(a,b)
 =\{a,b\}
 \cup
 \left\{{\log q\over r}:q\text{ a prime power},\ e^{ra}\le q\le e^{rb}\right\}.
\tag{6}
\]

A concave function on a closed interval attains its minimum at an endpoint.
Applying this separately to every consecutive knot cell gives

\[
\boxed{
 \inf_{a\le t\le b}\mathcal D_r(t)
 =\min_{t\in\mathcal K_r(a,b)}\mathcal D_r(t).}
\tag{7}
\]

This is an exact finite reduction at every `r`. No mesh approximation or
Lipschitz loss enters.

## 4. Global RH criterion on finite knot sets

Combining (7) with `T-20205` gives

\[
\boxed{
 RH
 \iff
 \min_{t\in\mathcal K_r(a,b)}\mathcal D_r(t)\ge0
 \quad\text{for every sufficiently large integer }r.}
\tag{8}
\]

Equivalently,

\[
\boxed{
 RH
 \iff
 \left[-\min_{t\in\mathcal K_r(a,b)}\mathcal D_r(t)\right]_+
 =e^{o(r)}.}
\tag{9}
\]

Each level is now a finite prime-power prefix ledger in the annulus

\[
 e^{ra}\le q\le e^{rb},
\]

plus two endpoint rows. The complete prime sum at a knot still contains all
prime powers up to that knot, but every coefficient is nonnegative by
`L-20206`.

## 5. Knot recurrence

Write the ordered prime-power knots as

\[
 q_1<q_2<\cdots
\]

inside the annulus and let

\[
 t_j={\log q_j\over r}.
\]

Between `t_j` and `t_(j+1)`, the prefix mass

\[
 A_j=\sum_{q\le q_j}{\Lambda(q)\over\sqrt q}
\]

is fixed, so

\[
 \mathcal D_r'(t)
 =r^2F'(t)-rF'(rt)+rA_j.
\tag{10}
\]

The derivative is strictly decreasing on the cell by (4), and at the next knot
it jumps upward by the next atom. Therefore the entire compact-cell shape is
encoded by one monotone archimedean derivative and the finite prime-prefix
masses.

This is the differential form of PR #219's prime polygon: the knot values are
exact polygon deficits, and the upward derivative jumps are the polygon's atom
masses.

## 6. Proof-producing consequence

A cofinal certificate no longer needs interval minimization in `t`. It needs:

1. the two exact endpoint rows;
2. one exact row for every prime power in `[e^(ra),e^(rb)]`;
3. complete prefix moments through each knot;
4. a finite minimum and subexponential lower bound.

A streaming producer can update the knot value and derivative from one prime
power to the next, retaining directed correlation throughout.

## 7. Proof boundary

- The curvature and cell-minimum statements are exact.
- The number of knots grows exponentially with `r`; this lemma supplies a finite
  reduction, not a complexity bound.
- No cofinal lower bound for the knot minima is proved.
- Concavity does not permit checking only the two outer endpoints; every prime
  knot remains a potential minimum because the derivative jumps upward there.
