# Rational tempered rotations: zeros, branches, and finite spectra

Status: **proposed exact local theorem; external novelty unreviewed**
Issue: [#764](https://github.com/gfreund123/riemann/issues/764)
Claim labels: GLO764.RATIONAL_ROTATION_ZERO_PERIOD,
GLO764.FIXED_BRANCH_POWER_PERIOD,
GLO764.ZERO_EXPONENT_CONVENTION_SPECTRUM, and
GLO764.INTEGER_POWER_COLLISION_SPECTRUM

## Scientific firewall

This packet closes the rational-rotation chamber deliberately excluded from
the adjacent irrational-rotation theorem.  It treats one determinant-one,
unramified, tempered rank-two recurrence.  The main mechanisms are finite
orbits, exact zeros, and an explicitly chosen real-axis logarithm branch.

Periodicity makes every fixed-branch series below rational, and the displayed
period denominator is unbounded as the angle denominator grows.  That fact
alone does **not** decide reduced-denominator degree: in the integer polynomial
chambers, (5.2) immediately gives the uniform bound \(k+1\).  This packet does
not classify the complementary noninteger chambers uniformly.  A
branch-dependent scalar power is not automatically multiplicative, and a
rational local series is not automatically a local factor of an automorphic
or motivic object.

Nothing here constructs a global Euler product, ramified factors, completion,
functional equation, conductor, root number, automorphic lift, motive,
explicit formula, or zero theory.  There is no RH or GRH consequence.

## 1. Normalization and the orbit skeleton

Let

\[
1\leq a<b,\qquad \gcd(a,b)=1,\qquad
\theta=\frac{a\pi}{b},\qquad x=2\cos\theta.
\tag{1.1}
\]

Define

\[
u_0=1,\qquad u_1=x,\qquad
u_{r+2}=x u_{r+1}-u_r.
\tag{1.2}
\]

Since \(0<\theta<\pi\),

\[
u_r=\frac{\sin((r+1)\theta)}{\sin\theta}.
\tag{1.3}
\]

Writing \(n=r+1\), coprimality gives the exact zero and shift laws

\[
u_r=0\iff b\mid r+1,
\tag{1.4}
\]

\[
u_{r+b}=(-1)^a u_r,
\qquad
u_{r+2b}=u_r.
\tag{1.5}
\]

There are both positive and negative nonzero terms.  One direct proof is to
observe that the residues \(na\pmod {2b}\) run through either every residue
when \(a\) is odd, or every even residue when \(a\) is even; in the latter
case \(b\) is odd.  In either case some residues lie strictly between \(0\)
and \(b\), and some lie strictly between \(b\) and \(2b\).

Rationality throughout means that the analytic germ at \(T=0\) belongs to
\(\mathbb C(T)\).

## 2. Absolute powers

For \(\lambda\in\mathbb C\) with \(\operatorname{Re}\lambda>0\), define

\[
A_\lambda(y)=
\begin{cases}
\exp(\lambda\log |y|),&y\neq0,\\
0,&y=0,
\end{cases}
\tag{2.1}
\]

where \(\log |y|\) is the ordinary real logarithm of a positive number.
This is branch-free.

**Theorem (GLO764.RATIONAL_ROTATION_ZERO_PERIOD).**  The sequence
\(A_\lambda(u_r)\) has minimal period exactly \(b\).  Consequently

\[
\sum_{r\geq0}A_\lambda(u_r)T^r
=
\frac{\displaystyle\sum_{r=0}^{b-1}A_\lambda(u_r)T^r}
     {1-T^b}
\in\mathbb C(T).
\tag{2.2}
\]

### Proof

Equation (1.5) gives \(|u_{r+b}|=|u_r|\), so \(b\) is a period.  The zero
set is the single congruence class \(r\equiv b-1\pmod b\).  Any positive
period must preserve that class and hence must be divisible by \(b\).
Therefore \(b\) is minimal.  Summing the repeated block gives (2.2).
\(\square\)

Minimal period does not imply that \(1-T^b\) is always the reduced
denominator: a periodic sequence can omit Fourier modes.  The theorem claims
the exact period and rationality, not a nonexistent universal no-cancellation
rule for arbitrary complex \(\lambda\).

## 3. Fixed real-axis logarithm branches

Fix \(J\in\mathbb Z\).  For
\(\operatorname{Re}\lambda>0\), define

\[
P_{\lambda,J}(y)=
\begin{cases}
\exp(\lambda\log y),&y>0,\\
\exp\!\left(\lambda(\log|y|+(2J+1)\pi i)\right),&y<0,\\
0,&y=0.
\end{cases}
\tag{3.1}
\]

The negative-to-positive phase is

\[
c_{\lambda,J}=e^{(2J+1)\pi i\lambda}.
\tag{3.2}
\]

The choice \(J=0\) is the upper-side principal real-axis convention used in
the next irrational-rotation packet.  Formula (3.1), rather than an
unqualified symbol \(y^\lambda\), is the definition.

**Theorem (GLO764.FIXED_BRANCH_POWER_PERIOD).**  The sequence
\(P_{\lambda,J}(u_r)\) is periodic and its minimal period is

\[
p(\lambda,J;a,b)=
\begin{cases}
b,&a\text{ even},\\
b,&a\text{ odd and }c_{\lambda,J}=1,\\
2b,&a\text{ odd and }c_{\lambda,J}\neq1.
\end{cases}
\tag{3.3}
\]

Thus

\[
\sum_{r\geq0}P_{\lambda,J}(u_r)T^r
=
\frac{\displaystyle\sum_{r=0}^{p-1}P_{\lambda,J}(u_r)T^r}
     {1-T^p}
\in\mathbb C(T).
\tag{3.4}
\]

The values are independent of \(J\) exactly when

\[
e^{2\pi i\lambda}=1,
\tag{3.5}
\]

which, under \(\operatorname{Re}\lambda>0\), is equivalent to
\(\lambda\in\mathbb Z_{>0}\).  For the principal convention \(J=0\),
the second line of (3.3) occurs exactly for positive even integers
\(\lambda\).

### Proof

If \(a\) is even, (1.5) fixes the signed value after \(b\) steps.  If \(a\)
is odd, it reverses the sign.  A sign reversal fixes (3.1) for every nonzero
orbit value exactly when \(c_{\lambda,J}=1\); otherwise two shifts, and no
one shift, return the value.  As in Section 2, the zero class forces every
period to be divisible by \(b\), proving minimality.

Changing \(J\) to \(J+1\) multiplies every negative value by
\(e^{2\pi i\lambda}\).  Negative terms exist, so all branch values agree
exactly when (3.5) holds.  The complex exponential equals one exactly at
integer \(\lambda\).  The principal-branch statement follows from
\(e^{\pi i\lambda}=1\iff\lambda\in2\mathbb Z\). \(\square\)

For noninteger \(\lambda\), allowing \(J\) to vary independently with
\(r\) is not another harmless branch convention: it inserts an uncontrolled
coefficient sequence.  This packet treats one fixed branch index.  Without
that datum the proposed scalar transform stops at L0.

## 4. The zero-exponent convention is mathematical data

At \(\lambda=0\), equation (2.1) no longer defines the values at the zeros.
Let \(z\in\mathbb C\) be the declared value of \(0^0\), and put

\[
q_r(z)=
\begin{cases}
1,&u_r\neq0,\\
z,&u_r=0.
\end{cases}
\tag{4.1}
\]

Then

\[
Q_z(T)=\sum_{r\geq0}q_r(z)T^r
=
\frac{1+T+\cdots+T^{b-2}+zT^{b-1}}{1-T^b}.
\tag{4.2}
\]

**Theorem (GLO764.ZERO_EXPONENT_CONVENTION_SPECTRUM).**  The reduced
denominator and minimal recurrence order of (4.2) are

\[
\begin{array}{c|c|c}
z&\text{reduced denominator}&\text{minimal order}\\ \hline
1&1-T&1\\
1-b&\dfrac{1-T^b}{1-T}=1+T+\cdots+T^{b-1}&b-1\\
z\notin\{1,1-b\}&1-T^b&b.
\end{array}
\tag{4.3}
\]

In particular, the convention \(0^0=1\) gives the constant sequence, while
the support convention \(0^0=0\) has reduced denominator \(1-T^b\).

### Proof

Let \(\omega=e^{2\pi i/b}\), and take the discrete Fourier coefficients of
one block.  The exceptional entry is at \(r=b-1\), so

\[
\widehat q_0=b-1+z,
\qquad
\widehat q_k=(z-1)\omega^{-k(b-1)}
\quad(1\leq k<b).
\tag{4.4}
\]

The reduced denominator is the product of \(1-\omega^kT\) over the nonzero
Fourier coefficients.  Formula (4.4) gives the three cases in (4.3).
Every retained coefficient is nonzero and its characteristic root is
distinct, so the number of retained factors is the minimal recurrence order.
\(\square\)

## 5. Branch-independent integer powers and collision spectra

Let \(k\in\mathbb Z_{>0}\), put \(\alpha=e^{i\theta}\), and define for
\(0\leq c<b\)

\[
S_c(k,b)=
\sum_{\substack{0\leq j\leq k\\j\equiv c\pmod b}}
(-1)^j\binom{k}{j}.
\tag{5.1}
\]

**Theorem (GLO764.INTEGER_POWER_COLLISION_SPECTRUM).**  The exact finite
spectrum of the branch-independent sequence \(u_r^k\) is

\[
u_r^k
=
\frac{1}{(\alpha-\alpha^{-1})^k}
\sum_{\substack{0\leq c<b\\S_c(k,b)\neq0}}
S_c(k,b)\alpha^{k-2c}
\left(\alpha^{k-2c}\right)^r.
\tag{5.2}
\]

The roots \(\alpha^{k-2c}\) retained in (5.2) are pairwise distinct.  Hence
the reduced denominator and minimal recurrence order are

\[
D_{k;a,b}(T)=
\prod_{\substack{0\leq c<b\\S_c(k,b)\neq0}}
\left(1-\alpha^{k-2c}T\right),
\tag{5.3}
\]

\[
d_{k,b}=\#\{c\in\{0,\ldots,b-1\}:S_c(k,b)\neq0\}.
\tag{5.4}
\]

This includes exact alias cancellation.  For example,
\(S_0(3,3)=1-1=0\), so the cube at \(b=3\) retains two rather than three
distinct modes.

### Proof

The binomial theorem applied to (1.3) gives

\[
u_r^k
=
\frac{1}{(\alpha-\alpha^{-1})^k}
\sum_{j=0}^{k}(-1)^j\binom{k}{j}
\alpha^{(k-2j)(r+1)}.
\tag{5.5}
\]

Terms with indices congruent modulo \(b\) have the same root because
\(\alpha^{2b}=1\).  Grouping them yields (5.2).  Conversely, equality of
the roots for \(c,c'\in\{0,\ldots,b-1\}\) implies
\(e^{2\pi i a(c-c')/b}=1\), hence \(b\mid c-c'\), and therefore
\(c=c'\).  Each retained simple partial fraction has nonzero coefficient,
so no factor in (5.3) cancels.  This proves (5.3) and (5.4). \(\square\)

## 6. Scalar transform versus a non-scalar parent

The matrix

\[
A_\theta=\operatorname{diag}(\alpha,\alpha^{-1})
\tag{6.1}
\]

is the rank-two parent of the original recurrence.  For integer \(k\), the
genuine non-scalar representation \(\operatorname{Sym}^k(A_\theta)\) has
weights

\[
\alpha^k,\alpha^{k-2},\ldots,\alpha^{-k}.
\tag{6.2}
\]

Equation (5.5) realizes the scalar transform as a weighted observable

\[
u_r^k=\operatorname{tr}(C_{k,\theta}B_{k,\theta}^{r}),
\tag{6.3}
\]

where \(B_{k,\theta}=\operatorname{Sym}^k(A_\theta)\) is diagonal in the
weight basis and \(C_{k,\theta}\) has diagonal entries

\[
\frac{(-1)^j\binom{k}{j}\alpha^{k-2j}}
     {(\alpha-\alpha^{-1})^k}.
\tag{6.4}
\]

This is a genuine \((k+1)\)-dimensional state-space parent, not just the same
scalar repeated in extra coordinates.  It also exposes the distinction that
the scalar series hides: the standard determinant
\(\det(I-B_{k,\theta}T)^{-1}\) retains representation multiplicities,
whereas the scalar observable can merge equal weights and can cancel a
merged mode through \(S_c(k,b)=0\).  Thus (5.3) must not be silently
identified with a symmetric-power local factor.

For noninteger \(\lambda\), periodicity still gives a finite cyclic
state-space realization after a branch is fixed, of dimension at most
\(2b\).  This denominator-dependent construction supplies no fixed-rank
interpolation of \(\operatorname{Sym}^k\); by itself it also supplies no lower
bound on the minimal realization dimension.

## 7. Exact controls and source lock

The adjacent dependency-free producer performs only integer, rational, and
symbolic root-label algebra.  It:

1. exhausts all reduced \((a,b)\) with \(2\leq b\leq12\);
2. checks the exact zero class and signed shift law without trigonometric
   floating point;
3. checks the period decision table for symbolic branch phase
   \(c_{\lambda,J}=1\) versus \(c_{\lambda,J}\neq1\);
4. reconstructs the three zero-exponent spectra in (4.3);
5. computes every grouped binomial spectrum through \(k=16\), including
   hostile cancellation rows; and
6. authenticates every imported file as an exact Git object at commit
   \(cdaa8bcb863b0aa30044fc599efdf4ac549a5c38\).

The arithmetic class is EXACT_RATIONAL.  Roots of unity are stored as exact
exponents modulo \(2b\); they are never approximated.

Replay from the repository root:

    python research/l-families/atlas/generalized/rational_rotation_branch_census.py --check
    python -O research/l-families/atlas/generalized/rational_rotation_branch_census.py --check
    python -m unittest tests.test_rational_rotation_branch_census
    python -O -m unittest tests.test_rational_rotation_branch_census

The finite rows are hostile controls for the formulas.  The all-\(a,b,k\)
statements are the proofs above, not an inference from the finite range.

## 8. L0--L9 survival ledger

| Object | L0 | L1 | L2 | L3 | First stop |
|---|---|---|---|---|---|
| absolute power, \(\operatorname{Re}\lambda>0\) | branch-free and zeros fixed | preserves multiplication of absolute values | formal for multiplicative inputs | rational pointwise; if \(\lambda=2m\), (5.2) gives degree at most \(2m+1\); the complementary uniform question is not classified here | uniform L3 outside the even-integer chamber |
| fixed-branch signed power | only after \(J\) is supplied | fails in general; on real scalars it requires \(c_{\lambda,J}^2=1\) | unavailable when L1 fails | the one-orbit series is rational | L1 |
| positive integer power \(k\) | branch-independent | multiplicative scalar map | formal for multiplicative inputs | exact finite spectrum (5.3), with the uniform bound \(d_{k,b}\leq k+1\) | L4 |
| unspecified value of \(0^0\) | fails | not reached | not reached | not reached | L0 |

The fixed branch can exceptionally satisfy L1 at noninteger \(\lambda\) if
\(c_{\lambda,J}=\pm1\); this is a scalar sign-law fact, not a functorial or
global construction.  Levels L4--L9 ask for coherent determinant/duality and
ramified data, completion, analytic continuation and functional equation,
twist/tensor/induction laws, a realization, and principled explicit-formula
or zero theory.  None is established here.

## 9. Nearby literature and novelty firewall

Oliver Knill and John Lesieutre,
[*Analytic continuation of Dirichlet series with almost periodic
coefficients*](https://arxiv.org/abs/0811.1362), explicitly contrast
irrational rotations with the rational case and decompose periodic
coefficients into finitely many residue classes.  Their target is analytic
continuation of Dirichlet and Taylor series, not the zero/branch/minimal
period census or the grouped scalar-observable spectrum (5.1)--(5.4).

William Kahan's
[*Branch Cuts for Complex Elementary Functions, or Much Ado About Nothing's
Sign Bit*](https://people.freebsd.org/~das/kahan86branch.pdf) is nearby
background for why a principal value and the value on a cut must be stated
explicitly.  This packet uses only the elementary logarithm branches in
(3.1); it imports no theorem from that paper.

All proof ingredients are standard finite-orbit, Fourier, binomial, and
complex-logarithm facts.  A self-contained formulation is not a priority or
novelty claim.  The external novelty status is unreviewed, and this packet
makes no claim of priority.

## 10. Known gaps

The packet excludes \(\operatorname{Re}\lambda\leq0\) except for the
explicit \(\lambda=0\) convention family.  Negative real part meets actual
zeros and cannot use the definition (3.1); purely imaginary powers do not
approach a branch-independent value at zero.  Unrestricted termwise branch
choices, determinant other than one, ramified data, the noninteger uniform
local-degree classification, and any global or categorical realization remain
open.
