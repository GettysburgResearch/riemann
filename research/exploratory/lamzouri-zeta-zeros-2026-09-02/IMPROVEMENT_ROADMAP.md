# Improvement roadmap

**Status:** proposed program. RH remains unproved.

The work should be improved on three independent axes:

```text
formal closure
numerical/proportion strengthening
RH-facing exceptional-zero detection.
```

They must not be conflated.

## Priority 0 - reproduce before extending

At the exact source SHA:

1. fetch the pinned Lean toolchain and Mathlib cache;
2. build every production module;
3. run Comparator and Nanoda;
4. print axioms of all six production counterparts;
5. scan production modules for `sorry`, `admit`, and undeclared axioms;
6. record tool versions, logs, and source-tree hashes;
7. compare the challenge types with the paper's Proposition 2.1 and Theorem 1.1.

This is the minimum evidence required before theorem extraction.

## Priority 1 - close the formal analytic inputs

### 1A. Riemann-von Mangoldt adapter

Do not re-formalize more than is needed. First search the Riemann formal spine,
Mathlib, and the pinned zeta dependencies for an existing zero-count theorem.
Prove an exact adapter to

```lean
ZetaZeros.RiemannVonMangoldt
```

including the package's zero range, multiplicity convention, and leading
normalization.

### 1B. BGST pair-correlation theorem

This is the major formal project. Decompose it into:

```text
admissible test class
explicit formula
Dirichlet-polynomial or prime-side second moment
off-line zero treatment
rational weight
uniform error
normalization adapter.
```

The source target should be the exact lemma used by Lamzouri, not an informal
`O`-notation paraphrase.

### 1C. Closed final corollary

Only after 1A and 1B prove:

```lean
theorem simple_proportion_lower_unconditional ...
theorem distinct_proportion_lower_unconditional ...
```

with no analytic hypothesis parameters and a clean axiom report.

## Priority 2 - improve auditability

The current proof is validly modularized at the top level, but the long
`AlphaExpansion` file is difficult to review. Refactor the mathematical spine
into theorem-sized modules:

```text
Gram identity
conjugation-real structure
flag construction
adapted orthonormal basis
coefficient formulas by range
Bessel bound
simple-real combinatorial extraction
distinct-point combinatorial extraction.
```

Each module should state the corresponding paper equation or lemma and expose
a short primary theorem.

Add:

- source-line and equation tags;
- a generated declaration map;
- exact `#print axioms` receipts;
- a proof-term size report;
- a linter verifying the challenge module is not imported by production;
- a CI job that actually invokes Comparator and Nanoda.

## Priority 3 - make the result effective

The source gives eventual proportions. An effective version should expose:

```text
T0(epsilon)
pair-correlation error constant
Riemann-von Mangoldt error
cutoff approximation error
Montgomery-Taylor approximation error
denominator positivity threshold.
```

Even enormous explicit thresholds are valuable because they:

- turn asymptotic reasoning into a finite certificate;
- permit direct comparison with verified zero tables;
- identify the dominant analytic loss;
- support hybrid finite-verification plus asymptotic arguments.

## Priority 4 - parameterize the support and regularity

The current application is tuned to the support-one BGST theorem. Develop a
theorem parameterized by a support radius `sigma`:

```text
PairCorrelation(sigma, error)
+ HilbertKernel(sigma)
  -> C_simple(sigma), C_distinct(sigma).
```

This creates a clean interface for any future improvement in unconditional
pair correlation.

Record which constants improve with `sigma`, and which proof steps require:

- compact support;
- smoothness;
- anchored Lipschitz continuity;
- evenness;
- nonnegativity of the primal profile;
- exact normalization.

## Priority 5 - retain the full Gram spectrum

The published proof reduces the Gram operator to:

```text
trace
Hilbert-Schmidt norm.
```

That is enough for effective rank but discards most operator information.

Instead compute or bound:

- spectral distribution;
- singular values of the good-sector evaluation map;
- principal angles between real/simple and defect subspaces;
- stable rank in local windows;
- lower quantiles of eigenvalues;
- Schur complement of the defect block.

This is the most direct route from a proportion theorem toward Riemann's
operator moat.

## Priority 6 - multi-kernel and vector-valued inequalities

A single scalar kernel has an extremal barrier. Replace it by a vector of
admissible kernels `K_1,...,K_r` and form a block Gram operator.

Optimize a semidefinite objective subject to all pair-correlation constraints.
Potential gains can come from:

- different support allocations;
- derivatives of a common kernel;
- even and conjugation-odd channels;
- simultaneous horizontal and multiplicity penalties;
- cross-kernel correlations.

A finite SDP may nominate a theorem, but the final certificate must be exact:
rational coefficients, interval-enclosed analytic constants, and a
machine-checked PSD factorization.

## Priority 7 - higher tensor powers and k-point correlation

Pair correlation controls a second Schatten moment. To force the good sector
closer to full rank, develop abstract `p`-moment analogues:

```text
tr(G), tr(G^2), ..., tr(G^p)
  -> bounds on bad rank, large multiplicities, and small eigenvalues.
```

Analytically this requires higher zero correlations or higher prime-side
moments. Formally, the Hilbert construction should be generalized first on
synthetic finite multisets, before importing any unproved zeta input.

A moment ladder may improve proportions toward one. It still does not
automatically remove a finite exceptional set.

## Priority 8 - extract horizontal displacement energy

The current scalar conclusion counts nonreal points but throws away their
distance from the real axis. The uncollapsed Hilbert coefficients should be
examined for a bound of the form

\[
\sum_{\rho}
m_\rho\,\Phi\!\left((\beta-\tfrac12)\log T\right)
\le \text{pair-energy budget},
\]

where `Phi` is positive and increasing.

Such a theorem could produce:

- quantitative horizontal zero density;
- thin-box concentration;
- penalties for zeros far from the line;
- better input for the Riemann Pick/Schur programs.

This is a more RH-relevant use of the proof than merely optimizing the final
percentage.

## Priority 9 - local-window theorem

Replace the global range `(0,T]` by windows such as

```text
(T, T+H]
```

with uniform control in the center and window length.

A local theorem could support:

- lower local simple-zero density;
- separation estimates;
- sampling-frame bounds;
- effective exclusion above a verified height.

The analytic difficulty is much greater: the prime-side transform and error
must remain controlled as the window shortens.

## Priority 10 - L-function families

The abstract multiset theorem is family-agnostic. Build an interface:

```text
functional equation / conjugation action
zero-count asymptotic
weighted pair correlation
kernel metric adapter
  -> simple symmetry-line and distinct-zero proportions.
```

Candidate families include primitive Dirichlet L-functions and automorphic
families, but each family needs exact conductor scaling and root-number
bookkeeping. Family averages must not be silently converted into an
individual principal-zeta conclusion.

## Computational program

### Experiment E1 - synthetic sharpness atlas

Enumerate finite conjugation-invariant multisets with controlled multiplicity
and compare the exact Hilbert bound to the true simple-real and distinct
counts. Search for equality and near-equality mechanisms.

### Experiment E2 - spectrum, not just trace

For known zeta zeros, build finite Gram matrices for the Lamzouri kernels and
record eigenvalue distributions, defect-sector principal angles, and
conditioning across height windows.

### Experiment E3 - multi-kernel SDP

Optimize block kernels under discretized pair-correlation constraints. Emit
exact rational candidate certificates.

### Experiment E4 - planted off-line quartet

Insert a synthetic functional-equation quartet into a real zero sample and
measure which kernel families detect it after `N(T)` normalization. This
quantifies the density-zero firewall.

### Experiment E5 - frame diagnostics

Using certified simple zeros, test local Paley-Wiener/de Branges sampling
constants and the dependence on `Xi'(gamma)`.

### Experiment E6 - matrix/Hilbert comparison

Construct the finite Weil compression and Lamzouri Gram operator on the same
sample and verify the exact congruence or limiting relation.

None of these experiments proves an asymptotic theorem. They should nominate
specific lemmas and counterexamples.

## Ranked theorem targets

1. exact matrix-Hilbert equivalence;
2. local flagged-Gram inequality retaining singular-value data;
3. support-parameterized zeta transfer theorem;
4. quantitative horizontal-energy inequality;
5. multi-kernel abstract theorem;
6. higher-moment abstract theorem;
7. effective local-window pair-correlation adapter;
8. complete formal closure of Riemann-von Mangoldt and BGST.
