# X-9306/X-9307 — Real-data exact portfolio-cone decision

This experiment applies L-9308 and the simplicial reduction L-9309 to the
smallest retained atomized shifted basin from PR #103.

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

## Exact breakthrough

For fixed nodes, L-9309 proves that

```text
beta -> P_beta(y)
```

is an isomorphism from zero-sum portfolios to polynomials of degree at most
`n-2`. The monomial-positive L-9308 cone is therefore simplicial. Its complete
set of extreme rays is obtained from

```text
P(y) = 1, y, ..., y^(n-2).
```

Thus `n-1` exact directed basis rows decide:

- the full monomial-positive portfolio cone;
- every such portfolio on every subset of the same nodes;
- every rational or real convex combination after `P(1)=1` normalization.

No optimizer, subset enumeration, or rational postselection is needed in the
proof path.

## Exact basis calculation

For each degree `k`, the checker constructs

```text
beta_i^(k) = -(-u_i)^k / product_{j != i}(u_j-u_i)
```

and verifies exactly:

```text
sum_i beta_i^(k) = 0
P_beta(y) = y^k.
```

It then contracts the exact residual

```text
sum_i beta_i log H_T(u_i)
-
sum_shell count_increment * sum_i beta_i log(u_i+B_shell)
```

using Fraction-only logarithm enclosures. The common power-of-two xi scaling
cancels because every basis vector sums to zero.

A negative upper endpoint is a finite RH-disproof nomination through the parent
analytic/count gates. Nonnegative lower endpoints for all basis rows rigorously
close the entire monomial-positive L-9308 cone at this exact table.

## Exploratory regression

`search.py` retains the earlier numerical LP/subset search as a discovery
regression. It is no longer needed for completeness and does not enter the
L-9309 proof boundary.

## Reproduction

```bash
python basis_check.py \
  --xi ../X-9302-total-count-zero-deflation/results/pr71-shift-fine/p3/xi-primitives-p512.json \
  --complete-result ../X-9302-total-count-zero-deflation/results/complete-result.json \
  --output results/basis.json
```
