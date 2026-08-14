# X-91685 — Target-Lorenz vector primal/dual replay

Run from this directory:

```bash
python3 verify.py
python3 recon.py
sha256sum -c SHA256SUMS
```

Expected exact theorem verdict:

```text
PASS_TARGET_LORENZ_VECTOR_PRIMAL_DUAL
```

`verify.py` uses exact `Fraction` arithmetic and integer square comparisons. It
checks the ordered-cone theorem through finite scalar projections, exact
fractional-knapsack vertices, equality of the greedy objectives with their
cutoff dual bounds, deliberate primal successes, deliberate dual failures, and
the child-interface firewall of `R-91685`, and the exact right-tail/full-signed
determinant lower bound of `L-91687`.

Expected discovery verdict:

```text
PASS_TARGET_LORENZ_STRUCTURED_RECONNAISSANCE
```

`recon.py` uses binary64 arithmetic on a structured finite grid. Its output is
**discovery only**. It does not certify the remaining real `(p,y)` arithmetic
cells, the live native-root allocation, CFFP or RH.
