# L-90023 — Any feasible packing with subquadratic signed seed-score loss closes RH

Claim ID: `L-90023` (provisional branch range)  
Title: A nonnegative carry packing need only match the deterministic parabolic seed in exact entropy score up to `o(log^2 X)`; unweighted slack, pointwise blocker bounds, and exact saturation are unnecessary  
Status: **PROPOSED COMPLETE EXACT OPTIMIZATION REDUCTION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: `T-90011`; the exact Legendre/Kummer carry identity; PR #265 `L-26201/L-26203`  
Scope: finite packing reduction and endpoint-scale greedy target; the required score estimate remains open

## 1. Positive carry packing

Let `d_X(n)>=0` be any finite row vector satisfying

\[
\boxed{
 \sum_{n\ge q}d_X(n)\beta_{nq}
 \le w_X(q)
 ={1\over\sqrt q}\log{X\over q}
 \qquad(2\le q\le X).
}
\tag{L-90023.1}

Put

\[
\boxed{
 \mathcal S_X(d)
 =\sum_nd_X(n)G_n,
}
\tag{L-90023.2}

where the average-binomial entropy row obeys the exact Legendre/Kummer identity

\[
 G_n=\sum_{q\le n}\Lambda(q)\beta_{nq}.
\tag{L-90023.3}

Since every `Lambda(q)>=0`, feasibility gives

\[
\begin{aligned}
 \mathcal S_X(d)
 &=\sum_q\Lambda(q)
   \sum_n d_X(n)\beta_{nq}\\
 &\le\sum_q\Lambda(q)w_X(q)
 =P_\Lambda(X).
\end{aligned}
\tag{L-90023.4}

No entropy approximation enters this inequality.

## 2. Compare with the positive parabolic seed

Let `d_X^(0)` be the nonnegative parabolic seed of PR #265 `L-26201`. Its exact score is

\[
\boxed{
 J_\Lambda(X)
 =\sum_nd_X^{(0)}(n)G_n
 =\sum_{m=2}^Xb_X(m)\log{m\over m-1}.
}
\tag{L-90023.5}

Define the **signed seed-score loss**

\[
\boxed{
 \mathfrak L_X(d)
 =J_\Lambda(X)-\mathcal S_X(d).
}
\tag{L-90023.6}

The quantity need not be nonnegative: a feasible packing may put more mass than the unweighted seed on favorable endpoint atoms and have a larger entropy score.

Using (L-90023.4),

\[
\boxed{
 F_\Lambda(X)
 =J_\Lambda(X)-P_\Lambda(X)
 \le\mathfrak L_X(d).
}
\tag{L-90023.7}

This is the exact optimization bridge.

## 3. Minimal sufficient theorem

Let

\[
 C_{\rm pp}=-1-\zeta(1/2)>0
\]

be the prime-square source constant of `L-90020`. `T-90011` proves that any fixed upper margin

\[
 \limsup{F_\Lambda(X)\over\log^2X}
 <{C_{\rm pp}\over4}
\]

implies RH.

Therefore it is enough to construct feasible nonnegative packings with

\[
\boxed{
 \limsup_{X\to\infty}
 {\mathfrak L_X(d)\over\log^2X}
 <{C_{\rm pp}\over4}.
}
\tag{L-90023.8}

In particular, the clean target

\[
\boxed{
 \mathfrak L_X(d)=o(\log^2X)
}
\tag{L-90023.9}

implies RH.

Even the one-sided estimate

\[
 \mathfrak L_X(d)\le0
\]

eventually is sufficient. No lower bound for the score loss is required.

## 4. Endpoint-scale greedy target

For the endpoint-scale packing of PR #265,

\[
 d_X^{\rm sc}
 =\sum_{T=3}^X\lambda_Ta_T,
\]

with positive endpoint atoms `a_T`, put

\[
 H_T=\sum_na_T(n)G_n.
\]

The unweighted seed has

\[
 d_X^{(0)}=\sum_{T=3}^Xa_T,
 \qquad
 J_\Lambda(X)=\sum_{T=3}^XH_T.
\]

Therefore the exact signed score loss is

\[
\boxed{
 \mathfrak L_X^{\rm sc}
 =\sum_{T=3}^X(1-\lambda_T)H_T.
}
\tag{L-90023.10}

This is the correct endpoint-scale closing scalar.

Weights `lambda_T>1` contribute favorable negative loss and may compensate entire frozen intervals with `lambda_U=0`. Consequently the older sufficient targets

```text
unweighted total column slack small;
every blocker loss pointwise small;
number of frozen scales bounded;
all scale weights <=1;
```

are strictly stronger than necessary and may destroy the exact continuum cancellation.

## 5. Exact relation to weighted residual slack

Let

\[
 s_X(q)=w_X(q)-\sum_nd_X(n)\beta_{nq}\ge0
\]

and define the von-Mangoldt weighted slack

\[
 \mathfrak W_X(d)=\sum_q\Lambda(q)s_X(q)\ge0.
\tag{L-90023.11}

Equation (L-90023.4) is actually the equality

\[
 \mathcal S_X(d)=P_\Lambda(X)-\mathfrak W_X(d).
\]

Hence

\[
\boxed{
 \mathfrak L_X(d)
 =F_\Lambda(X)+\mathfrak W_X(d).
}
\tag{L-90023.12}

For an explicit packing, any two of

```text
signed seed-score loss;
complete prime-power gap;
weighted residual slack
```

determine the third exactly.

This explains the endpoint-scale reconnaissance in PR #265: its weighted residual slack can be tiny while the packing score exceeds the unweighted seed, corresponding to a negative `mathfrak L_X`.

## 6. Continuum interpretation

PR #265 `L-26202` proves that the continuum parabolic defect admits an ordered transport with nonpositive logarithmic objective cost. In the endpoint-frame coordinate this predicts

\[
 \mathfrak L_X^{\rm sc}\lesssim0
\]

rather than small absolute blocker loss.

Thus (L-90023.10) is the exact finite scalar matching the continuum theorem: signed recombination of all endpoint weights occurs before a positive part or absolute value is taken.

The remaining finite arithmetic problem is now:

> prove that floor/divisor discretization changes the continuum nonpositive score by less than `(C_pp/4-o(1))log^2X`.

This is materially weaker than the previous `ESBT/ESGS` package.

## 7. Proof boundary

Closed exactly:

1. feasible packing score is bounded by the complete prime-power ramp;
2. complete gap is bounded by signed seed-score loss;
3. the `o(log^2 X)` sufficient theorem;
4. the exact endpoint-scale loss formula;
5. the exact identity with weighted residual slack;
6. the scope correction from unsigned slack to signed score.

Open:

1. the score estimate (L-90023.8) or (L-90023.9);
2. a finite ordered-transport proof for the endpoint greedy or another packing;
3. RH.