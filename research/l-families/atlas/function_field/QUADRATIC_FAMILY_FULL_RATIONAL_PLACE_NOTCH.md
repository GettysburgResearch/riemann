# The full-rational-place notch and its supersingular auxiliary curve

Status: **exact all-odd-prime-power theorem for every squarefree family
degree; family correlations, not zeros of individual L-functions**

Bounded replay:
[`quadratic_family_full_rational_place_notch.py`](quadratic_family_full_rational_place_notch.py).

## 0. Outcome

The multi-place interferometer has an exact maximal-aperture law.  Let `q`
be any odd prime power, let `H_n(q)` be the monic squarefree degree-`n`
polynomials in `F_q[T]`, and put

\[
 S^{\mathrm{full}}_{n,q}
 =\sum_{D\in\mathcal H_n(q)}
   \prod_{a\in\mathbf F_q}\chi(D(a)),
\tag{0.1}
\]

where `chi(0)=0`.  Define

\[
 s_q=(-1)^{(q+1)/2},\qquad g={q-1\over2}.
\tag{0.2}
\]

Then the complete generating series is

\[
 \boxed{
 \sum_{n\ge0}S^{\mathrm{full}}_{n,q}u^n
 =(1+s_qqu^2)^g{1-qu^2\over(1-u^2)^q}.}
\tag{0.3}
\]

Every factor on the right is even.  Consequently

\[
 \boxed{S^{\mathrm{full}}_{2k+1,q}=0
 \quad\text{for every }k\ge0.}
\tag{0.4}
\]

In particular, the complete rational-place correlation in the quadratic
quintic family vanishes for every odd prime power, even though the generic
five- and six-place correlations expose nontrivial genus-two trace channels.

The mechanism is not a formal exterior-character notch.  At full aperture,
the auxiliary curve itself becomes

\[
 C_q:\quad y^2=x-x^q,
\tag{0.5}
\]

and has the exact zeta numerator

\[
 \boxed{P_q(u)=(1+s_qqu^2)^g.}
\tag{0.6}
\]

Thus its odd Frobenius exterior coefficients vanish simultaneously.  This is
a geometric saturation law for the evaluation-character interferometer.
It is not an FFPS varying-closed-place estimate and says nothing about zeros
of one individual L-function.

## 1. The full-place auxiliary curve

For a marked set `A`, the source-convention polynomial in the locked
multi-place identity is

\[
 f_A(x)=\prod_{a\in A}(a-x).
\]

At `A=F_q`, because `q` is odd,

\[
 f_A(x)=(-1)^q\prod_{a\in\mathbf F_q}(x-a)
 =-(x^q-x)=x-x^q.
\tag{1.1}
\]

The degree is odd, so infinity is ramified and contributes one rational
point.  For every `x in F_q`, the right side of (0.5) is zero.  Hence

\[
 \#C_q(\mathbf F_q)=q+1,
\qquad \sum_{i=1}^{q-1}\alpha_i=0,
\tag{1.2}
\]

where the `alpha_i` are the reciprocal roots of `P_q`.

The `F_(q^2)` count determines every root.  The linear map

\[
 L(x)=x-x^q
\]

has kernel `F_q` and image the one-dimensional trace-zero line

\[
 V=\{v\in\mathbf F_{q^2}:v^q=-v\}.
\]

Choose `zeta in V^times`.  Every nonzero element of `V` is `zeta*t` with
`t in F_q^times`, and every such `t` is a square in `F_(q^2)`.  Moreover

\[
 \zeta^{q-1}=-1,
\]

so its quadratic character in `F_(q^2)` is

\[
 \chi_2(\zeta)
 =\zeta^{(q^2-1)/2}
 =(-1)^{(q+1)/2}=s_q.
\tag{1.3}
\]

Each value in `V` has `q` preimages.  Therefore

\[
 \sum_{x\in\mathbf F_{q^2}}\chi_2(x-x^q)
 =q(q-1)s_q
\]

and

\[
 \boxed{
 \#C_q(\mathbf F_{q^2})
 =q^2+1+q(q-1)s_q.}
\tag{1.4}
\]

Newton's point-count identity gives

\[
 \sum_{i=1}^{q-1}\alpha_i^2=-q(q-1)s_q.
\tag{1.5}
\]

Each summand has absolute value `q` by the Weil theorem, and the right side
has the maximal possible absolute value `q(q-1)`.  Equality in the triangle
inequality forces

\[
 \alpha_i^2=-qs_q
 \quad\text{for every }i.
\tag{1.6}
\]

Equation (1.2) then makes the two square roots occur with equal multiplicity
`g`.  Taking their characteristic polynomial proves (0.6).  No extension
field is enumerated in the replay; (1.4) is a linear-algebra count.

This curve calculation is externally known.  Lemma 1 of Setayesh--Tsimerman,
[*High ell-torsion rank for class groups over function
fields*](https://arxiv.org/abs/2006.07987), records `g` copies of the two
eigenvalues `+-sqrt(q*)` for `y^2=x^q-x`, with
`q*=(-1)^((q-1)/2)q`.  The source-convention curve (0.5) is its `-1`
quadratic twist; the eigenvalue squares, and hence the displayed even
numerator, agree.  No novelty is claimed for the supersingular curve or its
zeta function.  The project-specific result is its insertion into the exact
evaluation-character adapter, producing the full-place correlation law.

## 2. The family correlation series

The exact multi-place theorem says, for `m` distinct rational places,

\[
 \sum_{n\ge0}\sum_{D\in\mathcal H_n(q)}
 \prod_{a\in A}\chi(D(a))u^n
 =L(u,\psi_A){1-qu^2\over(1-u^2)^m}.
\tag{2.1}
\]

Here `m=q` is odd.  Infinity is ramified, so the finite Dirichlet polynomial
is exactly the curve numerator:

\[
 L(u,\psi_{\mathbf F_q})=P_q(u).
\tag{2.2}
\]

Substitution of (0.6) into (2.1) proves (0.3)--(0.4).

The even-degree rows are also explicit.  Put

\[
 B_{q,r}=\binom{q+r-1}{r}
 -q\binom{q+r-2}{r-1},
\qquad B_{q,0}=1,
\tag{2.3}
\]

with `B_(q,r)=0` for `r<0`.  Then

\[
 \boxed{
 S^{\mathrm{full}}_{2k,q}
 =\sum_{j=0}^{\min(g,k)}
 \binom gj(s_qq)^jB_{q,k-j}.}
\tag{2.4}
\]

Thus the theorem gives the entire family-correlation tower, not just the
odd vanishing.

## 3. How this differs from the fixed-degree exterior notch

For fixed family degree `n`, the earlier marked-place theorem found top
exterior-channel cancellation at `m=2n-1` and `m=2n`.  That law is imposed
by symplectic reciprocity on one coefficient channel.

The present notch has a different shape:

\[
 m=q,\qquad n\text{ arbitrary and odd}.
\]

All rational evaluation places are opened at once, and the entire auxiliary
L-polynomial is even.  The simultaneous odd-degree vanishing therefore
persists through every coefficient extraction.  The two mechanisms can
coincide numerically for a special pair `(n,q)`, but neither implies the
other.

This is a useful warning for growing-mark experiments.  A large marked-place
correlation can reach an exact geometric symmetry stratum that is invisible
in any fixed-`m`, `q->infinity` calculation.  The `m` and `q` limits do not
commute without tracking the auxiliary curve.

## 4. Bounded controls and claim boundary

The replay records formula panels at `q=3,5,7,9,11`.  It independently
enumerates only:

- all monic polynomials through degree five over `F_3`;
- all monic polynomials through degree three over `F_5`.

It filters squarefree inputs by a polynomial gcd and checks the complete
product over all rational places.  The 520 candidate polynomials reproduce
every formula row, including

\[
\begin{array}{c|rrrrrr}
q=3, n&0&1&2&3&4&5\\ \hline
S^{\mathrm{full}}_{n,3}&1&0&3&0&-3&0,
\end{array}
\]

and the `q=5` rows `1,0,-10,0`.  These are convention controls; the all-field
proof is Sections 1--2.

Proved exactly:

- the auxiliary curve identification (0.5);
- its complete numerator (0.6) for every odd prime power;
- the full generating series (0.3);
- all odd-degree vanishings and every even coefficient (2.4).

Not proved or claimed:

- external novelty or priority;
- a correlation over varying closed places or conductor degree;
- an FFPS physical-source adapter;
- a memberwise sign or zero statement;
- RH or GRH.
