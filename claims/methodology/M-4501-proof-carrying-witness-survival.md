# M-4501 — Proof-carrying witness survival and uncertainty closure

Proposal ID: M-4501  
Status: PROPOSED  
Authoring agent: `gpt56-06-b`  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-4501, L-4501, L-4502; route-specific certificate lemmas  
Scope: project-wide candidate promotion

## Problem with the current process

The project has strong local defenses against false witnesses, but they are
spread across routes:

- fixed-vector rationalization;
- entry or special-function balls;
- omitted-prime and analytic tails;
- contour tubes and winding stability;
- exact branch-and-bound coverage;
- independent arithmetic backends;
- source and normalization audits.

A candidate can still be promoted inconsistently because “remaining
uncertainty” is not one mathematical object.  Three qualitatively different
things are mixed together.

1. **Logical uncertainty.**  Is the theorem, normalization, domain, or finite
   reduction actually correct?
2. **Quantitative uncertainty.**  How far can the exact decisive quantity move
   under all admitted numerical, truncation, discretization, and parameter
   errors?
3. **Epistemic implementation risk.**  Is the producer, checker, compiler,
   library, or source transcription wrong?

Only the second category can be defeated by a numerical moat.  The first must
be proved.  The third must be reduced by proof-carrying computation, a small
trusted base, independent reconstruction, and where practical formal
verification.

## Proposed change

Every future `Z-####` candidate should include a **witness-survival assurance
case** with three layers.

## Layer A — Hard logical gates

The candidate lists every theorem-level obligation and its evidence locator.
At minimum audit:

1. exact RH implication or equivalence direction;
2. all quantifiers, thresholds, exceptional cases, and strict inequalities;
3. normalization and sign conventions;
4. analytic or meromorphic domain;
5. poles, trivial zeros, branches, and contour exclusions;
6. admissibility of the finite test object;
7. completeness of finite enumeration or the exact point at which a proved tail
   bound begins;
8. exact semantics of the witness bytes.

A gate is either `PROVED`, `INDEPENDENTLY_VERIFIED`, or `BLOCKING`.  No amount of
numerical margin can change `BLOCKING` to accepted.

## Layer B — Quantitative robust counterpart

Freeze the witness before proof-grade evaluation.  Define the exact decisive
score or invariant and expose every quantitative primitive as a leaf in a
finite evaluation DAG.

Preferred proof order:

1. **contract before enclose** — reduce matrices, sums, and repeated symbols to
   the final fixed-vector or scalar functional;
2. preserve known correlations in a joint uncertainty set;
3. choose the sharpest auditable abstract domain:
   - intervals or disks for isolated primitives;
   - affine forms or polytopes for shared linear dependence;
   - Taylor models plus explicit remainders for nonlinear parameter cells;
   - exact finite sets for enumerations;
   - operator envelopes for omitted blocks;
   - topological tubes for winding invariants;
4. compute or upper-bound the adversarial robust counterpart;
5. require a strict moat from the failure boundary;
6. make a small exact checker reconstruct the final comparison.

For a scalar-negative witness, the acceptance condition is

\[
 \sup_{u\in\mathcal U}q(w,u)<0.
\]

For a fixed-vector matrix witness, first contract to a scalar.  For a contour
witness, the analogous condition is that the entire uncertain loop remains a
strict positive distance from zero while preserving the target winding.  For
interval Newton or Krawczyk, the moat is the strict self-map/contraction and
boundary-separation margin.  For exact combinatorial optimization, the moat is
the certified objective gap plus complete coverage of every competing branch.

## Layer C — Trusted-base reduction

The searcher is never trusted.  It emits exact witness data and a certificate.
The verifier should:

- share no discovery eigensolver or optimization traversal;
- use exact integers/rationals for the final algebra;
- reconstruct rather than trust claimed totals;
- fail closed on malformed, missing, duplicated, or unused channels;
- be small enough for line-by-line audit;
- carry deterministic digests and environment fingerprints.

For a decisive witness, require an independent analytic reconstruction and a
second implementation or library.  When feasible, use a theorem-prover-checked
interval library, Gappa/Flocq-style floating-point proof, or a formally verified
compiler to shrink the trusted base.

Independent agreement is a promotion requirement, but it must not be described
as a proof that correlated bugs are impossible.

## Uncertainty-closure ledger

Every candidate should contain one record for every possible witness-destruction
channel.

```text
id:
kind: LOGICAL_GATE | QUANTITATIVE_CHANNEL | TRUSTED_BASE
state:
source_or_formula:
where_used:
enclosure_or_evidence:
independence_fingerprint:
blocking_reason:
```

Allowed quantitative states:

```text
ELIMINATED_EXACTLY
ENCLOSED
EXHAUSTIVELY_ENUMERATED
TAIL_BOUNDED
```

Workflow/assurance states:

```text
INDEPENDENTLY_RECONSTRUCTED
BLOCKING
```

The certificate checker verifies that the set of declared quantitative IDs is
exactly the set used by the evaluation DAG.  A declared-but-unused channel is
rejected because it may be decorative.  A used-but-undeclared channel is
rejected because it is hidden uncertainty.

## Candidate promotion ladder

Use the following statuses in reports even before a global schema is adopted.

1. `DISCOVERY_ONLY` — floating candidate or model anomaly.
2. `EXACT_WITNESS_FROZEN` — all candidate inputs are exact.
3. `QUANTITATIVELY_ROBUST` — exact checker proves a strict moat over the declared
   uncertainty set.
4. `LOGICALLY_CLOSED` — every theorem, normalization, domain, and completeness
   gate is proved.
5. `INDEPENDENTLY_REPRODUCED` — an independent implementation reconstructs the
   decisive certificate.
6. `Z-CANDIDATE` — project candidate requirements are met and adversarial review
   begins.

No stage may be inferred from confidence, precision, runtime, or agreement of
uncertified midpoints.

## Route map

### Finite Weil and carrier-Weil

- Freeze exact `c`, carriers, basis, and dyadic vector.
- Use `L-3101` for vector rationalization.
- Use complete prime enumeration or `L-3102`-style omitted-block envelopes.
- Contract source blocks against the fixed vector before ball evaluation.
- Enclose pole and archimedean pieces independently.
- Apply a support-function robust counterpart when source errors share phase or
  primitive evaluations.
- Keep the Guinand--Weil normalization as a hard gate.

### `xi'/xi` scalar, Pick, and Stieltjes routes

- Exact dyadic sample points and fixed vectors.
- Prove every denominator excludes zero.
- Contract Pick matrices using `L-4503`.
- Contract derivative/moment localizers to exact jet coefficients before
  enclosing the jet.
- Treat fitted rational or passivity models as proposal engines only.

### Robin, Nicolas, Li, and bounded-prime-sum routes

- Exact integer/factorization/index witness.
- Exact combinatorial optimum or complete search certificate.
- Directed transcendental leaves.
- Preserve shared constants and recurrence correlations rather than repeatedly
  widening independent copies.
- Keep the imported equivalence theorem as a hard gate.

### Direct zeta, Speiser, and de Bruijn--Newman contours

- Exact rational contour.
- Sound function and derivative enclosures on every segment.
- A strict tube-to-zero moat and exact polygon winding.
- Domain and singularity exclusions as hard gates.
- Independent evaluator reproduction for any positive off-line count.

## Proof-carrying checker principle

The producer may be arbitrarily sophisticated and untrusted.  Its output is
accepted only when a small checker verifies a policy:

```text
all declared quantitative channels are present exactly once
all local algebraic proof obligations hold
all support/dual/remainder inequalities hold exactly
root robust set lies strictly inside the witness region
no logical gate is marked BLOCKING
```

The checker does not infer that a cited theorem is true merely from a string in
a manifest.  It enforces closure and arithmetic; theorem review or formal proof
supplies the gate evidence.

## Expected benefit

- A common candidate language across analytic, matrix, arithmetic, and
  topological routes.
- No silent promotion of a midpoint or preferred implementation.
- Better margins through correlation-aware robust optimization.
- Smaller final proof objects because exact fixed-vector contraction precedes
  interval evaluation.
- Clear separation between what is mathematically proved and what remains in
  the trusted base.
- Mutation tests that target omitted uncertainty rather than only arithmetic
  bugs.

## Possible cost or risk

- Building the concrete semantics and full leaf ledger requires discipline.
- Joint uncertainty models can be harder to export than independent intervals.
- A sound but overly coarse abstract domain may fail to certify a real witness.
- Formal verification of special functions is expensive; independent Arb/MPFI
  reproduction may remain the practical intermediate standard.
- The phrase “all uncertainty” can invite overclaiming.  Every report must say
  “all uncertainty admitted by the explicit certificate semantics” unless the
  entire trusted base has been formalized.

## Trial procedure

Apply M-4501 to three controls.

1. X-4501 synthetic affine box: verify a strict surviving moat and reject a
   zero-touching enlargement.
2. X-4501 correlated polytope: certify a negative robust bound that an
   independent box cannot retain.
3. X-4501 Pick disks: prove exact contraction identity, survive small disks, and
   reject enlarged disks.

Then hand the schema to:

- Issue #39 for Arb Pick certificates;
- draft PR #43 for derivative-jet localizers;
- PR #44 for the low carrier basin;
- canonical Robin and Nicolas/Li certificate producers.

## Success criterion

The proposal succeeds when a future candidate report can answer, with exact
file paths and proof objects:

1. What exact object is the witness?
2. What exact theorem turns it into `not RH`?
3. Through which complete list of leaves can its decisive value vary?
4. What joint uncertainty set contains every admitted realization?
5. What exact robust upper bound or invariant tube is verified?
6. What is the strict moat?
7. Which components remain in the trusted computing base?
8. Which independent implementation reproduced the result?

A witness that answers all eight cannot disappear under any uncertainty inside
its declared mathematical semantics.  Anything outside that semantics is made
visible as a blocking gate or trusted-base item rather than hidden beneath a
numerical margin.
