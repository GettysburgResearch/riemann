# X-91108 — Positive butterfly lift of every monotone interval seed

This directed standard-library replay certifies the finite numerical gate in
`L-91321`:

```text
A_T > B_T > 0,  3 <= T <= 55,
B_T/A_T < 199/200.
```

Those inequalities make the exact recurrence

```text
eta_(e+1)=0,
eta_(n+1)=(m-B_n eta_n)/A_(n+1)
```

nonnegative for every monotone parity edge `1 <= e < o <= 54`. Symbolic
substitution then gives the exact seed identity

```text
sum_T eta_T P_T
 = m 1_(e<n<=o) + m rho_(e,o) delta_(o+1),
0 <= rho_(e,o) < 199/200.
```

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_INTERVAL_SEED_POSITIVE_BUTTERFLY_LIFT
```

The replay does not prove that the resulting signed butterfly row perturbation
fits beneath the resident baseline endpoint weights, nor that the positive
boundary overshoot is absorbed by the complementary rough reserve.
