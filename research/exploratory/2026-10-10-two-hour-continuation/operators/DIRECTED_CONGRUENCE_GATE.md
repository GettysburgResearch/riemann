# An exact congruence resolves interval elimination overestimation

Status: exact analytic acceptance lemma and new directed implementation.
This document does not assert that the physical native matrix has passed;
the completed separate receipts specify actual executions.

Let S be the actual real symmetric finite lower matrix, enclosed entrywise
by an outward symmetric Arb matrix A. For a specified exact epsilon>0,
choose ANY exact real square matrix P and enclose

C=P^T(A-epsilon I)P.

For each row, let its directed rational margin be the exact lower endpoint
of C_ii minus the sum of the larger absolute rational endpoints of C_ij
over j!=i. If every margin is strictly positive, the actual Hermitian
congruence is positive definite by Gershgorin (equivalently, the elementary
inequality2|x_i x_j|<=|x_i|²+|x_j|²). This argument covers complex coefficient
vectors and all correlations allowed by the input balls.

Its positivity itself forces P to be nonsingular: if P x=0 for a nonzero
x, the congruence quadratic form would vanish. Since P is square, it is
invertible and the actual S-epsilon I is positive definite. Thus S>=epsilon I
with no need to authenticate a separate inverse or determinant identity.

The helper selects a convenient P by enclosing the Cholesky factor of the
exact dyadic midpoint matrix minus epsilon I, then computing its inverse
transpose. This is ONLY a proposal generator. Every proposed entry is
replaced by its exact dyadic midpoint; the resulting P is a literal rational
matrix. Its approximate inverse quality is not an acceptance premise.
All acceptance comes from freshly enclosing the full congruence, including
EVERY original radius, and checking the exact rational row margins. No
floating eigenvalue or midpoint positivity is promoted to a certificate.

This is useful when ordinary interval LDL elimination magnifies repeated
interval dependencies. The original physical length21/20 weighted LDL
gate failed inconclusively at its ninth pivot. The original completed R,
all source/trial/coverage guards and failed log are preserved. A distinct
wrapper computes the SAME complete weighted lower matrix and uses this
new acceptance lemma. It does not shrink a source interval, ignore a prime
tail, infer negativity from the old failure, or repeat the R integration.

The source-specific weighted dual and primitive completion arguments are
unchanged. A successful new finite congruence gate supplies the SAME exact
epsilon premise required by those analytic arguments. Independent review
and paired normal/optimized runs remain necessary for artifact acceptance.
