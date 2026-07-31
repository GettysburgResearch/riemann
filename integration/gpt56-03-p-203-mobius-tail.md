# Integration handoff — exact local Möbius radical synthesis

Agent: `gpt56-03-p`  
Issue: #203  
Stack: PR #199

## New interfaces

- `L-20301`: exact local inverse of the arithmetic `E`-map on every compact
  multiplicative interval, with both source constraints enforced and an
  explicit lower-tail residual.
- `L-20302`: after a finite simple-line frame, the complete selected-zero
  kernel is an exact graph over the old radical packet and has the same rank.
- `T-20301`: cofinal RH criterion stated directly in terms of the explicit
  Möbius tail and Schur cross.
- `X-20301`: Fraction-only finite regression.

## Composition

```text
PR #192  finite ambient-deficit augmentation
    -> actual complete finite packet
PR #191  finite simple-line frame of its complement
    -> exact graph selected-zero kernel
L-20301  local Möbius inversion
    -> exact global-radical extension of every graph-kernel vector
T-20301  explicit tail LMI
    -> PR #199 corrected-kernel floor
    -> PR #169 full Schur floor
    -> cofinal lower envelope
```

## Exact remaining quantity

For the complete kernel basis `J_j`, choose `N_j a_j>b_j` and form the explicit
lower-tail operator `T_j`. The only remaining positive estimate is

```text
|Q_W(T_j c,T_j c)|
+ ||C_j^(-1/2) Z_j J_j c||^2
<= eta_j ||J_j c||_G^2,
eta_j -> 0,
```

uniformly in the coefficient vector.

## Nonclaim

The contribution closes qualitative capture, kernel dimension, and synthesis
existence. It does not prove the explicit Möbius-tail LMI or RH.
