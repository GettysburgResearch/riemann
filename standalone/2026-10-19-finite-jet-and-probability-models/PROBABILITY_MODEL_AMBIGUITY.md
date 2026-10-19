# Positive probability models: finite theta moments, xi-scale growth, and either zero geometry

**Status:** Proposed analytic theorem with proof. Independent review is required. The abstract theorem is conditional on a precisely stated finite nonsingular realization. Its theta-order-20 application consumes the proposed finite source theorem in PR #994; that source certificate was read, not independently recomputed.

**Not claimed:** equality to the theta density, an Euler product, the actual zeta zero-count remainder, all-order theta feasibility, an off-critical zeta zero, RH, or a new zeta boundary. No worldwide priority claim is made.

This strengthens the polynomial construction in the companion note. It keeps a genuine positive probability law, fixed variance, order-one entire growth, both main terms of the Riemann-von Mangoldt counting law, and the leading logarithmic theta tail rate. These features still do not turn a fixed finite moment realization into a proof about the actual xi function.

## 1. The finite realization hypothesis

Let `rho` be an even probability law with positive variance `v` and moments through order `2M`. Assume it has a **locally nonsingular finite ferromagnetic realization** of these moments:

There is an open real parameter set `U`, a point `p_0 in U`, and finite zero-field ferromagnetic Ising observables `Y_p`, such that:

* each observable is a nonnegative weighted sum of finitely many spins, with every observed weight strictly positive;
* the law has positive mass at both support endpoints `+/-S(p)`, where `S(p)>0` varies continuously;
* the map `p -> (kappa_2(Y_p),...,kappa_(2M)(Y_p))` is locally invertible at `p_0` (one may freeze inactive parameters);
* these cumulants equal those of `rho` at `p_0`.

The weighted ferromagnetic Lee-Yang theorem makes the characteristic function `F_p(z)=E exp(izY_p)` real-zero. It is a finite exponential sum and hence entire of exponential type `S(p)`.

For the actual theta law, the proposed theorem T20D in

`GettysburgResearch/riemann`, commit `c93ca65a510b6acaf167f929b9bf7e67d742b05a`,
`standalone/2026-10-18-theta20-and-native-cancellation/theta/PROOF20.md`

supplies exactly this hypothesis for `M=10`. It has ten active coordinates, an invertible center Jacobian, and strict full-cube margins. Scaling its variance-one observable by `sqrt(v)` preserves nonsingularity. The weighted Lee-Yang input and theta Fourier identity are stated in Newman and Wu, arXiv:1901.06596v2, Sections 2.1 and 2.5.

## 2. The theorem

**Theorem B.** Under the finite realization hypothesis, fix any `B>0` and `H>0`. There exists an even probability law `rho_*` with entire characteristic function `F_*` satisfying:

\[
\mathbb E_*X^{2r}=\mathbb E_\rho X^{2r},\qquad 1\le r\le M,\tag{B1}
\]

and

\[
|F_*(z)|\le \exp\bigl(v(\Im z)^2/2\bigr),\qquad z\in\mathbb C.\tag{B2}
\]

All its zeros lie in `|Im z|<=B`. Its nonreal zeros are exactly two horizontal arithmetic progressions

\[
z=\frac{(2k+1)\pi}{w}\pm iB,\qquad k\in\mathbb Z,\tag{B3}
\]

for some `w>0` with `pi/w>H`. All its remaining zeros are real.

It is an entire function of order one and infinite type. Moreover, as `y->+infinity`,

\[
\log F_*(iy)
=\frac y2\log y-\frac{1+\log(2\pi)}2y+O(\sqrt y),\tag{B4}
\]

and its zeros, counted with multiplicity in `0<Re z<=T`, satisfy

\[
N_*(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}
       +O(\sqrt T).\tag{B5}
\]

Constants depend on the constructed model. The error in (B5) is **not** the actual zeta error `O(log T)`. No simplicity or zeta pair-correlation statement is asserted.

The probability tails obey

\[
\log\Pr_*(X\ge x)=-\pi e^{2x}(1+o(1)),\qquad x\to+\infty,\tag{B6}
\]

and the identical left-tail statement by symmetry. This is a logarithmic tail-probability asymptotic, not equality to the theta density or its full tail expansion.

There is also a model satisfying (B1), (B2), (B4), (B5), and (B6) with **only real zeros**. Thus these data and leading growth constraints accommodate both zero geometries.

## 3. Three components

### 3.1 A small positive law carrying the off-axis zeros

For small `w>0`, put

\[
A_{w,B}(z)=\frac{\cosh(Bw)+\cos(wz)}{1+\cosh(Bw)}.\tag{B7}
\]

This is the characteristic function of a positive three-point law: masses `q/2` at `+/-w` and `1-q` at zero, where

\[
q=\frac1{1+\cosh(Bw)}.
\]

Its zeros are precisely (B3), its support radius is `w`, and its cumulants through any fixed order tend to zero as `w->0`. Choose `w` small enough that `cosh(Bw)<=2` and `pi/w>H`.

For later use, this law is sub-Gaussian with **its own variance** `qw^2`. Since `q>=1/3`, for `k>=1`,

\[
q w^{2k}\le (2k-1)!!(qw^2)^k.
\]

Indeed, `(2k-1)!!>=3^(k-1)`. Comparing the positive even coefficients of the moment generating functions gives

\[
A_{w,B}(iy)\le e^{qw^2y^2/2}.\tag{B8}
\]

### 3.2 A harmonic Rademacher tail

Let

\[
R_N(z)=\prod_{n>N}\cos\frac{z}{2n}.\tag{B9}
\]

The independent random series `sum_(n>N) epsilon_n/(2n)`, with fair independent signs, converges almost surely and in `L^2`. Its finite exponential moments follow from the bound on products of cosh. The product (B9) converges locally uniformly to its entire characteristic function, since `sum n^-2<infinity`.

Every zero is real, and the infinite product has no additional zeros away from its factor zeros: on each compact set the tail product converges absolutely and nonvanishingly. Its variance is at most `1/(4N)` and its cumulants of order `2r` are

\[
\frac{c_{2r}}{2^{2r}}\sum_{n>N}n^{-2r},\tag{B10}
\]

where `c_(2r)` is the fair-sign cumulant. These all tend to zero for fixed `r`.

This component costs arbitrarily little in any fixed list of cumulants but supplies order-one, infinite-type growth.

### 3.3 Arbitrarily large support at arbitrarily small cumulant cost

For an integer `K` and `delta>0`, the characteristic function

\[
C_{K,\delta}(z)=\cos(\delta z/K)^K\tag{B11}
\]

has real zeros and support radius `delta`. Its `2r`-th cumulant is

\[
c_{2r}\frac{\delta^{2r}}{K^{2r-1}}.\tag{B12}
\]

For `delta` in any fixed bounded interval, all the finitely many cumulants under consideration tend uniformly to zero as `K->infinity`. The interval may depend on `N`; `N` is fixed before `K` is chosen.

## 4. Exact moment repair and calibration of the linear growth term

Write `H_N=sum_(n<=N)1/n` and let `gamma` denote Euler's constant. Set

\[
D_N=H_N-\log4-2\gamma.\tag{B13}
\]

First choose sufficiently large `N` and sufficiently small `w` that the added cumulants from (B7) and (B9) lie inside the local inverse chart from Section 1. Also choose `N` so large that

\[
\delta_0=D_N/2-S(p_0)-w>2.
\]

For `delta` in `[delta_0-1,delta_0+1]`, take `K` sufficiently large that the cumulants in (B12) are uniformly small. The inverse chart then supplies a continuous `p(delta)` satisfying

\[
\kappa_{2r}(Y_{p(\delta)})
+\kappa_{2r}(A_{w,B})
+\kappa_{2r}(R_N)
+\kappa_{2r}(C_{K,\delta})
=\kappa_{2r}(\rho),\quad 1\le r\le M.\tag{B14}
\]

All parameters remain strictly inside the original ferromagnetic domain. The choices can be made so that

\[
|S(p(\delta))-S(p_0)|<1/2
\]

uniformly on this interval. Consequently the continuous function

\[
S(p(\delta))+w+\delta-D_N/2
\]

has opposite signs at its endpoints. The intermediate value theorem produces a positive `delta_*` for which

\[
S(p_*)+w+\delta_*=D_N/2.\tag{B15}
\]

Define

\[
F_*(z)=F_{p_*}(z)\, A_{w,B}(z)\, R_N(z)\,
           C_{K,\delta_*}(z).\tag{B16}
\]

This is the characteristic function of the sum of four independent, even, positive random variables. Equation (B14) and the triangular moment-cumulant relations prove (B1) exactly, not approximately. Equation (B15) will calibrate both linear growth terms.

For the all-real-zero version, omit `A_{w,B}`, set its cumulant and support contributions to zero, and repeat the same argument.

## 5. The variance-controlled bound

An even finite real-zero entire characteristic function of exponential type has the paired Hadamard product

\[
F_p(z)=\prod_j(1-z^2/\gamma_j^2),\qquad \gamma_j>0,
\]

with multiplicities. There is no quadratic exponential factor because its order is at most one, and evenness removes a linear exponential factor. Its variance is `2 sum_j gamma_j^-2`. Thus

\[
F_p(iy)\le \exp(\operatorname{Var}(Y_p)y^2/2).
\]

The Rademacher factors obey the analogous bound by `cosh t<=exp(t^2/2)`. The three-point factor obeys (B8). Variances add and (B14) fixes their sum to `v`. Finally, positivity of the probability law gives

\[
|F_*(x+iy)|\le F_*(iy)\le e^{vy^2/2},
\]

proving (B2). This also verifies all needed exponential-moment convergence statements without presuming RH.

## 6. Exact counting identity for the harmonic component

Put `X=T/pi`. The positive zeros of `cos(z/(2n))` are `pi*n*j` for odd positive `j`. Therefore

\[
N_{R_N}(T)=D(X)-D(X/2)-\sum_{n=1}^N
                  \left\lfloor\frac{\lfloor X/n\rfloor+1}{2}\right\rfloor,\tag{B17}
\]

where `D(X)=sum_(n<=X) floor(X/n)` for real `X>=0`. This identity counts zeros with multiplicity; coincidences are not discarded.

The elementary Dirichlet hyperbola formula gives

\[
D(X)=X\log X+(2\gamma-1)X+O(\sqrt X).
\]

For example, expand `D(X)=2 sum_(n<=sqrt X)floor(X/n)-floor(sqrt X)^2` and use the harmonic-sum expansion. Applying it in (B17), while the subtracted finite sum is `X H_N/2+O(N)`, gives

\[
N_{R_N}(T)=\frac{T}{2\pi}\log T
 +\frac{\log(2/\pi)+2\gamma-1-H_N}{2\pi}\,T
 +O_N(\sqrt T).\tag{B18}
\]

### Finite exponential-sum count used here

A finite exponential sum with real frequencies between `-S` and `S`, nonzero endpoint coefficients and all zeros real, has positive zero count `ST/pi+O(1)`.

Here is a direct argument. At sufficiently large fixed positive and negative imaginary parts, the endpoint terms dominate uniformly in the real part. Their arguments along the horizontal edges of a rectangle contribute `4ST+O(1)` in total. On a vertical edge, after rotation by a generic fixed phase, the imaginary part is a real linear combination of finitely many distinct real exponentials in the vertical coordinate. Such a nonzero combination has at most one fewer real zero than its number of terms, by induction using Rolle's theorem. Thus the vertical-edge argument changes are uniformly bounded independently of `T`. The argument principle gives the total count in `[-T,T]`; evenness gives the positive count. Endpoints that are zeros are handled by one-sided limits. All constants may depend on the finite sum, including its number of terms.

It follows that `F_(p_*)` contributes `S(p_*)T/pi+O(1)`. The `K` cosine factors contribute `delta_*T/pi+O(K)`. The two off-axis progressions together contribute `wT/pi+O(1)`. Add these to (B18) and use (B15): the linear coefficient becomes exactly `-(log(2*pi)+1)/(2*pi)`. This proves (B5).

## 7. Growth and the tail asymptotic

The paired real-zero product for `R_N` and integration by parts give

\[
\log R_N(iy)
=\int_0^\infty\frac{2y^2 N_{R_N}(t)}{t(t^2+y^2)}\,dt.
\]

Inserting (B18), using

\[
\int_0^\infty\frac{du}{1+u^2}=\pi/2,
\qquad
\int_0^\infty\frac{\log u}{1+u^2}\,du=0,
\]

yields

\[
\log R_N(iy)=\tfrac12 y\log y
 +\tfrac12[\log(2/\pi)+2\gamma-1-H_N]y+O_N(\sqrt y).
\]

The other three factors have logarithmic moment generating functions
`S(p_*)y+O(1)`, `wy+O(1)`, and `delta_*y+O(1)`, respectively. Equation (B15) gives (B4).

For an even probability law, the maximum of `|F_*(z)|` on `|z|<=r` equals `F_*(ir)`: the upper bound follows from the integral and monotonicity of the even moment generating function, and equality holds at `ir`. Therefore (B4) proves order one and infinite type.

For completeness, (B6) follows by exponential tilting, not merely by a Chernoff upper bound. Put `Lambda(y)=log F_*(iy)` and

\[
C=-\tfrac12(1+\log(2\pi)).
\]

Equation (B4) and convexity imply

\[
\Lambda'(y)=\tfrac12\log y+C+\tfrac12+o(1).
\]

This derivative consequence follows by bounding the derivative between secants at multiplicatively nearby arguments and then letting their relative separation tend to zero. Moreover,

\[
\Lambda''(y)=O(1/y).
\]

For the harmonic part this is the direct bound
`sum_(n>N)(4n^2)^(-1) sech^2(y/(2n))=O(1/y)`: split at `n=y` and bound the smaller `n` in dyadic groups. The other components have finite support with a positive endpoint mass, so their tilted variances decay exponentially for this fixed model.

Chernoff's inequality with `y=exp(2x-1-2C)` gives the upper logarithmic rate `-pi e^(2x)(1+o(1))`. For the lower bound, fix `epsilon>0` and choose the tilt with mean `x+epsilon`. Its variance tends to zero, so the tilted probability of `[x,x+2epsilon]` tends to one. Undoing the tilt gives

\[
\liminf_{x\to\infty}e^{-2x}\log\Pr(X\ge x)
\ge-(1/2+\epsilon)e^{2\epsilon-1-2C}.
\]

Let `epsilon` decrease to zero. Since `exp(-1-2C)=2*pi`, the lower and upper rates agree, proving (B6). QED.

### The constructed probability law has a density

It is not merely a discrete probability measure. For large real `t`, use only the factors in (B9) with `n>ceil(|t|)`. Their arguments have absolute value at most `1/2`, and `log cos u<=-u^2/2` on that interval. Since the remaining factors have modulus at most one,

\[
 |F_*(t)|\le\exp\left[-\frac{t^2}{8}\sum_{n>\lceil|t|\rceil}n^{-2}\right]
 \le e^{-|t|/16}
\]

for all sufficiently large `|t|` (depending on `N`). Fourier inversion therefore gives a nonnegative real-analytic probability density. This does not assert strict log-concavity or equality to the theta density.

## 8. Interpretation for the repository

The actual theta kernel has leading positive-tail logarithm `-pi exp(2x)` from its `n=1` term. Stirling's formula gives the two displayed leading terms in (B4) for its moment generating function. The classical Riemann-von Mangoldt law gives the two main terms in (B5). The constructed law matches those leading features but not the full theta source, its finer growth expansion, or its arithmetic structure.

In the theta application, this theorem preserves moments through 20, **not 26**. The companion polynomial theorem preserves the order-26 jet, but it does not claim a positive inverse Fourier law. These two scopes must not be combined into an unsupported order-26 probability theorem.

The mechanism identifies a concrete blind spot: arbitrarily small changes in finitely many cumulants can carry zeros at a fixed nonreal distance but arbitrarily large height. Even fixing positivity, variance, normality, entire order, two leading counting terms and the leading tail rate does not remove that blind spot.

The correct cofinal criterion remains valid. To obtain RH or a narrower strip, one must impose a source-specific all-order construction, a quantitative approximation bound on expanding complex domains, or another genuinely global identity. This theorem does not prove that such an approach is impossible.

The related `KERNEL_STRIP_INSTABILITY.md` in PR #1005 was read after this construction was developed. It proves a different, overlapping obstruction directly from the theta density, with smooth proximity and strong log-concavity. The present note does not claim priority for finite-moment instability; its distinguishing constraints are all-zero strip confinement, the variance envelope, and the calibrated leading asymptotics.
