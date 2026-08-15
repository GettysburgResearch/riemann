# X-91760 — Native Volterra source disintegration regression

This exact `fractions.Fraction` checker accompanies `L-91760/L-91761`.

It verifies:

```text
formal perfect-square instances of the one-colour Volterra identity;
complete-graph rank-one source cancellation;
negative-source exhaustion and positive-source non-overdraw;
finite seed = continuum seed + mismatch;
row, ordinary and radix-four observations preserve that identity;
literal bottom/retained/top source partition;
strict root/rough ownership separation at 67;
nine fail-closed mutations.
```

Run:

```bash
python3 verify.py certificates/control.json --output /tmp/verification.json
cmp /tmp/verification.json results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_NATIVE_VOLTERRA_RANK_ONE_COMMON_PARENT_SOURCE
```

Expected proof-object digest:

```text
783da11279e2dde564081af770f9bea976b34e400b54fc4c31f1d6a228c20bee
```

The checker is a finite exact regression. It does not certify the directed positivity of `L(x)`, the frozen finite-realization estimates, the endpoint consumer, or RH.

Additional exact regression gates: subcritical causal child mass and positive-source/signed-observation two-ledger residual.
