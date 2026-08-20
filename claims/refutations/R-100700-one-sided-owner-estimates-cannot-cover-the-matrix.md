# R-100700 — A one-sided owner theorem cannot by itself cover the double-owner matrix

Claim ID: `R-100700`  
Status: **PROVED EXACT SCOPE FIREWALL**  
Created: 2026-08-20  
RH status: **unproved**

The first-owner decomposition fixes the least selected prime but leaves an
arbitrary future Euler product. The largest-prime decomposition fixes the
greatest selected prime but leaves an arbitrary past/cofactor Euler product.

For every ordered prime set with at least three labels, the monomial selecting
only the first and last labels has the same first owner as every monomial
selecting the first label and any interior subset, and the same largest owner
as every monomial selecting the last label and any interior subset. Therefore
neither one-sided partition identifies its interior interval.

The exact common refinement is the pair `(i_-(A),i_+(A))`. Any proof which
uses a first-owner estimate for a future profile and a largest-owner estimate
for a cofactor profile **separately**, without proving that they refer to the
same source occurrence, may spend one monomial twice or leave it unassigned.

`L-100605` and `L-100700` repair this by giving respectively:

```text
one exact coefficient partition;
one convex Hilbert partition with total weight one.
```

This firewall is why `SCME100704` and `LRNM100704` are defined on disjoint
matrix regions rather than on two independently normalized owner trees.
