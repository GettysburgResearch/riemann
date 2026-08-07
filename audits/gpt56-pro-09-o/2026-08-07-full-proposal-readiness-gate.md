# Full-proposal readiness gate for the repository-wide RH spine

Date: 2026-08-07  
Agent: `gpt56-pro-09-o`  
Status: **REVIEW-READY AS A GAP/AUDIT PACKET; NOT READY AS A FULL RH PROOF PROPOSAL**

## Frozen live coordinates

- PR #229 parent snapshot: PR #218 at `5fade63daa279fe6003b66f3763ca3bf05fd912d`.
- PR #229 pre-audit head: `3060b12e6b610e4756c8e97795fbdb52978e6f06`.
- Completed Möbius–Farey packet/refutation: PR #231 at `f32aae44411ec1b635b32490f2836efde58e4466`.
- Analytic-totient second-moment route: PR #226 at `2362805cc9bcf1d95f7b8557d36c78f79704fd6a`.
- Replacement high-order Type-II architecture: PR #165 at `13d32ea7a694acf64f5e55b4a41b9b632cd22dd0`.
- Möbius-resolvent terminal proposal: PR #233 at `0211053679e1b5f524a9238093e64d2e7a4128e3`.

Later mutable heads do not inherit this audit automatically.

## Exact decision

PR #229 may be sent now for adversarial review of:

1. the screw/Laplace and Landau reduction;
2. the Selberg–Hankel exponential resolvent;
3. the compact and conditional-Hankel no-go results;
4. the first-cell Mertens decoder;
5. the classification of the true remaining arithmetic obstruction.

It must be described as a **gap-bearing proof spine / research audit**, not as a proposed proof of RH.

A full RH proof proposal may be sent only after a new child PR proves one arithmetic theorem which closes the first-cell mutation and the complete cofinal chain.

## The one unavoidable arithmetic burden

The first positive critical Farey cell is exactly

```text
B_(D,1)
=(i/(2*pi)+1/(2*pi^2))
 [M(D)-M(floor(2D/3))].
```

Therefore any valid completion must imply, without importing an RH-equivalent hypothesis,

```text
M(D)-M(floor(2D/3))
 = O_epsilon(D^(1/2+epsilon))
```

for every `epsilon>0`.

Equivalently, it may prove the completed analytic-totient local moment

```text
integral_(D/2)^D
 |1+S_D(x)+M_D/3+x^2 R_D|^2 dx
 <<_epsilon D^(1+epsilon)(1+B_D),
```

where `B_D<<D`, provided the proof explicitly preserves the Möbius signs, divisor coupling, endpoint channels, and common signed critical-cell contraction.

## Acceptable closure interfaces

A reviewer-ready full proposal may close the burden through exactly one of the following, with a complete proof and explicit cross-route map.

### A. Direct scalar closure

Prove `L-23002` in its completed Möbius-specific form, including all endpoint and adjacent-cell couplings.

### B. Balanced Type-II closure

Prove PR #165's `BTP(K)` on an unbounded order sequence, including:

- actual signed Heath–Brown/Möbius packets;
- same-scale acyclicity and finite complexity elimination;
- strict lower-scale routing;
- all cutoff, first-crossing, and factor-boundary residuals;
- `epsilon_K -> 0`, or `epsilon_K/(1-kappa_K) -> 0`;
- an explicit first-cell mutation proving the fixed-ratio Mertens estimate.

Terminal Euler closure alone is not enough.

### C. Alternative direct Mertens theorem

Prove the fixed-ratio Mertens increment bound directly by a new arithmetic argument. This alone closes the first-cell scalar, but the final packet must still supply the exact map into `T-23001` or the classical Mertens criterion.

## Mandatory promotion gates

A new child PR may be titled a full RH proof proposal only when all gates below pass.

1. **Single frozen dependency graph.** Every imported theorem is identified by exact commit SHA; no mutable-branch references remain.
2. **No open load-bearing theorem.** Every arrow in the claimed proof is accompanied by a proof, not a conjectural estimate, certificate family, or asymptotic schedule.
3. **First-cell mutation.** The proof mechanically recovers the `M(D)-M(2D/3)` square-root bound. Failure is fatal.
4. **Endpoint completeness.** The terms `M_D/3`, `x^2 R_D`, block endpoints, cutoffs, and transition rows are retained and bounded in the same sign-sensitive ledger.
5. **No generic-operator substitution.** The proof does not use the refuted subpower Farey-cluster norm, arbitrary-vector Cauchy–Schwarz, rowwise absolute values, or deletion of finitely many critical rows.
6. **No positive-Hankel shortcut.** The compact stop-loss adjoint and its zero-mass conditional variant are not reused after their negative terminal-atom refutations.
7. **Quantifier audit.** The order of `K`, scale `J`, `epsilon`, packet index, and cofinal limit is explicit and uniform where required.
8. **Normalization audit.** Screw, Selberg, analytic-totient, prime-only Hardy, and Mertens conventions are connected by written equalities with all constants and signs checked.
9. **Independent mutation suite.** At minimum retain the first-cell decoder, the `q=v=5,r=5` gcd-chain mutation, the cotangent-residue mutation, the positive-row `sqrt(D)` operator obstruction, and the negative terminal-atom test.
10. **Final theorem file.** A new theorem states the complete unconditional implication from established lemmas to RH, with no `OPEN`, `ASSUME`, `if BTP`, `if STC`, or `pending cofinal rate` language.

## Recommended packet architecture

Do not relabel PR #229 after a future repair. Preserve it as the gap audit. Open a child PR on its frozen head containing:

1. the proved arithmetic closure theorem;
2. a separate theorem mapping it to the first-cell Mertens bound;
3. the completed unconditional RH theorem;
4. exact dependency and normalization tables;
5. a concise adversarial checklist and mutation suite;
6. a report distinguishing proved mathematics from synthetic finite regression.

## When to send what

- **Now:** send PR #229 for an adversarial review of the reductions, exact algebra, and scope boundaries.
- **Not yet:** do not send it as a full RH proof proposal.
- **Full proposal threshold:** send a new child packet only after one acceptable closure interface above is proved and all ten promotion gates pass.

Current verdict:

```text
conditional proof spine                 COMPLETE FOR REVIEW
first-cell decoder and equivalence      COMPLETE FOR REVIEW
principal generic shortcuts             REFUTED
Möbius-specific critical estimate       OPEN
full RH proof proposal                   NOT READY
RH                                       NOT PROVED
```
