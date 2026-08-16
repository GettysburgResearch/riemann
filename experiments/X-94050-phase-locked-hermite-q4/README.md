# X-94050 — Phase-locked Q4 / First-Hermite finite replay

Status: **EXACT FINITE ALGEBRA + TARGETED FLOAT DIAGNOSTICS**  
Frozen parent: PR #498 head `6cc0da2fa5711017e260ebdcea4ba8c22e453288`

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_94050_PHASE_LOCKED_HERMITE_Q4
```

The replay checks:

- the frozen centered cubic weight, Mellin numerator, and finite endpoint identity;
- the exact Laurent factorization `5-4 cos(Lu)`;
- the critical conjugated shift factorization and its exact vanishing shift moments;
- strict finite-depth terminal signs;
- fixed-order wedge exponent cancellation and synthetic sublinear order profiles;
- finite prime-envelope sanity diagnostics;
- a finite maximum-modulus grid control;
- sign changes after centering the exact positive Q4 annulus;
- six hostile mutations.

It does **not** prove or replay:

- the Chebyshev/Stirling analytic estimates;
- the terminal-pair theorem;
- the uniform high-order Hermite derivative bounds;
- the coefficient-energy asymptotic;
- pointwise signed prime cancellation;
- RH.
