# L-91102 — Moment-neutral endpoint butterflies are compact and score-improving

Claim ID: `L-91102` (provisional research range)  
Title: The endpoint entropy density is strictly convex in the rank-two state coordinate; every adjacent martingale butterfly is a four-row, strictly score-positive move, and every detail-feasible convex-order spread has nonpositive signed score loss  
Status: **PROPOSED COMPLETE EXACT SCORE / CONVEX-ORDER THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-11  
Depends on: `L-91101`; PR #265 endpoint entropy; PR #352 `L-90029`  
Scope: exact score geometry and a new sufficient producer theorem; existence of the required feasible spread remains open

## 1. Endpoint entropy density

Let
\[
 \ell_m=\log\frac m{m-1},
\]
and retain the endpoint entropy score
\[
 H_T=\sum_na_T(n)G_n.
\]
Finite switching gives
\[
 H_T
 =
 \sum_{m=2}^{T-1}e_T(m)\ell_m.
\tag{L-91102.1}
\]

Put
\[
 P_N=\sum_{m=2}^{N}\sqrt m\,\ell_m,
 \qquad
 Q_N=\sum_{m=2}^{N}m\,\ell_m.
\tag{L-91102.2}
\]
Using
\[
 e_T(m)=\alpha_T\sqrt m-\delta_Tm
\]
and \(r_T=\delta_T/\alpha_T\),
\[
\boxed{
 H_T=\alpha_Th_T,
 \qquad
 h_T=P_{T-1}-r_TQ_{T-1}.
}
\tag{L-91102.3}
\]

Thus \(h_T\) is the entropy score per unit endpoint-state mass.

## 2. Exact adjacent chord slopes

Define the chord slope between the adjacent state nodes \(r_{T+1}<r_T\):
\[
 \sigma_T
 =
 \frac{h_T-h_{T+1}}{r_T-r_{T+1}}.
\tag{L-91102.4}
\]

Since
\[
 P_T=P_{T-1}+\sqrt T\,\ell_T,
 \qquad
 Q_T=Q_{T-1}+T\ell_T,
\]
direct subtraction gives
\[
\boxed{
 \sigma_T=-Q_{T-1}-B_T,
}
\tag{L-91102.5}
\]
where
\[
\boxed{
 B_T
 =
 \ell_T\sqrt T\,
 \frac{1-r_{T+1}\sqrt T}{r_T-r_{T+1}}>0.
}
\tag{L-91102.6}
\]

The positivity follows from
\[
 r_{T+1}<T^{-1/2}.
\]
Moreover \(r_T>T^{-1/2}\), so
\[
 1-r_{T+1}\sqrt T
 <
 \sqrt T(r_T-r_{T+1}),
\]
and therefore
\[
\boxed{
 0<B_T<T\ell_T.
}
\tag{L-91102.7}
\]

Now
\[
\begin{aligned}
 \sigma_{T+1}-\sigma_T
 &=-T\ell_T-B_{T+1}+B_T\\
 &<-B_{T+1}<0.
\end{aligned}
\tag{L-91102.8}
\]

Because the nodes \(r_T\) decrease with \(T\), (L-91102.8) is exactly strict convexity of the polygonal interpolation through the points
\[
 (r_T,h_T).
\]

Hence
\[
\boxed{
 h\ \text{is strictly convex and strictly decreasing as a function of }r.
}
\tag{L-91102.9}
\]

The monotonicity follows because every \(\sigma_T<0\).

## 3. Adjacent butterflies strictly improve the score

For \(T\ge4\), let
\[
 \theta_T
 =
 \frac{r_T-r_{T+1}}{r_{T-1}-r_{T+1}},
\]
and define the endpoint butterfly
\[
 \mathcal B_T
 =
 c_T^-a_{T-1}-a_T+c_T^+a_{T+1},
\tag{L-91102.10}
\]
where
\[
 c_T^-=\frac{\alpha_T\theta_T}{\alpha_{T-1}},
 \qquad
 c_T^+=\frac{\alpha_T(1-\theta_T)}{\alpha_{T+1}}.
\tag{L-91102.11}
\]

`L-91101` proves
\[
 \operatorname{supp}\mathcal B_T
 \subseteq\{T-3,T-2,T-1,T\}.
\tag{L-91102.12}
\]

Its entropy gain is
\[
\begin{aligned}
 E_T
 &: =
 c_T^-H_{T-1}-H_T+c_T^+H_{T+1}\\
 &=
 \alpha_T\left[
 \theta_Th_{T-1}
 +(1-\theta_T)h_{T+1}
 -h_T
 \right].
\end{aligned}
\tag{L-91102.13}
\]
Since
\[
 r_T=\theta_Tr_{T-1}+(1-\theta_T)r_{T+1},
\]
strict convexity gives
\[
\boxed{
 E_T>0.
}
\tag{L-91102.14}
\]

Thus every elementary mean-preserving spread of endpoint state mass:

```text
preserves the two inherited bulk moments;
changes only four boundary rows;
strictly increases the exact entropy score.
```

This is a finite arithmetic martingale \(T\)-transform.

## 4. A summable local score budget

Let
\[
 \Delta r_T=r_{T-1}-r_{T+1}.
\]
The convexity gap in (L-91102.13) is bounded by
\[
 \frac{\Delta r_T}{4}
 (\sigma_T-\sigma_{T+1}).
\tag{L-91102.15}
\]

From the interval-mean bounds of `L-91101`,
\[
 \Delta r_T
 <
 (T-2)^{-1/2}-(T+1)^{-1/2}
 <
 \frac3{2(T-2)^{3/2}}.
\tag{L-91102.16}
\]

Also
\[
 \sigma_T-\sigma_{T+1}
 =T\ell_T+B_{T+1}-B_T
 <T\ell_T+(T+1)\ell_{T+1}<3
\tag{L-91102.17}
\]
for \(T\ge4\), by \(\log(1+x)<x\).

Finally
\[
 \alpha_T=2\log\frac T{T-1}<\frac2{T-1}.
\]
Combining these estimates,
\[
 E_T
 <
 \frac{9}{4(T-1)(T-2)^{3/2}}.
\tag{L-91102.18}
\]
For \(T\ge4\),
\[
 4(T-1)(T-2)^{3/2}>T^{5/2},
\]
using \(T-1\ge3T/4\) and \(T-2\ge T/2\). Therefore
\[
\boxed{
 0<E_T<9T^{-5/2}.
}
\tag{L-91102.19}
\]

The complete available local butterfly gain is absolutely summable. Numerically the sharper asymptotic appears to be
\[
 T^{5/2}E_T\longrightarrow\frac12,
\]
but this asymptotic is not used here.

## 5. Convex-order score theorem

Let \(\lambda_T\ge0\) be endpoint weights on a finite interval, and compare them with baseline weights \(1\). Define the signed state measure
\[
\boxed{
 \eta_\lambda
 =
 \sum_T(\lambda_T-1)\alpha_T\delta_{r_T}.
}
\tag{L-91102.20}
\]

Assume the two moment constraints
\[
 \eta_\lambda(1)=0,
 \qquad
 \eta_\lambda(r)=0.
\tag{L-91102.21}
\]

Then
\[
 \sum_T(\lambda_T-1)H_T
 =
 \int h(r)\,d\eta_\lambda(r).
\tag{L-91102.22}
\]

If \(\eta_\lambda\) is nonnegative in convex order,
\[
 \int\phi\,d\eta_\lambda\ge0
 \qquad\text{for every convex }\phi,
\tag{L-91102.23}
\]
then strict convexity of \(h\) gives
\[
\boxed{
 \sum_T(\lambda_T-1)H_T\ge0.
}
\tag{L-91102.24}
\]

Equivalently, the signed seed-score loss of PR #352,
\[
 \mathfrak L_X^{(4)}
 =
 \sum_T(1-\lambda_T)H_T,
\]
satisfies
\[
\boxed{
 \mathfrak L_X^{(4)}\le0.
}
\tag{L-91102.25}
\]

By `L-91101`, condition (L-91102.23) is equivalent to a nonnegative adjacent-butterfly decomposition. Therefore no abstract convex-order theorem is being assumed: the admissible perturbation is an explicit finite sum of compact four-row packets.

## 6. A new RH-sufficient producer theorem

PR #352 `L-90029` proves that any nonnegative radix-four-detail-feasible endpoint weights satisfy
\[
 F_\Lambda(X)\le\mathfrak L_X^{(4)},
\]
and that \(\mathfrak L_X^{(4)}=o(\log^2X)\) implies RH.

Combining this with Section 5 gives:

> **Moment-Neutral Convex-Order Packing Criterion.**  
> Suppose that for every sufficiently large \(X\) there are endpoint weights \(\lambda_T\ge0\) such that:
>
> 1. the radix-four detail constraints are feasible;
> 2. the two endpoint moments in (L-91102.21) are preserved;
> 3. the endpoint state perturbation is a convex-order spread.
>
> Then
> \[
> \mathfrak L_X^{(4)}\le0
> \]
> and RH follows.

In symbols,
\[
\boxed{
 \text{detail feasibility}
 +\text{moment-neutral convex-order spread}
 \Longrightarrow
 \mathfrak L_X^{(4)}\le0
 \Longrightarrow
 \mathrm{RH}.
}
\tag{L-91102.26}
\]

The missing theorem is now an existence theorem for a positive finite transport, not an estimate of an oscillatory arithmetic sum.

## 7. Killed or shadow transport

Exact moment preservation may be too rigid near the finite boundary. A more flexible decomposition is
\[
 \eta_\lambda=\eta_{\rm cx}-\kappa,
\tag{L-91102.27}
\]
where

- \(\eta_{\rm cx}\) is a nonnegative convex-order increment;
- \(\kappa\ge0\) is killed endpoint mass.

Then
\[
 \sum_T(\lambda_T-1)H_T
 \ge
 -\int h\,d\kappa,
\tag{L-91102.28}
\]
so
\[
\boxed{
 \mathfrak L_X^{(4)}
 \le
 \int h\,d\kappa.
}
\tag{L-91102.29}
\]

Because \(h\) decreases with \(r\), killing mass at the largest \(r\)-nodes—equivalently the smallest endpoint scales—has the smallest score cost. This predicts a canonical structure:

```text
kill an initial endpoint prefix;
spread the remaining state mass by adjacent martingale butterflies;
use only compact four-row boundary packets.
```

This is the one-dimensional **moment-neutral shadow packing** architecture. It is the endpoint analogue of a partial or shadow martingale transport with a cemetery state.

## 8. Exact butterfly-coordinate objective

If
\[
 \lambda
 =
 \mathbf1
 +\sum_T\eta_T\,b_T^{\rm row}
 -z,
\qquad
 \eta_T\ge0,\ z_T\ge0,
\tag{L-91102.30}
\]
where \(b_T^{\rm row}\) is the coefficient vector of \(\mathcal B_T\), then the score is exactly
\[
\boxed{
 \mathfrak L_X^{(4)}
 =
 \sum_Tz_TH_T-\sum_T\eta_TE_T.
}
\tag{L-91102.31}
\]

Thus the objective has no hidden global arithmetic term:

```text
prefix-killing cost
minus
local martingale-curvature gain.
```

The detail constraints remain linear and positive. This is the proposed coordinate for the next attack.

## 9. Proof boundary

Closed exactly, subject to review:

1. the endpoint entropy density and exact chord slopes;
2. strict convexity and monotonicity in the rank-two state coordinate;
3. compact support and strict score gain of every adjacent butterfly;
4. a summable explicit gain bound;
5. the convex-order score theorem;
6. the moment-neutral convex-order RH criterion;
7. the killed/shadow score bound;
8. the exact local butterfly-coordinate objective.

Still open:

1. construction of detail-feasible moment-neutral or killed-shadow weights;
2. a finite left-curtain/shadow lift of the continuum block transport;
3. a proof that the killing cost is \(o(\log^2X)\), or is paid by butterfly gain;
4. RH.
