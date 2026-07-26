# X-9306 — Real-data L-9308 portfolio search

This experiment applies the exact resolvent-polynomial portfolio cone of L-9308
to the smallest retained atomized shifted basin from PR #103.

Inputs are already committed directed artifacts:

```text
xi table:
results/pr71-shift-fine/p3/xi-primitives-p512.json

count/certificate index:
results/complete-result.json

shift:
483/1024

previous best exact order-two determinant:
[8.15927411303488367082543395993660298195214288308488e-104,
 8.15927411303488367082665424432172959892044923176279e-104]
```

## Search domain

The discovery LP enforces exactly:

```text
sum beta_i = 0
P_beta coefficientwise >= 0
P_beta(1) = 1
```

where

```text
P_beta(y) = -sum_i beta_i product_{j != i}(y+u_j).
```

It solves:

- the full primitive point set;
- every three-point subset;
- every four-point subset;
- every contiguous subset of sizes five through ten.

HiGHS is used only for discovery. Every retained direction is converted to exact
rational coefficients, repaired into the response cone with an exact safe
endpoint row if needed, renormalized exactly, and replayed using Fraction-only
logarithm enclosures.

## Sign calculation

The exact residual is

```text
sum_i beta_i log H_T(u_i)
-
sum_shell count_increment * sum_i beta_i log(u_i+B_shell).
```

The common power-of-two xi scaling cancels because `sum beta_i=0`.

A strict upper endpoint below zero is a finite RH-disproof nomination through
L-9308 and the reviewed atomized count interface, pending independent theorem,
count, and special-function reproduction.

A wholly nonnegative output is only a finite search result; it does not prove
positivity of the full response cone outside the enumerated subset families or
at another ordinate.

## Reproduction

```bash
python search.py \
  --xi ../X-9302-total-count-zero-deflation/results/pr71-shift-fine/p3/xi-primitives-p512.json \
  --complete-result ../X-9302-total-count-zero-deflation/results/complete-result.json \
  --output results/search.json
```
