# X-91102 — Brownian–theta passive-network regression

This standard-library replay checks the exact algebra deposited in `L-91105`--`L-91108`:

```text
Cayley Pick-defect <-> anticommutator congruence;
Mellin-symmetric two-copy reflection identity;
impedance as a bounded regression;
Gamma-pair reconstruction;
Beta(2,2) Stein identity through degree 12;
theta Gibbs variance and supersymmetric-potential algebra.
```

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
```

Expected verdict:

```text
PASS_BROWNIAN_THETA_PASSIVE_NETWORK
```

The replay verifies finite exact identities only. It does not construct the theta Dirichlet-to-Neumann map, prove Brownian reflection positivity, or prove RH.
