# Agent report — direct completed-xi modulus witnesses

Agent: `gpt56-01-g`  
Issue: #75  
Branch: `agent/gpt56-01-g/75-xi-modulus-witness`  
Date: 2026-07-25

## Starting observation

The existing proof-grade value-only `xi'/xi` feature table was closed by an
exact feasible anchor on PR #67. Optimizing additional linear or PSD portfolios
over those unchanged primitive boxes therefore cannot produce a robust negative
witness. A new route must enlarge or move the primitive feature space.

## New primitive object

For fixed real `T`, define

```text
H_T(x^2) = |xi(1/2+x+iT)|^2.
```

Equivalently, `H_T(u)` is the entire descent of

```text
xi(1/2+z+iT) xi(1/2-z+iT)
```

through `u=z^2`.

Under RH, every zero of `H_T` is `-(T-gamma)^2<=0`, and `H_T` has order at most
one half. Its genus-zero product therefore has only positive linear factors on
`u>=0`. This yields two finite hierarchies:

1. `H_T` is absolutely monotone, so every divided difference is nonnegative;
2. `log H_T` has completely monotone derivative, giving alternating logarithmic
   divided differences and integer-power log-concavity rows.

The first-order witness is especially compact:

```text
|xi(1/2+x_2+iT)|^2 < |xi(1/2+x_1+iT)|^2,
0 <= x_1 < x_2.
```

It uses no division by `xi` and no denominator-zero exclusion.

## Completeness

If RH fails at `rho=1/2+delta+i gamma`, then `H_gamma(delta^2)=0`. Immediately
to the left of that positive zero, `H_gamma` decreases toward zero. Strictness
and continuity produce an open family of dyadic two-point witnesses.

Thus the two-point modulus test is existentially complete. The higher shape
rows are detection aids, not substitutes for the complete first-order witness.

## Exact checker

X-7501 adds a standard-library checker consuming exact rational complex
rectangles. It reconstructs:

- squared-modulus intervals with correct zero-crossing rules;
- two-point monotonicity;
- arbitrary divided differences in `u=x^2`;
- integer-power log-concavity rows with exact exponents;
- point, row, and normalization identities.

It evaluates no special function or floating point.

## Synthetic controls

The exact synthetic suite contains:

- an on-line positive-factor table passing first and second divided differences;
- an off-line dip with exact monotonicity value `-95/256`;
- a separate forbidden multiplicative-shape row equal to `-1023`.

Seven tests pass. During development, Python 3.13 exposed a dynamic-import
`dataclass` registration issue in the test harness; it was fixed by explicitly
registering the loaded module in `sys.modules`. No checker or mathematical
formula changed.

## Directed producer

The new Python-FLINT/Arb producer evaluates the standard completed product
without dividing by `xi`. It also evaluates `xi(1-s)` and requires functional-
equation rectangle overlap. Every Arb endpoint is serialized as an exact
rational.

The first finite production grid uses the exact dyadic ordinate

```text
20225875608343121406355 / 2^32
```

near the optimized high-carrier basin, with nine horizontal offsets from
`2^-20` through `2^-5`. It declares 22 monotonicity, second-difference, and
multiplicative shape rows. The workflow runs 192 and 256 bits and requires exact
coordinatewise nesting.

## Candidate status

No Riemann-xi negative interval has been computed yet. No `Z-####` candidate is
allocated. Synthetic negatives are checker controls only.

## Main uncertainties

1. Independent review should verify the order-halving and multiplicity descent
   in L-7501's genus-zero product.
2. The generic Python-FLINT zeta path may be slower than the C Riemann--Siegel
   backend at height `4.7e12`; the workflow result will decide whether a C direct-
   xi producer is required.
3. A common positive height normalization would improve conditioning but must be
   exactly independent of horizontal offset.
4. A nonnegative first grid says nothing beyond its declared nodes.

## Suggested next actions

1. Execute the two-precision high-carrier workflow.
2. If generic Arb is too slow, modify PR #56's rigorous C Riemann--Siegel
   primitive to emit direct completed-xi rectangles instead of only `xi'/xi`.
3. Adaptively insert horizontal nodes at the smallest exact moats.
4. Move to distinct exact ordinate windows after closing one local block.
5. Independently review L-7501 before candidate promotion.
