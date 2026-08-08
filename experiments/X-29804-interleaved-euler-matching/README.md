# X-29804 — Interleaved Euler parity and Hausdorff matching

This exact standard-library regression accompanies:

```text
R-29803  pair-first Euler positivity dichotomy;
R-29804  one-sided Pascal source failure;
L-29809  even-start interleaved Euler parity resolution;
L-29810  two-sided adjacent Hausdorff matching.
```

It verifies:

- the two-mode parity decomposition on rational Laplace fibers;
- the exact even-start Euler identity and positive remainder;
- 110,656 rational-grid weighted Hall interval inequalities;
- the exact negative odd-start jet `-2/105`;
- the exact one-sided source deficit `2/35`.

Run:

```bash
python experiments/X-29804-interleaved-euler-matching/verify.py
```

Retained proof-object SHA-256:

```text
9603b6041173939dac3f835266b030b9a122eb9b7549d774f13e7610f5c61307
```

The experiment does not construct the two-orientation balanced Pascal gadget,
prove the complete source-to-DCD congruence, prove DCD, or prove RH.
