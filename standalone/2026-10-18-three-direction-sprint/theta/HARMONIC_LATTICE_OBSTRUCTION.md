# A harmonic lattice leaves a stretched-exponential fingerprint

**Status: PROPOSED analytic theorem requiring independent hostile review.**
This is a stronger obstruction to the infinite-star completion candidate
than its first few Stirling coefficients. It is kept separate from the
reviewed finite certificates and the simpler obstructions. Its scope is
an exactly shifted harmonic weight tail and a coupling profile analytic
at zero; it does not exclude arbitrary tails or hierarchical graphs.

## 1. Statement and the proposed conclusion

Consider the symmetric infinite star of HARMONIC_STAR.md, with an
observed hub of fixed weight B>=0. Apart from finitely many leaves, let

\[
 w_n=\frac1{2(n+a)},\quad a>0,\qquad J_n=J(w_n), \tag{1}
\]

where J is real on a positive neighborhood of zero, holomorphic at zero,
J(0)=0, and J_n>=0. Finite head weights and couplings may be arbitrary
positive values. Its limit is growth controlled as proved there.

The proposed conclusion is that this law cannot equal the actual
original theta law, **including when B>0**. The lattice tail leaves a
nonzero oscillatory term of scale exp(-2sqrt(pi t)) in the second
derivative of its positive-real log MGF. The actual xi function has no
such term once its integer asymptotic coefficients are matched.

The proof is given below so the contour, endpoint, uniform-sum and
optimal-truncation claims can be checked separately. No numerical
experiment or all-orders-formal-equality shortcut is used.

## 2. The conditional second derivative and the continuum integral

Write L_J as in HARMONIC_STAR.md. Its second derivative is

\[
 L_J''(t)=\sum_n\frac1{4(n+a)^2}
   \operatorname{sech}^2\left[\frac{t}{2(n+a)}+
                         J\left(\frac1{2(n+a)}\right)\right]. \tag{2}
\]

Choose an integer N so large that A=N+a lies inside the domain needed
for J(1/(2z)) whenever |z|>=A and |arg z|<=pi/4. We can require
`|J(w)|<=C|w|` there. Every removed head contribution to (2) is
O(exp(-c t)), with its first finitely many t derivatives, since its
weight is fixed and positive. Define

\[
 F_t(x)=\frac1{4x^2}\operatorname{sech}^2
            \left[\frac{t}{2x}+J\left(\frac1{2x}\right)\right],
 \qquad I_J(t)=\int_A^\infty F_t(x)\,dx. \tag{3}
\]

The precise lattice fingerprint is

\[
\begin{split}
 L_J''(t)-I_J(t)
 ={}&C_*t^{-3/4}e^{-2\sqrt{\pi t}}\\
 &\cdot\left\{\cos\left(2\sqrt{\pi t}-\frac\pi8-2\pi a\right)
                   +O(t^{-1/2})\right\},\\
 C_*={}&2\sqrt\pi(2\pi)^{1/4}>0. \tag{4}
\end{split}
\]

Exponential-in-t errors and the faster exp(-2sqrt(2pi t)) terms are
absorbed into the displayed remainder. In particular (4) is flat to
every inverse-power order but is not O(exp(-c t)) for any c>0.

## 3. One-sided Poisson, endpoints and pole avoidance

For fixed sufficiently large t, F_t and its first two x derivatives are
integrable at infinity. The one-sided Poisson formula is

\[
 \sum_{n=0}^\infty F_t(A+n)
 =\frac12F_t(A)+I_J(t)
 +2\Re\sum_{k\ge1}e^{-2\pi i kA}
                   \int_A^\infty F_t(x)e^{2\pi i kx}\,dx. \tag{5}
\]

It follows, for example, by Fourier expansion of the periodized function
with its half endpoint value; two integrations by parts make its real
Fourier series absolutely summable. The half endpoint is O(exp(-c t)).

Rotate each positive-k integral into the ray x=e^(i pi/4)r, r>=A,
with the connecting fixed-radius arc. For this whole sector,

\[
 \Re\left[\frac{t}{2x}+J\left(\frac1{2x}\right)\right]
     \ge\frac{t/(2\sqrt2)-C/2}{|x|}>0 \tag{6}
\]

when t is large. Thus no sech pole is crossed. On the connecting arc,
F_t and each fixed x derivative are bounded by a polynomial in t times
exp(-c t). The first integration-by-parts endpoint at real x=A is
`F_t(A)e^(2pi i kA)/(2pi i k)`. After the phase in (5) and taking
real parts it vanishes, because F_t(A) is real. A second integration
by parts bounds the remaining real-endpoint arc error by
`C t^d exp(-c t)/k^2`. The other arc endpoint has the additional
factor exp(-sqrt(2)pi k A), and its sum is bounded by the same
exponential-in-t scale. These estimates justify summing the endpoint
errors, rather than treating a nonsummable O(exp(-c t)) for each k
as if it were already uniform.

## 4. Absolute exponential expansion on the rotated ray

By (6), on the ray we may use

\[
 F_t(x)=x^{-2}\sum_{m\ge1}(-1)^{m-1}m
                   e^{-m t/x}e^{-2mJ(1/(2x))}. \tag{7}
\]

The absolute value of a term, including its Fourier exponential, is
bounded by

\[
 C m r^{-2}\exp\left[-\frac{m(t-C')}{\sqrt2 r}
                              -\sqrt2\pi k r\right]. \tag{8}
\]

The sum over m at every r is finite. As r tends to infinity it is at
most a polynomial in r/t, while the exp(-sqrt(2)pi k r) factor
controls the integral. Near the ray's lower endpoint, exp(-c m t/A)
controls both m and its derivatives. Hence Tonelli applies to absolute
values after rotation, including the m,k sums. There is no unjustified
absolute expansion on the original real ray at x=infinity.

For m=k=1,

\[
 e^{-2J(1/(2x))}=1+O(1/r). \tag{9}
\]

The O(1/r) correction in (9) contributes at most O(t^(-1/2)) times
the magnitude scale of the main saddle integral: compare its absolute
integral with the p=3 version of the p=2 integral below. The positive
Laplace saddle r=sqrt(t/(2pi)) gives the stated factor t^(-1/2).
The inequality |exp(-2mJ)-1|<=C(m/r)exp(Cm/r) also makes this estimate
uniform for the subleading m,k terms. All terms with mk>=2 are bounded
by a polynomial times exp(-2sqrt(pi mk(t-C'))). Grouping by mk uses
only a divisor-count polynomial bound, so their total is
O(poly(t)exp(-2sqrt(2pi t))).

The missing lower-ray segment0<r<A for the main J=0 integral is
O(exp(-c t)); summing its Fourier factors remains harmless because
exp(-t/(sqrt(2)r)) dominates the geometric k sum near zero. Thus it
can be restored when evaluating the main integral exactly.

## 5. Exact leading Bessel integral and phase

For p=2 and positive m,k, analytic continuation of the usual Laplace
integral gives

\[
 \int_0^\infty x^{-2}e^{-mt/x+2\pi i kx}\,dx
 =2\left(\frac{-2\pi i k}{mt}\right)^{1/2}
       K_1\left(2\sqrt{-2\pi i kmt}\right). \tag{10}
\]

The integral is evaluated along the rotated ray, where it is absolutely
convergent. Square roots use argument -pi/4 for sqrt(-i).
The classical K integral and large-argument expansion are pinned to
[NIST10.32.10](https://dlmf.nist.gov/10.32#E10) and
[NIST10.40.2](https://dlmf.nist.gov/10.40#E2). Formula (10) first follows
with a positive damping parameter and then by contour continuation;
the final ray keeps arg K=-pi/4 inside its asymptotic sector.

For m=k=1 the asymptotic is

\[
 \sqrt\pi(2\pi)^{1/4}t^{-3/4}e^{-2\sqrt{\pi t}}
        e^{i(2\sqrt{\pi t}-\pi/8)}[1+O(t^{-1/2})]. \tag{11}
\]

Multiply by the phase exp(-2pi i A), take twice its real part,
and note A=a+N. This proves (4), with the constant and phase displayed
there. The analytic coupling profile changes only the relative
O(t^(-1/2)) correction, not the nonzero leading coefficient.

## 6. A genuine Gevrey bound for the continuum integral

The following step is stronger than existence of a formal expansion.
With u=t/(2x),

\[
 I_J(t)=\frac1{2t}\int_0^{t/(2A)}
                     \operatorname{sech}^2[u+J(u/t)]\,du. \tag{12}
\]

Choose r>0 inside the holomorphy disk of J so small that |J(w)|<pi/8
for |w|<=r. For each real u>=0, the function
`H_u(w)=sech^2[u+J(w)]` is holomorphic there, and

\[
 |H_u(w)|\le C e^{-2u},\qquad |w|\le r. \tag{13}
\]

For u in a bounded interval enlarge C; for larger u the bound follows
from the elementary exponential formula for cosh. Cauchy's estimates
give coefficients bounded by C r^(-j)e^(-2u). Increase A further so
1/(2A)<r/2. Taylor expansion at w=0 in (12), with its full geometric
remainder, therefore gives a remainder bounded by

\[
 \frac{C}{t}(rt)^{-q}\int_0^\infty u^q e^{-2u}\,du
       \le C D^q q!\,t^{-q-1}. \tag{14}
\]

Extending the coefficient integrals from t/(2A) to infinity costs
O(exp(-c t)), uniformly for q<=delta t with fixed sufficiently small
delta>0. This follows by bounding u^j e^(-2u) on that tail, using
j<=delta t and choosing delta<1/(4A). At the lower tail endpoint
u_0=t/(2A), the Taylor ratio is `u_0/(rt)=1/(2Ar)<1/2`; the
factorial-tail estimates stay uniform through q=floor(delta t).
Consequently I_J has an
integer inverse-power expansion with the explicit **Gevrey1** bound
(14), plus an exponential-in-t remainder, up to q<=delta t.
Choosing q=floor(epsilon t), with epsilon smaller than both delta
and1/(2eD), makes the bound O(exp(-c' t)). No conclusion about an
exponentially small remainder was inferred merely from all-order
formal matching.

## 7. The actual xi second derivative has the same Gevrey type

Let K_theta(t)=log[xi(1/2+t)/xi(1/2)]. For t>1/2, the exact gamma
and elementary prefactor identities give

\[
 K_\theta''(t)=\int_0^\infty e^{-tv}B_\theta(v)\,dv
                    +(\log\zeta)''(t+1/2), \tag{15}
\]
\[
 B_\theta(v)=\frac{v e^{-v/2}}{1-e^{-2v}}
                                  -2v\cosh(v/2). \tag{16}
\]

For (15), use the convergent trigamma integral and
`[log(t^2-1/4)]''=-1/(t-1/2)^2-1/(t+1/2)^2`.
The kernel B_theta is holomorphic near v=0 (its apparent pole is
removable), with its nearest possible denominator poles at +/-i pi.
Its positive-real growth is at most exponential. Cauchy bounds and
the same Laplace Taylor argument as (14) give a Gevrey1 integer
expansion with an O(exp(-c t)) optimally truncated remainder.
The absolutely convergent Dirichlet series for (log zeta)'' is itself
O(exp(-c t)), for example by bounding it at a fixed real point and
factoring out a power of2^(-t). Thus no stretched-exponential term
is hidden in this target estimate.

## 8. Contradiction and remaining scope

When B>0 the full symmetric log MGF differs from Bt+L_J(t)-log2 by
O(exp(-c_B t)), with its first two derivatives: the other hub branch
has ratio exp(-2Bt) times a fixed power of t. If it equalled the actual
theta MGF, (4) would force the integer asymptotic coefficients of
I_J and K_theta'' to agree at every order. Optimally truncate their
common series using (14)--(16). It would follow that

\[
 I_J(t)-K_\theta''(t)=O(e^{-c t}). \tag{17}
\]

But (4) contradicts (17) along the explicit sequence on which
`2sqrt(pi t)-pi/8-2pi a` is an integer multiple of2pi. Its cosine is1
and its relative error tends to zero. Finite head changes add only
exponential-in-t terms and cannot remove this contradiction.

For B=0, the separate integer-jet/opposite-branch obstruction in
HARMONIC_STAR.md already applies: matching theta forces h=7/2 and
then produces a positive t^(-7/2) term. Thus the proposed obstruction
covers both hub cases under the analytic-profile premise.

This result would require a successful star completion to leave at least
one of the exact harmonic lattice, analytic coupling profile, fixed-head
or single-hub assumptions. A nonanalytic/nonlattice tail or a hierarchy
is not excluded. No such surviving actual-theta construction is supplied
here, and no zero-free region follows from this obstruction.
