# X-32402 — Paired averaged Selberg finite gate

This experiment replays the finite portion of `L-32406` without binary floating-point sign decisions.

It certifies:

- the exact `Q(sqrt(2))` local dyadic generalized-prime/Selberg coefficients;
- rational directed logarithm intervals obtained from
  `log y = 2 atanh((y-1)/(y+1))` after dyadic range reduction;
- the scalar Jensen-ready inequality
  `bar(P0)^2 + bar(P1)^2 > bar(S0)` for every `6 <= n < 30000`;
- direct positive averaged energy defects for `n=2,4,5`;
- exact equality at `n=3` from the support table;
- the rational logarithm gates used by the elementary tail proof from `n=30000` onward.

The minimum directed lower bound in the finite scalar range occurs at `n=7` and is greater than

```text
0.775163360674092
```

in the retained 96-bit fixed-point enclosure.

Run:

```text
python experiments/X-32402-paired-averaged-selberg/verify.py
```

Expected verdict:

```text
PASS_EXACT_PARITY_PAIRED_AVERAGED_SELBERG_ABSORPTION_FINITE_GATE
```

Retained proof-object SHA-256:

```text
fb2e088bd2641ce4aec4a83fa4b5f43fd90766fba8cfb2d733fc1bfeb0029824
```

Scope: this proves the finite gate used by `L-32406`. The cofinal range is the written elementary estimate in the lemma. Neither artifact proves the remaining RH-sensitive physical boundary recurrence or RH.
