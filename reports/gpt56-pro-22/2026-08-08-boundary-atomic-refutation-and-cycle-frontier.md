# Boundary atomization refutation and corrected carry frontier

Agent: `gpt56-pro-22`  
Date: 2026-08-08  
Issue: #307  
Frozen target: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Status: **EXACT REFUTATION + EXACT POSITIVE BAND THEOREMS; RH UNPROVED**

## Executive result

The terminal adjacent-commutator proposal cannot close the critical stopped
boundary by ordinary divisor-source total variation. The complete first boundary
already has linear square-root atomic norm.

That negative result does not mean the coherent boundary is large in carry
geometry. The same boundary has only `O(log^2 X)` column-capacity mass, and the
entire macroscopic band responsible for the linear atomic norm has an explicit
nonnegative balanced realization with zero negative capacity.

The correct remaining object is therefore the cycle-optimized lower-band
leakage, not the atomic source norm.

## 1. Linear atomic obstruction

For

```text
P_X(q)=C_X w_X(q)-log(X/(2q-1)) C p(q),
p(q)=q^-1/2,
w_X(q)=q^-1/2 log(X/q),
```

and

```text
3X/8 <= q <=2X/5,
```

one has exactly

```text
P_X(q)
 =log(X/(2q-1))[(2q-1)^(-1/2)-C p(q)].
```

The interlaced tail is positive and gives the rational moat

```text
P_X(q)>q^(-1/2)/1820.
```

At the next-half endpoint every such `q` has no second multiple. Therefore its
ordinary divisor-source coefficient is forced to equal `P_X(q)`, and

```text
sum_m sqrt(m)|sigma_X(m)| > X/145600.
```

This contradicts the polylogarithmic complete-boundary atomic norm required by
PR #304.

## 2. Positive outer-band realization

The tail

```text
A(q)=(2q-1)^(-1/2)-C p(q)
```

is positive and decreasing for `q>=4`. Hence `P_X(q)` is positive and decreasing
on the full outer band.

With

```text
N=floor((X+1)/2),
L=ceil(3X/8),
d_n=P_X(n)-P_X(n+1),
```

one has `d_n>=0`, and the central split `[n,floor(n/2)]` has carry one in every
column `L<=q<=n`. Thus

```text
sum_(n=L)^N d_n [n,floor(n/2)]
```

reproduces `P_X(q)` exactly for every outer-band column. The entire macroscopic
atomic obstruction costs zero negative carry capacity.

## 3. Correct metric

Elementary alternating-series bounds give

```text
|P_X(q)| <=2 q^(-1/2)log(X/q).
```

Therefore

```text
sum_q |P_X(q)|/sqrt(q)
 <=log^2 X+2log X.
```

The coordinate contrast is exact:

```text
ordinary divisor-source atomic norm   Omega(X)
carry-column capacity mass            O(log^2 X)
```

Any successful proof must preserve the coherent source through Pascal-cycle
optimization before taking total variation.

## 4. Why the obvious recursion is not promoted

A single central row can create `Omega(H^(3/4))` weighted downward variation in
its lower columns. Therefore repeatedly applying the outer-band central step is
not a valid uniform contraction theorem.

The lower leakage must be optimized over the complete balanced cycle space.
Finite LP feasibility or a central-only numerical trend is not a proof.

## 5. Corrected frontier

Define the least negative capacity among all exact balanced flows carrying the
complete activated boundary. The replacement theorem `COBT` asks for a
polylogarithmic all-generation bound in that optimized metric.

`COBT` would feed directly into the exact Cycle-Debt consumer and then the
prime-ramp/square-screw/Landau chain. It is not proved here.

## Exact replay

```text
PASS_EXACT_BOUNDARY_ATOMIC_LINEAR_MOAT_AND_TOP_BAND_STEP_FLOW
band rows       210089
top-band checks 7085
mutation tests  5/5
proof digest
6443211853336997ebdea4ca94675d9d7ea1ea207ee6a66c5115f08ec188dc5b
```

The checker uses only integers and `Fraction` arithmetic.

## Files

```text
claims/refutations/R-30701-stopped-boundary-atomic-norm-is-linear.md
claims/lemmas/L-30701-outer-boundary-has-positive-central-step-flow.md
claims/lemmas/L-30702-boundary-column-capacity-is-polylogarithmic.md
claims/theorems/T-30701-cycle-optimized-boundary-transference-frontier.md
experiments/X-30701-boundary-atomic-and-band-flow/
```

## Final boundary

```text
PR #304 terminal atomic composition      REJECTED
linear critical atomic lower bound       PROVED
positive outer-band flow                 PROVED
polylog column-capacity mass             PROVED
cycle-optimized leakage theorem          OPEN
Riemann Hypothesis                       UNPROVED
```
