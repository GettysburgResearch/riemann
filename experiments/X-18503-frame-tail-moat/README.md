# X-18503 — Exact frame–tail moat replay

This experiment verifies the scalar algebra in `L-18508` and the scope
correction in `R-18502` using only Python integers and `fractions.Fraction`.

## Passing control

The exact inputs are

```text
frame floor sigma       1
omitted-zero budget B   1/10
radical endpoint eps    1/50
```

They satisfy

```text
B+2 eps = 7/50 < 1 = sigma.
```

The canonical Gaussian-schedule choice is

```text
beta      = eps+(sigma-B)/2 = 47/100
threshold = B+beta           = 57/100
```

and the counted visible margin is

```text
beta-eps = 9/20.
```

The direct frame restriction is stronger:

```text
sigma-B = 9/10.
```

## Direct-floor-only control

The second exact input is

```text
sigma = 1/4,
B     = 0,
eps   = 1/2.
```

The requested interval is empty because `eps>sigma`, but the direct visible
floor remains strictly positive:

```text
sigma-B=1/4.
```

This is the finite scope counterexample recorded in `R-18502`.

## Verification classes

The verifier returns one of

```text
CERTIFIED_GAUSSIAN_FRAME_TAIL_MOAT
CERTIFIED_DIRECT_VISIBLE_FLOOR_ONLY
NO_POSITIVE_DIRECT_VISIBLE_FLOOR
REJECTED
```

and checks typed rational inputs, nonnegative budgets, every strict scalar gate,
the explicit beta, the threshold, and the expected classification.

## Local validation

```text
python3 -m unittest discover -s tests
.........
Ran 9 tests
OK
```

Retained proof-object digests:

```text
passing moat
96e745f12aeebe4ded65ed36f40fd94c2b66eb7130906461b234529bac4b8d2f

direct-floor-only scope control
a46f04d677441d7a22f8194cd199d0e2e0d9522fc76229353abaed4eba6916ee
```

These are exact synthetic regressions. They do not contain a production Suzuki,
zeta-zero, or harmonic-packet value.
