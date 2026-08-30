# Generalized L-objects: recurrence rigidity and a contrasting non-scalar parent

Status: proposed exact local/finite research for
[programme #764](https://github.com/gfreund123/riemann/issues/764), with a
synthetic structural comparison for
[#763](https://github.com/gfreund123/riemann/issues/763).
This records the requested work scope, not a claim that five wall-clock
hours have elapsed. RH and GRH remain unproved.

## What this branch adds

Two independent mathematical lanes test different meanings of a generalized
L-object. Neither lane is a new arithmetic L-function.

| Lane | New repository result | Exact stopping boundary |
|---|---|---|
| [Multiplicative recurrence preservers](MULTIPLICATIVE_RECURRENCE_AND_MIXED_PARENTS.md) | One nondegenerate shifted-circle recurrence test classifies every continuous multiplicative map as `z^m bar(z)^n`; the bounded-degree moduli and continuous-deformation obstruction are exact | Continuous scalar maps and ordinary recurrences; no prime-indexed or ramified family |
| [Complete circle-probe geometry](CIRCLE_PROBE_GEOMETRY.md) | An origin-touching circle leaves infinitely many false positives at each fixed positive degree; every positive non-touching center eliminates them. Connected pointwise-continuous families passing the touching probe are constant | Prose classification for irrational rotations; no natural-boundary theorem or general local-constancy claim in the degenerate topology |
| [Mixed-rank representation parents](MULTIPLICATIVE_RECURRENCE_AND_MIXED_PARENTS.md#4-the-mixed-rank-determinant-parent-question) | A universal finite graded determinant parent exists exactly when the nontrivial input ranks are empty, one rank, or `(2,2)`; the unique formal escape has a negative second relation module whenever at least two ranks exceed one | Universal representation identities, not fitted matrix eigenvalues or convergent infinite determinants |
| [Fixed-label cycle response](../../../exploratory/fixed-label-cycle-response/README.md) | Two colored directed sources with the same entire commutative determinant have different three-sheet lift responses; the real part of the third-trace gap is an exact commutator energy | Fixed label identifications matter; the response is not vertexwise gauge invariant and is not attached to zeta |

The first lane treats arbitrary continuous multiplicative maps and arbitrary
mixed input ranks, beyond the eleven local-power packets already present at
the frozen base. The second starts with independently specified vertices,
colored edges, and label matrices, rather than selecting eigenvalues from a
desired scalar output.

## Source and ownership boundary

- Base: `ab7ebfa3d4e3f1a657b4127b40796953060b6b3e`, the current #766 head
  when this branch began. Existing #766 files were not rewritten; a README
  entry and separately named theorem/replay files were added.
- Core first proof: `4f4950e47`; exact replay and discrete-moduli checkpoint:
  `0f7be357b`; corrected core freeze: `8834fdc7a0dfe15f6bb95eefe0729cb77c93c807`.
  The [independent frozen-source review](REVIEW_8834fdc7.md) covers that
  core and found no remaining mathematical or implementation blocker.
- Circle companion freeze: `ee7318869424ee7c333a03b87992f33e12072bf9`.
  Its [independent review](REVIEW_ee731886.md) found no remaining blocker
  for the complete probe classification and connected-family corollary.
- Graph source: `26314df4e5ed9a5c16b7da61e155a48d325789cc`, imported by
  cherry-pick. The integration at `b800f754d3c53d61746dfb3a068e250c53b62771`
  includes the reviewed real-part wording and packet-local LF checkout
  metadata. Its frozen fixture was replayed without changing expected output.
- The separate #763 actual-source branch is not a mathematical dependency
  of these results. No sheaf/graph comparison map is assumed or constructed.
- Active all-prime Satake-deformation and Estermann-completion work elsewhere
  was identified before choosing this scope and is not duplicated here.

All edits belong to this isolated worktree. No original checkout, other
agent branch, build cache, or large computation was changed by this lane.

## What the two lanes can actually say together

The graph theorem proves an exact failure of descent from a scalar shadow:
no function of the commutative determinant alone recovers the declared
fixed-label lift response on the stated source class. Therefore no scalar
postprocessing of its coefficients, including the multiplicative recurrence
preservers classified here, can recover that response either. This last
consequence is simple composition: equal inputs remain equal after every
such postprocessing.

That is the shared structural lesson and the full logical connection. The
two lanes do not identify graph cycles with arithmetic primes, give a
functor from the #763 source sheaf to graphs, or transfer positivity to an
arithmetic explicit formula. A proposed arithmetic adapter would have to
be a new theorem with its own inputs and normalization.

The graph example also preserves the correct transpose duality when labels
are transposed along with the reversed source. It is the fixed-label
response that differs. This distinction and the explicit failure of
vertexwise gauge invariance prevent a misleading claim of intrinsic
arithmetic geometry.

## Evidence and bounded replay

The corrected core packet passed 27 focused tests under ordinary Python and
the same 27 under optimized Python, together with both full producer checks
and focused Ruff validation. The circle companion passed 14 tests in each
mode, both producer checks, and Ruff validation. The integrated graph packet
passed 18 tests in each mode and both producer checks. Independent reviews
are bound to the frozen core and companion sources above and the graph
source in its own review sidecar; they report the serialized test results
without claiming independent runs.

The root agent serialized these runs to avoid competing with another
active Codex agent. The core replay took about three seconds per complete
validation cycle on this host. It uses 16 circle rows, a bounded mixed-rank
census, eight local Gaussian-rational controls, four small tensor-matrix
controls, and bounded integer moduli counts. No build, CAS, prime sweep,
zero scan, large-field enumeration, or parallel local test farm is required.
The circle companion adds 29 exact touching-circle controls, 24 polynomial
probe controls, 36 explicitly labeled theorem specializations, and two
held-out-center controls. The specializations are not finite certificates
of analytic nonrationality.

From this branch, the release checks are:

```text
python -B research/l-families/atlas/generalized/multiplicative_recurrence_mixed_parents.py --check
python -B -O research/l-families/atlas/generalized/multiplicative_recurrence_mixed_parents.py --check
python -B -m unittest tests.test_multiplicative_recurrence_mixed_parents
python -B -O -m unittest tests.test_multiplicative_recurrence_mixed_parents
python -B research/l-families/atlas/generalized/circle_probe_geometry.py --check
python -B -O research/l-families/atlas/generalized/circle_probe_geometry.py --check
python -B -m unittest tests.test_circle_probe_geometry
python -B -O -m unittest tests.test_circle_probe_geometry
python -B research/exploratory/fixed-label-cycle-response/cycle_response.py --check
python -B -O research/exploratory/fixed-label-cycle-response/cycle_response.py --check
python -B -m unittest discover -s research/exploratory/fixed-label-cycle-response/tests
python -B -O -m unittest discover -s research/exploratory/fixed-label-cycle-response/tests
```

The JSON certificates bind source files and exact outputs. They are not
machine proofs of the all-parameter analytic, topological, or representation
theorems. Ordinary and optimized checks have the same acceptance logic;
scientific validation does not depend on Python `assert` statements.

## Ranked continuation queue and stop rules

1. **A genuinely analytic parent.** Start from the forced formal virtual
   grades, specify an independently defined topology and operator, and
   prove the scalar recovery and determinant convergence contract. Stop if
   the proposal only places preselected coefficients on a diagonal.
2. **An intrinsic extension of the graph observable.** Replace the fixed
   sheet-space identification with extra declared source data or a
   gauge-invariant comparison and prove which information survives. Stop
   if a gauge change silently alters the comparison being claimed.
3. **Actual arithmetic coherence.** Select one existing arithmetic family
   and prove a literal twist/duality/ramification compatibility statement.
   Do not label scalar twist weight, local rationality, or a formal
   determinant identity as that statement.
4. **Arithmetic cancellation strata.** Replace the generic complex
   noncollision hypothesis by a stated arithmetic coefficient image and
   classify the surviving spectrum there. A finite trace table is not the
   classification.

No additional scan of elementary power examples is prioritized. The
classical Fourier, Hadamard, Segre, graph-zeta, and representation literature
is cited at the theorem sites; no external publication priority is claimed.
