# Internal review of the growing probe span and actual rectangular centering

Status: **source-qualified component review; no full mixed mean approved.**

The coordinator read and reconstructed
`eisenstein/GROWING_GAUSS_GRAM.md`, raw SHA256
`6953daaa8ddf829d68b28458de59025aa5d25b19db0c8486415b18a9df638e5e`,
and `rational/ACTUAL_RECTANGULAR_CENTERING.md`, raw SHA256
`922b9b0c14f9de13cb3c8abbc23d74b96c344002562573de41e3bdffeec80c65`.
The latter identity includes the explicit convention that the fixed twist
is already in the input coefficients and is not applied a second time
inside psi. The preceding reviewed formulas are unchanged.

For squarefree rows, inserting the exact Mobius-square expansion into
the primitive planar character kernel gives the sum of
min(U/(Na)^2,sqrt(NC)). Its split at sqrt(U)(NC)^(-1/4) gives
sqrt(U)(NC)^(1/4). The zero-only masks are retained, including their
overlap with conductor primes, where their corresponding terms vanish.
Distinct sixth-power-free labels have a nonprincipal quotient at some
good prime, so a fixed ray twist cannot turn it into a principal pair.
The diagonal local density Q/(Q+1) is positive. Normalization and the
O(K) label count give the stated Gershgorin range K<U^(1/3).

The full-sixth-free-row version uses the actual kernel already jointly
derived in this sprint: sum min(U/(Na)^6,sqrt(NC)) gives
U^(1/6)(NC)^(5/12). After diagonal normalization the row sum is
U^(-5/6)K^(11/6), giving K<U^(5/11). Its common phase on nonsquarefree
rows is explicitly a stipulated unit phase. It is not misidentified
with a raw Gauss sum that can vanish there. This part shares the
coordinator's earlier kernel derivation, so it is not an independent
root derivation of a theorem invented solely by another track.

For either row space, the actual source inverse second mean at D=U
and elementary plain second mean at N=sqrt(U) give a U-sized squared
pairing against every flat probe. The conditioned Gram inverse then
pays the entire K-dimensional orthogonal row projection by U K, and
K=U^(1/5) gives U^(6/5). The formula is the genuine V G^-1 V* row
projection. It is not a statement about bare column Gauss coefficients
or a complete spectral decomposition. The source comparison's adjoint
remainder and the complementary row space are still unpaid.

The rectangular-centering note expands the original four variables
before bounding. Each complete d1=d2 or n1=n2 strip is a positive
single-factor second moment times a coefficient square mass O(1).
Their common strip costs O(U), with every zero mask and shared prime.
Inclusion-exclusion gives the complete both-different covariance up
to an O(U) error. The union itself need not be positive; the proof
uses the absolute error bound, not an invalid positivity assertion.

The small-conductor absolute pair majorant remains valid after the
both-different restriction: at fixed collapsed products it is still
bounded by tau(A)tau(B)/L, independently of any cancellation inside
their convolution coefficients. Thus Q=U^(9/8) costs U^(115/96),
leaving the stated 1/480 exponent margin below U^(6/5). The remaining
complete both-different high-conductor covariance is an OPEN estimate,
and its corner bound would still require the all-length consumer.

No blocking gap was found in these component arguments. The separate
positive-completion barrier correctly concerns a nonnegative resource
introduced by adding collision terms; it is not a lower bound for the
actual mixed mean. None of these projections or centerings supplies
the missing complementary signed estimate.

For comparison with a row matrix carrying sqrt(w), the same pairing
argument applies to the weighted vector sqrt(w)f: its flat multiplier is
w instead of sqrt(w). Boundedness of the one fixed nonnegative profile
preserves the U K estimate. This does not change either frozen proof.
