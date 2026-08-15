# X-93781 — Exact Target-Lorenz typed leaf and native-ledger compiler

The checker uses exact `Fraction` arithmetic to replay the algebra of
`L-93783--L-93785`:

```text
one leftmost coefficient vector;
positive residual source nu;
current-only physical row bonus B;
explicit score surplus sigma;
one leaf owner;
ordinary q and 4q before radix-four detail;
signed observation correction outside the source cone;
positive radix-four inversion;
empty exported recursive family;
zero auxiliary port;
60989 < 61000 direct native charge.
```

Run:

```bash
python3 verify.py --output /tmp/x93781.json
```

Expected verdict:

```text
PASS_TARGET_LORENZ_TYPED_LEAF_COMMON_PARENT_NATIVE_LEDGER
```

The replay is a theorem/compiler regression. It does not prove the analytic
AVLT, endpoint-frame density, all-column bounds, endpoint consumer or RH.
