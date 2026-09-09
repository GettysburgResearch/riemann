# T-108501 — Commutative hypercomplex extensions of zeta carry only jets

```text
Status:  PROVED (elementary, self-contained below; novelty subject to the
         boundary audit in research/exploratory/2026-08-30-two-programme-pass/;
         the bicomplex special case is known in the literature and cited)
Scope:   global over the class of finite-dimensional commutative unital
         R- or C-algebras; says nothing about noncommutative, operator-valued,
         or infinite-dimensional extensions
Exact sources or dependencies: structure theory of Artinian commutative
         algebras (standard); local uniform convergence of Dirichlet series
         and their derivatives (standard); no repository dependencies
What was actually run: the finite verification script
         experiments/X-108501-commutative-collapse/verify.py (bicomplex and
         dual-number instances, exact + high-precision cross-checks)
Smallest remaining gap: none for the statement below; the noncommutative
         analogue is deliberately left open (see Section 6)
RH status: RH is unproved and this document does not address it.
```

Programme context: issue #764 (Generalized L-Objects), axis L (higher-
dimensional parents and shadow geometry) and central question 13 ("when does
a hypercomplex extension introduce genuine interaction between directions?").
This theorem closes the finite-dimensional **commutative** corner of that
axis with a collapse result: every such extension of `zeta` (or of any fixed
meromorphic function) is a finite package of jets of the original function,
componentwise over the spectrum. Genuine hypercomplex novelty therefore
requires noncommutativity or infinite dimension.

## 1. Setting

Let `A` be a finite-dimensional commutative unital algebra over `R`, and
`A_C = A ⊗_R C` its complexification (a finite-dimensional commutative
unital `C`-algebra). Examples relevant to #764:

- bicomplex numbers `BC = C ⊗_R C ≅ C × C`;
- dual numbers `C[ε]/(ε^2)`;
- multicomplex algebras `MC_n`;
- group algebras of finite abelian groups;
- any finite product of such.

For `s ∈ A_C` write `σ(s) ⊂ C` for the spectrum (the set of values of `s`
under all `C`-algebra homomorphisms `A_C → C`, equivalently eigenvalues of
multiplication by `s`).

**Definition 1 (algebra-valued zeta).** For `s ∈ A_C` with
`Re λ > 1` for every `λ ∈ σ(s)`, set

```text
zeta_A(s) := sum_{n >= 1} exp(-s log n)   in A_C,
```

where `exp` is the algebra exponential (absolutely convergent power series).
This is the definition every SERIES/FUNCTIONAL-CALCULUS hypercomplex zeta
specializes; non-power-series function theories (e.g. slice-regular) are
outside this definition and outside this theorem's scope (Section 5).

## 2. Structure of the algebra

**Lemma 1.** `A_C ≅ B_1 × ... × B_r` as `C`-algebras, where each `B_i` is a
local finite-dimensional commutative `C`-algebra with residue field `C`;
i.e. `B_i = C · 1 ⊕ N_i` with `N_i` its nilpotent maximal ideal. Moreover
an element of `B_i` is invertible iff its `C`-component (residue) is nonzero.

*Proof.* A finite-dimensional commutative unital `C`-algebra is Artinian,
hence a finite product of local Artinian `C`-algebras; the residue field is
a finite extension of `C`, hence `C` itself. In a local Artinian algebra the
maximal ideal is nilpotent and every element outside it is a unit (its
residue is a nonzero scalar, so it is `c(1 + n)` with `n` nilpotent, and
`(1+n)^{-1} = 1 - n + n^2 - ...` terminates). ∎

Write the resulting decomposition of `s ∈ A_C` as
`s = (s_1, ..., s_r)`, `s_i = λ_i + n_i` with `λ_i ∈ C` (the spectrum with
multiplicity structure) and `n_i ∈ N_i` nilpotent, `n_i^{m_i} = 0` with
`m_i <= dim B_i`.

## 3. The collapse theorem

**Theorem (T-108501).** Fix `s = (λ_i + n_i)_i ∈ A_C` with `Re λ_i > 1`
for all `i`. Then the series of Definition 1 converges absolutely and

```text
zeta_A(s) = (  sum_{j=0}^{m_i - 1}  zeta^{(j)}(λ_i) n_i^j / j!  )_{i=1..r} .
```

Consequently:

1. **(jets only)** `zeta_A` is completely determined by the scalar functions
   `zeta, zeta', ..., zeta^{(m-1)}` (`m = max_i m_i`) evaluated on the
   spectrum; the extension carries exactly the `(m_i - 1)`-jets of `zeta`
   along each spectral component and nothing else;
2. **(no new zeros)** `zeta_A(s)` is invertible in `A_C` iff
   `zeta(λ_i) != 0` for every `i`; the "zero set" of `zeta_A` is exactly the
   preimage of the zero set of `zeta` under the spectral projections — the
   zero geometry of the extension is the zero geometry of `zeta`, repeated;
3. **(everything decomposes)** the same formula with `zeta` replaced by any
   function `F` holomorphic on a neighbourhood of `{λ_i}` computes the
   functional-calculus extension `F_A`; in particular Euler products,
   completed functional equations, and meromorphic continuation of `zeta_A`
   all hold componentwise and jet-wise, and assert nothing beyond their
   scalar content.

*Proof.* Work in one local factor `B = C·1 ⊕ N`, `s = λ + n`, `n^m = 0`.
For each `n >= 1` (integer index; the nilpotent is written `n` only inside
`B`, the index is `k` below to avoid collision): for `k >= 1`,

```text
exp(-(λ + n) log k) = k^{-λ} · exp(-n log k)
                    = k^{-λ} · sum_{j=0}^{m-1} (-log k)^j n^j / j! ,
```

a FINITE sum because `n^m = 0`. Summing over `k` and exchanging the (finite)
`j`-sum with the `k`-sum:

```text
sum_k exp(-s log k) = sum_{j=0}^{m-1} ( sum_k (-log k)^j k^{-λ} ) n^j / j! .
```

The inner sums converge absolutely for `Re λ > 1` (standard: derivatives of
a Dirichlet series), and `sum_k (-log k)^j k^{-λ} = zeta^{(j)}(λ)` — the
`j`-th derivative of `zeta`, by termwise differentiation of `sum k^{-λ}`,
justified by local uniform convergence on `Re λ > 1`. Absolute convergence
of the `A_C`-valued series follows from absolute convergence of each of the
finitely many coordinate series (fix any algebra norm; all norms on a
finite-dimensional space are equivalent). This proves the displayed formula
on one local factor; Lemma 1 gives the product decomposition, and homomorphic
projection onto each factor commutes with the series termwise.

(1) is the formula. (2): by Lemma 1, an element of `B_i` is invertible iff
its residue is nonzero; the residue of the `i`-th component of `zeta_A(s)`
is the `j=0` term, `zeta(λ_i)`. (3): the identical computation runs with
any `F` whose Taylor expansion at each `λ_i` exists — i.e. `F` holomorphic
near the spectrum — using the functional-calculus definition
`F(λ + n) := sum_{j<m} F^{(j)}(λ) n^j / j!` (which is the unique definition
compatible with polynomials and limits); for `zeta` on `Re λ > 1` the series
of Definition 1 agrees with it by the computation above, and each side of
the classical global identities (Euler product on `Re λ > 1`, the completed
functional equation after the standard continuation of each jet coordinate)
is then an identity of finite jet packages of scalar identities. (In what
sense the continued object is unique and analytic: on each local factor
`B_i` the residue `lambda_i` is a LINEAR functional of `s`, so the jet
package is an `A_C`-valued analytic function of `s` wherever every
`lambda_i(s)` avoids the scalar poles, agrees with the series on the
common domain, and is the unique componentwise continuation by the scalar
identity theorem — sentence added after adversarial review.) ∎

## 3b. Corollary: the associative case collapses too

**Corollary 1 (single-variable associative collapse).** Let `A` be ANY
finite-dimensional associative unital `R`-algebra (quaternions `H`, matrix
algebras, Clifford algebras, ...) and let `s ∈ A_C` satisfy `Re λ > 1` on
the spectrum of `s`. Then the series of Definition 1 lies in the COMMUTATIVE
subalgebra `C[s] ⊂ A_C`, and the Theorem applies inside `C[s]`: the value is
the jet package of `zeta` along the spectrum of `s`, and `zeta_A(s)` is
invertible in `A_C` iff `zeta` is nonzero on the spectrum of `s`.

*Proof.* Every term `exp(-s log k)` is a limit of polynomials in `s`, and
`C[s]` is a finite-dimensional (hence closed) commutative subalgebra
containing all partial sums, so the sum lies in `C[s]`; apply the Theorem to
the algebra `C[s]`. Invertibility in a unital subalgebra of a
finite-dimensional algebra agrees with invertibility in the ambient algebra:
if `x ∈ B ⊆ A` is invertible in `A`, left multiplication by `x` is injective
on `A`, hence on `B`, hence surjective on `B` by finite dimension, so
`x^{-1} ∈ B`. ∎

In particular the naive **quaternionic zeta** — `sum_k exp(-s log k)` for a
single quaternionic argument — collapses slice-wise, in the following
precise sense (corrected after adversarial review: the first deposit
wrongly said `C[s] ≅ C`): for non-real `s ∈ H`, the REAL subalgebra
`R[s] ⊂ H` is isomorphic to `C` (the slice through `s`), and the series
lies in `R[s]`; inside `A_C = H ⊗ C ≅ M_2(C)` the subalgebra `C[s]` is
2-dimensional, `≅ C x C`, with spectrum the conjugate pair
`{lambda, conj(lambda)}` (the roots of the minimal polynomial of `s`), and
the value is the jet package `(zeta(lambda), zeta(conj lambda))` — i.e.
exactly the classical `zeta` on the slice, seen through its two conjugate
embeddings. Here the "spectrum of s" means the roots of its minimal
polynomial (equivalently the eigenvalues of left multiplication), which is
the correct reading of Corollary 1's hypothesis in a noncommutative
ambient algebra (there are no C-algebra homomorphisms `M_2(C) -> C`).
This proves, for all series/functional-calculus definitions, the collapse
half of the #764 theorem target "prove that a broad class of naive
quaternionic or multicomplex extensions collapses slice-wise to ordinary
complex zeta, or construct an intrinsically coupled counterexample".

## 4. What this closes

- The **bicomplex** zeta (`BC ≅ C × C`, both `m_i = 1`): `zeta_BC` is the
  pair `(zeta(λ_1), zeta(λ_2))` of independent copies — the idempotent
  decomposition PUBLISHED in the bicomplex literature: Rochon (2004) treats
  the bicomplex Riemann zeta and its RH statement, which is equivalent to
  classical RH precisely BECAUSE of this collapse; the underlying algebra
  mechanism goes back to Scheffers-era hypercomplex function theory (see
  also Plaksa-Shpakivskyi). None of this special case is claimed as new
  here; this theorem is its uniform generalization with the jet bookkeeping.
- **Multicomplex / dual-number / group-algebra** zetas: jets of `zeta`,
  by the theorem; a dual-number zeta is exactly `(zeta(λ), zeta'(λ))` — the
  first jet — so e.g. "simple zeros of zeta" is the precise content of
  "invertibility of the dual-number zeta at a zero's residue perturbation",
  and nothing deeper.
- Any proposal of the form "extend `s` to a finite-dimensional commutative
  hypercomplex domain and study the richer zero geometry": by (2) there is
  no richer zero geometry. A genuinely new object must break one of the
  hypotheses: commutativity, finite dimension, or the functional-calculus
  compatibility of its definition.

This is deposited as a **reusable firewall** for #764 axis L (and the
hypercomplex collapse test, experiment 18 of the issue): a slice-wise or
jet-wise repetition of `zeta` is a *visualization*, not a new arithmetic
object, and the theorem makes "slice-wise" precise and exhaustive in the
commutative finite-dimensional world.

## 5. Sharpness remarks

- Commutativity of the ambient algebra is not needed for a SINGLE algebra
  variable (Corollary 1): one element always generates a commutative
  subalgebra. What Corollary 1 does NOT cover are definitions that are not
  the one-variable series/functional calculus — e.g. slice-regular
  quaternionic function theory (Gentili–Struppa; CITATION-NEEDED precision)
  or genuinely several-noncommuting-variable objects; those are recorded as
  the open boundary, not claimed.
- Finite dimension is used for: nilpotency of the maximal ideal, finiteness
  of the jet, and norm equivalence. Infinite-dimensional commutative
  extensions (e.g. function-algebra-valued `s`) are untouched.
- The theorem applies verbatim with `zeta` replaced by any Dirichlet series
  or completed `L`-function on the corresponding half-plane, and after
  continuation, to any meromorphic `F` away from its poles.

## 6. Open counterpart (deliberately not claimed)

By Corollary 1, escaping the collapse within finite dimensions requires the
DEFINITION to involve more than one-variable functional calculus: genuinely
several-variable noncommutative arguments (`zeta` of a noncommuting tuple,
e.g. via a chosen ordering or a free functional calculus), slice-regular or
other non-power-series function theories, or operator-valued/infinite-
dimensional constructions (#764 axis J). Constructing such an extension
whose zero geometry provably differs from a repetition of the scalar one —
or proving a collapse theorem for a class of free/ordered functional calculi
— is the open counterpart. Stated as a target, not a claim.
