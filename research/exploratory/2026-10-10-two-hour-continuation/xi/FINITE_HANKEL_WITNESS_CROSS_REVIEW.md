# Independent review of the constructive complete Hankel witness

Status: ACCEPT at source SHA256
`396f428d865c5bda2a67c141673700b29c48b08d776e7e3ea4f46e0d2f336513`.
Source: [cofinal-audit/CONSTRUCTIVE_FINITE_HANKEL_WITNESS.md](cofinal-audit/CONSTRUCTIVE_FINITE_HANKEL_WITNESS.md).
Reviewer: the outer-ray proof worker, independently of the author.
Scope: complete analytic FW1–FW4 review; no actual-Xi native negative form
or finite spectral-head authentication is claimed.

The complete inverse-square summability makes the node set bounded and
finite outside every positive-radius disk. Conjugate closure makes the
finite annihilator Z real, and excluding the target pair leaves Z(beta)
nonzero. The interpolation determinant Im(beta) is nonzero for an off-real
positive-half-plane root. Its real linear factor therefore has the exact
target value i*rho, giving beta*P(beta)^2=-1 and the conjugate contribution
also -1. Every other finite head contribution vanishes independently of
multiplicity. No spectral approximation occurs in these identities.

I checked the explicit coefficient bounds and complete tail price:
`|P_M(x)|<=C0*(eta/|beta|)^M` on the entire tail disk, and the sum of
absolute tail weights is finite. Choosing finite M with this squared price
less than the target multiplicity makes the complete quadratic form
strictly negative. This works even when the target is neither the largest
node nor a simple zero. A small imaginary part only increases C0 and the
required finite exponent. There is no omitted complex tail or substituted
finite-head moment matrix.

The complete Hankel contraction uses p_(i+j+1), with exactly the source
weight x in the functional. A strict negative form remains negative after
sufficiently close rational approximation of its finite coefficient vector.
The shifted version replaces the target root by a square root of 1/beta
and retains the same exact negative pair and absolute tail argument.
Removing known real occurrences does not remove an off-real target.

The result proves equivalence between all-order complete Hankel positivity
and a real spectrum under the stated imaginary-axis exclusion. It permits
real multiplicities and does not prove simplicity. Its refutation search
is conditional on a nonreal source zero and convergent native moment
evaluation. The proof uses a complete spectral head as mathematical data;
it does not claim that an actual-Xi zero computation has supplied such a
head or a negative coefficient vector.

This direct finite-filter argument pays the full tail and avoids a moment
representation import. It supplies the exact missing positivity condition,
not that condition's truth for the actual theta/arithmetic source.
