# X-28001 — Global fragmentation-spine exact replay

Run:

```bash
python experiments/X-28001-global-fragmentation-spine/verify.py
```

Expected verdict:

```text
PASS_EXACT_GLOBAL_FRAGMENTATION_SPINE_ALGEBRA
stochastic_rows 255
green_rows 51
first_entrance_rows 51
quarter_balanced_tree_rows 16382
top_fifth_derivative_lower_gt 1/25
abel_witnesses -1,-13/16,-91/256,-1168054960769/4096
```

The checker uses only Python integers and `fractions.Fraction` except to nominate rational square-root brackets, whose validity is then checked exactly by squaring.

It verifies:

- row-stochasticity of the size-biased binary–ternary chain;
- the Green/hitting representation on several rational synthetic targets;
- the exact first-entrance identity;
- all declared quarter-balanced extraction trees through `n=256`;
- an exact atanh-series/rational interval proof of the worst top-fifth derivative gate;
- the four fixed Abel-order counterexamples.

It does **not** prove first-entrance positivity for the critical source, producer positivity, the sharp prime ramp, or RH.

The `verifier_sha256` in the retained result binds the byte-identical checker used for the local replay. Runtime and hardware are not theorem data.
