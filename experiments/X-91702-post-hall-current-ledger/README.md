# X-91702 — Post-Hall current-ledger exact algebra replay

Run:

```bash
python3 verify.py
```

The checker uses only Python standard-library `Fraction` arithmetic.  It checks:

- the exact two-coordinate countermodel of `R-91701`;
- coefficientwise positivity of the current row from `Q_parent>=Q_child`;
- exact parent = current + child row identities;
- exact ordinary and signed radix-four linear response telescopes;
- exact capacity-faithful child replacement at the response-ledger level;
- exact literal-score telescoping.

It does **not** verify the arithmetic root Hall identity `O-91703.2`.  That is the
remaining proof-facing gate.
