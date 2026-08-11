# Canonical extraction plan

This pass integrates scientific status and provenance. It does not copy entire research branches or rewrite historical theorem files. The next merge stage should extract only independently reviewed theorem packets.

The scientific-cutoff ledger remains frozen. Exact post-cutoff review resolutions are overlaid by `POST_CUTOFF_CLAIM_RESOLUTIONS.tsv` and `POST_CUTOFF_REFUTATION_EVIDENCE.tsv`.

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

### Packet 2 — Brownian finite algebra and Bohr-instability firewall

Extract together:

- finite beta-gamma/Dirichlet factorization;
- explicit all-`N` numerator;
- reciprocal Hermite identity;
- local-uniform convergence;
- reviewed `N=2,3,4` stability;
- fixed-compact `1/N` expansion with its corrected initial domain;
- `L-90601/R-90601`, proving the current raw all-large/cofinal stability target false;
- `L-90603/L-90604/R-90602`, proving the current logarithmic Nörlund and central-binomial Green finite-real-zero finishes false at the reviewed scope;
- the precise retained alternatives: height-dependent truncation, redesigned producers and a direct infinite canonical system.

Do not retain cofinal half-plane nonvanishing of the current raw producer as an open front-door theorem.

### Packet 3 — corrected one-fiber Brownian / Robin

Extract the corrected one-fiber theorem, the earlier reflected-tail and arbitrary positive-fiber-superposition no-go theorems, and the later Bohr-instability results for the exact current finite mixtures. Preserve individual-fiber self-adjointness while making clear that it does not imply aggregate finite real-rootedness.

The live global Brownian frontier is a direct infinite canonical/Hermite-Biehler construction, a height-dependent construction, or a genuinely redesigned producer outside the reviewed no-go hypotheses.

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

Extract uniform-Pascal Green formula, outer `255/256` positivity, bottom-tail/critical-tail distinction and low-row zero-safe transforms. Do not label full SHARP proved. Incorporate later independently reviewed corrections before promoting recursive critical-hinge claims.

### Packet 6 — endpoint, occupancy and annular flux

Extract exact endpoint Mellin symbol, prime-power moat, factor-64 certificate/minimality scope, positive occupancy, prime-square drift, endpoint/Gamma law and signed score objective. Label every RH-equivalent criterion explicitly. Later factor-64 reduction claims require their own delta review.

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

Attach the exact counterexamples to the false multiplier/inertia and coefficient/operator transfers. Do not extract PR #359 as a theorem composition. Record PIG and the exact integrated adapter as open. Review every later Q4 full proposal and Fourier/Goldbach normal form at its own exact head before promotion.

### Packet 8 — operator/kernel/Fredholm infrastructure

Extract the Schur sign firewall, Xi-cardinal finite-packet capture, confluent-jet normalization and reviewed corrected pole completions. Block corrupted T-90502. Quarantine unreviewed odd-sector, Gaussian-Pontryagin, terminal-heat and fixed-degree-carrier descendants until their specialist review.

### Packet 9 — finite witness programmes

Index exact finite Robin/Nicolas/Li/Pick/Loewner results as semidecisions and feature-space exclusions. No strict negative witness is currently canonical.

### Packet 10 — external Zeta23 provenance

Register upstream paper/note hashes, Lean/Mathlib commits and exact fixed-window theorem scope separately from every local extension.

### Packet 11 — cross-cutting firewalls

Collect generic no-go and scope theorems so future branches can depend on one canonical warning packet rather than rediscovering them. Include the finite-stationary fragmentation no-gap theorem, Q4 scalar/matrix/current firewalls, Schur sign, Brownian mixture/Bohr no-go theorems and external-formalization boundaries.

## Lifecycle actions on headline proposals

| Proposal | Canonical action |
|---|---|
| PR #247 | retain conditional architecture and exact finite spine; supersede frozen BTF hinge |
| PR #292 | mark frozen GFEP theorem refuted by #356; retain first-entrance/Markov identities |
| PR #301 | split false eta/Pascal positive matching from surviving actual-coordinate decoder |
| PR #304 | refute polylog atomic closure; retain commutator and optimized-flow descendants |
| PR #314 | canonicalize exact MCF refutation and preserve Mersenne localization |
| PR #318 | supersede original Brownian formula; canonicalize corrected fiber and early no-go theorems |
| PR #343 | retain finite raw algebra and local convergence; mark the global cofinal stability antecedent false via #376/#388 |
| PR #296 | retain finite Nörlund/Green algebra; mark the current finite-real-zero finishes false via #376/#388 |
| PR #351 | retain WSTS and bootstrap infrastructure; attach #356 refutation edges |
| PR #359 | supersede full composition as false; salvage aggregate negative-inertia lemma |
| PR #362 | record RH-to-PIG only as reviewed; PIG-to-RH remains open pending assembly |
| PR #368 | canonicalize only reviewed snapshot `f6951a6...`; block T-90502 and quarantine later delta |
| PR #373 | quarantine pending first independent review |
| PR #375 | quarantine pending terminal heat/residue review |
| PR #376 | canonicalize only after applying the four non-load-bearing source fixes recorded by PR #388; preserve the review packet and exact source head |

## Review packet preservation

The original review PRs and PR #388 remain immutable evidence deposits. Before closing or deleting their branches, preserve their narrative reports, TSVs and handoffs permanently. The integration front door summarizes them but is not a substitute for the line-by-line reconstruction.

## Suggested merge sequence

1. Merge exact-SHA review resolutions before opening new family extraction packets.
2. Open packet-extraction PRs by family; do not merge research branches wholesale.
3. Run validators against claim IDs, SHAs, overlays and supersession edges.
4. Apply required wording/scope fixes in corrected extracted packets, not by rewriting source history.
5. Freeze a new creation cutoff before any proposal is described as a complete proof.
