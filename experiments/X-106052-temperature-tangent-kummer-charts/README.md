# X-106052 — Temperature-tangent Kummer-chart replay

Exact standard-library replay for `L-106052`.

It checks:

```text
quadratic roots have a common character square;
square-completion contributions are quadratic-chart trivial;
the midpoint tangent Hadamard transform selects the total owner/prime class;
the two principal charts recombine to the full tangent;
2^omega(q) tensor chart count.
```

Run:

```bash
python3 verify.py --output /tmp/x106052.json
cmp /tmp/x106052.json results/verification.json
```

The replay checks finite cyclic-character exponent algebra only. It does not
prove physical orientation, `TKCA106050`, `SGIC102890`, or RH.
