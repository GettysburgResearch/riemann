# Exact used-label corrections to every SHARP removal pair

Status: **Root-reviewed analytic component lemmas E1--E10.**
This file preserves the exact beta source and the two distinct labels at 67.
No critical-power or RH assertion is made.

Fix m>1, a=(m+1)/2 and x>=1. Let the labels be every ordinary prime and
one further labelled copy of 67. Write n_A for the product of a finite
subset of label indices. Put

\[
 r_A(m,x)=n_A^{-1/2}\left[\frac{T(x/n_A)}{T(x)}\right]^m,
 \quad T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},\qquad
 V(a)=\sum_q q^{-a}=P(a)+67^{-a}.
 \tag{E1}
\]

The empty-subset term is one. Define

\[
 S_k=\sum_{|A|=k}r_A,
 \qquad D_k=\sum_{|A|=k}r_A\sum_{q\in A}q^{-a}.
 \tag{E2}
\]

The sum in each D_k is over label indices, including both copies of 67
when both occur. At each finite x all active sums and all active levels
are finite. Their signed projection is exactly H_m(x)/T(x)^m: at n=67^j l,
67 not dividing l, the projected coefficient is mu(l), -2mu(l), mu(l),
and zero for j=0,1,2, and j>=3 respectively. This is precisely the native
beta coefficient. V converges absolutely since a>1.

## 1. A removal estimate with the used labels excluded

**E3.** For every active A and every unused label q,

\[
 r_{A\cup\{q\}}\le q^{-a}r_A.
 \tag{E3}
\]

If the larger product is inactive, its left side is zero. Otherwise let
y=x/n_A>=q. Both T values are positive and

\[
 \frac{T(y/q)}{T(y)}
 =\frac{4\sqrt y/\sqrt q-3}{4\sqrt y-3}
 \le q^{-1/2}.
\]

Multiplication by the positive denominator reduces this inequality to
3>=3/sqrt(q). Raising to the positive power m and multiplying by q^-1/2
proves (E3). An inactive A has only inactive supersets.

Each (k+1)-element subset is counted exactly k+1 times by removal of one
of its labels. Hence (E3), the exact excluded-label sum, and positivity give

\[
 (k+1)S_{k+1}
 =\sum_{|A|=k}\sum_{q\notin A}r_{A\cup\{q\}}
 \le\sum_{|A|=k}r_A\left(V-\sum_{q\in A}q^{-a}\right)
 =V S_k-D_k.
 \tag{E4}
\]

Only finitely many left-side terms are active; all right-side sums
converge or are finite, so there is no rearrangement of a conditional
source series. Duplicate numeric labels are distinct indices throughout.

**E5.** If V<3, every even/odd pair beginning at even k>=2 is nonnegative,
and more precisely

\[
 S_k-S_{k+1}\ge\left(1-\frac V{k+1}\right)S_k+\frac{D_k}{k+1}\ge0.
 \tag{E5}
\]

The signed level identity and discarding the other nonnegative pairs yield

\[
 \frac{H_m(x)}{T(x)^m}
 \ge1-S_1+\sum_{k\in\{2,4,6\}}
       \left[\left(1-\frac V{k+1}\right)S_k+\frac{D_k}{k+1}\right].
 \tag{E6}
\]

Any selected positive subset sums may replace S_k and D_k on this right
side. In particular, restricting their product to n_A<=N is valid for
x>=N. This retains the six-label positive pair without importing an
infinite five-label negative majorant. It also pays the label-exclusion
correction instead of treating used labels as available removal choices.

## 2. Complete marked moments using a final-label prefix

For a product cutoff t<=N and even k in {2,4,6}, define seven ordinary
and marked finite moments

\[
 C_{k,j}(a,t)=\sum_{|A|=k,n_A\le t}n_A^{-a+j/2},\quad
 D_{k,j}(a,t)=\sum_{|A|=k,n_A\le t}
 n_A^{-a+j/2}\sum_{q\in A}q^{-a},\quad 0\le j\le6.
 \tag{E7}
\]

Every label of a product with k>=2 and n_A<=N is <=N/2. Therefore the
complete primes through N/2, plus the extra 67, suffice for all these
finite moments. This assertion does not truncate the infinite V.

`exclusion_moments.py` inherits the complete label sieve and ordinary
prefix weights unchanged from `weighted_moments.py`. For chosen first
k-1 indices, let n be their product, w=n^-a, u=sum q^-a over those indices,
and let J be the interval of permitted final indices (strictly larger
than the last chosen index and with label <=floor(t/n)). The ordinary
moment contribution is

\[
 n^{-a+j/2}\sum_{q\in J}q^{-a+j/2}.
\]

The marked moment contribution is exactly

\[
 n^{-a+j/2}\left[
 u\sum_{q\in J}q^{-a+j/2}+\sum_{q\in J}q^{-2a+j/2}\right].
 \tag{E8}
\]

Both final sums are prefix differences. The recursive minimum-consecutive-
label-product pruning excludes precisely branches whose smallest possible
remaining product already exceeds the available quotient. Increasing
indices enumerate every selected subset exactly once, including the
native duplicate labels. Exact integer quotient floors enforce activation.
Ordinary and marked vectors bind their common exponent, cutoff and level.

The binomial bounds (W2)--(W4) apply termwise to either moment family,
because every static mark sum is positive. They therefore give directed
lower bounds for both selected normalized S_k and D_k. The marked weight
requires no convergence claim: all selected sums are finite.

## 3. Uniform real rectangles and entire infinite tails

**E9.** Each selected S_k and D_k is nondecreasing in x and nonincreasing
in m. The normalized kernel ratio is nondecreasing in x, including its
positive activation jump, and its ratio base is <=1. Each static weight
q^-(m+1)/2 is also nonincreasing in m. Products and positive sums preserve
these directions. For a power slab [m0,m1] and endpoint interval [L,U],
use a directed upper bound for V((m0+1)/2) and S_1(m0,U), and directed
selected lower bounds for S_k(m1,L), D_k(m1,L) in (E6). All coefficients
1-V/(k+1) are positive when the upper V<3. A positive resulting margin
proves the whole real rectangle.

For a whole tail x>=N, retain single-label products only through B=N/2
and even products through N. Put

\[
 t_1=V(a_0)-C_{1,0}(a_0,B),\quad c_0=1-t_1,\quad
 c_k=1-V(a_0)/(k+1),\quad z=x^{-1/2}.
\]

The omitted single-label normalized mass is at most t_1, since every
normalized subset mass is at most its static n^-a weight. The guards
require directed t_1>0, c_0>0, and V(a_0)<3. Let d_l,d_h be the positive
lower kernel polynomials for the normalization denominators at m0,m1,
and d_h^+ their upper bound at m1. Let Q_1 be the selected single-label
upper polynomial at m0, and P_k,P_k^D the ordinary and marked lower
polynomials at m1. Formula (E6) and the denominator directions give

\[
 \frac{H_m(x)}{T(x)^m}\ge
 c_0-\frac{Q_1(z)}{d_l(z)}+
 \frac{\sum_{k=2,4,6}[c_kP_k(z)+P_k^D(z)/(k+1)]}{d_h^+(z)}.
\]

The exact lower polynomial must be positive on the activation domain
v in [0,3/4], as guarded and proved in (W3). In particular Q_1 and every
P_k,P_k^D are nonnegative sums of positive termwise lower/upper polynomials
on this tail domain. Multiplying the last display by the positive d_l d_h^+
gives its numerator. Replacing the positive c_0 d_l d_h^+ by its lower
c_0 d_l d_h yields the further lower polynomial

\[
 N_E(z)=c_0d_l d_h-Q_1d_h^+
       +d_l\sum_{k=2,4,6}[c_kP_k+P_k^D/(k+1)].
 \tag{E10}
\]

Thus positive N_E on 0<=z<=N^-1/2 proves every real endpoint in the
whole unbounded tail and every real power in the slab. The unchanged
Bernstein coefficient identity (W8), exact dyadic subdivisions, and
entire-ball comparisons certify this continuous interval. No finite
scan is interpreted as an infinite-height proof.

The restriction V<3 is essential to this particular comparison. V(a)
diverges as a decreases to one, while any claimed positivity for all
supercritical m>1 at every endpoint would pass to the native critical
kernel by finite-sum continuity. Neither such assertion is derived here.
