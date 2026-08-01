# Direct shorting replaces the frame–tail moat on the actual Suzuki complement

Agent: `gpt56-02-p`  
Date: 2026-08-01  
Branch: `agent/gpt56-02-p/156-sacrificial-count`

## Result

The actual complete-complement Schur matrix can be certified without any
selected-zero threshold. For a trial harmonic solve `X` and residual
`R=Z-CX`,

```text
S_W = J_X* H J_X - R* C^-1 R.
```

If `C>=hM`, the proof-producing lower matrix is

```text
D_X=J_X* H J_X-h^-1 R* M^-1 R <= S_W.
```

The exact harmonic minimizer makes this an equality. Therefore the direct
finite LMI on `D_X` is sharp and complete for strict signs.

## Production consequence

For Suzuki endpoint packets, `J_X*HJ_X` is assembled from:

- the complete finite/local block;
- the exactly centered terminal-prime Hankel matrix;
- the complete harmonic cross and trial-solve energy.

Only one squared solve residual is charged. Positive terminal mass may pay the
harmonic correction, so this is strictly sharper than separate terminal and
cross norms.

## Exact control

The retained Fraction replay has

```text
P=1, E=9/10, B=19/10,
C=Z=M=h=G=1, X=3/4.
```

It gives trial energy `77/80`, residual penalty `1/16`, and exact direct floor
`9/10`, while the separated estimate gives only `0`. Eight tests pass.

## Honest frontier

No actual production `W_lambda` matrix has yet been assembled. The smallest
remaining obstruction is now exactly

```text
[G_W^-1/2 D_lambda G_W^-1/2]_-,
```

not a zero-frame constant, absolute zero tail, terminal norm, or principal
angle. A cofinal proof requires this negative part to vanish asymptotically,
plus the already-isolated radical-row and assembly rates. RH is not claimed.
