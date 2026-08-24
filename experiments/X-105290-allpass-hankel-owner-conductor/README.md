# X-105290 — All-pass Hankel owner-conductor replay

Run:

```bash
python experiments/X-105290-allpass-hankel-owner-conductor/verify.py
```

Expected output:

```text
PASS_T105290_ALLPASS_HANKEL_OWNER_CONDUCTOR
4319e3d89d5022a65e3d9869c35e987aab8077ba2c881774fd9c75fe9e029a1a
```

The standard-library replay checks:

- the exact degree-five square-root polynomial coefficients;
- cancellation of source degrees one through five;
- the corrected physical `alpha=2` prime-simplex tail;
- the conservative two-orientation bound `<1/18500`;
- the five-rung source cost `<1/3700`;
- the remaining ninety-percent allowance `3579/37000`;
- one exact matrix all-pass degree/Hankel fixture;
- the sharp sign-pair Gram formula behind square-phase occupancy;
- the finite-alpha oriented-ratio identity.

It does **not** evaluate Xi, authenticate Conrey's analytic proof, construct the
complete owner-conductor source exhaustion, estimate coherent cross-owner
Hankel terms, prove `HOCH105290`, prove ninety percent, prove density one or
prove RH.
