# Fixed-planar last-coordinate support and a finite-activation obstruction

This is a proof-only consequence of the literal twenty source moments in
`ALL_HORIZON_THREE_PRIME_SOURCE_MOMENTS.md`. It concerns a prescribed
oriented planar path and arbitrary linear combinations of those source
moments. It does not assert that a gradient of the original physical
quadratic at H30 or any other horizon satisfies one of the sign conditions
below. No new numerical computation is used.

## 1. The actual fixed-planar control space

Fix a continuous coordinatewise nondecreasing planar path from (0,0) to
(1,1). Remove pauses and use its total planar increment s=u+v in [0,2]
as parameter. The functions u and v are nondecreasing and 1-Lipschitz,
and du+dv=ds. Vertical segments of the third coordinate w may be inserted
at any point of this same oriented planar path, including either endpoint.

After the exact R dw gauge from the twenty-moment note, a linear source
functional has a fixed endpoint and planar contribution plus

\[
 \mathcal J(w)=\int w\,dA+\int w^2\,dB,\qquad
 dA=P_1\,du+Q_1\,dv,\quad dB=P_2\,du+Q_2\,dv.             \tag{1.1}
\]

Here A and B are finite signed, atomless measures. They have bounded
densities with respect to ds, but **A need not be absolutely continuous
with respect to B**, even when B is a positive measure. In particular,
the vanishing of the quadratic coefficient does not remove the linear
cost on that portion of the path.

The admissible controls are nondecreasing functions w:[0,2]->[0,1],
identified up to atomless-measure null sets. Their one-sided endpoint
values need not be 0 and 1: an initial vertical segment supplies the
missing initial increase, and a final vertical segment supplies the
remaining terminal increase. Every such control has an actual continuous
BV realization by completing its monotone graph with vertical segments.
Thus no convex mixture of observed fields is being substituted for an
actual path.

Every control can equivalently be written, up to the irrelevant values
at its countably many jumps, as

\[
 w(s)=\int_{[0,2]}\theta_t(s)\,d\mu(t),\qquad
 \theta_t(s)={\bf1}_{s>t},                              \tag{1.2}
\]

where mu is a probability measure. Its masses at 0 and 2 represent initial
and terminal activation. Conversely every such probability measure gives
an admissible control. For an atomless finite signed measure C, Fubini gives

\[
 \int w\,dC=\int_{[0,2]} C((t,2])\,d\mu(t).             \tag{1.3}
\]

The tail t->C((t,2]) is continuous, including the endpoint values.

The control class is compact for the integrals in (1.1). To see this
without a density assumption relative to B, select a subsequence converging
at every rational s. Monotonicity determines a limit and gives convergence
at every continuity point of that limit. Its discontinuities are countable;
the measure |A|+|B| has no atoms. Dominated convergence therefore gives
convergence of both integrals in (1.1). In particular a minimum exists,
even if B changes sign. The convex and concave cases below give additional
structure, not an exhaustive classification of signed B.

## 2. Nonpositive quadratic measure: one activation is exact

Suppose B<=0 as a measure along this fixed planar path. Since 0<=w<=1,

\[
 \int(w^2-w)\,dB\ge0,\qquad
 \mathcal J(w)\ge\int w\,d(A+B).                        \tag{2.1}
\]

Using (1.3), the right side is a probability average of the continuous
tail costs of A+B. For a threshold control theta_t, equality holds in
(2.1). Consequently

\[
 \min_w \mathcal J(w)=\min_{0\le t\le2}(A+B)((t,2]).     \tag{2.2}
\]

The minimum is attained by raising w from 0 to 1 once at a minimizing
point on the fixed planar path. The initial and final activation orders
are included. Pointwise inequalities P2<=0 and Q2<=0 on the unit square
are sufficient for this hypothesis, but the hypothesis in (2.2) only
concerns the actual combined measure on the prescribed path. The case
B=0 includes the earlier H25 one-activation linear-support reduction.

This is a statement about a linear source support functional. It does not
turn a single activation into a general quadratic-energy minimizer.

## 3. Nonnegative quadratic measure: a convex variational problem

Suppose B>=0. Then (1.1) is convex on the compact convex control class.
A control w* minimizes it if and only if

\[
 \int(v-w_*)\,dA+2\int w_*(v-w_*)\,dB\ge0
 \quad\hbox{for every admissible }v.                    \tag{3.1}
\]

Necessity follows by differentiating along the admissible segment from
w* to v. Sufficiency and a useful gap bound follow from the exact identity

\[
 \mathcal J(v)-\mathcal J(w_*)
 =\int(v-w_*)\,d\Lambda_*+\int(v-w_*)^2\,dB,
 \qquad d\Lambda_*=dA+2w_*\,dB.                        \tag{3.2}
\]

In particular all minimizers agree B-almost everywhere. They need not be
unique on B-null sets. Formula (3.1), rather than an assumed pointwise
target, covers a linear cost carried by such sets.

There is also an exact tail formulation. If mu* represents w* as in
(1.2), then (3.1) is equivalent to

\[
 \int w_*\,d\Lambda_*=\min_t\Lambda_*((t,2]),            \tag{3.3}
\]

or equivalently to mu* being supported on the minimizing set of this
continuous tail function. Indeed the minimum of the linear functional
v->integral v dLambda* on the control class is its minimum over threshold
controls, by (1.3). This is an implicit optimality criterion because
Lambda* itself depends on w*.

Only under the additional hypotheses A<<B and
f=dA/dB in L2(B) may one complete the square as the usual weighted
isotonic projection:

\[
 \mathcal J(w)=\int(w+f/2)^2\,dB-\tfrac14\int f^2\,dB.   \tag{3.4}
\]

The restrictions of bounded monotone controls form a closed convex set
in L2(B), as follows again from the subsequence argument above. This
justifies (3.4) under its stated hypotheses; it does not justify discarding
the singular part of A in general.

For a concrete warning, on [0,1] take

\[
 dA=-2{\bf1}_{[0,1/2]}\,ds,\qquad
 dB={\bf1}_{(1/2,1]}\,ds.                              \tag{3.5}
\]

The nondecreasing control w=1 has cost -1/2 and is a minimizer. To check
this, put t equal to the left limit of w at 1/2: its first-half integral
is at most t/2 and its second-half square integral is at least t^2/2,
so the cost is at least -t+t^2/2>=-1/2. Ignoring A on the B-null half
would instead select the zero target and miss the minimum. Both measures
in (3.5) are atomless.

## 4. Two literal source moments prevent finite-activation compression

In the displayed twenty-moment basis take coefficient 1 on

\[
 M_6=\int w^2\,du,\qquad M_{13}=\int u^2\,dw,           \tag{4.1}
\]

and zero on every other moment. Prescribe the planar path u=v=s for
0<=s<=1. Integration by parts, including the endpoint vertical segments,
gives the exact identity

\[
 M_6+M_{13}
 =1+\int_0^1(w(s)^2-2s w(s))\,ds
 =\frac23+\int_0^1(w(s)-s)^2\,ds.                       \tag{4.2}
\]

The diagonal control w=s is admissible and is the unique minimizing
control up to ds-null sets. Its two moments are both 1/3. Every finite
activation staircase differs from s on a set of positive measure and
therefore has strictly larger sum in (4.2). It cannot reproduce even
these two moments, hence cannot reproduce all twenty source moments on
the same planar path.

This does not contradict `NATIVE_FOUR_ACTIVATION_COMPRESSION.md`:
that theorem preserves the six H25 moment coordinates on a fixed planar
path. The new quadratic dependence on w in (4.1) is absent from the
six-coordinate compression argument. Conversely, (4.2) is not a claim
that any given horizon's physical gradient equals this two-moment
functional, nor that its physical readout detects both moments separately.

## 5. Exact penalty for at most k activations

Let k>=1. A staircase with at most k positive w-jumps has a set of levels

\[
 0=q_0<q_1<\cdots<q_j=1,\qquad j\le k.                 \tag{5.1}
\]

Initial or final endpoint jumps are allowed; some endpoint levels may
therefore be used only at a single point. For any assignment of those
levels to a monotone staircase, the pointwise squared error is at least
the squared distance from s to the nearest level. On the gap between
q_(i-1) and q_i, whose length is Delta_i, the integral of that nearest-level
error is

\[
 2\int_0^{\Delta_i/2}x^2\,dx=\frac{\Delta_i^3}{12}.
                                                                    \tag{5.2}
\]

Since the gaps sum to 1, convexity of x^3 gives

\[
 \int_0^1(w-s)^2\,ds
 \ge\frac1{12}\sum_{i=1}^j\Delta_i^3
 \ge\frac1{12j^2}\ge\frac1{12k^2}.                    \tag{5.3}
\]

Equality for the k-activation problem is attained by the levels q_i=i/k
and jumps at s=(i-1/2)/k. These jumps have an actual continuous realization
as vertical w-segments inserted into u=v=s. Thus the exact optimum of the
two-moment functional among such staircases is

\[
 \boxed{\ \min_{\le k\ \mathrm{activations}}(M_6+M_{13})
       =\frac23+\frac1{12k^2}\ }.                      \tag{5.4}
\]

No fixed number of activations can reproduce the full twenty-moment
diagonal source on this same planar path. Increasing k approximates it
with the displayed exact penalty; no statement about a physical
quadratic-energy penalty or an unrestricted change of planar path is
inferred.

## 6. The obstruction is already a literal H50 source functional

The underlying half-source has the exact squarefree coefficients

\[
 \Lambda_2=-u/2,\qquad \Lambda_5=-w/2,\qquad
 \Lambda_{10}=uw/4.                                    \tag{6.1}
\]

Write its raw ordered record as
\(B(n,m)=2\int\Lambda_m\,d\Lambda_n\), before physical
\(1/\sqrt{nm}\) weighting or equal-ratio collection. The two records
with products \(10\cdot5=50\) and \(10\cdot2=20\) satisfy

\[
\begin{aligned}
 B(10,5)&=-\tfrac14\int(w^2\,du+uw\,dw)
         =-\frac{1+M_6}{8},\\
 B(10,2)&=-\tfrac14\int(uw\,du+u^2\,dw)
         =-\frac{1+M_{13}}8.                            \tag{6.2}
\end{aligned}
\]

Indeed the two endpoint identities are
\(\int uw\,dw=(1-M_6)/2\) and
\(\int uw\,du=(1-M_{13})/2\). Thus

\[
 M_6+M_{13}=-8\,[B(10,5)+B(10,2)]-2.                  \tag{6.3}
\]

Both records are retained by the literal source at horizon H50. Any
same-planar replacement preserving that complete raw record array must
preserve (6.3), and therefore cannot use finitely many w activations for
the diagonal source path. If S is the sum of these two records, then for
at most k activations
\[
 S_{\rm staircase}-S_{\rm diagonal}\le-\frac1{96k^2},    \tag{6.4}
\]
with equality for the optimal staircase of §5. This is not claimed to be
the first horizon where compression fails. The next section checks the
physical aliases separately; a literal-record argument alone would not
justify that transfer.

## 7. Complete H50 physical aliases still detect the obstruction

Keep the same fixed planar path u=v=s. Let C_rho be the actual coefficient
of the reduced ratio rho in the H50 physical observation, and remove
only its common nonzero factor by writing S_rho=sqrt(rho) C_rho for the
integer ratios used below. The original physical weighting gives

\[
 S_\rho=\sum_{d^2\rho\le50}\frac{B(d\rho,d)}d.           \tag{7.1}
\]

Every displayed d is supported on primes 2,3,5. At ratio2 the complete
list is d=1,2,3,4,5; at ratio5 it is d=1,2,3. Higher prime powers are
therefore retained, not replaced by a squarefree-only list.

In addition to (6.1), the exact local half-source has
\(\Lambda_4=-1/2+3u/8\), \(\Lambda_8=-u/16\),
\(\Lambda_3=-v/2\), \(\Lambda_6=uv/4\), and
\(\Lambda_{15}=vw/4\). Literal integration gives

| Ratio | d | Raw ordered record \(B(d\rho,d)\) on \(u=v=s\) |
| --- | ---: | --- |
| 2 | 1 | \(-1\) |
| 2 | 2 | \(-3/16\) |
| 2 | 3 | \(-1/6\) |
| 2 | 4 | \(5/128\) |
| 2 | 5 | \(-(1+M_6)/8\) |
| 5 | 1 | \(-1\) |
| 5 | 2 | \(-(1+M_{13})/8\) |
| 5 | 3 | \(-(1+M_{13})/8\) |

The first four ratio2 records depend only on the fixed planar path.
For example \(B(8,4)=\int(1/16-3u/64)\,du=5/128\).
The last ratio5 identity uses v=u, so
\(\int v^2\,dw=M_{13}\). Substituting the required factors 1/d yields

\[
\begin{aligned}
 S_2&=-1-\frac3{32}-\frac1{18}+\frac5{512}
               -\frac{1+M_6}{40}
      =-\frac{26831}{23040}-\frac{M_6}{40},\\
 S_5&=-1-\frac{1+M_{13}}{16}-\frac{1+M_{13}}{24}
      =-\frac{53}{48}-\frac{5M_{13}}{48}.              \tag{7.2}
\end{aligned}
\]

Thus these two coalesced physical coefficients recover both moments on
this fixed planar path. If delta denotes a difference from the diagonal
source, then

\[
 M_6+M_{13}-\frac23
       =-40\,\delta S_2-\frac{48}{5}\,\delta S_5.       \tag{7.3}
\]

Distinct rational-ratio Mellin frequencies are linearly independent:
after collecting equal frequencies, differentiating a vanishing finite
exponential sum produces a Vandermonde system. Equality in the original
observation space also gives this equality of finite sums, because its
measure has positive density on an interval and the sum is analytic.
Consequently equality of the actual H50 observed field forces equality
of the two coefficients in (7.2). Equations (4.2) and (7.3) show that no
finite-activation replacement on this same planar path can preserve that
physical field. This conclusion does not rely on any measured atlas rank.

There is also a nonnumerical field-distance bound. On the finite-dimensional
H50 observation space the coefficient functional
\[
 L(\delta F)=-40\sqrt2\,\delta C_2
                 -\frac{48}{5}\sqrt5\,\delta C_5
\]
has a finite positive operator norm \(K_L\) in the original observation
norm. Combining (5.3) and (7.3) gives
\[
 \|F_{\rm staircase}-F_{\rm diagonal}\|
       \ge\frac1{12K_L k^2}.                          \tag{7.4}
\]
No value of \(K_L\) is estimated here. This is distance between fields,
not a positive difference of their squared norms or an assertion that
the diagonal minimizes the original physical energy. The argument remains
restricted to the prescribed planar path; it does not rule out changing
that planar path while preserving the observation.
