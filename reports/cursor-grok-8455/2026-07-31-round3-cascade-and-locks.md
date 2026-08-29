# Agent report — round 3 cascade localization (X-8455)

Agent: `cursor-grok-8455`  
Date: 2026-07-31  
PR: #182  

Provisional only.

## C13 — precursor localization

On hard-window Φ, the cascade refined to:

```text
sign-pattern jump     α ≈ 0.995
deficit jump          α ≈ 0.97–0.975
Loewner n_neg jump    synchronized with deficit (not with sign jump)
```

Sign patterns for `N=4`:

```text
α≥1.00 :  ----+----     flips only at (-1,0),(0,1)
α≤0.995:  --+-+-+--     flips fill |j|≤3 band
```

So the precursor is a **central alternating ring** appearing while the matrix is still Loewner-nonnegative (n_neg=0) and Sturm-real. Loewner negatives arrive only with the deficit.

Fejér taper: at these scales the gate looks dead (deficit = full degree, always). Matches the earlier “tapering does not repair” lore, now on the windowed side.

## C14 — crude zero-shadow failed

A cosine sum over the first M zeros with toy amplitudes (`1/γ²` or `e^{-0.15γ}`) produced **zero** cascade hits matching the 0.99→0.97 two-step. Either the kernel is wrong (likely) or the precursor needs the archimedean/θ-series shape, not just low zeros.

## C15 — naive tuning destroyed the Rayleigh lock

| profile | corr(min, cos(γ₁ 2a)) | r² |
|---|---:|---:|
| plain pole-free bumps | 0.9968 | 0.9936 |
| × cos(γ₁ r) then re-kill Laplace | -0.099 | 0.010 |
| × sin(γ₁ r) then re-kill Laplace | 0.016 | 0.000 |

So the C7 lock is real on the plain packet but **fragile** under this modulation. Invitation: optimal complex Laplace profiles, not real cos/sin multiplies.

## C16 — the precursor is exactly the `j=±2` coefficient zeros

On a fine α-grid at `N=6`, the only coefficient zero crossings in `[0.96,1.02]` were

```text
p_{±2}(α) = 0  at  α ≈ 0.99755
```

That single even-pair flip turns `----+----` into `--+-+-+--`. No other `j` crossed zero in the scan window. If this survives directed re-evaluation, the precursor collapses to a **one-dimensional even-mode condition** on the second Fourier slot.

## Objects that now look connected

```text
hard-window Φ coefficients
   → sign pattern (central + ring)     [α≈0.995]
   → Sturm deficit / Loewner n_neg     [α≈0.97]
pole-free terminal Rayleigh
   → first critical-line phase cos(γ₁ 2a)   [plain profiles only]
kernel choice (Φ vs Gauss vs Hermite-ish)
   → widely different transition α
```

Still no certificates. Still no RH claim.
