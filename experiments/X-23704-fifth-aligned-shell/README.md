# X-23704 — Fifth-aligned cumulative-shell interval replay

This experiment is the proof-producing finite companion to `L-23710`.

Run from the repository root:

```bash
python experiments/X-23704-fifth-aligned-shell/verify.py
python -m unittest discover \
  -s experiments/X-23704-fifth-aligned-shell/tests \
  -p 'test_*.py'
```

The verifier uses only Python's standard library:

- exact Möbius values;
- `fractions.Fraction` arithmetic;
- integer-square-root outward brackets;
- the positive atanh series for logarithms with an explicit geometric tail.

It certifies the complete interval `1<=y<=100`, not only integer samples. On each integer cell the derivative numerator is affine in `sqrt(y)`, so the checker verifies that no negative-to-positive crossing can create an interior minimum.

The retained result is:

```text
EXACT_FIFTH_ALIGNED_SHELL_ANNULUS_VERIFIED
endpoint y=1                         exactly 0
all endpoints 2<=N<=100             >9637/10000
increasing cells                     45
A_N<=0 cells, interior min impossible 54
unresolved cells                      0
```

This experiment does **not** prove the global fifth-shell sign, `DGB(5)`, Greedy Slack/DCRS, or RH.
