# T99300 — Positive Mellin witness recovery

This is the remote recovery of the unpublished T99300 packet, stacked on PR #641 at exact head `19cd3939a54ccea73b055b3952b5dd7ed638c4fb`.

**Scientific status:** proposed conclusion-oriented reduction for hostile reconstruction. RH remains unproved.

## Core idea

For one fixed component row `j`, do not insist that every finite/continuum correction be positive or that every global score/capacity coordinate close exactly. It is sufficient to construct a nonnegative surrogate `D_X(j)` whose difference from the canonical Möbius row

```text
c_X(j) = sum_{n<=X/j} mu(n)/sqrt(n) Q_{X/n}(j)
```

belongs to the Mellin-holomorphic error class

```text
A_+ = { e : integral_1^infty |e(X)| X^{-sigma-1} dX < infinity for every sigma>0 }.
```

Then the fixed-row transform

```text
C_j(s) = C_j/s^2 + P_j(s+1/2)/(s^2 zeta(s+1/2))
```

retains every off-line reciprocal-zeta pole which survives `P_j`, while the error transform is holomorphic in `Re(s)>0`. Landau can therefore be applied to the nonnegative surrogate.

## New compositional move

Solve compact Hall **before endpoint integration**, pointwise in the endpoint parameter. The residual Hall source then integrates to one nested positive vector measure. All rough-prime children are literal restrictions/pushforwards of that common parent, with only the `alpha` children recursing and total child mass `<1/sqrt(67)<1/8`. The Hall row bonus is current-owned and never copied recursively.

This packet therefore replaces the strongest previous equality-frame demand by a single local interface:

```text
pointwise compact Hall + native first-owner ledger
    -> one nested positive common parent
    -> fixed-row nonnegative surrogate modulo A_+
    -> preserved reciprocal-zeta pole
    -> Landau contradiction if an off-line zero exists.
```

## Exact boundary

```text
positive-Mellin-witness transfer          proved analytically
pointwise differential Hall composition   proved conditionally on local Hall inequalities
first-owner source partition              proved abstractly
factor-67 alpha contraction               inherited exact
local compact Hall inequalities           frozen input / reconstruction target
native first-owner coefficient ledger     frozen input / reconstruction target
Riemann Hypothesis                        unproved
```
