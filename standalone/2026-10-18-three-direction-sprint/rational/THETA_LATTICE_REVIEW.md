# Independent internal review of the harmonic-lattice obstruction

Reviewed the full `../theta/HARMONIC_LATTICE_OBSTRUCTION.md`, SHA256
`d508313ca0cc475ee08800a8b1bf9c8f0e28089677c6407b7e9cab33e807bcd4`,
and its `HARMONIC_STAR.md` definitions/construction. This is independent
internal component review, not external referee acceptance or an RH result.
No blocking error found at the exact harmonic-tail, analytic-profile,
finite-head, fixed-hub scope stated in that draft.

The following points were reconstructed independently rather than inferred
from the supplied numerical checks.

1. The conditional log-MGF's second derivative has the displayed 1/(4x^2)
   factor. The one-sided Poisson formula has the correct half endpoint and
   phase exp(-2pi i k A). The first real-endpoint term after contour
   integration by parts is purely imaginary after that phase, so it
   vanishes under twice the real part. The next endpoint/remainder has
   the summable k^-2 bound. The other endpoint on the quarter circle
   has geometric decay in k. Thus a nonsummable endpoint error has not
   been summed by fiat.

2. The stated lower bound on the real part of t/(2x)+J(1/(2x)) is valid
   over the entire quarter sector when A,t are sufficiently large. The
   analyticity disk supplies |J(1/(2x))|<=C/(2|x|). Positive real part
   avoids every sech pole. The large-radius contour arc vanishes because
   of the x^-2 factor and the Fourier damping, including its near-real
   endpoint. No pole or unproved Stokes jump is crossed.

3. The sech-squared expansion has coefficient m after cancellation of
   the original 1/4. On the rotated ray its absolute bound is exactly
   a positive Laplace form with m(t-C)/r and kr. Both the m and k sums
   are absolutely integrable there. At large r, the m sum costs only
   a polynomial, while Fourier damping is exponential. At the fixed
   lower endpoint the t damping controls m. Grouping mk>=2 gives a
   strictly faster stretched-exponential scale.

4. For the leading term the analytic profile contributes 1+O(1/r).
   Comparing the absolute p=3 and p=2 Laplace integrals gives relative
   O(t^-1/2). The leading J=0 integral may be restored down to zero
   at exponential-in-t cost. The modified-Bessel integral and its
   asymptotic, checked against primary
   [DLMF 10.32.10](https://dlmf.nist.gov/10.32#E10) and
   [DLMF 10.40.2](https://dlmf.nist.gov/10.40#E2), give exactly
   C*=2sqrt(pi)(2pi)^(1/4), phase -pi/8-2pi a, and decay
   exp(-2sqrt(pi t)). The branches have argument -pi/4 as required
   after continuation onto the convergent rotated ray.

5. The continuum integral's Cauchy estimate is uniform in real u>=0:
   the small disk keeps Im J away from the sech poles and gives
   |sech^2(u+J(w))|<=C exp(-2u). Its Taylor remainder integrates to
   C D^q q! t^(-q-1). The coefficient-tail extension remains uniform
   for q<=delta t: u_0=t/(2A), j<=delta t<u_0/2, and the boundary
   Taylor ratio 1/(2Ar)<1/2 make the sum geometric. Optimal q proportional
   to t therefore gives a genuinely exponential remainder, not merely
   all-orders formal flatness.

6. The actual xi kernel is correctly normalized. Changing variables in
   the trigamma integral gives v exp(-v/2)/(1-exp(-2v)); the elementary
   quadratic prefactor gives -2v cosh(v/2). The nearest denominator
   singularities are at +/-i pi, and the positive-real growth is at most
   exponential. Cauchy estimates plus a short Laplace Taylor expansion
   give the same Gevrey1 optimal-truncation type. The absolutely convergent
   real log-zeta derivative series is exponentially small for large t.

7. With B>0 the other hub branch has exponentially small relative size,
   even after its fixed polynomial factor and two derivatives. Finite
   head changes have the same type. Equality with actual theta would
   force every integer coefficient to match; optimal truncation would
   then make the continuum difference exponentially small. The explicit
   sequence of t with cosine one contradicts the nonzero leading
   stretched-exponential term. The separate B=0 obstruction in the
   stated source covers that endpoint; no arbitrary graph, nonlattice
   tail, or nonanalytic profile has been excluded.

The conclusion is an obstruction to a specified complete model family.
It does not construct actual-theta approximants, prove an improved strip,
or settle RH. The finite Bessel comparison is a sanity check and was not
used as the justification for any analytic step in this review.
