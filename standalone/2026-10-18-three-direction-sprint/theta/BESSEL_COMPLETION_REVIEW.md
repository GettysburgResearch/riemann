# Independent internal reconstruction of the Bessel attempt and cusp

Reviewed `../BESSEL_COMPLETION_ATTEMPT.md`, actual-byte SHA256
`58364d69ea5dff78f277dc80e40dfe89a5707b9b86bfa2cc10918e25d9c41b37`.
Reviewer: parallel theta track. No blocking error found at the stated
component scope. This is internal review, not an external referee
decision, priority claim or approval of an actual theta completion.

The base transform normalization is exact: the factor2 from evenness
cancels the Jacobian1/2 under t=2x, leaving K_(iz/2)(a). The Bessel
equation produces the displayed half-line Schrödinger equation with
eigenvalue z^2/4. Its large-A Laplace estimate and differentiated form
give the energy-space endpoint conditions for every fixed complex z.
The leading asymptotic also makes the solution nonzero. At a putative
transform zero the Dirichlet boundary condition at0 and integration
against conjugate(y) force z^2/4 to be a positive real number, hence
z real. No zeta spectral identification is used.

The R log R growth bound is order at most1 even though it need not
have finite exponential type. Paired real-zero Hadamard products still
have summable reciprocal squares and no quadratic exponential. Their
partial products give the stated real-rooted polynomial approximation.
For a nonconstant real-rooted polynomial, the squared distance difference
to each real root at z+ib and z-ib is4b Im z>0. Thus the sum of the two
shifted values has no upper-half-plane zero; real symmetry handles the
lower half-plane. Constant factors and b=0 cause no issue. Locally
uniform convergence transfers this result to F_a and its finite cosh
augmentations. The double-exponential kernel dominates every fixed
augmentation in the Fourier integral.

I also reconstructed the full weak-limit obstruction for its broader
auxiliary class. The weighted X^2 restriction proves local density
ratios from weak convergence. The positive three-anchor difference
bounds a_N. The1-to2 ratio then bounds the small-zero sum and large-zero
count. In particular its logarithmic lower bound3t/5 for t<=1 is
valid: log(1+3t/(1+t))>=3t/(1+4t)>=3t/5.
The anchor-normalized auxiliary product is therefore an entire normal
family. This is an entire-density extension argument, not an inference
that weak convergence preserves tails.

Finally the theta-cusp calculation retains the complete source. The
identity Phi=2v^(9/4)Theta''+3v^(5/4)Theta' expands to the same
normalized kernel used in the finite certificates. At v=i+epsilon,
the exact half-character Gaussian Poisson formula has frequencies
m+1/2. Extracting their smallest squared frequency1/4 leaves a uniformly
summable Gaussian tail after either of the two needed derivatives.
The resulting flat bound exp[-pi/(4epsilon)] times a fixed power of
epsilon forces all Taylor coefficients of any hypothetical holomorphic
extension at z0=i pi/4 to vanish. The analytic coordinate has derivative
1/(2i), so no order is lost. Identity with the positive real theta
kernel gives the contradiction. Nonvanishing along the cusp path is
not required, and none is assumed in the reviewed proof.

The zero-field closure obstruction has classical overlap with Newman's
1976 paper as credited separately in LITERATURE_SCOPE.md. The source
correctly leaves arbitrary changing onsite shapes and other observation
maps outside its theorem, and claims no RH proof or improved zeta band.
