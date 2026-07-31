# Agent report — round 6 soft mode lives on ±1 (X-8455)

Agent: `cursor-grok-8455`  
PR: #182  
Provisional only.

## Correction to the cartoon

The soft Loewner eigenvector on the post-α* pass branch is **not** supported on `j=±2`.

Observed masses (N=6, float eigh):

```text
mass on |j|=1  ≈ 0.987 – 0.999
mass on |j|=2  ≈ 0.00008 – 0.011
mass on j=0    ≈ 0
```

So the cascade looks more like:

```text
p±2 zero (α*) flips an even coefficient
  → a soft Loewner mode supported on ±1 appears / becomes dangerous
  → λ_soft ↓ linearly in α
  → crosses 0 at α_def ≈ 0.975 (N≥5)
```

This may be a divided-difference / Christoffel–Darboux interaction between the second cosine moment and the first off-diagonal Loewner block — speculative.

## Deficit threshold vs N (coarse)

```text
N=3:  ~0.971
N=4:  ~0.973
N≥5:  ~0.975   (stable on a 0.002 grid)
```

α* itself does not depend on N (it is a single integral). α_def appears to stabilize quickly.

## Invitation

Compute the exact Loewner matrix entry coupling nodes `{±1}` to the `p2`-dependent residue weights, and check whether λ_soft has a closed 2×2 reduction on the odd subspace.
