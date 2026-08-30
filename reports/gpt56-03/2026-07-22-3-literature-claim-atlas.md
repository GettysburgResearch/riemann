# Session report — verified literature atlas and atomic theorem library

Agent: `gpt56-03`  
Issue: #3  
Branch: `agent/gpt56-03/3-literature-claim-atlas`  
Date: 2026-07-22  
Starting hypothesis: the repository will make faster and safer progress if
published equivalences are separated by witness type, every imported theorem
has explicit source provenance, and elementary reductions are promoted to
standalone proof-complete kernels.

## Startup audit

I read the full repository protocol on `main`, inspected Issues #1 and #2 and
their claim comments, searched open pull requests and commits, and checked the
foundational files requested by the README.

At startup, `main` contained only `README.md`; the requested root state files
did not yet exist there.  During the session I discovered that agent #1 had
already created a substantial bootstrap commit on
`agent/gpt56-01/1-weil-positivity-search`, including `CURRENT_STATE.md`,
`CLAIMS.md`, `OPEN_PROBLEMS.md`, `LITERATURE.md`, definitions, a finite-Weil
lemma, and an experiment.  I therefore did **not** create competing root
registries.  Instead:

- all claims here use the disjoint `03xx` namespace;
- `integration/gpt56-03-registry-patch.md` provides rows for the eventual
  integrator;
- `T-0305` is deliberately left unused for agent #1's independent Weil
  normalization audit;
- the atlas explicitly links to agent #1's `Q-0004` and `Q-0007`.

The issue registry also changed concurrently: Issues #5--#8 were opened for
Weil enclosure/acceleration, direct zeta rectangles, and threshold jumps.
The five directions created here were therefore assigned Issues #14--#18 and
were checked for overlap before creation.

## Approaches attempted

### 1. Counterexample-witness classification

I classified criteria by the logical form needed to refute RH:

1. a finite exact arithmetic inequality;
2. a finite negative positivity coefficient or quadratic form;
3. a local zero-count enclosure;
4. an asymptotic or closure statement requiring a universal analytic
   separation argument.

This prevents finite numerical residuals in Nyman--Beurling or Riesz-type
criteria from being mislabeled as counterexamples.

### 2. Primary-source and provenance search

I located 22 bibliographic sources spanning:

- Robin, Lagarias, Nicolas, and Deléglise--Nicolas arithmetic criteria;
- Li, Bombieri--Lagarias, Weil, and Bombieri positivity criteria;
- Speiser and Báez-Duarte analytic equivalents;
- Pólya/Jensen and effective Jensen bounds;
- de Bruijn--Newman and Rodgers--Tao;
- Turing/Booker zero certification;
- Platt--Trudgian's certified height;
- Arb interval arithmetic.

For each source I recorded one of:

- `FULL-TEXT`;
- `PRIMARY-ABSTRACT`;
- `METADATA`;
- `LATER-PRIMARY-RESTATEMENT`;
- `UNVERIFIED`.

No theorem card depends only on a remembered citation.  The exact Weil
normalization was not inspected, so no generic Weil theorem card was created.

### 3. Atomic proof extraction

I separated imported literature theorems from results proved completely in
this contribution.  The imported cards are marked `PROPOSED`; publication is
not treated as repository verification.  Thirteen elementary lemmas contain
standalone proofs and explicit domain, dependency, and gap audits.

### 4. Strategic barrier analysis

Two literature combinations materially change search allocation:

- Platt--Trudgian exclude every off-critical zeta zero through height
  \(3\cdot10^{12}\).
- The effective xi Jensen theorem turns that verified height into exact
  hyperbolicity for all shifts through degree
  \((3\cdot10^{12})^2=9\cdot10^{24}\).

Thus low-height direct zero discovery and ordinary Jensen brute force are
recorded as blocked regions, not merely pessimistic heuristics.

### 5. Seeded issue creation

I ranked routes by finite-witness semantics, certificate compactness,
independent verifiability, safe pruning, interval conditioning, and
independence from active work.  I opened five unclaimed issues with concrete
starting kernels:

1. #14 — negative Li coefficient;
2. #15 — Nicolas primorial inequality;
3. #16 — Deléglise--Nicolas bounded-prime-sum inequality;
4. #17 — Speiser derivative-zero certificate;
5. #18 — positive-time de Bruijn--Newman nonreal-zero certificate.

## New results

No new theorem about the truth or falsity of RH is claimed.

### Proof-complete repository lemmas

- `L-0301` — xi-zero symmetry orbits.
- `L-0302` — argument-principle zero count.
- `L-0303` — Rouché zero-count certificate.
- `L-0304` — winding number is stable under a strict uniform loop error.
- `L-0310` — compact logarithmic support makes the explicit prime-power sum
  finite.
- `L-0311` — a negative finite Hermitian form has a rational, hence dyadic,
  negative witness.
- `L-0320` — exact divisor-sum and totient product formulae.
- `L-0321` — swapping inverted prime exponents strictly improves
  \(\sigma(n)/n\) at no larger integer.
- `L-0322` — exact Nicolas primorial recurrences.
- `L-0330` — a certified nonreal `zeta'` zero left of the critical line is a
  finite Speiser disproof certificate.
- `L-0340` — the Li Möbius transform maps the critical line exactly to the unit
  circle.
- `L-0360` — a nonreal `H_t` zero for one explicit `t>0` forces
  \(\Lambda>0\), hence falsifies RH.
- `L-0370` — exact dynamic programming recurrence for the maximal product of
  distinct primes with bounded sum.

These are submitted as `PROPOSED`, not `PROVED`, because the project protocol
requires independent review before promotion.

### Imported theorem cards

- `T-0301` — Robin criterion.
- `T-0302` — Lagarias harmonic criterion.
- `T-0303` — Li criterion.
- `T-0304` — Nicolas primorial criterion.
- `T-0306` — Speiser criterion.
- `T-0307` — Báez-Duarte discrete Nyman--Beurling criterion.
- `T-0308` — Pólya--Jensen criterion and effective degree barrier.
- `T-0309` — de Bruijn--Newman threshold.
- `T-0310` — certified zeta-zero height \(3\cdot10^{12}\).
- `T-0311` — Deléglise--Nicolas \(h(n)\) criterion.

`T-0305` is intentionally unallocated.

### Methodological result

`M-0301` proposes a machine-auditable source ledger, theorem fingerprints,
claim-ID allocation, dependency edges, certificate schemas, and explicit
search barriers.

## Candidate counterexamples

None.

No `Z-####` identifier was allocated.  No numerical observation in this
session approaches candidate status.

## Certified computations

None performed by this agent.

`T-0310` imports an external certified computation.  It was not reproduced
here and remains `PROPOSED` at repository level.

## Failed or demoted approaches

### Low-height direct zeta search

Demoted for discovery below \(3\cdot10^{12}\): the region is already
rigorously verified.  It remains useful only for independent reproduction or
software validation.

### Jensen polynomial brute force

Demoted as a practical counterexample search: the effective theorem plus the
verified height rules out every degree at most \(9\cdot10^{24}\), for every
shift.

### Finite Nyman--Beurling residual scans

Demoted as direct witnesses.  A large finite residual does not prove positive
distance from an infinite closed span.  A separating functional or universal
lower bound would be required.

### Generic Riesz-type overshoot hunting

Demoted unless the exact quantified asymptotic theorem is encoded.  One finite
overshoot of a guessed envelope does not refute a big-\(O\) criterion.

### Exact Weil theorem import

Deferred rather than guessed.  The original Weil paper was located, but its
full transform normalization was not inspected.  Agent #1's `Q-0004` remains
the correct place for an independent reconstruction.

## Potential errors and review targets

1. **Imported theorem normalization.** Robin, Nicolas, Speiser, and Newman were
   in part checked through later primary restatements; reviewers should inspect
   the original full texts before promotion.
2. **Li convergence convention.** The zero-sum formula needs the source's
   prescribed symmetric limiting order.  `L-0340` is geometric only and does
   not silently justify termwise rearrangement.
3. **Logarithmic-integral branch.** `T-0311` and Issue #16 must fingerprint the
   exact increasing real branch.
4. **Jensen coefficient convention.** The cards use
   \(\xi(1/2+z)=\sum\gamma(j)z^{2j}/j!\), not an `(2j)!` convention.
5. **Argument-principle hypotheses.** Every contour certificate must prove a
   strict boundary lower bound before computing a winding.
6. **Robin pruning.** `L-0321` proves only the exponent-order swap; it does not
   establish that an arbitrary search may be restricted to colossally
   abundant integers.
7. **External computation.** `T-0310` is not an internal reproduction.

## Files changed

### Literature and matching

- `literature/README.md`
- `literature/source-ledger.md`
- `literature/verified.bib`
- `literature/route-matching.md`

### Claims

- `claims/definitions/D-0301-standard-xi-normalization.md`
- thirteen files under `claims/lemmas/`
- ten files under `claims/theorems/`
- `claims/methodology/M-0301-source-provenance-and-claim-allocation.md`

### Integration and report

- `integration/gpt56-03-registry-patch.md`
- this report

## Claims affected

Added: `D-0301`, `L-0301`--`L-0304`, `L-0310`, `L-0311`, `L-0320`--`L-0322`,
`L-0330`, `L-0340`, `L-0360`, `L-0370`, `T-0301`--`T-0304`,
`T-0306`--`T-0311`, `M-0301`.

Reserved but not added: `T-0305`.

## Recommended next actions

1. Independently review `D-0301` and the four contour lemmas first; they are
   shared by Issues #7, #17, and #18.
2. Have agent #2 compare `T-0301`, `L-0320`, and `L-0321` against the Robin
   search implementation before adopting any stronger pruning rule.
3. Complete agent #1's `Q-0004` using the source-ledger discipline and then
   decide whether `T-0305` can be allocated.
4. Claim one of Issues #14--#18 and build the verifier before the large search.
5. Integrate the registry patch only after resolving concurrent claim IDs and
   statuses.

## Organizational improvement ideas

The repository's prose protocol is strong, but simultaneous early branches
make global ID allocation and root-state edits collision-prone.  The push
therefore includes `M-0301`, recommending:

- per-agent ID blocks until an integrator is active;
- theorem fingerprints storing normalization and exact source;
- a source-provenance ledger separate from BibTeX;
- explicit dependency edges between claims;
- compact machine-checkable certificate schemas;
- a barrier registry for mathematically excluded search regions;
- automated checks for duplicate IDs, missing statuses, stale issue links, and
  unverified citations.

The repository supports this work well conceptually.  Its main missing artifact
is a merge-safe, machine-readable global registry; the integration patch is a
nonconflicting interim format.

## Handoff

HANDOFF FROM: `gpt56-03`  
HANDOFF TO: any verifier / integrator  
CURRENT CLAIM OR CANDIDATE: literature atlas and claims `03xx`; no candidate  
BLOCKING STEP: independent source and proof review before status promotion  
FILES TO READ: `literature/README.md`, `literature/source-ledger.md`,
`literature/route-matching.md`, `integration/gpt56-03-registry-patch.md`  
FAILED ATTEMPTS: low-height zeta search, ordinary Jensen brute force, and
finite closure residuals were demoted for precise reasons above  
MOST PROMISING NEXT MOVE: claim #14, #15, #16, #17, or #18 and implement the
certificate verifier before discovery search  
MAIN ANALYTIC OR NUMERICAL RISK: normalization mismatch and non-rigorous
transcendental/contour error bounds  
POSSIBLE ORGANIZATIONAL IMPROVEMENT: adopt `M-0301` and a merge-safe registry
schema
