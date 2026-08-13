# Fractional columns and transport disintegration

Date: 2026-08-12  
Branch: `research/gpt56-pro/91101-moment-neutral-shadow-transport`  
PR: #399  
Status: **proposed full factor-54 composition; RH not independently verified**

## 1. Starting obstruction

The rough-prime work had closed:

```text
positive least-prime support routing;
positive SHARP-preserving state completion;
endpoint Schur payment of every projective correction;
exact affine Pascal carry lift on a selected color.
```

The remaining problem was forgetting the color. An affine child of color `m`
was exact on columns `mq`, but its nonnegative response at physical columns not
divisible by `m` had no target ledger. Superposing all children could therefore
spend one physical target column more than once.

## 2. Fractional Pascal Green identity

For a finite seed `F`, the response at a real column `q` is exactly

\[
 \overline v_q(F)
 =\sum_{j\ge1}
 \left[
 F(\lfloor jq\rfloor)-F(\lfloor jq\rfloor+1)
 +2\{jq\}\Delta A_F(\lfloor jq\rfloor)
 \right].
\]

This promotes the complete factor-54 producer to feasibility on every real
column after one global safety factor

\[
 (1+3403/K)^{-1}
\]

and a fixed top omission of width `100000`. The exact replay checks the Green
identity, affine covariance and constants using `Fraction` arithmetic.

Consequently the affine lift of a continuously feasible child is physically
feasible at every integer parent column `Q`, through the fractional child
column `Q/m`.

## 3. Target partition by transport disintegration

`L-90028` gives one positive scale-free Markov kernel from the factor-four block
law `Y` to the complete capped-Gamma target law `H`. A positive source
partition

\[
 \mu=\mu_0+\sum_b\mu_b
\]

therefore induces the exact target partition

\[
 \nu=K_*\mu_0+\sum_bK_*\mu_b.
\]

The rough least-prime labels partition source atoms; the positive state
completion preserves the SHARP ledger `(1,2)`; the Schur correction is paid from
branch-local positive source reserve. Thus each rough color receives its own
positive target portion, and these portions sum to the single physical target.

B-spline quantization is positive and linear, so it preserves this partition.
The finite mismatch, collar, safety factor and top omission are applied once to
the total source, not once per color.

## 4. Proposed conclusion

For every physical column `Q`, branchwise affine covariance and continuous
feasibility give

\[
 \operatorname{Resp}_b(Q)\le\Omega_b(Q).
\]

Target disintegration gives

\[
 \sum_b\Omega_b(Q)\le\Omega_X(Q).
\]

Hence the color-forgetting projection is capacity-contracting. All endpoint
weights remain nonnegative.

The score ledger is favorable under state completion, martingale quantization
and affine lift; the only adverse finite operations cost `O(1)` per reset.
Therefore the proposed composition satisfies

\[
 \mathfrak L_X\le\mathfrak L_{K_X}+O(1),
 \qquad K_X\le c_0X+O(1).
\]

The conditional consumer `T-91101` would then yield

\[
 \mathfrak L_X=O(\log X)=o(\log^2X)
\]

and RH.

## 5. Hostile-review frontier

This is not yet promoted to an accepted proof. The load-bearing checks are:

1. the SHARP functional must be the exact native factor-four source-mass ledger;
2. the completed least-prime colors plus Schur slack must be an exact positive
   partition of that source measure;
3. the scale-free transport must commute with affine dilation before
   quantization;
4. the score recurrence must have the stated orientation and apply the global
   safety loss only once;
5. every proposed dependency must survive independent review.

New files:

```text
L-91324  fractional-column Green identity and continuous reset
X-91112  exact fractional response replay
L-91325  monotone transport disintegration and proposed color closure
X-91113  exact disintegration algebra replay
```

```text
Riemann Hypothesis: PROPOSED COMPOSITION / NOT INDEPENDENTLY VERIFIED
```
