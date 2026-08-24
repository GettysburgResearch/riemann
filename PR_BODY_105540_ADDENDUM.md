## Checkpoint I — unimodular bank realization (T-105540)

The T-105530 bank has an exact polynomial Bezout completion.  With

```text
w0=I-X/2-X^2/4,  w1=X/2,  b=I+X/2,
```

```text
U(X) = [[w0,-b],[w1,I]],
U(X)^(-1) = [[I,b],[-w1,w0]].
```

Thus `det U=1` in the scalar case and the displayed inverse is exact for every
operator `X`.  The map `f -> (w0 f,w1 f)` has the holomorphic left inverse
`(g0,g1) -> g0+b g1`.  There is no bank-induced common zero, dimension loss,
or strip partial index.

Together with the pinned functional-equation folding, reciprocal-tail, and
coefficient-freezing estimates, this proves the horizontal realization gate
`BANKREAL105530` on the strict one-sided frame.  Since `X=O(1/log T)`, the
bank anchor is `I+O(log(T)^-3)`.

The two-gate T-105530 conjunction collapses to one gate:

```text
MATRIXLERC105541 -> N0(T,2T)/N(T,2T) > 0.9.
```

`MATRIXLERC105541`, 90%, the public record, and RH remain open.
