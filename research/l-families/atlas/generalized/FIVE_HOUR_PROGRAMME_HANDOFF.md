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

The machine-readable [L0-L9 survival map](PROGRAMME_L0_L9_SURVIVAL_MAP.json)
compares seven transformation/source classes across all ten programme
levels and pins their proof commits. Its `qualified` status may record a
partial theorem or an obstruction; it never means that the entire
arithmetic level survived. In particular a finite graph operator, virtual
representation, or commutator energy is not arithmetic L8 or L9 evidence.

| Lane | New repository result | Exact stopping boundary |
|---|---|---|
| [Multiplicative recurrence preservers](MULTIPLICATIVE_RECURRENCE_AND_MIXED_PARENTS.md) | One nondegenerate shifted-circle recurrence test classifies every continuous multiplicative map as `z^m bar(z)^n`; the bounded-degree moduli and continuous-deformation obstruction are exact | Continuous scalar maps and ordinary recurrences; no prime-indexed or ramified family |
| [Complete circle-probe geometry](CIRCLE_PROBE_GEOMETRY.md) | An origin-touching circle leaves infinitely many false positives at each fixed positive degree; every positive non-touching center eliminates them. Connected pointwise-continuous families passing the touching probe are constant | Prose classification for irrational rotations; no natural-boundary theorem or general local-constancy claim in the degenerate topology |
| [Mixed-rank representation parents](MULTIPLICATIVE_RECURRENCE_AND_MIXED_PARENTS.md#4-the-mixed-rank-determinant-parent-question) | A universal finite graded determinant parent exists exactly when the nontrivial input ranks are empty, one rank, or `(2,2)`; the unique formal escape has a negative second relation module whenever at least two ranks exceed one | Universal representation identities, not fitted matrix eigenvalues or convergent infinite determinants |
| [Fixed-label cycle response](../../../exploratory/fixed-label-cycle-response/README.md) | Two colored directed sources with the same entire commutative determinant have different three-sheet lift responses; the real part of the third-trace gap is an exact commutator energy | Reusing fixed numerical labels after changing fibre identifications is not gauge invariant; no arithmetic zeta attachment |
| [Based holonomy response](../../../exploratory/marked-holonomy-response/README.md) | Two marked word-cycle automata have identical responses under every abelianized representation; their full unitary responses agree exactly when the two holonomies commute. The based source makes the commutator response gauge covariant and predicts complete lifted cycle lengths | Additional based representation and word/clock data are declared, not recovered from the original scalar graph shadow; no arithmetic adapter |
| [Positive holonomy defect](../../../exploratory/marked-holonomy-response/POSITIVE_DEFECT_AND_CRITICAL_CIRCLE.md) | The same finite source gives a positive Gram operator, unitary determinant roots on the unit circle, and reciprocal duality; permutation principal constants remain in the positive operator's kernel | Finite graph mechanisms only; positive total trace does not give a principal lower bound or any arithmetic critical-line statement |

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
- Based-holonomy source: `e7fc8b0af2c42ce43384543972df2ed44f343300`, imported
  at `d3c0b7c80`. It is a separately defined source with extra marked data,
  not a rewrite of the original fixed-label obstruction. Its
  [source review](../../../exploratory/marked-holonomy-response/REVIEW_E7FC8B0A.md)
  and integrated replay are separate from the original packet.
- Positive-defect sequel source: `6b4f0f4a53bc9ff5bc6b84a2b6e3f603a04f2336`,
  imported at `eebbb8951`. Its proof and five additional tests leave the
  original based-holonomy producer and canonical fixture unchanged.
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

The based-holonomy companion addresses that boundary by declaring extra
source data: a free-group representation and marked word-cycle automata,
with one clock step per edge. Its character response descends under
simultaneous conjugation, and basis changes on each already defined
automaton preserve its determinant and trace. This is an explicit
enrichment that makes the comparison natural. It does not reverse the
earlier counterexample about reusing numerical labels after discarding
their common based identification, and it does not supply an arithmetic
source map.

The positive-defect sequel strengthens the finite mechanism to
`H=(I-K)*(I-K)/2>=0`, reciprocal unitary determinant duality and an exact
spectral circle. It also exposes the relevant limitation: in permutation
sources the global constant vector lies in `ker(H)`, even when `tr(H)>0`.
Thus the example supplies no positive lower bound on its principal line.
This is a concrete failure of a proposed inference from total positivity,
not an obstruction to every arithmetic method.

## Evidence and bounded replay

The corrected core packet passed 27 focused tests under ordinary Python and
the same 27 under optimized Python, together with both full producer checks
and focused Ruff validation. The circle companion passed 14 tests in each
mode, both producer checks, and Ruff validation. The integrated graph packet
passed 18 tests in each mode and both producer checks. Independent reviews
are bound to the frozen core and companion sources above and the graph
source in its own review sidecar; they report the serialized test results
without claiming independent runs.
The based-holonomy companion and positive-defect sequel passed fourteen
tests in each mode, with the original producer checks unchanged, at their
source branch; final imported replay is a separate release check. This
brings the four replay directories to 73 focused tests per Python mode.

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

The core and circle source freezes are direct ancestors of this branch.
The original graph commits have different identities from their imported
cherry-picks and are preserved on a separate review-source branch. Before
replay, acquire that history with:

```text
git fetch --no-tags origin refs/heads/codex/review-sources-fixed-label-cycle-five-hour
```

A shallow checkout must also acquire the required full histories. Check
with `git rev-parse --is-shallow-repository`; if it reports `true`, run
`git fetch --unshallow --no-tags origin`, then fetch the review-source
branch above. A missing frozen object is a provenance failure to repair by
fetching its history, not by weakening the checker or replacing its SHA.

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
python -B research/exploratory/marked-holonomy-response/holonomy_response.py --check
python -B -O research/exploratory/marked-holonomy-response/holonomy_response.py --check
python -B -m unittest discover -s research/exploratory/marked-holonomy-response/tests
python -B -O -m unittest discover -s research/exploratory/marked-holonomy-response/tests
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
2. **A native adapter to the based holonomy source.** The finite-model
   gauge repair is now explicit. Select an independently defined arithmetic
   or geometric source and prove a literal map preserving a specified native
   observable. Stop if the map is fitted to the desired scalar output or
   silently discards the marking, representation, or clock needed for it.
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
