# The fixed zero-free half-plane to Mertens adapter

Status: **PROPOSED self-contained reconstruction of a classical analytic
adapter; mathematical review requested.** No new zero-free region is proved.

Scope: zeta itself, a fixed theta in [1/2,1), and every fixed epsilon>0.
Constants depend on theta and epsilon. This supplies the explicit adapter
used in `NEGATIVE_MASS.md`; an external 2026 zero-free theorem is still an
imported input, not a result established by this packet.

Dependencies: analytic continuation of zeta, its Möbius Dirichlet series for
Re(s)>1, Borel--Carathéodory, the maximum principle for subharmonic functions,
and truncated Perron inversion. The growth estimate and Perron truncation
error are derived below rather than assumed as RH-facing oracles.

## 1. Statement

**Proposed theorem A-ZM1.** Suppose

\[
 \zeta(s)\ne0\quad(\Re s>\theta),\qquad 1/2\le\theta<1.
 \tag{Z1}
\]

Then for every epsilon>0,

\[
 M(x):=\sum_{n\le x}\mu(n)=O_{\theta,\epsilon}(x^{\theta+\epsilon}).
 \tag{Z2}
\]

The proof has two stages: establish subpolynomial reciprocal-zeta growth
on every strictly smaller zero-free half-plane, then shift a quantitatively
truncated Perron integral. Absence of zeros alone is not substituted for a
growth bound in the contour step.

## 2. An elementary polynomial bound for zeta

For integer N>=1 and Re(s)>1, partial summation of the counting function
floor(u) gives

\[
 \zeta(s)=\sum_{n\le N}n^{-s}+\frac{N^{1-s}}{s-1}
                -s\int_N^\infty\{u\}u^{-s-1}\,du.
 \tag{Z3}
\]

The integral converges absolutely for Re(s)>0, providing the continuation
of this identity there, away from s=1. Its absolute value is at most
|s| N^(-Re(s))/Re(s).

Fix any 0<a<1 and a bounded real strip a<=Re(s)<=4. At |Im(s)|>=2 choose
N=ceil(|Im(s)|). The absolute finite sum is O_a(N^(1-a)); the integral is
O_a(N^(1-a)); the rational term is smaller. Therefore

\[
 |\zeta(\sigma+it)|\ll_a(2+|t|)^{1-a},
 \quad a\le\sigma\le4,\quad |t|\ge2.
 \tag{Z4}
\]

Only this polynomial upper bound, rather than a convexity or Lindelöf
bound, is used next.

## 3. Borel--Carathéodory gives logarithmic growth of log zeta

Fix 0<delta<1-theta and set

\[
 a_0=\theta+\delta/8,\qquad a=\theta+\delta/4,\qquad b=2.
\]

For sufficiently large positive t, the disk centered at 2+it of radius
R=2-a0 lies inside the zero-free region and avoids the pole at 1. Choose
the analytic logarithm g=log zeta on that disk, taking the value at the
center from the absolutely convergent Euler logarithm. The latter has a
uniform bound, because

\[
 \log\zeta(2+it)=\sum_p\sum_{k\ge1}\frac{p^{-k(2+it)}}k.
\]

The real part of g is log|zeta|. Equation (Z4) bounds it above by C log t
throughout the disk. Borel--Carathéodory on its concentric inner disk of
radius r=2-a, whose gap R-r=delta/8 is fixed and positive, gives

\[
 |g(\sigma+it)|\ll_{\theta,\delta}\log t,
 \quad a\le\sigma\le2.
 \tag{Z5}
\]

The branch is consistent for different disks: in the zero-free upper
half-plane it is the branch obtained by analytic continuation of the Euler
logarithm from Re(s)>1. That upper half-plane is simply connected and the
pole at 1 is on its boundary, so no logarithm across the pole is required.

## 4. Finite-strip interpolation makes the reciprocal subpolynomial

The gain from (Z5) to a power of log(t) strictly below one is essential.
Here is a direct finite-rectangle argument.

For a large t0>0 consider the rectangle

\[
 a\le\sigma\le b,\qquad t_0/2\le t\le3t_0/2,
 \qquad d=b-a.
\]

Choose fixed constants C0>=1 and C1 so that |g|<=C0 on the right edge
(Euler logarithm), and |g|<=A=C1 log(t0) everywhere on the other three
edges, using (Z5). Take t0 large enough that A>=C0. Let

\[
 p(\sigma)=\frac{b-\sigma}{d},\qquad
 L(\sigma)=p(\sigma)\log A+[1-p(\sigma)]\log C_0.
\]

For u(s)=log|g(s)|, a subharmonic function, u-L<=0 on the vertical edges
and u-L<=log(A/C0) on the horizontal edges. Zeros of g merely give u=-infinity
and cause no difficulty. Put k=pi/(2d), midpoint q=(a+b)/2, and

\[
 B(\sigma,t)=
 \frac{\cos(k(\sigma-q))\cosh(k(t-t_0))}
      {\cos(kd/2)\cosh(kt_0/2)}.
\]

B is harmonic and positive on the closed rectangle. It is at least one
on either horizontal edge, since |sigma-q|<=d/2. The maximum principle
therefore gives

\[
 u(\sigma+it_0)\le L(\sigma)
       +\log(A/C_0)B(\sigma,t_0).
\]

At the middle height, B=O_d(exp(-pi t0/(4d))). Exponentiating yields

\[
 |\log\zeta(\sigma+it)|
 \ll_{\theta,\delta}(\log t)^{(2-\sigma)/(2-a)}
 \quad(a\le\sigma\le2,\ t\text{ sufficiently large}).
 \tag{Z6}
\]

For sigma>=theta+delta the exponent is at most

\[
 p_0=\frac{2-\theta-\delta}{2-\theta-\delta/4}<1.
\]

Consequently

\[
 \left|\frac1{\zeta(\sigma+it)}\right|
 \le\exp\{C_{\theta,\delta}(\log t)^{p_0}\}
 \ll_{\theta,\delta,\eta}(1+|t|)^\eta
 \quad\text{for every eta>0, uniformly in }
 \theta+\delta\le\sigma\le2.
 \tag{Z7}
\]

Negative t follows by conjugation. Bounded t follows by compactness:
1/zeta is holomorphic in Re(s)>theta, with a removable zero at s=1.
For sigma>=2 the absolutely convergent reciprocal Euler product supplies
a uniform bound, so (Z7) also holds on the whole closed half-plane
sigma>=theta+delta.

## 5. Truncated Perron with a controlled contour shift

It suffices to prove (Z2) when 0<epsilon<1-theta; larger epsilon follows
from the trivial |M(x)|<=x. For integers n>=3 take the half-integer
x=n+1/2, so M(x)=M(n), and put

\[
 c=1+1/\log x,\qquad T=x^2,
 \qquad\sigma_0=\theta+\epsilon/2,\qquad\eta=\epsilon/4.
\]

For D(s)=1/zeta(s)=sum mu(j)j^(-s) in Re(s)>1, truncated Perron gives

\[
 M(x)=\frac1{2\pi i}\int_{c-iT}^{c+iT}
               D(s)\frac{x^s}s\,ds
       +O\left(\sum_{j\ge1}(x/j)^c
           \min\{1,[T|\log(x/j)|]^{-1}\}\right).
\]

The displayed error is O(x log(x)/T). For j<=x/2 or j>=2x, the logarithm
is bounded away from zero, and x^c zeta(c)/T=O(x log(x)/T) controls the
sum. In x/2<j<2x, one has |log(x/j)|>=|j-x|/(2x), (x/j)^c<=4, and the
half-integer distance gives sum 1/|j-x|=O(log x). This also yields
O(x log(x)/T). Thus

\[
 M(x)=\frac1{2\pi i}\int_{c-iT}^{c+iT}D(s)\frac{x^s}s\,ds
                      +O(x\log(x)/T).
 \tag{Z8}
\]

D(s) is holomorphic on the rectangle from c to sigma0: there are no zeros
of zeta there, and its pole gives a zero of D. Also s=0 is outside it.
Shift to sigma0. On each horizontal segment, (Z7) gives the bound
O(x T^(eta-1)), since x^c=e x. On the new vertical segment it gives

\[
 \int_{-T}^T |D(\sigma_0+it)|\frac{x^{\sigma_0}}{|\sigma_0+it|}\,dt
 \ll_{\theta,\epsilon}x^{\sigma_0}(1+T^\eta).
\]

Therefore, with T=x^2 and eta=epsilon/4,

\[
 M(x)\ll_{\theta,\epsilon}
   x^{\theta+\epsilon/2}x^{\epsilon/2}
       +x^{-1+\epsilon/2}+x^{-1}\log x
 \ll_{\theta,\epsilon}x^{\theta+\epsilon}.
\]

This proves (Z2) for all integer n, hence for every real x by taking its
integer part. QED.

## 6. Exact negative-mass exponent for the fixed SHARP source

Let Theta be the supremum of real parts of nontrivial zeta zeros.
It lies in [1/2,1] by the classical zero symmetries and existence of zeros.
For Theta<1, apply A-ZM1 with theta=Theta, since by definition there are no
zeros in the strictly larger half-plane. Combine it with A-NM2 and the
unconditional A-NM1 lower bound. For Theta=1 the trivial bound in (A3)
provides the same upper exponent. Thus the source in (A1) satisfies

\[
 \boxed{
 \limsup_{Y\to\infty}\frac{\log(1+N(Y))}{\log Y}
       =\Theta-\frac12.}
 \tag{Z9}
\]

The equality concerns a growth exponent, not a bound at the endpoint.
It neither asserts that the supremum is attained nor certifies a zero.
In particular RH is equivalent to subpower logarithmic negative mass for
this fixed source. Importing any proved theta<1 zero-free half-plane gives
N(Y)=O_epsilon(Y^(theta-1/2+epsilon)) through the full adapter above, without
an additional unstated growth assumption.
