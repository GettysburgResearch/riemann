# Attempt at the near-linear bound: a critical-line formula, its tail, and a one-sided alternative

Status: component proof draft; independent review required. **The requested
bound |B_(2j^2+1)| = O_epsilon((2j^2+1)^(1+epsilon)) is NOT proved. RH and
the original uniform block-gain assertion remain unproved.** This note records
an attempted proof, not a replacement of its missing estimate by a PASS marker.

Frozen parent: PR #805, ccd0a80dbd9844d06ccd6331a15b085b9c9afa41.
Parent proof: standalone/2026-09-07-astra-balanced-hyperbola/PROOF.md.
No previous source is changed. The Perron, contour, Mertens and Landau
principles below are classical; no novelty or priority is claimed for them.

## 1. Source and exact starting identity

All arithmetic sums in this note are on positive odd integers unless stated
otherwise. Let mu be the ordinary Mobius function, and put

    M_o(x) = sum_(n<=x, odd) mu(n),
    m_o(x) = sum_(n<=x, odd) mu(n)/n,
    Q(x)   = M_o(x) - x m_o(x).

For odd Y>=3 define lambda_k=mu(k)-Y m_o(Y) 1_(k=Y), for odd k<=Y,
and zero otherwise. Then lambda_1=1 and sum lambda_k/k=0, including when Y
is nonsquarefree. Define

\[
 Z(s)=(1-2^{-s})\zeta(s),\qquad P_Y(s)=\sum_{k\le Y}\lambda_k k^{-s},
 \quad W(z)=\sum_{r\le z}(z/r-1),
\]

with W=0 below 1, and

\[
 \mathcal B_Y=\sum_{a,b\le Y}\lambda_a\lambda_b W(Y^2/(ab)).       \tag{1}
\]

The frozen parent proves, with all cross terms retained,

\[
 Q(Y^2)=2Q(Y)+\mathcal B_Y.                                    \tag{2}
\]

One can rederive (2) by putting u(n)=1 on odd integers and L=lambda in the
Dirichlet convolution ring. The defect b=e-u*L vanishes below Y. The identity
mu-(2L-u*L*L)=mu*b*b is supported at n>=Y^2. Its coefficient at Y^2 need not
vanish, but its weight 1-Y^2/n does. Applying that weight gives (2).

The elementary divisor identity sum_(n<=N)mu(n)floor(N/n)=1 gives
|sum_(n<=N)mu(n)/n|<=1. Separating powers of two therefore gives |m_o(x)|<=2,
and hence |Q(x)|<=3x. These bounds use no RH or zero computation.

## 2. CL26.1: the contour reaches the critical line unconditionally

For every fixed odd Y>=3 the following integral is absolutely convergent:

\[
 \boxed{\mathcal B_Y=-\frac{Y}{\pi}\Re\int_0^\infty
 \frac{Z(\tfrac12+it)P_Y(\tfrac12+it)^2Y^{2it}}{t^2+1/4}\,dt.}  \tag{3}
\]

**Proof.** Mellin inversion of (z-1)_+ gives, for c>1,

\[
 W(z)=\frac1{2\pi i}\int_{(c)}\frac{Z(s)z^s}{s(s-1)}\,ds.
\]

At z equal to an odd integer the newly entering summand is zero, so there
is no half-weight ambiguity. Absolute convergence on this line and the
finite a,b sum give

\[
 \mathcal B_Y=\frac1{2\pi i}\int_{(c)}
       \frac{Z(s)P_Y(s)^2Y^{2s}}{s(s-1)}\,ds.                   \tag{4}
\]

Since P_Y(1)=0, its square cancels BOTH powers in the possible pole of
Z(s)/(s(s-1)) at 1. The integrand is holomorphic on Re(s)>0. In particular,
no zero-free hypothesis is required: zeta is in the numerator, not the
reciprocal. For fixed Y, P_Y is bounded on each vertical strip used here.
The standard zeta strip bounds (for instance via the approximate functional
equation and Phragmen--Lindelof) make the horizontal integrals tend to zero.
A bound O_eta(T^(1/4+eta)) uniformly on 1/2<=Re(s)<=c, with 0<eta<3/4,
is more than sufficient. The critical-line bound |zeta(1/2+it)|=O(t^(1/4))
itself follows by bounding both length-O(sqrt(t)) sums in the approximate
functional equation absolutely [2]. Thus the shifted integral is absolutely
convergent. On s=1/2+it, s(s-1)=-(t^2+1/4). Pair conjugate t values to obtain
(3). This shift crosses no unaccounted residue. QED.

The square in (3) is P_Y(s)^2, NOT |P_Y(s)|^2. The signed real part is
essential. Replacing that square by its modulus is an inequality with a new
estimation obligation, not another exact identity.

## 3. CL26.2: the complete high-frequency tail costs only O(Y)

Choose any finite constant C_zeta such that

\[
 |Z(\tfrac12+it)|\le C_\zeta t^{1/4}\quad(t\ge1).
\]

Its existence follows from [2]; no certified numerical value is asserted.
Set A_Y=sum |lambda_k|/sqrt(k). The exact terminal correction and |m_o|<=2
imply

\[
 A_Y\le\sum_{k\le Y}k^{-1/2}+\sqrt Y|m_o(Y)|\le4\sqrt Y.
\]

For EVERY T>=1, the omitted part of (3) is at most

\[
 \boxed{\left|\mathcal B_Y+\frac Y\pi\Re\int_0^T
  \frac{Z(\tfrac12+it)P_Y(\tfrac12+it)^2Y^{2it}}{t^2+1/4}\,dt\right|
 \le\frac{4C_\zeta}{3\pi}Y A_Y^2 T^{-3/4}
 \le\frac{64C_\zeta}{3\pi}Y^2T^{-3/4}.}                       \tag{5}
\]

Indeed |P_Y|<=A_Y, t^2+1/4>=t^2, and
integral_T^infinity t^(-7/4)dt=(4/3)T^(-3/4). No frequency is sampled or
omitted without this bound. Taking the predetermined T=Y^(4/3) proves

\[
 \mathcal B_Y=-\frac Y\pi\Re\int_0^{Y^{4/3}}
  \frac{Z(\tfrac12+it)P_Y(\tfrac12+it)^2Y^{2it}}{t^2+1/4}\,dt+O(Y). \tag{6}
\]

The constant is independent of Y. The requested assertion on Y_j=2j^2+1 is
therefore equivalent to a subpower bound on the signed integral in (6) along
that same grid. That bound is NOT established here.

An attempted sufficient majorant is

\[
 \mathcal M_Y=\int_0^\infty
 \frac{|Z(\tfrac12+it)|\,|P_Y(\tfrac12+it)|^2}{t^2+1/4}\,dt,
 \qquad |\mathcal B_Y|\le(Y/\pi)\mathcal M_Y.                   \tag{7}
\]

Its finiteness for each Y is proved; its subpower growth is NOT. A generic
diagonal mean-square argument is insufficient. The parent's positive-block
counterexample, with its fixed coefficients at 1 and 3 added, is balanced,
has lambda_1=1 and sum lambda_k^2/k<5, yet B_Y is bounded below by a positive
constant times Y^2 for all sufficiently large members of that family. Formula
(7), which holds for any finite balanced source, forces M_Y to be at least a
positive constant times Y there. This is not the actual Mobius source. It
rules out a source-independent, subpower diagonal domination; it does not
rule out the special estimate needed for the literal P_Y.

## 4. CL26.3: an unconditional actual-source improvement, below the requested strength

Let f(v)=v^(3/5)(log v)^(-1/5), for v sufficiently large. Import the classical
unconditional Mertens estimate, in the form established explicitly by
Lee--Leong [3]: there exist positive C,a,x_0 such that, for the ORDINARY
Mertens function M(x)=sum_(n<=x)mu(n),

\[
 |M(x)|\le Cx\exp(-a f(\log x))\quad(x\ge x_0).                \tag{8}
\]

We import this theorem, not its numerical constants or a new replay of its
external computations. It is not an RH-conditional assertion.

It implies the following bound for the ACTUAL source, on all odd Y and hence
on the requested grid:

\[
 \boxed{|\mathcal B_Y|\ll Y^2\exp\{-c(\log Y)^{3/5}
                                      (\log\log Y)^{-1/5}\}}  \tag{9}
\]

for some c>0. This is a consequence of established Mertens theory, not a new
power saving or a new zero-free region.

**Proof.** Exactly, M_o(x)=sum_(2^r<=x) M(x/2^r). Split this sum when
x/2^r reaches sqrt(x). The large-argument part is bounded by
2Cx exp(-a f((log x)/2)); the remaining part is O(sqrt(x)). Since
f(v/2)>=2^(-3/5)f(v) for large v, this proves

    |M_o(x)| <= C_1 x exp(-a_1 f(log x)).

Partial summation makes sum_(n odd)mu(n)/n convergent. Its value is zero,
by Abel's theorem applied to 1/Z(s) as real s decreases to 1. Consequently

\[
 Q(x)=x\int_x^\infty\frac{M_o(t)}{t^2}\,dt.                  \tag{10}
\]

The integral is absolutely convergent under (8). For v>=L>=e^2, f(v)/sqrt(v)
is increasing, so f(v)>=f(L)sqrt(v/L). Hence

\[
 \int_L^\infty e^{-a_1f(v)}dv
 \le 2L e^{-a_1f(L)}\left(\frac1{a_1f(L)}+\frac1{a_1^2f(L)^2}\right)
 \ll e^{-a_2f(L)}
\]

with some a_2>0. Inserting this into (10) gives
Q(x)=O(x exp(-a_2f(log x))). Equation (2) proves (9); decrease c and enlarge
the constant to handle the shorter term Q(Y) and finite initial range. QED.

For every fixed 0<epsilon<1, the ratio of the right-hand comparison function
in (9) to Y^(1+epsilon) tends to infinity:

    exp((1-epsilon)log Y - c f(log Y)) -> infinity.

This is a statement about the TWO BOUNDS, not a lower bound for B_Y. Thus
(9) does not prove the requested estimate for any such fixed epsilon.

## 5. CL26.4: either one-sided near-linear estimate would suffice

The absolute value in the requested target can be weakened. Each of the
following assertions, separately, is equivalent to RH:

    for every epsilon>0, B_(2j^2+1) <= C_epsilon (2j^2+1)^(1+epsilon);
    for every epsilon>0, B_(2j^2+1) >= -C_epsilon (2j^2+1)^(1+epsilon).

The sign is fixed across the whole assertion, not chosen at each index.
Neither one-sided estimate has been proved here. This observation is an
application of classical Landau positivity, not a proof of positivity.

Here is a proof including the needed Landau lemma. If g>=0 is locally
integrable on [1,infinity), and its Mellin integral has finite abscissa of
convergence alpha, then the real point alpha is a singularity. Otherwise,
choose s_0=alpha+eta so close to alpha that the Mellin transform is analytic
in a disk about s_0 of radius greater than eta. Differentiation under the
integral gives (-1)^n F^(n)(s_0)=integral g(x)x^(-s_0-1)(log x)^n dx>=0.
Its Taylor series at s_0, evaluated at s_0-h for h>eta within that disk,
converges. Monotone convergence identifies the series with the integral
of g(x)x^(-s_0+h-1), contradicting the definition of alpha. Analyticity on
the half-plane together with a neighborhood of alpha supplies such a disk.
This proves the lemma; see also Suzuki [4], Proposition 1.

For any 0<sigma<1, either Q(x)<=Cx^sigma or -Q(x)<=Cx^sigma implies that
zeta has no zero in Re(s)>sigma. Indeed apply the lemma to
Cx^sigma-Q(x), or Cx^sigma+Q(x), respectively, increasing C on a finite
initial interval if necessary. Initially for Re(s)>1,

\[
 \widehat Q(s)=\int_1^\infty Q(x)x^{-s-1}dx
       =-\frac1{s(s-1)Z(s)}.                              \tag{11}
\]

This follows termwise from Q(x)=-sum_(k<=x)mu(k)(x/k-1).
Its meromorphic continuation is regular at every real s>0: zeta has no
positive real zero, and the apparent singularity at 1 is removable.
For 0<s<1 the nonvanishing follows from the positive alternating eta series.
Thus the nonnegative transform C/(s-sigma) minus or plus (11) has no real
singularity above sigma. Landau forces convergence throughout Re(s)>sigma.
The inequality |Q(x)|<=Cx^sigma+g(x) then makes (11) absolutely convergent
there. Multiplying by s(s-1)Z(s) excludes every zeta zero in that region.

Now suppose one of the displayed one-sided bounds for B holds. By (2) and
|Q(Y)|<=3Y the corresponding bound for Q at X_j=(2j^2+1)^2 is
O_epsilon(X_j^((1+epsilon)/2)). The parent's exact piecewise-linear Green
interpolation bounds the error between these nodes by 81sqrt(x), so the
same ONE-SIDED bound holds on the entire half-line. Apply the preceding
argument with sigma=(1+epsilon)/2 for every 0<epsilon<1. This proves RH.
For the reverse implication, import the classical RH-to-Mertens estimate
M(x)=O_epsilon(x^(1/2+epsilon)), obtain the same bound for Q by partial
summation, and use (2). That implication is conditional on RH, not an
unconditional ingredient in (9). QED.

## 6. Result of the attempted proof

The contour shift, complete high-frequency tail, classical-scale actual
upper bound, and one-sided implication are justified above. The shift itself
is legal without RH; the missing input is the SIZE of the finite critical-line
integral, not permission to move the contour. Bounding only diagonal terms
in (7) would discard correlated source terms, and the parent examples rule
out that generic shortcut. No estimate for the actual short-Mobius phases
that closes this gap was obtained. In particular neither (6) nor Landau's
lemma supplies the one-sided near-linear inequality it would consume.

The requested theorem remains unresolved in this attempt. The finite checker
accompanies the algebra and source conventions only. It does not verify a
contour integral, the classical Mertens theorem, Landau's analytic argument,
a cofinal upper bound, or RH.

## References and import scope

[1] M. N. Huxley and N. Watt, Mertens Sums requiring Fewer Values of the
Mobius function, 2018, https://arxiv.org/abs/1807.05890 . Classical short-source
quadratic identities and the contour approach are already discussed there.
The present exact balanced identity is inherited from the frozen parent.

[2] NIST DLMF, section 25.9, https://dlmf.nist.gov/25.9 . The approximate
functional equation yields the used critical-line O(t^(1/4)) bound by absolute
summation; standard strip interpolation justifies the horizontal limits.
No zero-free or Lindelof hypothesis enters CL26.1--2.

[3] E. S. Lee and N. Leong, New explicit bounds for Mertens function and the
reciprocal of the Riemann zeta-function, arXiv:2208.06141v4, Theorem 1.2 and
Introduction, https://arxiv.org/html/2208.06141v4 . Only the qualitative
existence of constants in (8) is imported. Their numerical/computational
inputs are not independently replayed. No claim of the latest constants.

[4] M. Suzuki, On variants of Chebyshev's conjecture, Ramanujan Journal 68,
95 (2025), section 2.4, Proposition 1,
https://doi.org/10.1007/s11139-025-01238-9 . Classical Landau-Mellin positivity;
the short proof needed here is supplied above. One-sided criteria do not
by themselves establish the required sign or the requested bound.
