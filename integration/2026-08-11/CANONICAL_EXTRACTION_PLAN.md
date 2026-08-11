# Canonical extraction plan

This pass integrates scientific status and provenance. It does not copy entire research branches or rewrite historical theorem files. The next merge stage should extract only independently reviewed theorem packets.

## Promotion gates

A claim may enter a canonical theorem packet only when all are present:

1. exact source PR and commit SHA;
2. exact path and claim identifier;
3. complete statement with quantifiers and scope;
4. dependency list pinned to exact SHAs;
5. independent review verdict;
6. all known corrections and refutations attached;
7. computation class and trusted base declared;
8. surviving scope stated without downstream overclaim;
9. no material post-review source drift;
10. a clear first open consumer.

`VERIFIED WITH FIXES` material must be extracted into a corrected standalone packet rather than imported through an unsafe ancestor.

## Proposed packet families

### Packet 1 — finite xi, explicit-formula and matrix foundations

Extract reviewed finite determinant, Gram, inertia, explicit-formula normalization and Schur algebra. Retain early artifact/provenance warnings. Do not promote unauthenticated production zero data.

### Packet 2 — raw Brownian / Dirichlet–Hermite

Extract:

- finite beta-gamma/Dirichlet factorization;
- explicit all-N numerator;
- reciprocal Hermite identity;
- local-uniform convergence;
- reviewed small-N stability.

Front-door open theorem: cofinal half-plane nonvanishing.

### Packet 3 — corrected symmetrized Brownian / Robin

Extract the corrected one-fiber theorem and both exact no-go theorems. Keep aggregate canonical-system closure visibly open.

### Packet 4 — carry, fragmentation and policy Green debt

Extract:

- carry/Pascal identities;
- Möbius divergence;
- balanced fragmentation/Farkas equivalence;
- Markov occupation and policy-drift duality;
- one-pass `4 log 2` lower bound;
- frozen-policy resonance refutation;
- finite-stationary no-gap theorem and escape clauses.

Front-door open theorem: source-specific signed Green debt or equivalent all-generation boundary recurrence.

### Packet 5 — SHARP and low-row sources

Extract uniform-Pascal Green formula, outer `255/256` positivity, bottom-tail/critical-tail distinction and low-row zero-safe transforms. Do not label full SHARP proved.

### Packet 6 — endpoint, occupancy and annular flux

Extract exact endpoint Mellin symbol, prime-power moat, factor-64 certificate/minimality scope, positive occupancy, prime-square drift, endpoint/Gamma law and signed score objective. Label every RH-equivalent criterion explicitly.

### Packet 7 — corrected Q4 source and state infrastructure

Extract only reviewed surviving objects:

- independent-frequency block;
- zero-safe all-pass source;
- physical/carry placement;
- reserve and jet-frame packets at corrected scope;
- source-order repairs;
- two-state Hermitian representation;
- aggregate negative-inertia lemma;
- rowwise recurrence and pole visibility.

Attach the exact counterexamples to the false multiplier/inertia and coefficient/operator transfers. Do not extract PR #359 as a theorem composition. Record PIG and the exact integrated adapter as open.

### Packet 8 — operator/kernel/Fredholm infrastructure

Extract the Schur sign firewall, Xi-cardinal finite-packet capture, confluent-jet normalization and reviewed corrected pole completions. Block corrupted T-90502. Quarantine all post-review deltas.

### Packet 9 — finite witness programmes

Index exact finite Robin/Nicolas/Li/Pick/Loewner results as semidecisions and feature-space exclusions. No strict negative witness is currently canonical.

### Packet 10 — external Zeta23 provenance

Register upstream paper/note hashes, Lean/Mathlib commits and exact fixed-window theorem scope separately from every local extension.

### Packet 11 — cross-cutting firewalls

Collect generic no-go and scope theorems so future branches can depend on one canonical warning packet rather than rediscovering them.

## Lifecycle actions on headline proposals

| Proposal | Canonical action |
|---|---|
| PR #247 | retain conditional architecture and exact finite spine; supersede frozen BTF hinge |
| PR #292 | mark frozen GFEP theorem refuted by #356; retain first-entrance/Markov identities |
| PR #301 | split false eta/Pascal positive matching from surviving actual-coordinate decoder |
| PR #304 | refute polylog atomic closure; retain commutator and optimized-flow descendants |
| PR #314 | canonicalize exact MCF refutation and preserve Mersenne localization |
| PR #318 | supersede original Brownian formula; canonicalize corrected fiber and no-go theorems |
| PR #351 | retain WSTS and bootstrap infrastructure; attach #356 refutation edges |
| PR #359 | supersede full composition as false; salvage aggregate negative-inertia lemma |
| PR #362 | record RH-to-PIG only as reviewed; PIG-to-RH remains open pending assembly |
| PR #368 | canonicalize only reviewed snapshot `f6951a6...`; block T-90502 and quarantine later delta |
| PR #373 | quarantine pending first independent review |

## Review packet preservation

The four review PRs remain immutable evidence deposits. Before closing or deleting their branches, copy their narrative reports, TSVs and handoffs into a future merged audit archive or preserve the branches permanently. This integration PR references them by exact head and must not be treated as a substitute for their detailed proofs.

## Suggested merge sequence

1. Merge this synthesis PR after checking provenance and internal consistency.
2. Open packet-extraction PRs by family; do not merge the review PRs wholesale.
3. Run validators against claim IDs, SHAs and supersession edges.
4. Update root README only after packet paths are resident on main.
5. Freeze a new creation cutoff before any proposal is described as a complete proof.
