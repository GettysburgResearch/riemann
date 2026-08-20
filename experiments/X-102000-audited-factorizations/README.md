# X-102000 — Audited factorization replay

This replay checks the finite algebra added and corrected on PR #696.

It verifies:

- `a_U=b_U*1`;
- `a_U*a_U*mu=b_U*a_U`;
- the two-wing/gcd/single-Möbius coefficient identity;
- the unique-largest-prime recurrence for `N_V`;
- the corrected finite joint-survival telescoping law;
- the depth-two threshold at `Z=sqrt(T)`;
- the bounded carrier-subtracted endpoint kernel.

Run:

```bash
python3 experiments/X-102000-audited-factorizations/verify.py \
  --output experiments/X-102000-audited-factorizations/results/verification.json
```

Expected verdict:

```text
PASS_X_102000_AUDITED_FACTORIZATIONS
```

The replay authenticates finite exact algebra and finite-threshold bookkeeping only. It does not prove `SOW102008`, either ratio-four field-energy estimate, or the Riemann Hypothesis.
