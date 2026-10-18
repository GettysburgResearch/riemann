# Strip-confined approximation: one exponential moment restores compactness

Status: **PROPOSED native analytic lemmas and exploratory finite computations.**
Independent review at a frozen source identity is required. This file alone
claims no finite moment equality, growth-controlled cofinal theta realization,
improved zeta zero-free boundary, or RH proof. PROOF22.md, PROOF24.md and
the degree-26 certificates separately establish finite equalities.
COFINAL_WALL_CONSTRUCTION.md constructs exact cofinal moment matches in the
correlated-field class, and proves that their exterior growth budget fails.

Scope: symmetric bounded-support probability laws, their entire Fourier
transforms, controlled-strip products, and finite original-theta moments.
The bounded supports may grow without bound along a sequence.

Exact sources: #994 at `c93ca65a510b6acaf167f929b9bf7e67d742b05a`
(theta source and degree-20 model), #981 at
`cf41f3f94a0f1df2bb503d22ab384bfc69288f33` (cofinal real-zero consumer).
Imported classical inputs: Hadamard factorization for exponential-type entire
functions, Montel's theorem, Hurwitz's theorem, and the theta Fourier identity.
The new strip argument was co-derived within this three-direction sprint;
it is not presented as an independently refereed result or a priority claim.

Repository overlap discovered during the sprint: #1001 at
`f6beb3774ae7ff5eca4cb046786eae10e4f88abc` already supplies the
correlated real-field ferromagnetic class, its strip theorem and a uniform
zero-field-variance consumer. #1002 at
`1319373815ee408146705b25a426fba6b22ed755` already supplies the rare-jump
warning, the bounded-jump variance estimate below and a one-budget transfer
for arbitrary entire characteristic functions with budget height above 1/2
in the actual Xi variable. These are credited as overlapping prior repository
work. ONE_POINT_ENTIRE.md proves the stronger height threshold `R>delta`
for whole-plane normality of bounded-support strip-confined models.

Smallest remaining RH-facing gap: construct a cofinal sequence whose every
fixed theta moment converges, whose Fourier zeros stay in the desired fixed
strip, and whose one specified exponential moment stays uniformly bounded.

## 1. The one-point normality lemma

Let `delta>=0`, choose `y>sqrt(2)*delta`, and let `M>=1`.
Let `X` be any symmetric bounded-support real random variable. Set

\[
 f(z)=\mathbb E e^{izX}.
\]

Assume every zero of `f` lies in `|Im z|<=delta` and `f(iy)<=M`.
For `delta>0` define

\[
 c=y^2\min\{2,y^2/\delta^2-2\}>0,
 \tag{1}
\]

and for `delta=0` set `c=2y^2`. Then, for every complex `z`,

\[
 \boxed{|f(z)|\le \exp\!\left(\frac{M^2-1}{c}|z|^2\right).}
 \tag{2}
\]

The estimate is uniform over the support diameter, number of atoms, and
number/multiplicity of zeros. Only the stated strip and **one** exponential
moment are required. This is a sufficient bound, not an optimal constant.

### Proof

Symmetry gives `f(-z)=f(z)`, `f(0)=1`, and `f` is real on the real axis.
Bounded support makes `f` entire of exponential type. Its zeros occur in
opposite pairs and conjugate pairs. There is no zero at zero. There is also no
purely imaginary zero, since `f(it)=E cosh(tX)>0` for real `t`.

Select one zero `lambda` from each opposite pair, with `Re lambda>0`, retaining
multiplicity. Hadamard factorization paired in opposite pairs gives

\[
 f(z)=\prod_\lambda (1-z^2/\lambda^2),\qquad
 \sum_\lambda |\lambda|^{-2}<\infty.
 \tag{3}
\]

The exponential factor in a genus-one exponential-type factorization has
degree at most one. Pairing opposite zeros cancels their genus-one linear
factors; evenness removes the remaining linear exponential factor, while
`f(0)=1` fixes its constant. In particular there is no hidden quadratic
exponential factor. Formula (3) includes a finite or empty zero set.

Put `r=|lambda|` and `u=|Im lambda|<=delta`. At the one imaginary point,

\[
 q_\lambda:=|1+y^2/\lambda^2|^2
 =1+\frac{y^2(2r^2+y^2-4u^2)}{r^4}.
 \tag{4}
\]

If `delta=0`, (4) gives `q_lambda-1>=2y^2/r^2`.
If `delta>0` and `r^2<=delta^2`, then `u^2<=r^2` and

\[
 2+(y^2-4u^2)/r^2\ge y^2/r^2-2
 \ge y^2/\delta^2-2.
\]

If instead `r^2>=delta^2`, then `u^2<=delta^2` and

\[
 2+(y^2-4u^2)/r^2
 \ge 2+(y^2-4\delta^2)/r^2
 \ge \min\{2,y^2/\delta^2-2\}.
\]

Thus in every case

\[
 q_\lambda\ge1+c/r^2>1.
 \tag{5}
\]

Absolute convergence of the paired product and positivity of `f(iy)` give

\[
 \prod_\lambda q_\lambda=f(iy)^2\le M^2.
\]

For every finite subset of the zeros, positivity gives
`1+sum(q_lambda-1)<=product q_lambda<=M^2`.
Increasing the finite subsets and applying (5),

\[
 c\sum_\lambda |\lambda|^{-2}
 \le\sum_\lambda(q_\lambda-1)\le M^2-1.
 \tag{6}
\]

Finally apply `|1-z^2/lambda^2|<=1+|z|^2/r^2<=exp(|z|^2/r^2)`
to (3) and use (6). This proves (2).
If `M=1`, the same argument forces an empty zero set and `f=1`;
equivalently `E cosh(yX)=1` forces `X=0` almost surely. This also covers the
degree-zero law and proves the claimed edge case. QED.

## 2. Cofinal moment matching in a strip

Let `mu` be an even probability law with an entire characteristic function
`F`, normalized by `F(0)=1`. Suppose symmetric bounded-support laws `X_j`
satisfy the following three conditions:

1. Every zero of `f_j(z)=E exp(izX_j)` lies in `|Im z|<=delta`.
2. For one fixed `y>sqrt(2)*delta`, `sup_j E cosh(yX_j)<=M<infinity`.
3. For every fixed nonnegative integer `r`, `E X_j^r` tends to the `r`th
   moment of `mu`.

Then `f_j` tends locally uniformly on the entire plane to `F`, and every
zero of `F` lies in the same closed strip.

Indeed (2) is a common entire bound, so Montel gives local-uniform
subsequential limits. Cauchy's integral formula transfers the derivatives at
zero to every such limit. Condition3 identifies them with all derivatives of
the target entire function, hence the limit equals `F` by its Taylor series.
Every subsequence has that same limit, so the full sequence converges.
Hurwitz applies separately to the connected open regions above and below the
closed strip. The limit is not identically zero on either region because it
is an entire function with `F(0)=1`. This proves the zero confinement.

Exact matching through an unbounded sequence of orders implies condition3.
No nesting of supports/models, common number of components, or growing-order
Jacobian estimate is needed **for this analytic consumer**. Those facts do
not construct the required models.

### Original-theta normalization

For #994's original unstandardized theta variable `T`,

\[
 \mathbb E e^{izT}=\xi(1/2+iz)/\xi(1/2),\qquad
 v=\mathbb ET^2=0.04620998623\ldots.
\]

A strip `|Im z|<=1/3` for this Fourier transform would imply
`1/6<=Re rho<=5/6` for the nontrivial zeta zeros. For the standardized
variable `Y=T/sqrt(v)`, the corresponding strip is

\[
 \delta_Y=\sqrt v/3\simeq0.07166,
 \tag{7}
\]

because its Fourier transform is `F(z/sqrt(v))`. A band imposed on the
standardized models must be scaled by (7); using width1/3 there would give a
different, much weaker conclusion.

For unstandardized models one may choose `y=1`, since `1>sqrt(2)/3`.
Thus the new sufficient premise can use just a uniform bound on `E cosh X_j`
alongside cofinal moment convergence and the prescribed zero band. The actual
theta source has all exponential moments, but this does not automatically
give the same uniform estimate for arbitrary moment-matching approximants.

## 3. Why fixed moments alone do not replace condition2

Fix `delta>0` and let `w_j` tend to infinity. Define

\[
 a_j=\cosh(\delta w_j),\qquad
 f_j(z)=\frac{a_j+\cos(w_jz)}{a_j+1}.
 \tag{8}
\]

This is the Fourier transform of the symmetric three-point law with mass
`a_j/(a_j+1)` at0 and mass `1/[2(a_j+1)]` at each of `+-w_j`.
Its zeros are exactly

\[
 z=((2k+1)\pi\pm i\operatorname{arcosh}a_j)/w_j,
\]

so every zero lies on `|Im z|=delta`. Every fixed positive even moment is
`w_j^(2r)/(a_j+1)`, which tends to zero; all odd moments vanish. Also
`|f_j(x)-1|<=2/(a_j+1)` on the entire real axis. Nevertheless, for every
`y>delta`, `f_j(iy)` tends to infinity like
`exp((y-delta)w_j)`.

Thus even convergence of all fixed moments, a fixed zero band, and uniform
real-axis convergence do not imply local-uniform entire convergence.
The failure is an explicit rare-jump mechanism, rather than a numerical
failure to locate zeros. It violates condition2 of the cofinal consumer.

## 4. A directly checkable product subclass

Suppose `X=sum_i Z_i` is any finite sum of independent symmetric variables,
each supported in `[-W,W]`, where `W>0` is fixed. Write
`V=sum_i E Z_i^2`. Then

\[
 \mathbb E\cosh(yX)
 \le\exp\!\left[\frac{V}{W^2}(\cosh(Wy)-1)\right].
 \tag{9}
\]

For every component and integer `r>=1`,
`E Z_i^(2r)<=W^(2r-2) E Z_i^2`. Expand its nonnegative cosh series to obtain
`E cosh(yZ_i)<=1+(E Z_i^2)(cosh(Wy)-1)/W^2`.
Independence multiplies these generating functions; use `1+x<=exp x`.
This proves (9), including repeated components and atoms at zero.

Consequently a common individual-component support bound and total variance
bound supply condition2. The total support may grow with the number of
components. This covers finite products of the three-point factors (8),
real-zero factors, and mixtures of these types **by independent convolution**,
provided their individual Fourier zero strips are known and their moment
constraints are actually satisfied. It does not cover arbitrary convex
mixtures merely because their summands have the desired zeros.

Further finite constructions and executed controls are recorded in NOTES.md.

## 5. A zero gap makes bounded variance sufficient again

Suppose the hypotheses on `f` in Section1 hold except for the one-point
moment bound. Assume instead `Var(X)<=V`, and every zero `lambda=x+iu`
satisfies

\[
 |x|\ge a>\delta\ge|u|.
\]

Let `kappa=(a^2-delta^2)/(a^2+delta^2)>0`. Then

\[
 \boxed{|f(z)|\le\exp\left(\frac{V}{2\kappa}|z|^2\right).}
 \tag{10}
\]

In fact the paired factorization (3) and differentiation at zero give
`Var(X)/2=sum_lambda Re(lambda^-2)`. For every selected opposite pair,

\[
 \Re(\lambda^{-2})
 =\frac{x^2-u^2}{x^2+u^2}|\lambda|^{-2}
 \ge\kappa|\lambda|^{-2}.
\]

All sums converge absolutely; combine this identity with the same product
bound as before to prove (10). A radial alternative is the assumption
`|lambda|>=R>sqrt(2)*delta`, with
`kappa=1-2delta^2/R^2`, proved in exactly the same way.

Thus a fixed variance and a checkable uniform zero gap provide another
automatic compactness consumer. This excludes the rare-jump example (8),
whose zeros approach the imaginary lines at real parts tending to0.
One must actually prove the zero gap for the chosen model class.

### Bounded three-point factors

For `(a_0+cos(wz))/(a_0+1)` with `a_0>1`, the real parts of all zeros have
absolute value at least `pi/w`. Therefore finite independent products with
all `w<=W` and strip width at most `delta<pi/W` satisfy (10) with
`a=pi/W`. Multiplying by real-zero bounded-support factors preserves this
conclusion if their first real zeros have a common lower bound at least `a`.

## 6. Opposite exponential tilts enlarge the controlled-strip architecture

Let `U` be any symmetric probability law supported in `[-W,W]` with a
real-zero entire characteristic function `phi`. For real `h>=0`, let `U_+`
and `U_-` be independent exponential tilts with densities relative to `U`

\[
 d\mu_\pm(x)=\frac{e^{\pm hx}}{\phi(ih)}d\mu(x).
\]

Their sum `Z_h=U_++U_-` is symmetric and has characteristic function

\[
 g_h(z)=\frac{\phi(z+ih)\phi(z-ih)}{\phi(ih)^2}.
 \tag{11}
\]

Both tilted laws are honest positive probability measures, since
`phi(ih)=E cosh(hU)>0`. Reflection interchanges them. Formula (11) follows
by independence and shows that its zeros are exactly the original real
zeros shifted onto the lines `Im z=+-h`, with multiplicity. No zero is
lost in the strictly positive normalization. This works for correlated
finite ferromagnetic base blocks, not only independent signs.

For real `x` with `|x|<pi/(2W)`, the integrand `cos(xU)` is strictly positive,
so `phi(x)>0`. Thus every zero of the base `phi` has absolute value at least
`pi/(2W)`, and every zero of `g_h` has real part of absolute value at least
that same number. Finite independent products of such paired blocks with
`h<=delta<pi/(2W)` satisfy the automatic variance bound (10), with
`a=pi/(2W)` and with the actual total variance of the product law.
The number of blocks and total support may be unbounded.

For a fair sign of amplitude `w/2`, (11) reduces exactly to

\[
 g_h(z)=\frac{\cosh(hw)+\cos(wz)}{\cosh(hw)+1}.
\]

Hence the three-point model is the simplest case of a larger positive-law
construction with an explicit global zero band and automatic compactness
under the stated support and variance constraints. At `h=0` the law is
precisely two independent copies of the base block, providing an exact
boundary chart whenever two identical blocks are present in an old model.

This construction gives a legal new model architecture. It does not prove
that the original theta moments admit cofinal realizations in it.
