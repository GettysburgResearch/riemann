# Every uniformly regular moving probability carrier gives an RH-equivalent beta energy

Status: **exact abstract moving-kernel reverse theorem, exact
two-parameter tilted-tent corollary, and an all-subpower moving-order
RH equivalence; no beta-energy estimate, proof of RH, or GRH result**

Bounded replay:
[ffps_uniform_moving_carrier_beta_criterion.py](ffps_uniform_moving_carrier_beta_criterion.py).
Canonical summary:
[ffps_uniform_moving_carrier_beta_criterion.json](ffps_uniform_moving_carrier_beta_criterion.json).

Frozen sources:

| source quartet | commit |
|---|---|
| critical moving-order phase boundary | **db37529e44bcaada9a6e39dd6cdd73c97dda8b94** |
| tilted-tent detector renormalization flow | **46ea68808e238b0c9b85050158ba149649b1b37e** |

The producer pins all eight Git blobs. No live predecessor module is
imported.

## 0. Outcome

Let

\[
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67).
\tag{0.1}
\]

For every \(X\), let \(Q_X\) be a nonnegative probability density
supported on the same interval \([0,S]\). Extend it by zero to
\(\mathbb R\), take \(D\) in the distributional sense, and assume that
the distribution \(J_X=DQ_X\) is represented by an ordinary compact
\(L^2\) function. In particular, this excludes unrecorded endpoint
atoms and forces the appropriate zero boundary traces. Define

\[
\begin{aligned}
 H_X(u)
 &=\sum_{n\le X}{\beta(n)\over\sqrt n}
 J_X(u-\log n),\\
 \mathcal E_Q(X)&=\int_{\mathbb R}|H_X(u)|^2\,du.
\end{aligned}
\tag{0.2}
\]

Then there is no growth or regularity hypothesis in the reverse
direction:

\[
\boxed{
 \mathcal E_Q(X)=X^{o(1)}
 \quad\Longrightarrow\quad
 \mathrm{RH}.}
\tag{0.3}
\]

The estimate in (0.3) is required for every sufficiently large prefix
\(X\), not merely for a sparse subsequence.

For the forward direction, suppose in addition that \(J_X\) is compact
BV and

\[
 \|J_X\|_\infty+\operatorname {Var}(J_X)=X^{o(1)}.
\tag{0.4}
\]

Then the classical Mertens consequence of RH and Abel summation give

\[
 \mathrm{RH}\quad\Longrightarrow\quad
 \mathcal E_Q(X)=X^{o(1)}.
\tag{0.5}
\]

Thus every moving probability-derivative family satisfying (0.4) is an
exact RH-equivalent energy family.

The key mechanism is elementary and uniform:

\[
\boxed{
 \widehat J_X(\alpha)
 =\alpha\int_0^S Q_X(u)e^{-\alpha u}\,du
 \ge\alpha e^{-\alpha S}
 \qquad(\alpha>0).}
\tag{0.6}
\]

No complex moving-carrier Landau theorem and no pointwise Fourier
comparison are needed.

### Tilt/order corollary

For \(a\ge1\), put

\[
 f_a(v)={ae^{av}\over e^a-1}\mathbf1_{[0,1]}(v),
 \qquad P_a=f_a*f_a.
\tag{0.7}
\]

For an integer \(m\ge1\), define the fixed-support compressed density
and its derivative

\[
 Q_{a,m}(x)=mP_a^{*m}(mx),
 \qquad J_{a,m}=DQ_{a,m}.
\tag{0.8}
\]

Let \(a=a(X)\ge1\) and \(m=m(X)\ge1\) be arbitrary schedules. The
reverse theorem gives

\[
\boxed{
 \mathcal E_{a(X),m(X)}(X)=X^{o(1)}
 \quad\Longrightarrow\quad\mathrm{RH}}
\tag{0.9}
\]

with no restriction at all on their growth. Moreover,

\[
\boxed{
 a(X)m(X)=X^{o(1)}
 \quad\Longrightarrow\quad
 \left[
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal E_{a(X),m(X)}(X)=X^{o(1)}
 \right].}
\tag{0.10}
\]

Taking \(a(X)=1\) proves, in particular,

\[
\boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal E_{m(X)}(X)=X^{o(1)}
 \quad\text{for every prescribed }m(X)=X^{o(1)}.}
\tag{0.11}
\]

This strictly supersedes the *RH-equivalence region* in the frozen
phase-boundary packet. That packet remains valid and useful as a sharp
theorem about one positive Fourier-comparison mechanism. Its spectral
boundary is not a boundary for the criterion itself.

Nothing here estimates an energy unconditionally. The new theorem
widens and clarifies the target; it does not prove the target.

## 1. Finite-prefix Laplace--Cauchy identity

Fix a real number \(\alpha>0\). Because \(Q_X\) and \(J_X\) are causal
and supported in \([0,S]\),

\[
 \operatorname {supp}H_X\subset[0,\log X+S].
\tag{1.1}
\]

Finite Fubini and translation give the exact identity

\[
\begin{aligned}
 \int_0^\infty H_X(u)e^{-\alpha u}\,du
 &=
 \widehat J_X(\alpha)
 \sum_{n\le X}{\beta(n)\over n^{1/2+\alpha}}.
\end{aligned}
\tag{1.2}
\]

Since \(J_X=DQ_X\), compact integration by parts gives

\[
 \widehat J_X(\alpha)
 =\alpha\widehat Q_X(\alpha).
\tag{1.3}
\]

Positivity, unit mass, and support in \([0,S]\) imply

\[
 e^{-\alpha S}
 \le\widehat Q_X(\alpha)\le1.
\tag{1.4}
\]

This proves (0.6), uniformly over the entire moving family.

Cauchy--Schwarz on the left side of (1.2) yields

\[
\begin{aligned}
 \left|\int_0^\infty H_X(u)e^{-\alpha u}\,du\right|
 &\le
 \mathcal E_Q(X)^{1/2}
 \left(\int_0^\infty e^{-2\alpha u}\,du\right)^{1/2}\\
 &={\mathcal E_Q(X)^{1/2}\over\sqrt{2\alpha}}.
\end{aligned}
\tag{1.5}
\]

Combining (0.6), (1.2), and (1.5) gives the explicit uniform bound

\[
\boxed{
 \left|
 \sum_{n\le X}{\beta(n)\over n^{1/2+\alpha}}
 \right|
 \le
 {e^{\alpha S}\over\alpha\sqrt{2\alpha}}\,
 \mathcal E_Q(X)^{1/2}.}
\tag{1.6}
\]

Therefore the energy premise in (0.3) implies, for every fixed
\(\alpha>0\),

\[
 A_\alpha(X):=
 \sum_{n\le X}{\beta(n)\over n^{1/2+\alpha}}
 =X^{o(1)}.
\tag{1.7}
\]

This is where the moving parameter disappears. The arithmetic partial
sum on the left is independent of \(Q_X\), while positivity gives a
carrier lower bound independent of \(X\).

## 2. Partial sums force holomorphic continuation

Fix \(\alpha>0\). For every \(\varepsilon>0\), (1.7) gives

\[
 A_\alpha(x)=O_{\alpha,\varepsilon}(x^\varepsilon).
\tag{2.1}
\]

Abel summation therefore makes

\[
 G_\alpha(s)
 =\sum_{n\ge1}{\beta(n)\over n^{1/2+s}}
\tag{2.2}
\]

converge locally uniformly in

\[
 \Re s>\alpha.
\tag{2.3}
\]

Indeed, on a compact subset of (2.3), choose a fixed
\(\varepsilon<\inf\Re(s-\alpha)\) and apply (2.1) to the coefficient
sequence

\[
 {\beta(n)\over n^{1/2+\alpha}}.
\tag{2.4}
\]

Thus \(G_\alpha\) is holomorphic on (2.3). In the initial absolute
convergence half-plane \(\Re s>1/2\), the beta source gives

\[
\boxed{
 G_\alpha(s)
 ={1-67^{-(s+1/2)}\over\zeta(s+1/2)}.}
\tag{2.5}
\]

Equivalently,

\[
 \zeta(s+1/2)G_\alpha(s)
 =1-67^{-(s+1/2)}.
\tag{2.6}
\]

Suppose \(\zeta(\rho)=0\) with \(\Re\rho>1/2\), and put

\[
 s_0=\rho-\frac12.
\tag{2.7}
\]

Choose \(0<\alpha<\Re s_0\). To make continuation across the sole zeta
pole explicit, set

\[
 F(s)=
 \left(s-\frac12\right)
 \left[
 \zeta(s+1/2)G_\alpha(s)
 -\left(1-67^{-(s+1/2)}\right)
 \right].
\tag{2.7a}
\]

This is holomorphic on \(\Re s>\alpha\), vanishes on
\(\Re s>1/2\), and hence vanishes identically. Since
\(s_0\ne1/2\), remove the prefactor and evaluate at \(s_0\). It would
give

\[
 0=1-67^{-\rho}.
\tag{2.8}
\]

But

\[
 |67^{-\rho}|=67^{-\Re\rho}<1,
\tag{2.9}
\]

so (2.8) is impossible. There is no nontrivial zeta zero to the right
of the critical line. The functional equation reflects every
nontrivial zero on the left to one on the right. This proves (0.3).

The proof uses neither a zeta-zero census nor a numerical zeta value.

## 3. Why complex carrier zeros are irrelevant here

The earlier moving-order work correctly tracked the complete carrier.
For the original \(a=1\) tilted tent,

\[
 \widehat J_m(s)
 =s\widehat P(s/m)^m
\tag{3.1}
\]

has no nonforced zero in \(0<\Re s<1\), and on each compact subset
\(K\) of that strip,

\[
 \inf_{m\ge1,\ s\in K}|\widehat J_m(s)|>0.
\tag{3.2}
\]

One can prove (3.2) from local uniform convergence

\[
 \widehat P(s/m)^m\longrightarrow e^{-\mu s}
\tag{3.3}
\]

plus finitely many nonzero initial rows.

That complex statement is true, but it is stronger than needed.
Evaluating only at the positive real point \(\alpha\) turns the carrier
into the Laplace transform of a probability density. Inequality (0.6)
then proves the uniform lower bound without locating a single complex
zero. Abel summation recovers the whole complex half-plane afterward.

This change of order is the central simplification:

\[
\text{positive real carrier}
\longrightarrow
\text{arithmetic partial sums}
\longrightarrow
\text{complex holomorphy}.
\tag{3.4}
\]

## 4. Exact two-parameter tilted family

The tilted atom in (0.7) has Laplace transform

\[
\boxed{
 \widehat f_a(s)
 ={a(e^{-s}-e^{-a})\over(1-e^{-a})(a-s)}.}
\tag{4.1}
\]

The value at \(s=a\) is removable. Since \(P_a=f_a*f_a\),

\[
 \widehat J_{a,m}(s)
 =s\,\widehat f_a(s/m)^{2m}.
\tag{4.2}
\]

Besides the forced simple derivative zero at \(s=0\), its nonforced
zeros are

\[
 s=m(a-2\pi i k),
 \qquad k\in\mathbb Z\setminus\{0\}.
\tag{4.3}
\]

Each zero in (4.3) has multiplicity \(2m\). For \(a\ge1\), these lie
on \(\Re s=am\ge1\). This supplies an
independent complex-carrier check of the real positivity argument.

On the Fourier axis,

\[
\boxed{
 |\widehat f_a(it)|^2
 =
 {1+\dfrac{4e^{-a}}{(1-e^{-a})^2}\sin^2(t/2)
 \over
  1+t^2/a^2}.}
\tag{4.4}
\]

Consequently

\[
 {1\over1+t^2/a^2}
 \le|\widehat f_a(it)|^2\le1.
\tag{4.5}
\]

The upper bound is also the characteristic-function bound. Algebraically,
it follows from

\[
 {4e^{-a}\over(1-e^{-a})^2}\sin^2(t/2)
 \le {t^2\over a^2}.
\tag{4.6}
\]

The order-\(m\) derivative weight is

\[
\boxed{
 w_{a,m}(t)
 =t^2|\widehat P_a(it/m)|^{2m}
 =t^2|\widehat f_a(it/m)|^{4m}.}
\tag{4.7}
\]

The exponent bookkeeping in (4.7) is load-bearing: if
\(R_a=|\widehat f_a|^2\), then the last factor is \(R_a^{2m}\), not
\(R_a^{4m}\).

Equation (4.5) gives the exact global floor

\[
\boxed{
 w_{a,m}(t)
 \ge t^2
 \left(1+{t^2\over a^2m^2}\right)^{-2m}.}
\tag{4.8}
\]

This recovers the positive Fourier-comparison route as a separate
corollary, but (0.3) is stronger and simpler.

## 5. Uniform BV cost and the forward implication

Extend \(f_a\) by zero outside \([0,1]\). Its distributional derivative is

\[
 Df_a
 =af_a(v)\,dv
 +{a\over e^a-1}\delta_0
 -{ae^a\over e^a-1}\delta_1.
\tag{5.1}
\]

Therefore

\[
\boxed{
 \|Df_a\|_{\rm TV}
 =a\left(1+\coth{a\over2}\right).}
\tag{5.2}
\]

Since \(P_a=f_a*f_a\),

\[
 \|D^2P_a\|_{\rm TV}
 \le
 a^2\left(1+\coth{a\over2}\right)^2.
\tag{5.3}
\]

Convolution by a probability density contracts measure variation.
More explicitly,

\[
 D^2Q_{a,m}
 =m^3
 \left[(D^2P_a)*P_a^{*(m-1)}\right](m\,\cdot).
\tag{5.3a}
\]

Total variation under the displayed dilation contributes a factor
\(m^{-1}\). The compressed dilation in (0.8) therefore gives

\[
\boxed{
 \operatorname {Var}(J_{a,m})
 \le
 m^2a^2
 \left(1+\coth{a\over2}\right)^2.}
\tag{5.4}
\]

The same right side bounds \(\|J_{a,m}\|_\infty\) up to an absolute
constant, because the compact kernel vanishes outside its support.

Assume RH. The standard Mertens implication for the complete beta source
is

\[
 B(y):=
 \sum_{n\le y}{\beta(n)\over\sqrt n}
 =O_\delta(y^\delta)
\tag{5.5}
\]

for every fixed \(\delta>0\). Abel summation of the moving field against
(5.5) gives

\[
 \sup_u|H_X(u)|
 \ll_\delta
 m^2a^2
 \left(1+\coth{a\over2}\right)^2
 X^\delta.
\tag{5.6}
\]

Its support has length \(O(1+\log X)\), so

\[
\boxed{
 \mathcal E_{a,m}(X)
 \ll_\delta
 (1+\log X)X^{2\delta}
 m^4a^4
 \left(1+\coth{a\over2}\right)^4.}
\tag{5.7}
\]

For \(a\ge1\), the hyperbolic factor is uniformly bounded. If
\(a(X)m(X)=X^{o(1)}\), choose \(\delta\) after a prescribed final
exponent. Equation (5.7) proves the forward half of (0.10).

## 6. What the phase boundary now means

The frozen phase packet proved a sharp certified region for the
pointwise comparison

\[
 |\widehat B_{\infty}(t)|^2
 \le X^{o(1)}w_{m(X)}(t)
\tag{6.1}
\]

inside the critical frequency window. That theorem remains exact. The
present packet proves that (6.1) is not necessary for RH equivalence.

The distinction is:

| question | answer |
|---|---|
| When does this particular positive Fourier comparison close? | the frozen logarithmic phase region |
| When is the moving beta energy itself RH-equivalent? | every subpower order schedule |
| Is the energy estimate known for any new moving schedule? | no |

Thus the earlier boundary is a **method phase transition**, not an
arithmetic truth phase transition.

This is useful beyond correcting terminology. Future detector searches
need not optimize spectral domination merely to preserve equivalence.
They can choose a moving positive density for analytic convenience,
provided its derivative cost stays subpower.

## 7. Scope and firewalls

| statement | grade |
|---|---|
| finite-prefix Laplace identity (1.2) | **PROVED EXACT** |
| universal real carrier floor (0.6) | **PROVED EXACT** |
| energy to weighted beta partial sums (1.6) | **PROVED EXACT** |
| Abel holomorphy and RH reverse theorem | **PROVED** |
| arbitrary-growth reverse theorem for the tilted family | **PROVED** |
| all-subpower tilt/order RH equivalence | **PROVED** |
| unconditional moving beta-energy estimate | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

The hypotheses that must be preserved are:

1. the estimate holds for every large prefix \(X\);
2. \(Q_X\) is nonnegative, has mass one, and has uniformly bounded
   causal support;
3. the detector is its derivative;
4. the source remains the complete duplicate-\(67\) beta source;
5. forward equivalence additionally needs subpower BV cost.

Dropping positivity destroys the elementary carrier floor. Dropping
normalization permits an \(X\)-dependent scalar to fake a small energy.
Dropping uniform support can make the factor \(e^{\alpha S(X)}\)
arithmetic-sized. These are structural conditions, not presentation
choices.

No external novelty or priority is claimed without a dedicated
literature comparison.

## 8. Bounded replay

The producer:

- checks all eight frozen Git blobs;
- evaluates four tilts, four orders, and three fixed Laplace points;
- verifies the exact positive-real probability floor on four rows;
- checks convergence to the fixed-tilt large-order carrier on twelve
  bounded rows;
- evaluates no beta sum, zeta zero, numerical zeta value, prime, curve,
  random sample, contour, or quadrature.

The sampled rows authenticate formulas and serialization only. The
theorems are the analytic arguments above.

~~~text
python -B research/l-families/atlas/function_field/ffps_uniform_moving_carrier_beta_criterion.py --check
python -O -B research/l-families/atlas/function_field/ffps_uniform_moving_carrier_beta_criterion.py --check
python -B -m unittest tests.test_ffps_uniform_moving_carrier_beta_criterion
python -O -B -m unittest tests.test_ffps_uniform_moving_carrier_beta_criterion
python -m ruff check research/l-families/atlas/function_field/ffps_uniform_moving_carrier_beta_criterion.py tests/test_ffps_uniform_moving_carrier_beta_criterion.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_uniform_moving_carrier_beta_criterion.py tests/test_ffps_uniform_moving_carrier_beta_criterion.py
~~~
