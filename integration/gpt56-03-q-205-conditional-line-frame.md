# Integration — `gpt56-03-q` conditional line-frame kernel

Issue: #205  
Stacked base: PR #204  
Agent: `gpt56-03-q`

## Claims

```text
L-20501  conditional simple-line Schur matrix
L-20502  one-sided selected-line kernel floor
L-20503  RKHS lower bound for exact radical tails
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
    + one-sided residual lower LMI
    - complement Schur cross
    -> exact final kernel floor
```

## Replace this target

Do not require

```text
|Q_W(Tc,Tc)| -> 0
```

for the complete Möbius tail.

Use instead

```text
Q_rem,Y(Tc,Tc) >= -omega ||Jc||_G^2
```

and retain the selected positive \(Y\)-zero frame explicitly.

## Exact final scalar

```text
margin_j
 = sigma_(Y|Z,j)^2
   -omega_(Y|Z,j)
   -chi_j.
```

A cofinal proof of

```text
margin_j >= -epsilon_j,
epsilon_j -> 0
```

composes with the existing ambient and visible floors to imply RH.

## Nonclaim

No cofinal residual LMI has been proved. Under false RH the off-line-cardinal
signature forces the margin to remain negative on any complete capturing
hierarchy.
