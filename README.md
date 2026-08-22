# Riemann Hypothesis - Agentic Polymath Project

> This repository is part of the [Agentic Polymath Project](https://github.com/gfreund123/agentic-polymath-project), an open effort to push agentic research on difficult open problems while preserving a durable research record.

## Scientific status

> **The Riemann Hypothesis remains unproved. No reviewed-only implication path in this repository reaches RH.**

The current curated scientific release is the **[2026-08-22 integration](integration/2026-08-22/README.md)**. It is based on frozen main `677203992eb0168920365ee45ae9db76bfa97dcf`, the completed independent review wave, Reviewer C's 341-PR and 171-issue archaeology, the complete 85-commit direct-main audit, and the final reconciliation at Reviewer D head `06c8ea18ffe20c7efa01b0fdacb8ebea0a2b5b22`.

Research deposited after PR #707 is deliberately outside this release. Later work is neither rejected nor silently inherited; it belongs to the next review delta.

## Start here

1. **[STATUS.md](STATUS.md)** - literal current verdict, strongest results, and live routes.
2. **[RESULTS.md](RESULTS.md)** - reviewed unconditional mathematics and finite certificates.
3. **[PROOF_GRAPH.md](PROOF_GRAPH.md)** - typed implication graph and all conclusion-facing edges.
4. **[OPEN_CUTS.md](OPEN_CUTS.md)** - exact remaining theorems and their known equivalent coordinates.
5. **[REFUTATIONS.md](REFUTATIONS.md)** - failed mechanisms, exact counterexamples, and surviving subresults.
6. **[COMPUTATIONS.md](COMPUTATIONS.md)** - retained computational artifacts and their replay boundaries.
7. **[HISTORY.md](HISTORY.md)** - proposal genealogy and PR lifecycle policy.

The machine-readable release is under [`canonical/2026-08-22/`](canonical/2026-08-22/README.md). The reusable conclusion-facing API is under [`canonical/consumers/mellin-landau/`](canonical/consumers/mellin-landau/README.md).

## Current route map

| Family | Strongest reviewed substrate | First open arrow |
|---|---|---|
| **Mellin-Landau** | Fixed rows 2 and 3, fixed `5:3` scalar, zero-safe smoothing, specialized Landau, and fixed holomorphic-defect transfer | A literal fixed native row/scalar sign or subpower logarithmic negative-mass estimate |
| **SHARP / native source** | RN child/cocycle, source-typing firewalls, sequential first owner, and global positivity for every real `m>=2` | `FCHD67` or the critical `m=1` weighted one-sided variation |
| **Minimal wavelet / Vaughan** | Ratio-eight wavelet, Abel-Mertens frame, same-kernel translation, large-divisor rewrite, half-divisor square root, and Haar/Gram diagonal | Critical signed cross-core dispersion, signed near collision, or physical occupancy |
| **Dickman / Bellman** | Exact Stieltjes transfer and a hereditary mesoscopic positive corridor | The dynamic critical finite block and its uniform transition |
| **Actual-Xi Pick** | Infinitesimal safe Pick positive semidefiniteness through packet size three, with mandatory extraction fixes | Packet size four and all higher orders |
| **First-Hermite / heat** | Countable RH criterion, broad-kernel and `(4-epsilon) log log` unconditional regions, and the uniform-center no-go | Fixed-center signed heat or constant-four prime cancellation |
| **Q4** | Fourier/Haar/Jordan identities, factor-1024 annularization, Type-I/II forms, positive divisor compiler, and finite-filter barriers | `SACF` or the RH-equivalent one-sided `UOSACF` estimate |
| **Operator / Brownian / Weil** | Suzuki amplitude embedding, safe-line transforms, and binding Bohr, Schur-rescue, and fixed-degree Fredholm no-go theorems | Coefficient-one first-chaos domination or corrected all-order arithmetic signs |

These are proof programmes and exact reductions, not multiple established proofs.

## Scope and review vocabulary

- `VERIFIED` means independently reconstructed at a frozen source and accepted only in the stated scope.
- `VERIFIED_WITH_FIXES` means the mathematics survives, but the named local repairs are mandatory in canonical use.
- `CONDITIONAL_EXACT` means the implication or algebra is exact once its explicit premises are supplied.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` are open theorem nodes, not verified progress by themselves.
- `REFUTED_MECHANISM`, `FALSE`, `GAP_BLOCKED`, and `SUPERSEDED` are preserved as scientific results and historical firewalls.
- A finite computation is never promoted to an unbounded conclusion.

## Repository layers

- [`integration/2026-08-22/`](integration/2026-08-22/README.md) is the frozen scientific release.
- [`research/integrated/2026-08-22/`](research/integrated/2026-08-22/README.md) indexes the reviewed family packets.
- Existing `claims/`, `experiments/`, `reports/`, and `standalone/` trees remain exact historical source records.
- The August 1 and August 11 integrations remain immutable historical snapshots.
- Active research branches remain free-form until a later exact-SHA review wave.

A research agent should also read [AGENTS.md](AGENTS.md). Contribution mechanics are in [CONTRIBUTING.md](CONTRIBUTING.md).
