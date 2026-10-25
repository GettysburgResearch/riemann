# Independent review of the marked arithmetic components

Reviewer: fractional-parameter track, 25 October 2026.

Verdict: **PASS for the stated component theorems, after the scope
corrections recorded below.** No new zero-free half-plane is certified by
this review. The fixed-power estimate for the signed marked discrepancy
and the native sextic fractional mean remain open.

This was an independent analytic review of the proofs, including the
branch conventions, signed contour comparison, dependence on the growing
integer parameter, and the Mellin-transform contradiction. No finite
numerical experiment was used to certify an analytic assertion.

## 1. Exact reviewed files

All three files are in `second-pass/marked/`.

| File | SHA-256 |
|---|---|
| `MATCHED_PRIME_SQUAREFREE_REMAINDER.md` | `6cf6a71909f23fa29f7b1d7a0833da477fc2b1a58d9c81aeab8bdc19032348b0` |
| `GROWING_INTEGER_RESONANCE.md` | `5a42b1ce61200a33e5bef112f5691fe03e3b9a9457779f8515952e46875347d2` |
| `GEVREY_INTEGER_WINDOW.md` | `2eabc9818994e00d8113c237d95eb76a7dae46675000c45adf60f97279d9d216` |

The exact circle convention was checked against PR #1021's
`POSITIVE_MARKED_COUNT_TARGET.md`, SHA-256
`18e58007abfa604c3e884e60b4721e6b15c86e63335e23c147dcff13364540af`,
at mathematical commit `742e952be4ef7843de86ea12678c0bdd3d3579c3`.

## 2. Prime/squarefree discrepancy and principal matching

The local convolution identity is correct. At a prime, the logarithmic
coefficient is `q/(1+q)`, so multiplication by the squarefree Euler
factor `1+q` gives `q`. The correction coefficients
`(-1)^(j-1)-1/j`, including the zero correction at `j=1`, therefore
give the stated global identity for `mu^2 omega`. The prime-square
remainder has size `sqrt(X) sum_(p<=sqrt(2X)) 1/p`; prime powers of
exponent at least three have an absolutely summable square-root weight.
Completing the correction main term costs `O(sqrt(X))`. No prime
diagonal is silently discarded.

The continuous density `(1-u^(-1))/log u` has exactly the Mellin
transform `log(s/(s-1))` for `Re s>1`. Its removable value at one and
its zero extension below one are compatible with the stated Stieltjes
convention. The discrepancy is finite before any contour manipulation.

The full principal matching is exact. On the known disk around one,

\[
 \log\zeta(s)-\log\frac{s}{s-1}
 =\log((s-1)\zeta(s))-\log s
\]

is holomorphic and vanishes at one. Its product with
`F_1(s)=zeta(s)/zeta(2s)` is therefore holomorphic. This is stronger
than agreement of finitely many asymptotic coefficients. The correction
`F_1 h_1` contributes precisely the stated simple-pole residue.

The cutoff sign was checked independently in two ways. The lower-minus-
upper jump of `log(s/(s-1))` is `2 pi i`. Also differentiation of the
exact real-integral principal term in PR #1021 with respect to its
radius gives `F_1(1-r) W_hat(1-r) X^(1-r)`. Both give

\[
 C_c^{(0)}(X)-C_b^{(0)}(X)
 =\int_c^b F_1(v)\widehat W(v)X^v\,dv.
\]

For a nonnegative nonzero profile the integrand at the upper endpoint
is negative. The endpoint expansion and its sign in the note are
correct. The remaining vertical integrals need no unproved zero-free
region: `1/zeta(2s)` is bounded by its absolutely convergent series
on the line `Re s=c>1/2`, and smooth Mellin decay beats the polynomial
growth of zeta. The two one-sided values at `c` are finite.

Under the explicitly conditional hypothesis `|R(u)|<=C_R u^beta`, the
reciprocal moment exists by integration by parts. Its value is exactly
zero because the continued Mellin transform has value
`log(G(1)/1)=0`. Thus replacing `S_W(X/u)` by its error `E_W(X/u)`
is justified over the complete infinite integral. The boundary at one
vanishes since `R(1)=0`; the boundary at infinity vanishes since
`beta<1`. The derivative bound on the two ranges gives

\[
 \sqrt X\int_1^{2X}u^{\beta-3/2}\,du
 +X\int_{2X}^\infty u^{\beta-2}\,du
 \ll_{\beta}X^\beta.
\]

This genuinely removes the earlier separate-hyperbola loss. It
recovers the supplied exponent `beta`; it does not improve that
exponent or prove the hypothesis about `R`.

The local Hankel coefficient is also correct. Multiplying the local
coefficient `m g(rho)` by the inverse-Laplace factor
`(-1)^(m+1) m!` gives the displayed
`(-1)^(m+1) m zeta^(m)(rho)`. The final file explicitly restricts this
discussion to `Re rho>1/2`, where the denominator `zeta(2rho)` is
known finite and nonzero. The note correctly treats this as a local
germ calculation, not as a global zero expansion.

## 3. Growing integer resonance

The resonance is actual growth of the continued Euler product. With
`R=K^(1/sigma)` and `t_K=pi sigma/log R`, one has

\[
 Kp^{-\sigma-it_K}
 = e^{-i\pi\sigma}(p/R)^{-\sigma}
      e^{-it_K\log(p/R)}.
\]

The limiting phase is in the open lower left quadrant. It is not on
the forbidden negative axis. In fact no local factor can vanish at
the selected point: a zero of `1+Kp^(-s_K)` would first force `p=R`
by its modulus, and then require `e^(-i pi sigma)=-1`, impossible for
the fixed `1/2<sigma<1` under review. The real logarithms in the
resonance argument are well-defined.

The prime-number-theorem passage is valid with the stated order of
limits. On a fixed compact interval in `p/R`, the integrands converge
uniformly. The small-prime tail, normalized by `R/log R`, is bounded
by a constant times `delta^(1-sigma)` after taking `K` large for fixed
`delta`. The large-prime tail is bounded by a constant times
`M^(1-2sigma)`. Both powers have the required signs. The error from
expanding only `K log(1-p^(-s_K))` is `O_sigma(K)`, which is
`o(R/log R)`.

The integral and its branch were checked directly. For
`alpha=1/sigma` in `(1,2)`, differentiation on the positive real
`z` axis gives

\[
 \frac{d}{dz}\int_0^\infty
   [\log(1+zy^{-\sigma})-zy^{-\sigma}]\,dy
 =\frac{\alpha\pi z^{\alpha-1}}{\sin\pi\alpha}.
\]

Scaling fixes the integration constant, and both sides continue
holomorphically to the slit plane. The principal power of
`z=e^(-i pi sigma)` is `z^alpha=-1`. Consequently the real constant
is `-pi/sin(pi/sigma)>0`, with exactly the sign claimed. The factor
`zeta(s_K)^K` changes its logarithmic modulus by only `O_sigma(K)`;
nonvanishing on the relevant real interval is elementary.

The complete pole subtraction is controlled at the required scale.
On the shrinking pole circle of radius `1/log K`, the near-prime
cost is `O(K log K)`, the far-prime cost is `O(K)`, and the pole of
zeta contributes at most `O(K loglog K)` to the logarithm. Cauchy's
principal-part kernel stays a fixed positive distance from its pole
when evaluated at `s_K`. Hence the pole part has logarithmic size
`O(K log K)`, negligible compared with `K^(1/sigma)/log K`.
The positive profile ensures `W_hat(s_K)` tends to a positive value;
the smoothing cannot erase this near-real resonance.

The uniform-quantifier contradiction is sound. For fixed `K`, the
asserted uniform bound is available for every
`X>=exp(4K log K)`. The integral over that upper range converges on
`Re s>b`; the lower range contributes at most
`exp(O(K(log K)^2))`. The Mellin transform of the exact residue
polynomial on `X>=1` is precisely its Laurent principal part. The
piece `X<1` has only the unit term and is independent of `K`. Thus
there is no unaccounted large principal term in the contradiction.

Choosing `max(1/2,b)<sigma<1` makes
`K^(1/sigma)/log K` dominate `K(log K)^2`. For the window
`K<=(log X)^theta`, choosing
`max(1/2,b)<sigma<theta` gives the same contradiction with the lower
split `exp(2K^(1/theta))`. This proves the necessary condition
`b>=theta` exactly in the stated range `1/2<theta<=1`. It does not
assert a contradiction for unrestricted constants depending on a
fixed `K`, or for a differently normalized character-family mean.

## 4. Gevrey profile and the positive uniform window

The chosen bump has the claimed uniform Mellin decay. On a disk of
radius a fixed small multiple of the distance to the nearer endpoint,
`Re(1/q(z))` is bounded below by a positive multiple of the reciprocal
distance. Cauchy's formula therefore bounds the `j`th derivative by
`C^(j+1)(j!)^2`, uniformly for the real Mellin parameter on a compact
strip. Choosing `j` proportional to `sqrt(|t|)` after integration by
parts gives `exp(-c sqrt(|t|))`. Extension by zero is smooth because
each fixed derivative tends to zero at the endpoints.

The uniform Euler-correction estimate has the right scale and no
unstated `K` dependence. Splitting at `P=(2K)^(1/sigma)` gives

\[
 K\sum_{p\le P}p^{-\sigma}
 +K^2\sum_{p>P}p^{-2\sigma}
 \ll_\sigma K^{1/\sigma}/\log K.
\]

The elementary prime-counting upper bound suffices. Possible zeros of
finite Euler factors cause no problem for an upper bound on the
modulus. The tail logarithms use absolutely convergent Taylor series.

The contour shift is first performed for each fixed integer `K`.
This is legitimate since the smooth Mellin decay beats every fixed
polynomial in height. Only after obtaining the exact integral is a
uniform estimate applied. Euler summation gives
`|zeta(sigma+it)|<=C_sigma(1+|t|)`. The resulting integral of
`(1+t)^K exp(-c sqrt(t))` is at most
`C^(K+1)(2K+2)!`, giving exactly the additional `O(K log(2K))`
in the exponent. There is no exchange of an uncontrolled growing
parameter and an infinite contour limit.

For `K<=(log X)^theta`, choosing a fixed
`sigma>max(1/2,theta)` makes both uniform exponential costs
`exp(o(log X))`. This remains true with any fixed power of
`loglog X` in the parameter cutoff. The upper exponent
`max(1/2,theta)+epsilon` is therefore proved; when `theta>1/2`,
the resonance result supplies the matching necessary threshold up to
the arbitrarily small loss. Nothing here asserts optimality at or
below `theta=1/2`.

The factorial correction in the local-zero discussion is essential
and correct. The elementary coefficient is
`(-1)^(N+1) N! X^rho/(log X)^(N+1)`. If `N=o(log X)`, Stirling's
formula makes its logarithmic suppression `o(log X)`. In particular
`N` of order `log X/loglog X` does not by itself supply a fixed
power saving. This calculation is explicitly separated from an
unproved uniform moving-order arithmetic Hankel expansion.

## 5. Corrections made during this review and retained limitations

The author applied the following requested corrections:

- The conditional discrepancy bound now states dependence on `beta`
  and the input constant `C_R`.
- The local branch discussion in the integer-order notes now includes
  any vanishing order of `H_K` and of the smoothing transform.
  Finite Euler factors of `H_K` can vanish.
- The marked zero germ is explicitly restricted to `Re rho>1/2`.
- The growing-resonance discussion now points to the factorial
  correction rather than suggesting that order `log X/loglog X`
  could supply a fixed power merely by controlling other constants.

The marked note also explicitly distinguishes generic worst-case
Chebyshev conditioning from an actual-family lower bound. That
qualification is necessary: the failure of a generic interpolation
guarantee is not a proof that every arithmetic transfer fails.

The component results establish an exact discrepancy formula, a real
recovery of an input prime-error exponent, a uniform growing-order
upper theorem, and an actual arithmetic obstruction at larger orders.
They do not prove the decisive noninteger or signed-remainder estimate,
move the imported numerical zero-free boundary, or transfer the scalar
statements to the physical sextic row family.
