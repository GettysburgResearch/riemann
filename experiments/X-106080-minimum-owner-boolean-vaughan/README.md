# X-106080 — Minimum-owner Boolean Vaughan replay

Run from the repository root:

```bash
python experiments/X-106080-minimum-owner-boolean-vaughan/verify.py \
  --output experiments/X-106080-minimum-owner-boolean-vaughan/results/verification.json
```

Expected result:

```text
PASS_X_106080_MINIMUM_OWNER_BOOLEAN_VAUGHAN
checks=34250
sha256=86bb5ac732d2548679b16000a61c1fa40d961c962bde5d44edf9d39c110f98df
```

The replay checks exactly:

- the Boolean/disjoint-support Vaughan identity on finite squarefree Euler cubes;
- the two-distinct-core-prime support of the balanced row;
- the minimum-owner rule with and without one horizon-exceptional label;
- `lambda^2<=core` on every balanced fixture;
- the dyadic implication `L^2<2B`;
- the centered same-prime-family off-diagonal kernel identity;
- `mu^2(n)=sum_(k^2|n)mu(k)` and the squarefree lattice reindexing;
- nonzero Ramanujan phases for clean opposite owners.

It does not authenticate the inherited analytic phase-packing estimate, the
transport of its literal owner weights to the new Boolean coordinate, the
global Type-I Hilbert assembly, the Mellin consumer, or RH.  Those are the
load-bearing review targets in `M-106080`.