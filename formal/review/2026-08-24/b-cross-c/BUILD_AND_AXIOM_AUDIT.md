# Build and axiom audit

## Frozen object

- Repository: `gfreund123/riemann`
- Bootstrap base: `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f`
- Target PR: `#735`
- Frozen target head: `4863c31dd497ffe69ea400fe29275decf4cb5d29`
- Target branch: `formal/030-xi-operator-qa`
- Review branch: `formal/review/2026-08-24/b-cross-c`
- RH proved: **NO**

The target head was re-read from GitHub before the audit and was unchanged.

## Requested command matrix

| Command | Frozen-head result | Evidence boundary |
|---|---|---|
| `lake exe cache get` | **BUILD_FAILURE: no executable run obtained** | The audit container has neither `lake` nor `lean`, and no networked Mathlib cache. |
| `lake build` | **BUILD_FAILURE: no executable run obtained** | PR #735 exposes no workflow run/status. |
| `lake build Challenge.XiPickThreeNode Solution.XiPickThreeNode` | **NOT EXECUTED** | Both exact files exist; the solution is sorry-free by static read-back. |
| `lake build Challenge.OperatorPositiveSchurRescue Solution.OperatorPositiveSchurRescue` | **NOT EXECUTED** | Both exact files exist; the solution directly invokes the formal firewall. |
| `lake build Challenge.XiPickOrderThreeConditional Solution.XiPickOrderThreeConditional` | **NOT EXECUTED** | Files exist, but the challenge covers only the ordered-distinct generic theorem. |
| `python3 scripts/generate_registry.py` | **NOT EXECUTED ON A COMPLETE CHECKOUT** | Source inspected; no full local target checkout/toolchain was available. |
| `python3 scripts/validate_registry.py` | **NOT EXECUTED ON A COMPLETE CHECKOUT** | Same boundary. |
| `python3 scripts/verify_source_locks.py` | **NOT EXECUTED ON A COMPLETE CHECKOUT** | Static audit shows it locks repository/toolchain dependencies, not the external high-zero theorem. |
| `python3 scripts/validate_blueprint.py` | **NOT EXECUTED ON A COMPLETE CHECKOUT** | Blueprint content was read back and audited manually. |
| `python3 scripts/verify_declaration_map.py` | **STATICALLY AUDITED; NOT EXECUTED** | It checks a declaration leaf by regex, not the fully qualified type. |
| `python3 scripts/check_statement_sources.py` | **STATICALLY AUDITED; NOT EXECUTED** | It trusts manually supplied evidence booleans. |
| `bash scripts/check_no_sorry.sh` | **STATICALLY AUDITED; NOT EXECUTED** | Target patch contains exactly three `sorry`s, all in the three Challenge files. |
| `bash scripts/check_axioms.sh` | **STATICALLY AUDITED; NOT EXECUTED** | The generated Lean axiom output is unavailable without a build. |

A disposable review-only branch was pinned to the exact target head, one inert
file was added, and temporary PR #748 was opened and marked ready so the existing
workflow could run without changing PR #735. GitHub exposed no workflow run or
commit status for either the target head or the probe head. The probe therefore
does not supply build evidence.

This is an **absence-of-verification** verdict, not a claim that Lean compilation
has been shown to fail.

## Static trust-boundary audit

### Placeholder isolation

The frozen PR patch has exactly three `sorry` occurrences:

1. `Challenge/OperatorPositiveSchurRescue.lean`
2. `Challenge/XiPickOrderThreeConditional.lean`
3. `Challenge/XiPickThreeNode.lean`

No `sorry` or `admit` occurs in Reviewer C's changed `RiemannFormal`,
`ChallengeDeps`, or `Solution` files. No changed trusted file declares a custom
`axiom`, `opaque`, or `unsafe` declaration.

This static result is consistent with the intended challenge/solution boundary,
but it does not replace compilation or `#print axioms`.

### Axiom audit mechanics

`check_axioms.sh` compiles `RiemannFormal/AxiomAudit.lean` and every
`comparator/PrintAxioms/*.lean`, then permits only `propext`,
`Classical.choice`, and `Quot.sound`.

The output parser rejects `sorryAx` and missing/unexpected output for the
`#print axioms` statements it discovers. That part is well designed.

The missing fail-closed joint is registry completeness: no script derives the
expected axiom-audit declaration set from `C.tsv`. The current manual
`AxiomAudit.lean` appears to contain all present C delta declarations, but a
future or mistyped row can evade the audit.

### External propositions are not axioms, but are not source locks

`XiOrderThreeExternalInputs` contains proof fields for six arbitrary
proposition parameters. This does not introduce a custom axiom: theorem users
must supply those proofs. It also does not lock the intended mathematics. The
type contains no verified height, source theorem, grouped Xi expansion, orbit
quotient, multiplicity residual equation, or reciprocal-square tail statement.
`#print axioms` cannot detect that semantic weakness.

## Independent exact replay

`replay/symbolic_operator_replay.py` uses exact symbolic arithmetic and passed:

- two-point Pick determinant identity;
- three-node determinant factorization;
- three-dimensional LDL identity;
- reciprocal-concavity cross-square certificate;
- off-line orbit curvature formula;
- all finite firewall witnesses.

No floating arithmetic is used.

## Build verdict

```text
FULL LEAN BUILD:                 NOT ESTABLISHED
COMPARATOR BUILDS:               NOT ESTABLISHED
GENERATED AXIOM OUTPUT:          NOT ESTABLISHED
STATIC SORRY BOUNDARY:           PASS
STATIC CUSTOM DECLARATION SCAN:  PASS
EXACT SYMBOLIC REPLAY:           PASS
OVERALL BUILD/TRUST VERDICT:     BUILD_FAILURE
RH PROVED:                       NO
```

A successful authoritative frozen-head workflow run is an exact integration
blocker.
