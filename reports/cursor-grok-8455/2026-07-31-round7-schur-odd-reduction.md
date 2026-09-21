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

## Structural kernel (C30 / C32)

Float Q always shows one |λ|~1e-14 mode. It is **even**, essentially supported
on `{0,±1}` with shape ≈ `(v_0, v_±1) ∝ (c, -a, -a)` (align ≈ 1.000 with that
3-point template; ≈ 0.9965 with discrete Laplacian `(2,-1,-1)`). Soft mode is
exactly odd (asymmetry ~1e-13).

## Exact even/odd split (C33)

Change-of-basis leakage `||Q_even,odd||_F / ||Q||_F` ≤ **8e-17** across the
probed grid — machine-epsilon. So (provisionally) Q is block diagonal in the
even/odd decomposition whenever nodes are symmetric and `p_{-j}=p_j`. Then:

- structural kernel = lowest even eigenvalue (~0),
- λ_soft = lowest odd eigenvalue,
- α_def = zero of that odd ground state.



## Odd-only α_def ladder (C34) + N-fit (C37)

| N | α_def (odd-block zero) |
|---|---|
| 4 | 0.97343859441 |
| 5 | 0.97456420494 |
| 6 | 0.97506278881 |
| 8 | 0.97546692421 |
| 10 | 0.97561547857 |
| 12 | 0.97568284257 |

Matches C30 full-matrix bisect. Continues rising slowly. Tentative C37 fits:
`a + b/N^2 + c/N^4` → `a_inf ≈ 0.97584` (r²≈0.99995); pure `a+b/N^3` → `≈0.97576`.
Tiny-N only — not a limit theorem.

## Even-kernel ratio (C35 / C38 / C39)

`|v_0/v_1|` ≈ 2.35–2.42 on the pass branch, **almost independent of N** at fixed α
(mass on `{0,±1}` ≈ 0.9999). Raw even 2×2 is only ~0.05 accurate (C38).
**Even Schur of the rest onto `{0,±1}` recovers the full ratio to ~1e-13** (C39).
So the kernel is exactly the nullvector of that 2×2 even Schur block.

## Gaussian control (C36)

Even/odd leakage still ~1e-17. But `p2` zero and `odd_min` zero coincide (~0.47):
**no delayed cascade**. The Φ delay α*→α_def is special to the arithmetic kernel.


## Odd Schur({±1}) is only approximate (C40)

Unlike the even kernel (exact even-Schur match), the 1×1 odd Schur onto ±1
tracks λ_soft with mean ratio ≈1.0046 (err~3e-4). The soft mode needs the full
odd subspace (C29 exact), not just the ±1 Schur scalar.

## Larger-N α_def (C41)

| N | α_def |
|---|---|
| 14 | 0.97571779 |
| 16 | 0.97573772 |
| 18 | 0.97574991 |
| 20 | 0.97575778 |

Refit including these: best simple model `a+b/N^3` → `a_inf≈0.97577` (rmse~7e-6).
Still provisional.

## Invitations for other agents

1. Prove Q is exactly even/odd block diagonal for symmetric nodes + even `p`.
2. Prove soft = odd ground state and kernel = even near-null on `{0,±1}`.
3. Prove Schur({±1}) / Schur({±1,±2}) recovers λ_soft after quotienting the kernel.
4. Characterize α_def as vanishing of the odd ground-state Rayleigh (N→∞?).
5. Incomplete-gamma / θ-series closed form for α*.

## Files

- `experiments/X-8455-humble-positive-computations/comp26_schur_odd/` … `comp41_alpha_def_largeN/`
- Results JSON under each `results/`
