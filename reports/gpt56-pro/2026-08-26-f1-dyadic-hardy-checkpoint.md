# F1 dyadic-cell and one-Hardy-primitive checkpoint

The requested checkpoint-four commit is present remotely and remains in the
ancestry of PR #730.  The first pass of the present continuation pushed
`T-105460`, identifying the prime-box Chow square with the Boolean/Wick source
and reducing the physical obstruction to one reflection-odd total-variation
gate.

This checkpoint removes the remaining continuous kernel layer.

1. The fixed derivative-outer kernel has breakpoints only at `n,2n,4n,8n`.
   Therefore the physical current is exactly `A_m+B_m sqrt(X)` on every open
   integer cell.
2. The logarithmic absolute mass of a cell has a closed primitive and is
   uniformly equivalent to its two endpoint values.
3. For

   ```text
   W(x)=2 sum_{n<=x}a_n - sqrt(x) sum_{n<=x}a_n/sqrt(n),
   Delta_2=(I-S)^2(I-sqrt(2)S),
   ```

   the right endpoint is exactly `H_K(m+)=4 Delta_2 W(m)`.
4. The left/right endpoint discrepancy is the same four-term dyadic filter
   applied to the coefficient sequence.
5. The frozen source-diagonal and equal-product energy makes the weighted jump
   ledger `M^(-1/2+o(1))`; it does not estimate different-product
   correlations.
6. Consequently `F1VAR105460` is equivalent to

   ```text
   F1HARDY105470:
     sum_{M<=m<=2M}|Delta_2 W(m)|/m = M^(o(1)).
   ```

7. Weighted l1 duality turns the same gate into one scalar family of signed
   source correlations.  No pair-owner tensor remains.
8. A one-sample-per-cell shortcut is false exactly.

The latest PR #751 head was frozen at
`98af0db6ec7f77d6333a77a3dac53c4698852f43`, including its centered
double-incidence alternative.  That new route does not invalidate the
reflection-Hardy equivalence.

Replay:

```text
PASS_T105470_F1_DYADIC_HARDY
proof_object_sha256=7241f2c46f70d02c45f0344e20144f5788d6a2302cccbae9c66867000d3400f9
finite_checks=186004
hostile_mutations=15
```

`F1HARDY105470`, `BCI102990`, and RH remain open.
