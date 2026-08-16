# X-93260 — Exact cubic-dispersion replay

Arithmetic class: `EXACT_RATIONAL_WITH_SYMBOLIC_LOG4_PAIR`

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

The checker authenticates:

- the exact `K`, `W`, and `J` polynomial identities;
- both vanished Mellin moments of `W`;
- the minimal two-switch sign witnesses;
- the positive cumulative square of `J`;
- the positive Peano kernel `Phi` and `D^2 Phi=xW`;
- finite radix-four telescoping on rational fixtures;
- the formal `Lambda=mu*log` hyperbola identity;
- the exact balanced large-divisor bilinear reindexing;
- the corrected `d_N(a)` modulus line;
- the complete bounded base-two Q4 coefficient pattern;
- four hostile mutations.

It does not authenticate PNT, the general second-order Euler summation theorem,
the open large-divisor Mobius estimate, the First-Hermite one-carrier theorem,
or RH.
