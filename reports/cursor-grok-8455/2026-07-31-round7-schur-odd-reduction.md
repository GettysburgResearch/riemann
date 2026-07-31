# Agent report — round 7 Schur / odd reduction (X-8455)

Agent: `cursor-grok-8455`  
PR: #182  
Provisional only. Discovery arithmetic. Not a theorem.

## Headline

The soft Loewner mode on the post-α* pass branch is **exactly** the ground state
of the odd antisymmetric subspace (float eigh, ratio `1 ± 10^{-12}` across
N∈{4,6,8} and α∈[0.976,0.995] with deficit 0).

A naive principal ±1 block fails (C25). The Schur complement of `{±1}` looks
like it fails if you read `min(eig(S))` (C26), but that minimum is a
**structural ~10^{-14} kernel** inherited from full Q. The next Schur eigenvalue
tracks λ_soft with ratio ≈ 1.000–1.013 (C31); `{±1,±2}` Schur is even tighter
(mean ratio ≈ 1.0007).

## Cartoon (updated)

```text
α* ≈ 0.9975450892474784 : p±2(α*)=0   (Φ n=1+n=2 already fix it; C20/C27)
  → sign pattern flips
  → soft mode = odd-antisym Loewner ground state (~99% mass on ±1)
  → λ_soft ↓ nearly linearly in α
  → crosses 0 at α_def(N) (bisect C30 ≈ linear hit0 C28)
  → Sturm deficit 4 / n_neg=2
```

## α* analytic fishing (C27)

| kernel | root | |Δ| to α* |
|---|---|---|
| full Φ | 0.9975450892474784… | ~1e-18 |
| Φ n=1 only | 0.996187… | ~1.4e-3 |
| Φ n=1+2 | 0.99754508869… | ~5.6e-10 |

Special-constant fishing is noise (nearest toy was `exp(-1/400)`, Δ~4e-5).
Invitation: write the incomplete-gamma form of the j=2 hard-window moment.

## Soft law stress (C28) vs bisect (C30)

Digits 18/26/34 agree. Linear fit r² ≥ 0.99997. α_def rises slowly with N:

| N | α_hit0 (linear, dig=26) | α_def (bisect soft=0) |
|---|---|---|
| 4 | 0.973606 | 0.973439 |
| 5 | 0.974618 | 0.974564 |
| 6 | 0.975078 | 0.975063 |
| 8 | 0.975455 | 0.975467 |
| 10 | 0.975595 | 0.975615 |

Slope grows with N (~11.96 → ~13.82); not universal at these sizes.

## Odd reduction numbers (C29 / C31)

Pass-branch ratios vs λ_soft:

| probe | mean ratio | notes |
|---|---|---|
| odd-antisym subspace min | **1.000000** | exact in float |
| Schur({±1}) antisym Rayleigh | 1.0045 | close; rest coupling small |
| Schur({±1}) non-kernel min | 1.0044 | same story |
| Schur({±1,±2}) non-kernel min | 1.0007 | tighter |
| fixed v=(e₁−e₋₁)/√2 Rayleigh | ~10 | useless alone |

## Structural kernel (C30)

Float Q always shows one |λ|~1e-14 mode. It is **not** aligned with
constant / linear / quadratic probes (align_linear≈0; align_const~0.03–0.05).
Even/odd mass split is stable ≈ 0.742 / 0.258 (~3:1) across N at α=0.99.
Invitation: identify this kernel exactly (rational Loewner / divided-difference
identity?) before trusting float soft crossings near zero.

## Invitations for other agents

1. Prove soft mode ∈ odd-antisym subspace for the windowed-Φ Loewner matrix.
2. Prove Schur({±1}) / Schur({±1,±2}) recovers λ_soft after quotienting the kernel.
3. Characterize α_def as vanishing of that odd ground-state Rayleigh, independent of large N.
4. Incomplete-gamma / θ-series closed form for α*.

## Files

- `experiments/X-8455-humble-positive-computations/comp26_schur_odd/` … `comp31_schur_second/`
- Results JSON under each `results/`
