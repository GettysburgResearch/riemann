# Formalization Reviewer B repair report

## Freeze

- Repository: `gfreund123/riemann`
- Bootstrap base: `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f`
- Primary PR: `#733`, branch `formal/020-arithmetic-mellin`
- Binding cross-review: PR `#750` at
  `81d201849514224d0a5899ac6b61dc66a71b8d1e`
- Research cutoff: PR `#707`
- RH status: **UNPROVED**

This repair preserves exact finite algebra while removing canonical names and
formal statuses from statements that proved only weaker helpers.

## P0 repairs

### First-owner fidelity

The declarations `nativeEuler`, `firstOwner`, and
`firstOwner_eq_nativeEuler` were replaced by explicitly generic names:

- `finiteEulerProduct`;
- `scalarFirstOwnerExpansion`;
- `scalarFirstOwnerExpansion_eq_finiteEulerProduct`.

The canonical row `ARITH.SHARP.SEQUENTIAL_FIRST_OWNER` is now
`BLOCKED_MATHEMATICS`.  The generic lemma does not encode the labelled
occurrence, commuting-shift, complete-future-product, accumulated-parity, or
disjoint/exhaustive ownership content of reviewed `L-99601`.

### Exact source firewalls

The previous numeral-only RN and normalization examples were replaced by:

- the exact SHARP target `T(y)=(4 sqrt(y)-3) 1_{y>=1}`;
- raw cutoff and RN density definitions;
- exact `(Y,Z,t)=(16,4,4)` theorems giving parent `5`, child `1`, RN density
  `1/5`, raw cutoff `1`, and the transport identity;
- typed response/capacity sources built from that exact cell;
- a quantified theorem for every real `p>1` proving
  `p^-1 < p^-1/2`, hence inequality;
- a quantified `r` versus `2r^2` theorem on `0<r<1/2`;
- two distinct labels over prime `67` and an accumulated-parity fixture.

The role-indexed API is documented honestly.  It blocks implicit substitution
of different role parameters, but public coefficient projection and explicit
reconstruction remain available.  The fixed/moving detector structures record
data shape; query independence is a separate proposition.

### Circular RH assembly removed

`fixed_native_subpower_negative_mass_implies_RH` and its arbitrary `consumes`
field were removed.  `FixedDetectorAssembly.lean` now contains only:

- fixed native source/detector data;
- one- and two-row numerator certificates;
- exact five-three and rows-2/3 arithmetic packages;
- specification theorems whose conclusions are only coefficient identities and
  numerator noncancellation.

No theorem in Reviewer B's Mellin-Landau module concludes RH.  Final analytic
composition is deferred until Reviewer A's repaired API is reconciled.

## P1 scope repairs

### Wavelet

The generic finite statements were retained but renamed:

- `ratioEight_support` -> `dyadic_four_tap_index_span`;
- `factor67_antisymmetry` -> `affine_nuisance_sign_flip`;
- `finite_abel_mertens` -> `finite_sum_by_parts`;
- `sameK1Translation` -> `sameKernelIdentity`.

The canonical minimal ratio-eight kernel, factor-67 piecewise identity,
Abel-Mertens frame, and quantitative same-K1 translation remain
`BLOCKED_MATHEMATICS`.  The false historical K0/K1 edge is not a formal proof
dependency.

### Half-divisor

The following exact scopes remain proved:

- `etaCoeff_antidiagonal`;
- `eta_mul_eta` at `ArithmeticFunction ℚ` Dirichlet-convolution scope;
- `genericOneFieldConvolution`.

The last theorem was renamed from `oneFieldReduction` because it does not
formalize the reviewed `b_U/h_U` fields, ratio-four kernel, Hardy norm-three
estimate, endpoint localization, or signed near-collision statement.

## Registry and provenance

`formal/registry/deltas/B.tsv` now keeps only the exact rows-2/3 and fixed 5:3
claims as `PROVED`, and the exact alpha-child coefficient refutation as
`REFUTED_FORMALIZED`.  Canonical claims represented only by partial helpers are
`BLOCKED_MATHEMATICS`.

`formal/registry/deltas/B_SOURCE_LOCKS.tsv` separately locks every accepted
local theorem to an exact PR, SHA, path, claim ID, and literal formal scope.
Its header deliberately does not use the sparse-registry `semantic_id` field,
so the bootstrap registry generator does not treat local helper rows as
canonical status overrides.

`formal/blueprint/src/content-B.tex` marks incomplete canonical nodes
`\notready` and removes the false five-three-to-RH `\uses` edge.

## Trust direction

`RiemannFormal.Arithmetic` no longer imports `ComparatorSmoke`; the trusted
library therefore does not depend on solution modules.  Comparator solutions
remain separate and are audited by
`comparator/PrintAxioms/ArithmeticFixedRows.lean`.

## Axiom coverage

`RiemannFormal.Arithmetic.AxiomAudit` directly prints axioms for:

- rows 2/3 and fixed 5:3;
- the renamed scalar first-owner helper;
- labelled duplicate/parity;
- `r` versus `2r^2`;
- exact RN raw-cutoff/response/capacity fixtures;
- quantified normalization;
- role separation and explicit reconstruction;
- fixed-to-moving query independence;
- half-divisor coefficient, convolution, and generic one-field identities;
- generic tap/minimality/shift/summation helpers;
- K0/K1 type separation;
- the non-circular arithmetic input specifications.

The comparator print module audits both B comparator solutions.

## Validation commands

The repaired tree preserves the requested suite:

```bash
cd formal
lake exe cache get
lake build
lake build Challenge.ArithmeticRows23 Solution.ArithmeticRows23
lake build Challenge.FixedDetectorFiveThree Solution.FixedDetectorFiveThree
python3 scripts/generate_registry.py
python3 scripts/validate_registry.py
python3 scripts/verify_source_locks.py
python3 scripts/validate_blueprint.py
bash scripts/check_no_sorry.sh
bash scripts/check_axioms.sh
```

This repair environment did not possess Lean/Lake or a Mathlib cache.  The
exact remote head is intended for the separately requested laptop compilation;
no unexecuted build is reported as passing here.
