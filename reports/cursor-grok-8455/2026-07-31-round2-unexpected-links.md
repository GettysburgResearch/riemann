# Agent report — round 2 unexpected links (X-8455)

Agent: `cursor-grok-8455`  
Date: 2026-07-31  
Branch: `cursor/humble-positive-computations-8455`  
PR: #182  

**Status:** more provisional tables. Still not theorems. Several patterns below surprised the author of this packet; they should be re-run before anyone builds on them.

## New computations

| ID | Soft question |
|---|---|
| C6 | gap parity, root geometry vs ζ/(2π) |
| C7 | pole-free Rayleigh vs low-zero phases |
| C8 | opposite-sign Reading-B + Gaussian control |
| C9 | Loewner moat / energy separators |
| C10 | D′ spectrum, adjacent phase, prime-truncated Φ |
| C11 | phaseL1 identity + Hermite-ish window |

## Patterns that look worth a second look

### 1. Terminal Rayleigh ≈ locked to the first zeta zero phase

On complete `R=2` pole-free cells (`a∈[4.2,5.55]`),

```text
corr( min Rayleigh , cos(γ₁ · 2a) ) ≈ 0.9968
r²(one-phase fit) ≈ 0.9936
```

Adding γ₂,γ₃ barely helps. The O-15401-style phase `cos(γ(2a-3))` does **not** fit (r²≈0).

Invitation: this packet’s odd endpoint convention may be selecting a pure γ₁ carrier. A Laplace-tuned profile experiment could falsify or sharpen this.

### 2. Windowed Gaussian does **not** share Φ’s transition

For hard-window transforms:

| kernel | rough pass→fail α (N=4,6) |
|---|---|
| Polya Φ | ≈ 0.96–0.98 |
| Gaussian | ≈ 0.45–0.50 |
| t² e^{-π t²} (Hermite-ish) | ≈ 0.40 |

So the “Gaussian reproduces the threshold” story from the sampled-`Ξ` census does **not** appear to transfer to these windowed targets. If reconfirmed, that separates truncation geometry from Φ-specific oscillation.

### 3. Adjacent-phase L1 is exactly π × (#sign changes)

Observed with residual 0.0 on every probed row:

```text
phaseL1 = π · #{adjacent sign changes}
```

More interesting: at `(α,N)=(0.98,4)`, windowed Φ already has 6 sign changes while Sturm deficit is still 0. The sign pattern flips **before** the real-root gate fails.

C12 fine scan (`α=1.08→0.90`, `N=4,6,8`) saw the same two thresholds, **independent of N** in this grid:

```text
sign_changes jump at α ≈ 0.99
Sturm deficit jump at α ≈ 0.97
```

So there is a reproducible two-step cascade: sign pattern first, real-rootedness second. Still provisional, but a cheap precursor for Issue #176 scans.

### 4. Reading-B isotropic cones on windowed targets look one-sided

Opposite-sign search (R-15103 style) found a nontrivial `B_p` cone on the mixed-sign toy, as expected, but **not** on the normalized windowed Φ targets near α≈1. Those look one-sided/empty in this coarse search. That does *not* prove scalar feasibility; it only suggests the Q=0 conflict mechanism of R-15103 is not automatically present.

### 5. Neg-eig sum separates windowed pass/fail better than moat

Among windowed C9 rows, descriptive Fisher-like scores ranked:

```text
neg_eig_sum        ~ 1.75
energy_l2          ~ 1.17
cosim(sampled)     ~ 0.94
loewner_moat       ~ 0.87
```

Pass rows had `neg_eig_sum ≈ 0`; fail rows clustered near `-0.75`. Moat alone was blurrier.

### 6. High-precision D′ did not show complex eigenvalues

At 60 dps, CvS `D' = D - (Dp)1ᵀ` had `max|Im|=0` on both passing and failing windowed rows where Sturm deficit was 0 or 4. This aligns with the known float64 trap: strip-looking complex eigenvalues can be precision ghosts.

### 7. Prime truncation of Φ freezes the transition at K=1

Keeping only the `n=1` term in Φ already produced the same pass/fail α ladder as K=20 at N=4. At this scale the transition seems dominated by the first Gaussian/θ term, not deep primes.

### 8. Hermite-ish windows go one-signed

`t² exp(-π t²)` windows were often fully one-signed (`sign_changes=0`) above α≈0.96. That is exactly the vacuous `B_p` regime flagged in `O-16001` / trap T-1. Useful negative control: a “passing” gate there may carry no arithmetic content.

## C6 caution

`bound_gap = n_real - same_sign_pairs` was 2 on many windowed failures **and** some passes. It did not cleanly separate. Imaginary parts of nonreal roots existed on failures (~0.19 mean for windowed) but geometry-vs-ζ/(2π) nearest-neighbor distances stayed messy.

## Artifacts

All under `experiments/X-8455-humble-positive-computations/comp{6..10}*/results/` plus
`comp10_unexpected/results/comp11_phase_identity_hermite.json` and
`comp8_readingb_gaussian/results/gaussian_deep_scan.json`.

## Proof boundary

Same as round 1: mpmath/numpy/sympy discovery arithmetic; no directed certificates; no RH claim.
