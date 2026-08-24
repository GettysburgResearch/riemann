# Ninety-percent Wick–Pick continuation report

Date: 2026-08-24  
Branch: `research/gpt56-pro/105200-xi-summable-residue-coherence`  
PR: `#726`

## Main advance

The old T-105310 multiplicity-robust inequality has a structural ceiling of
`0.8358`, even at perfect effective rank.  The new `L-105500` finite theorem
uses the complete confluent Hermite signature and reciprocal Cauchy index,
removing the `821/5000` subtraction and the separate common-zero charge:

\[
\liminf N_0/N\ge2\liminf\eta_T-1.
\]

The source-owned `K=2` Wick factor cancels Euler degrees one and two.  Its
one-sided normalized coefficient energy is rigorously below `1/1000`, so the
frozen model has effective rank above `500/501`.  Under an explicit 99/101
actual-Xi trace/HS transfer, the resulting conditional proportion is

\[
1563433/1703567=0.917740834\ldots.
\]

## Independent checks

The replay uses exact rational arithmetic.  It checks the Wick recurrence,
energy fractions, final proportion, and a confluent-signature regression
against exact Sturm distinct-root counts on structured repeated-root/nonreal
families and seeded random polynomials.

## Boundary

`W2XFER105500` remains open.  In particular, the degree-two exponential Wick
factor has a stronger horizontal-boundary cost than the degree-one factor.
No ninety-percent result for zeta and no proof of RH is claimed.
