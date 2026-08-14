# X-91692 — Exact factor-67 compact-reserve closure

This replay certifies the new finite and algebraic assertions used by
`L-91692/T-91661`.

Run:

```bash
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected classification:

```text
PASS_FACTOR67_COMPACT_RESERVE_PROOF_OBLIGATION
```

The checker uses exact `Fraction` arithmetic, directed integer-square-root
intervals, and the positive rational `atanh` series for logarithms with an exact
geometric tail.  It verifies:

```text
159/500 < L(x) < 183/100 < 2 on every cell 1<=x<67;
Psi(x)>2 at the hostile first-cell witness;
exact target-Hall residual-plus-bonus row transparency;
C67<19;
strict interior reserve 41/[32(K+178)];
strict terminal reserve 581 X^(-3/2);
support-compatible bottom and top source ownership;
one aggregate P61/67 Schur port;
grouped rather than fibre-repeated causal children;
retention of the nonzero finite/continuum defect.
```

The replay does not independently reconstruct the frozen endpoint-frame,
positive-quantizer, port, causal, dual, or endpoint-to-RH theorems.  It does not
establish RH.
