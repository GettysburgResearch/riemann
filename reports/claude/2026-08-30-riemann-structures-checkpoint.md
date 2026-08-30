# Programme #763 checkpoint — first pass (2026-08-30)

```text
Status:  first Gate-0 pass, claims band 1080xx (+ shared substrate)
Scope:   see M-108000; RH and GRH are unproved and unaddressed
Sibling: #764 checkpoint report (same date); bridge report ties the two
```

## The instrument (proved + battery-verified)

**T-108002 — the refusal-capable structure detector** (`core/reconstruct.py`,
backbone L-108001, replay `X-108002` with 14 exact checks after the
adversarial wave's fixes — see the claim's failure ledger, which records
one FATAL and four majors found and repaired, with counterexample rows
added): from exact local coefficient or trace data it reconstructs the
unique candidate finite-rank local object or REFUSES at the first failing
axiom of

```text
A1 FINITE_RANK -> A2 EFFECTIVITY -> A3 INTEGRALITY -> A4 PURITY -> A5 HELD_OUT (+ A6 TENSOR)
```

with an exact witness per refusal. Battery: genuine elliptic-type data
passes A1-A5; structureless data refuses at A1; non-integral at A3;
weight-violating at A4; corrupted tails are caught; tensor compatibility
holds on true products and fails with indexed witnesses on perturbed ones.

## The headline exact findings

1. **The two Mobius ontologies are separated by the weight of their
   virtual parts.** Number-field Mobius local data `mu(p^k)`: finite rank
   HOLDS, refusal at A2 EFFECTIVITY with exact witness numerator `(1-T)` —
   the virtual negative of the trivial WEIGHT-0 object. Function-field
   affine Mobius (exhaustive exact computation over monic polynomials,
   q = 2, 3): virtual with witness `(1-qT)` — pure of WEIGHT 2
   (Tate-twisted). Phrased under the Brauer-Nesbitt caution mandated by
   the boundary audit (trace data cannot certify non-semisimplicity; the
   convention-invariant statement is exactly "A1 holds, A2 fails, with
   these witnesses"). The pass's original "nilpotent/purity" phrasing was
   WRONG and is recorded as corrected in the claim's failure ledger.
2. **Angle-stratified purity of a #764 object** (O-108506, bridge): the
   detector's purity axiom, applied to the m=3 defect of T-108500, is
   decided by `sign(a_p^2 - p)` — a mechanism cell whose truth value is a
   density, discovered by pointing the #763 instrument at a #764 object.

## The ablation/independence table

As built: T-108000 aggregates matrix/MATRIX.md (12 worlds, zero
validation problems) into the three-cell-type table the audit mandated —
WITNESSED separations with exact corpus certificates ({Euler, FE, trace}
not forcing the line via the Sturm-certified non-Ramanujan graphs, with
the refinement that self-adjointness gives spectrum realness but not the
purity gap; {Euler} not forcing FE via the fully proved 2-deleted zeta;
{FE} without Euler product via the exact Q(zeta_20) Davenport-Heilbronn
derivation; archimedean non-freeness via the proved non-entire
wrong-gamma pole transport), PROVABLY-EMPTY cells carrying Hamburger,
Kaczorowski-Perelli, and Weil-converse citations, and OPEN cells as the
frontier. Every individual separation is classical and cited (Terras's
zeta dictionary as the direct ancestor); the machine-validated table with
witnesses attached is the pass's artifact. The cross-tabulation also
yields the corpus headline below.

## The central open cell (stated as the programme's sharpest question)

Does there exist a NUMBER-FIELD-ontology world with the full package
{Euler product, FE, explicit formula, tensor operations} and NO
positivity/purity mechanism, yet a critical-line theorem? Every world in
the corpus with a critical-line THEOREM has an identified
positivity/purity mechanism (Frobenius weights; adjacency
self-adjointness), and every world lacking one either fails the line
(non-Ramanujan graphs, class-number > 1 Epstein) or has it OPEN (zeta
itself). The corpus makes this co-occurrence exact and witnessed; it
proves nothing about zeta, and is deposited as the programme's organizing
observation, not as evidence.

## Ranked continuation queue (#763)

1. Point the detector at more repository-native observables: the
   duplicate-67 labelled native source at composite labels; codex-atlas
   genus-2 trace tables across q; beta-lane exact sequences where
   rational-valued. [Extends O-108004 — see as-built status at wrap.]
2. Tensor-compatibility as rigidity: formulate the exact conjecture
   "bounded-rank local systems with tensor-compatible trace data across
   two independent constructions arise from a representation-ring object"
   (Tannakian flavour, cited as such) and hunt exact countermodels with
   the counterfeit generator.
3. The graph world as a quantitative mechanism laboratory: exact
   spectral-gap -> zero-free-annulus-width dictionary (graph analogue of
   zero-free regions), then test which quantitative features transfer to
   the function-field row — a transfer-theorem target with fully exact
   both sides.
4. The archimedean lane (deferred by design this pass): boundary-map
   anchors are deposited in BOUNDARY_AUDIT_CONSOLIDATED.md; first target:
   compatibility census of candidate gamma-factor mechanisms against the
   wrong-gamma obstruction lemma's method.
5. Measure-valued mechanism cells (from O-108506) — joint schema revision
   with #764.
```

## Continuation pass (2026-08-31)

1. **O-108004 — the held-out first, delivered**: the detector on
   repository-native observables. The T-99930 native duplicate-67 source's
   Euler factorization was re-verified exactly to n = 500, and the
   detector READS THE LABEL BOOKKEEPING: witness numerator
   `(1-T)^{#labels(p)}` — multiplicity 2 at the duplicated prime 67,
   1 elsewhere; uniformly virtual, uniformly weight 0. The codex genus-2
   family trace laws (pinned to their branch blobs, PROVED status recorded
   in their own lane) evaluated along prime-power towers are certified as
   TATE-MONOMIAL VIRTUAL objects: multiplicity vectors exactly the law
   coefficients, no Frobenius angles surviving family aggregation — the
   sharpest available contrast between individual-object data (carries
   angles) and family-aggregated data (provably does not, at these laws).
   Corpus now 13/13, matrix reassembled, zero validation problems.
2. **L-108005 — the quantitative mechanism dictionary** (+`X-108005`,
   exact): the standard tree-spectrum parametrization assembled into a
   two-directional dictionary `Re s = 1/2 ∓ arccosh(|lambda|/2 sqrt q)/log q`
   with the Vieta pairing as the functional-equation shadow; certified
   one-for-one on the corpus (prism: one untempered eigenvalue-square,
   one off-circle pole by exact resultant census; Petersen: zero and
   zero); and the transfer statement: graphs and curves share ONE
   algebraic dictionary, differing only in the SUPPLIER of the bound
   (spectral gap vs Weil purity) — reducing the next-pass mechanism
   theorem to naming what supplies the bound at number fields.
