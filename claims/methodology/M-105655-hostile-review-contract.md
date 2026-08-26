# M-105655 — Hostile review contract for the corrected Cauchy trace frontier

Claim ID: `M-105655`  
Created: 2026-08-27  
Applies to: `R-105654`, `L-105654`, `T-105655`  
RH status: **unproved**

An independent reviewer should attack the packet in the following order.

## A. Binding sibling correction

1. Recompute the two-factor fixture with shallow depths `1,2` and matched deep depths `3,4`.
2. Verify

   ```text
   model overlap = 147/100;
   cross-Dirichlet scalar = 49/60;
   canonical adverse charge = 53/100.
   ```

3. Confirm that the complex cross-Dirichlet scalar is not a positive model-space overlap.
4. Confirm that corrected sibling `L-106514` uses only the valid majorization

   ```text
   canonical charge <= denominator phase statistic.
   ```

5. Reject every dependency which still describes the phase statistic as the exact canonical charge.

## B. One-factor calculation

For a shallow factor of depth `delta` and its matched factor of depth
`delta+2H`, verify

```text
squared model-vector overlap
  = delta(delta+2H)/(delta+H)^2;

phase defect
  = H^2/(delta+H)^2;

exponential/current reserve
  = H/(2delta+H).
```

Check the exact positive difference

```text
H delta^2 / ((delta+H)^2(2delta+H)).
```

No packet conclusion may be inferred by summing these scalar rows without an
explicit model-space theorem.

## C. Cauchy Gram normal form

For `lambda_j` in the open right half-plane and `H>0`, check

```text
G_s(i,j)=1/(conj(lambda_i)+lambda_j+s).
```

Verify:

```text
source trace = tr(G_0^-1 G_H);
matched model overlap
  = tr(G_0^-1 G_(2H) G_(4H)^-1 G_(2H));
```

and hence `CTI105655` is exactly

```text
tr(G_0^-1 G_(2H) G_(4H)^-1 G_(2H))
  >= tr(G_0^-1 G_H).
```

Every inverse is taken only after deleting repeated nodes or using the
confluent limit.

## D. Logical strength

The following substitutions are forbidden:

```text
cross-Dirichlet scalar for canonical overlap;
phase-angle majorant for the exact defect;
scalar addition of nonorthogonal factors;
determinant comparison for trace comparison;
Loewner order when only a trace inequality is proved;
numerical stress tests for a general packet proof.
```

## E. Entire Xi passage

Even a proof of finite `CTI105655` must retain:

```text
canonical-product truncation;
common-zero cancellation;
confluent blocks;
Cartwright exponential carrier;
horizontal endpoints;
cofinal regular-window passage;
terminal derivative review status.
```

The following must remain false until separately proved:

```text
D0PHASE105650 proved for Xi;
POINTID105630 proved;
cofinal endpoint ledger closed;
fixed-width moving saddle authenticated;
Riemann Hypothesis established.
```
