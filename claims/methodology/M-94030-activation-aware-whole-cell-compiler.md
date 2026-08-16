# M-94030 — Activation-Aware Whole-Cell Compiler (`AAWCC`)

Methodology ID: `M-94030`  
Status: **PROPOSED / OPEN PRODUCER SPECIFICATION**  
Created: 2026-08-16  
RH status: **unproved**

The exact repair to `R-94030` is to quantize only where the complete typed active set is constant.

## 1. Typed activation set

For fixed integer `X`, collect every activation point used by the actual source and physical profiles, including at least

\[
 s=\frac Xk
\]

for squarefree source labels and every additional knot at which

\[
 Q_{X/(sk)}(j)
\]

changes formula or causal support.

Let `A_X` be the finite set of integer cells whose interior contains one of these knots with a nonzero typed jump. The construction must derive `A_X` from the literal source/profile formulas; a sampled grid is insufficient.

## 2. Good and anchored cells

Split the retained endpoint source into:

```text
good cells:
  constant source and profile activation set;

anchored activation cells:
  every cell in A_X, with literal source incidence retained.
```

On a good cell, apply the positive reciprocal-mode martingale quantizer and prove exact target and declared-score transport using the fixed-support affine identities.

On an activation cell, do not apply a stencil across the knot. Either:

1. retain the complete finite endpoint contribution literally; or
2. subdivide at the exact activation points and construct a positive boundary realization whose endpoint source owners and all typed coordinates are explicit.

## 3. One-use and observation order

Every source occurrence has exactly one good-cell or anchored-cell owner. Sum all positive rows before testing ordinary capacity. Evaluate ordinary `q` and ordinary `4q` on the same total row, then form radix-four detail.

Finite/continuum, collar, and terminal comparison vectors remain signed observation data. They are not positive source packets.

No auxiliary port is introduced unless the repair explicitly invokes a Schur or projective state-completion mechanism.

## 4. Required closing theorems

A completed `AAWCC` must prove:

1. exact source/target/score identities on every good cell;
2. one explicit positive realization for every anchored activation cell;
3. a corrected adjacent-error formula including every jump term;
4. an all-column estimate for the combined good and anchored rows, including `q<K`;
5. terminal reserve after the new activation ledger;
6. a direct native `Y_4` cost `o(log^2X)`;
7. no repetition of Hall, quantization, correction, omission, or port below the root.

The present packet proves only the necessity of this interface. It does not construct the anchored activation rows.
