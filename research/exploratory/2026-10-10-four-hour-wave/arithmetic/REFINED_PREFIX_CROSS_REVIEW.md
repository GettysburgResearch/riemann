# Independent refined-prefix guard review

Status: **ACCEPT for the exact scoped source/finite guard binding below.**
Reviewer: delegated arithmetic agent, independent of the outer-ray producer.
Review date: 2026-10-10 UTC. RH remains open.
Final replay also binds explicit R>0,A>=0 in MN and P_R(0)=1 in SA;
these source-domain hypotheses were independently read after the repair.

I read the complete checker, REFINED_PREFIX_MOMENTS.md, MOMENT_NORM_TRANSPORT.md
and SEXTIC_ABSORPTION.md at the following hashes. I replayed the frozen checker
once in optimized Python with an explicit temporary output, without editing
any outer-ray file. The direct-source/output bindings and every explicit
acceptance condition remained active.

| Source | SHA-256 |
|---|---|
| `check_refined_prefix_moments.py` | `4d6c98f8290e6f45f83f74c69b08faf36214b361a8dc31a5155629a682046f66` |
| `produce_refined_prefix.py` | `3b15320247b2d4fc6b31faa250f33f5c3c0ffbd25d4100737594bdcf2a0ca156` |
| `refined_prefix_candidates.json` | `cd8a4c8baa5a235823ebc546a7b92ab63b92113b6f1af7550a13e67b99c376b1` |
| `REFINED_PREFIX_MOMENTS.md` | `d2d26190cefca1a6fe0e5084ac3cfd0197b9059cedeb38f1a45bb242a344eaaa` |
| `MOMENT_NORM_TRANSPORT.md` | `9279440530af0efc1f4c19b3dd9aca608ec9a5d6afde278687dc098b010967c4` |
| `SEXTIC_ABSORPTION.md` | `9d6a56bf4ea5553419d710ce96848122316886d0abbf4e8b490f46aca8d1f5e5` |
| `refined_prefix_moments.json` | `95204a030b6b86df781908aa7f472cf63edde02b226558b0713a1442177e08ba` |

The command from `/workspace/riemann` was:

```bash
nice -n 19 /workspace/.riemann-tools/python/bin/python3 -B -O \
  research/exploratory/2026-10-10-four-hour-wave/xi/outer-ray/check_refined_prefix_moments.py \
  --output /tmp/refined-prefix-independent-arithmetic-v2.json
```

The command exited zero and reported
`PASS_DIRECTED_REFINED_PREFIX_MOMENT_GUARDS PREFIX 111 K 6905`.
The complete temporary JSON is byte-identical to the official receipt. Its
SHA-256 is `95204a030b6b86df781908aa7f472cf63edde02b226558b0713a1442177e08ba`.

The replay authenticates 111 strictly nested dyadic root brackets, 222 actual
Gamma/zeta Hardy-Z endpoint signs at 224 bits, the actual degree-six Xi
logarithmic jet, directed subtraction of the complete retained 8049 root
intervals, and the exact rational cone/Gaussian/artificial-root guards for
the whole resulting three-moment box. It also replays the native FLINT
complete count at8192 and every direct source hash of the imported receipt.

The remaining7938 original endpoint signs and the prior complete simple
census are explicitly imported. Neither this review nor this checker
reproduces historical Gram/Rosser verification. The complete paired product
and logarithmic moment identity are analytic dependencies. The norm transport
uses the complete strip phase projections; the two-pair construction has the
correct strict feasibility interval, positive Gaussian guard, and excluded
artificial roots. No protected companion slab, sector, full parameter-family
transport predicate, new zero-free result, or RH statement is certified.

The smallest un-replayed input needed to interpret these native moments is
the prior source-qualified complete simple census together with its historical
complete-count contract. The finite checker alone does not replace it.
