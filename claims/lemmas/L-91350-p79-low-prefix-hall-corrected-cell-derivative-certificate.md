# L-91350 — Corrected cell-derivative certification closes every finite `P_79` one-prime Hall prefix

Claim ID: `L-91350`  
Status: **PROVED DIRECTED FINITE-PARAMETER THEOREM**  
Created: 2026-08-13  
Depends on: `L-91342`, `L-91345-p79-one-prime-splice-has-a-monotone-two-ledger-kernel-and-large-prefix-reserve.md`; `R-91308`; `X-91127`  
RH status: **unproved**

## 1. One-prime prefix margin

Let

\[
 P_{79}=\prod_{q\le79}q,
 \qquad p\ge83,
 \qquad1\le y<83.
\]

For `a=4` (SHARP target) or `a=5` (endpoint score), define

\[
 K_a(d;p,y)
 =d^{-1/2}[a\sqrt{py/d}-3]\mathbf1_{d\le py}
 -p^{-1/2}d^{-1/2}[a\sqrt{y/d}-3]\mathbf1_{d\le y}.
\]

At an odd squarefree threshold `t<4096`, the shifted-eight Hall margin is

\[
 \mathcal H_{a,t}^{(8)}(p,y)
 =\sum_{\substack{e\le t+8\\\mu(e)=1}}K_a(e;p,y)
 -\sum_{\substack{o\le t\\\mu(o)=-1}}K_a(o;p,y).
\tag{L-91350.1}
\]

## 2. Reduction in the prime parameter

Let

\[
 A_t=\sum_{e\le t+8,\mu(e)=1}\frac1e
     -\sum_{o\le t,\mu(o)=-1}\frac1o,
\]

\[
 B_t=\sum_{e\le t+8,\mu(e)=1}\frac1{\sqrt e}
     -\sum_{o\le t,\mu(o)=-1}\frac1{\sqrt o},
\]

and let `A_t(y),B_t(y)` denote the same prefixes with the additional cutoff
`d<=y`.  With `s=sqrt(y)` and `u=sqrt(p)`, one has exactly

\[
 \boxed{
 \mathcal H_{a,t}^{(8)}(p,y)
 =a s\left(uA_t-\frac{A_t(y)}u\right)
  -3B_t+\frac{3B_t(y)}u.
 }
\tag{L-91350.2}

Its derivative in `u`, after multiplication by `u^2`, is

\[
 a s(A_tu^2+A_t(y))-3B_t(y).
\]

The shifted child Hall margin is positive at every child-cell endpoint by the
terminal `P_79` theorem and the additional nonnegative even capacity through
`t+8`.  Hence (L-91350.2) increases with `u` on the admissible range.  It is
enough to take

\[
 p=\max(83,t/y).
\tag{L-91350.3}
\]

## 3. Correct finite cell analysis

The child prefixes change only at divisors of `P_79` below `83`, and at the
switch point `y=t/83`.

If `y>=t/83`, then `p=83`; the margin is affine in `sqrt(y)` on each activation
cell, so its minimum is at one endpoint.

If `y<=t/83`, then `p=t/y`.  On one activation cell the margin is

\[
 H(s)=C+\frac{-aA_t(y)s^2+3B_t(y)s}{\sqrt t}.
\tag{L-91350.4}
\]

For `A_t(y)>=0`, this is concave and its cell minimum is at an endpoint.  For
`A_t(y)<0`, its derivative numerator is

\[
 -2aA_t(y)s+3B_t(y).
\tag{L-91350.5}
\]

The directed checker evaluates (L-91350.5) at both endpoints and proves it has
one sign throughout every active cell.  Thus no convex vertex lies in an active
cell; the minimum is again at an endpoint.  This is the corrected step fenced
by `R-91308`.

## 4. Directed certificate

`X-91127` uses exact `Fraction` arithmetic and rational square-root enclosures
with denominator `10^30`.  It checks:

```text
all odd P_79 thresholds t<4096;
all child activation cells 1<=y<83;
the switch y=t/83;
both a=4 and a=5;
all child Hall endpoint gates;
all Hall endpoint gates;
all convex-cell derivative sign gates.
```

The replay executes

\[
 \boxed{383472}
\]

directed inequalities and proves

\[
 \boxed{
 \mathcal H_{4,t}^{(8)}(p,y)>1,
 \qquad
 \mathcal H_{5,t}^{(8)}(p,y)>1
 }
\tag{L-91350.6}

for every

\[
 p\ge83,
 \qquad1\le y<83,
 \qquad t<4096.
\]

The directed lower margins are in fact above `4.31` for target and `5.27` for
score, so no close floating-point sign decision is involved.

Together with `L-91345`, which closes every threshold `t>=4096`, this proves all
scalar target and score Hall gates for the `P_79` one-prime splice.

## 5. Scope

The theorem gives separate target and score Hall feasibility.  It does not by
itself identify a common transport or type the inherited row.  Those interfaces
must be closed by a separate packet theorem or by the direct positive row splice.

```text
finite target Hall gates         DIRECTED EXACT
finite score Hall gates          DIRECTED EXACT
large-prefix gates               ANALYTICALLY CLOSED
common target/score packet       SEPARATE
inherited row typing             SEPARATE
Riemann Hypothesis               UNPROVED
```
