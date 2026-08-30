# L-9503 — Prime-knot convexity and streaming reduction

Claim ID: L-9503  
Title: Strict convexity of every post-`log(2)` prime-power cell and complete finite minimization  
Status: PROPOSED  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: D-9501  
Scope: scalar `Psi` search and reusable primitive table for all Issue #95 matrices  
Related counterexample candidates: none yet

## Statement

Let

\[
 B=\frac12\left(\psi\!\left(\frac14\right)-\log\pi\right),
 \qquad C=\pi^2+8G,
\]

and define the smooth non-prime part of `Psi` by

\[
 A(t)=4(e^{t/2}+e^{-t/2}-2)+Bt
 +\frac14\left(C-e^{-t/2}\Phi(e^{-2t},2,1/4)\right).
\tag{L-9503.1}
\]

For every `t>0`, it has the absolutely convergent form

\[
 A(t)=4(e^{t/2}-2)+Bt+\frac C4
 -4\sum_{m=1}^{\infty}
   \frac{e^{-(4m+1)t/2}}{(4m+1)^2}.
\tag{L-9503.2}
\]

Let `q_j`, `tau_j`, `w_j`, `P_0,j`, and `P_1,j` be as in `D-9501`.  On every
prime-power cell

\[
 I_j=[\tau_j,\tau_{j+1}],
\]

we have

\[
 \Psi(t)=A(t)-tP_{0,j}+P_{1,j}.
\tag{L-9503.3}
\]

The derivatives in the open cell are

\[
 A'(t)=2e^{t/2}+B
 +\operatorname{arctanh}(e^{-t/2})
 +\arctan(e^{-t/2})-2e^{-t/2},
\tag{L-9503.4}
\]

and

\[
 A''(t)=e^{t/2}
 -\frac{e^{-5t/2}}{1-e^{-2t}}.
\tag{L-9503.5}
\]

Let `rho_pl` be the unique positive root of

\[
 y^3-y-1=0
\]

(the plastic constant).  Then

\[
 A''(t)>0
 \quad\Longleftrightarrow\quad
 t>\log\rho_{\rm pl}.
\tag{L-9503.6}
\]

In particular, every cell beginning at a prime power is strictly convex,
because

\[
 \log 2>\log\rho_{\rm pl},
 \qquad
 A''(t)\ge A''(\log2)=\frac{5}{3\sqrt2}>0
 \quad(t\ge\log2).
\tag{L-9503.7}
\]

Consequently the minimum of `Psi` on `I_j` occurs at exactly one of:

1. the left knot `tau_j`;
2. the right knot `tau_{j+1}`;
3. the unique interior solution of
   \[
      A'(t)=P_{0,j},
   \tag{L-9503.8}
   \]
   when the one-sided endpoint derivatives have opposite signs.

Thus the exact minimum of `Psi` on any finite interval
`[log 2, log Q]` is reduced to finitely many knot values and at most one
monotone root per prime-power cell.  No mesh or Lipschitz extrapolation is
needed.

Finally, for `t in I_j`, there is a cancellation-resistant local recurrence

\[
 \Psi(t)=\Psi(\tau_j)
 +A(t)-A(\tau_j)-P_{0,j}(t-\tau_j),
\tag{L-9503.9}
\]

and in particular

\[
 \Psi(\tau_{j+1})=\Psi(\tau_j)
 +A(\tau_{j+1})-A(\tau_j)
 -P_{0,j}(\tau_{j+1}-\tau_j).
\tag{L-9503.10}
\]

The recurrence needs only the current directed value of `Psi` and the single
prefix `P_0,j`; the two-prefix form (L-9503.3) remains available for
independent checkpoints.

## Proof

Expanding the Lerch term gives

\[
 e^{-t/2}\Phi(e^{-2t},2,1/4)
 =16\sum_{m=0}^{\infty}
   \frac{e^{-(4m+1)t/2}}{(4m+1)^2}.
\]

The `m=0` contribution cancels the `4e^{-t/2}` term in (L-9503.1), proving
(L-9503.2).

On `I_j`, precisely the prime powers `q_r` with `r<=j` have been deposited.
Their contribution is

\[
 -\sum_{r\le j}w_r(t-\tau_r)
 =-tP_{0,j}+P_{1,j},
\]

which proves (L-9503.3).  At an endpoint the newly arriving summand is zero,
so the formula agrees continuously from both sides.

Differentiate (L-9503.2).  With `x=e^{-t/2}`,

\[
 2\sum_{m=1}^{\infty}\frac{x^{4m+1}}{4m+1}
 =\operatorname{arctanh}x+\arctan x-2x,
\]

which gives (L-9503.4).  Differentiating once more gives

\[
\begin{aligned}
 \frac{d}{dt}
 \left(\operatorname{arctanh}x+\arctan x-2x\right)
 &=-\frac{x^5}{1-x^4},
\end{aligned}
\]

and hence (L-9503.5).

Since `t>0`, the denominator in (L-9503.5) is positive.  Put `y=e^t>1`.
Then

\[
 A''(t)>0
 \Longleftrightarrow
 e^{t/2}(1-e^{-2t})>e^{-5t/2}
 \Longleftrightarrow
 y^3-y-1>0.
\]

The polynomial has derivative `3y^2-1>0` on `y>=1`, is negative at `1`, and
tends to infinity, so it has one root there and (L-9503.6) follows.  Because
`2^3-2-1=5>0`, all prime-power cells lie beyond the threshold.

Moreover, write

\[
 h(t)=\frac{e^{-5t/2}}{1-e^{-2t}}
     =\frac{x^5}{1-x^4}.
\]

The function `x^5/(1-x^4)` is strictly increasing in `x in (0,1)`, while
`x=e^{-t/2}` decreases, so `h'(t)<0`.  Therefore

\[
 A'''(t)=\frac12e^{t/2}-h'(t)>0.
\]

Thus `A''` is increasing and its post-`log2` lower bound is its value at
`log2`, namely `5/(3sqrt2)`.  Inside a cell,

\[
 \Psi'(t)=A'(t)-P_{0,j},
 \qquad
 \Psi''(t)=A''(t)>0.
\]

The derivative is strictly increasing, proving the three-way minimum
classification and uniqueness of (L-9503.8).

Subtracting (L-9503.3) at `t` and at `tau_j` proves (L-9503.9), and setting
`t=tau_{j+1}` proves (L-9503.10).  QED.

## Strong-convexity cell certificate

Let

\[
 \mu_j=A''(\tau_j)>0.
\]

For every `x,y in I_j`, strict convexity and monotonicity of `A''` give

\[
 \Psi(y)\ge
 \Psi(x)+\Psi'(x)(y-x)+\frac{\mu_j}{2}(y-x)^2.
\]

Minimizing the right-hand quadratic over the whole real line yields the
rigorous lower bound

\[
 \min_{y\in I_j}\Psi(y)
 \ge
 \Psi(x)-\frac{\Psi'(x)^2}{2\mu_j}.
\tag{L-9503.11}
\]

Therefore a proof backend need not enclose the stationary point extremely
tightly.  It suffices to find a directed point enclosure `x` for which the
right side of (L-9503.11) has positive lower endpoint.  Conversely, any exact
`x` whose directed `Psi(x)` has negative upper endpoint is already a scalar
counterexample by Suzuki's pointwise criterion.

A universal but weaker choice is `mu=5/(3sqrt2)` for every cell after
`log2`.

## Explicit smooth-series tail

For

\[
 r_m(t)=\frac{e^{-(4m+1)t/2}}{(4m+1)^2},
\]

the ratio satisfies

\[
 \frac{r_{m+1}(t)}{r_m(t)}
 =e^{-2t}\left(\frac{4m+1}{4m+5}\right)^2
 \le e^{-2t}.
\]

Hence, after retaining terms through `m=M`,

\[
 0<\sum_{m>M}r_m(t)
 \le
 \frac{r_{M+1}(t)}{1-e^{-2t}}.
\tag{L-9503.12}
\]

For `t>=log2`, the geometric ratio is at most `1/4`.  This gives a tiny,
transparent alternative to a black-box Lerch evaluator.

## Computational significance

A complete scalar pass through a cutoff `Q` can stream the sorted prime-power
manifest once:

1. carry `P_0,j` and the current knot enclosure;
2. classify the cell by the two directed endpoint derivatives;
3. evaluate a stationary candidate only when a sign change occurs;
4. certify the whole cell with (L-9503.11);
5. update the next knot by (L-9503.10);
6. periodically reconstruct the knot from the independent two-prefix formula
   (L-9503.3) to prevent unnoticed drift.

This replaces billions of huge phases by monotone real arithmetic.  The local
recurrence also avoids subtracting two quantities of size about `exp(t/2)` to
recover a value conjecturally of order one.

## Analytic domain audit

All series are absolutely convergent for `t>0`.  Differentiation is justified
uniformly on compact subsets of `(0,infinity)`.  At prime-power knots the
function is continuous but only one-sided first derivatives are used.  No
claim differentiates through a knot.

## Dependency audit

Only the explicit prime formula in `D-9501` is used.  The convexity theorem is
unconditional and does not use RH.  RH enters only when a negative value is
interpreted as a counterexample via Suzuki's imported theorem.

## Gap audit

- `P_0,j` must include every higher prime power exactly once.
- The cell formula changes at `tau_{j+1}` even though the value is continuous.
- A binary64 root of (L-9503.8) is reconnaissance only.
- Long interval recurrences can accumulate width; shard checkpoints from
  (L-9503.3) are mandatory in a production pass.
- The lower bound (L-9503.11) must be evaluated with correlated/directed
  quantities.  Squaring a wide derivative interval naively can lose the
  certificate but cannot justify narrowing it.
- Formula (L-9503.12) bounds the smooth tail only; it says nothing about
  omitted prime powers.

## Adversarial tests

1. Symbolically differentiate (L-9503.2) and compare with (L-9503.4).
2. Verify the convexity threshold by substituting `y=e^t` in both directions.
3. Check `A''(log2)=5/(3sqrt2)` exactly.
4. On a small manifest, compare every knot value from (L-9503.3) and
   (L-9503.10).
5. For each stationary cell, verify opposite directed endpoint derivative
   signs before bisection.
6. Perturb a cutoff through a prime power and require exactly one new
   zero-valued deposition followed by the correct derivative jump.

## Remaining uncertainty

The mathematical reduction is complete, but no directed billion-term run has
been performed.  It is not yet known whether scalar positivity remains far
from zero at the repository's largest available prime cutoff.

## Suggested next attack

Implement a segmented, checkpointed Arb producer over the existing complete
prime-power manifest.  Rank cells by the strong-convexity lower bound and
retain the smallest certified margins as exact scalar and matrix nodes for
`L-9501` and `L-9502`.
