# Integration handoff — X-17804

Stack on PR #190.

Add:

```text
L-17804  exact local-cell and cumulative-moment prime identities
O-17804  directed closure of the first J=12 prime cell
X-17804  all-MPFR local degree-23 producer and exact consumer
```

Use the 448-bit prime interval as `prime_interval` in the phase-band certificate. Do not reuse the superseded binary64 value from Issue #193.

The remaining artifact is the directed selected-zero phase interval. Once available, feed it and the existing `J=12` high-zero moat into `X-15605`.
