# Transfer-matrix parents for coefficient powers

Status: **exact parent--shadow theorem and determinant-compression
classification; standard tensor algebra, external novelty not claimed**

Issue: [#764](https://github.com/gfreund123/riemann/issues/764)

Claim labels:
`GLO764.TENSOR_PARENT_IDENTITY`,
`GLO764.GENERIC_POWER_MINIMAL_DENOMINATOR`,
`GLO764.DETERMINANT_ONE_SPECTRAL_COMPRESSION`,
`GLO764.HIGHER_RANK_DETERMINANT_QUOTIENT`, and
`GLO764.FINITE_PARENT_INTERPOLATION_OBSTRUCTION`.

## Start here

The earlier Gate-0 packets classified two scalar coefficient-power series.
This packet answers a different question required by the programme:

> What honest non-scalar object explains the rational integer-power cases?

For a matrix coefficient

\[
 a_r=\ell(A^rv),
\]

the pointwise power `a_r^k` is itself a matrix coefficient of the genuine
symmetric-power representation `Sym^k(A)`.  Thus the scalar generating
function is a shadow of an independently defined finite-dimensional parent:

\[
 \sum_{r\geq0}a_r^kT^r
 =\ell^{\odot k}
   (I-T\operatorname{Sym}^k A)^{-1}
   v^{\odot k}.
\]

The determinant results identify a structural feature hidden by the
determinant-one normalization.  For a polynomial transform of degree at most
`d`, a generic rank-two diagonal parent has

\[
 \binom{d+2}{2}
\]

distinct weights.  Imposing `det(A)=1` collapses the same filtered parent to
only `2d+1` distinct weights.  The linear recurrence bound in the first
packet is therefore a determinant-one spectral compression, not the generic
rank-two law.  In rank `n`, the same character-lattice quotient changes the
filtered count from `binom(n+d,n)` to
`binom(n+d,n)-binom(d,n)`.

These are local representation statements.  They construct no global Euler
product, completion, automorphic lift, motive, explicit formula, or zero
theorem, and they have no RH or GRH consequence.

## 1. The honest parent

Let `R` be a commutative characteristic-zero ring, let `V` be a finite free
`R`-module, and take

\[
 A\in\operatorname{End}_R(V),\qquad
 v\in V,\qquad \ell\in V^*.
\]

Put `a_r=ell(A^r v)`.  The symmetric tensor `v^(odot k)` lies in
`Sym^k(V)`, and `ell^(odot k)` lies in its dual.

### Theorem GLO764.TENSOR_PARENT_IDENTITY

For every integer `k>=0` and every `r>=0`,

\[
 \boxed{
 a_r^k
 =\ell^{\odot k}
   \bigl((\operatorname{Sym}^k A)^r v^{\odot k}\bigr).
 }
\tag{1.1}
\]

Consequently, as a formal power series,

\[
 \boxed{
 \sum_{r\geq0}a_r^kT^r
 =\ell^{\odot k}
  (I-T\operatorname{Sym}^k A)^{-1}v^{\odot k}.
 }
\tag{1.2}
\]

Its reduced denominator divides

\[
 \det(I-T\operatorname{Sym}^k A).
\tag{1.3}
\]

The resolvent matrix coefficient in (1.2) is generally

\[
 \frac{N_{k,A,\ell,v}(T)}
      {\det(I-T\operatorname{Sym}^k A)},
\]

not the determinant inverse itself.  The numerator defects in the earlier
Gate-0 packet are concrete witnesses to this distinction.  The parent
therefore explains finite recurrence and its possible poles; it does **not**
identify the coefficient-power Euler factor with the usual symmetric-power
`L`-factor.

### Proof

The tensor identity

\[
 (\ell(A^rv))^k
 =(\ell^{\otimes k})
  ((A^{\otimes k})^rv^{\otimes k})
\]

is functorial.  Both pure tensors are symmetric, and the restriction of
`A^(tensor k)` to the symmetric tensors is `Sym^k(A)`.  This proves (1.1).
Summing the geometric resolvent gives (1.2), and every matrix coefficient of
a finite resolvent has denominator dividing its characteristic determinant.
\(\square\)

This is an honest object rather than a fitted realization: `Sym^k` exists
before the scalar sequence or its generating function is evaluated, respects
change of basis, and is functorial in `A`.

## 2. Exact generic denominator in rank two

Work over a field and suppose that `A` is diagonalizable with eigenvalues
`alpha,beta`.  In an eigenbasis write

\[
 a_r=c_\alpha\alpha^r+c_\beta\beta^r.
\tag{2.1}
\]

Then

\[
 a_r^k
 =\sum_{j=0}^k
   \binom{k}{j}
   c_\alpha^{k-j}c_\beta^j
   (\alpha^{k-j}\beta^j)^r.
\tag{2.2}
\]

### Theorem GLO764.GENERIC_POWER_MINIMAL_DENOMINATOR

Assume `c_alpha*c_beta != 0` and that the `k+1` weights

\[
 \alpha^{k-j}\beta^j,
 \qquad 0\leq j\leq k,
\]

are pairwise distinct.  Then the reduced denominator is exactly

\[
 \boxed{
 D_{k,A}(T)=
 \prod_{j=0}^k
 (1-\alpha^{k-j}\beta^jT),
 }
\tag{2.3}
\]

and the minimal recurrence order is `k+1`.

### Proof

Equation (2.2) is a partial-fraction decomposition with distinct poles and
nonzero coefficients.  At the reciprocal of one weight, precisely one term
has a nonzero residue.  No factor cancels. \(\square\)

The hypotheses are necessary.  If one eigen-coordinate vanishes, some
weights are absent.  If `alpha/beta` is a root of unity, distinct symmetric
weights can collide.  These are structural degeneration loci, not failures
of the parent identity.

## 3. Polynomial transforms and the filtered parent

Let

\[
 \Phi(z)=\sum_{k\in S}c_kz^k,
 \qquad c_k\ne0,
 \qquad S\subseteq\{0,\ldots,d\}.
\]

There is a canonical parent

\[
 \mathcal P_\Phi(A)
 =\bigoplus_{k\in S}\operatorname{Sym}^k(A),
\tag{3.1}
\]

with the scalar coefficients `c_k` placed in the output covector.  Therefore
`Phi(a_r)` is a matrix coefficient of (3.1).  This proves rationality without
inventing a scalar local factor.

The parent dimension is

\[
 \sum_{k\in S}(k+1).
\tag{3.2}
\]

For the full degree filtration `S={0,...,d}`, it is

\[
 N_d=\frac{(d+1)(d+2)}2.
\tag{3.3}
\]

### Generic two-torus spectrum

The possible weights are

\[
 \mathcal R_d^{(2)}
 =\{\alpha^a\beta^b:a,b\geq0,\ a+b\leq d\}.
\tag{3.4}
\]

If `alpha` and `beta` are multiplicatively independent, every exponent pair
is distinct, and

\[
 |\mathcal R_d^{(2)}|
 =\binom{d+2}{2}.
\tag{3.5}
\]

Thus the generic filtered scalar shadow sees the full triangular parent
spectrum.

### Determinant-one spectrum

If `alpha*beta=1`, the weight attached to `(a,b)` becomes

\[
 \alpha^{a-b}.
\]

As `(a,b)` ranges over the triangle `a+b<=d`, the difference `a-b` ranges
over every integer from `-d` to `d`.  Hence

\[
 \mathcal R_d^{(1)}
 =\{\alpha^n:-d\leq n\leq d\},
 \qquad
 |\mathcal R_d^{(1)}|=2d+1,
\tag{3.6}
\]

provided `alpha` is not a root of unity.

### Theorem GLO764.DETERMINANT_ONE_SPECTRAL_COMPRESSION

For the full filtered parent through degree `d`, the generic two-torus
spectrum has triangular size `(d+1)(d+2)/2`.  On the determinant-one torus it
has only `2d+1` distinct weights.  The compression is the quotient of the
exponent triangle by

\[
 (a,b)\longmapsto a-b.
\tag{3.7}
\]

This explains, but does not improve, the `2d+1` recurrence bound in the first
Gate-0 packet.

### Proof

The exponent pairs in (3.4) are exactly the lattice points in the triangle
`a,b>=0`, `a+b<=d`, whose count is (3.5).  Multiplicative independence makes
the weight map injective.  Under `alpha*beta=1`, the map factors through
(3.7).  Every integer `n` in `[-d,d]` occurs: take `(n,0)` for `n>=0` and
`(0,-n)` for `n<0`.  This gives (3.6). \(\square\)

## 4. Higher-rank determinant quotient

The rank-two compression is the first case of a general weight-polytope
quotient.  Let `V` have rank `n`, and consider the full filtered parent

\[
 \mathcal P_{n,d}(A)
 =\bigoplus_{k=0}^d\operatorname{Sym}^k(A).
\tag{4.1}
\]

For a diagonal matrix with eigenvalues
`alpha_1,...,alpha_n`, its weight exponents are

\[
 E_{n,d}
 =\left\{
 (a_1,\ldots,a_n)\in\mathbb Z_{\geq0}^n:
 \sum_i a_i\leq d
 \right\}.
\tag{4.2}
\]

Stars and bars gives

\[
 |E_{n,d}|=\binom{n+d}{n}.
\tag{4.3}
\]

On the determinant-one torus, exponent vectors define the same character
exactly when they differ by an integer multiple of `(1,...,1)`, assuming no
further character relation.

### Theorem GLO764.HIGHER_RANK_DETERMINANT_QUOTIENT

The generic rank-`n` torus spectrum of (4.1) has

\[
 \binom{n+d}{n}
\]

distinct characters.  Its restriction to the generic determinant-one torus
has exactly

\[
 \boxed{
 Q_{n,d}
 =\binom{n+d}{n}-\binom{d}{n},
 }
\tag{4.4}
\]

where `binom(d,n)=0` for `d<n`.

### Proof

Every class in
`Z^n / Z(1,...,1)` represented by `a in E_(n,d)` has the canonical
representative

\[
 a^\circ=a-\min_i(a_i)(1,\ldots,1).
\tag{4.5}
\]

It is nonnegative, has at least one zero coordinate, and remains in
`E_(n,d)`.  Conversely, two nonnegative representatives with a zero
coordinate cannot differ by a nonzero multiple of `(1,...,1)`.  The desired
count is therefore obtained from the unique representative with minimum
coordinate zero: it is the number of exponent vectors in (4.2) with at least
one zero coordinate.

There are `binom(n+d,n)` vectors in all.  Vectors with every coordinate
positive are in bijection, after subtracting one from every coordinate, with
nonnegative vectors whose sum is at most `d-n`; their count is `binom(d,n)`.
Subtracting proves (4.4). \(\square\)

For fixed `n>=2`,

\[
 Q_{n,d}
 =\frac{n}{(n-1)!}d^{n-1}+O_n(d^{n-2}).
\tag{4.6}
\]

Thus one determinant relation lowers the degree of filtered spectral growth
by one.  The theorem counts characters of the honest parent.  A particular
scalar observable can still cancel characters and have a smaller reduced
denominator.

More generally, imposing several independent monomial relations asks for
the image of `E_(n,d)` in a quotient character lattice.  Its exact count and
Ehrhart behaviour form a concrete determinant/moduli continuation, not a
claim of a new `L`-function.

## 5. Why determinant is load-bearing

For a fixed power `k`, both generic and determinant-one parents have `k+1`
weights.  The compression appears when several degrees are combined.

If `delta=alpha*beta` remains an independent parameter, then

\[
 \alpha^{k-j}\beta^j
 =\alpha^{k-2j}\delta^j.
\tag{5.1}
\]

The two exponent coordinates in (5.1) retain the triangular count.  Setting
`delta=1` discards the second coordinate and creates the linear count.
Therefore the determinant-one polynomial-transform bound must not be exported
unchanged to a varying-determinant family.

This is the held-out prediction of the parent viewpoint: a deformation that
frees the determinant should generically restore quadratic, not linear,
spectral growth across polynomial degrees.

## 6. Finite-parent interpolation obstruction

The parent theorem also converts the earlier scalar nonrationality theorem
into an object-level obstruction.  Fix real `x>2` and let

\[
 u_0=1,\qquad u_1=x,\qquad
 u_{r+2}=xu_{r+1}-u_r.
\]

Use the positive real logarithm to define `u_r^lambda` for complex `lambda`.

### Theorem GLO764.FINITE_PARENT_INTERPOLATION_OBSTRUCTION

There exist a finite-dimensional complex vector space `W`, an endomorphism
`B`, a vector `w`, and a covector `phi` satisfying

\[
 u_r^\lambda=\phi(B^rw)\qquad(r\geq0)
\tag{6.1}
\]

if and only if `lambda` is a nonnegative integer.

### Proof

Every finite-dimensional matrix coefficient has rational generating function:

\[
 \sum_{r\geq0}\phi(B^rw)T^r
 =\phi((I-TB)^{-1}w).
\tag{6.2}
\]

The authenticated source theorem classifies the left side of (6.1) as
rational exactly when `lambda` is a nonnegative integer.  This proves the
only-if direction.

Conversely, put

\[
 A=\begin{pmatrix}x&-1\\1&0\end{pmatrix},\qquad
 v=\begin{pmatrix}x\\1\end{pmatrix},\qquad
 \ell=(0,1).
\]

Then `u_r=ell(A^r v)`.  For `lambda=k>=0`, Theorem
`GLO764.TENSOR_PARENT_IDENTITY` realizes `u_r^k` on `Sym^k(C^2)`.
\(\square\)

This theorem rules out finite-dimensional vector-space parents with an exact
matrix-coefficient shadow.  It does not rule out nuclear operators,
regularized determinants, Deligne or other complex-rank categories,
categorical traces, or approximate/interpolated shadows.  Those are now the
correctly located research frontier rather than conclusions of this packet.

## 7. Counterfeits and degeneration controls

The exact replay includes three hostile controls.

1. **Multiplicatively independent roots.** `alpha=2,beta=3` realizes the
   triangular count exactly.
2. **Determinant one.** `alpha=2,beta=1/2` realizes the `2d+1` quotient.
3. **Dependent roots.** `alpha=2,beta=4` produces cross-degree collisions,
   showing that a numerical count without the independence hypothesis is not
   a moduli theorem.

The higher-rank replay adds ranks `2` through `5` and checks every degree
through `8` against (4.4).  These rows test the quotient formula; the proof is
the canonical-representative argument above.

It also checks the non-unit-determinant recurrence

\[
 u_0=1,\quad u_1=5,\quad
 u_{r+2}=5u_{r+1}-6u_r,
\]

whose roots are `3,2`.  The identity

\[
 u_r=3\cdot3^r-2\cdot2^r
\]

is replayed together with its exact power parents and minimal denominators.

## 8. Structural survival ledger

| object | L0 | L1--L2 | L3 | first unresolved level |
|---|---|---|---|---|
| monomial coefficient power `a_r^k` | exact | preserves a multiplicative coefficient system | honest rational local parent `Sym^k(A)` | L4: ramified, determinant and duality coherence in a global family |
| polynomial transform `Phi(a_r)` | exact | universal multiplicativity fails unless `Phi` is a normalized monomial | rational via a direct sum of symmetric parents | L1 in general |
| noninteger positive-branch power | branch-defined in the earlier chamber | no global coherence proved | no finite rational parent in the earlier theorem | L3 |

The local symmetric parent is a genuine representation-theoretic object, but
calling it a global symmetric-power `L`-function would additionally require
primewise parameters, ramified factors, functorial compatibility, completion,
and analytic realization.  None is supplied here.

Complex-rank tensor categories are a genuine neighbouring theory, not an empty
name for the failed finite-dimensional interpolation.  Determining whether a
categorical trace can reproduce these particular noninteger shadows while
retaining duality and primewise coherence remains open here.

## 9. Literature and novelty firewall

Integer powers and generating functions of second-order recurrences are
classical.  A nearby primary source is Pantelimon Stănică,
[*Generating Functions, Weighted and Non-Weighted Sums for Powers of
Second-Order Recurrence Sequences*](https://arxiv.org/abs/math/0010149),
which explicitly treats closed generating functions for integer powers.

Complex-rank representation theory is also established territory: Pavel
Etingof's [*Representation theory in complex rank,
I*](https://arxiv.org/abs/1401.6321) develops interpolating tensor categories.
The finite-parent obstruction above must not be advertised as an obstruction
to that theory; it only says that an exact realization cannot remain a
finite-dimensional complex vector-space matrix coefficient.

The tensor-parent proof above is elementary representation theory, and this
packet makes no novelty or priority claim for it.  The value here is the
programme-level distinction between:

```text
scalar transformed coefficients;
the honest symmetric-tensor parent;
generic two-torus spectral complexity;
determinant-one spectral compression;
higher-rank character-lattice quotient.
```

A specialist literature comparison is required before presenting the precise
filtered-compression packaging as new.

## 10. Replay and scope

Run from the repository root:

    python -B research/l-families/atlas/generalized/transfer_matrix_symmetric_parent.py --check
    python -B -O research/l-families/atlas/generalized/transfer_matrix_symmetric_parent.py --check
    python -B -m unittest tests.test_transfer_matrix_symmetric_parent
    python -B -O -m unittest tests.test_transfer_matrix_symmetric_parent

The replay uses exact integers, fractions, binomial coefficients, exponent
pairs, and polynomial recurrences.  It enumerates no primes, curves,
conductors, zeros, automorphic forms, or parameter grids and performs no
floating-point arithmetic.

The packet is a local parent--shadow theorem and determinant-compression
classification.  RH and GRH remain unproved.
