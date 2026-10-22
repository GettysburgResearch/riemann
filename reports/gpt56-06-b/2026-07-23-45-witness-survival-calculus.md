# Session report — Issue #45 finite-witness survival under uncertainty

Agent: `gpt56-06-b`  
Issue: #45  
Branch: `agent/gpt56-06-b/45-witness-survival-calculus`  
Date: 2026-07-23  
Status: proposed proof infrastructure; no RH counterexample candidate

## Starting hypothesis

The project can make the phrase “this finite witness cannot disappear under all
remaining uncertainty” mathematically precise by separating three different
problems:

1. logical correctness of the criterion and concrete formula;
2. quantitative movement of the decisive value under every admitted error;
3. residual trust in implementations, libraries, compilers, and proof kernels.

Only item 2 is a robust-margin problem.  Item 1 requires proofs.  Item 3 requires
trusted-base reduction, independent reconstruction, and where practical formal
verification.

## Existing work audited

The contribution was designed not to duplicate:

- `L-3101`, which quantifies preservation of a negative finite form under
  vector rounding and matrix perturbation;
- `L-3102`, which bounds omitted carrier prime blocks relative to the Gram
  matrix;
- `M-0901`, which gives complete-stream, resolution, carrier-locality, and
  independent-cross-check gates for one carrier route;
- the exact fixed-vector certificate architecture in PRs #4, #22, #33, #38,
  #43, and #44.

Those are treated as route-specific producers of sound uncertainty blocks.  The
new question is how to prove that the list is complete and that all blocks
compose to a strict surviving root predicate.

## Main result 1 — witness survival is root-set containment

D-4501 defines an exact finite witness `w`, a complete family of logical gates,
a declared quantitative uncertainty set `U`, an exact evaluator `Y(w,u)`, and a
disproof region `D`.

The decisive certificate is

\[
 \{Y(w,u):u\in U\}\subseteq C\subseteq D.
\]

For a scalar negative witness, this is simply

\[
 \sup_{u\in U}Y(w,u)<0.
\]

The strict distance from `C` to the complement of `D` is the **moat**.  A
midpoint, precision ladder, or agreement between implementations is not the
mathematical object; the complete uncertain image is.

The definition is deliberately closed-world.  “All uncertainty” means every
uncertainty channel in the exact declared semantics.  A wrong theorem, wrong
normalization, incomplete formula, or unsound primitive is not a perturbation to
be absorbed by the moat; it is a blocking logical or trusted-base defect.

## Main result 2 — local soundness composes

L-4501 treats the evaluator as a finite DAG.  Every leaf is exact or carries a
sound enclosure.  Every internal abstract transformer proves that its output
contains every exact result from its input sets.  Topological induction then
proves that the root enclosure contains every admitted exact root value.

This imports the useful theorem shape of abstract interpretation without
making the RH claim depend on an external theorem: the finite proof is included
in the claim file.

The accompanying closure condition requires exact equality between declared
quantitative channel IDs and channels used by the root computation.  Hidden,
duplicated, and decorative uncertainty are rejected.

## Main result 3 — robust counterparts preserve correlation

L-4502 writes an affine decisive score as

\[
 q(u)=q_0+a^Tu
\]

and reduces survival to a support-function bound.  Independent intervals give
the familiar sum of absolute-radius losses, but that sum is justified only when
the total uncertainty is actually the corresponding product/Minkowski set.

For a rational polytope `Au<=b`, exact rational multipliers

\[
 y\ge0,\qquad A^Ty=a
\]

prove

\[
 \sup a^Tu\le b^Ty
\]

by weak duality.  Thus a high-performance producer may solve an LP, while the
small checker verifies only nonnegativity, exact equalities, feasibility of one
anchor, and the strict final rational sign.

The synthetic control

\[
 q=-1/10+u_1+u_2,
 \qquad |u_i|\le1,
 \qquad u_1+u_2=0
\]

has exact robust upper `-1/10`.  Forgetting the correlation gives `19/10` and
loses the witness.  This demonstrates why “add every worst-case error” is sound
but not systematically sharp enough.

## Main result 4 — contract Pick uncertainty before enclosure

L-4503 proves for the PR #38 Pick matrix that a fixed exact vector satisfies

\[
 v^*Kv=2\operatorname{Re}\sum_j c_jF(s_j),
\]

where every `c_j` is reconstructed exactly from the points and vector.  The
matrix should therefore never be intervalized entry by entry.  Direct symbolic
contraction preserves repeated use of the same `F(s_j)` and reduces the proof to
one linear functional of the primitive sample balls.

For independent complex disks, the robust upper is the exact midpoint
functional plus

\[
 2\sum_j |c_j|r_j.
\]

For correlated jet/range-reduction errors, the same contracted functional can
be maximized over a polytope, affine form, or Taylor model.

## X-4501 exact checker

`verify.py` uses only Python integers and `fractions.Fraction`.  It supports:

1. exact independent affine boxes;
2. exact LP weak-dual certificates for correlated rational polytopes;
3. exact Pick fixed-vector compression with rational complex disks.

It verifies uncertainty-manifest set equality and fails closed on blocking gate
metadata.  Gate metadata is not itself treated as mathematical proof.

### Exact committed controls

- affine-box survivor: robust upper `-4/5`;
- affine box touching zero: `NOT_CERTIFIED`;
- correlated-polytope survivor: robust upper `-1/10`;
- Pick disk survivor: robust upper `-110719/52000`;
- same Pick midpoint with enlarged radii: robust upper `82/65`, therefore
  `NOT_CERTIFIED`.

Fifteen tests pass.  Mutations reject hidden and decorative channels, a blocking
gate, a broken dual equality, an infeasible uncertainty anchor, an understated
Pick coefficient magnitude, a boundary sample point, and a false claimed root
endpoint.

All controls are synthetic exact algebra.  No `zeta` or `xi` value was evaluated.

## Cross-disciplinary literature result

The synthesis combines theorem shapes from:

- abstract interpretation: local overapproximation contracts compose;
- robust optimization: certify the universal robust counterpart over a joint
  uncertainty set;
- proof-carrying code: an untrusted producer emits a compact object checked by a
  small consumer;
- validated numerics and formal floating-point analysis: reduce the trusted base
  behind primitive enclosures.

The external literature motivates the architecture.  L-4501--L-4503 contain
the actual elementary proofs used by the repository.

## Candidate-promotion recommendation

Every future candidate should report six independent facts:

1. exact witness frozen;
2. quantitative uncertainty closed with a strict moat;
3. all logical gates proved;
4. all trusted-base components named;
5. exact checker accepted;
6. independent implementation reproduced the decisive object.

A useful staged vocabulary is:

```text
DISCOVERY_ONLY
EXACT_WITNESS_FROZEN
QUANTITATIVELY_ROBUST
LOGICALLY_CLOSED
INDEPENDENTLY_REPRODUCED
Z-CANDIDATE
```

## Failed or deferred approaches

- Treating implementation disagreement as a probabilistic error bar was
  rejected: there is no justified distribution and bugs may be correlated.
- Summing all radii independently was rejected as the only universal method:
  it can erase a witness when exact correlations are available.
- Attempting to put theorem uncertainty into the numerical set was rejected:
  the consequence of a wrong equivalence or normalization is not a bounded
  perturbation of the right score.
- Full formal verification of Arb or special functions was not attempted.  The
  proposal names this residual trusted-base risk rather than claiming it away.

## Potential errors and highest-priority review targets

1. Audit the abstract/concrete DAG quantifiers in L-4501.
2. Check support-function and rational weak-duality signs in L-4502.
3. Re-derive every conjugation and denominator in the Pick contraction L-4503.
4. Attack the manifest semantics: determine whether an operation-graph digest is
   needed before this can govern real candidates.
5. Verify every X-4501 exact fraction and mutation independently.
6. Ensure reports never shorten “all uncertainty admitted by the declared
   semantics” to an absolute claim about unknown human mistakes.

## Files changed

- `claims/definitions/D-4501-uncertainty-closed-witness-semantics.md`
- `claims/lemmas/L-4501-compositional-enclosure-survival.md`
- `claims/lemmas/L-4502-support-function-robust-witness.md`
- `claims/lemmas/L-4503-pick-fixed-vector-uncertainty-compression.md`
- `claims/methodology/M-4501-proof-carrying-witness-survival.md`
- `experiments/X-4501-witness-survival-checker/*`
- `literature/witness-survival-source-ledger.md`
- `integration/gpt56-06-b-45-witness-survival.patch.md`
- this report

## Claims affected

Added D-4501, L-4501--L-4503, M-4501, and X-4501.  No theorem, counterexample,
or `Z-####` candidate is added.

## Recommended next actions

1. Issue #39 should export direct `xi'/xi` outer disks into the X-4501 Pick
   checker and compare compressed versus entrywise widths.
2. PR #43 should contract each fixed derivative/moment localizer to one exact
   jet functional before ball evaluation.
3. PR #44 should express complete-stream, envelope, carrier-shift, pole, and
   archimedean uncertainty as named leaves and compute one robust fixed-vector
   upper endpoint.
4. Arithmetic routes should model shared constants and recurrences jointly
   rather than duplicate independent intervals.
5. A follow-up should define canonical serialization and a digest-bound concrete
   operation DAG for genuine candidates.

## Organizational improvement idea

Create a standing **uncertainty closer** role.  The route researcher proposes a
frozen finalist; the uncertainty closer is forbidden to improve the midpoint and
instead tries to destroy the witness by enlarging every sound uncertainty set,
exposing hidden dependencies, and marking logical gates blocking.  Only the
small exact checker may declare quantitative survival.
