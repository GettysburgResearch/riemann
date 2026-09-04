# Lamzouri Hilbert-space zeta-zero proof: exact import and RH-facing map

```text
Status: IMPORTED / REVIEW_PENDING
Scope: global asymptotic theorem in the source mathematics; conditional theorem transfer in Lean
Exact sources or dependencies:
  paper: Youness Lamzouri, arXiv:2609.02882v1
  paper SHA256: fa33485f517b3c94d2f6e4d4366f3ab14a1e413a738db512e1862f4a0944f5f9
  code: AxiomMath/ZetaZeros@4bcaf70e544506c311d83a5a5b143a134b9fc5f7
  Riemann base: main@6dda8b5125457ed936330229f8c9eb6491728e76
What was actually run:
  remote exact-SHA source, theorem, assumption, comparator, and CI inspection
  exact hash/metadata inspection and visual rendering of all 14 paper pages
  repository-level mathematical synthesis
  no local Lean build and no local comparator replay
Smallest remaining gap:
  formal closure requires internal proofs or exact trusted adapters for Riemann-von Mangoldt
  and the BGST pair-correlation theorem; an RH proof additionally requires an
  exceptional-zero amplifier that does not lose zero-density exceptions
```

**The Riemann Hypothesis remains unproved.**

This packet imports and analyzes a short new proof that

\[
\liminf_{T\to\infty}\frac{N_0^s(T)}{N(T)}
\ge
C_0
=
\frac32-\frac1{\sqrt2}\cot\!\left(\frac1{\sqrt2}\right)
=
0.6725007\ldots
\]

and

\[
\liminf_{T\to\infty}\frac{N_d(T)}{N(T)}
\ge
\frac{1+C_0}{2}
=
0.8362503\ldots .
\]

Here `N(T)` counts nontrivial zeta zeros up to height `T` with multiplicity,
`N_0^s(T)` counts simple zeros on the critical line, and `N_d(T)` counts
distinct zeros.

## Exact import

The formal repository is retained, without flattening or rewriting, as a
gitlink at

```text
research/exploratory/imports/lamzouri-zeta-zeros-2026-09-02/ZetaZeros
```

pinned to

```text
AxiomMath/ZetaZeros@4bcaf70e544506c311d83a5a5b143a134b9fc5f7
```

The upstream commit is signed and its recorded Lean workflow succeeded. This
does not substitute for an independent local replay or semantic proof review.

The paper itself is not copied into the repository. The exact supplied arXiv
v1 PDF is locked by SHA256, size, page count, metadata, and a fourteen-page
render audit in `SOURCE_LOCK.json` and `PDF_AUDIT.md`.

## What is genuinely new

The main innovation is not another mollifier and not another finite matrix
optimization. Lamzouri isolates a general theorem about a finite
conjugation-invariant multiset of complex points.

For an admissible compactly supported function `eta`, let

\[
K(z)=\widehat{\eta^2}(z).
\]

One Hilbert-space tensor norm controls both:

1. the number of real points of multiplicity one; and
2. the number of distinct points.

This replaces the finite compression of Weil's Hermitian form and the
rank-trace/inertia machinery in the Alpoge-Furman proof by nested Hilbert
subspaces, Gram-Schmidt, and Bessel's inequality. The attached paper makes the
flag and the scalar extraction completely explicit:

```text
U = multiple-real plus nonreal-even span
V = all-real plus nonreal-even span
W = V plus nonreal-odd span

first basis range:   a^2 + 4 >= 4a
middle basis range:  a^2 + 1 >= 2a
last basis range:    a <= 0.
```

Crucially, the proof never requires each off-line kernel term to be
nonnegative.

The zeta application then uses:

```text
functional-equation reflection
  -> conjugation-invariant rescaled zero multiset
  -> abstract Hilbert inequalities
  -> differential removal of the BGST rational weight
  -> unconditional pair correlation
  -> Montgomery-Taylor extremal constant.
```

Remark 3.4 proves that the Montgomery-Taylor constant is optimal for this
scalar support-one second-moment method. Improving the percentage therefore
requires genuinely new information rather than a smoother cutoff.

## Trust boundary

There are two different meanings of "unconditional" here.

### In ordinary analytic number theory

The result is unconditional: Riemann-von Mangoldt and the BGST pair-correlation
formula are established theorems, not RH-like conjectures.

### In the current Lean repository

The abstract finite-multiset inequalities are closed proofs. The zeta
proportion theorems accept

```lean
hRvM : RiemannVonMangoldt
hPC  : PairCorrelation
```

as explicit hypotheses. Comparator therefore confirms theorem fidelity and
logical axiom cleanliness, but it does not mean that those two analytic inputs
have been proved inside the package.

## Reading order

1. `PDF_AUDIT.md` - exact paper hash, render audit, and page-by-page proof map.
2. `PAPER_DIGEST.md` - proof architecture and exact constants.
3. `FORMALIZATION_AUDIT.md` - theorem surface and formal trust boundary.
4. `CLAIM_MAP.tsv` - compact status table.
5. `RIEMANN_CONNECTION_MAP.md` - precise links to current Riemann programs.
6. `IMPROVEMENT_ROADMAP.md` - formal, analytic, and computational extensions.
7. `RH_CLOSURE_PROGRAM.md` - what must be added before this architecture could prove RH.
8. `REPRODUCE.md` - independent replay commands.
9. `REVIEW_CHECKLIST.md` - promotion criteria.

## Strongest immediate value to Riemann

The source should first be imported as an abstract operator lemma, not as an RH
claim. Its reusable content is:

```text
trace/mass
+ Hilbert-Schmidt pair energy
+ conjugation symmetry
  -> quantitative lower bounds for the simple-real and distinct sectors.
```

This is an averaged rank theorem. It interfaces naturally with Riemann's
Schur-complement, cardinal-kernel, Pick/Loewner, and theta-Darboux programs,
but it does not provide their missing complete-capture or coefficientwise
positivity theorems.

The highest-value new theorem target remains a basis-free horizontal-defect
energy extraction before the proof collapses the full Gram spectrum to a
cardinality bound.

## Nonclaims

This packet does not assert any of the following:

- that `67.25%` can be improved by retuning the same scalar test function;
- that density one of simple critical-line zeros would imply RH;
- that a positive-density set of simple line zeros is automatically a complete
  sampling frame;
- that the pair-correlation theorem has been formalized in Lean here;
- that the upstream CI run performed the independent Comparator command;
- that the importer visual audit is an independent mathematical review;
- that RH follows from this paper or from its combination with current Riemann
  packets.
