# T-104100: root-return plus root-free packing closes the fixed detector

Claim ID: `T-104100`  
Status: **PROVED CONDITIONAL IMPLICATION; TERMINAL INPUTS OPEN; RH UNPROVED**  
Created: 2026-08-21  
Base: PR #704, `66f755df4321a03874e0da3f61b033300173e364`

Let `G` be the fixed zero-safe conclusion-facing detector inherited from PR
#697 and retained by PR #704.  The inherited Mellin--Landau consumer states
that

```text
integral_1^Y G(X)_- dX/X = Y^o(1)
```

implies the Riemann Hypothesis.

For the dyadic block `B_L=[2^L,2^(L+1)]`, suppose there is an exact
root-containing positive square

```text
Q_L(X)=|G(X)|^2+E_L(X),    E_L(X)>=0.
```

Assume the following two arithmetic statements.

## SORR104100: strict source-owned root return

There are `0<=theta_L<1` and source-prescribed `R_L(X)>=0` such that

```text
|G(X)|^2 <= theta_L Q_L(X)+R_L(X)
```

on `B_L`, with

```text
(1-theta_L)^(-1)=2^o(L).
```

The source prescription must be fixed before the pointwise sign of `G` is
observed; otherwise this condition can be circular.

## RFCP104100: root-free cross-core packing

The quantities `E_L` and `R_L` are root-free after the displayed algebraic
separation and satisfy

```text
integral_(B_L)
  [sqrt(E_L(X))+sqrt(R_L(X))] dX/X
=2^o(L).
```

## Conclusion

By `L-104101`,

```text
integral_(B_L) G(X)_- dX/X=2^o(L).
```

Dyadic summation gives the inherited global subpower negative-mass condition,
and hence RH.

Therefore

```text
SORR104100 + RFCP104100 -> RH.
```

## Relation to PRs #697 and #704

This theorem is the scalar Schur-complement quotient of PR #697's nonnegative
Perron matrix.  PR #704's matched-transfer identity may be used before this
quotient to preserve a common carrier and manufacture a legitimate remainder.
The present theorem does not supersede either packet and does not prove the two
arithmetic hypotheses.

## Boundary

```text
root/excess absorption                    proved exact
fixed-detector interface                  inherited exact
SORR104100                                open / RH-bearing
RFCP104100                                open / RH-bearing
Riemann Hypothesis                        unproved
```
