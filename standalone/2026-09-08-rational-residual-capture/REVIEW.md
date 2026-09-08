# Independent review priorities

This submission claims RC1--RC5 at their component scopes, not an RH proof.
Review the mathematical proof separately from the exact finite checker.

1. Reconstruct the covariance in (10) conditional on the common residue modulo
   gcd(m,n). Check complex polarization and the subtraction killed by balance.
   V includes the constant Fourier mode |b+sum(a)/2|^2; do not delete it.
2. Check the rational-frequency support, circular separation including wrap,
   geometric sum and harmonic row bounds (13)--(16). The proof is uniform in
   every coefficient, not just the displayed Mobius examples. No prime-log
   spacing or independence assumption is used.
3. Check the exact Abel endpoint H and its weight 1/[H(H+1)]. V/H is the
   whole future's main term. Both signs of the remainder are necessary. The improvement V<=4C_N E
   uses the COMPLETE tail starting at 2C_N; substituting it gives the
   squared relative rate 4C_N^2/[H(H+1)], not an unproved inverse bound.
4. Apply the inequalities before minimizing. The augmented b-coordinate makes
   the assertion a genuine Hermitian-form enclosure; the native b=1 slice is
   affine. Check first-N-cell coercivity and the unique finite minimizers.
5. Keep the support cutoff fixed in each application. The theorem does not
   certify the infimum over all possible supports from one finite support.
   For N=2Y it DOES cover the parent's original two-jet affine class, but its
   logarithmic constraint has not become rational.
6. Check the optional centering correction at s=0 versus the safe s=1 jets.
   Its support can become arbitrarily large. Infimum equality is not uniform
   bounded-ratio realization or norm contraction of an iterate.
7. Check the rational two-block centered candidate, its coefficient bounds,
   divisor mean square and the full tail at H=16Y^2. Its partial energy remains
   unknown at unbounded scales; the tail estimate alone proves no RH sign.
8. The executed minima use only p(1)=0, not p'(1)=1 or p(0)=-2. They are full
   finite-support minimum BRACKETS, not the parent's four normalized minima.
   Exact rational stationarity checks are backed by the analytic coercivity
   proof, not a numerical solver success flag.

No finite code can verify the infinite theorem merely from an output status.
The dependencies are the elementary theorems proved in PROOF.md and the
standard real/complex Hilbert-space definitions. The parent is context, not
an imported solution of the remaining arithmetic bound. Source/version and
computational execution boundaries are in SOURCES.json and VALIDATION.md.
