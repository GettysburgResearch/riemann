# X-8455 — Continuum / finite double-root collision (focused)

**Agent:** `cursor-grok-8455`  
**Date:** 2026-07-31  
**Status:** discovery arithmetic toward a compact theorem-quality artifact.  
**Not a certificate. Not an RH claim.**

This packet isolates the strongest mathematical lead from the fat
`humble-positive-computations` reconnaissance (PR #182 review):

```text
first deficit-four event  =  paired even/odd double-root collision
R_N(α,r)=0,  ∂_r R_N(α,r)=0
  → continuum limit
G_α(r)=0,  ∂_r G_α(r)=0
  → (α_∞, r_∞) and an N^{-3} law
```

It deliberately does **not** re-dump the C1–C41 JSON archive.

## Exact structure (review corrections absorbed)

- For symmetric nodes and even `P`, `Q = Q_even ⊕ Q_odd` exactly.
- The ~0 even “structural mode” is the target kernel: `Q p = 0`.
- At the first collision, `P(s)=(s²-r_N²)² H(s)`, with extra kernels
  `x_even,j = p_j/(j²-r_N²)` and `x_odd,j = j p_j/(j²-r_N²)`.
- `p_2=0` is a sign-pattern precursor, not the collision itself.

## Computations

| ID | Directory | Question |
|---|---|---|
| D1 | `comp1_qp0_paired/` | Verify `Qp≈0`; paired even/odd soft modes; collision-vector alignment |
| D2 | `comp2_continuum_GG/` | High-dps solve `G=∂_rG=0` → `(α_∞,r_∞)` |
| D3 | `comp3_finite_RR/` | Solve `R_N=∂_rR_N=0` for N=4…20 |
| D4 | `comp4_N3_law/` | Check `N³(α_∞-α_N)` vs predicted constant |
| D5 | `comp5_root_margin_recon/` | Float L-15124-style root displacement / soft-mode localization |
| D6 | `comp6_largeN_N3/` | Push α_N to N=24,30,40 for the N⁻³ constant |
| D7 | `comp7_arb_continuum_box/` | Arb `acb.integral` residuals + Jacobian excludes 0 |

## Proof boundary

- `mpmath` / NumPy discovery only unless noted.
- Decimal-rationalized coeffs + binary64 eigensolves are **not** certificates.
- Directed interval Newton / Arb enclosures are the next proof-facing step
  (invited, not claimed here).
