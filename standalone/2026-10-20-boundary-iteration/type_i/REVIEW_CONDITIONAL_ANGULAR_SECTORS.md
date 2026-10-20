# Review of the conditional angular-sector consumer

20 October 2026. Independent derivation check by the root agent of the
sector argument authored by the type-I agent. This review does not
independently re-prove the inherited theta reflection or common
zero-free premise.

Reviewed `CONDITIONAL_ANGULAR_SECTORS.md`, SHA256
`313bb31cf85a967533490ccea53d696d02db968717db194682d61a3ee63945a3`.
The frozen angular mean and uniform reciprocal dependencies are those
hashed in that note.

The strict inequality `p>(2 beta+1)/6` puts the ordinary Hecke factor
in the cube completion at `Re z>beta`. It is not an inverse completed
L-function with gamma factors. The finite conductor is fixed and its
angular analytic conductor is quadratic in `1+|ell|+|t|`. Deleted
Euler factors cost an arbitrary small power of the cubic row. Thus
the reciprocal has the claimed subpower angular and row cost, on a
fixed positive-width substrip.

Multiplying the reflected mean by this reciprocal bound gives the
square mean `B^(2-2p)` with angular/height power `4-4p`. Cauchy in the
`O(B)` outer rows then gives exactly `A^p B^(3/2-p)` and angular power
`2-2p`. Fixed radial Mellin decay absorbs the height integral; no
angular derivative whose order grows with ell is being hidden.

For a periodized bump of width Delta, its Fourier coefficient is
`Delta exp(-2 pi i k theta0) phi_hat(Delta k)`. Therefore the weighted
sum with power `2-2p+epsilon` is
`O(Delta^(-2+2p-epsilon))`. The zero coefficient is precisely
`Delta integral(phi)`, so the subtraction of the actual `T0` is exact.
This is essential: the spherical mode may have a main term.

The ratio of the conditional error to the unconditional error, with
small losses suppressed, is

\[
             (A\Delta^2/B)^{p-1/2}.
\]

Since `p<1/2`, the improvement condition is `A Delta^2>B`, as stated.
Writing `A=X^a`, the exponent of X before the width loss is
`3/2-p+(2p-3/2)a`. Comparing to the absolute scale `X Delta` gives

\[
 \xi_p(a)=\frac{p-1/2+(3/2-2p)a}{3-2p}.
\]

Substitution of the limiting allowed p gives (S12); subtracting `a/4`
gives `(1-beta)(3a-2)/(4(4-beta))`. Hence the gain occurs exactly for
`a>2/3`. The balanced width remains `X^(-1/8+eta)`. The `a=1` example
and the stated positivity threshold are consistent. The positive
buffers in p, epsilon, and the width exponent are chosen in the
correct order; no endpoint-uniform constant is assumed.

**Verdict:** no gap found in this consumer under its explicitly stated
upstream hypotheses. It is a smooth weighted Gauss-sector discrepancy
for a free inner column. It is neither a prime-sector theorem nor a
smaller numerical zero-free bound. A change to the reviewed source
requires a new hash and review.
