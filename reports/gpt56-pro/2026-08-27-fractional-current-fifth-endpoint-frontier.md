# Fractional-current fifth-endpoint 90% frontier

## Result

The direct Conrey reconstruction gives trusted low-order baselines but does not
have the quantitative shape required for 90%. The live fifth-endpoint
programme starts at the unconditional `R_5/N>0.997` row and has already paid
`0.075 N` of its `0.097 N` loss budget.

This pass reconstructs the complete fifth-current source under the strong
log-concavity of the Xi Fourier kernel. The source is not the base Maxwell
law: it is a positive mixture of generalized-Maxwell orders 1, 2 and 3. Its
metric nevertheless satisfies the uniform exact sandwich

\[
e^{-H\xi-7H^2/(3\kappa_0)}\le r_{5,H}(\xi)\le e^{-H\xi}.
\]

A fractional Calderón identity then recovers the unweighted shallow canonical
defect from a continuum of actual current scales. This eliminates the
fixed-scale degree firewall, finite source coverage, and frame conditioning.

At `a=1/1000`, `H_0=1/20`, the complete metric/tail conversion costs less than
`0.000701 N` when the denominator degree is bounded by `2N`. Therefore a
literal current-weighted scale-wise primal residual below `0.021 N` implies a
shallow canonical charge below `0.021701 N`. Together with the deep charge,
the total is below `0.096701 N`, leaving the exact margin `0.000299 N`.

## Status

```text
generalized fifth-current source profile    PROVED EXACT
fractional Calderón identity                PROVED EXACT
scale-wise primal transport                 PROVED EXACT
strict rational 90% ledger                  PROVED EXACT
FRACTRANS104630                             OPEN
more than 90%                               UNPROVED
RH                                          UNPROVED
```

The next attack should construct the scale-dependent transports directly from
the carrier-free packets `R_0,C_0,R_5,C_5`, retaining the two denominator
channels separately rather than collapsing them into one scalar phase.
