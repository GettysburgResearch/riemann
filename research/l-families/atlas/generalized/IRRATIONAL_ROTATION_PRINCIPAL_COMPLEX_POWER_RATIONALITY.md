# Principal complex powers on an irrational tempered orbit

Status: **proposed exact local theorem; external novelty unreviewed**
Issue: [#764](https://github.com/gfreund123/riemann/issues/764)
Claim labels: GLO764.IRRATIONAL_FIXED_BRANCH_COMPLEX_POWER_RATIONALITY,
GLO764.IRRATIONAL_PRINCIPAL_POWER_MINIMAL_DENOMINATOR, and
GLO764.NONINTEGER_POWER_FINITE_STATE_NO_GO

## Scientific firewall

This packet treats the branch-sensitive scalar power of one
determinant-one, unramified, tempered rank-two recurrence.  The exponent is
either \(0\), handled separately, or satisfies
\(\operatorname{Re}\lambda>0\).  A single real-axis logarithm branch is
fixed once and for all.  The principal convention is the case \(J=0\).

The result is a local rationality and finite-state classification.  It is
not a nonintegral symmetric-power no-go in an infinite-dimensional,
categorical, \(p\)-adic, or automorphic setting.  It supplies no global
Euler product, ramified factors, completion, functional equation, conductor,
root number, automorphy, motive, explicit formula, or zero theorem.  There is
no RH or GRH consequence.

## 1. Recurrence and branch convention

Fix

\[
0<\theta<\pi,
\qquad
\frac{\theta}{\pi}\notin\mathbb Q,
\qquad
x=2\cos\theta.
\tag{1.1}
\]

Let

\[
u_0=1,\qquad u_1=x,\qquad
u_{r+2}=x u_{r+1}-u_r.
\tag{1.2}
\]

Then

\[
u_r=\frac{\sin((r+1)\theta)}{\sin\theta}.
\tag{1.3}
\]

Irrationality implies \(u_r\neq0\) for all \(r\geq0\).

For \(J\in\mathbb Z\) and
\(\lambda\in\mathbb C\) with
\(\operatorname{Re}\lambda>0\), define on the real axis

\[
P_{\lambda,J}(y)=
\begin{cases}
\exp(\lambda\log y),&y>0,\\
\exp\!\left(\lambda(\log|y|+(2J+1)\pi i)\right),&y<0,\\
0,&y=0.
\end{cases}
\tag{1.4}
\]

Here every logarithm of a positive real number is the ordinary real
logarithm.  The value at zero makes the associated periodic function
continuous; the sampled orbit itself never uses it.  The upper-side
principal convention is \(J=0\).

Set

\[
H_{\lambda,J,\theta}(T)
=
\sum_{r\geq0}P_{\lambda,J}(u_r)T^r.
\tag{1.5}
\]

Rationality means that the analytic germ (1.5) at \(T=0\) belongs to
\(\mathbb C(T)\).  At \(\lambda=0\), define the sequence separately by
\(P_{0}(u_r)=1\); no zero convention is needed on the nonzero orbit.

## 2. Exact fixed-branch classification

**Theorem
(GLO764.IRRATIONAL_FIXED_BRANCH_COMPLEX_POWER_RATIONALITY).**  For every
fixed \(J\in\mathbb Z\) and every exponent in the domain

\[
\{0\}\cup\{\lambda\in\mathbb C:
\operatorname{Re}\lambda>0\},
\tag{2.1}
\]

\[
H_{\lambda,J,\theta}(T)\in\mathbb C(T)
\quad\Longleftrightarrow\quad
\lambda\in\mathbb Z_{\geq0}.
\tag{2.2}
\]

For \(k\in\mathbb Z_{\geq0}\), the reduced denominator is

\[
D_{k,\theta}(T)
=
\prod_{j=0}^{k}
\left(1-e^{i(k-2j)\theta}T\right),
\tag{2.3}
\]

and the minimal constant-coefficient recurrence order is exactly

\[
k+1.
\tag{2.4}
\]

For \(k=0\), these formulas mean
\(H_{0}(T)=(1-T)^{-1}\) and order \(1\).

The rationality classification is the same for every fixed \(J\), although
the noninteger coefficient sequences depend on \(J\).  The sequence is
branch-independent for all \(J\) exactly at integer exponents.

## 3. Eventual recurrence forces finite Fourier support

We need the \(2\pi\)-periodic form of the dense-orbit gate.

**Lemma.**  Let \(f:\mathbb R/2\pi\mathbb Z\to\mathbb C\) be continuous,
and suppose \(\theta/\pi\) is irrational.  If

\[
b_r=f((r+1)\theta)
\tag{3.1}
\]

satisfies a nonzero constant-coefficient recurrence for all sufficiently
large \(r\), then \(f\) is a trigonometric polynomial.

### Proof

Write the eventual recurrence, after deleting zero end coefficients, as

\[
\sum_{\ell=0}^{d}c_\ell b_{n+\ell}=0
\qquad(n\geq N),
\tag{3.2}
\]

with a nonzero polynomial

\[
Q(z)=\sum_{\ell=0}^{d}c_\ell z^\ell.
\tag{3.3}
\]

The continuous function

\[
R(t)=\sum_{\ell=0}^{d}c_\ell f(t+\ell\theta)
\tag{3.4}
\]

vanishes on a tail of the rotation orbit.  Since
\(\theta/(2\pi)\) is irrational, that tail is dense modulo \(2\pi\).
Thus \(R(t)=0\) everywhere.

With Fourier convention

\[
\widehat f(n)=\frac{1}{2\pi}
\int_0^{2\pi}f(t)e^{-int}\,dt,
\tag{3.5}
\]

taking the \(n\)-th coefficient of (3.4) gives

\[
Q(e^{in\theta})\widehat f(n)=0.
\tag{3.6}
\]

The points \(e^{in\theta}\), \(n\in\mathbb Z\), are pairwise distinct;
otherwise \(\theta/\pi\) would be rational.  A nonzero polynomial has only
finitely many roots, so \(\widehat f(n)\) is nonzero for only finitely many
\(n\).  Fejér's theorem identifies a continuous periodic function with its
finite Fourier sum.  Hence \(f\) is a trigonometric polynomial. \(\square\)

A rational ordinary generating function has an eventual recurrence: if
\(H(T)=A(T)/Q(T)\) with \(Q(0)=1\), the coefficients of
\(Q(T)H(T)=A(T)\) vanish beyond \(\deg A\).  Thus the lemma applies to
every rational series in (1.5).

## 4. The branch cusp excludes nonintegers

For \(\operatorname{Re}\lambda>0\), define the continuous
\(2\pi\)-periodic function

\[
f_{\lambda,J}(t)=P_{\lambda,J}(\sin t).
\tag{4.1}
\]

Since \(\sin\theta>0\), equation (1.3) gives

\[
P_{\lambda,J}(u_r)
=
(\sin\theta)^{-\lambda}
f_{\lambda,J}((r+1)\theta).
\tag{4.2}
\]

The nonzero constant does not affect rationality.  If (1.5) were rational,
the lemma would make \(f_{\lambda,J}\) a trigonometric polynomial and hence
\(C^\infty\).

Near \(t=0\), set

\[
h_\lambda(t)=
\exp\!\left(\lambda\log\frac{\sin t}{t}\right).
\tag{4.3}
\]

The quotient \(\sin t/t\) is positive and smooth near zero, so
\(h_\lambda\) and its reciprocal are smooth with value \(1\) at zero.  On
the positive side,

\[
f_{\lambda,J}(t)=t^\lambda h_\lambda(t).
\tag{4.4}
\]

Suppose \(\lambda\notin\mathbb Z_{>0}\), and choose an integer
\(N>\operatorname{Re}\lambda\).  The coefficient

\[
(\lambda)_N
=
\lambda(\lambda-1)\cdots(\lambda-N+1)
\tag{4.5}
\]

is nonzero, because \(\lambda\) is not one of
\(0,1,\ldots,N-1\).  On \(t>0\),

\[
\frac{d^N}{dt^N}t^\lambda
=(\lambda)_N t^{\lambda-N},
\tag{4.6}
\]

whose magnitude is
\(|(\lambda)_N|t^{\operatorname{Re}\lambda-N}\), unbounded as
\(t\downarrow0\).  Dividing (4.4) by the smooth nonvanishing factor
\(h_\lambda\) shows that \(f_{\lambda,J}\) cannot be \(C^N\).  Therefore
the rationality assumption is impossible.

If \(\lambda=k\in\mathbb Z_{>0}\), then

\[
e^{(2J+1)\pi i k}=(-1)^k,
\tag{4.7}
\]

so every branch gives

\[
f_{k,J}(t)=\sin^k t.
\tag{4.8}
\]

This is a trigonometric polynomial.  Together with the separate constant
case \(k=0\), this proves (2.2).

## 5. Integer powers and the minimal denominator

For \(k\geq0\),

\[
\sin^k t
=
(2i)^{-k}
\sum_{j=0}^{k}(-1)^j\binom{k}{j}
e^{i(k-2j)t}.
\tag{5.1}
\]

Every coefficient is nonzero.  Substitution into (4.2) gives

\[
P_{k,J}(u_r)
=
\sum_{j=0}^{k}
A_j\left(e^{i(k-2j)\theta}\right)^r,
\tag{5.2}
\]

with

\[
A_j=
\frac{(2i)^{-k}(-1)^j\binom{k}{j}
e^{i(k-2j)\theta}}
{\sin^k\theta}
\neq0.
\tag{5.3}
\]

Irrationality makes the \(k+1\) roots in (5.2) pairwise distinct.  Therefore

\[
H_{k,J,\theta}(T)
=
\sum_{j=0}^{k}
\frac{A_j}{1-e^{i(k-2j)\theta}T}.
\tag{5.4}
\]

At each candidate pole, exactly one summand has a pole and its residue is
nonzero; all other summands are analytic there.  No factor cancels.  This
proves (2.3) and (2.4). \(\square\)

## 6. Exact non-scalar parent and finite-state no-go

Let

\[
A_\theta=\operatorname{diag}(e^{i\theta},e^{-i\theta}),
\qquad
B_{k,\theta}=\operatorname{Sym}^k(A_\theta).
\tag{6.1}
\]

In the weight basis, \(B_{k,\theta}\) has the \(k+1\) eigenvalues in
(5.2).  With the diagonal observation matrix whose entries are the
coefficients \(A_j\),

\[
H_{k,J,\theta}(T)
=
\operatorname{tr}\!\left(
C_{k,\theta}(I-TB_{k,\theta})^{-1}
\right).
\tag{6.2}
\]

Thus the integer scalar transform has a genuine non-scalar
\((k+1)\)-dimensional resolvent parent, and

\[
D_{k,\theta}(T)=\det(I-TB_{k,\theta}).
\tag{6.3}
\]

The equality of denominators does not identify (6.2) with
\(\det(I-TB_{k,\theta})^{-1}\): the former is a weighted resolvent trace,
with a different numerator and coefficient sequence.

**Corollary (GLO764.NONINTEGER_POWER_FINITE_STATE_NO_GO).**  If
\(\operatorname{Re}\lambda>0\) and
\(\lambda\notin\mathbb Z_{>0}\), there do not exist a finite-dimensional
complex vector space \(V\), a fixed endomorphism \(B\), a vector \(v\), and
a linear functional \(\ell\) satisfying

\[
P_{\lambda,J}(u_r)=\ell(B^rv)
\qquad(r\geq0).
\tag{6.4}
\]

Indeed, Cayley--Hamilton would give a constant-coefficient recurrence and a
rational generating function, contradicting (2.2).  This corollary rules out
only a constant finite-dimensional linear state-space realization.  It says
nothing against infinite-dimensional, parameter-varying, categorical, or
nonlinear parents.

## 7. Exact replay

The adjacent producer uses exact integer, rational, and Laurent-polynomial
algebra.  It:

1. reconstructs the scaled Fourier coefficients in (5.1) for
   \(0\leq k\leq10\);
2. builds \(\prod_{j=0}^k(1-\alpha^{k-2j}T)\) symbolically and checks exact
   tail annihilation;
3. records exact rational controls for real and genuinely complex
   \(\lambda\), including the first derivative order forced to diverge;
4. checks branch independence at integers and branch dependence controls
   away from integers;
5. locks the finite-state corollary to the rationality theorem; and
6. authenticates every imported source as an exact Git object at commit
   \(834a24e71878a584e00215edf1e0c813faa9f578\).

The repository arithmetic class is EXACT_RATIONAL.  The angle remains a
symbolic irrational-rotation hypothesis; no floating approximation to
\(\theta\) is used.

Replay from the repository root:

    python research/l-families/atlas/generalized/irrational_rotation_principal_complex_power_rationality.py --check
    python -O research/l-families/atlas/generalized/irrational_rotation_principal_complex_power_rationality.py --check
    python -m unittest tests.test_irrational_rotation_principal_complex_power_rationality
    python -O -m unittest tests.test_irrational_rotation_principal_complex_power_rationality

The finite rows are hostile controls.  The complex-exponent classification is
the proof in Sections 3--5, not an inference from those rows.

## 8. L0--L9 survival ledger

| Object | L0 | L1 | L2 | L3 | First stop |
|---|---|---|---|---|---|
| noninteger power with no branch datum | fails: values on negative terms are ambiguous | not reached | not reached | not reached | L0 |
| fixed-branch noninteger power, \(\operatorname{Re}\lambda>0\) | defined | generally fails scalar multiplicativity | unavailable when L1 fails | fails on every irrational tempered orbit | L1 and L3 |
| integer \(k\geq0\) | branch-independent | scalar multiplicativity | formal for multiplicative inputs | exact degree \(k+1\), with resolvent parent | L4 |

Levels L4--L9 ask for coherent determinant, weight, duality, and ramified
data; completion; analytic continuation and functional equation;
twist/tensor/induction laws; a realization; and a principled explicit formula
or zero theory.  The matrix in Section 6 is a local state-space parent, not a
claim that those higher levels hold.

## 9. Nearby literature and novelty firewall

Oliver Knill and John Lesieutre,
[*Analytic continuation of Dirichlet series with almost periodic
coefficients*](https://arxiv.org/abs/0811.1362), study irrational-rotation
coefficient series, Fourier partial fractions, meromorphic continuation for
trigonometric-polynomial data, and natural boundaries under additional
hypotheses.  This packet asks the narrower exact eventual-recurrence and
rationality question for the fixed-branch function
\(P_{\lambda,J}(\sin t)\).  It does not import or strengthen their
natural-boundary results.

William Kahan's branch-cut paper is nearby background for explicit principal
values.  Formula (1.4) is self-contained and does not rely on a software
signed-zero convention.

The proof combines standard recurrence, irrational rotation, Fourier
uniqueness, cusp regularity, and Cayley--Hamilton facts.  A self-contained
proof is not a priority claim.  External novelty remains unreviewed, and this
packet makes no novelty claim.

## 10. Excluded boundary

No theorem is asserted here for nonzero \(\lambda\) with
\(\operatorname{Re}\lambda\leq0\).  Although the irrational sampled orbit
never hits zero, the periodic model is unbounded when
\(\operatorname{Re}\lambda<0\) and has no limit at the sine zeros for a
nonzero purely imaginary exponent.  The continuity gate used in Section 3
therefore does not apply.  Excluding this region is a proof boundary, not a
rationality prediction.
