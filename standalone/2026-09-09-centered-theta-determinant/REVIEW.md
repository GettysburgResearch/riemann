# Review guide

This is a component manuscript, not a completed RH proof. Local equation numbers
refer to PROOF.md. The source is the literal infinite theta density; no numerical
zero selects a coefficient or a subspace. The parent is not independently
accepted by this author continuation.

## Load-bearing checks

1. Verify the factor 4/6 full-line density in (1), mean-zero normalization,
   differentiated tails, and the complete Hilbert--Schmidt integral (7).
2. Reconstruct the maximal differentiation domain and its restriction from
   the mean-zero Hilbert space onto the full one. Check K*K, not KK*, in
   the exact connection to the parent's H, and retain the operator domains.
3. In the bounded-interval determinant calculation retain the det_2 product
   correction. Without it an unwanted exponential remains. The general
   formula centers the probability mean; evenness sets that mean to zero.
4. Check conditional centering in K_R=B_R K P_R. Neither an uncentered cutoff
   nor separate boundedness of the infinite Volterra pieces is used. Prove
   Hilbert--Schmidt convergence before using determinant continuity.
5. Check the parity block determinant. It gives one ordinary trace-class
   determinant equal to Xi(z)/Xi(0), not its square. K is Hilbert--Schmidt;
   T=-K^2 on the odd subspace is trace class, not claimed positive.
6. Reconstruct the algebraic multiplicity and the exponential Jordan-chain
   argument. Geometric multiplicity one does not establish simple xi zeros.
7. Verify q_j=w^(j)/w lies in H_w and the adjoint chain K*q_(j+1)=-q_j.
   Prove its independence from the actual theta tail, and inspect the kernel
   mismatch ruling out any bounded coercive positive symmetrizer on each
   finite cut. The infinite intersection retains all nonzero root spaces,
   but no assertion about spectral reality or eigenvector completeness follows.

## Exact open point

No proof is provided that every nonzero eigenvalue of T is positive real.
That property would imply RH directly from the ordinary determinant identity.
The positive differential base, positive even moments, and coefficient signs
of the determinant do not supply it. The naive bounded-metric plan is disproved
for the specified full spaces; this does not disprove RH or every spectral route.

## Execution boundary

check.py validates finite rational identities on explicitly named control
models. It does not certify any actual theta value or approximate an actual
xi zero. The finite Volterra matrices are algebraic analogues, not a claimed
convergent theta discretization. The 110 cases do not machine-prove the infinite
arguments. Standard Fredholm facts are imported as listed in PROOF.md; no
complete external-paper audit, formal build, parent checker, full repository
checkout or remote CI execution is represented as having run.
