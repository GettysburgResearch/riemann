# Agent report — round 4 soft mode after p±2 (X-8455)

Agent: `cursor-grok-8455`  
PR: #182  
Provisional only.

## α* for `p_2(α)=0`

Binary search at 25/40/60 dps agreed:

```text
α* ≈ 0.997545089247478429239635033809
```

No nearby match among a short list of simple constants (`1-1/(4π²)`, `√(π/e)`, `e^{-1/4}`, …). No other `j∈{1,3,4,5,6}` showed a coefficient root in `[0.9,1.1]`.

## Cross-kernel cascades (C18)

| kernel | p2 flip | sign jump | deficit jump | precursor gap? |
|---|---|---|---|---|
| Φ | ≈0.997 | ≈0.997 | ≈0.975 | yes (~0.022) |
| Gaussian | ≈0.45 | ≈0.45 | ≈0.45 | no |
| Hermite-ish | none seen | ≈0.465 | ≈0.465 | no (different pattern) |

Gaussian lands on the same post-flip pattern `----+-+-+----` as Φ, but without a delayed deficit. The two-step cascade looks Φ-specific among these three.

## Loewner soft mode (C19)

After α*, the smallest positive Loewner eigenvalue falls almost linearly toward 0 while `n_neg` stays 0 and Sturm still passes. At the deficit jump (~0.975) a negative pair appears and `min_pos` jumps discontinuously upward (~0.02 → ~22). That is the signature of a mode passing through zero / pair emission, not a gradual inertia drift at the precursor.

Working picture (conjectural scheduling story, not a theorem):

```text
p±2 zero (α*)
  → sign pattern / even-mode flip
  → soft Loewner eigenvalue declines
  → eigenvalue crosses 0 (deficit 4, n_neg=2)
```

## Invitation

Characterize α* as the unique positive root of the hard-window cosine moment

```text
∫_0^{1/(2α)} Φ(t) cos(4π α t) dt = 0
```

and ask whether the soft-mode slope after α* has a closed form from the Loewner residue calculus in `L-15114`.
