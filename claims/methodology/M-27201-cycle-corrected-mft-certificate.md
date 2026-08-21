# M-27201 — Cycle-corrected MFT certificate

Claim ID: `M-27201`  
Status: **FAIL-CLOSED METHODOLOGY / PRODUCTION SCHEMA**

## Purpose

`L-27204` replaces the unstructured MFT feasibility problem by one canonical
signed tree flow plus uniquely indexed balanced fundamental cycles.

For each endpoint `X`, a proof object should emit

```text
r_X              exact Möbius target divergence;
T                canonical central-tree matrix;
d_tree=T r_X     canonical signed exact flow;
C                balanced fundamental-cycle matrix;
z                sparse cycle coefficients;
d=d_tree+C z     final flow.
```

## Mandatory exact checks

1. Every split in `T`, `C`, and `d` is eta-balanced.
2. Every fundamental cycle has zero node divergence.
3. `partial d_tree=r_X`.
4. `partial d=r_X`.
5. Every coefficient of `d` is nonnegative.
6. Every integer carry column equals `w_X(q)` exactly.
7. The unweighted carry/entropy comparison of `L-27203` is recomputed.
8. The dyadic and `2/3` Mertens projections remain unchanged.
9. The directed ternary mutation `X=10^7,n=63` is repaired by nonzero cycle
   coordinates rather than suppressed.

## Automatic rejection

Reject a certificate that:

- uses an unbalanced intermediate edge;
- changes the node divergence;
- takes a positive part before adding cycles;
- omits one canonical-tree edge created by a cycle;
- reports only LP feasibility without exact reconstruction;
- promotes finite feasibility to a cofinal theorem;
- loses the entropy metric or a fixed-ratio shell mutation.

## Remaining theorem

The exact open statement is to construct such `z_X` for all sufficiently large
`X`, or with total slack `X^o(1)`. The present schema does not assert existence.
