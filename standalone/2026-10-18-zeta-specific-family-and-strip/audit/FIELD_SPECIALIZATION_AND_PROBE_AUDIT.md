# Field specialization and finite-probe audit

Status: independent source/scope audit; the elementary probe lemmas below have
complete proofs. No new zeta zero-free bound and no RH proof are asserted.

Scope: ordinary zeta versus fixed quadratic Dedekind zeta, finite changes of
profiles, and fixed finite families of finite-order character probes. This is
not a review approval of the complete proposed theta contour arguments.

Reading date: 2026-10-18. The main branch was observed at
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`.

## 1. Assessment of the current work

Dropping the all-field conclusion is a sensible research choice, but it only
changes an exponent if the proof stops paying a scale-dependent cost. A fixed
class group or discriminant constant is not such a cost. More useful freedoms
are restricting the target character, preserving the correlation in a ratio,
or changing the family so the target is present in every member.

There are three different kinds of current progress:

* [#977, COMPOSITION.md](https://github.com/GettysburgResearch/riemann/blob/1b473843c920b004994a3ffb7e9b6b7f9ce54c05/standalone/2026-10-18-zero-free-reflected-numerator/COMPOSITION.md)
  proposes the all-field boundary `271/300`. Its new step reuses the same
  selected zero-free rectangle on both sides of a reflected L-ratio. It still
  takes absolute values of the root numbers. The enlarged Euler domain,
  selected-family density input, and full two-height contour composition
  remain substantive review obligations. This audit read its proof and
  reflection lemma; it did not reprove every imported metaplectic statement.
* [#986, PROOF.md](https://github.com/GettysburgResearch/riemann/blob/5b9a4ae1426938d02d469a6082793efedc4f8e21/standalone/2026-10-18-mixed-mollifier-residual/PROOF.md)
  proposes `sum |L_a M_A-1|^2 << U^(11/15+epsilon)` on the fixed line
  `Re s=3/4`, with a longer mollifier. The proof retains the mixed character
  structure and treats principal rows separately. This is a bound for a SUM
  over the family, not a zeta strip or a reciprocal bound for a prescribed
  member. At any zero of a particular member its summand is exactly one,
  which is compatible with the positive exponent `11/15`.
* [#996, PRIMITIVE_CORE_EQUIVALENCE.md](https://github.com/GettysburgResearch/riemann/blob/56ec8747ccf75d7fc19c2395a6523a664938b9f6/standalone/2026-10-18-quadratic-angular-all-order/PRIMITIVE_CORE_EQUIVALENCE.md)
  removes the angular variable from one principal target. For the Eisenstein
  field the source is `mu(n) 2^omega(n)` supported on squarefree integers
  with every prime `p=1 mod 3`. Its two invertible Euler corrections preserve
  the square-root cancellation problem exactly. The criterion concerns RH
  for `zeta_K=zeta L(chi_-3)`, hence both ordinary RH and the fixed quadratic
  Dirichlet factor. It is stronger than ordinary RH alone. The correction
  does not supply new cancellation.

The [main README and STATUS](https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/STATUS.md)
retain an older reviewed integration baseline. The later PR heads above are
proposals, not newly integrated or independently accepted simply because
they have been pushed or their finite checkers pass.

### The ordinary-zeta benchmark needs the current version

Baiying Liu's [arXiv:2610.12234v2](https://arxiv.org/html/2610.12234v2), main
theorem and Part IV, reports

\[
B_{\rm new}=\frac{18x+7}{18x+9}
=0.874957019420098946\ldots,
\qquad 1188x^3-2160x^2+171x+190=0,
\quad 0.38858<x<0.38859.
\]

The quoted `(1507-2 sqrt(921))/1653=0.874957069799...` is the earlier
algebraic improvement, retained as an intermediate result in v2. Both are
below `271/300`. Liu's optimality statement is confined to the explicitly
specified comparison system, not all possible arguments. These are imported
reported results; this audit checks their source statements, not their whole
analytic proof or Lean build.

## 2. What fixed profile changes can and cannot accomplish

The prior [#962, PRINCIPAL_TWO_VARIABLE_FACTOR.md, Section 5](https://github.com/GettysburgResearch/riemann/blob/b2032c663736ecd1e3872559d160ce069664ea06/standalone/2026-10-17-critical-scattering-reset/PRINCIPAL_TWO_VARIABLE_FACTOR.md)
already identifies a restriction on the proposed profile experiment: at the
principal double residue, admissible smoothing profiles only change the
scalar `M(1/6) W_hat_1(1)`, while the arithmetic factor is unchanged.

**Lemma 1 (common principal factor).** Suppose a finite collection of legal
probes has principal contributions

\[
I_j^{\rm prin}(s)=c_j T(s),\qquad 1\le j\le m,
\]

where the scalars `c_j` are independent of `s`, and `T` is the common
meromorphic arithmetic expression. For every fixed set of complex weights,

\[
\sum_j w_jI_j^{\rm prin}(s)
=\Big(\sum_jw_jc_j\Big)T(s).
\]

Consequently a combination normalized to retain `T` retains every part of
this common factor; a combination annihilating it also removes the detector.

**Proof.** Linearity, initially off the poles and then by meromorphic
continuation. This is not an asymptotic argument. QED.

This lemma does NOT forbid cancellation of separately identified
nonprincipal contributions whose profile dependence differs. It says that
varying only these smoothing profiles cannot alter the principal arithmetic
factor. A genuine probe experiment must write out that different dependence,
rather than assume it is present.

The [#975 transverse calculation](https://github.com/GettysburgResearch/riemann/blob/edbc27b61208ccc7ee1fa99fa3f4e861f5a03452/standalone/2026-10-18-resonant-transverse-jet/PROOF.md)
is a useful example of changing something substantive: on the functional
equation hyperplane the residue loses all target poles, but the first
transverse finite part retains them through a normalized `-Z'/Z`. The
physical transverse projection and its signed estimate remain open. Simply
bounding the zero-blind residue cannot substitute for them.

## 3. Fixed finite character probes leave a large invisible class

This gives a quantitative acceptance test for finite root-of-unity masks.
It is an elementary consequence of character orthogonality and the fixed
ray-class prime ideal theorem, not a new large-sieve theorem.

Fix a number field `F`, a finite set `S`, and distinct finite-order Hecke
characters `phi_1,...,phi_m`, all unramified outside a fixed modulus. For any
complex weights, possibly depending on `U`, put

\[
P_U(\mathfrak a)=\sum_{j=1}^m w_j(U)\phi_j(\mathfrak a),
\qquad P_U((1))=\sum_j w_j(U)=1.
\]

Every character is extended by zero on its nonunits. All prime sums below
exclude the fixed conductors and `S`.

**Theorem 2 (fixed-probe energy floor).** As `U` tends to infinity,

\[
\sum_{N\mathfrak p\le U}|P_U(\mathfrak p)|^2
\ge (1-o(1))\operatorname{Li}(U)\sum_j|w_j(U)|^2
\ge \frac{1-o(1)}m\operatorname{Li}(U).
\tag{1}
\]

The `o(1)` is uniform in the weights, because the finite probe characters
are fixed. In particular, a normalized fixed finite character mask cannot
have `O(U^(1-delta))` square mass on all n-th-power-free ideal rows, for any
fixed positive `delta`; prime ideals already violate that estimate.

**Proof.** All the characters factor through one fixed finite ray quotient.
The prime ideal theorem in its finitely many classes gives

\[
\frac1{\operatorname{Li}(U)}
\sum_{N\mathfrak p\le U}
\phi_j(\mathfrak p)\overline{\phi_k(\mathfrak p)}
\longrightarrow \delta_{jk}.
\]

The `m` by `m` Gram matrix therefore converges in operator norm to the
identity. Its smallest eigenvalue is `1-o(1)`, proving the first inequality
for every vector of weights simultaneously. Cauchy--Schwarz and
`sum w_j=1` give `sum |w_j|^2>=1/m`. Every prime ideal is n-th-power-free for
every integer `n>=2`, so enlarging the positive sum to those rows preserves
the lower bound. QED.

If the listed characters contain repetitions, consolidate their weights
first; `m` denotes the number of distinct characters.

There is also a pointwise version. On the prime ideals splitting completely
in the common finite abelian extension cut out by the characters, every
`phi_j(p)=1`, hence `P_U(p)=1` for every normalized choice of weights. Those
primes have positive density within the fixed prime ideal distribution.
The [explicit Eisenstein source in #983](https://github.com/GettysburgResearch/riemann/blob/e9ce2d171fba2bcca4cb4d8c6e78dc97f69613e9/standalone/2026-10-18-native-moment-scope/EISENSTEIN_FAMILY.md)
shows why these can be genuinely nonprincipal Kummer rows: a new exterior
prime in an n-free row has nontrivial ramification. Being invisible to a
fixed list of probes does not make the full row character principal.

For reference, the fixed-ray prime asymptotic is also explicitly used in
Liu v2, Section 8.2, Lemma 8.2; its scope is fixed modulus. Equation (1) makes
no uniform claim when the modulus or number of probes grows with `U`.

### Precise limitation of this obstruction

Equation (1) concerns the mask itself. It does not lower-bound a signed
L-ratio sum or a mollified residual multiplied by that mask. Such an
arithmetic summand may have additional cancellation. Nor does the theorem
exclude a successful finite-probe combination that cancels a small set of
explicit nuisance coefficients while leaving the other rows under analytic
control. It prevents claiming that fixed local phases alone isolate the
principal row or make every nonprincipal row sparse.

## 4. The exact rank and conditioning test for useful probes

Let `c` be the target column in `C^m`, and let `B` be an `m` by `r` matrix
whose columns are the explicitly derived nuisance signatures. Use the
Hermitian normalization `w* c=1`, `w* B=0`; conjugating the coefficient
notation recovers the transpose convention in the suggested experiment.
Let `Pi` be orthogonal projection onto `ker B*`.

**Lemma 3 (existence and exact coefficient cost).** Such a combination
exists exactly when `Pi c` is nonzero. Its minimum Euclidean coefficient
norm is

\[
\min\|w\|_2=\frac1{\|\Pi c\|_2},
\qquad
w_{\min}=\frac{\Pi c}{\|\Pi c\|_2^2}.
\tag{2}
\]

**Proof.** The nuisance condition says `w` lies in `ker B*`, so
`w* c=w* Pi c`. If `Pi c=0`, the target condition is impossible. Otherwise
Cauchy--Schwarz gives `1<=||w|| ||Pi c||`, with equality for the displayed
vector. QED.

If the complete error vector satisfies `||E||_2<=R`, the best-norm
combination has error at most `R/||Pi c||_2`. Thus full rank without a
quantitative separation is insufficient: a near-dependence can consume the
entire proposed exponent gain. An exact null vector at one numerical
sample is insufficient as well.

When the signatures depend on a complex Mellin variable, (2) is a
pointwise norm calculation. The Hermitian formula itself is generally not
holomorphic in that variable. A Mellin continuation argument needs fixed
weights or a separately justified holomorphic choice with controlled norm
and no newly introduced poles on the claimed domain.

## 5. How this changes the research priorities

The best specialization is one that changes the unresolved quantifier or
estimate. A common-zeta-factor family directly addresses the fact that a
single exceptional family member can survive every positive-power average.
A controlled strip of zeros for convergent xi approximants changes the
finite-model construction problem from exact reality of all zeros. Both
have a sharper acceptance test than a new numerical optimization of the
same all-field comparison.

A principal Eisenstein probe programme remains worthwhile if it produces
an explicit nuisance matrix with nonzero, quantitatively separated target
projection and a complete analytic error bound. Fixed phase multiplication
alone cannot improve a worst-case matrix norm: multiplying rows or columns
by unit-modulus phases is a unitary operation. A signed combination can be
different, but must pass Lemmas 1--3 on its actual source.

Finally, the small field is not itself a reason to expect orthogonality.
[de Faveri--Dunn--Hoffstein, arXiv:2607.07911v1](https://arxiv.org/html/2607.07911v1),
Theorems 1.1--1.2, prove cubic and quartic large-sieve lower bounds over the
corresponding simplest cyclotomic fields. These are worst-case operator
obstructions, not statements that the particular Möbius/principal target is
a worst-case vector. [de Faveri, arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1),
Theorem 1.1, supplies the four-monomial upper bound with both indices
n-th-power-free. The proof cannot freely replace that support by squarefree
indices or replace a character times its conjugate by the same character
of a product.

## Review boundary and smallest remaining gap

No finite check is being offered as certification of an infinite estimate.
The new elementary statements here are the scalar rigidity identity, the
fixed finite-character energy floor, and the exact projection cost. Their
external analytic input is only the classical fixed-modulus prime ideal
theorem. No published-theorem priority claim is made.

For a successful new Eisenstein cancellation argument, the smallest
remaining task is to exhibit legal probes with a complete source identity,
prove a nonvanishing quantitative target projection, and bound the full
signed remainder on that same family and contour. None of the reviewed
positive-moment exponents or these elementary obstructions supplies that
estimate.
