# Candidate handoff — exact positive-anchor run at `w=4`

## Target

Use the PR #103 atomized-minimum ordinate

```text
T numerator   20225875608343133989267
T denominator 4294967296
```

and add the exact horizontal point

```text
x = 2
u = x^2 = 4
s = 5/2 + i T.
```

## Required producer changes

1. Reuse the reviewed completed-xi normalization
   `riemann-xi-standard-half-s-sminus1-v1`.
2. Preserve the same common xi scale and functional-equation gates.
3. Emit only the new `x=2` point at 512 and 640 bits.
4. Require componentwise nesting and a modulus-square lower endpoint above zero.
5. Apply the exact PR #103 atomized shells without changing endpoint semantics.

## Required checker steps

1. Load `experiments/X-9306-real-log-portfolio-search/results/basis.json`.
2. Regenerate `positive_anchor.py --anchor 4` and bind its SHA-256.
3. Compute the new residual interval `F(4)` and reuse old reference `x-20`.
4. Use the exact L-9315 reduced coefficients to enclose `b0`.
5. Independently compute the direct 17-point response-1 contraction and require
   overlap with the reduced interval.
6. Contract the L-9314 lower and upper exact rational witness polynomials.
7. Return one of:

```text
CERTIFIED_NEGATIVE_LOWER_SQUARE
CERTIFIED_NEGATIVE_UPPER_Y_SQUARE
NO_CERTIFIED_NEGATIVE
UNRESOLVED
```

## Discovery target

Ordinary 70-digit reconnaissance gave

```text
b0-lower approximately 2.8574989484e-12
upper-b0 approximately 6.6524756024e-12.
```

The old moment-box contribution is below `7.071e-33`. The lower gap divided by
`|beta_w|` is about `0.01226887`, so the directed new-point precision requirement
should be mild.

## Promotion boundary

Do not allocate a `Z-####` object from a midpoint. A nomination requires a strict
negative complete quadratic interval, dual-replay overlap, exact normalization
binding, and independent completed-xi reproduction.
