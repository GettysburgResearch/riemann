# X-105290 — All-pass Hankel owner-conductor replay

Run:

```bash
python experiments/X-105290-allpass-hankel-owner-conductor/verify.py
```

Expected output:

```text
PASS_T105290_ALLPASS_HANKEL_OWNER_CONDUCTOR
365cb91ba2af9276377fd0b2dc69c796c20dca51e478459132f3aced12582747
```

The standard-library replay checks:

- the exact degree-five square-root polynomial coefficients;
- cancellation of source degrees one through five;
- the corrected physical `alpha=2` prime-simplex tail;
- the conservative two-orientation **unphased** bound `<1/18500`;
- the five-rung unphased frozen-source cost `<1/3700`;
- the remaining ninety-percent allowance `3579/37000`;
- one exact matrix all-pass degree/Hankel fixture;
- the sharp sign-pair Gram formula behind square-phase occupancy;
- the finite-alpha oriented-ratio identity.

It explicitly records:

```text
global_phase_family_diagonal_bound_proved=false;
phase_family_excess_retained_in_hoch105290=true;
hoch105290_proved=false;
ninety_percent_established=false;
density_one_established=false;
rh_established=false.
```

The replay does **not** evaluate Xi, authenticate Conrey's analytic proof,
construct the complete owner-conductor source exhaustion, bound the complete
phase-family diagonal, estimate coherent cross-owner Hankel terms, or prove
`HOCH105290`.
