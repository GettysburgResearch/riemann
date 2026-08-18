# R-97800 — Source-blind growing-prime shortcuts do not prove the two-row tail

Claim ID: `R-97800`  
Status: **EXACT NEGATIVE CONTROLS / BINDING FIREWALLS**  
Created: 2026-08-18  
RH status: **unproved**

The following shortcuts are invalid for the growing-prime tail.

1. **Fixed-depth LAPBR.** PR #589 proves that the quantified `LAPBR67` current is eventually negative at a moving least-prime state. It cannot be used as a positive tail theorem.
2. **Fixed finite sieve extrapolation.** `L-97800` is uniform only after its explicit cutoff budget is checked. A theorem for each fixed `P` does not by itself justify a cofinal `P=P(X)`.
3. **Square/PSD sign inference.** The scalars `v` and `-v` have the same square. Hence a diagonal, autocorrelation spectrum or SACF energy bound without phase information cannot determine the one-sided sign.
4. **Scalar-to-two-row lift.** The vector `(-1,2)` has positive `5:3` scalar and a negative first row. Scalar Lorenz exactness does not certify both rows.
5. **Safe-filter redesign.** PR #579 proves the phase-locked covariance is invariant under every invertible fixed safe-line preconditioner. A gauge change cannot supply missing arithmetic cancellation.
6. **Absolute values.** The normalized absolute future-prime mass contains the divergent prime-harmonic profile. Replacing `mu(r)` by `|mu(r)|` destroys the only available cancellation and cannot give the sharp constant one in (L-97801.7).

These controls do not refute eventual two-row positivity; they identify the arithmetic information a proof of `FPCB23` must retain.
