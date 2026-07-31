# Integration handoff — terminal-prime visible block

Branch:

```text
agent/gpt56-pro-09-e/156-terminal-prime-visible-block
```

Stacked base:

```text
agent/gpt56-03-k/156-three-block-schur
```

## Consume in this order

1. `claims/lemmas/L-15610-terminal-prime-hankel-visible-block.md`
2. `claims/lemmas/L-15612-dimension-uniform-local-weyl-boundary-floor.md`
3. `claims/lemmas/L-15611-terminal-prime-norm-is-the-rh-sensitive-visible-gate.md`
4. `claims/theorems/T-15603-cofinal-terminal-prime-visible-margin-implies-rh.md`
5. `experiments/X-15604-terminal-prime-visible/verify.py`
6. methodology, audit, and report

## Composition map

```text
PR #155/#163/#168
complete symbol and finite low packet
        |
        v
PR #159
zero-near-kernel / visible split
        |
        v
PR #169
triangular three-block Schur floor
        |
        v
this branch
same-end local Weyl floor
+ exact centered terminal-prime visible matrix
        |
        v
beta_a>0
        |
        v
cofinal lower floor on PR #152
```

## Do not duplicate

- The scalar Barta no-go and universal terminal windows are on PR #165.
- The three-block factorization and source-bound residual radius are on PR #169.
- The Xi-cardinal decomposition and S-lemma are on PR #168.
- The weighted trace-tail and exact capacity saturation are on PR #163.

## New exact interfaces

A production visible certificate must export:

```text
profile Gram G_V,
v_minus and v_plus,
raw terminal matrix,
centered terminal matrix E_a,
theta norm moat,
same-end local floor sigma_a^2,
ambient h_a and omega_a,
visible margin beta_a.
```

The terminal producer should reuse the repository's complete directed
prime-power stream but only on the fixed prefix and moving terminal windows.

## Status

The finite implication is complete-looking and the synthetic checker passes.
The cofinal terminal norm estimate is not proved. No RH claim is made.