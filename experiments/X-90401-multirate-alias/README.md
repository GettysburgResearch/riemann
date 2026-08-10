# X-90401 — multirate/alias diagnostics

Status: **FINITE NUMERICAL DIAGNOSTIC — NOT AN ANALYTIC PROOF**  
Related claims: `L-90401`, `L-90402`, `L-90403`

Run:

```bash
python3 experiments/X-90401-multirate-alias/verify.py
```

Expected verdict:

```text
PASS_X_90401_MULTIRATE_ALIAS
```

The standard-library replay checks finite numerical instances of:

1. the no-alias Poisson collapse for two offset, incommensurable lattices;
2. the exact alias/polyphase kernel expansion for `P<L`;
3. period-averaged trace and Frobenius identities, including a strictly positive alias tax;
4. exact phase locking `r log p = log(p^r)`;
5. the closed-form Montgomery–Taylor scalar optimizer against several competitors.

The generated record is

```text
results/verification.json
```

## Proof boundary

The script does not prove:

- distributional Poisson summation;
- the analytic end/tail estimates;
- the prime-side trace asymptotics;
- the Montgomery–Vaughan off-diagonal estimate;
- the subpolynomial resonant-budget theorem;
- any zero-proportion theorem;
- RH.

Its purpose is regression, sign/conjugation checking, and reproducible reconnaissance only.
