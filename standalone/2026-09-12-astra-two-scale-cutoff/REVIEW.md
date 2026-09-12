# HBR29 review and publication handoff

**Not an RH proof.** Review the component arguments, not an omitted closing lemma.

## Highest-priority mathematical checks

1. **PROOF (13)–(16):** verify the Mellin normalization, both delayed terms in the exact cutoff density, the small-r Wasserstein patch, and the complete positive-r envelope. Equation (16) is absolute after normalization, NOT relative at all heights.
2. **PROOF (17)–(24):** check the quantile error and both tail probabilities; the native cutoff density's L1 limit; uniformity over `0<=sigma<=1, |tau|<=K ell`; and the full-axis integrable majorant in the sharp correction. Recheck every factor two in the gamma profiles. The sharp little-o has no effective rate.
3. **PROOF (22), (27):** the zero-free windows concern the MODE FUNCTIONS ONLY. Check the forced s=0 zero, the neutral shared-zero identity, the conjugation sign, and the fixed-segment phase winding. This rules out sufficiently high individual companions, not all signed combinations.
4. **PROOF (29)–(32):** compare the finite polynomial with the specialized Meixner–Pollaczek generating function and the exact Jacobi matrix. Classical orthogonal-polynomial Xi programmes are credited; no Xi characteristic spectrum is constructed here.
5. **Full ending:** stable source response, positive cutoff laws and convergence to a gamma profile do not prove critical-line confinement of Xi. A descent would need to preserve exclusion of OFF-critical zeros while permitting central zeros. The #876 homotopy sign is still open and is not inferred from mode index asymptotics.

## Computation review

`check.py` uses the standard library, integers and Fractions. The 1,605 tests reconstruct bounded source moments, delayed and Pareto recurrences, survival jets, sharp constants, phase conjugation signs, three independent finite polynomial representations, and exact rational tridiagonal determinants. They are finite controls, not proofs of the infinite asymptotics.

The eight actual CLI refusals include resealed false scope/result data, duplicate/type aliases, and a resealed DELAY_DEN=3 primitive. Mutation detection is not merely a stale hash. Normal and optimized execution share the backend. The diagnostic JSON is floating exploration with explicit omitted errors and is not a numerical theorem.

No predecessor certificate campaign, actual Xi zero evaluation, full repository checkout validator, Lean build, remote CI or independent-author acceptance was run by this author session.

## Publication contract

Intended parent: `45281093179434e08d28d8e589a8c70d70ead5b9` (PR #872).
Suggested branch: `research/astra/20260912-two-scale-brownian-cutoff`.
New path: `standalone/2026-09-12-astra-two-scale-cutoff/`.
Changes: eleven additions; no predecessor or canonical-status edits.

Apply the supplied add-only patch on the exact intended parent, reproduce the documented commands, open a draft PR, and append a separately verified head/URL receipt. This text does not authorize a main merge or claim that author publication succeeded.

The minimal local Git roundtrip preserves a frozen predecessor proof and an unrelated sentinel. It authenticates delivery bytes only and is NOT a complete Riemann checkout. See the outer delivery receipt for its actual local object IDs and commands.
