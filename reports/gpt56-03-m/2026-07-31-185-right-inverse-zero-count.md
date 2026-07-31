# Report — exact selected-zero count from a cardinal right inverse

Agent: `gpt56-03-m`  
Issue: #185  
Stack: PR #168

## Result

The requested count

\[
N_{G_C^{-1/2}K_T^CG_C^{-1/2}}(B_T+\beta)
\le\dim R
\]

is automatic on the exact cardinal–radical packet once one records the metric
norm of its selected-zero right inverse.

If `VC=I`, `R=ker V`, and `C^*GC<=Lambda I`, then

\[
V^*V\ge\Lambda^{-1}G
\]

on `R^(perp_G)`. Any larger certified-zero Gram dominates `V^*V`, so every
threshold below `1/Lambda` has at most `dim R` generalized eigenvalues below it.

For the packet of `T-14306`, `V_Z C_tilde=I` and the exact selected-zero kernel
is the repaired radical packet. The finite-section cardinal/radical identities
give a source-bound residual budget `B_(T,m,Z)(L)->0` as support grows. The
right-inverse Gram stays finite at each fixed packet. Hence support—not an
unbounded verification of all zeros—may be chosen so that

```text
B_(T,m,Z)(L)+beta < 1/Lambda.
```

This gives the count and the positive Schur floor directly. A larger finite
certified-zero block may be used, but completeness to an unbounded height is not
assumed.

## Main correction to the frontier

The selected-zero count is **not** the remaining RH theorem for the constructed
packet. It is a finite conditioning statement and is now closed. The remaining
RH-bearing statement is complete low-index capture: prove that the constructed
cardinal–radical packet accounts for every dangerous direction of the exact
localized Weil operator. `T-14307` shows why that distinction is essential.

## Validation

- exact Fraction-only replay: pass;
- nine adversarial tests: pass;
- SHA ledger: pass locally;
- proof object:
  `a5c1c569f6a95e8ef2f5915a9d8a42aab181e1500ef860190cde8964f751eed3`.

## Status

No RH proof is claimed. The contribution removes the count as an independent
analytic blocker and hands the project back one sharply isolated capture theorem.
