# Focused report — continuum / finite double-root collision (X-8455)

Agent: `cursor-grok-8455`  
Branch: `cursor/continuum-double-root-collision-8455`  
Responds to: review on PR #182  
Status: discovery arithmetic; **not certificates / not RH**

## Claim being tested

The first windowed-Φ deficit-four event is the paired even/odd double-root collision

```text
R_N(α,r)=0,   ∂_r R_N(α,r)=0,
R_N(s)=Σ_{|j|≤N} p_j(α)/(j-s),   p_j=(-1)^j G_α(j),
```

with continuum limit

```text
G_α(r)=0,   ∂_r G_α(r)=0
```

and asymptotics `α_∞ − α_N ∼ C / N³`.

## Results

### Continuum root (D2)

High-dps `mpmath` solve recovers the review values to working precision:

```text
α_∞ = 0.97577952846160346768042134217814...
r_∞ = 2.17949022036079642556231631723481...
```

Residuals at 80 dps: `|G|,|G_r| ≲ 1e-82`.  
Jacobian determinant at the root ≈ `-0.005055` (nonsingular in float/mpmath FD).

### Finite double roots (D3)

| N | α_N (R=R_r=0) | r_N | N³(α_∞−α_N) |
|---|---|---|---|
| 4 | 0.97343859440907386 | 2.1919886581220114 | 0.149820 |
| 6 | 0.97506278881038203 | 2.1833184295906813 | 0.154816 |
| 8 | 0.97546692420226499 | 2.1811593490417205 | 0.160053 |
| 10 | 0.97561547856389962 | 2.1803658792030985 | 0.164050 |
| 12 | 0.97568284257236398 | 2.1800061847198736 | 0.167073 |
| 16 | 0.97573771657215233 | 2.1797132829158123 | 0.171261 |
| 20 | 0.97575777903847116 | 2.1796062320251673 | 0.173995 |

These `α_N` agree with the earlier odd-eigenvalue α_def ladder (C34/C41) to ~1e-12,
so the float soft-mode zero **is** the double-root collision.

### N⁻³ law (D4)

Predicted `C ≈ 0.1866219902712081`. Observed `N³(α_∞−α_N)` rises monotonically
`0.150 → 0.174` for N=4…20 (`ratio/C` → `0.93` at N=20). Consistent with a
slow approach to the linearized constant.

### Exact kernel structure (D1 / D1b)

- `‖Qp‖/‖p‖ ~ 1e-15` and kernel eigenvector aligns with `p` at `1.000000`
  (confirms `Qp=0`, not a mysterious structural mode).
- Just above α_N: one exact kernel (`p`) and two small positive soft eigenvalues.
- Just below α_N: `n_neg=2` — one odd direction with `align(x_odd)≈1` and one
  even direction; matches the paired-collision geometry and `deficit=4`.

### L-15124 recon (D5)

Float root–gamma pairing only. Not a directed ledger. Soft eigenvalue approaches
0 as α↓α_N while a real root sits near `r≈2.18`. Full `δ_k`, `B_kl`, `E_k`
margins remain open (need certified Xi zeros + transform enclosures).

### Larger N (D6)

| N | N³(α_∞−α_N) | ratio / C_pred |
|---|---|---|
| 24 | 0.175911 | 0.9426 |
| 30 | 0.177902 | 0.9533 |
| 40 | 0.179968 | 0.9643 |

Monotone approach toward `C≈0.18662` continues.

### Arb Jacobian (D7)

Using `python-flint` `acb.integral` on truncated Φ (`nmax≤20`) at the discovery
root:

- point residuals `|G|,|G_r| ≲ 10^{-32}` (rad `≲ 10^{-56}`);
- Jacobian determinant
  `det ≈ -0.005055263264366649…` with Arb radius `≲ 10^{-45}`,
  **excludes 0**.

Caveat: Φ-tail bound for `n>nmax` is not yet written into the enclosure; this is
a directed probe, not a finished uniqueness certificate.

## Corrections absorbed from the review

- Parity split and `Qp=0` are exact, not discoveries.
- `p_2=0` is a precursor; the collision is `R=R'=0`.
- Old C22 is not Reading-B evidence (archive branch only).
- Decimal→binary64 pipelines are discovery-grade.

## Proof-facing next step (invited)

Directed / interval Newton on

```text
(R_N(α,r), ∂_r R_N(α,r)) = 0
```

for N=4…20, plus a certified enclosure of `(α_∞,r_∞)` with nonsingular Jacobian,
and inertia/root-count on both sides. That is the compact theorem-quality artifact
requested in the review.

## Files

`experiments/X-8455-continuum-collision/` (D1–D5 + shared helpers)
