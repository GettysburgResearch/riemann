# Review of the full column adapter and simultaneous conductor cleanup

Status: **internal component reconstruction; the coherent complement remains open.**

The coordinator read `rational/SQUAREFREE_COLUMN_ADAPTER.md`, raw SHA256
`76813808d72bb24dce02aaa372bc68595fde2ab6d92a5d164f7222e468489efe`.
The unique factorization n=h^2 s, g=(d,s), d=ga,s=gb gives exactly its
coefficient and central normalization. No coprimality with h is available
or imposed. Its row power keeps every shared-prime zero.

The input mask identity uses the COMPLETE Q-smooth convolution, rather
than just squarefree divisors. Its central-line absolute resource is the
stated Euler product, a subpower for polynomially bounded Q. In the
coprimality projector the two Mobius factors cancel. The resulting outer
coefficient is +1/Nell, not mu(ell)/Nell. The imported inverse second mean
at shortened lengths <=C U and the trivial squarefree plain bound then
give the stated complete B bound. Summing the FULL g and h tails by
Minkowski gives UN/G and UN/H^2, with their overlap paid by the triangle
inequality. Their hardest retained g=h=1 component remains unestimated.

The stripped primitive cross character has conductor xy after removal of
the shared R. Its CRT phase involves theta(R)^(-2); the original shared
R remains a zero-only mask. Replacing the stripped characters by the full
columns would spuriously kill this actual contribution. The note retains
this distinction and does not claim a positive large sieve for the full
signed covariance.

The reviewed `rational/ROW_CONDUCTOR_FILTER.md` has raw SHA256
`cbd1272574d7de0668f9a76c4f8760d3346a2c4e23845220754320f42c54974c`.
At every good prime of valuation 1 through 5 the primitive local character
has conductor p. Primitive planar Poisson has unit root number, even for
a nonsquarefree presentation of that row. Absolute Schwartz counting gives
|S_N|^2<=C Q_u/N at both long and subunit dual lengths. The low-conductor
row subset is positive, so its product mean is bounded by this pointwise
bound times the original all-row inverse mean. This does not reindex the
inverse theorem by the moving conductor. The conditional witness
consequence and powerful-part inequality follow directly.

The reviewed `rational/JOINT_CONDUCTOR_CENTERING.md` has raw SHA256
`b050fa36e376ae268b525bfecab6c19265f51a70aef1c97d8ef530d9ffd9258e`.
The smooth radical partition is made on the original positive mean. On
each powerful part z the remaining squarefree variable has a uniformly
smooth radial cutoff; the changing radical scale does not enlarge its
Euler derivatives. The complete powerful sum has subpower mass at the
needed exponent. Thus the filtered pair kernel has its OWN valid
sqrt(U) C^(1/4) estimate. The stronger unfiltered sixth-free estimate
cannot simply be reused after inserting this arithmetic filter.

Section 5 gives a different legal comparison: the removed low-radical
rows number at most Q0 U^epsilon, since each radical has at most
5^omega(r) valuation choices. At each fixed pair conductor the original
coefficient absolute mass is C^(-1/2) up to subpowers. This pays their
entire small-pair-conductor sector by Q0 sqrt(Q1), before subtracting it
from the actual unfiltered sector. All both-different conditions and
shared-prime masks stay under the same absolute coefficient majorant.
The exponents at Q0=U^(51/80),Q1=U^(9/8) are exactly
1,91/80,115/96,6/5. This proves the displayed cleanup, not a bound for
its remaining signed high-row, high-pair-conductor form.

Combining this centering with the outer column adapter would require
centering in the adapter's new variables. It is not legitimate to move
the original both-different restriction through a Minkowski decomposition.
These scope restrictions are explicit in the reviewed notes.
