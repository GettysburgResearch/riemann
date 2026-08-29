# Agent report — round 5 linear soft mode (X-8455)

Agent: `cursor-grok-8455`  
PR: #182  
Provisional only.

## C20 — α* is a two-prime event

| K (Φ terms) | α*(p2=0) |
|---|---|
| 1 | 0.9961872290180905764600538532 |
| 2 | 0.997545088688992152015089232 |
| ≥3 / full | 0.997545089247478315996886522 |

So the precursor is essentially determined by the first two θ-series terms; K=1 is close but visibly short.

## C21 — soft mode is almost perfectly linear

On the post-α* pass segment from C19:

```text
min_pos ≈ -12.923 + 13.254 · α
r² ≈ 0.999965
extrapolated zero at α ≈ 0.97505
```

That extrapolated zero agrees with the observed deficit jump (~0.975) to about `5e-5`. Fit vs `p2` is similarly tight (r²≈0.99987).

Invitation: prove a first-order Loewner perturbation formula

```text
λ_min(α) = c · (α - α_def) + O((α-α_def)^2)
```

with `α_def` identified from the hard-window moment hierarchy.

## C22 — Reading-B cone mostly one-sided along the cascade

Opposite-sign probes stayed `has_neg`-only on almost every α, including after the deficit jump. One isolated `nontrivial=True` at α=0.9975 (p2≈0) looks like a conditioning artifact (1 pos / 1 neg in 250 trials). This does **not** support “Reading B opens at the precursor.”

## Updated cascade cartoon

```text
K=1,2 of Φ fix α* ≈ 0.9975450892474783 where p±2 = 0
        ↓
sign pattern flips; Loewner still PSD
        ↓
λ_min decreases linearly in α
        ↓
λ_min hits 0 at α ≈ 0.975 → deficit 4 / n_neg=2
```
