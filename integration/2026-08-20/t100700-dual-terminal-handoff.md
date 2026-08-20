# T100700 successor handoff

Frozen base:

```text
PR #691
c85123d6c25b5b2ade89ab30a736f9b18844a489
```

## First review order

1. `L-100700`: reconstruct the two nested applications of scalar convexity.
2. `L-100701`: verify the Cauchy characteristic-function calculation.
3. `L-100702`: check that completion touches only interior labels and that
   divisor renewal is invoked only after the sign is exposed.
4. `L-100703`: check root removal and the direct-sum moment observation.
5. `L-100704`: verify exact short/long source partition and negative-part
   gluing.

## Two successor attacks

### SCME100704

Use the compact three-band formulas, centered logarithmic moments and
least/greatest-owner phase factors. The target is an L2 estimate only on
`p_j/p_i<=8` plus diagonal blocks.

### LRNM100704

Use interior finite squaring, explicit divisor signs and positive renewal. The
target is a one-sided L1 estimate only on `p_j/p_i>8`.

Do not broaden either theorem back into a global owner-Carleson criterion.

```text
SCME100704 open
LRNM100704 open
RH unproved
```
