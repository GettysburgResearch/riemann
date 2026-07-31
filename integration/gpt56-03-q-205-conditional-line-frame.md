# Integration — `gpt56-03-q` conditional line-frame kernel

Issue: #205  
Stacked base: PR #204  
Agent: `gpt56-03-q`

## Claims

```text
L-20501  conditional simple-line Schur matrix
L-20502  separated one-sided kernel-floor adapter
L-20503  RKHS lower bound for exact radical tails
L-20504  joint corrected-residual moat
T-20501  cofinal conditional-frame criterion
R-20501  absolute Möbius-tail smallness is overstrong
M-20501  production protocol
X-20501  exact rational replay
```

## Composition

```text
PR #192:
    finite canonical augmentation closes the infinite complement

PR #191:
    finite simple-line frames exist on every finite complement

PR #204:
    every complete-kernel vector has an explicit exact global-radical extension

this branch:
    first frame -> graph kernel
    second frame -> conditional Schur matrix
    selected positive line mass
    + joint [signed residual - full positive-sector Schur correction]
    -> exact final kernel floor
    + triangular metric adapter
    -> production lower envelope
```

## Replace these targets

Do not require

```text
|Q_W(Tc,Tc)| -> 0
```

for the complete Möbius tail.

Do not begin by charging residual and Schur cross separately when they are
available in one basis.

Use the joint corrected residual

```text
R_corr,Y
 = Q_rem,Y|K-L_K* C_+^-1 L_K
```

and certify

```text
R_corr,Y >= -nu G_K.
```

Retain the selected positive \(Y\)-zero frame explicitly.

The modular fallback

```text
Q_rem,Y|K >= -omega G_K,
L_K* C_+^-1 L_K <= chi G_K
```

gives `nu<=omega+chi` but may lose strict positivity.

## Exact final scalar

```text
margin_j
 = sigma_(Y|Z,j)^2-nu_(Y|Z,j).
```

Let `Lambda_j` be the inflation of the exact triangular square-completion metric
relative to the production metric, and `delta_j` the assembly radius. A cofinal
proof of

```text
Lambda_j * (-margin_j)_+ + delta_j -> 0
```

composes with the canonical complement and `T-14302` to imply RH.

## Nonclaim

No cofinal joint residual LMI has been proved. Under false RH the off-line-cardinal
signature forces the margin to remain negative on any complete capturing
hierarchy.
