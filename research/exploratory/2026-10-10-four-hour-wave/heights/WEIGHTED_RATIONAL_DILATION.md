# Weighted rational dilation certifies global order 700000 and square-root tail growth

Status: independently reviewed by the root and operator research agents.
The classical complete xi source and published zero-count estimate remain
explicit inputs. The global conclusion additionally uses the published
verified critical-line census. RH remains unproved.

## 1. Result

Put `H0=3*10^12`. Under the complete-source and count inputs of
[GROWING_TAIL_ORDER.md](GROWING_TAIL_ORDER.md), every complete height-tail
Pick kernel `K_{>T}` is positive definite at every packet of distinct positive
nodes through each even order `n>=256` for which

\[
                  T\ge H_0,\qquad 6n^2\le T. \tag{W1}
\]

Thus the tail order grows as `sqrt(T/6)+O(1)`, improving the preceding cubic
root deduction. This tail conclusion uses no critical-line census. With the
published Platt--Trudgian critical-line census through the conservative
`H0`, the full xi Pick kernel is positive definite through order **700000**
at distinct positive nodes, and positive semidefinite with repetitions.
The largest even order directly allowed at `T=H0` is `707106`; the rounded
headline is deliberately conservative.

The proof replaces narrow annular polynomial frames with a weighted rational
norm on the entire high-height half-axis. It pays endpoint concentration at
cost `n^2/T`, matching the quadratic obstruction in
[RATIONAL_DILATION.md](RATIONAL_DILATION.md). No unsupported restriction of a
full-axis Hardy norm is made.

## 2. A weighted polynomial dilation lemma

Let `n>=256`, `T>=H0`, and let `x_i>0`, `sigma_i in {+1,-1}`. Consider any
proper rational function

\[
 R(b)=\frac{A(b)}{\prod_{i=1}^n(b+i\sigma_i x_i)},\qquad\deg A\le n-1.
\]

The numerator may have complex coefficients. Write `t=T/b` and exactly

\[
 R(T/t)=T^{-1}\frac{tP(t)}{Q(t)},\quad
 Q(t)=\prod_i(1+i\sigma_i\beta_i t),\quad\beta_i=x_i/T,
 \quad\deg P\le n-1.
\]

The logarithmically weighted norm becomes

\[
 B_R:=\int_T^\infty\log b\,|R(b)|^2\,db
       =T^{-1}\int_0^1 W(t)|P(t)|^2\,dt,
 \quad W(t)=\frac{\log(T/t)}{\prod_i(1+\beta_i^2t^2)}. \tag{W2}
\]

This is finite for every proper rational `R`. Since `0<t<=1`,
`W(t)>=W(1)>0`. Let `p_0,...,p_(n-1)` be the degree-ordered orthonormal
polynomial basis for `L2(W dt)`. The endpoint reproducing trace satisfies

\[
 W(1)\sum_{k=0}^{n-1}|p_k(1)|^2\le n^2. \tag{W3}
\]

Indeed the left side is `W(1)` times the squared norm of evaluation at one.
The inequality `W>=W(1)` compares that norm with unweighted polynomial
evaluation on `[0,1]`; shifted Legendre orthogonality gives the latter trace
`sum_(k=0)^(n-1)(2k+1)=n^2`. This argument also applies to complex polynomials.

Let `D=t d/dt`, acting on polynomials of degree at most `n-1`. Its matrix is
triangular in this basis, with diagonal entries `0,1,...,n-1`. Integration
by parts gives the exact identity

\[
 D+D^*=W(1)\,\mathbf e\mathbf e^*
             -M_{1+tW'/W},\qquad e_k=p_k(1). \tag{W4}
\]

The boundary term at zero vanishes since `tW(t)=O(t log(1/t))`.
The multiplier satisfies

\[
 1+tW'/W=1-\sum_i\frac{2\beta_i^2t^2}{1+\beta_i^2t^2}
                          -\frac1{\log(T/t)},
 \quad |1+tW'/W|\le2n+1/28. \tag{W5}
\]

The compressed multiplication operator thus has Frobenius norm at most
`(2n+1/28)sqrt(n)`. The rank-one endpoint matrix has Frobenius norm at most
`n^2`. Triangularity gives

\[
 \|D\|_F^2=
   \frac{\|D+D^*\|_F^2-2\sum_{k=0}^{n-1}k^2}{2},
 \quad
 \|D\|\le\frac{n^2+(2n+1/28)\sqrt n}{\sqrt2}
                    <\frac{13}{16}n^2. \tag{W6}
\]

For the last inequality use `sqrt(n)>=16`, `1/sqrt(2)<5/7`, and the exact
worst-case rational inequality
`(5/7)(1+1/8+1/(28*256*16))<13/16`. Every bound is uniform in the pole scales
and signs. Consequently

\[
       \|D^kP\|_{W}\le n^{2k}\|P\|_{W}\quad(k\ge0). \tag{W7}
\]

Differentiating `tP/Q` gives the additional multiplier `1-tQ'/Q`, whose
modulus on the real interval is at most `n+1`, since each
`|i sigma_i beta_i t/(1+i sigma_i beta_i t)|<=1`.
Combining this with (W6) and `(n+1)/n^2<=257/256^2<3/16` proves

\[
       \boxed{\|bR'\|_{\log b,[T,\infty)}\le n^2\|R\|_{\log b,[T,\infty)}}.
       \tag{W8}
\]

Also (W2)--(W3) give the exact endpoint control

\[
                  \log T\,|R(T)|^2\le\frac{n^2}{T}B_R. \tag{W9}
\]

## 3. Complete source sampling

Import the source-qualified count discrepancy
`|N_+(b)-mathcal M(b)|<(1/4)log b` for `b>=H0`, with the right-continuous
multiplicity count and one-sided endpoint values. The measure `2 dN_+`
is exactly the positive reference weight of the squared-pole source.
For `f=|R|^2`, integration by parts on `(T,infinity)` and (W8)--(W9) give

\[
 \left|2\int_{(T,\infty)}f\,d(N_+-\mathcal M)\right|
 \le\frac12\left(\log T f(T)+
                     \int_T^\infty\log b\,|f'(b)|\,db\right)
 \le\frac32\frac{n^2}{T}B_R. \tag{W10}
\]

The term at infinity vanishes because `R(b)=O(1/b)`. For the integral term
use `|f'|<=2|R R'|`, `1/b<=1/T`, and weighted Cauchy--Schwarz. This calculation
excludes any atom at `T`, as required by `K_{>T}`. It holds for arbitrary
complex numerator `A`, so it will apply to every `D^kP` in (W7).

The main density is `2mathcal M'(b)=(1/pi)log(b/(2pi))`. Elementary
`3<pi<22/7`, `log(2pi)<2`, and `log T>28` imply

\[
 \frac{13}{44}\log b<2\mathcal M'(b)<\frac13\log b.
\]

Thus with `q=n^2/T` and `S(q)=1/3+3q/2`,

\[
 \left(\frac{13}{44}-\frac32q\right)B_R
 <\sum_{b_\alpha>T}w_\alpha|R(b_\alpha)|^2
 \le S(q)B_R. \tag{W11}
\]

The elementary constants can be certified with alternating Machin arctangent
series, as in the replay. The lower strict inequality uses the strict imported
count/main bounds; non-strict upper bounds are sufficient below.

## 4. Variable complex displacements and polynomial sampling

For each source ordinate independently, take any `|a_b|<=A<=1/2` and set
`z=b+i a_b`, `t'=T/z=t/(1+i a_b/b)`. Let `gamma=-log(1+i a_b/b)`, using the
continuous branch at zero. Then exactly

\[
 P(t')=e^{\gamma D}P(t)
       =\sum_{k=0}^\infty\frac{\gamma^k}{k!}D^kP(t),
       \qquad |\gamma|\le2A/T. \tag{W12}
\]

This is a dilation of a fixed-degree polynomial. The coefficient varies with
the source ordinate, which is allowed: apply the norm triangle inequality in
the weighted discrete `ell2` space, then bound each coefficient by its common
supremum. By (W7) and the sampling upper bound in (W11), the norm of this series
is at most `exp(2An^2/T) sqrt(S(q)B_R)` after including the real prefactor
`b^-1/Q(t)`.

Changing that prefactor to the complex one costs at most `exp(4nA/T)`.
In fact

\[
 \left|\frac{b}{z}\frac{Q(t)}{Q(t')}\right|
 =\left|\frac zb\right|^{n-1}
          \prod_i\frac{|b+i\sigma_i x_i|}{|z+i\sigma_i x_i|}
 \le\left(\frac{1+A/T}{1-A/T}\right)^n
 \le e^{4nA/T}. \tag{W13}
\]

The last inequality uses `A/T<=1/2`, `log(1+u)<=u`, and
`-log(1-u)<=2u`. Under `q<=1/6`, `n>=256`, the combined exponent is at most

\[
 (2n^2+4n)A/T\le q(1+2/n)
              \le129/768<1/5.
\]

Hence its exponential is less than `1/(1-1/5)=5/4`. Put `kappa=5/4`.
The same reasoning applied to `D^jP` shows that its sampled complex norm,
with this prefactor, is at most `kappa n^(2j) sqrt(S(q)B_R)`.
No comparison of a variable-height complex shift with a single constant shift
is needed, and no factorial derivative estimate is extrapolated.

## 5. Two complex derivative controls

For `B(t')=1-t'Q'(t')/Q(t')`, the identities

\[
 zR'(z)=-z^{-1}Q(t')^{-1}[DP+B P](t'),
\]

\[
 z^2R''(z)=z^{-1}Q(t')^{-1}
 [D^2P+(2B+1)DP+(B^2+B+DB)P](t') \tag{W14}
\]

follow by differentiating `z^-1 P(T/z)/Q(T/z)`. On every allowed vertical
path, `|i sigma_i x_i/(z+i sigma_i x_i)|<=2`, since each denominator has real
part `b>=T` and differs from its real-axis value by at most `A`.
Also `|z/(z+i sigma_i x_i)|<=2`. Therefore

\[
 |B|\le3n,\qquad |DB|\le4n,\qquad
 |2B+1|\le7n,\qquad |B^2+B+DB|\le13n^2.
\]

Since `|b/z|<=1`, (W12)--(W14) give, in the weighted discrete source norm,

\[
 \|R(z_b)\|_{\rm src}\le\kappa\sqrt{S(q)B_R},\\
 \|bR'(z_b)\|_{\rm src}\le2\kappa n^2\sqrt{S(q)B_R},\\
 \|b^2R''(z_b)\|_{\rm src}\le2\kappa n^4\sqrt{S(q)B_R}. \tag{W15}
\]

Here `n^2+3n<=2n^2` and `n^4+7n^3+13n^2<=2n^4` hold at every `n>=256`.
The argument is uniform in all independently chosen `a_b`, including the
depths `tau a_b` needed in Taylor's integral remainder.

## 6. Applying the estimates to both xi moment blocks

Fix any even `n>=256` distinct positive nodes, put
`q_x(s)=prod_i(x_i^2+s)`, and use the exact node congruence of
[ANNULAR_GLOBAL_PICK.md](ANNULAR_GLOBAL_PICK.md). Each of its two normalized
moment-block quadratic forms has, up to a positive constant, the form

\[
 \sum_{b_\alpha>T}w_\alpha
       \frac{s_\alpha^jP(s_\alpha)^2}{q_x(s_\alpha)},
 \qquad j=0,1,\quad\deg P\le n/2-1.
 \tag{W16}
\]

Here `P` has real coefficients: it is the polynomial of a real quadratic
vector in the real symmetric moment block. Testing these real vectors is
sufficient for positive definiteness of that block.

Set

\[
 R_+(z)=\frac{z^jP(z^2)}{\prod_i(z+i x_i)},\qquad
 R_-(z)=\frac{z^jP(z^2)}{\prod_i(z-i x_i)},\qquad f(z)=R_+(z)R_-(z).
\]

These are proper rational functions of denominator dimension `n`, including
`j=1`. On the real axis `R_-` is the conjugate of `R_+`, so their real-axis
norms are identical, say `B>0`, and `f(b)=|R_+(b)|^2`.
The actual squared pole is `(b+i a)^2`; (W16) is exactly the source sampling
of `f(b+i a)`. The real-height reference is the positive sampling of `f(b)`.

Weighted discrete Cauchy--Schwarz and (W15) give, uniformly in the individual
vertical displacements,

\[
 \sum w_\alpha|f''(b_\alpha+i a_\alpha)|
 \le\frac{12\kappa^2 n^4}{T^2}S(q)B
       =\frac{75}{4}q^2S(q)B. \tag{W17}
\]

For example each `R_+''R_-` term costs at most
`2kappa^2 n^4 S(q)B/T^2`, while `2R_+'R_-'` costs at most
`8kappa^2 n^4 S(q)B/T^2`. The two outer terms and the middle term sum to the
coefficient 12. The factors `b^-2` are bounded by `T^-2` before applying
Cauchy--Schwarz.

Conjugate pole groups cancel the imaginary first Taylor term. Taylor's
integral remainder on the vertical segment thus changes the complete
reference quadratic form by at most

\[
 \frac{A^2}{2}\frac{75}{4}q^2S(q)B
               \le\frac{75}{32}q^2S(q)B. \tag{W18}
\]

Critical pairs have `a=0` and contribute no such error. Multiplicities and
both off-line reflected upper zeros are included by the exact measure
`sum w=2 dN_+`; no finite source truncation is substituted.

Combining (W11) and (W18), every nonzero quadratic form in (W16) is bounded
below by

\[
 \left[\frac{13}{44}-\frac32q-
                 \frac{75}{32}q^2\left(\frac13+\frac32q\right)\right]B
 \ge\frac{379}{50688}B>0\qquad(q\le1/6). \tag{W19}
\]

All coefficients of the subtracted polynomial are positive, so its maximum
on `[0,1/6]` occurs at `1/6`. At that endpoint the count cost is `1/4`, the
strip cost is `175/4608`, and the gap is exactly `379/50688`.

## 7. Complete summation, global consequence, and scope

The complete source and all derivative/remainder sums above converge
absolutely. This follows from proper rational decay and the imported
`N_+(b)=O(b logb)` count; finite lower cutoffs can also be used throughout
before passing to the limit. The exact invertible arbitrary-node congruence
therefore proves positive definiteness of `K_{>T}` whenever (W1) holds.
Principal submatrices cover all smaller orders; repeated nodes follow by
continuity. The maximal allowed even order is
`max{n even:6n^2<=T}=sqrt(T/6)+O(1)`.

At `T=H0`, the published critical-line census makes the entire source below
or at `H0` a nonnegative critical-pair Gram kernel. Adding it to the strictly
positive tail proves the global order statement. The integer inequality
`6*(700000)^2=2940000000000<H0` is exact. A direct largest-even calculation
gives `707106` and `(707108)^2*6>H0`.

The growing tail theorem has no below-`T` census input, and its tail kernels
change with `T`. The global fixed-order result still has a finite verified
height input. Neither conclusion yields all-order positivity for one full
kernel, and RH remains unproved.

## 8. Replay boundary

[verify_weighted_rational.py](verify_weighted_rational.py) checks all uniform
scalar guards, the exact endpoint gap, sample tail orders, Machin bounds for
the elementary pi constants, and independently reconstructs the polynomial
endpoint trace on `[0,1]`. It checks the triangular Frobenius identity on
explicit nonsymmetric matrices rather than relying on optimized-mode
assertions. The analytic integration-by-parts, weighted polynomial norm,
variable-coefficient discrete Minkowski, complete source identities, and
published count/census inputs remain distinct from these finite controls.
