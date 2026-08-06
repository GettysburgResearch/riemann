# Integration handoff — Issue #221

## Add as proposed

```text
L-22101  exact prime-ramp wavelet identity
L-22102  finite signed cubic Type-II cell decomposition
R-22101  absolute semiprime majorants are exponentially large
R-22102  resolution/diagonalization uncertainty barrier
M-22101  signed balanced-semiprime dispersion programme
O-22101  critical local Dirichlet-Hardy embedding connection
X-22101  exact formal-shift/scaling checker
```

## Relationship to PR #216

These files do not replace `T-21502/L-21504`. They attack their final open
estimate and preserve the same status boundary.

The new preferred arithmetic interface is

```text
Q_H^P = Delta_1^3 (I-2T_log4) F(.-1)
```

with `F` the weighted prime ramp, together with the finite signed cubic cell
expansion of each unit energy block.

## Do not use

- independent absolute cell bounds;
- a row-sum absolute norm;
- a shrinking window intended to isolate primes;
- a finite positive block ladder;
- the long-double data as a theorem.

`R-22101/R-22102` prove that the first three shortcuts lose the required
exponent.

## Remaining theorem

Produce one source-bound signed dispersion inequality for the complete cell
vector, either

```text
B_H(j) <= poly(j)+epsilon_j max_(k<j) B_H(k),
epsilon_j -> 0,
```

or directly

```text
[O_H^P(j)]_+ <= exp(epsilon*j)
```

for every epsilon and all sufficiently large `j`.

Subject to independent verification of `T-21502`, this is the last arithmetic
arrow to RH.

## Merge and review

- Stack this work on PR #216 or review it as a child PR.
- Keep every new claim `PROPOSED` until independently reconstructed.
- Do not merge the no-go statements as if they verified the open Type-II sign.
