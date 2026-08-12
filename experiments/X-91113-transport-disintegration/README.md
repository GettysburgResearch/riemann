# X-91113 — Transport disintegration replay

This exact finite replay checks the algebra behind `L-91325`:

- a positive source partition pushed through one Markov kernel gives an exact
  target partition;
- branch responses bounded by their own target portions cannot overfill the
  physical target;
- one global safety factor commutes with the color sum.

Run:

```bash
python3 verify.py
```

Expected verdict:

```text
PASS_TRANSPORT_DISINTEGRATION_AND_SINGLE_TARGET_LEDGER
```
