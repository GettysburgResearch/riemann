# Formalization Reviewer C: repaired Xi/operator QA report

## Freeze and status

```text
repository:       gfreund123/riemann
bootstrap merge:  573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f
primary PR:       #735
repair branch:    formal/030-xi-operator-qa
binding review:   PR #749 @ 9da1e250b647575418290407c6e30054322bb581
research cutoff:  PR #707
RH:               UNPROVED
```

No workflow file, Reviewer A theorem, Reviewer B theorem, or A/B registry delta
is modified by this repair.

## Preserved exact finite algebra

The accepted finite layer is retained:

- exact two-point Pick determinant identity;
- exact three-node determinant and reciprocal/companion divided-difference
  factorization;
- exact two- and three-dimensional LDL/congruence identities;
- PSD versus PD separation and a PSD-not-PD fixture;
- finite positive-sum reciprocal-concavity algebra;
- finite Hermite and Q4 identities;
- the six minimal finite operator firewalls.

The repair changes the source-specific wrappers and QA evidence, not these
accepted algebraic statements.

## Concrete actual-Xi and external inputs

The repaired comparator dependency module defines the actual completed function
explicitly:

```text
riemannXi(s)   = (1/2) s (s-1) completedRiemannZeta(s)
centeredXi(z)  = riemannXi(1/2+z)
actualXiNodeP(x) = Re(centeredXi'(x)/(x centeredXi(x)))
```

The old arbitrary proposition labels are removed. The replacement declarations
state:

- the exact height `3000175332800`;
- the exact critical-line conclusion imported from the external publication;
- title, authors, journal, DOI, arXiv identifier, artifact identifier, and a
  normalized theorem/citation SHA-256 independent of the local claim blob;
- one injective reflected off-line representative convention, its reflected partner,
  and analytic-order multiplicity equalities on both sides;
- the grouped actual-Xi zero expansion;
- locally uniform convergence of values and derivatives zero, one and two on
  `t>1/4`, both for the raw grouped expansion and the exact paid-prefix
  regrouping;
- the selected critical reserve and exact `(m0-1)R0` residual;
- the reciprocal-square finite-prefix tail inequality and numerical budget;
- exact source-faithful paid prefixes formed from unspent reserve, the
  `(m0-1)R0` residual, paid off-line blocks and all other critical blocks;
- nonnegative shares, every orbit paid, total use at most one, one-use identity,
  and nonnegative leftover.

Simplicity is not an input to the repaired headline and no simplicity proposition is installed by the external source lock.

The external machine lock is
`formal/registry/deltas/C_EXTERNAL_SOURCE_LOCKS.tsv`; it is separate from the
canonical scientific claim source SHA.

## Source-specific reserve algebra

`RiemannFormal.Operator.XiSourceSpecific` now contains:

- the exact off-line defect formula;
- the exact transformed cross-curvature formula with
  `Q_kappa(s)` and complete denominator/domain hypotheses;
- `epsilon = 2 m kappa/(1-kappa)`;
- the exact payment inequality;
- derivation of `c-r >= (2/3)b^2`, `kappa <= 9/(4b^2)`, `kappa<1/2`, and
  `epsilon <= 9m/b^2` from the concrete orbit/reserve hypotheses;
- multiplicity-aware reflected-orbit data;
- construction of a source-locked finite-prefix one-use reserve allocation from exact tail
  and numerical-budget inputs.

The complete global analytic tail and grouped convergence remain explicit
hypotheses. The local algebra is not mislabeled as proving those inputs.

## Repeated-node repair

No theorem accepts a premise that directly returns `IsPSD3` on a repeated-node
branch. Values are evaluations of the one function `actualXiNodeP`.

For positive nodes, equality of squared nodes implies equality of nodes. Equal
nodes therefore have equal function values and duplicate rows/columns. Exact
congruence identities reduce duplicate `12`, `13`, and `23` packets to the
actual-Xi order-two PSD theorem.

The full headline records one-node nonnegativity, all two-node principal
packets, and the complete three-node packet for every positive triple, and
concludes PSD only.
It contains no distinct-node PD or order-four statement.

## Semantic split

`formal/registry/deltas/C.tsv` now maps source-specific canonical IDs only to
source-specific declarations. Generic finite lemmas are recorded separately in
`C_API.tsv` under `FORMAL.API.OPERATOR.*` identifiers and are not used as
surrogates for stronger actual-Xi claims.

The following canonical declarations are `PROVED_CONDITIONAL` because their
precise external, convergence or source-bridge hypotheses remain explicit:

- actual-Xi order two;
- actual-Xi companion curvature;
- complete critical reserve budget;
- actual-Xi reciprocal concavity;
- full actual-Xi PSD through sizes one, two and three;
- the stated low-order Loewner interface.

## Comparator fidelity

`XiPickOrderThreeConditional` now uses one shared Mathlib-only
`ChallengeStatement`. The formal library proves that exact proposition; the
Challenge states that exact proposition with one placeholder; the Solution is
sorry-free and reuses the library theorem. The statement includes concrete
external structures, the exact reserve statement, the source-faithful paid-prefix
C2 limit, repeated nodes, PSD only, and
no order-four conclusion.

`verify_comparator_fidelity.py` compiles Challenge and Solution separately and
checks equal normalized theorem signatures. For the headline it additionally
type-checks both against the exact shared `ChallengeStatement`.

## Generated QA evidence

The repair removes manually trusted evidence booleans.

- `verify_declaration_map.py` imports the built Lean environment and executes
  fully qualified `#check` and `#print` commands for every C canonical and API
  declaration.
- `check_statement_sources.py` derives canonical source fidelity, external lock
  fidelity, formal-status consistency and comparator/source evidence from the
  registries and exact Lean source-lock object.
- `check_external_input_usage.py` builds the source dependency closure of the
  headline, rejects the former arbitrary labels and wholesale repeated-node
  premise, and requires every concrete bridge/reserve/repeated-node dependency.
- `check_axioms.sh` generates its audit declaration set from `C.tsv` and
  `C_API.tsv`, then parses every output against the standard Lean axiom allowlist.
- `check_no_sorry.sh` enforces the Challenge-only placeholder boundary and runs
  the declaration, source, comparator and dependency audits.

Generated Lean evidence is written under `formal/reports/generated/` by the exact-head
suite rather than asserted in the committed TSV.  The committed
`C_REPAIR_STATIC_REPLAY.json` records nine exact `Fraction` regression fixtures
for the cross-curvature, defect/payment, duplicate-row identities, and the
recomputed external-statement hash; it is diagnostic and does not replace Lean.

## Validation boundary

The complete runnable suite is:

```bash
bash formal/scripts/run_c_repair_validation.sh
```

This publication environment does not contain Lean/Lake and therefore does not
claim that the repaired head compiled here. A separate laptop Codex will run the
suite. Until that exact-head run passes, build status is
`PENDING_INDEPENDENT_EXACT_HEAD_BUILD`.

## Literal conclusion

```text
formal RH proof: NONE
Riemann Hypothesis: UNPROVED
```
