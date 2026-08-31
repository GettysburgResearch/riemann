# Independent review of native S3 curvature isotypes

Reviewed freeze:cb9278bec3844cc3fd8072987a6890f1df32a368.

NATIVE_S3_CURVATURE_ISOTYPES.md has Git blob
dca8a2d57dd922168604c6ea168389919c8ca910. The working proof has no diff
from this freeze. I read the complete proof and its final strengthening
for all three central projectors. This is a proof-only review; I ran no
scientific job or test suite. The coordinator also reported a complete
proof read before freezing it.

The multilinear kernel, its ungraded S3 character and the20-dimensional
curvature quotient are consistent. The degreewise characters give
three trivial, three sign and seven standard copies, and the displayed
central idempotents have the correct normalizations. The distinction
between the ungraded kernel isomorphism and its graded structure is
retained.

For general arity, the sign-vector argument makes Psi onto the stated
coefficient-form space. The radial polynomial potential for a closed
form has zero second derivative in each variable and is therefore
multilinear. This proves the exact quotient sequence and the character
formula fix(sigma)*3^(cycles(sigma)-1)-2^cycles(sigma)+1, with the stated
multidegree dimensions. It does not import an arithmetic-cover action.

The physical obstruction at H25 is also correctly scoped. A nonzero
W201 vector is observed, while W102 and W012 are absent. The trivial and
sign projectors introduce the former missing component, and the standard
projector introduces the latter. Thus each fails to preserve the visible
subspace. Passing to its annihilator in the dual and using an invariant
reference inner product proves the noncommutation with the pulled-back
physical Gram. This is not an assertion about every horizon or about the
infinite-horizon metric.

The unit-row test correctly prevents treating the ambient sign and
standard projections as legal native paths. Coordinate S3, arithmetic
cover S3 and parity/Walsh operations remain distinct. No physical
orthogonality, all-height projector or full retained-gamma conclusion is
claimed. No blocker was found in the stated source and representation
scope.
