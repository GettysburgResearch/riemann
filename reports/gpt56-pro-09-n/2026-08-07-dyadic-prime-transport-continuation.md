# Full-problem continuation — dyadic prime transport

Date: 2026-08-07  
Agent: `gpt56-pro-09-n`  
Status: **PROPOSED; RH remains unproved and undisproved**

## Step back

The preceding Haar/r-adic work reduced RH to one-sided dilation defects. The fixed compact-cell version still used physical intervals whose width grew with the dilation parameter. This continuation replaces that geometry by a tiled shrinking schedule and then aligns the schedule with exact dyadic prime blocks.

## New theorem chain

### Curvature-corrected prime polygon

`L-20208` proves that at every prime knot the compact-cell defect is

```text
prime-polygon transport reserve
-
Bregman curvature penalty.
```

`L-20209` identifies the penalty with a dual Bregman divergence and proves the sharp sufficient bound

```text
penalty <= [A-H'(T)]^2/(2m).
```

`T-20206` composes these identities with the endpoint/knot minimum theorem and the compact-cell Landau criterion.

### Shrinking-cell tiling

`T-20207` uses

```text
I_r=[a,a+a/r],
J_r=[ra,(r+1)a].
```

The physical cells tile the complete tail and have constant logarithmic width. The small scale remains before the first prime knot. A subexponential negative-part bound on the defects yields a subexponential upper bound for `Psi`; Landau applied to `-Psi` gives RH.

`L-20210` supplies the uniform Taylor normal form and a curvature condition number bounded independently of `r`.

### Exact dyadic schedule

`T-20208` sets `a=log 2`. The small-scale ramp then contains only `q=2`; adding the explicit correction

```text
r^2 log(2)/sqrt(2) * (t-log 2)
```

cancels it exactly. All remaining prime coefficients are nonnegative, and the physical support is the exact dyadic block

```text
[2^r,2^(r+1)].
```

The correction is only `O(r)`, so the corrected all-positive criterion remains RH-equivalent.

`L-20211` gives a streaming baseline-plus-positive-ramps formula. `L-20212` stitches adjacent dyadic endpoints through one explicit `O(r)` archimedean edge term.

## Exact finite proof object

`X-20203` is a standard-library integer/Fraction regression for:

- primal/dual margin equality;
- Bregman penalty;
- strong-convexity square gate;
- quantile-transport recurrence;
- strict positive, zero, and negative synthetic rows;
- eight mutation tests.

It is synthetic algebra only.

## Current full theorem

It is sufficient to prove, for every prime-power knot `T_j=log q_j` in the dyadic block and every sufficiently large `r`,

```text
H_r^*(A_j)-B_j
 >= [A_j-H_r'(T_j)]^2/(2m_r)-exp(o(r)),
```

with the stitched endpoint ledger.

Here:

- the left side is the one-sided quantile-transport reserve;
- the numerator is the centered cumulative prime-mass square;
- the denominator is the explicit renormalized archimedean curvature.

This is the exact interface to Selberg/prime-pair energy. A plain `L2` or phase-blind PNT estimate is insufficient because it discards the reserve orientation.

## Serious resolution path

The preferred attack is now:

```text
Selberg / prime-pair block identity
    -> one-sided quantile transport reserve
    -> curvature-normalized discrepancy square
    -> all-positive dyadic defect
    -> shrinking-cell Landau theorem
    -> RH.
```

The remaining theorem is global and arithmetic; no finite positive ladder can replace it.
