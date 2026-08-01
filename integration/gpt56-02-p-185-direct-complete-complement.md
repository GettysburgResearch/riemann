# Integration handoff — direct production `W_lambda` Schur certificate

The frame–tail scalar is no longer the preferred production interface.

For the actual complete harmonic complement

```text
W_lambda=R_lambda^(perp_GC) intersect U_lambda,
```

build one trial harmonic solve `X_lambda` and residual

```text
R_lambda=Z_(W,lambda)-C_lambda X_lambda.
```

The proof-facing lower matrix is

```text
D_lambda
 =J_X* H_lambda J_X
  -h_lambda^-1 R_lambda* M_lambda^-1 R_lambda.
```

A directed LMI

```text
D_lambda >= m_lambda G_(W,lambda)
```

proves the **actual** Schur-corrected `W_lambda` block positive. For the endpoint
packet, assemble `J_X*H J_X` with the complete centered terminal-prime matrix,
all finite/local terms, and the harmonic response in one contraction. Do not
replace it by separate `||E_terminal||` and `||Z||^2/h` charges unless needed as
a fallback.

Required first production artifact:

1. exact/directed basis of the actual `W_lambda`;
2. complete finite Suzuki prime-power manifest and archimedean/local blocks;
3. finite form-core trial solve `X_lambda`;
4. coercive residual Gram;
5. directed LDL certificates for `D_lambda-mG_W`;
6. independent zero-side replay only as a normalization check.

The exact remaining obstruction is the negative part of this one finite matrix.
