# Rational rotations: the uniform local-degree gate

Status: **proposed exact local theorem; external novelty unreviewed**
Issue: [#764](https://github.com/gfreund123/riemann/issues/764)
Claim labels: GLO764.PERIODIC_DFT_MINIMAL_ORDER,
GLO764.SAMPLED_MODE_PERSISTENCE,
GLO764.ABSOLUTE_UNIFORM_DEGREE_GATE,
GLO764.FIXED_BRANCH_UNIFORM_DEGREE_GATE, and
GLO764.ABSOLUTE_FIRST_POWER_FULL_SPECTRUM

## Scientific firewall

The earlier rational-rotation census proved rationality one orbit at a time.
Its displayed period can grow with the angle denominator, but that alone does
not prove that the **reduced** denominator grows.  Integer powers already show
why: their symmetric-power expansion has at most \(k+1\) modes even when the
orbit period is arbitrarily large.

This packet closes that exact logical gap.  For a fixed exponent with positive
real part, reduced local degrees over all rational rotations are uniformly
bounded precisely in the polynomial exponent chambers:

\[
\begin{array}{c|c}
\text{transform}&\text{uniformly bounded exactly when}\\ \hline
|u_r|^\lambda&\lambda\in2\mathbb Z_{>0},\\
P_{\lambda,J}(u_r)&\lambda\in\mathbb Z_{>0}.
\end{array}
\tag{0.1}
\]

The proof is a compact sampling theorem, not an inference from a finite
experiment.  It concerns one determinant-one, unramified, tempered rank-two
recurrence.  It does not construct a prime-indexed family, global Euler
product, ramified factors, completion, functional equation, automorphic lift,
motive, infinite-dimensional parent, explicit formula, or zero theorem.  It
has no RH or GRH consequence.

## 1. Rational-rotation family and degree

Let

\[
1\leq a<b,\qquad \gcd(a,b)=1,\qquad
\theta=\frac{a\pi}{b},
\tag{1.1}
\]

and

\[
u_0=1,\qquad u_1=2\cos\theta,\qquad
u_{r+2}=2\cos\theta\,u_{r+1}-u_r.
\tag{1.2}
\]

Then

\[
u_r=\frac{\sin((r+1)\theta)}{\sin\theta}.
\tag{1.3}
\]

For \(\operatorname{Re}\lambda>0\), zeros are assigned the value zero.  Define

\[
A_\lambda(y)=
\begin{cases}
\exp(\lambda\log|y|),&y\neq0,\\
0,&y=0,
\end{cases}
\tag{1.4}
\]

and, for a fixed \(J\in\mathbb Z\),

\[
P_{\lambda,J}(y)=
\begin{cases}
\exp(\lambda\log y),&y>0,\\
\exp\!\left(\lambda(\log|y|+(2J+1)\pi i)\right),&y<0,\\
0,&y=0.
\end{cases}
\tag{1.5}
\]

Both coefficient sequences are periodic and hence have rational ordinary
generating functions.  Write \(d_{\rm abs}(\lambda;a,b)\) and
\(d_J(\lambda;a,b)\) for their minimal eventual constant-coefficient
recurrence orders, equivalently the degrees of their reduced denominators.

The restriction \(\operatorname{Re}\lambda>0\) is essential here.  It makes
the functions in (1.4)--(1.5) continuous at their zeros and avoids the
separate \(0^0\) convention spectrum.

## 2. Periodic sequences: reduced degree is Fourier support

Let \(s:\mathbb Z/q\mathbb Z\to\mathbb C\), put
\(\zeta_q=e^{2\pi i/q}\), and use the normalized discrete Fourier transform

\[
\widetilde s_q(k)
=\frac1q\sum_{n=0}^{q-1}s(n)\zeta_q^{-kn}.
\tag{2.1}
\]

Fourier inversion gives

\[
s(n)=\sum_{k=0}^{q-1}\widetilde s_q(k)\zeta_q^{kn}.
\tag{2.2}
\]

**Lemma (GLO764.PERIODIC_DFT_MINIMAL_ORDER).**  The periodic sequence
\(s(0),s(1),\ldots\) has reduced denominator

\[
\prod_{\widetilde s_q(k)\neq0}(1-\zeta_q^kT)
\tag{2.3}
\]

and minimal recurrence order

\[
d(s)=\#\{k:\widetilde s_q(k)\neq0\}.
\tag{2.4}
\]

### Proof

Substituting (2.2) into the generating series gives a partial-fraction
expansion with one term
\(\widetilde s_q(k)/(1-\zeta_q^kT)\) for each mode.  The roots
\(\zeta_q^k\) are distinct, and a retained residue is nonzero.  Therefore no
retained linear factor cancels, which proves (2.3)--(2.4).
\(\square\)

A cyclic shift, multiplication of the sample index by a unit modulo \(q\),
or multiplication of all values by a nonzero scalar merely permutes or
rescales the Fourier coefficients.  None changes their support cardinality.

## 3. A sampling lemma that retains arbitrarily many modes

Let \(f:\mathbb R/\mathbb Z\to\mathbb C\) be continuous, with Fourier
coefficients

\[
\widehat f(k)=\int_0^1 f(x)e^{-2\pi ikx}\,dx.
\tag{3.1}
\]

Sample the \(q\)-grid:

\[
s_q(n)=f(n/q),\qquad
\widetilde f_q(k)=
\frac1q\sum_{n=0}^{q-1}f(n/q)e^{-2\pi ikn/q}.
\tag{3.2}
\]

For each fixed \(k\), the second expression is a Riemann sum, so

\[
\widetilde f_q(k)\longrightarrow\widehat f(k)
\qquad(q\to\infty).
\tag{3.3}
\]

**Lemma (GLO764.SAMPLED_MODE_PERSISTENCE).**  If \(f\) has infinitely many
nonzero Fourier coefficients, then

\[
\sup_{q\geq1}\#\{k\bmod q:\widetilde f_q(k)\neq0\}=\infty.
\tag{3.4}
\]

Consequently the minimal recurrence orders of the periodic grid samples are
unbounded.

### Proof

Fix \(M\).  Choose distinct integers
\(k_1,\ldots,k_M\) with \(\widehat f(k_j)\neq0\).  For all sufficiently large
\(q\), these integers are distinct modulo \(q\).  By (3.3), after increasing
\(q\) again if necessary, every \(\widetilde f_q(k_j)\) is nonzero.  Thus the
sampled Fourier support has size at least \(M\).  Since \(M\) was arbitrary,
(3.4) follows, and Section 2 converts support size to recurrence order.
\(\square\)

The lemma makes no claim about a quantitative rate in \(q\).  It also avoids
an invalid argument from growing raw periods: it works directly with
noncancelling modes of the reduced denominator.

## 4. Exactly which power-sine functions have finite spectrum?

For the absolute chamber, consider the continuous \(\pi\)-periodic function

\[
f_\lambda(t)=
\begin{cases}
\exp(\lambda\log|\sin t|),&\sin t\neq0,\\
0,&\sin t=0.
\end{cases}
\tag{4.1}
\]

For the fixed branch, let

\[
g_{\lambda,J}(t)=P_{\lambda,J}(\sin t),
\tag{4.2}
\]

a continuous \(2\pi\)-periodic function.

**Lemma.**  Under \(\operatorname{Re}\lambda>0\):

1. \(f_\lambda\) is a trigonometric polynomial exactly when
   \(\lambda\in2\mathbb Z_{>0}\).
2. \(g_{\lambda,J}\) is a trigonometric polynomial exactly when
   \(\lambda\in\mathbb Z_{>0}\), independently of \(J\).

### Proof

A trigonometric polynomial is real analytic.  Suppose either function is one
near \(t=0\), and approach zero through \(t>0\).  If its zero there has
integer order \(m\), then

\[
\frac{(\sin t)^\lambda}{t^m}
=t^{\lambda-m}
\left(\frac{\sin t}{t}\right)^\lambda
\tag{4.3}
\]

must tend to a finite nonzero limit.  Its magnitude forces
\(\operatorname{Re}\lambda=m\), while its phase forces
\(\operatorname{Im}\lambda=0\).  Thus \(\lambda=m\in\mathbb Z_{>0}\).

For \(g_{\lambda,J}\), integer \(m\) makes the negative-side multiplier
\(e^{(2J+1)\pi im}=(-1)^m\), so (4.2) is exactly \((\sin t)^m\), a
trigonometric polynomial.

For \(f_\lambda\), analyticity across zero additionally requires
\(|t|^m=t^m\) on the negative side, so \(m\) must be even.  Conversely
\(|\sin t|^{2m}=\sin^{2m}t\) is a trigonometric polynomial.
\(\square\)

A continuous periodic function has finite Fourier support exactly when it is
a trigonometric polynomial.  Hence every exponent outside these integer
chambers has infinitely many nonzero continuous Fourier modes.

## 5. Sharp absolute-power classification

**Theorem (GLO764.ABSOLUTE_UNIFORM_DEGREE_GATE).**  Fix
\(\lambda\in\mathbb C\) with \(\operatorname{Re}\lambda>0\).  Then

\[
\sup_{\substack{1\leq a<b\\\gcd(a,b)=1}}
d_{\rm abs}(\lambda;a,b)<\infty
\quad\Longleftrightarrow\quad
\lambda\in2\mathbb Z_{>0}.
\tag{5.1}
\]

If \(\lambda=2m\), the sharp supremum is

\[
\sup_{a,b}d_{\rm abs}(2m;a,b)=2m+1.
\tag{5.2}
\]

### Proof

Take first \(\lambda\notin2\mathbb Z_{>0}\).  Set \(a=1\) and let \(b\)
grow.  Apart from a cyclic shift and the nonzero scalar
\((\sin(\pi/b))^{-\lambda}\), the coefficient block is the \(b\)-grid sample
of the \(\pi\)-periodic function (4.1).  After rescaling its period to one,
Sections 3--4 show that the sampled Fourier-support sizes, hence the reduced
degrees, are unbounded.

If \(\lambda=2m\), the binomial expansion of \(\sin^{2m}t\) has exactly
\(2m+1\) possible modes.  Sampling can merge or cancel modes but cannot create
new ones, so every degree is at most \(2m+1\).  When \(b>2m\), the exact
grouped binomial spectrum has no collisions and all binomial coefficients are
nonzero, giving degree \(2m+1\).  This proves sharpness.
\(\square\)

## 6. Sharp fixed-branch classification

**Theorem (GLO764.FIXED_BRANCH_UNIFORM_DEGREE_GATE).**  Fix
\(J\in\mathbb Z\) and \(\lambda\in\mathbb C\) with
\(\operatorname{Re}\lambda>0\).  Then

\[
\sup_{\substack{1\leq a<b\\\gcd(a,b)=1}}
d_J(\lambda;a,b)<\infty
\quad\Longleftrightarrow\quad
\lambda\in\mathbb Z_{>0}.
\tag{6.1}
\]

If \(\lambda=k\in\mathbb Z_{>0}\), the sharp supremum is

\[
\sup_{a,b}d_J(k;a,b)=k+1.
\tag{6.2}
\]

### Proof

For noninteger \(\lambda\), restrict to odd \(b\) and choose \(a=2\).  Then
\(\theta=2\pi/b\), and the orbit samples the full \(b\)-grid of the
\(2\pi\)-periodic function (4.2), up to cyclic shift and nonzero scaling.
Sections 3--4 force unbounded support and degree.

For integer \(k\), (1.5) is branch independent and
\(P_{k,J}(u_r)=u_r^k\).  Its symmetric-power/binomial expansion contains at
most \(k+1\) modes for every rational angle.  Choosing \(b>k\) removes all
root-of-unity collisions, so all \(k+1\) nonzero binomial modes remain.
\(\square\)

Thus rationality at every rational point is cheap, while a uniform finite
state-space rank is rigid: within these scalar chambers it occurs exactly at
the honest integer symmetric-power shadows.

## 7. A full-spectrum hostile witness

The first excluded absolute exponent already attains the entire orbit period.

**Theorem (GLO764.ABSOLUTE_FIRST_POWER_FULL_SPECTRUM).**  For
\(\lambda=1\), \(a=1\), and every \(b\geq2\),

\[
d_{\rm abs}(1;1,b)=b.
\tag{7.1}
\]

### Proof

On one block, before the harmless shift and scaling, take

\[
s(n)=\sin(\pi n/b),\qquad 0\leq n<b.
\tag{7.2}
\]

All these values are nonnegative, so this is the absolute-power sample.  Put
\(\eta=e^{\pi i/b}\) and \(\omega=\eta^2\).  For every
\(k\in\{0,\ldots,b-1\}\), two geometric sums give

\[
\sum_{n=0}^{b-1}s(n)\omega^{-kn}
=\frac1i\left(
\frac1{1-\eta\omega^{-k}}
-\frac1{1-\eta^{-1}\omega^{-k}}
\right).
\tag{7.3}
\]

Both geometric ratios have \(b\)-th power \(-1\), so neither denominator
vanishes.  Their difference has numerator
\(\omega^{-k}(\eta-\eta^{-1})\neq0\).  Every one of the \(b\) discrete
Fourier modes therefore survives.  Section 2 proves (7.1).
\(\square\)

This exact family is a useful guard against mistaking the upper denominator
\(1-T^b\) for merely nonminimal bookkeeping.

## 8. L0--L9 and parent interpretation

| Object | L0 | L1 | L2 | uniform L3 | First stop |
|---|---|---|---|---|---|
| absolute power, non-even \(\lambda\) | branch-free with zero value fixed | multiplicative on absolute values | formal if inputs are multiplicative | fails by (5.1) | uniform L3 |
| absolute power \(2m\) | branch-free | scalar multiplicativity | formal | passes with sharp degree \(2m+1\) | L4 |
| fixed-branch noninteger power | passes only after \(J\) is fixed | generally fails | generally unavailable | fails by (6.1) | L1 and uniform L3 |
| integer power \(k\) | branch independent | scalar multiplicativity | formal | passes with sharp degree \(k+1\) | L4 |

For integer \(k\), the bounded state space is the honest
\(\operatorname{Sym}^k\) parent, while the scalar coefficient series remains
a matrix coefficient rather than the standard determinant inverse.  For a
noninteger exponent, each individual rational orbit still has a cyclic finite
state realization, but (5.1) and (6.1) prove that no uniform finite dimension
can realize the whole rational-angle family in these constant-coefficient
scalar models.

This is only a finite-dimensional constant-state-space obstruction.  It does
not exclude infinite-dimensional, nuclear, categorical, \(p\)-adic analytic,
or parameter-dependent constructions, and it does not by itself prove or
disprove an \(L\)-function.

## 9. Exact replay and source lock

The dependency-free companion producer uses only integer, rational, binomial,
and root-exponent algebra.  It:

1. checks the full-spectrum certificate (7.3) through a declared \(b\)-range;
2. replays every reduced rational rotation in a finite hostile range and
   verifies the uniform \(k+1\) integer bound;
3. verifies collision-free sharpness whenever \(b>k\);
4. checks exact finite-Fourier alias support for polynomial controls;
5. records the analytic sampling and cusp obligations separately from the
   finite replay; and
6. authenticates every imported source as an exact Git object.

Replay from the repository root:

    python research/l-families/atlas/generalized/rational_rotation_uniform_degree_gate.py --check
    python -O research/l-families/atlas/generalized/rational_rotation_uniform_degree_gate.py --check
    python -m unittest tests.test_rational_rotation_uniform_degree_gate
    python -O -m unittest tests.test_rational_rotation_uniform_degree_gate

Finite rows are regression controls, not evidence for the universal theorem.
The universal noninteger direction is the proof in Sections 2--6.

## 10. Literature and novelty boundary

Oliver Knill and John Lesieutre,
[*Analytic continuation of Dirichlet series with almost periodic
coefficients*](https://arxiv.org/abs/0811.1362), study Taylor and Dirichlet
series generated by periodic functions along irrational rotations and
explicitly contrast rational finite orbits.  Their analytic-continuation and
natural-boundary questions are adjacent, but they do not state the present
uniform reduced-degree classification over rational angle denominators.

The NIST
[*Digital Library of Mathematical Functions, Section 1.8*](https://dlmf.nist.gov/1.8)
is a reference boundary for the standard Fourier conventions and uniqueness
facts used here.  The grid-persistence argument itself is the elementary
Riemann-sum proof in Section 3.

All ingredients are standard Fourier, sampling, local-analytic, and binomial
facts.  The assembled theorem is not a priority claim.  External novelty is
unreviewed.

## 11. What remains open

The theorem gives no quantitative lower bound as a function of \(b\), only
unboundedness.  It excludes \(\operatorname{Re}\lambda\leq0\), the
\(\lambda=0\) convention family, varying determinant, higher-rank torus
orbits, ramified local data, and nonconstant or infinite-dimensional state
spaces.  Most importantly, it does not solve L4--L9: determinant/duality,
ramification and conductor, completion and functional equation, functorial
laws, realization, and principled explicit-formula or zero theory remain
open.
