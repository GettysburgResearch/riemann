# Integration handoff — Reviewer A cross-review of Reviewer B

**Primary review:** PR #708 at `eb1987502ef9043e782ac6ab1e19c47be9daef93`  
**Frozen main:** `677203992eb0168920365ee45ae9db76bfa97dcf`  
**RH:** unproved.

## Reconciliation disposition

PR #708 is a strong scientific review and should be retained as evidence. It is not yet a canonical machine-traversable graph.

### Required before integration

1. Split `CONSUMER.MELLIN.SUBPOWER_NEGATIVE_MASS` into:
   - a verified analytic implication API;
   - an open source-faithful arithmetic estimate.
2. Register every route-edge premise and conclusion as a semantic node.
3. Add the omitted fixed `5:3` scalar and its separate open producer premise.
4. Reclassify `SACF` as `OPEN_SUFFICIENT_FOR_RH`; retain `UOSACF` as `OPEN_RH_EQUIVALENT`.
5. Move the unquantified Brownian "new producer" category out of theorem reachability.
6. Replace `PR_BODY`, directory and wildcard provenance with exact PR/head/path/internal-ID records.
7. Deposit a deterministic registry/reachability validator.
8. Apply the PR #446 local fixes:
   - replace corrupt verifier;
   - repair external source lock;
   - retain residual multiplicity of the selected critical orbit or import its simplicity;
   - state PSD canonically and prove strictness separately if positive definiteness is wanted.
9. Reconcile the omitted Q4/Q4-Hermite candidates with Reviewer C.

## Scientific decisions

```text
actual-Xi Pick PSD through order three       ACCEPT WITH FIXES
fixed rows 2,3 Mellin consumer               ACCEPT
fixed 5:3 scalar                             ADD OMITTED NODE
PR #641 moving-row conclusion                GAP / EXCLUDE
uniform-center fractional heat               REFUTED / RETAIN
First-Hermite criterion and regions          ACCEPT WITH FIXES
Q4 annular and Type-I/II reductions          ACCEPT WITH FIXES
SACF                                          OPEN SUFFICIENT, NOT EQUIVALENT
UOSACF                                        OPEN RH-EQUIVALENT
Brownian Bohr no-go                           RETAIN
```

## Minimal blockers after reconciliation

No proven-only route reaches RH. The open conclusion-facing inputs remain:

- fixed source-faithful row/scalar positivity or subpower negative mass;
- actual-`Xi` Pick orders four and above;
- coefficient-one first-chaos domination;
- fixed/pole-centered signed heat;
- First-Hermite constant-four signed prime cancellation;
- Q4 UOSACF/balanced Type-II cancellation;
- a Brownian producer outside the reviewed Bohr class;
- corrected Weil/Fredholm all-order signs.

## Reviewer D use

Use `VERDICT_DELTA.tsv` for changed/accepted verdicts, `GRAPH_DEFECTS.tsv` for registry repairs, `SOURCE_PROVENANCE_FIXES.tsv` for exact-object extraction, and `MISSED_CLAIM_CANDIDATES.tsv` only as a queue to reconcile against Reviewer C. Do not treat the omitted-candidate table as a complete census.
