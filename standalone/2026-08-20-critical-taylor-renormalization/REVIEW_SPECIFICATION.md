# Hostile review specification for T-99930

Reject the packet if any of the following fails.

## Native source

- The two labelled `67` vertices project to `(1,-2,1)`.
- Every other prime projects to `(1,-1)`.
- No contracted `r^2` child is substituted for a native `r` coefficient.

## Supercritical positivity

- Removing an active label `q` has ratio strictly below
  `q^(-(m+1)/2)`.
- The complete labelled exponent-`3/2` mass, including the second `67`, is
  strictly below one.
- Every infinite-looking sum is finite at fixed endpoint or absolutely
  convergent at its stated scope.

## Taylor ladder

- The integral remainder identity holds for `z>1` as well as `z<=1`.
- The scaling inequality has the correct direction.
- Positivity is claimed only while the effective prime exponent exceeds one.
- The `k=m-1` critical remainder is not silently included in the convergent
  pairing theorem.

## Mellin consumer

- The full multiplicative transform and the compact `(0,1)` correction are both
  present.
- Residues at every `s=j/2`, `j>=2`, cancel exactly.
- The `s=1/2` cancellation uses the reciprocal-zeta zero at one.
- The kernel multiplier has no zeros at translated off-line zeta zeros.
- The numerator `1-67^(-rho)` is checked at the complex zero, not only on the
  real axis.

## Scientific status

The replay and theorem ledger must keep these false:

```text
critical_envelope_sign
critical_negative_mass_bound
rh_established
```

A finite endpoint scan or positivity of `G_m`, `m>=2`, is not a proof of the
critical envelope.