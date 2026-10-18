# Internal review of the full fixed-onsite weak-closure obstruction

Status: **scoped internal review of proposed component mathematics.**
This is not a review or proof of RH or of a new zero-free region.

The coordinating track read the complete
`theta/ENTIRE_ONSITE_OBSTRUCTION.md` at raw SHA256
`d8258999312ad8b7be598f6e771718e877159a602141076c5cfb683a60006887`.
It also reconstructed the underlying native local-density compactness
lemma and the real-zero Gaussian-mediator predecessor. The rational
track separately reconstructed the main theorem.

For auxiliary zeros in a fixed finite band, one fixed rescaling puts
their MGF real parts inside .1. Pure imaginary zeros are represented
by actual single factors, not complex square roots. The quartet
logarithm is strictly concave as a function of x^2 beyond .02; its
fixed 1,2,3 finite difference is positive, comparable uniformly to
min(r^-4,1). This includes the near-zero and far-zero limits and the
remaining compact set. The exact positive onsite differences therefore
bound every positive onsite coefficient, the entire far-zero resource,
and the number of near factors. This is a conclusion from weak
convergence, rather than an assumed parameter bound.

The reviewer checked the explicit quadratic subtraction at far zeros.
For r>=1, the quartet polynomial is 1+A x^2+B x^4, where
A>=1.96/r^2 and A^2>=2B. Its logarithm is concave in x^2 on the
positive axis. Subtracting its tangent gives a nonnegative increasing
remainder at most 2r^-4 x^4. The local 1-to-2 potential ratio bounds
the remaining quadratic coefficient even when the original coefficient
diverges. Near factors have uniformly bounded normalized complex
polynomials, including when their zeros tend to zero.

The compact complex bound for the far renormalized product has a
convergent O_R(r^-4) tail; the bounded-radius residual set is counted
by the same resource. Thus the complete density ratios form an entire
normal family. They are identified on a real interval by the weak
logconcavity argument. The separate mass normalization on [1,2]
correctly recovers p_N(1), so the entire limit is the density on the
whole real line, including the inner interval. No tail-continuity
assumption is substituted for that step.

The coordinator supplied the native Jacobi-Poisson cusp argument in
`BESSEL_COMPLETION_ATTEMPT.md`; the rational track independently
reviewed its exact constants and coordinate. Flatness along the cusp
path plus positivity at real points excludes an entire continuation
of the actual density. Nonvanishing on the cusp path itself is not
required, and the final reviewed note correctly removes that extra
assertion. The proof does not infer anything about actual Fourier
zeros from nonanalyticity of the density.

No blocking gap was found at the stated scope. The conclusion excludes
the exact positive fixed-entire-onsite transfer architecture, with a
quadratic counterterm and uniformly strip-confined symmetric auxiliaries.
It does not exclude all direct spin observables or arbitrary cofinal
Lee--Yang constructions. Uncontrolled growing onsite families and other
observation maps remain outside this theorem. No priority over existing
closure theory is asserted by this internal receipt.
