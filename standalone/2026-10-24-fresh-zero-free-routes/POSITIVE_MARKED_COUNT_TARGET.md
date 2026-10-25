# A direct ordinary-zeta target using a positive marked count

Status: proved analytic reduction; the power-error estimate is OPEN.
Scope: the ordinary Riemann zeta function. This route does not use the
OpenAI/Liu family theorem, a sextic large sieve, or a prescribed zero census.
What was actually run: no numerical contour calculation is used in this proof.
Smallest remaining gap: the complete error estimate (10), for one nonzero
smooth weight, with the exact principal term defined below.

The target `b=3/4` would be a substantial new half-plane. It is a target,
not an achieved boundary. Fractional Euler powers, Selberg--Delange main
terms, and monodromy are classical tools; no literature-priority claim is made.
The purpose here is an explicit, source-complete alternative to the recent
inverse-moment optimization, with the known pole at one removed correctly.

## 1. The arithmetic object is a positive count

Fix `1/2<b<1`, put `r=1-b`, and let `W` be a nonzero smooth function with
compact support in `(1,2)`. It may be chosen nonnegative. Define

\[
 A_z(X)=\sum_{n\ge1}\mu^2(n)z^{\omega(n)}W(n/X),
 \qquad
 A_\omega(X)=\sum_{n\ge1}\mu^2(n)\omega(n)W(n/X).
 \tag{1}
\]

For `0<z<1` and nonnegative `W`, every summand is nonnegative. The second
sum counts each squarefree integer with its number of distinct prime factors.
The sums are finite, and `A_omega=partial_z A_z|_(z=1)` exactly.

With `W_hat(s)=integral W(x)x^(s-1) dx`, the initial Dirichlet series are

\[
 F_z(s)=\prod_p(1+zp^{-s})=\zeta(s)^z H_z(s),
 \qquad
 H_z(s)=\prod_p(1+zp^{-s})(1-p^{-s})^z,
 \quad \Re s>1.
 \tag{2}
\]

The logarithm in the second factor is the power-series logarithm, valid
for `Re s>0`. For every compact set of complex `z`, cancellation of the
linear prime terms proves local uniform convergence of `H_z` for `Re s>1/2`.
In particular `H_z(s)` is entire in `z` there. For real `0<z<1` it is
nonvanishing, since both local factors have canonical logarithms and their
logarithms form a normally convergent sum.

At the two integer parameters needed below,

\[
 H_{-1}(s)=1,\qquad H_1(s)=1/\zeta(2s).
 \tag{3}
\]

There is an actual known singularity at `s=1` for a fractional positive
parameter. A bound on `A_z` alone by `X^(b+epsilon)` would be false. The
next section removes this principal contribution without an asymptotic
truncation or any information about high zeros.

## 2. A small zero-free disk and an exact main term

The disk `|s-1|<=1/2` contains no zero of zeta. Here is an elementary
verification that does not import a numerical zero table. For `Re s>0`,
Euler summation gives

\[
 \zeta(s)=\frac1{s-1}+\frac12
       -s\int_1^\infty(\{x\}-1/2)x^{-s-1}\,dx.
 \tag{4}
\]

Thus the holomorphic remainder `h(s)=zeta(s)-1/(s-1)` obeys
`|h(s)|<=1/2+|s|/(2 Re s)`. On the disk of radius `r<=1/2`, geometry gives
`|s|/Re s<=1/sqrt(1-r*r)<=2/sqrt(3)<7/6`. Consequently

\[
 |(s-1)h(s)|\le13/24<1.
 \tag{5}
\]

The removable function `G(s)=(s-1)zeta(s)` is therefore nonzero there,
and has the unique holomorphic logarithm with `log G(1)=0`.

Parametrize the counterclockwise circle by
`w(theta)=1+r exp(i theta)`, `-pi<=theta<=pi`. On this parametrized
circle define the continuous branch

\[
 \ell(w(\theta))=\log G(w(\theta))-\log r-i\theta.
 \tag{6}
\]

This is a logarithm of zeta along the circle. Its values at the two
copies of the leftmost point differ, as they must around the simple pole.
For `X>0`, define the **entire-in-z** principal term

\[
 C_z(X)=\frac1{2\pi i}
   \int_{-\pi}^{\pi}
     e^{z\ell(w(\theta))}H_z(w(\theta))
     \widehat W(w(\theta))X^{w(\theta)}w'(\theta)\,d\theta,
 \qquad
 C_\omega(X)=\left.\partial_z C_z(X)\right|_{z=1}.
 \tag{7}
\]

The radius is fixed before `X` varies. All the values in this integral
have imaginary part at most `r<1/2`; the correction Euler product is
absolutely convergent. In particular the definition does not use the
unknown zeros the proposed estimate is intended to exclude. For real `z`
and real `W`, the conjugate symmetry of the parametrized circle makes
`C_z(X)` real.

At integer parameters the integrand is single-valued, so the residue
theorem gives the exact identities

\[
 C_0(X)=C_{-1}(X)=0,\qquad
 C_1(X)=\frac{X\widehat W(1)}{\zeta(2)}.
 \tag{8}
\]

### An exact real-integral form of the principal term

The circle in (7) can be eliminated from the actual definition needed
for computation. Put, for `0<=t<=r`,

\[
 Q_z(t;X)=G(1-t)^z H_z(1-t)\widehat W(1-t)X^{1-t},
 \tag{8a}
\]

using the real logarithm of `G(1-t)>0` for the power. For real
`0<z<1`,

\[
 C_z(X)=\frac{\sin\pi z}{\pi}
             \int_0^r Q_z(t;X)t^{-z}\,dt.           \tag{8b}
\]

In particular, if `W>=0`, then `C_z(X)>0` for every `X>0` and
`0<z<1`. This positivity is a property of the exactly defined main
term; it does not bound the signed arithmetic remainder.

**Proof of (8b).** Collapse the counterclockwise circle onto the slit
from `1-r` to `1`, using the analytic functions `G`, `H_z`, and
`W_hat` on the known disk. At `w=1-t`, the lower and upper values of
the fractional pole factor are respectively `t^(-z) exp(i pi z)` and
`t^(-z) exp(-i pi z)`. The outer circle equals the lower-minus-upper
jump integral. The small circle about one tends to zero because
`0<z<1`, giving (8b) with the displayed positive sign. Positivity
follows because `G(1-t)>0`, the real Euler factors of `H_z` are
positive, and the Mellin transform of a nonzero nonnegative `W` is
positive on the real axis.

Subtracting the endpoint value gives the useful nonsingular form

\[
 C_z(X)=\frac{\sin\pi z}{\pi(1-z)}
             Q_z(0;X)r^{1-z}
       +\frac{\sin\pi z}{\pi}
          \int_0^r\{Q_z(t;X)-Q_z(0;X)\}t^{-z}\,dt.
 \tag{8c}
\]

The first quotient is removable at `z=1`; the difference inside the
integral is `O(t)` uniformly on compact coefficient-parameter sets.
Thus (8c) is holomorphic for `Re z<2` and agrees there by continuation
with the entire principal term (7). It may be differentiated at one.
Writing `c=widehat W(1)/zeta(2)` and using `h_1` from (15), this gives

\[
 \boxed{\quad
 C_\omega(X)
 =cX\{h_1(1)-\log r\}
       +\int_0^r\frac{cX-Q_1(t;X)}{t}\,dt,
 \qquad
 Q_1(t;X)=
  \frac{G(1-t)\widehat W(1-t)X^{1-t}}{\zeta(2-2t)}.
 \quad}                                             \tag{8d}
\]

The integrand at `t=0` has its removable value `-partial_t Q_1(0;X)`.
To check the derivative signs, `sin(pi z)/[pi(1-z)]` has value one and
derivative zero at `z=1`, while `partial_z[sin(pi z)/pi]` is minus one
there. Also `partial_z Q_z(0;X)|_(z=1)=cX h_1(1)`.
Formula (8d) therefore requires only real zeta values in the explicitly
known range `1-r<=s<=1` (with the removable normalization at one),
absolutely convergent zeta values at `2-2r<=s<=2`, and the absolutely
convergent prime sum `h_1(1)`. No complex contour integration or unknown
zero data is needed to evaluate this exact principal term.

A finite expansion in descending powers of `log X` is not a substitute
for (7). Its omitted terms can be much larger than `X^b` at any fixed
truncation order. The entire principal term is part of the target.

## 3. A single fractional or singly marked estimate excludes every zero

**Theorem 1 (fractional positive count criterion).** Fix an irrational
`z in (0,1)`. If, for every `epsilon>0`,

\[
 |A_z(X)-C_z(X)|\ll_{W,z,b,\epsilon}X^{b+\epsilon}
 \qquad(X\ge1),
 \tag{9}
\]

then `zeta(s)` is zero-free for `Re s>b`.

**Theorem 2 (one prime-factor mark suffices).** If, for every
`epsilon>0`,

\[
 \boxed{
 |A_\omega(X)-C_\omega(X)|
       \ll_{W,b,\epsilon}X^{b+\epsilon}\quad(X\ge1),}
 \tag{10}
\]

then `zeta(s)` is zero-free for `Re s>b`. No irrational parameter or
assumption about zero multiplicities is needed in this second criterion.

### Proof, including the principal term and the Mellin smoothing

For `s` outside the closed circle in Section 2, set

\[
 K_z(s)=\frac1{2\pi i}\int_{-\pi}^{\pi}
  \frac{e^{z\ell(w)}H_z(w)\widehat W(w)}{s-w}w'(\theta)d\theta.
 \tag{11}
\]

This is holomorphic in `s` outside that disk and entire in `z`. For
`Re s>1+r`, absolute convergence and (7) give

\[
 \int_1^\infty C_z(X)X^{-s}\frac{dX}{X}=K_z(s).
 \tag{12}
\]

The finite lower-range function
`E_z(s)=integral_0^1 A_z(X)X^(-s)dX/X` is entire in `s,z`: only the
unit term can occur and its support is bounded away from zero. The Mellin
transform of the actual finite arithmetic sum gives initially

\[
 \widehat W(s)F_z(s)
 =E_z(s)+K_z(s)+
    \int_1^\infty(A_z(X)-C_z(X))X^{-s}\frac{dX}{X}.
 \tag{13}
\]

Under (9), the last integral is holomorphic on `Re s>b`, by using a
smaller epsilon on each compact subset. Thus (13) supplies a
single-valued holomorphic continuation of `W_hat F_z` on
`{Re s>b}\setminus{|s-1|<=r}`. That domain is connected to the original
right half-plane. There are no zeros inside or on the removed disk by (5).

If a zero `rho` outside the disk has multiplicity `m>=1`, locally
`zeta(s)=(s-rho)^m g(s)` with `g(rho) != 0`. The nonvanishing `H_z`
and the nonzero local factor `g^z` have no local monodromy. Going once
around `rho` multiplies the germ in (13) by `exp(2 pi i m z) != 1`.
A zero of `W_hat` has an integer order and cannot remove this
monodromy. Since `W` is nonzero, its entire Mellin transform is not
identically zero. This proves Theorem 1.

For Theorem 2 differentiate the initial Dirichlet identity at `z=1`:

\[
 D_\omega(s):=\sum_n\frac{\mu^2(n)\omega(n)}{n^s}
 =\frac{\zeta(s)}{\zeta(2s)}\{\log\zeta(s)+h_1(s)\},
 \tag{14}
\]

where

\[
 h_1(s)=\sum_p\left\{
       \frac{p^{-s}}{1+p^{-s}}+\log(1-p^{-s})\right\}
 \tag{15}
\]

is holomorphic on `Re s>1/2`: again its linear prime terms cancel.
The derivative version of (13), using (10), continues
`W_hat D_omega` single-valuedly on the same domain. At a zero of
multiplicity `m`, continuation once around the zero changes (14) by
`2 pi i m zeta(s)/zeta(2s)`. After multiplication by `W_hat`, this is
still not identically zero in a punctured neighborhood. Indeed
`zeta(2s)` is finite and nonzero there since `Re(2s)>1`. Thus the
logarithmic branch cannot disappear, even if both zeta and the smoothing
vanish at its center. This contradicts the single-valued continuation.
Theorem 2 follows.

The error estimate is not proved by these Mellin manipulations.
They establish its consequence and precisely identify its known main term.

## 4. An actual endpoint and why its derivative is not already controlled

The unmarked endpoint `z=1` is elementary:

\[
 A_1(X)-C_1(X)=O_W(X^{1/2}).
 \tag{16}
\]

Expand `mu^2(n)=sum_(d^2|n) mu(d)`, and use
`sum_m W(m/T)=T integral W+O_W(1)` on each nonempty scale. There are
`O(sqrt X)` possible `d`. Completing `sum mu(d)/d^2` to `1/zeta(2)`
costs another `O(sqrt X)`. This proves (16).

Differentiating a bound valid at a single parameter value does not bound
the derivative there. Equations (14)--(15) show the exact obstruction:
`zeta(s)/zeta(2s)` is holomorphic at a zero, whereas its marked version
contains `(s-rho)^m log(s-rho)`. It vanishes at the zero but is not
holomorphic through it. A small coefficient perturbation does not imply
a small change in the power of `X` in an error term.

For `b=3/4`, (10) asks for a full `X^(3/4+epsilon)` error in a positive
marked squarefree count. The familiar unmarked error (16) is an available
anchor; the singly marked error is the new, unresolved analytic task.
This formulation bypasses the inherited `13/15` floor of the particular
theta direct estimate. It does so by changing the arithmetic observable
and its analytic continuation, not by claiming that the old estimates
have crossed that floor.

## 5. Coefficient interpolation survives the exact principal subtraction

The continuum-transfer theorem in `arithmetic/COEFFICIENT_CONTINUATION.md`
can also be applied after (7), although `C_z(X)` is not a polynomial.
Here are the details needed to avoid treating it as one.

On the fixed circle, the elementary inequality
`|1+v|<=exp(Re v+|v|^2/2)` and the cancellation in (2) give

\[
 |C_z(X)|\le C_{b,W}X^{1+r}
       \exp(C_b(|z|^2+|z|)),\qquad X\ge1.
 \tag{17}
\]

The prime sum controlling this bound is `sum p^(-2b)<infinity`.
For any fixed compact disk of coefficient parameters, truncate the Taylor
series of `C_z(X)` at zero to degree

\[
 N_X=\left\lceil6\log X/\log\log X\right\rceil
 \quad(X\text{ sufficiently large}).
 \tag{18}
\]

Cauchy's estimate on a coefficient circle of radius proportional to
`sqrt(N_X)` bounds the uniform tail by
`C X^(1+r) exp(-N_X log(N_X)/2+O(N_X))=X^(-3/2+o(1))` or better,
since `r<1/2`. In particular it is `O(X^(b+epsilon))` for every
epsilon. Bounded `X` is absorbed into the constant.

The finite sum `A_z(X)` itself has degree
`O(log X/loglog X)` because its support is squarefree. Hence
`A_z(X)-Taylor_(N_X) C_z(X)` has that same sublogarithmic degree.
Pointwise bounds (9) on a fixed positive-measure set of real coefficient
parameters therefore transfer, with only `X^epsilon` loss, to `z=-1`.
By (8) the exact principal term is zero there, so one obtains an actual
smoothed Mobius estimate of order `X^(b+epsilon)`.

This last statement is another conditional adapter, not a substitute for
(9). A single irrational parameter already gives the zero-free conclusion
by Theorem 1. The interpolation argument additionally transfers the
arithmetic estimate itself and explains why the exact principal
subtraction is compatible with the new coefficient method.

## 6. First failed attempt to prove the marked estimate

The identity `mu^2(n)omega(n)=sum_(p|n) mu^2(n)` gives

\[
 A_\omega(X)=\sum_p\sum_{\substack{m\ {\rm squarefree}\\p\nmid m}}
                    W(pm/X).
 \tag{19}
\]

Separate primes at `sqrt X`, retaining the coprimality condition. On the
small-prime side the needed uniform formula is

\[
 \sum_{\substack{m\ {\rm squarefree}\\p\nmid m}}W(m/Y)
 =\frac{Y\widehat W(1)}{\zeta(2)(1+1/p)}+O_W(\sqrt Y),
 \qquad Y\ge1.                                     \tag{19a}
\]

To check uniformity in `p`, expand `mu^2(m)` and keep `p` out of both
the square divisor and the residual integer. The latter sum is
`T(1-1/p) integral W+O_W(1)`, by subtracting the multiples of `p`
from the full integer sum. Completing the square-divisor series gives
`(1-1/p)/[zeta(2)(1-p^(-2))]=1/[zeta(2)(1+1/p)]`; its tail and the
sum of elementary errors are `O_W(sqrt Y)` with a constant independent
of `p`.

Consequently the small-prime squarefree counting error, estimated independently,
is at most a constant times
`sqrt X sum_(p<=sqrt X) p^(-1/2)`, hence `O(X^(3/4))` by elementary
prime counting (even the integer upper bound suffices at this scale).
On the large-prime side, the remaining squarefree index is `O(sqrt X)`.
An inherited prime-counting error `O(Y^(beta+epsilon))`, used separately
for each such index, costs

\[
 X^{\beta+\epsilon}\sum_{m\ll\sqrt X}m^{-\beta}
       \ll X^{(1+\beta)/2+\epsilon}.
 \tag{20}
\]

For the current source-qualified beta near 0.8749 this exponent is near
0.9374, so that direct separate-bound argument does not reach (10).
Equation (20) is a bound for that proposed method, not a lower bound on
the actual error. More precisely, (19a) and the prime-counting
replacement produce their own hybrid main expression. An estimate for
its difference from the exact `C_omega(X)` has not been proved here;
these separate error calculations must not be described as an already
assembled estimate for (10). The large-prime side still retains
`p not dividing m`; in this range removing the excluded diagonal
prime squares, if desired, costs only `O_W(sqrt X)`.

A successful proof must retain cancellation between
the complete prime/squarefree convolution and the exact principal term;
neither prime density nor the unmarked endpoint alone supplies it.

## 7. Research decision

The direct marked-count route is the most distinct arithmetic target in
this packet: one positive weight, one fixed smooth test, one explicitly
defined principal term, and one all-length error estimate. It is not
claimed to be easier than proving a new zero-free region, and no generic
Tauberian theorem supplies the requested error. Its value is that it
removes the current field, Gauss-coefficient, projection-complement, and
prime-amplifier bookkeeping from the statement of the decisive task.

The immediately useful work is to study the *signed remainder* in (19),
with (7) retained, rather than improving another unrelated positive norm.
