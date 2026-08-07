# X-23703 — Digital-freeze and base-`p` phase replay

This standard-library-only checker verifies the exact finite identities used by
`L-23707` and `L-23708`.

## Verified

1. The frozen-corridor renormalization
   ```text
   beta_(L(k+1)-1, Le)=beta_(k,e)
   ```
   for `2<=L<=12`, `2<=k<=50`, and `2<=e<=k`.
2. The prime-base digit increment
   ```text
   sum_(n<=N)[1-(p-1)v_p(n)]=s_p(N)
   ```
   for `p=2,3,5,7` through `N=500`.
3. The Euler-aligned convolution
   ```text
   c_p*b_p = delta_1-p delta_p
   ```
   through `N=500` for the same four bases.
4. Mutation rejection for the wrong corridor row shift.

## Retained result

```text
corridor renormalization checks   13,475
base-p digit increment checks      2,000
base-p convolution checks          2,000
verdict
PASS_EXACT_DIGITAL_FREEZE_AND_BASE_P_PHASE_ALGEBRA
```

## Commands

```bash
python verify.py
python -m unittest discover -s tests -v
```

## Proof boundary

The replay verifies finite integer and rational algebra only. It does not verify:

- the outer four-band theorem imported by `L-23707`;
- the source-bound map from carry spill to digit phases;
- a strict fifth-scale recurrence;
- Greedy Slack or DCRS;
- RH.
