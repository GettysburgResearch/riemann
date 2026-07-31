# X-15603 — Exact weighted-deficit capacity regression

This standard-library-only experiment verifies the finite algebra behind
`L-15607`, `L-15608`, and `T-15603`.

It checks two logically independent facts.

1. **External source repair preserves rank.**  Starting from
   `P=span(e1,e2)`, the constraint
   `ell(x)=x1+2x2+x3`, and the external corrector `Q(c)=c e3`, the graph repair
   gives `e1-e3,e2-2e3`.  Both repaired vectors satisfy the constraint, and
   their exact Gram has positive LDL pivots `2,3`.  The packet dimension remains
   two.
2. **Weighted-deficit index saturation needs no subspace alignment.**  The
   synthetic deficit operator has eigenvalues
   `3/2,6/5,1/2,1/10` and threshold `G-Gamma=1`, so its exact dangerous index is
   two.  The corresponding operator has exactly two eigenvalues below
   `Gamma=1`.  A different two-dimensional trial packet, containing small
   components in the high eigenspace, nevertheless has its full compression
   below `t=19/20`.  Min--max therefore closes the count sandwich exactly.

Run:

```bash
python experiments/X-15603-weighted-deficit-capacity/verify.py
```

Expected verdict:

```text
PASS_EXACT_L15607_L15608_T15603_REGRESSION
```

Proof-object SHA-256:

```text
9d32649d92d953d736cd8afe7bc326cd12db3fc59e8dc54ba73d8a53491a2e5c
```

This is a synthetic exact regression.  It does not evaluate the Suzuki symbol,
build a zeta radical packet, prove the cofinal weighted-index/capacity
comparison, or prove RH.
