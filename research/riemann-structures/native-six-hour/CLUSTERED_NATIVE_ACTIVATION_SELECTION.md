# A fixed activation schedule improves every tight three-prime cluster

The original compact logarithmic kernel selects a nonuniform native path
on an explicit open family of prime configurations. This is a constructive
selection theorem for the L-102707 primitive and its original ratio norm.
It uses all eight factor allocations, the physical factor 1/sqrt(K), and
the original measure nu=|kappahat(t)|^2 dt/(2pi). It does not assert a full
principal-family bound or an identification with post-renewal gamma.

Let p1<p2<p3 be odd primes, K=p1*p2*p3, and assume

\[
 p_1p_2/p_3>\sqrt8,\qquad 1<p_3/p_1\le\sqrt2.
 \tag{1}
\]

The native schedules `(u1,u2,u3)=(s,s,s)` and `(s,s^2,s)` have activation
vectors u=(1/3,1/3,1/3) and q0=(1/4,1/2,1/4), respectively. They have the
same endpoints and signed product-current observation. Nevertheless their
original ratio energies obey the strict, quantitative inequality

\[
 E(u)-E(q_0)>\frac{17}{720K}\log(p_3/p_1)>0.
 \tag{2}
\]

The fixed powers 1:2:1 were obtained from the analytic cluster limit, not
fitted separately to the bounded fixtures. This contrasts with the already
proved widely separated three-prime regime, where uniform activation is
the unique minimizer. Source endpoint invariance does not select an
observation-independent schedule.

## 1. Exact kernel cusp from the native primitive

Put L=log2 and z=sqrt2. The authenticated L-102880 primitive has kappa(u)
supported on [0,3L], with the following formulas in y=exp(u):

```
[1,2):  8-4 sqrt(y)
[2,4): -8(1+sqrt2)+4 sqrt2 sqrt(y)
[4,8):  8 sqrt2-2 sqrt(y).
```

Use Gamma(delta)=integral kappa(u)kappa(u-delta)du. For 0<=delta<=L,
the five nonempty intervals are [delta,L], [L,L+delta], [L+delta,2L],
[2L,2L+delta], [2L+delta,3L]. Integrating the two elementary factors on
each interval gives the exact expression

\[
\begin{split}
 \Gamma(\delta)={}&\Gamma_0-(576+256z)\delta\\
 &+(288+192z)(e^{\delta/2}-1)
 -(576+192z)(e^{-\delta/2}-1),\\
 \Gamma_0={}&(384+128z)L-288.
\end{split}\tag{3}
\]

The replay reconstructs (3), at rational exponential arguments, by an
independent nine-overlap integration of the frozen primitive. Logarithms
are reduced to exact prime valuations before comparing the two formulas;
agreement is algebraic, not numerical quadrature.

The right cusp slope is -A, where

\[
 A=144+64\sqrt2.
 \tag{4}
\]

It also equals one half of the sum of squared jumps of kappa, including
its two support endpoints. Those jumps are
`4, -8-4sqrt2, 4+8sqrt2, -4sqrt2`. This is an independent check of the
normalization. From (3),

\[
 \Gamma''(\delta)=\tfrac14\big((288+192z)e^{\delta/2}
                 -(576+192z)e^{-\delta/2}\big).
\]

This derivative is increasing from -72 to 48 on [0,L]. Therefore

\[
 |\Gamma(\delta)-\Gamma_0+A\delta|\le36\delta^2
 \qquad(0\le\delta\le L).
 \tag{5}
\]

Evenness supplies the two-sided cusp. No differentiability at zero is
incorrectly assumed.

## 2. All eight source factors and the exact energy difference

For any monotone primewise path from zero to one, define

\[
 q_j=\int_0^1u'_j(s)\prod_{i\ne j}u_i(s)ds,
 \qquad q_j\ge0,\quad\sum_jq_j=1.
 \tag{6}
\]

The actual `2 ds` primitive gives, at the factor indexed by S subset
{1,2,3}, stripped coefficient `-sum_{j in S}q_j/4`. Thus the empty
factor is zero, the full factor is -1/4, singleton coefficients are
-q_j/4, and complementary pairs have coefficients -(1-q_j)/4.
All are divided by sqrt(K) once in the physical field.

The first condition in (1) separates every two different cardinality
bands by a factor exceeding sqrt8. Their frequency differences exceed
log8, so they are orthogonal in the original nu norm. Within either
three-element band put

\[
 H_{ij}=\Gamma(2\log(p_i/p_j)).
\]

The complete energy, including the full-factor mode, is exactly

\[
 E(q)=\frac{\Gamma_0+q^THq+(\mathbf1-q)^TH(\mathbf1-q)}{16K}.
 \tag{7}
\]

No mean mode or literal factor is deleted. Let
a=log(p2/p1), b=log(p3/p2), w=a+b. Substitution in (7) gives

\[
 E(u)-E(q_0)=
 \frac{-3\Gamma_0+4\Gamma(2a)+4\Gamma(2b)-5\Gamma(2w)}{576K}.
 \tag{8}
\]

By (5), the numerator is at least

\[
 2Aw-36\{16a^2+16b^2+20w^2\}
 \ge2w(A-648w).
 \tag{9}
\]

Since w<=L/2, sqrt2>7/5 and log2<7/10 give
`A-648w >= A-324log2 > 34/5`. Equations (8)--(9) prove (2).
The theorem does not require comparable adjacent gaps.

## 3. The unique optimizer and a cofinal prime family

The constrained energy is strictly convex. Indeed H is the Gram matrix
of three distinct exponentials in a nonzero absolutely continuous measure;
a finite exponential polynomial cannot vanish on a set of positive
Lebesgue measure unless all coefficients vanish. Hence H is positive
definite and (7) has a unique minimizer on the simplex.

For the asymptotic location, additionally suppose a/b stays in a fixed
compact subinterval of (0,infinity), and w tends to zero. Write

\[
 H=\Gamma_0\mathbf1\mathbf1^T-2A D+R,
 \quad D_{ij}=|\log p_i-\log p_j|,
 \quad |R_{ij}|\le144w^2.
 \tag{10}
\]

On the simplex the leading minimization is the maximization of
`q^TDq+(1-q)^TD(1-q)`. Its loss from q0 is exactly

\[
 4a(q_1-1/4)^2+4b(q_3-1/4)^2.
 \tag{11}
\]

The Hessian in the coordinates q1,q3 is therefore bounded below by a
positive constant times w; the gradient perturbation from R is O(w^2).
Solving the two-variable stationary equation gives

\[
 q_*= (1/4,1/2,1/4)+O(w).
 \tag{12}
\]

For small w this stationary point is interior and hence the unique simplex
minimizer. The constants in (12) are uniform under the stated comparability
condition. Merely knowing a,b tend to zero, without that condition, is not
used as a conditioning estimate.

Such prime triples exist cofinally without a shrinking-interval theorem.
For each fixed positive epsilon_j tending to zero, ordinary PNT supplies
primes in each of

```
[X, (1+epsilon_j^2)X],
[(1+epsilon_j)X, (1+epsilon_j+epsilon_j^2)X],
[(1+2epsilon_j)X, (1+2epsilon_j+epsilon_j^2)X]
```

once X is sufficiently large for that fixed j. Choose X_j successively
larger than those thresholds. Then a/b tends to one, w tends to zero,
and the band-separation condition holds. This is a diagonal sequence of
fixed-relative-interval consequences of PNT, not a uniform shrinking-window
claim. PNT is the only external existence input; the selection theorem
itself is an elementary implication for each triple.

Along this sequence,

\[
 E(u)-E(q_0)\sim\frac{A w}{288K},\qquad
 E(q)\sim\frac{3\Gamma_0}{8K}
 \quad\text{for each fixed activation }q.
 \tag{13}
\]

The last displayed energy asymptotic is independent of q because all
within-band frequencies coalesce. The improvement is positive but
absolutely small, and its relative size tends to zero. No numerical
conditioning or global source-moment lower bound follows.

## 4. Bounded proof replay and scope

The fixed bounded controls are (71,73,79), already present in the native
zero chart, and (41,43,47). The replay verifies primality, both conditions
in (1), all eight physical modes, the full Gram energy versus (7), the
exact five-interval formula versus the independent nine-overlap kernel,
and the strict rational enclosure for (2). No optimizer is fitted to
either fixture and no new prime search is performed. A third bound-only
control checks the symbolic rational constant in (9).

The source-defined power paths preserve the primitive endpoint and signed
product current. They change the original ratio observation. The result
selects between admissible source paths for this particular observation;
it does not authorize deleting a source sector, changing the physical
measure, or treating independently optimized tuples as one global path.
The separate global-horizon experiment addresses that last question.

Validation is delegated to the coordinating agent. The bounded certificate
is not offered as the proof of the cofinal assertion, whose argument is
given above.
