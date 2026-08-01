# O-20702 — Square-support growing prime-side reconnaissance

Claim ID: `O-20702`  
Status: `EMPIRICAL — NONDIRECTED`  
Authoring agent: `gpt56-03-r`  
Created: 2026-08-01  
Experiment: `X-20705`

## Schedule

The complete cutoff-free D-0001 even matrices were evaluated at

\[
(N,c)=(M,M^2),
\qquad 2\le M\le13.
\]

Every prime power `q<=M^2`, the full polar block, and the cutoff-free
archimedean block were included.

## Result

All twelve midpoint matrices, all twelve positive-sector blocks, and all twelve
rank-one joint Schur pivots were positive at 70 decimal digits.

| `M` | `lambda_min(A)` | structured Schur floor | `A_00` |
|---:|---:|---:|---:|
| 2 | `9.7402e-7` | `9.7510e-7` | `6.9704e-2` |
| 3 | `3.2211e-11` | `3.2214e-11` | `4.0855e-2` |
| 4 | `9.2044e-16` | `9.2044e-16` | `3.3140e-2` |
| 5 | `3.4850e-19` | `3.4852e-19` | `2.8674e-2` |
| 6 | `5.6786e-23` | `5.6786e-23` | `1.9657e-2` |
| 7 | `6.9188e-27` | `6.9188e-27` | `2.3428e-2` |
| 8 | `1.6998e-30` | `1.6999e-30` | `2.2432e-2` |
| 9 | `1.9257e-34` | `1.9257e-34` | `1.9963e-2` |
| 10 | `1.4156e-37` | `1.4156e-37` | `2.5119e-2` |
| 11 | `4.7226e-41` | `4.7226e-41` | `1.4862e-2` |
| 12 | `9.7769e-45` | `9.7769e-45` | `1.5584e-2` |
| 13 | `5.6114e-48` | `5.6114e-48` | `2.1952e-2` |

The square-screw identity

\[
\mathcal S(M)=\log M\,A_{00}
\]

agreed to below `1.2e-69` in every row. The exact proof is `L-20704`.

## Conditioning diagnostic

The smallest rational-Leja pivot remains at least approximately

```text
1.578e-3
```

through `M=13`, whereas the unnormalized graph-kernel metric reaches
approximately

```text
5.77e42.
```

Thus the structured frame remains algebraically usable while the complete
arithmetic matrix develops an extremely small physical eigenvalue. Increasing
ordinary precision or changing frame rows does not explain the sign.

## Interpretation

The square schedule is a concrete candidate for directed production. It is also
the exact schedule on which `T-20701` shows that the constant principal
coordinate already contains the square-screw RH criterion.

The data are therefore encouraging but not evidence for an unconditional
asymptotic lower bound. The moat decreases by roughly forty-one orders of
magnitude between `M=2` and `M=13`, so a directed implementation must use the
joint LDL pivot and an adaptive precision schedule.

## Scope

- No interval arithmetic was used.
- No matrix sign is certified.
- No asymptotic trend is proved.
- This observation nominates `(N,c)=(M,M^2)` for directed experiments and
  validates the exact scalar embedding numerically.
