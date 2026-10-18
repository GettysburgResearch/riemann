# Review and freeze record

## Independent review of the quadratic probe note

Reviewed file: ../field/QUADRATIC_PROBES.md.

SHA-256:
3eeee16681c63412c770662711cebfef1ddd2fbc1406118148ad5e74322a97dc.

The reviewer of that note is the author of the two native notes below,
not the author of the quadratic probe note. No blocking mathematical or
scope issue was found.

The review checked the primitive quadratic Gauss completion over odd
squarefree moduli and the substitution $v=-u/4$ in Proposition 1.
For Proposition 2, the polynomial has constant coefficient one and
degree at most $p-1$; cyclotomic irreducibility therefore forces every
coefficient to equal one. The multiplicative convolution eigenvalues
are the stated Jacobi sums, up to inversion of a character label. Both
exceptional eigenvalues are $-1$, and all remaining ones have absolute
value $\sqrt p$, so the claimed inverse exists. The Galois-closure
ramification argument proves the irreducibility assertion for every
sufficiently large prime for each fixed number field.

For Proposition 3, the ramified local correction is correct. The right
side has an exactly simple zero at one, whereas the square of a
holomorphic continuation would have even zero order. The scope is
limited to the stated uncentered summatory bound; it is not an
impossibility theorem for a branch-subtracted source. The Ramanujan
Dirichlet series in Section 4 retain the reciprocal zeta denominator
and have the asserted absolute convergence domains.

## Native notes and correction history

The following are the author's freeze records, rather than a claim of
independent review of the author's own files.

| File | SHA-256 |
|---|---|
| MOBIUS_CLOSURE_ATTEMPT.md | ecb78edf41a1632c8b9ef06a3edb7e8e11ecef605df924b5d9fc893f5935b457 |
| JOINT_NUMERATOR_CLOSURE.md | aa854ac365a480523bd26295c8a1e17359ba51963711fe86f45fbd02e23a12ce |

During independent review, the root reviewer identified an ambiguity in
the native note's balance bound: the constant norm bound applies only
at literal reciprocal sign crossings. The corrected Section 1 now
states the general-$Y$ bound, defines the crossing set, and asserts the
constant bound only on that set. It explicitly asserts no all-$Y$
constant bound or crossing-spacing estimate.

The final Section 6 recombines the complete prefix before applying the
crossing bound. It proves a norm estimate for the two boundary terms,
including all mixed terms through root-norm comparisons. The interior
quadratic expression remains. The note records no exponent contraction
and no new global zero-free boundary.

The separate field reviewer and the root reviewer independently checked
the joint domination algebra, the physical prime-supply transition, the
piecewise affine contour optimization, and the monotonicity argument in
the joint note. No blocking mathematical issue was reported. Inline
math delimiters were repaired afterward without changing that argument.
Its enlarged contour interval is explicitly an algebraic relaxation;
the note does not silently enlarge the analytic profile theorem.

No experiment or finite numerical predicate is a premise of these
arguments. No upstream proof or external analytic import has been
independently authenticated by this record.
