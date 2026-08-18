# Research reset — fractional Julia–Tao–Hermite RH candidate

## Executive summary

This pass discarded the requirement to preserve any prior proof architecture.
The strongest surviving exact ingredients were:

- the reciprocal-Julia positive two-channel arithmetic;
- the Tao semigroup Schur completion;
- the positive `5:3` Stieltjes source;
- the exact four-profile quotient recurrences;
- the fact that pointwise ports, trace-bearing consumers, fixed Bellman
  apertures, finite Q4 filters, and shallow parity depths do not close RH.

The new candidate introduces a tunable fractional power `B_diamond^theta` and
places its generalized-prime histories in one source-labelled symmetric Fock
space.  The reciprocal-Julia sign is parity, the Mellin carrier is the log
number operator, and the First-Hermite heat window is a contraction of that
operator.  The atomwise Tao completion supplies the common Schur diagonal
before Stieltjes integration.

The key proposed estimate has heat-energy exponent proportional to `theta`.
An off-line zero has exponent `(beta-1/2)^2`, independent of `theta`; choosing
`theta` sufficiently small creates the contradiction.

## Why this is not another renamed factor-67 gate

The candidate does not assume GPC67, CPBD, SACF, C4MBI67, CSCBI, ZMCSCBI67,
RJTE, a Bellman barrier, or a prime-carrier large-sieve estimate.  It constructs
one new cross-scale object and attempts to prove its energy bound directly by
finite Fock exhaustion.

## Strongest exact advances

1. Fractional reciprocal-Julia powers admit positive even/odd chaos channels.
2. The native defect factors as `1-B=2S(Q-S)`.
3. All higher generalized-prime chaos is zero-free and absolutely convergent in
   `Re s>1/2`; the first prime carrier contains all RH sensitivity.
4. The Tao completion has an explicit atomwise source Gram.
5. A branch pole of `B^theta` creates a localized Hermite heat packet with
   rate `exp((beta-1/2)^2T)`.

## Load-bearing new proof

`L-98703` supplies the fractional Fock heat-energy estimate.  It uses:

- normalized even/odd coherent chaoses;
- the reflected Gaussian carrier kernel;
- the common atomwise Tao Gram;
- positive Stieltjes integration;
- Weyl removal of the real pole mode;
- a finite-cutoff direct limit.

This is the exact place where independent reconstruction should concentrate.
The repository's known no-go fixtures are included as required negative
controls.

## Scientific status

```text
complete written proof candidate             yes
new unconditional theorem accepted           no
independent hostile reconstruction            pending
Riemann Hypothesis                            unproved
```
