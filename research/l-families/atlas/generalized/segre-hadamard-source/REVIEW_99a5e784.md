# Independent review: equivariant matrix-factorization trace

Scientific freeze: `99a5e78462f6e1c17334f16a887089c756032b2f`.
Reviewer: the extension-order lane, not an author of this packet.
Conclusion: no mathematical or implementation blocker found.

I read the entire proof, producer, replay contract, and all 18 test sources.
The five scientific files agree with the exact freeze by Git comparison.
I inspected the artifact's source/owned-file manifest and its determinant,
second-power, and representative Tor-weight records. The declared proof and
artifact pins at `a895f47628b0bc7c7ee5e0392df2f79c24166f92` match local Git
objects already checked in the companion invariant-base review.

The map columns carry the stated delta powers: the two generator characters
in homological degree i are delta^i r and delta^i s. Their degree shifts and
the two-step determinant-square twist are necessary for equivariance. The
even/odd source-monomial characters give the claimed rational functions.
Both finite-order examples have zero first trace on every nonzero two-
dimensional Tor module, while the squared operator recovers trace two.
The ordinary determinant remains 1-u^2. These are all-degree consequences
of the actual character formula, not extrapolations from the displayed rows.

The replay uses exact Gaussian integer pairs and literal source monomials.
It separately verifies the matrix weights, rational character formulas,
Chow-source character, and all Euler rows visible at the cutoff. Generic
positive inputs and the second finite-order input are meaningful controls.
Source authentication precedes its reconstruction, and serialized comparison
distinguishes Boolean or floating numeric aliases from integer coordinates.

Root reports all producer modes and 18 tests in each interpreter mode passed.
No computation was run by this reviewer. The residual operator is explicitly
a finite linear model, not a claimed Frobenius of a previously constructed
global cover. The actual infinite resolution is not replaced by the finite
free-looking scalar character, and no new abstract periodicity theorem is
claimed. Frozen early status text remains unchanged.
