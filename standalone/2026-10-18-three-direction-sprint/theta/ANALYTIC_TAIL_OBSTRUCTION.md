# Analytic weight perturbations and bounded-complexity heads do not remove the fingerprint

**Status: PROPOSED analytic extension requiring independent review.**
HARMONIC_LATTICE_OBSTRUCTION.md was independently reconstructed within
the sprint at actual file-byte SHA256
`d508313ca0cc475ee08800a8b1bf9c8f0e28089677c6407b7e9cab33e807bcd4`.
The extension below preserves that file unchanged. It excludes a broader
regular-tail class; it does not construct actual theta approximants or
prove an improved zero-free region.

## 1. The broader tail and the nonzero phase multiplier

Let the star's tail weights be

\[
 w_n=W(1/(n+a)),\qquad
 W(u)=\tfrac12u+c u^2+O(u^3),\quad a>0, \tag{1}
\]

where W is holomorphic near zero with real Taylor coefficients.
Let tail couplings be J(w_n), with J also holomorphic near zero,
J(0)=0, real on the positive axis. All sufficiently late w_n are
positive. A fixed finite number of exceptional leaves may have arbitrary
positive observed weights and arbitrary finite **real** couplings to the
hub. The hub has a fixed nonnegative observed weight B.

Then the star cannot have the actual original theta distribution.
For a Lee--Yang application the eventual couplings can be required
nonnegative, and finite negative edges can be charged by the root
signed-edge band budget. The obstruction itself does not require the
finite head couplings to be positive.

The conditional second-derivative summand is now

\[
 F_t(x)=W(1/x)^2\operatorname{sech}^2[tW(1/x)+J(W(1/x))]. \tag{2}
\]

Choose the tail endpoint A=a+N sufficiently large for every displayed
analytic function on |x|>=A in the quarter sector. The same contour
argument gives

\[
\begin{split}
 \sum F_t(n+a)-\int_A^\infty F_t(x)dx
 ={}&C_*t^{-3/4}e^{-2\sqrt{\pi t}}\\
 &\cdot\left\{\cos\left(2\sqrt{\pi t}-\frac\pi8-2\pi a+4\pi c\right)
                                  +O(t^{-1/2})\right\}. \tag{3}
\end{split}
\]

The constant C_* is the same positive2sqrt(pi)(2pi)^(1/4). Thus no
analytic coefficient c can annihilate the leading amplitude.

To check this, rescale the m=k=1 Fourier integral by x=sqrt(t)y.
Its exponent and amplitude are

\[
 -2tW(1/x)+2\pi ix
 =\sqrt t[-1/y+2\pi iy]-2c/y^2+O(t^{-1/2}), \tag{4}
\]
\[
 4W(1/x)^2=x^{-2}[1+O(t^{-1/2})].
\]

The saddle is `y_s=e^(i pi/4)/sqrt(2pi)`. The extra analytic amplitude
at that saddle is exactly

\[
 \boxed{\exp[-2c/y_s^2]=\exp(4\pi i c)\ne0.} \tag{5}
\]

The local analytic saddle expansion has large parameter sqrt(t).
After a Gaussian rescaling, its first odd term integrates to zero;
the remaining relative correction is O(t^(-1/2)). Analytic Cauchy
bounds on a fixed saddle neighborhood control the remainder, while
the complementary ray has strictly smaller real exponent. This is the
same complex-Laplace estimate used for the K1 leading integral in the
frozen proof, now with the analytic nonvanishing amplitude exp(-2c/y^2).

The shift sanity check is exact: W(u)=u/[2(1+d u)] has c=-d/2, and
(3) becomes the frozen phase with a replaced by a+d, as its weights
require.

## 2. Uniform control of the remaining contours and Fourier terms

On the tail sector W(1/x)=1/(2x)+O(1/x^2), so choose A large enough
that Re W(1/x)>0. Since J(w)=O(w), tW+J has positive real part for
large t; the contour remains free of sech poles. On the fixed-radius
connecting arc every term is O(poly(t)exp(-c_0t)). The real endpoint's
1/k boundary term is pure imaginary after its Poisson phase; the
remaining arc error sums by the same1/k^2 argument as in the frozen proof.

For general m,k the large-ray exponent is
`-2mtW(1/x)+2pi ikx`. The quadratic W coefficient has purely imaginary
effect along x=e^(i pi/4)r; more generally choose A so large that the
absolute contribution of higher W coefficients is less than epsilon
times mt/|x|, with fixed epsilon small enough that
`sqrt(2(1-epsilon))>1`. The absolute integral is then bounded by a
polynomial times exp(-2sqrt((1-epsilon)pi mk t)). Hence mk>=2
still decays strictly faster than the main exp(-2sqrt(pi t)) term.
The expansion and absolute m,k summation use exactly the estimates in
sections3--4 of the frozen proof. Neither a fixed head nor a regular
quadratic correction can cancel the main m=k=1 saddle.

## 3. The continuum still has a genuine Gevrey1 expansion

The local analytic inverse of W gives

\[
 x(w)=\frac1{2w}+2c+O(w),\qquad
 D(w):=w^2[-x'(w)]=\tfrac12+O(w^2), \tag{6}
\]

with D holomorphic at zero. Therefore the continuum integral is

\[
 I(t)=\int_0^{w_A}D(w)\operatorname{sech}^2[tw+J(w)]dw
 =\frac1t\int_0^{tw_A}D(u/t)
                      \operatorname{sech}^2[u+J(u/t)]du. \tag{7}
\]

For a small fixed complex disk |w|<=r, the product
`D(w)sech^2[u+J(w)]` is bounded by C exp(-2u) uniformly in realu>=0.
The Cauchy remainder and full u integration give
`C A_0^q q! t^(-q-1)` through q<=delta t, plus exp(-c_0t), just as in
the frozen proof. Optimal truncation is therefore exponential in t.

There is no linear term in D(w). It follows that the logarithmic
coefficients of the two conditional log MGFs are still +/-h/2,
where h=J'(0). Thus when B=0 the smooth-profile fractional obstruction
still forces |h|=7/2 (h=7/2 for eventually nonnegative couplings) and
then a nonzero positive t^(-7/2) correction, after interchanging the
two hub branches if necessary.
When B>0 the other branch is exponentially small. The actual xi
second derivative has the explicit Gevrey1 Laplace kernel in the frozen
proof. Equality would force common coefficients, then an exp(-ct)
continuum difference, contradicting (3) along a cosine-maximizing sequence.

An arbitrary fixed finite real-coupling head changes only the leading
linear terms, constants and exponential-in-t corrections: each finite
conditional factor has a positive coefficient at its largest fixed
observable value. Its first two logarithmic derivatives beyond the
linear term decay exponentially. In particular fixed weak negative
head couplings do not remove this obstruction.

## 4. A cofinal consequence under uniform analytic regularity

The obstruction concerns a full limiting function, not merely one
formula with fixed parameters. It also excludes the following cofinal
scheme. Let finite stars use the first N tail leaves, with N tending to
infinity, and suppose:

- a_N remains in a compact subinterval of(0,infinity);
- W_N,J_N are holomorphic and uniformly bounded on common complex disks,
  W_N(0)=J_N(0)=0 and W_N'(0)=1/2;
- the hub weights and a fixed number of head weights/couplings lie in
  compact ranges, with observed head weights positive in the limit;
- every early tail index whose argument or image is outside the common
  disks is included in that compact head. Equivalently, require a fixed
  tail starting index L_0 beyond which all arguments and images lie in
  the common disks, and require compact coordinate control for every
  index below L_0. Local holomorphic bounds alone do not control such
  early evaluations.

Montel and a diagonal subsequence give analytic limits W,J and convergent
head/hub parameters. To spell out the domain condition, let the common
W disk have radius R_u and the J disk radius R_w. Uniform Cauchy bounds
and W_N(0)=0 give `|W_N(u)|<=C|u|` on |u|<=R_u/2. The compact lower
bound a_N>=a_min>0 permits one fixed L_0 such that
`1/(L_0+a_min)<=min(R_u/2,R_w/(2C))`. All later W arguments and their
J images then lie uniformly inside the required disks. The preceding
compact-head premise explicitly controls the finitely many excluded
indices; it is not deduced from the local disk bounds.
Uniform tail estimates give
`sum_(n>L)w_(N,n)^2=O(1/L)` and
`sum_(n>L)|w_(N,n)tanh J_N(w_(N,n))|=O(1/L)`.
Consequently the conditional products converge locally uniformly to
the corresponding infinite regular-tail star; the estimates are uniform
in N and give a common entire MGF bound. If every fixed moment of these
models converged to the actual theta moment, that limiting entire law
would be the actual theta law by the identity theorem, contradicting
sections1--3.

Thus a successful star sequence must leave at least one of these uniform
regularity/compact-head premises, or change the single-hub architecture.
The argument does not exclude growing-head constructions, profiles with
nonanalytic or arithmetic tail structure, noncompact parameter limits,
or hierarchical graphs. No such actual theta construction is supplied
by this obstruction.
