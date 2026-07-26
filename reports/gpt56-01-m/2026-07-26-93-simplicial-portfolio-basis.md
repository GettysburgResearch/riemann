# Report — exact simplicial basis for direct-xi portfolios

Agent: `gpt56-01-m`  
Issue: #93  
Date: 2026-07-26

## Breakthrough

For fixed nodes, the L-9308 map from zero-sum logarithmic portfolio coefficients
to the negative-derivative response polynomial is a linear isomorphism. The
monomial-positive response cone is therefore exactly the image of the standard
nonnegative coefficient orthant.

The complete extreme-ray set is finite:

```text
P(y)=1,y,...,y^(n-2).
```

Hence `n-1` exact basis rows decide the entire normalized cone and every
monomial-positive subset portfolio. The earlier numerical LP and subset search
are unnecessary for proof completeness.

## Exact controls

- one synthetic table has a negative degree-zero basis row and is detected;
- one synthetic table has every basis row equal to `1/2`, certifying the entire
  cone nonnegative;
- seven adversarial tests pass.

## Production consequence

The committed PR #103 atomized 512-bit table can now receive an exact all-cone
verdict by evaluating only its basis rows. A negative upper endpoint is already
a finite witness; positive lower endpoints for all rows close the whole
monomial-positive L-9308 cone at that table.

## Counterexample status

No Riemann-xi negative interval is included. No candidate ID is allocated.
