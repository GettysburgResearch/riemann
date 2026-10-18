# Independent review of the complete theta source and Gaussian polynomial certificates

## Verdict and precise scope

**Pass for the finite existence claims.** The reviewed source and directed
checker prove the existence of the three claimed real-zero entire functions,
matching the actual variance-one theta function through Taylor orders 22, 24,
and 26. No load-bearing defect was found in the source normalization, analytic
remainder bounds, power-sum matching equations, or full-cube contraction.

The order labels describe matched Taylor coefficients. The polynomial factors
have degrees 128, 256, and 256, respectively. The approximants need not be
characteristic functions of positive probability laws. The proof uses their
entireness, real zeros, coefficient matching, and common growth bound.

The conditional all-order implication is correct, including the final
strengthenings that remove the Gaussian reserve and then allow positive real
weights in a construction on the two open half-planes. The remaining cofinal
positive weighted construction remains unproved; the finite certificates establish
neither RH nor any improved zeta zero-free boundary.

This review was performed independently of the parameter search. It includes
analytic inspection and complete-source replay with the inherited directed
backend. It is **not** a second implementation of interval arithmetic.

## 1. Identification of the actual theta function

The density used by the producer has the correct physical Fourier variable.
One way to check all constants directly is to set

\[
 \psi(x)=\sum_{n\ge1}e^{-\pi n^2x},\qquad
 g(t)=e^{t/2}\psi(e^{2t}).
\]

Differentiation gives precisely

\[
 g''(t)-\frac14g(t)
 =\sum_{n\ge1}(4\pi^2n^4e^{9t/2}-6\pi n^2e^{5t/2})
                   e^{-\pi n^2e^{2t}}=\Phi(t).
\]

The theta transformation implies
`psi'(1)=-(1+2 psi(1))/8`, hence `g'(0)=-1/4`. Integrating twice by parts gives

\[
 2\int_0^\infty\Phi(t)\cos(zt)\,dt
 =\frac12-2(z^2+\tfrac14)
                    \int_0^\infty g(t)\cos(zt)\,dt
 =\xi(\tfrac12+iz),
\]

where the last equality is the ordinary split-at-one theta integral for xi.
All integrals converge locally uniformly in complex `z` by the exponential
decay of the density. Every summand of `Phi(t)` is positive for `t>=0`, so the
normalizing mass is positive.

Consequently the standardized target is
`H(z)=F_theta(z/sqrt(v))`, with `v=E[T^2]`. The physical approximant is
`P(sqrt(v) z)`. This direction of rescaling, including its consequence for
nonzero Fourier zero bands, agrees with both source and proof.

## 2. Complete integration and interval backend

The imported primitive is authenticated by Git blob
`c32015f110d10186538ffabcb4689ba5bbc060d0`; its SHA-256 is
`2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55`.
The new settings of 512 fractional bits and Taylor degree 220 are read as
module globals by the operations used here. The review checked outward
integer multiplication, division and reciprocals, exact rational coercion,
integer square roots, the argument-reduced exponential enclosure, and the
alternating Machin-formula remainders. Changing precision does not discard
those elementary-function remainders.

The new integration uses 162 cells over the eleven stated index-specific
intervals. The density polynomial is multiplied by the full moment polynomial
before integration; the product is not truncated back to degree 220.
`integrate_moment` includes the even extension's factor two.

The following three omitted contributions are all bounded and included:

1. On the radius-`1/8` Cauchy circles the density modulus is below `10^16`.
   The half-cell ratio is `1/4`, and the full explicit integration length is
   `81/4<32`. Thus the stated complete error
   `32*10^16*(5/2)^j/(4^221*(3/4))` bounds raw moment `j`. It enlarges both
   endpoints.
2. Each of the eleven time tails is bounded using
   `exp(2x)>=1+2x` and the positive rate
   `lambda=2*pi*n^2*exp(2U)-9/2`. Expanding `(U+x)^j` and integrating gives
   exactly the producer's finite factorial sum. Dropping the negative
   prefactor term gives a valid upper bound.
3. Every omitted theta index `n>=12` is included by the stated geometric
   majorant. The ratio of consecutive `n^4*exp(-pi*n^2)` terms is below
   `1/2`, while the denominator increases. The leading-index expression
   multiplied by two is therefore a valid bound for the whole tail.

Time and index tails are positive and enlarge only the upper endpoint.
Division by the enclosed positive mass, variance normalization, and the
finite cumulant recursion all preserve enclosure. Dependencies between
moments may widen intervals but do not invalidate their inclusion of the
single actual theta vector. In particular the actual standardized variance
is exactly one even though its outward interval may have positive width.

## 3. Matching equations and the entire approximants

For

\[
 P(z)=e^{-az^2}\prod_{j=1}^{N}(1-b_jz^2),
 \qquad a=\tfrac12-\sum_jb_j,
\]

the logarithmic coefficient of `z^(2r)`, for `r>=2`, is
`-sum_j b_j^r/r`. The target coefficient is
`(-1)^r kappa_(2r)/(2r)!`. Thus the checker's equations

\[
 \sum_jb_j^r=(-1)^{r+1}\frac{r\kappa_{2r}}{(2r)!}
 \qquad(2\le r\le M)
\]

have the correct factorial, sign, and variance normalization. Constant,
quadratic, and odd coefficients are already exact, so these equations imply
`P-H=O(z^(2M+2))`.

All nodes and the remaining Gaussian parameter are certified positive on
the full cube. The only zeros are the real points `+/-1/sqrt(b_j)`, with
multiplicity. Since `a+sum b_j=1/2`, the elementary product bound gives
`abs(P(z))<=exp(abs(z)^2/2)` on the entire plane. Neither statement requires
a positive inverse Fourier density.

## 4. Full-domain contraction

The active coordinates form a closed rational cube of radius `10^-50`; all
inactive nodes are fixed at their exact rational centers. Interval conversion
enlarges these domains outward. The checker includes all `N` terms in each
power sum and all entries `r*b_j^(r-1)` of the active Jacobian on that entire
cube. No point sampling or statistical error estimate enters acceptance.

The exact rational bounds verify

\[
 \|Rf(x_0)\|_\infty\le\beta,\qquad
 \sup_B\|I-RDf\|_\infty\le L<1,
 \qquad \beta+L\rho<\rho.
\]

These prove that `x-Rf(x)` contracts and maps the full cube strictly into
itself for the actual enclosed theta target. The same norm bound at the
center makes `R Df(x_0)` invertible, hence the square matrix `R` invertible;
a fixed point therefore solves `f=0`. The claimed uniqueness is correctly
restricted to the active cube with the remaining nodes fixed.

The upward rounded bounds in the proof table agree with the exact receipt.
In particular even the largest contraction upper bound is below `8.859e-35`;
the smallest certified node exceeds `0.0002765`; and every Gaussian parameter
exceeds `0.0531`. These margins are far larger than the rounding enclosure.

## 5. Conditional compactness and what remains open

The final proof strengthens the original sufficient all-order condition:
the sum of nodes need not stay below `1/2`, and `a` may be negative. This
strengthening was reviewed after the finite arithmetic had been frozen.
For every complex `w`, the elementary inequality
`log(1-2 Re(w)+abs(w)^2)<=-2 Re(w)+abs(w)^2` gives
`abs((1-w)exp(w))<=exp(abs(w)^2/2)`; at `w=1` the conclusion is immediate.
Rewriting the products as

\[
 P(z)=e^{-z^2/2}\prod_j[(1-b_jz^2)e^{b_jz^2}]
\]

and using `sum b_j^2=Q_2` gives the common bound
`exp(abs(z)^2/2+Q_2*abs(z)^4/2)` without a Gaussian-reserve restriction.

If such functions exist at unbounded matched orders, this common quartic
envelope yields a normal family on every complex compact set. Any
subsequential limit has every Taylor coefficient of `H`, hence equals `H`.
Choosing an increasing sequence of matched orders therefore gives local
uniform convergence of the whole sequence. Hurwitz on the two open
half-planes then forces every zero of `H` to be real. Its limit cannot vanish
identically because `H(0)=1`.

This conditional proof is complete. It supplies no construction at orders
beyond those certified. A positive measure with fractional node weights
does not automatically produce entire products. The separate final note
`WEIGHTED_CANONICAL.md` correctly avoids needing that conclusion and further
removes integer multiplicity from a sufficient all-order criterion:

- For `b>0`, the principal `Log(1-b*z^2)` is holomorphic in the open upper
  half-plane and real at `z=it`, `t>0`. Each fractional canonical product
  therefore is holomorphic and nonvanishing on that common open domain.
- The same canonical-factor bound, multiplied by positive weights, gives
  the common quartic envelope from `sum lambda_j*b_j^2=Q_2`.
- The global real-variable logarithm remainder, bounded by `x^M/M` for
  every `x>=0`, proves convergence on a small positive imaginary interval.
  Its sum is paid by the matched moment `Q_M`, and Cauchy's bound for the
  target logarithm makes it tend to zero. This is valid even without a
  common node-support bound or a common disk about zero for the products.
- Montel, identity, and Hurwitz then apply in the open upper half-plane;
  the real coefficients supply the lower half-plane as well.

The branch points lie on the real boundary, so they obstruct neither this
normal-family argument nor zero exclusion in its open domain. This review
checked the global remainder's sign, its use of the last matched power, and
the target Cauchy radius. No truncated positive-moment converse is assumed;
the displayed Hankel tests are only stated as necessary conditions.

Thus the Gaussian reserve is needed only for the sharper quadratic envelope
of the three finite models, and unit multiplicity is needed only for their
whole-plane polynomial representation. No inference
from numerical zeta-zero seeds is used by the checker or needed by the
finite existence proof.

## 6. Replay and immutable evidence

The accompanying `theta_gaussian_audit.json` binds the reviewed source,
parameters, proof, checker, and receipt by SHA-256 and records byte-for-byte
agreement of the final complete-source and optimized replays with the
canonical receipt. The commands were:

```bash
python theta/check_gaussian.py --rebuild-source \
  --source /path/to/pinned/theta \
  --output audit/theta_gaussian_final_replay.json
python -O theta/check_gaussian.py \
  --source /path/to/pinned/theta \
  --output audit/theta_gaussian_optimized_replay.json
```

The first run rebuilds the source from its density rather than merely
accepting the source digest. The optimized run confirms that disabling
Python assertions does not disable acceptance guards. The earlier replay
`theta_gaussian_replay.json` predated a source producer default-path edit;
its mathematical fields agree with the final receipt, and only its producer
hash differs. The final replay removes that provenance ambiguity.
