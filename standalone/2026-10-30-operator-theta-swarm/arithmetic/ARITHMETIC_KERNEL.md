# The arithmetic zero kernel: a failed Markov interpolation and an exact repair

Status: proposed component theorems with complete proofs below; independent review requested.
Scope: the actual harmonic-step Nyman–Beurling zero kernel, its high-height limit,
and an exact infinite-divisibility classification of that limit. No RH proof or
new zero-free region is obtained.
What was actually run: the standard-library rational certificate in `verify.py`.
The auxiliary floating experiment, if present, is reconnaissance only.
Smallest remaining RH-bearing gap: a source-faithful upper bound for the actual
Nyman–Beurling approximation error; none of the positive limiting kernels supplies it.

## 1. Outcome and relation to earlier work

The attempted mechanism was to turn the high-height arithmetic zero kernel into
a continuous convolution semigroup, use its positivity at all times, and transport
that positivity back to the native approximation problem. This mechanism fails
in a precise way: its complex phases prevent infinite divisibility. Every real
coefficient test of the logarithmic kernel misses this failure. A three-point
complex coefficient test detects it, and the negative sign can be certified by
integer/rational arithmetic.

There is a sharp positive repair. Adding one particular log-gamma noise law
produces an infinitely divisible distribution. Adding a fraction less than one
does not. The repair's Fourier multiplier decays exponentially, so recovering
the native phase information requires exponential amplification. The repair is
therefore not an RH transfer theorem.

The exact zero functionals and elementary norm bound in Section 2 already occur
in the repository's PR #901, at commit
`93126fa9131ebfa93311c1874eeb4cbd93c97864`, particularly the residual and spectral
synthesis chapters. The classical Hilbert-space criterion is due to
Nyman–Beurling and Báez-Duarte; the step-space formulation is Bagchi's.

During this work an independently derived high-height formula was found to
overlap Scott Schubr's *Collision-uniform kernel asymptotics for Báez–Duarte zero
packets*, edition 4, 30 October 2026. The author's abstract explicitly reports
stronger growing-packet and collision-uniform results. We do not claim novelty
for Sections 2–4; our short proof is retained as a self-contained derivation and
to fix all normalizations used by the new attempt. A later retrieval by the
parent agent obtained the 19-page external manuscript and confirmed the
overlapping kernel, jet and fixed-multiplicity formulas; this is not a full
independent audit of its growing-packet theorem. The targeted search did not locate the
signed Lévy classification in Sections 5–8, but this is not an exhaustive
priority claim.

## 2. The exact arithmetic source and its zero functionals

Let

\[
 H=\ell^2\bigl(\mathbb N,1/[k(k+1)]\bigr),\qquad
 b_n(k)=\{k/n\},\quad n\ge2,
\]

and put

\[
 E_N=\inf_{c_2,\ldots,c_N}
 \left\|1-\sum_{n=2}^Nc_nb_n\right\|_H^2,
 \qquad E_\infty=\lim_NE_N.
\]

The limit exists by monotonicity. The classical strong criterion says
`E_infinity = 0` if and only if RH. We use the criterion only to explain the
remaining problem, not as an unproved input to the calculations below.

For `Re(s)>1/2` define the analytic vector

\[
 q_s(k)=k(k+1)\bigl(k^{-s}-(k+1)^{-s}\bigr).
 \tag{2.1}
\]

The corresponding bounded complex-linear functional is

\[
 L_s(f)=\sum_{k\ge1}f(k)\bigl(k^{-s}-(k+1)^{-s}\bigr).
 \tag{2.2}
\]

With the inner product linear in its first argument, its representer is
`conjugate(q_s)`. The norm is finite because
`q_s(k)=s k^(1-s)(1+O_s(1/k))`; the same conclusion holds after any fixed
number of derivatives in `s`, locally uniformly in this half-plane.

Summation by parts, first for `Re(s)>1`, gives

\[
 L_s(1)=1,\qquad
 L_s(b_n)=\zeta(s)\bigl(n^{-1}-n^{-s}\bigr).
 \tag{2.3}
\]

Indeed, `b_n(k)-b_n(k-1)=1/n-1_(n|k)`. The paired series in (2.2) is absolutely
convergent for bounded `b_n` throughout `Re(s)>0`, so analytic continuation
proves (2.3) there, with the removable value at `s=1` understood.

If `rho` is a zero of multiplicity at least `m`, then for `0<=j<m`

\[
 L_\rho^{(j)}(b_n)=0,\qquad L_\rho^{(j)}(1)=\mathbf1_{j=0}.
 \tag{2.4}
\]

Consequently the complete native approximation error obeys the corresponding
finite Gram lower bounds. This does not require a spectral-synthesis assertion
about the entire orthogonal complement.

The familiar continuous bound is

\[
 \|q_s\|_H^2\le {|s|^2\over2\Re(s)-1}.
 \tag{2.5}
\]

To prove it, write the difference as `s integral_k^(k+1) x^(-s-1) dx` and apply
Cauchy–Schwarz with weights `x^-2` and `x^(-2 Re(s))`; the first weight integrates
to `1/[k(k+1)]`. Sum the resulting inequalities.

## 3. A short high-height derivation

Fix `1/2<sigma<3/2` and put `alpha=3-2 sigma`, so `0<alpha<2`. Define

\[
 C(a)=\frac{\pi}{\Gamma(1+a)\sin(\pi a/2)}
      =2\int_0^\infty(1-\cos u)u^{-1-a}\,du,
 \qquad0<\Re(a)<2.
 \tag{3.1}
\]

For real `a`, the integral identity follows without an oscillatory limiting
argument: insert the Laplace representation of `u^(-1-a)`, use Tonelli, and
evaluate

\[
 \frac{2}{\Gamma(1+a)}\int_0^\infty\frac{t^{a-1}}{1+t^2}\,dt.
\]

The beta integral gives the displayed gamma expression. Holomorphy then extends
the equality to the complex strip.

### Proposition 3.1: complete scalar asymptotic

As `T->infinity`, uniformly for `sigma` in any compact subset of `(1/2,3/2)`,

\[
 \|q_{\sigma+iT}\|_H^2
   = C(\alpha)T^\alpha+O_\sigma(T^{\alpha/2}).
 \tag{3.2}
\]

The constant in the `O` term may depend on the compact set. In the RH strip
`1/2<sigma<1`, this replaces the scale `T^2` in (2.5) by `T^(3-2 sigma)`.

**Proof.** With `r_k=1+1/k`, the summand equals

\[
 k^{\alpha-1}r_k
 (1-r_k^{-\sigma-iT})(1-r_k^{-\sigma+iT}).
\]

Set `Y=sqrt(T)`. For `k<=Y`, both the exact summands and the model summands
`2 k^(alpha-1)(1-cos(T/k))` have total absolute size `O(Y^alpha)`.

For `k>Y`, expand `log(1+1/k)=1/k+O(k^-2)` and
`r_k^(-sigma)=1+O_sigma(k^-1)`. On `Y<k<=T`, the product error is bounded by
`O_sigma(T/k^2)`. On `k>T`, use additionally
`|1-exp(iT/k)|<=T/k`; this gives the same product error. The factor `r_k`
is absorbed by these bounds. Hence the total error is

\[
 O_\sigma\left(T\sum_{k>Y}k^{\alpha-3}\right)
   =O_\sigma(T^{\alpha/2}).
\]

For the model function `f_T(x)=2x^(alpha-1)(1-cos(T/x))`, discard `(0,Y]`
at the same cost. On `[Y,infinity)`, comparison of the sum and integral by
total variation costs at most a constant times
`|f_T(Y)|+integral_Y^infinity |f_T'(x)| dx`. Splitting the derivative integral
at `T`, and using `|sin(T/x)|<=min(1,T/x)` and
`1-cos(T/x)<=min(2,T^2/(2x^2))`, bounds this by `O_sigma(T^(alpha/2))`.
Finally substitute `u=T/x` in the complete integral to obtain `C(alpha)T^alpha`.
All bounds are uniform on the indicated compact sets. ∎

### Proposition 3.2: analytic gauges and centered jets

For `z` in a sufficiently small fixed complex disc, set

\[
 F_T(z)=T^{z-\alpha/2}q_{\sigma+iT+z}.
 \tag{3.3}
\]

For `z,w` in such discs, with `alpha-Re(z)-Re(w)` bounded away from `0` and `2`,

\[
 \langle F_T(z),F_T(w)\rangle_H
  =C(\alpha-z-\overline w)+O(T^{-\eta})
 \tag{3.4}
\]

for some `eta>0`, uniformly on smaller closed discs. Every fixed mixed
derivative has the same conclusion, with possibly a changed constant.

**Proof.** Repeat the preceding summand argument with the complex exponent
`a=alpha-z-conjugate(w)`. The oscillatory increments still have main factors
`1-exp(-iT/k)` and `1-exp(iT/k)`, while the extra bounded exponents produce only
the same `O(1/k)` errors. Before applying the gauge, the error is
`O(T^(Re(a)/2))`. The gauge divides its magnitude by `T^Re(a)`, proving uniform
decay on a compact substrip. The kernel is holomorphic in `z` and antiholomorphic
in `w`; Cauchy's formula on slightly larger discs proves the derivative claims. ∎

In particular, for a fixed integer `m`, the Gram matrix of
`F_T^(j)(0)`, `0<=j<m`, tends to

\[
 M^{(m)}_\alpha(j,l)=(-1)^{j+l}C^{(j+l)}(\alpha).
 \tag{3.5}
\]

This matrix is strictly positive definite: it is the moment Gram of
`1,log u,...,(log u)^(m-1)` for the positive measure

\[
 2(1-\cos u)u^{-1-\alpha}\,du.
 \tag{3.6}
\]

A nonzero polynomial in `log u` cannot vanish almost everywhere against this
measure. The zeros of its density are discrete and do not alter that argument.

## 4. Exact target transport matters

Suppose `rho=sigma+iT` is an actual zero of multiplicity at least `m`. By (2.4),
the centered jet functionals on the residual have the target vector

\[
 T^{-\alpha/2}v_m(\log T),\qquad
 v_m(L)=(1,L,\ldots,L^{m-1})^\mathsf T.
 \tag{4.1}
\]

It is not the vector `(1,0,...,0)` after the gauge. Finite Gram duality and
(3.4) give the following consequence whenever such zeros tend to infinity at
fixed `sigma,m`:

\[
 E_\infty\ge(1+o(1))T^{-\alpha}
 v_m(\log T)^\mathsf T(M^{(m)}_\alpha)^{-1}v_m(\log T).
 \tag{4.2}
\]

The relative error follows from matrix norm convergence and strict positivity
of the fixed limiting matrix, so it is uniform over all target vectors, even
though (4.1) grows with `log T`.

For `m=1`, (4.2) gives `T^(-alpha)/C(alpha)`. For `m=2`, the quadratic is exactly

\[
 \frac1{C(\alpha)}+
 \frac{(L+C'(\alpha)/C(\alpha))^2}
 {C(\alpha)(\log C)''(\alpha)},
\quad
 (\log C)''(\alpha)
  =-\psi_1(1+\alpha)+\frac{\pi^2}{4}\csc^2(\pi\alpha/2)>0.
 \tag{4.3}
\]

The positivity is also the variance of `log u` under (3.6), divided by its
total mass. This is a lower bound conditional on the presence of a zero,
not an upper bound excluding one. No complete spectral synthesis has been used.

## 5. The log-scale law and the proposed semigroup

Normalize (3.6) and put `X=log U`. Its probability density is

\[
 p_\alpha(x)=\frac{2}{C(\alpha)}e^{-\alpha x}(1-\cos(e^x)),
 \qquad x\in\mathbb R.
 \tag{5.1}
\]

It has exponential tails on both sides and moment generating function

\[
 \mathbb E e^{zX}=\frac{C(\alpha-z)}{C(\alpha)},
 \qquad \alpha-2<\Re z<\alpha.
 \tag{5.2}
\]

Its characteristic function
`phi_alpha(t)=C(alpha-it)/C(alpha)` has no real zero. That alone does not
imply infinite divisibility. To create the proposed convolution semigroup,
all continuous powers `phi_alpha(t)^theta`, `theta>0`, would have to be
characteristic functions, using the continuous logarithm equal to zero at
the origin.

### Theorem 5.1: the native law is not infinitely divisible

For every `0<alpha<2`, the law (5.1) is not infinitely divisible. Its continuous
logarithm has the exact signed Lévy representation

\[
 \log\mathbb E e^{zX}
  =m_\alpha z+\int_{\mathbb R}
   (e^{zx}-1-zx)\,\nu_\alpha(dx),
 \tag{5.3}
\]

where `m_alpha=E X=-C'(alpha)/C(alpha)` and the signed density is

\[
 \begin{aligned}
 \nu_\alpha(x)&=\frac{e^{-\alpha x}}x
   -\frac{e^{-(\alpha+1)x}}{x(1-e^{-2x})}
   =\frac{e^{-\alpha x}}x\left(1-\frac1{2\sinh x}\right),
   &&x>0,\\
 \nu_\alpha(-x)&=\frac{e^{-(2-\alpha)x}}{x(1-e^{-2x})},
   &&x>0.
 \end{aligned}
 \tag{5.4}
\]

In particular its positive-jump density is negative precisely on

\[
 0<x<\operatorname{arsinh}(1/2)
   =\log\frac{1+\sqrt5}{2}.
 \tag{5.5}
\]

**Proof.** Reflection and duplication for gamma give

\[
 C(a)=\frac{\sqrt\pi\,2^{1-a}\Gamma(1-a/2)}
 {a\,\Gamma((a+1)/2)}.
 \tag{5.6}
\]

Set `b=1-alpha/2` and `c=(alpha+1)/2`. Equation (5.2) becomes

\[
 \mathbb E e^{zX}
  =2^z\frac{\alpha}{\alpha-z}
    \frac{\Gamma(b+z/2)}{\Gamma(b)}
    \frac{\Gamma(c)}{\Gamma(c-z/2)}.
 \tag{5.7}
\]

The centered log-gamma identity, obtained from its Weierstrass product, is

\[
 \log\Gamma(b+z)-\log\Gamma(b)-z\psi(b)
  =\int_0^\infty(e^{-zx}-1+zx)
       \frac{e^{-bx}}{x(1-e^{-x})}\,dx.
 \tag{5.8}
\]

Apply it to the two gamma factors and use the elementary exponential-law
identity for `alpha/(alpha-z)`. This gives (5.3)–(5.4). The integrals converge
absolutely after the centered subtraction: near zero the signed densities are
`O(x^-2)`, while both tails decay exponentially.

To justify the negative-density obstruction without assuming a uniqueness
claim for a nonpositive Lévy measure, differentiate the logarithmic
characteristic function twice. Its negative second derivative is the Fourier
transform of the finite signed measure `x^2 nu_alpha(dx)`. If the law were
infinitely divisible, its finite second moment would make this same function
the Fourier transform of the nonnegative finite measure
`a delta_0+x^2 nu_ID(dx)`, with `a>=0`. Uniqueness of Fourier transforms of
finite measures forces equality of these measures. This is impossible on the
interval (5.5). Finally (5.5) follows directly from `2 sinh x<1`. ∎

The negative density behaves as `-1/(2x^2)+O(1/x)` as `x` decreases to zero.
Adding a drift or any Gaussian noise cannot repair it. Nor can convolution
with an independent infinitely divisible law of finite variance whose positive
jumps have finite variation: domination of this negative density would require an infinite
integral of `x nu(dx)` near zero. These are consequences of the same finite
measure uniqueness argument, not merely numerical observations.

## 6. Exact threshold for a positive repair

Let `G_c` have gamma density `u^(c-1)e^-u/Gamma(c)` and let

\[
 Y=-\tfrac12\log G_c,\qquad c=(\alpha+1)/2.
\]

Its characteristic function is infinitely divisible by (5.8). Thus it belongs
to a convolution semigroup `Y_theta`, `theta>=0`, with

\[
 \mathbb E e^{zY_\theta}
   =\left(\frac{\Gamma(c-z/2)}{\Gamma(c)}\right)^\theta.
 \tag{6.1}
\]

Take `X` and `Y_theta` independently.

### Theorem 6.1: sharp gamma-noise threshold

The law of `X+Y_theta` is infinitely divisible if and only if `theta>=1`.
At the endpoint,

\[
 X+Y_1\ \overset d=\ \log2+E_\alpha+\tfrac12\log G_b,
 \qquad b=1-\alpha/2,
 \tag{6.2}
\]

where `E_alpha` is an exponential variable of rate `alpha` and the variables
on the right are independent.

**Proof.** Adding `Y_theta` changes (5.4) on the positive half-line to

\[
 \frac{e^{-\alpha x}}x
 +(\theta-1)\frac{e^{-(\alpha+1)x}}{x(1-e^{-2x})}.
 \tag{6.3}
\]

This is nonnegative for `theta>=1`; the negative half-line is unchanged and
positive. Lévy–Khintchine therefore constructs the infinitely divisible law.
For `theta<1`, (6.3) is `(theta-1)/(2x^2)+O(1/x)` near zero, so the preceding
uniqueness argument excludes infinite divisibility. At `theta=1`, cancellation
of the gamma denominator in (5.7) proves (6.2) by equality of moment generating
functions near the origin. ∎

This is a complete classification within a specified positive convolution
family. It supplies no membership or invariance result for the native
Nyman–Beurling closure.

The price of undoing the repair is explicit. Along the Fourier axis,

\[
 \left|\frac{\Gamma(c-it/2)}{\Gamma(c)}\right|
 \sim\frac{\sqrt{2\pi}}{\Gamma(c)}
       (|t|/2)^{c-1/2}e^{-\pi|t|/4}.
 \tag{6.4}
\]

Thus deconvolution multiplies high frequencies by an exponential
`exp(pi |t|/4)` up to a polynomial. Stirling's formula is sufficient here.
Any proposed transfer must explicitly pay that cost and retain the target
vector from Section 4.

## 7. Why real-valued positivity tests look deceptively good

### Theorem 7.1: the symmetrization is infinitely divisible

For an independent copy `X'`, the difference `X-X'` is infinitely divisible for
every `0<alpha<2`. Its Lévy density on each half-line is, for `x>0`,

\[
 \nu_{\mathrm{sym}}(x)
  =\frac1x\left[e^{-\alpha x}+
   \frac{e^{-(2-\alpha)x}-e^{-(\alpha+1)x}}{1-e^{-2x}}\right]>0.
 \tag{7.1}
\]

**Proof.** Add the signed densities at `x` and `-x` in (5.4). After multiplying
by the positive factor `x(1-e^-2x)e^(alpha x)`, the sign is that of

\[
 (1-e^{-x})+(e^{-(2-2\alpha)x}-e^{-2x}),
\]

which is strictly positive because `alpha>0`. The resulting density is a
Lévy measure; its tails decay and it is only `O(1/x)` at the origin after the
leading signed singularities cancel. ∎

Accordingly, `|phi_alpha(t)|^(2 theta)` is positive definite for every
`theta>0`, while the corresponding assertion for the phase-preserving
`phi_alpha(t)^theta` is false. For any finite real coefficient vector with
sum zero, the quadratic form of `log phi_alpha(t_i-t_j)` is nonnegative:
the imaginary antisymmetric part cancels, and the real part is half the
logarithm of the infinitely divisible symmetrization. Complex coefficients
are necessary to detect the obstruction.

At the especially simple native value `alpha=3/2` (`sigma=3/4`),

\[
 |\phi_{3/2}(t)|^2
  =\frac{(3/2)^2}{(3/2)^2+t^2}
    \frac{(1/2)^2}{(1/2)^2+t^2}.
 \tag{7.2}
\]

This is the characteristic function of a sum of two independent centered
Laplace variables. Yet the original, complex-phase law is not infinitely
divisible.

## 8. A finite rationally certified phase obstruction

Take `alpha=3/2`, nodes `t=(0,8,16)`, and

\[
 c=(-1-3i/2,\ 2,\ -1+3i/2),\qquad \sum c_j=0.
 \tag{8.1}
\]

Let `L(t)` be the continuous logarithm of `phi_(3/2)(t)` with `L(0)=0` and
put `A_ij=L(t_i-t_j)`. Infinite divisibility would require
`c^* A c>=0`: differentiate the positive semidefinite matrix
`[exp(theta A_ij)]` at `theta=0` on a sum-zero vector.

In fact this quadratic is negative. Write `L(8)=r_8+i v_8` and
`L(16)=r_16+i v_16`. Direct three-by-three expansion gives

\[
 Q=-8r_8-\tfrac52r_{16}+12v_8-6v_{16}.
 \tag{8.2}
\]

The real parts are elementary:

\[
 r_t=-\tfrac12\log\left((1+(2t/3)^2)(1+4t^2)\right).
\]

Using (5.7), `Gamma(5/4+z)=(1/4+z)Gamma(1/4+z)`, and the centered
Weierstrass product, all linear imaginary terms cancel in (8.2). Therefore

\[
 \begin{aligned}
 Q={}&-8r_8-\tfrac52r_{16}
 +12[\arctan(16/3)+\arctan16]
 -6[\arctan(32/3)+\arctan32]\\
 &+12\sum_{n=0}^\infty
 \left[\arctan\frac8{n+1/4}-2\arctan\frac4{n+1/4}\right].
 \end{aligned}
 \tag{8.3}
\]

Every summand is negative: `atan(2x)-2 atan(x)<0` for `x>0`, as follows
by differentiation from its value zero at zero. Hence truncating after
sixteen terms gives a strict upper bound `Q<Q_16` without estimating the
omitted tail. The accompanying checker uses rational alternating-series
bounds for arctangent, a rational atanh series for logarithms, and Machin's
formula for pi. It verifies

\[
 -1.435<Q_{16}<-1.434,
 \qquad\text{therefore }Q<-1.434<0.
 \tag{8.4}
\]

The infinite sum is approximately `-4.262302575` after the other terms are
included, but that floating value is unnecessary for the proof. The exact
checker authenticates (8.4), not RH, an asymptotic formula, or any imported
paper's theorem.

## 9. What this leaves to attack

1. A phase-preserving convolution-semigroup interpolation of the native
   limiting kernel is ruled out, with a finite witness. Gaussian smoothing
   and finite-variance, finite-variation jump corrections cannot fix it.
2. There is a precisely priced positive completion, and its threshold is
   exact. A successful use of it would need a source-specific deconvolution
   estimate overcoming (6.4); no such estimate is proved.
3. The native finite approximation problem remains available. Its actual
   complex phases and the target transported in (4.1) must be kept. Replacing
   its kernel by the modulus or an infinitely divisible completion changes
   the object whose approximation error is equivalent to RH.

The source-specific remaining inequality is still an unconditional vanishing
upper bound for `E_N`, or another proved arithmetic estimate that implies it.
The present theorems diagnose and repair a proposed mechanism at its exact
scope; they do not claim that repair transfers to the zeta source.

## Sources and inspection boundaries

- B. Bagchi, *On Nyman, Beurling and Báez-Duarte's Hilbert space reformulation
  of the Riemann hypothesis* (2006), https://arxiv.org/abs/math/0607733 .
- L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the
  Riemann hypothesis*, https://arxiv.org/abs/math/0202141 .
- Repository PR #901, frozen at
  https://github.com/GettysburgResearch/riemann/tree/93126fa9131ebfa93311c1874eeb4cbd93c97864/standalone/2026-09-19-zeta-iteration-chat-packet .
  The source's zero-functional and open-synthesis statements were inspected
  through the GitHub connector's full patch.
- Scott Schubr, *Collision-uniform kernel asymptotics for Báez–Duarte zero
  packets*, edition 4, 30 October 2026,
  https://research.luminaryoddities.com/collision-uniform-kernel-asymptotics-baez-duarte-zero-packets/v/4 .
  Initial author-page metadata and abstract established relevant prior-art
  overlap. A later parent-agent retrieval obtained the 19-page manuscript at
  https://research.luminaryoddities.com/collision-uniform-kernel-asymptotics-baez-duarte-zero-packets/v/4/files/Collision_uniform_arithmetic_packets.pdf
  and checked the overlapping kernel, jet and fixed-multiplicity formulas.
  No full independent verification of that paper's growing-packet theorem is claimed.
- bramble_trace, *A logarithmic-prefix Nyman–Beurling criterion and transferred
  zero bounds*, rStation 47/v1,
  https://rstation.ai/problems/riemann_hypothesis/papers/47/v1 .
  The main text and its source qualifications were inspected; its stronger
  logarithmic-prefix theorem is not needed by the proofs here.
- F. Calderaro, J. Manzur, W. Noor, C. Santos, *Orthogonality questions in the
  Hardy space related to zeta-zeros*, https://arxiv.org/html/2203.05030v4 .
  This supplies related operator context, not an imported missing invariance.
- J. Manzur and W. Noor, *A Hardy-space operator acting on zeta-zeros*,
  https://arxiv.org/abs/2610.03568 . Only the abstract was accessible; no
  theorem about its exact operator is asserted or used here.

Gamma reflection/duplication, the beta integral, Stirling asymptotics,
Lévy–Khintchine, and uniqueness of finite-measure Fourier transforms are
classical background. All nonstandard applications needed for the claimed
classification are explicitly derived above.
