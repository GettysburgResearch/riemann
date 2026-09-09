# X-108501 — finite verification for the commutative collapse theorem (T-108501)

Run from the repository root:

```
python3 experiments/X-108501-commutative-collapse/verify.py
```

Expected banner: `PASS_108501_COMMUTATIVE_COLLAPSE checks=4`.

Checks: C1 nilpotent exponential jet law in `Q[e]/(e^m)` (EXACT_RATIONAL);
C2 the finite-N sum-exchange collapse identity with free rational
parameters (EXACT_RATIONAL — this is the identity the theorem's proof
reduces to); C3 exact bicomplex idempotent decomposition and the
invertibility criterion (EXACT_RATIONAL); C4 dual-number truncated zeta
sums vs the jet formula (FLOATING_RECONNAISSANCE, corroboration only,
decides nothing). Writes `results/verification.json` with
`"rh_established": false`.

Tests: `python3 -m unittest discover -s experiments/X-108501-commutative-collapse/tests`
