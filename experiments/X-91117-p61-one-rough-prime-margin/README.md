# X-91117 — `P_61` one-rough-prime margin

Companion directed replay for `L-91328`.

```bash
python3 experiments/X-91117-p61-one-rough-prime-margin/verify.py
```

Expected verdict:

```text
PASS_P61_ONE_ROUGH_PRIME_MARGIN
```

The standard-library checker traverses all `262,144` activation cells of the
finite Boolean block through `61` and certifies `1,048,414` endpoint/channel
gates with exact integer/Fraction arithmetic and directed inverse-square-root
enclosures.

The result is a one-new-least-prime theorem. It does not claim scalar
multiprime tensorization.
