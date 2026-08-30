# Programme #763 checkpoint — first pass (2026-08-30)

```text
Status:  first Gate-0 pass, claims band 1080xx (+ shared substrate)
Scope:   see M-108000; RH and GRH are unproved and unaddressed
Sibling: #764 checkpoint report (same date); bridge report ties the two
```

## The instrument (proved + battery-verified)

**T-108002 — the refusal-capable structure detector** (`core/reconstruct.py`,
backbone L-108001, replay `X-108002` with 10 exact checks): from exact
local coefficient or trace data it reconstructs the unique candidate
finite-rank local object or REFUSES at the first failing axiom of

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

[AS-BUILT SLOT — T-108000 aggregates matrix/MATRIX.md after assembly.
Structure fixed in advance per the audit: three cell types —
WITNESSED (exact corpus witness: non-Ramanujan prism with Sturm
certificates for {Euler, FE, trace} not forcing the line; the 2-deleted
zeta for {Euler} not forcing FE, fully proved via the exact zero
s0 = 2 pi i/log 2 plus the classical nonvanishing zeta(1+it) != 0;
Davenport-Heilbronn for {FE} without Euler product, with the density-zero
caveat; the wrong-gamma obstruction for archimedean non-freeness),
PROVABLY-EMPTY (dependence theorems: Hamburger uniqueness at degree 1;
Kaczorowski-Perelli degree classification; Weil converse at GL(2) with
twists — imported, cited), and OPEN (the discovery frontier). Every
individual separation is folklore or classical and cited as such (Terras's
zeta dictionary named as the direct ancestor); the table artifact — one
schema, witnesses attached, empties proved — is the pass's contribution.]

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
