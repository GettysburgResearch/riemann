# L-101500: matched-transfer negative-part identity

For a real number `x`, write `x_- = max(-x,0)`.

## Statement

For every `f,g,tau in R`,

```text
(f+g)_- <= (f+tau)_- + (g-tau)_-.
```

Moreover,

```text
(f+g)_- = inf_tau [(f+tau)_- + (g-tau)_-].
```

The same statement holds pointwise for measurable real-valued functions. Consequently, if for each horizon `Y` there is one measurable transfer `tau_Y(X)` such that

```text
int_1^Y (f+tau_Y)_- dX/X = Y^o(1),
int_1^Y (g-tau_Y)_- dX/X = Y^o(1),
```

then

```text
int_1^Y (f+g)_- dX/X = Y^o(1).
```

## Proof

The first inequality is the subadditivity of the negative part applied to

```text
f+g = (f+tau) + (g-tau).
```

For equality of the infimum, if `f+g>=0`, choose any `tau` in `[-f,g]`; both summands vanish. If `f+g<0`, choose `tau=-f`; the first summand vanishes and the second equals `-(f+g)`. The integral consequence follows pointwise.
