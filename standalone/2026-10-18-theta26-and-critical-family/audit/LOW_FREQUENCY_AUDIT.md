# Independent review of the retained-window logarithmic packet

**Pass for the counterexample class as stated.** The reviewer did not author
the construction and read its complete argument, including the final
first-coefficient normalization and distributional clarification.

Reviewed file: `arithmetic/LOW_FREQUENCY_ATTACK.md`.

SHA-256: `cc11e3456b5c77a4414fc31d1c684ac4c6d7dd2be483d0695b5bfcab8a8c3b0a`.

The theorem concerns the exact native spectral operator acting on a larger
class of old coefficients. It is not a counterexample to an estimate for
the actual Möbius coefficients. In particular, the constructed coefficients
do not satisfy the full old-prefix Dirichlet inverse identities, and the
manuscript does not apply the native Newton recurrence to them.

## Squarefree interpolation and exact balances

The blockwise construction interpolates a smooth logarithmic packet with
positive reciprocal squarefree weights. The elementary squarefree-count
error suffices for blocks of length `ceil(100*sqrt(Y))`; all blocks meeting
the packet have positive mass bounded below by a fixed multiple of `H/Y`.
The resulting coefficients have size `O(Y^((kappa-1)/2))`, so are bounded
by one for large Y. They are supported on squarefree integers. The prefix
sum agrees with the prescribed smooth function at block endpoints and has
uniform interpolation error `O(Y^(kappa/2-1))` between endpoints.

After logarithmic rescaling this gives the stated L1, L2, and uniform
`O(Y^(-1/2))` errors with common compact support. Changing variables in
the energy has the correct factor `exp(u)`; the unit-cell equality is
exact because the prefix vanishes near its upper endpoint.

Both finite base prefixes have first coefficient one and zero reciprocal
sum. Their reciprocal identities and logarithmic moments were rederived.
The first logarithmic magnitude is `log(360)/6<1`, while the second is
greater than one. The packet's logarithmic moment tends to zero from
below. Their convex mixture therefore gives `a_Y(1)=1`, all coefficient
magnitudes at most one, and both M and B exactly zero. Its prefix sum
vanishes above index 11, so it contributes only bounded old energy and
does not overlap the moving packet.

## Full spectral convergence

Partial summation gives the factor
`Y^(kappa/2-it)*(s-1)*fhat_Y(t)` with the correct Fourier sign. Squaring
and retaining the actual zeta factor yields the proposed limit
`zeta(s)*(s-1)*fhat(t)^2`.

The proof pays all high frequencies using homogeneity of the previously
reviewed polynomial moment bound. At the auxiliary cutoff `Y^(1/4)`,
the normalized tail tends to zero after choosing a sufficiently small
epsilon. On the remaining interval, the error linear in the uniformly
small Fourier discrepancy is integrable because the fixed packet is
smooth. Its quadratic error has squared norm
`O(Y^(-2)*Y^((3+13/42)/4+epsilon))`, with exponent `-197/168` before
the small loss. The fixed base's cross term is negligible using the
second polynomial moment, and its pure contribution is integrable using
the same pointwise zeta exponent.

Thus the asserted convergence is genuinely in full spectral L2. Projection
onto any growing frequency window preserves it by contraction and the
vanishing tail of the fixed limit. This is stronger than an argument on
one compact frequency interval and correctly prevents unaccounted
cancellation by other retained frequencies after physical restriction.

## Causal impulse and physical window

The differentiated remainder kernel was checked locally as a distribution.
Two applications of `D-1/2` remove its smooth linear bracket and yield the
stated combination of delta derivatives and delta masses at `log n`.
The infinite impulse expression is first interpreted on compactly
supported tests. Its tempered interpretation for Fourier analysis comes
from differentiating the L2 kernel on the left; a divergent termwise
Schwartz-function sum is not assumed.

Convolution with the fixed compact smooth `g=f*f` is therefore valid and
is a finite sum at each physical point. The chosen support width is
strictly less than `log(2)`, so on the first negative packet interval only
the `n=1` impulse contributes. The retained limit there is `g'-g/2`, with
squared norm `||g'||^2+||g||^2/4>0`. This calculation preserves the signed
zeta multiplier and proves that it does not annihilate the packet.

After translation by `2*log(Y)`, the literal strict square-step window
converges to the negative half-line. Its multiplication operators are L2
contractions. Full L2 convergence and dominated convergence give the
claimed positive norm limit, including every growing cutoff. For a fixed
positive cutoff, the nonzero bandlimited limit is entire and cannot
vanish on a whole half-line, which supplies the separate positive constant.

The final exponent comparison is consequently correct: a uniform bound
using only this larger class must pay
`alpha >= (2-p)*kappa`. The sample `p=3/2, alpha=1/3` fails on that class
for `kappa>2/3`. This identifies information insufficient for the proposed
spectral strategy. It leaves open whether the full Möbius inversion
identities eliminate the obstruction for the actual target.

No finite computation is presented as a check of the asymptotic theorem.
The proof uses the already reviewed native transform and polynomial-moment
bound, with Bourgain's named pointwise theorem as an imported input.
