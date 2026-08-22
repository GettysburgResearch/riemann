# X-90210 — Claude Zeta23 index-bridge replay

This standard-library verifier supports the finite-channel firewall in
`L-90228` and the constants in `L-90227`.

It checks exactly, over `Fraction`:

- the rank-two factorization invariants of random pullbacks
  `a b^T + b a^T`;
- the Cauchy--Schwarz identity showing that the two possible nonzero
  eigenvalues have opposite weak signs;
- the canonical near-line model with eigenvalues `2` and `-2 epsilon^2`.

It also records the Montgomery--Taylor line and pair-budget constants using
ordinary high-precision floating evaluation; that numerical line is a display
check only, not a proof of Claude's imported theorem.

Run:

```bash
python3 verify.py
```

Expected verdict:

```text
PASS_X_90210_CLAUDE_ZETA23_INDEX_BRIDGE
```
