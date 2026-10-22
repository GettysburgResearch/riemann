# Five-adic renewal second pass

The first PR #322 formulation is retained, but the review standard is strengthened.

## Surviving mechanism

The correct object is not atomic boundary debt. The correct object is the signed residue-renewal state under exact five-adic splitting.

For X=5Y,

w_X(5q)=5^{-1/2}w_Y(q)

induces a lower-scale critical component plus finite residue commutators.

## Important correction

The remaining finite residue automaton is not cosmetic. It is the actual RH-bearing theorem. Any proof must emit the finite transition matrix and certify contraction; no generic endpoint-count argument is accepted.

## New attack target

Construct the five-state residue operator K on the quotient by the critical scaling mode. Prove

rho(K)<1.

Then the recurrence

D_X <= rho D_{X/5}+polylog(X)

closes by iteration.

## Fail conditions

Reject if:

1. residue classes regenerate current-scale debt;
2. the critical mode has multiplicity greater than one;
3. contraction only holds after taking absolute values;
4. the transition matrix depends on X without a limiting compact operator.

The next step is exact symbolic construction of K, not another scalar debt bound.
