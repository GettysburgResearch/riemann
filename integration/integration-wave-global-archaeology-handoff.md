# Global archaeology handoff for the next sole integrator

**Review cutoff:** `2026-08-11T05:37:06Z`  
**Frozen main:** `d6409319b4041cd09bee85f55a344631508f2501`  
**Review branch:** `review/integration-wave-20260811-archaeology`  
**Scope:** review and genealogy only; no theorem packets were integrated and no source branch was modified.

## Executive handoff

The repository should not be integrated PR-by-PR. The live graph contains many coordinate changes and renamed hinges that are mathematically identical. The next canonical state should be organized around canonical objects, theorem packets, and explicit supersession edges.

The archaeology ledger reconstructs **41 major proposal/correction lineages**. No accepted RH proof is present. The principal integration task is to preserve exact finite and structural mathematics while preventing four recurrent errors:

1. treating a failed final arrow as erasing every upstream theorem;
2. treating one exact witness as a class-wide no-go;
3. counting an RH-equivalent criterion as progress on its missing sign;
4. importing scalar, finite, one-frequency, or source-mistyped results at matrix, cofinal, two-frequency, or corrected-source scope.

## 1. Recommended canonical route families

### Family A — finite xi, Pick, Weil, and operator foundations

**Packets:**

- completed-xi normalization and finite transforms;
- finite determinant/Gram/inertia algebra;
- finite Pick/Loewner controls;
- Cayley/Herglotz local sign and current criteria;
- exact Schur-complement identities;
- artifact/provenance firewall.

**Do not combine:** production zero datasets with finite algebra unless source and hash certification are independently closed.

**Frontier:** source-complete cofinal arithmetic floor.

### Family B — Brownian, gamma, Nörlund, Robin, and Hermite

**Packets:**

1. finite Brownian/gamma/Nörlund approximation;
2. corrected one-fiber Robin classification;
3. aggregate mixture firewalls and length moments;
4. raw Dirichlet-average/Hermite factorization;
5. endpoint/carry Gamma probability identities.

**Mandatory supersession:** original cardinal formula → PR #63 correction → PR #318 corrected centered fiber.

**Frontiers:** aggregate canonical system; raw all-N half-plane stability.

### Family C — carry, fragmentation, Pascal, and Cycle Debt

**Packets:**

1. atomized carry rows and Pascal identities;
2. Möbius divergence and Farkas duality;
3. actual-coordinate boundary decoder;
4. optimized boundary/cycle norm;
5. Markov occupation and policy-drift duality;
6. finite-policy no-go and escape classes;
7. conditional prime-ramp consumer.

**Mandatory separation:** frozen binary–ternary policy is REFUTED AS STATED; adaptive, signed, nonstationary, and continuum policies remain live.

**Frontiers:** cycle-optimized all-generation boundary transference; explicit adaptive policy with subpower negative Green debt.

### Family D — SHARP and low-row zero-safe source

**Packets:**

- square-root hinge and average-carry inverse;
- uniform Pascal Green kernel;
- finite outer-band theorems through `255/256`;
- shifted-zeta bottom-tail state;
- continuum critical scalar `Psi`;
- low-row critical-log Volterra transform;
- RH-equivalence firewall.

**Frontier:** finite deeper-band theorem or a genuinely new consumer; do not present all-depth one-sign as a sub-RH lemma.

### Family E — Q4 reflected/Jordan/Hermitian source

**Packets:**

1. compact zero-safe radix-four source;
2. plus/minus all-pass and parity frames;
3. exact physical/carry placement;
4. corrected source-order ledger;
5. vector Jordan curvature and aggregate negative-inertia theorem;
6. two-state reflected/all-pass telescope;
7. PIG filtered-Chebyshev equivalence firewall.

**Mandatory supersessions:**

- scalar source-cone lifts → coupled source matrix;
- PR #346 source formulas → PR #349/#350 corrections;
- local scalar Schur shortcut → vector curvature;
- negative-inertia-to-current inference → PR #357 counterexample;
- PR #359 full composition → PR #362 PIG firewall.

**Frontier:** a new product-block statistic or altered observable, not another trace/determinant/inertia estimate.

### Family F — endpoint, WSTS, annular, and prime-power flux

**Packets:**

1. positive occupancy source and mean-age identity;
2. endpoint Mellin symbol and WSTS consumers;
3. prime-power/prime-square moat;
4. factor-64 annular filter and declared-class minimality;
5. Gamma/Pascal delay/deconvolution;
6. signed endpoint packing objective.

**Canonical object:** one prime–radical flux with several transforms.

**Frontier:** source-specific adaptive packing or martingale coupling with subquadratic signed loss.

### Family G — zeta-23, window architecture, and complete-kernel capture

**Packets:**

1. source-pinned Anthropic theorem and Lean commit;
2. native short-window/conductor claims with independent review status;
3. finite co-lattice/no-alias/coherent-window no-gain theorems;
4. off-line pair spectrum and Gaussian isolation;
5. Xi-cardinal finite-packet capture;
6. confluent jet renormalization;
7. corrected-kernel classifier and RH-equivalence firewall.

**Mandatory separation:** upstream formal theorem, repository analytic extension, finite diagnostics, and arithmetic RH floor must have distinct statuses.

**Frontiers:** growing irregular/prime-resonant moments; order-`O(log T)` jet conditioning; explicit source-complete arithmetic floor.

### Family H — cross-cutting firewalls and no-go theorems

This should be a first-class family, not scattered footnotes.

Include:

- artifact/provenance failures;
- finite/cofinal and scalar/matrix scope corrections;
- one-frequency/two-frequency distinctions;
- convolution-order/source-typing corrections;
- finite stationary atomic no-gap;
- MCF exact no-go;
- scalar Schur and negative-inertia/current no-gos;
- window-bank collapse theorems;
- RH-equivalence firewalls.

## 2. Recommended theorem packet boundaries

Every packet should contain only claims with the same source, scope, and verification status.

### Packet type 1 — exact finite theorem

Required fields:

- statement with finite domain;
- exact dependencies;
- proof or replay source;
- artifact hash if computation is involved;
- explicit non-cofinal disclaimer.

### Packet type 2 — analytic/cofinal theorem

Required fields:

- exact quantifiers and endpoint interpolation;
- source normalization;
- pole/zero cancellation audit;
- all analytic continuation dependencies;
- separation from finite reconnaissance.

### Packet type 3 — correction/refutation

Required fields:

- exact target SHA;
- smallest matching contradiction or class-wide theorem;
- hypothesis match;
- strongest surviving subclaim;
- resurrection category;
- supersession edge.

Never rewrite the historical source file. Add a canonical correction record pointing to it.

### Packet type 4 — conditional consumer

Required fields:

- producer theorem as a named input;
- complete chain to RH;
- whether the input is sub-RH, RH-bearing, or RH-equivalent;
- pole visibility and cancellation checks.

### Packet type 5 — external import

Required fields:

- upstream URL/reference;
- exact source commit or document hash;
- theorem statement exactly as imported;
- formal-build status;
- repository extensions separated by status.

### Packet type 6 — empirical/reconnaissance

Required fields:

- endpoint and precision range;
- whether search was exhaustive in a declared finite class;
- no extrapolation language;
- mutation tests and retained result hash.

## 3. Claim-ledger schema

The next ledger should add the following fields to the existing registry style.

```text
claim_id
canonical_object_id
title
theorem_type
statement
verdict
lifecycle
rh_strength                 # SUB_RH / RH_BEARING / RH_EQUIVALENT
scope_finite_or_cofinal
scope_scalar_or_matrix
scope_one_or_two_frequency
scope_signed_or_positive
source_type
convolution_order
norm_or_metric
introduced_pr
introduced_sha
reviewed_sha
source_branch
dependencies_exact
consumers_exact
correction_of
refuted_by
supersedes
superseded_by
strongest_surviving_subclaim
failure_type
resurrection_category
aliases
artifact_manifest
artifact_hashes
experiment_scope
independent_review_status
notes
```

The `scope_*`, `source_type`, `convolution_order`, and `norm_or_metric` fields are load-bearing. Most major historical failures arose from changing one of these without recording it.

## 4. Supersession relationships that must be canonical

At minimum, create these directed edges:

```text
#44 production claim -> #48/#52 provenance corrections -> artifact quarantine
#55 original Brownian fiber -> #63 -> #318 corrected fiber
fixed-order Abel positivity -> #299 exact witnesses -> #292 all-generation recombination
#247 frozen BTF/GFEP branch -> #292/#351 -> #356 refutation
#301 positive eta/Pascal matching -> #303/#312 corrections -> decoder salvage
#304 terminal atomic closure -> #305/#308/#315/#317
#302 eventual MCF descendant -> #314 exact refutation
#322 radix-five source-free closure -> #323 character firewall
#297 scalar source lift -> #325/#345 vector/Hermitian family
#346 source formulas -> #349 -> #350 corrected source order
#357 inertia state -> #359 full proposal -> #362 PIG equivalence firewall
#348 WSTS front door -> #352 annular endpoint -> #353 positive occupancy state
#358 zeta-23 import -> #360/#363 window no-go -> #364/#365/#366 pair-capture route
#199 kernel classifier -> #365 capture -> #366 confluent scope correction
#214 historical front door -> this integration wave as a new snapshot, not a rewrite
```

## 5. Archive structure

Recommended layout:

```text
research/
  current/
    INDEX.md
    families/
      finite-xi-operator/
      brownian-robin-hermite/
      carry-fragmentation-pascal/
      sharp-lowrow/
      q4-jordan/
      endpoint-prime-flux/
      zeta23-kernel-capture/
      firewalls-no-go/
  packets/
    <canonical-object-id>/
      theorem.md
      dependencies.yaml
      status.yaml
      artifacts.md
  open/
    dormant-questions.md
    rh-equivalent-firewalls.md
  external/
    anthropic-zeta23/
  archive/
    snapshots/
      2026-08-01/
      2026-08-11/
    historical-front-doors/
```

Do not move or rewrite source PR files during the integration. Canonical packets should point to exact immutable source paths and SHAs.

## 6. Front-door structure

The root front door should answer five questions in this order.

1. **Is RH proved here?** No.
2. **What is verified?** Link to finite/sub-RH packets.
3. **What full proposals existed, and what happened to them?** Link to genealogy DAG.
4. **Which mechanism classes are genuinely dead?** Link to no-go registry with scope.
5. **What are the current open hinges?** Separate sub-RH dormant questions from RH-equivalent firewalls.

Suggested top-level table:

| Family | Strongest verified packet | Current open hinge | RH strength | Latest reviewed SHA |
|---|---|---|---|---|

Do not lead with PR count or experiment count. Lead with canonical objects and verdicts.

## 7. Dormant-question roadmap

Import the ranking from `reports/integration-wave/20260811-dormant-questions.md` into four workstreams.

### Workstream 1 — optimized carry policies

- cycle-optimized boundary transference;
- all-generation actual boundary norm;
- explicit nonstationary Green policy;
- adaptive endpoint packing.

### Workstream 2 — aggregate spectral systems

- corrected Brownian aggregate canonical system;
- raw Brownian/Hermite half-plane stability;
- coupled interior Hermitian source matrix.

### Workstream 3 — product-block and matrix information

- Q4 statistic beyond negative inertia;
- high-order confluent moment-Gram;
- explicit finite corrected-kernel hostile tests.

### Workstream 4 — new moment architectures

- growing irregular/prime-resonant Gabor aliases;
- finite low-row SHARP extensions;
- lambda-extremality proof or counterexample.

Each roadmap item should include a binary falsifier and must not be phrased as “prove the missing theorem.”

## 8. Strongest salvageable packets to prioritize

The first canonical integration should prioritize these ten packets:

1. finite xi determinant/Gram/inertia algebra with provenance firewall;
2. corrected Brownian one-fiber Robin classification;
3. exact carry divergence and actual-coordinate boundary decoder;
4. atomic-versus-optimized boundary norm theorem;
5. Markov occupation and policy-drift duality;
6. finite stationary atomic no-gap plus uniform-Pascal escape;
7. corrected Q4 source/frame/vector-curvature packet;
8. endpoint positive occupancy/Gamma/prime-square state;
9. Xi-cardinal cofinal finite-packet capture;
10. confluent finite-cluster jet renormalization.

These are reusable even if every current RH-facing sign remains open.

## 9. Genuinely dead mechanisms to register

Create explicit no-go records for:

- finite stationary fixed-ratio source-independent spectral-gap policies;
- frozen binary–ternary GFEP/producer/BTF;
- exact eventual MCF support menu;
- declared finite-update uniform `C/m` reservoir recurrence;
- finite corrected-Robin reflected-tail domination;
- arbitrary positive superposition closure of good Robin fibers;
- strict complete eta contraction in a norm containing zeta-zero modes;
- zeta-only source-free radix-five closure;
- scalar Q4 Schur shortcut;
- negative-inertia-to-positive-current inference;
- finite co-lattice coherent multiwindow gain;
- finite no-alias multirate gain.

Each record must state the exact theorem and its hypotheses. Do not use a generic `dead` label without scope.

## 10. Heavy artifacts not rerun

The integration should inherit, not regenerate, the review's computation policy. This archaeology pass did not rerun:

- historical zero/prime/interval/spectral/Robin/matrix production;
- factor-64 scans and Bernstein production;
- outer SHARP tail gates;
- large fiber-WHT searches;
- finite-atomic Rouché/interval certificate;
- Anthropic Lean build;
- Gabor/Xi-cardinal and confluent-cluster suites.

Before promotion, the integrator should check manifest existence, byte identity, declared scope, and whether the theorem actually depends on the artifact. Regeneration is a separate review task.

## 11. Immediate decisions required from the integrator

1. Choose canonical object IDs, preferably those proposed in the Rosetta stone.
2. Decide whether open-PR heads are imported as source-pinned packets or first independently reviewed by the assigned mathematical reviewers.
3. Treat PR #356 as the supersession authority for frozen GFEP/BTF and finite stationary policy scope.
4. Treat PR #362 as the Q4 RH-equivalence firewall.
5. Treat PR #318 as the Brownian cardinal-fiber authority.
6. Keep PR #214 immutable as a historical front door.
7. Build a new exact-SHA snapshot rather than advancing `main`'s old index incrementally.
8. Require every imported external theorem to state formal-build status separately from source pinning.

## 12. Final integration recommendation

The canonical repository should have three visible layers:

```text
Layer 1: VERIFIED / VERIFIED WITH FIXES theorem packets
Layer 2: correction, refutation, and no-go DAGs
Layer 3: open hinges split into sub-RH dormant questions and RH-equivalent firewalls
```

A proposal should never be globally discarded because its terminal theorem failed. A refutation should never be globalized beyond its hypotheses. A criterion should never be promoted merely because it is compact.

This handoff performs no integration and changes no mathematical source branch. It supplies the structure needed for the sole integrator to build a new canonical state after the parallel mathematical reviews arrive.
