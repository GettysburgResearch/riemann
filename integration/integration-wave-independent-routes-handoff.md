# Integration-wave handoff: independent Riemann routes

**Cutoff:** `2026-08-11T14:03:15Z`  
**Base:** `main@d6409319b4041cd09bee85f55a344631508f2501`  
**Review branch:** `review/integration-wave-20260811-independent-routes`  
**Detailed report:** `reports/integration-wave/20260811-independent-routes-review.md`  
**Status table:** `audits/integration-wave/20260811-independent-routes-status.tsv`  
**External provenance:** `literature/integration-wave/20260811-external-provenance.tsv`

## Integration posture

RH remains unresolved. Integrate exact finite theorems, exact refutations, provenance locks, and route infrastructure while preserving every cofinal or RH-equivalent endpoint as open.

## Immediate blockers

### 1. False two-by-two defect formula

PR #357 at `a2843d31649822014219a13ec29c70e4a30932cc` contains a false universal statement in `L-90301.8`. For `K=-I_2`, the displayed radical formula returns `1`, while `tr(K_-)=2`.

The adjacent trace/curvature inequalities in `L-90301.6-.7` remain correct and may be integrated separately.

Required repair:

- if `lambda_+<=0`, use `delta(K)=-tr K`;
- if `lambda_-<0<lambda_+`, use the radical expression;
- if `lambda_->=0`, use `delta(K)=0`.

### 2. Corrupted theorem artifact

PR #368 at `0de8f97f37617c050534c242ee3761af15b87a97` contains invalid UTF-8/binary corruption in

`claims/theorems/T-90502-pole-null-fredholm-heat-rh-equivalence.md`.

Blob: `f5bbc2392327b965a278917076c470f7eb15f359`.

Do not integrate this file. Recreate it from a clean UTF-8 source after reconciling it with `L-90505`, `L-90506`, `L-90507`, and `POLE_NULL_LEVY_HEAT_COMPLETION.md`.

## Route handoff

### Raw Brownian/direct-xi

Integrate:

- finite gamma/Laplace/Mellin factorization;
- strip error and local-uniform convergence to xi;
- exact Dirichlet-average factorization;
- explicit all-`N` exponential numerator;
- reciprocal Hermite interpolation;
- exact `N=2,3,4` half-plane stability;
- adverse-shift and explicit minimum/Laplace normal forms.

Keep open:

`E[Q_N^z] != 0` for `Re z>1/4` for all large `N` or a cofinal sequence.

This route is genuinely independent of carry/Q4 and genuinely avoids the symmetrized positive-mixture obstruction.

### Symmetrized Brownian/Robin

Integrate:

- corrected one-fiber determinant and self-adjointness;
- reflected-tail no-go;
- positive-mixture counterexample.

Do not retain as live mechanisms:

- finite reflected-tail domination;
- positive-fiber-mixture real-rootedness.

Keep open only the aggregate canonical-system/de Branges construction.

### Weil/screw/carrier/operator

Integrate exact finite algebra with explicit type labels:

- carrier fixed-vector results: `FINITE SEMIDECISION`;
- screw convexity/minimization: `ROUTE INFRASTRUCTURE`;
- localized bottoms: conditional on completeness;
- finite packet repair and complement augmentation: finite infrastructure;
- Schur identity: exact theorem;
- corrected-kernel floor: `RH-EQUIVALENT CRITERION`;
- square-screw principal coordinate: exact theorem;
- Suzuki/localizer results: shifted/unshifted guardrail.

Preserve prominently:

`B-Z* C^{-1} Z <= B`.

A positive complement cannot repair a negative kernel direction.

### Finite Robin/Nicolas/Li/Pick/Loewner

Integrate only with finite scope.

- Robin #24 is an authenticated finite barrier.
- Robin #34 needs a retained-stream provenance caveat.
- Robin #53 remains unverified until its complete terminal stream is supplied.
- Nicolas `L-3107` is checkpoint infrastructure, not a global theorem.
- Li scans are empirical; a negative quartet contribution is not a negative total coefficient.
- Pick/Loewner exact tables close declared finite feature spaces only.
- No strict negative Riemann-data witness exists at the reviewed SHAs.

### Anthropic Zeta23

Preferred import boundary: PR #361 at `c13b8836f6c7f4e36f17ab1c4ebe41e4cf072f2e`.

Upstream pins:

- paper SHA-256 `6792988e6cd0e17690621ce898abd5d534f98407741bc7cb14bbe7d07c77d72f`;
- concise note SHA-256 `45e0330ad37965e5531fa1f4f11e5bebcae147a5237a3e5b3d029efa7ddf759d`;
- Lean repository `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`;
- Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`.

Import as upstream verified only:

- headline Theorems A-E;
- fixed dyadic/cumulative windows;
- each fixed primitive Dirichlet character.

Keep local/unformalized:

- short-window and growing-conductor theorem;
- co-lattice/multirate/alias extensions;
- prime-resonant banks;
- off-line-pair isolation;
- Xi-cardinal capture;
- confluent clusters;
- Gaussian terminal scalar;
- pole-null Fredholm/heat route;
- all Q4 transfer.

PR #364 moved from `219330bd0441a284fd16ff728dd843a7ee4503ee` to `46caa771ad2ab7875c3ccd079d3ba327249fd9a4` and was re-reviewed at the latter.

## First open theorem queue

1. Raw Brownian all-`N`/cofinal minimum phase.
2. Aggregate canonical system for symmetrized Brownian approximants.
3. Cofinal carrier/screw/localized capture with complete tails.
4. Fully Schur-corrected kernel floor tending to zero.
5. Gaussian-Chebyshev terminal scalar sign.
6. Pole-null heat-trace nonpositivity for every positive heat parameter.
7. Short-window/growing-conductor Zeta23 uniform analytic theorem.
8. Growing prime-resonant bank including all cross-alias terms.
9. Cofinal finite-feature completeness or a strict negative Pick/Loewner witness.
10. Repair `L-90301.8` before any Q4 reuse.

## Heavy work not rerun

No large Brownian scan, carrier replay, Nyström/Fredholm sweep, Lean build, interval campaign, large matrix/feature search, or prime-bank search was rerun. Retained source, proofs, manifests, hashes, certificates, and audit files were inspected.

## Explicit RH status

No reviewed branch establishes RH or its negation. The strongest complete theorem in scope is the imported Zeta23 zero-proportion theorem, which explicitly remains below RH. The strongest local proposals terminate at open all-`N`, corrected-floor, terminal-scalar, or heat-sign statements that are RH-bearing or RH-equivalent.
