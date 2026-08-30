# Multiplicative recurrence preservers and mixed-rank determinant parents

Status: **proposed exact local theorems; independent review pending; no
external novelty claim**.

Scope: continuous multiplicative maps on the complex numbers, ordinary
constant-coefficient recurrences, and universal finite graded determinant
identities for finite-dimensional representations. This is not a global
L-function construction, an arithmetic realization, or an RH/GRH result.

Exact source: `ab7ebfa3d4e3f1a657b4127b40796953060b6b3e`, the eleven-packet
state of [PR #766](https://github.com/gfreund123/riemann/pull/766). The source
manifest authenticates the dense-orbit precursor and equal-rank finite-graded
parent theorem. Their proofs are not inferred from generated fixtures.

What is replayed: exact Laurent coefficients, finite spectrum aggregation,
Gaussian-rational local sequences and denominator annihilation, mixed-rank
identity numerators by two methods, rational Sturm controls, and independent
rank-two tensor determinants. See Section 8 for the exact boundary.

Smallest remaining burden: frozen-source independent review. Global
compatibility and analytic convergence of infinite graded products remain
open. The graph/non-scalar comparison, if supplied separately, has its own
source and does not become an arithmetic adapter by analogy.

## 1. A single nondegenerate circle classifies all multiplicative maps

A sequence is **recurrent** here if it satisfies a nonzero
constant-coefficient linear recurrence for every sufficiently large index.
Equivalently its ordinary generating series is rational. Minimal order means
the degree of its reduced denominator, so finite prefixes do not matter.

### Theorem GLO764.MULREC.SHIFTED_CIRCLE_RIGIDITY

Let `Phi:C->C` be continuous, satisfy `Phi(1)=1`, and obey

\[
 \Phi(zw)=\Phi(z)\Phi(w)\quad(z,w\in\mathbb C).
\tag{1.1}
\]

Fix **any one** real `c>1` and `theta/(2pi)` irrational. The following are
equivalent:

1. `b_r=Phi(c+exp(i r theta))`, `r>=0`, is recurrent;
2. there are unique integers `m,n>=0` such that
   `Phi(z)=z^m conjugate(z)^n` for every `z in C`;
3. applying `Phi` termwise to every complex recurrent sequence again gives
   a recurrent sequence.

For `(m,n)=(0,0)` the map is identically one, including at zero. In every
other case its value at zero is zero. In case 1 the minimal order is exactly
`m+n+1`. No unspecified logarithm or termwise branch choice occurs.

#### Proof: multiplicative coordinates

For `z!=0`, (1.1) gives `Phi(z)Phi(1/z)=1`; therefore `Phi(z)!=0`.
A continuous homomorphism from the circle to `C^*` has compact image, hence
unit modulus, and is `exp(it)->exp(ikt)` for one integer `k`. For
completeness, lift it continuously along `t in R` with value zero at `t=0`;
the lift is additive modulo `2pi`, hence additive by continuity, and its
periodicity forces its slope to be an integer. Likewise, taking a continuous
logarithm of the homomorphism `t->Phi(exp t)` on the simply connected real
line makes its logarithm additive, so it is `a t` for some `a in C`.
Consequently

\[
 \Phi(r e^{it})=\exp(a\log r)e^{ikt},\qquad r>0,
 \quad a\in\mathbb C,\ k\in\mathbb Z.
\tag{1.2}
\]

If `Phi(0)!=0`, applying multiplicativity to `0*z` makes `Phi` identically
one. Otherwise continuity at zero forces `Re(a)>0`: its modulus is
`r^Re(a)`. We will not need a choice of argument outside the factor
`e^{ikt}`, which is single valued because `k` is integral.

#### Proof: recurrence forces finite Fourier support

For any continuous `2pi`-periodic `f`, an eventual recurrence for
`f(r theta)` gives a nonzero polynomial `Q` such that a finite linear
combination `sum_j q_j f(t+j theta)` vanishes on a tail of the irrational
orbit. The tail is dense, so the combination vanishes everywhere. Fourier
coefficients therefore satisfy

\[
 Q(e^{i\ell\theta})\widehat f(\ell)=0\quad(\ell\in\mathbb Z).
\tag{1.3}
\]

The arguments `exp(i ell theta)` are distinct and `Q` has finitely many
roots. Thus only finitely many Fourier coefficients survive. Fourier
uniqueness for continuous functions, for example by Fejer means, makes `f`
a Laurent polynomial on the unit circle. Conversely such a polynomial
clearly yields a finite exponential sum.

Apply this to `f(t)=Phi(c+exp(it))`. Put

\[
 \mu=(a+k)/2,\quad \nu=(a-k)/2.
\]

On the annulus `1/c<|w|<c`, both `c+w` and `c+w^(-1)` have the logarithms
defined by their convergent expansions about `c`. Hence

\[
 F(w)=\exp\{\mu\log(c+w)+\nu\log(c+w^{-1})\}
\tag{1.4}
\]

is holomorphic and nonzero there. On `|w|=1`, the two logarithms are
complex conjugates, so (1.2) shows `F(w)=Phi(c+w)`. Thus the Laurent
polynomial `P` obtained from (1.3) equals `F` on the annulus, by the identity
theorem. It is nonzero, and

\[
 \frac{P'(w)}{P(w)}
 =\frac{\mu}{c+w}-\frac{\nu}{w(cw+1)}.
\tag{1.5}
\]

Both sides are rational functions, so equality on the annulus is global.
The points `-c` and `-1/c` are distinct, finite, and nonzero. The right
side has residues `mu` and `nu` there. At any nonzero finite point, the
logarithmic derivative of a nonzero Laurent polynomial has residue equal
to its zero multiplicity, a nonnegative integer (zero when there is no
zero). Therefore `mu=m` and `nu=n` lie in `Z_{>=0}`. Equation (1.2) is now
`Phi(z)=z^m conjugate(z)^n` away from zero, and continuity gives the stated
value at zero. This proves `1=>2` without analytic continuation of a
multivalued power across a chosen branch cut.

At these exponents,

\[
 (c+w)^m(c+w^{-1})^n
 =\sum_{\ell=-n}^{m} C_\ell w^\ell,
\quad
 C_\ell=\sum_{i-j=\ell}\binom mi\binom nj c^{m+n-i-j}>0.
\tag{1.6}
\]

Every integer between `-n` and `m` occurs. Irrationality makes the sampled
roots distinct, and each nonzero coefficient gives an actual simple pole
in `sum_r b_r T^r`. The order is exactly `m+n+1`.

Finally, recurrent sequences are eventually exponential polynomials
`sum_j p_j(r) lambda_j^r`, apart from terms of finite support. Complex
conjugation and finite products preserve this form, as do finite prefix
changes. Thus `2=>3`. The sequence `c+exp(i r theta)` is itself recurrent,
so `3=>1`. Uniqueness of `m,n` follows from `a=m+n,k=m-n`. QED.

### Why the hypotheses are load bearing

- A circle centered at zero tests only `e^{ikt}` and sees no radial
  exponent. Every continuous map `r^a e^{ikt}` with `Re(a)>0` passes it.
- The origin-touching circle `1+exp(it)` is also insufficient. The
  continuous multiplicative map `Phi(z)=z^2/conjugate(z)` for `z!=0`,
  `Phi(0)=0`, is not a polynomial in `z,conjugate(z)`, but
  `Phi(1+w)=w+w^2` on `|w|=1`, including `w=-1`. In (1.5) its two
  singularities have collided; `c>1` prevents exactly this cancellation.
- A rational rotation is periodic and tests no rationality rigidity.
- Without multiplicativity, changing a continuous function outside the
  tested circle preserves every sampled value. For example
  `1+max(0,|z|-(c+1))` is constant one on the circle and at `z=1`, but is
  not a multiplicative map. One orbit cannot classify such functions.

## 2. Multicoefficient version and exact operation laws

### Corollary GLO764.MULREC.MULTICOEFFICIENT_RIGIDITY

Let `Psi:C^q->C` be continuous and multiplicative for coordinatewise
products, with `Psi(1,...,1)=1`. Suppose its restriction to each coordinate
axis with all other coordinates equal to one passes one nondegenerate
shifted-circle test from Section 1. Then, uniquely,

\[
 \Psi(z_1,\ldots,z_q)=\prod_{j=1}^q z_j^{m_j}\bar z_j^{n_j},
 \qquad m_j,n_j\in\mathbb Z_{\ge0}.
\tag{2.1}
\]

Indeed multiplicativity splits `Psi` into its coordinate restrictions;
apply Theorem 1 to each. The coordinatewise tests are explicit assumptions:
one correlated multivariable orbit is not silently substituted for them.

For one surviving map the exact scalar twist law is

\[
 \Phi(\eta z)=\eta^m\bar\eta^n\Phi(z).
\tag{2.2}
\]

Thus its unitary twist weight is `m-n`, whereas its positive-dilation
degree is `m+n`. Requiring the **same** unitary twist as the input gives
`m-n=1`, but still permits every `z^{n+1}bar z^n`; twist weight alone is
not holomorphy. Requiring the same twist for every `eta in C^*` forces
`m=1,n=0`. Additivity likewise forces `m+n=1`, since at `1+1` it says
`2^{m+n}=2`; the two remaining maps are identity and conjugation.

For a matrix `A`, the tensor representation
`A^(tensor m) tensor conjugate(A)^(tensor n)` has character
`Phi(Tr A)`. Consequently multiplicativity of traces under tensor products
is coherent in these coordinates. This does **not** identify the complete
symmetric-coefficient series
`sum_r Phi(Tr(Sym^r A))T^r` with a determinant inverse of that tensor
representation. Sections 4--6 classify this different question.

### Theorem GLO764.MULREC.DISCRETE_DEFORMATION_MODULI

For an integer `D>=1`, the normalized continuous multiplicative maps whose
shifted-circle order is at most `D` form exactly

\[
 \{z^m\bar z^n:m,n\ge0,\ m+n\le D-1\}.
\]

Their number is `D(D+1)/2`. At fixed integral unitary twist weight `w`,
the number is

\[
 \max\left(0,1+\left\lfloor\frac{D-1-|w|}{2}\right\rfloor\right).
\tag{2.3}
\]

Moreover, any family of maps satisfying Theorem 1 for which evaluation at
each fixed complex number varies continuously has locally constant
exponents `(m,n)`. In particular a family over a connected parameter space
is constant, even without a prescribed uniform order bound.

Proof: Theorem 1 gives order `m+n+1`; counting the integer triangle proves
the first assertion. At fixed `w=m-n`, the possible total degrees are
`|w|,|w|+2,...,D-1`, giving (2.3). For the last assertion, evaluation at
`2` has value `2^{m+n}` in a discrete set. The total degree is therefore
locally constant. On a neighborhood where it is `K`, only `K+1`
bidegrees remain. Evaluation at one fixed `eta=exp(i alpha)` with
`alpha/(2pi)` irrational distinguishes their integer weights. Its finite
image is discrete, so the weight, and hence both exponents, are locally
constant. A locally constant map on a connected space is constant. QED.

This is a precise obstruction to continuous interpolation **inside these
scalar axioms**. It says nothing about p-adic interpolation, discontinuous
families, changing target categories, or infinite-dimensional parents that
do not retain the recurrence hypothesis.

## 3. Sharp generic orders and exact cancellation semantics

### Theorem GLO764.MULREC.GENERIC_BIDEGREE_ORDER

Let `a_r=sum_(j=1)^d b_j lambda_j^r`, with `lambda_j,b_j` nonzero complex
numbers. Fix `m,n>=0`. For compositions `|u|=m`, `|v|=n`, put

\[
 \omega_{u,v}=\lambda^u\bar\lambda^v,
 \qquad
 B_{u,v}=\binom m{u}\binom n{v}b^u\bar b^v.
\tag{3.1}
\]

The transformed sequence is `sum_(u,v) B_(u,v) omega_(u,v)^r`.
Its reduced denominator is exactly

\[
 \prod_{\omega:\,\sum_{\omega_{u,v}=\omega}B_{u,v}\ne0}(1-\omega T).
\tag{3.2}
\]

If all displayed roots are distinct, its order is

\[
 \boxed{\binom{d+m-1}{m}\binom{d+n-1}{n}.}
\tag{3.3}
\]

Proof: the multinomial expansion gives (3.1). Sum equal roots **with their
coefficients**, discard zero sums, and sum the surviving geometric series.
Distinct poles with nonzero residues cannot cancel. This proves (3.2) and
(3.3). The distinctness hypothesis is nonempty: choose `lambda_j=p_j
exp(i theta_j)` with distinct primes `p_j` and `1,theta_1/(2pi),...,
theta_d/(2pi)` rationally independent. Equality of moduli first gives
`u+v=u'+v'` by unique prime factorization, and equality of phases gives
`u-v=u'-v'`; thus the pairs coincide. QED.

For a rank-`d` semisimple matrix with distinct nonzero eigenvalues,

\[
 h_r(A)=\operatorname{Tr}(\operatorname{Sym}^r A)
       =\sum_j b_j\lambda_j^r,
 \qquad b_j=\frac{\lambda_j^{d-1}}
                  {\prod_{i\ne j}(\lambda_j-\lambda_i)}\ne0.
\tag{3.4}
\]

Hence this theorem applies to the actual local coefficient normalization.
It also constructs a matrix-coefficient parent on
`Sym^m(C^d) tensor Sym^n(conjugate(C^d))`, using the Binet state realization
and tensoring its input/output vectors. The Binet output vectors depend on
the matrix and can become singular when eigenvalues coalesce. This is an
honest representation state space with a recovery map on the distinct-root
locus, not one universal fixed matrix coefficient valid for every matrix.

Reality, determinant constraints, torsion, repeated roots, or special output
vectors may lower the count. For real roots, conjugation already identifies
weights, so (3.3) must not be used. Repeated eigenvalues, even in diagonalizable
matrices, can produce polynomial-in-`r` factors and higher pole orders in
the complete symmetric-coefficient sequence. Such sequences, including
Jordan cases, remain recurrent; the simple-pole formula (3.2) is asserted
only as stated.

## 4. The mixed-rank determinant-parent question

Let `V_1,...,V_k` be the defining representations of
`G=product_i GL_(d_i)(C)`, with `d_i>=1`. Set

\[
 F_{\boldsymbol d}(\boldsymbol A,T)
  =\sum_{r\ge0}\prod_{i=1}^k
      \operatorname{Tr}(\operatorname{Sym}^r A_i)T^r.
\tag{4.1}
\]

A **universal finite graded virtual determinant parent** is a finite list
`R_1,...,R_D` of virtual finite-dimensional continuous complex
representations of `G`, independent of `A`, with

\[
 F_{\boldsymbol d}(\boldsymbol A,T)
 =\prod_{j=1}^D\det(1-T^j R_j(\boldsymbol A))^{-1}
\tag{4.2}
\]

as formal series for **every** tuple of invertible matrices. A virtual
difference has the quotient-of-determinants meaning. Algebraic
representations are allowed; the obstruction actually needs only
`R_j(I)=I`. Fitted Frobenius scalars not arising from representations are
excluded. No claim is made from equality on a dense set of continuous
representations; the all-matrix quantifier is literal.

### Theorem GLO764.MULREC.MIXED_RANK_FINITE_GRADED_PARENT

Such a parent exists if and only if, after deleting all rank-one factors,
the rank list is one of

\[
 \boxed{(),\qquad(d)\ (d\ge2),\qquad(2,2).}
\tag{4.3}
\]

This extends the equal-rank/repeated-factor boundary at the frozen source
to arbitrary independent local objects. It does not assume that matching
one matrix or a finite sample proves universality.

## 5. Unequal-rank identity numerator and proof of necessity

Write `a_i=d_i-1`, `A=sum_i a_i`, and `M=max_i a_i` (zero when all ranks
are one). At the identity,

\[
 F_{\boldsymbol d}(\boldsymbol I,T)
 =\sum_{r\ge0}\prod_i\binom{r+a_i}{a_i}T^r
 =\frac{H_{\boldsymbol a}(T)}{(1-T)^{A+1}}.
\tag{5.1}
\]

### Lemma GLO764.MULREC.UNEQUAL_SEGRE_ROOTS

`H(0)=1`, `H(1)=A!/product_i a_i! >0`, and `H` has degree `A-M`.
When this degree is positive, all its roots are simple and negative.

#### Native proof

Let `D=T d/dT`. Multiplying the `r`th coefficient by `binom(r+a,a)` is
the operator `product_(j=1)^a (D+j)/j`. Apply the largest factor `M`
first to `1/(1-T)`; its result is `1/(1-T)^(M+1)`.

Suppose some full factors totaling `B>=M` have already been applied, and
we are at step `1<=j<=a<=M` of the next factor. Immediately before that
step the denominator exponent and numerator degree are respectively

\[
 d=B+j,\qquad m=B-M+j-1.
\]

The operation sends `H/(1-T)^d` to `Q/(1-T)^(d+1)`, where

\[
 Q(T)=\frac{[j+(d-j)T]H(T)+T(1-T)H'(T)}j.
\tag{5.2}
\]

If `H` has positive constant and leading coefficients and `m` simple
negative roots, the leading coefficient of `Q` is that of `H` times

\[
 \frac{d-j-m}{j}=\frac{M-j+1}{j}>0.
\tag{5.3}
\]

At successive roots `r_s` of `H`,
`Q(r_s)=r_s(1-r_s)H'(r_s)/j`; these signs alternate. Together with
`Q(0)=H(0)>0` and the leading sign at negative infinity they force one
root in each intervening interval, one to the right of the largest root
and one to the left of the smallest. The new degree is `m+1`, so these
are all the roots and all are simple negative. For `m=0` the formula is
the positive multiple of `1+(d-j)T/j`, with `d-j=B>0`.

Induction adds exactly `sum_(i after largest) a_i=A-M` roots. Rank-one
factors do nothing. The constant stays one. Evaluation of (5.2) at `T=1`
multiplies `H(1)` by `d/j`; telescoping gives `A!/product_i a_i!`.
This also shows that no denominator factor cancels. QED.

At the identity (4.2) becomes `product_(j=1)^D(1-T^j)^(-dim R_j)`.
Every finite zero or pole is a root of unity. If `A-M>=2`, the lemma
gives at least two distinct negative roots, and at most one is a root of
unity, namely `-1`; impossibility follows. If `A-M=1`, the positive
`a_i` are exactly `M,1`; direct first-coefficient comparison gives

\[
 H(T)=1+M T.
\tag{5.4}
\]

Its zero is a root of unity only for `M=1`, hence only two rank-two
factors. If `A-M=0`, there is at most one rank greater than one. This
proves necessity in all cases without a finite extrapolation.

## 6. Construction, formal escape, and a conjugate-input corollary

Let `chi` be the product of all rank-one characters. If there are no other
factors, take `R_1=chi`. If there is one remaining `V`, take
`R_1=chi tensor V`. These are the ordinary symmetric-power identities.

For two rank-two factors `V,W`, one has the universal identity

\[
 \boxed{\sum_{r\ge0}h_r(A)h_r(B)T^r
 =\frac{1-\det(A)\det(B)T^2}
        {\det(1-T(A\otimes B))}.}
\tag{6.1}
\]

For distinct eigenvalues, expand each `h_r` by (3.4), multiply, and sum
four geometric series; multiplication by the four-term denominator
leaves exactly the displayed numerator. Alternatively the four
characteristic roots are `alpha_i beta_j`, and direct expansion gives
the same numerator. Both sides have polynomial formal coefficients in
the matrix entries, so the identity extends to repeated eigenvalues and
Jordan matrices. Restoring rank-one factors replaces `T` by `chi T`:
`R_1=chi tensor V tensor W` and
`R_2=-chi^2 det(V)det(W)`. This proves sufficiency.

There is always a unique **formal** infinite-graded virtual product in
the representation ring:

\[
 \sum_{r\ge0}\left[\bigotimes_i\operatorname{Sym}^r V_i\right]T^r
 =\prod_{j\ge1}\sigma_{T^j}(W_j).
\tag{6.2}
\]

To construct it, remove lower grades and take the coefficient of the first
remaining grade. Since `sigma_(T^j)(W)=1+WT^j+...`, this recursion both
exists and is unique without dividing in the ring. It is only a `T`-adic
identity; no completed vector space or analytic determinant is asserted.

Put `U=tensor_i V_i`. The first two classes are

\[
 W_1=U,\quad W_2=\bigotimes_i\operatorname{Sym}^2V_i-
                         \operatorname{Sym}^2U.
\]

The flip on `U tensor U` is the product of the individual flips. Its
positive eigenspace is the sum of tensor products having an even number
of exterior-square factors. Therefore

\[
 W_2=-\bigoplus_{\substack{S\subseteq\{1,\ldots,k\}\\
                   |S|\ge2,\ |S|\ {\rm even}}}
     \bigotimes_{i\in S}\Lambda^2 V_i\otimes
     \bigotimes_{i\notin S}\operatorname{Sym}^2 V_i.
\tag{6.3}
\]

It has strictly negative dimension exactly when at least two ranks exceed
one. Consequently no **all-effective** graded parent, finite or infinite,
exists in that chamber. Outside the finite cases (4.3), infinitely many
virtual grades are nonzero, by the finite-parent obstruction, not by a
computed tail. Its exact second dimension is

\[
 \dim W_2=\prod_i\binom{d_i+1}{2}
             -\binom{\prod_i d_i+1}{2}.
\tag{6.4}
\]

### Corollary GLO764.MULREC.CONJUGATE_COEFFICIENT_PARENT

For `Phi(z)=z^m bar z^n` and fixed matrix rank `d`, the series
`sum_r Phi(h_r(A))T^r` admits a universal finite graded virtual parent
among continuous complex representations of `GL_d(C)` precisely when

\[
 d=1,\qquad m+n\le1,\qquad\hbox{or}\qquad(d,m+n)=(2,2).
\tag{6.5}
\]

For necessity, evaluation at the identity yields (5.1) with `m+n` copies
of rank `d`, even though the copies and their conjugates are no longer
independent. Sufficiency follows by repeating or conjugating the
constructions above. The `m=n=1,d=2` exception is

\[
 \sum_{r\ge0}|h_r(A)|^2T^r
 =\frac{1-|\det A|^2T^2}
        {\det(1-T(A\otimes\bar A))}.
\tag{6.6}
\]

Conjugation is continuous/real algebraic, not holomorphic algebraic on
`GL_d(C)`. For that reason (6.5) does not claim a classification in the
smaller category of holomorphic algebraic representations.

## 7. Literature boundary and the new scope

The ingredients are established mathematics. No publication priority is
claimed for these statements or their synthesis.

- Knill--Lesieutre, [*Analytic continuation of Dirichlet series with almost
  periodic coefficients*](https://abel.math.harvard.edu/~knill/kam/papers/denjoy/index.html),
  was read in the introduction and almost-periodic Taylor-series section.
  It supplies the nearby Fourier/geometric-series setting. Its stronger
  natural-boundary claims have additional hypotheses; none is imported.
- Ferretti--Zannier, [*Equations in the Hadamard ring of rational
  functions*](https://arxiv.org/abs/math/0701772), abstract checked, treats
  arithmetic equations in recurrence rings over number fields. Section 1
  instead quantifies over continuous multiplicative maps on all complex
  numbers. That distinction is a scope statement, not proof of novelty.
- Morales, [*Segre embeddings, Hilbert series and Newcomb's
  problem*](https://arxiv.org/abs/1306.6910), identifies the classical
  Segre Hilbert numerators. The unequal ranks in Section 5 are still
  classical Segre algebra; the self-contained interlacing proof and
  representation-parent obstruction specify their role here.
- The inherited [finite-graded theorem](FINITE_GRADED_VIRTUAL_PARENT_CLASSIFICATION.md)
  already proves the equal-rank repeated-factor boundary and the formal
  escape. This packet claims the arbitrary independent rank list,
  complex-conjugate transform adapter, and the single shifted-circle
  classification as its additional repository scope.

The scientific gain is a separation of three different compatibility
questions: universal scalar recurrence preservation, an honest
matrix-coefficient parent, and a universal determinant parent. The surviving
class at one level need not survive the next. All-prime Satake deformation
and Estermann continuation work was already active elsewhere at the frozen
base and is deliberately not duplicated here.

## 8. Exact replay, held-outs, and what it does not establish

The dependency-free producer and tests live next to this note and under
`tests/test_multiplicative_recurrence_mixed_parents.py`. The canonical JSON
records both exact finite identities and the interpretation boundary.
Small hard caps apply before loops; no floating point, random sampling,
prime/zero/family sweep, CAS, or Lean build is used.

The controls distinguish:

1. the full Laurent spectrum on a nondegenerate circle from rational-angle
   collisions and the origin-touching false positive;
2. generic complex local factors from real/conjugate and torsion collisions;
3. symmetric-coefficient recurrence order from tensor determinant degree;
4. rank-one twists, the exceptional independent `(2,2)` pair, and forbidden
   unequal `(2,3)` / `(2,4)` / higher-multifactor profiles;
5. distinct eigenvalues from directly checked repeated/Jordan matrices;
6. exact mixed-rank differential numerators from an independent
   finite-difference reconstruction and rational Sturm root controls.

Source authentication resolves the frozen `commit:path` Git objects,
compares their compiled blob identifiers, and compares LF-normalized
content hashes. The canonical fixture hashes note, producer, tests, and
source manifest. Acceptance requires equality with full recomputation,
not just a self-consistent JSON checksum. This does not machine-prove
continuity, density, all-parameter interlacing, or global analytic claims.

## 9. Next proof obligations

1. Define a truly source-natural infinite graded object, and prove an
   analytic determinant contract rather than merely (6.2).
2. Study tensor/duality/ramification coherence for an actual prime-indexed
   family. Equation (2.2) is only the scalar twist law; it is not that task.
3. Classify cancellations on a specified arithmetic coefficient image;
   generic complex weights in (3.3) do not classify a global family.
4. Test an independently defined graph or dynamical parent without choosing
   its spectrum from desired zeros. Its extra mixed observable should be
   visible before scalar specialization.

A finite table, a fitted resolvent, or a formal graded identity alone is
not grounds to promote an analytic/global L-object. RH and GRH remain open.
