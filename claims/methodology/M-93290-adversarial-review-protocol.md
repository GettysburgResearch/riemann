# M-93290 — Adversarial review protocol for the actual-row/covariance successor

Claim ID: `M-93290`  
Status: **METHODOLOGY**  
Created: 2026-08-18

Review in this order:

1. Compare the full-row and `mu_>3` coefficient sequences; reject any scan that
   substitutes one for the other.
2. Reconstruct the open-cell derivative and integer recurrence of `L-93290`.
3. Inspect the exact `Q=10^18` square-root brackets in `certify_rows.cpp` and
   verify that floating `sqrt` is only a seed.
4. Recompute the two retained minimum scaled integers.
5. Verify the fixed-finite-sieve terminal identity `a_(j,P)(n)=1_(n,P)=1` after
   `(j+1)P`.
6. Check both exact `p=5` monotonicity counterexamples.
7. Fix the Fourier convention and verify the reflection in Parseval before
   accepting the covariance cancellation.
8. Verify gauge invariance only for multipliers that preserve the declared
   legal function spaces.
9. Reconstruct the Besicovitch autocorrelation by finite truncation, then pass
   to the square-summable limit.
10. Keep the finite theorem, fixed-depth theorem, carrier mean-square theorem,
    and pointwise RH producers logically separate.

Immediate rejection tests:

```text
ordinary mu used in place of mu_>3;
integer values promoted to real-X positivity without A(N);
floating sqrt trusted without the u128 inequalities;
finite X<=10^8 certificate called eventual positivity;
fixed finite P theorem applied with P=P(X);
positive autocorrelation promoted to pointwise SCID_PL;
a fixed invertible kernel preconditioner claimed to change the covariance;
RH reported proved.
```
